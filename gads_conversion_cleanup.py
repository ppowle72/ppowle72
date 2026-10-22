"""Clean up Google Ads conversion actions. PREVIEW by default; changes nothing without --apply.

    python gads_conversion_cleanup.py            # shows the plan
    python gads_conversion_cleanup.py --apply    # executes it

Plan:
  1. Primary (used for bidding): "Google Shopping App Purchase"
  2. Secondary (reported only): calls, local actions, YouTube, AdPulse import
  3. Remove: dead Universal Analytics goals and the festivetreat.com purchase
Google-hosted actions (calls/local/YouTube) may refuse API edits; those are listed so you can
switch them in Google Ads > Goals > Conversions > Summary instead.
Uses the same .env as the other gads_*.py scripts.
"""
import argparse
import os
import sys

from dotenv import load_dotenv
from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException

TO_PRIMARY = ["Google Shopping App Purchase"]
TO_SECONDARY = [
    "Clicks to call", "Local actions - Directions", "Local actions - Other engagements",
    "Local actions - Website visits", "YouTube channel subscriptions", "YouTube follow-on views",
    "Shopify paid orders (AdPulse import)",
]
REMOVE_TYPES = {"UNIVERSAL_ANALYTICS_GOAL"}
REMOVE_NAME_CONTAINS = ["festivetreat.com"]


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
    csvc = client.get_service("ConversionActionService")

    rows = [r.conversion_action for b in gsvc.search_stream(
        customer_id=cid,
        query="SELECT conversion_action.resource_name, conversion_action.name, conversion_action.type, "
              "conversion_action.status, conversion_action.primary_for_goal "
              "FROM conversion_action WHERE conversion_action.status != 'REMOVED'")
        for r in b.results]

    plan = []  # (kind, action)
    for a in rows:
        t = a.type_.name
        if a.name in TO_PRIMARY and not a.primary_for_goal:
            plan.append(("MAKE PRIMARY", a))
        elif a.name in TO_SECONDARY and a.primary_for_goal:
            plan.append(("MAKE SECONDARY", a))
        elif t in REMOVE_TYPES or any(s in a.name for s in REMOVE_NAME_CONTAINS):
            plan.append(("REMOVE", a))

    found = {a.name for a in rows}
    for n in TO_PRIMARY + TO_SECONDARY:
        if n not in found:
            print(f"(note) '{n}' not found in this account")

    print(f"{'PREVIEW' if not args.apply else 'APPLYING'}: {len(plan)} changes\n")
    for kind, a in plan:
        print(f"  {kind:<15} {a.name}  [{a.type_.name}]")
    if not args.apply:
        print("\nNothing changed. Re-run with --apply to execute.")
        return

    ok = bad = 0
    for kind, a in plan:
        op = client.get_type("ConversionActionOperation")
        if kind == "REMOVE":
            op.remove = a.resource_name
        else:
            op.update.resource_name = a.resource_name
            op.update.primary_for_goal = (kind == "MAKE PRIMARY")
            op.update_mask.paths.append("primary_for_goal")
        try:
            csvc.mutate_conversion_actions(customer_id=cid, operations=[op])
            ok += 1
            print(f"  OK   {kind}: {a.name}")
        except GoogleAdsException as e:
            bad += 1
            msg = e.failure.errors[0].message if e.failure.errors else str(e)
            print(f"  FAIL {kind}: {a.name} -> {msg[:110]}  (do this one in the Google Ads UI)")
    print(f"\nDone: {ok} changed, {bad} need the UI.")


if __name__ == "__main__":
    main()
