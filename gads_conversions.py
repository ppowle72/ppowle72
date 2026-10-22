"""List every Google Ads conversion action with status, primary/secondary and 30-day volume.
READ-ONLY: changes nothing.

    python gads_conversions.py          # active actions (not REMOVED)
    python gads_conversions.py --all    # include REMOVED / hidden ones
Also writes conversion_actions.csv in the current folder.
Uses the same .env as gads_audiences.py.
"""
import argparse
import csv
import os
import sys

from dotenv import load_dotenv
from google.ads.googleads.client import GoogleAdsClient


def digits(v):
    return "".join(c for c in (v or "") if c.isdigit())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true", help="include REMOVED actions")
    args = ap.parse_args()
    load_dotenv()

    need = ["GOOGLE_ADS_DEVELOPER_TOKEN", "GOOGLE_ADS_CLIENT_ID", "GOOGLE_ADS_CLIENT_SECRET",
            "GOOGLE_ADS_REFRESH_TOKEN", "GOOGLE_ADS_CUSTOMER_ID"]
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
    client = GoogleAdsClient.load_from_dict(cfg)
    cid = digits(os.environ["GOOGLE_ADS_CUSTOMER_ID"])
    svc = client.get_service("GoogleAdsService")

    def run(q):
        return [r for b in svc.search_stream(customer_id=cid, query=q) for r in b.results]

    where = "" if args.all else "WHERE conversion_action.status != 'REMOVED'"
    actions = run(
        "SELECT conversion_action.id, conversion_action.name, conversion_action.status, "
        "conversion_action.type, conversion_action.category, conversion_action.origin, "
        "conversion_action.primary_for_goal, conversion_action.counting_type "
        f"FROM conversion_action {where}")

    # Metrics query only returns actions that had activity in the window
    vol = {}
    for r in run("SELECT conversion_action.id, metrics.all_conversions, metrics.all_conversions_value "
                 "FROM conversion_action WHERE segments.date DURING LAST_30_DAYS"):
        v = vol.setdefault(r.conversion_action.id, [0.0, 0.0])
        v[0] += r.metrics.all_conversions
        v[1] += r.metrics.all_conversions_value

    rows = []
    for r in actions:
        a = r.conversion_action
        n, val = vol.get(a.id, [0.0, 0.0])
        rows.append({
            "id": a.id, "name": a.name, "status": a.status.name, "type": a.type_.name,
            "category": a.category.name, "origin": a.origin.name,
            "primary": "PRIMARY" if a.primary_for_goal else "secondary",
            "counting": a.counting_type.name,
            "conv_30d": round(n, 2), "value_30d": round(val, 2),
        })
    rows.sort(key=lambda x: (x["status"] != "ENABLED", x["primary"] != "PRIMARY", -x["conv_30d"], x["name"]))

    print(f"{len(rows)} conversion actions in account {cid}\n")
    print(f"{'STATUS':<8} {'ROLE':<9} {'30d conv':>8}  {'TYPE':<22} NAME")
    for x in rows:
        print(f"{x['status']:<8} {x['primary']:<9} {x['conv_30d']:>8}  {x['type']:<22} {x['name']}")

    enabled = [x for x in rows if x["status"] == "ENABLED"]
    idle = [x for x in enabled if x["conv_30d"] == 0]
    print(f"\nEnabled: {len(enabled)} | primary: {sum(x['primary']=='PRIMARY' for x in enabled)} "
          f"| enabled with 0 conversions in 30d: {len(idle)}")
    print("Primary actions drive bidding. Review idle primary ones first; nothing was changed.")

    with open("conversion_actions.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else ["id"])
        w.writeheader()
        w.writerows(rows)
    print("Saved conversion_actions.csv")


if __name__ == "__main__":
    main()
