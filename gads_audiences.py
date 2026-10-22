"""Attach the GA4 audiences to Google Ads Search campaigns as Observation.

Run on your PC from the Mango SEO agent folder (needs: pip install google-ads python-dotenv).

    python gads_audiences.py            # LIST ONLY: shows audience lists + campaigns, changes nothing
    python gads_audiences.py --apply    # attach lists to ENABLED Search campaigns (observation)
    python gads_audiences.py --apply --exclude-purchasers "Campaign name"
                                        # also exclude Purchasers lists from the named campaign(s)

.env variables (standard Google Ads names):
    GOOGLE_ADS_DEVELOPER_TOKEN, GOOGLE_ADS_CLIENT_ID, GOOGLE_ADS_CLIENT_SECRET,
    GOOGLE_ADS_REFRESH_TOKEN, GOOGLE_ADS_CUSTOMER_ID (digits only),
    GOOGLE_ADS_LOGIN_CUSTOMER_ID (optional; manager account id)

Audiences only appear in Google Ads 24-48h after the GA4 <-> Google Ads link is on.
Demand Gen targeting is not scripted here; add those lists in the UI.
"""
import argparse
import os
import sys

from dotenv import load_dotenv
from google.ads.googleads.client import GoogleAdsClient
from google.api_core import protobuf_helpers

WANTED = [
    "Basket abandoners 90d", "Checkout starters 90d", "Item viewers 90d",
    "Non-purchasers 90d", "Past purchasers 540d", "Overseas visitors",
    "Fresh mango viewers", "Disengaged purchasers", "High-value purchasers",
]


def digits(v):
    return "".join(c for c in (v or "") if c.isdigit())


def make_client():
    need = ["GOOGLE_ADS_DEVELOPER_TOKEN", "GOOGLE_ADS_CLIENT_ID",
            "GOOGLE_ADS_CLIENT_SECRET", "GOOGLE_ADS_REFRESH_TOKEN", "GOOGLE_ADS_CUSTOMER_ID"]
    missing = [k for k in need if not os.environ.get(k)]
    if missing:
        sys.exit("Missing in .env: " + ", ".join(missing))
    cfg = {
        "developer_token": os.environ["GOOGLE_ADS_DEVELOPER_TOKEN"],
        "client_id": os.environ["GOOGLE_ADS_CLIENT_ID"],
        "client_secret": os.environ["GOOGLE_ADS_CLIENT_SECRET"],
        "refresh_token": os.environ["GOOGLE_ADS_REFRESH_TOKEN"],
        "use_proto_plus": True,
    }
    login = digits(os.environ.get("GOOGLE_ADS_LOGIN_CUSTOMER_ID"))
    if login:
        cfg["login_customer_id"] = login
    return GoogleAdsClient.load_from_dict(cfg)


def query(client, cid, gaql):
    svc = client.get_service("GoogleAdsService")
    return [row for batch in svc.search_stream(customer_id=cid, query=gaql) for row in batch.results]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--exclude-purchasers", nargs="*", default=[], metavar="CAMPAIGN")
    args = ap.parse_args()
    load_dotenv()
    client = make_client()
    cid = digits(os.environ["GOOGLE_ADS_CUSTOMER_ID"])

    lists = query(client, cid, "SELECT user_list.resource_name, user_list.name, "
                  "user_list.size_for_search, user_list.membership_status FROM user_list")
    found = {}
    print("== Audience lists in Google Ads ==")
    for r in lists:
        ul = r.user_list
        hit = next((w for w in WANTED + ["Purchasers"] if w.lower() in ul.name.lower()), None)
        if hit:
            found[ul.name] = ul.resource_name
            print(f"  {ul.name} | search size {ul.size_for_search} | {ul.membership_status.name}")
    missing = [w for w in WANTED if not any(w.lower() in n.lower() for n in found)]
    if missing:
        print("  Not synced yet (wait 24-48h after linking GA4):", ", ".join(missing))

    camps = query(client, cid, "SELECT campaign.resource_name, campaign.name, "
                  "campaign.advertising_channel_type, campaign.status FROM campaign "
                  "WHERE campaign.status = 'ENABLED'")
    print("== Enabled campaigns ==")
    for r in camps:
        print(f"  {r.campaign.name} [{r.campaign.advertising_channel_type.name}]")

    if not args.apply:
        print("\nList only. Re-run with --apply to attach audiences.")
        return

    target_lists = [rn for n, rn in found.items()
                    if any(w.lower() in n.lower() for w in WANTED)]
    purchaser_lists = [rn for n, rn in found.items()
                       if n.lower().startswith("purchasers") or "past purchasers" in n.lower()]

    cc_svc = client.get_service("CampaignCriterionService")
    camp_svc = client.get_service("CampaignService")
    for r in camps:
        c = r.campaign
        if c.advertising_channel_type.name == "SEARCH":
            # Observation = bid_only: audiences adjust bids but never narrow reach
            upd = client.get_type("CampaignOperation")
            camp = upd.update
            camp.resource_name = c.resource_name
            tr = camp.targeting_setting.target_restrictions.add()
            tr.targeting_dimension = client.enums.TargetingDimensionEnum.AUDIENCE
            tr.bid_only = True
            client.copy_from(upd.update_mask, protobuf_helpers.field_mask(None, camp._pb))
            camp_svc.mutate_campaigns(customer_id=cid, operations=[upd])

            ops = []
            for rn in target_lists:
                op = client.get_type("CampaignCriterionOperation")
                crit = op.create
                crit.campaign = c.resource_name
                crit.user_list.user_list = rn
                ops.append(op)
            if ops:
                resp = cc_svc.mutate_campaign_criteria(customer_id=cid, operations=ops, partial_failure=True)
                print(f"Search '{c.name}': attached {len(ops)} lists (observation)")
        if c.name in args.exclude_purchasers:
            ops = []
            for rn in purchaser_lists:
                op = client.get_type("CampaignCriterionOperation")
                crit = op.create
                crit.campaign = c.resource_name
                crit.negative = True
                crit.user_list.user_list = rn
                ops.append(op)
            if ops:
                cc_svc.mutate_campaign_criteria(customer_id=cid, operations=ops, partial_failure=True)
                print(f"'{c.name}': excluded {len(ops)} purchaser lists")


if __name__ == "__main__":
    main()
