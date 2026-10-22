"""Make PURCHASE the only account-default (biddable) conversion goal.
PREVIEW by default; changes nothing without --apply.

    python gads_goals.py            # shows current goals and the planned changes
    python gads_goals.py --apply    # turns off "account default" on every goal except Purchase
Reversible: Google Ads > Goals > Summary > Edit goal > Use for account default goals.
Uses the same .env as the other gads_*.py scripts.
"""
import argparse
import os
import sys

from dotenv import load_dotenv
from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException

KEEP = {"PURCHASE"}


def digits(v):
    return "".join(c for c in (v or "") if c.isdigit())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    load_dotenv()
    need = ["GOOGLE_ADS_DEVELOPER_TOKEN", "GOOGLE_ADS_CLIENT_ID", "GOOGLE_ADS_CLIENT_SECRET",
            "GOOGLE_ADS_REFRESH_TOKEN", "GOOGLE_ADS_CUSTOMER_ID"]
    missing = [k for k in need if not os.environ.get(k)]
    if missing:
        sys.exit("Missing in .env: " + ", ".join(missing))
    cfg = {k.lower().replace("google_ads_", ""): os.environ[k] for k in need[:4]}
    cfg["use_proto_plus"] = True
    if digits(os.environ.get("GOOGLE_ADS_LOGIN_CUSTOMER_ID")):
        cfg["login_customer_id"] = digits(os.environ["GOOGLE_ADS_LOGIN_CUSTOMER_ID"])
    client = GoogleAdsClient.load_from_dict(cfg)
    cid = digits(os.environ["GOOGLE_ADS_CUSTOMER_ID"])
    gsvc = client.get_service("GoogleAdsService")
    svc = client.get_service("CustomerConversionGoalService")

    goals = [r.customer_conversion_goal for b in gsvc.search_stream(
        customer_id=cid,
        query="SELECT customer_conversion_goal.resource_name, customer_conversion_goal.category, "
              "customer_conversion_goal.origin, customer_conversion_goal.biddable "
              "FROM customer_conversion_goal") for r in b.results]

    print(f"{'ACCOUNT DEFAULT':<16} {'CATEGORY':<24} ORIGIN")
    for g in sorted(goals, key=lambda g: (not g.biddable, g.category.name)):
        print(f"{'yes' if g.biddable else 'no':<16} {g.category.name:<24} {g.origin.name}")

    plan = [g for g in goals if g.biddable and g.category.name not in KEEP]
    print(f"\n{'APPLYING' if args.apply else 'PREVIEW'}: turn OFF account default on {len(plan)} goals; keep {sorted(KEEP)}")
    for g in plan:
        print(f"  OFF  {g.category.name} / {g.origin.name}")
    if not args.apply:
        print("\nNothing changed. Re-run with --apply to execute.")
        return

    ok = bad = 0
    for g in plan:
        op = client.get_type("CustomerConversionGoalOperation")
        op.update.resource_name = g.resource_name
        op.update.biddable = False
        op.update_mask.paths.append("biddable")
        try:
            svc.mutate_customer_conversion_goals(customer_id=cid, operations=[op])
            ok += 1
            print(f"  OK   {g.category.name} / {g.origin.name}")
        except GoogleAdsException as e:
            bad += 1
            msg = e.failure.errors[0].message if e.failure.errors else str(e)
            print(f"  FAIL {g.category.name} / {g.origin.name} -> {msg[:100]}  (do in UI)")
    print(f"\nDone: {ok} changed, {bad} need the UI.")


if __name__ == "__main__":
    main()
