"""Create the GA4 audiences via the Admin API (v1alpha).

Setup (run on your PC, from the Mango SEO agent folder):
    pip install google-auth requests python-dotenv
    python ga4_audiences.py --dry-run     # prints payloads, creates nothing
    python ga4_audiences.py               # creates them

Credentials: set GOOGLE_APPLICATION_CREDENTIALS in .env to the service-account
JSON path. That service account needs Editor access on the GA4 property.
"""
import argparse
import json
import os

import google.auth.transport.requests
import requests
from dotenv import load_dotenv
from google.oauth2 import service_account

PROPERTY_ID = os.environ.get("GA4_PROPERTY_ID", "294116937")
API = f"https://analyticsadmin.googleapis.com/v1alpha/properties/{PROPERTY_ID}/audiences"
SCOPE = "https://www.googleapis.com/auth/analytics.edit"
ALL_SESSIONS = "AUDIENCE_FILTER_SCOPE_ACROSS_ALL_SESSIONS"


def event(name):
    return {"eventFilter": {"eventName": name}}


def clause(kind, expr):
    return {
        "clauseType": kind,
        "simpleFilter": {"scope": ALL_SESSIONS, "filterExpression": expr},
    }


def audience(name, desc, days, clauses):
    return {
        "displayName": name,
        "description": desc,
        "membershipDurationDays": days,
        "filterClauses": clauses,
    }


def build():
    return [
        audience("Basket abandoners 90d", "add_to_cart without purchase", 90, [
            clause("INCLUDE", event("add_to_cart")),
            clause("EXCLUDE", event("purchase")),
        ]),
        audience("Checkout starters 90d", "begin_checkout without purchase", 90, [
            clause("INCLUDE", event("begin_checkout")),
            clause("EXCLUDE", event("purchase")),
        ]),
        audience("Item viewers 90d", "view_item", 90, [
            clause("INCLUDE", event("view_item")),
        ]),
        audience("Non-purchasers 90d", "Any session event, never purchased", 90, [
            clause("INCLUDE", event("session_start")),
            clause("EXCLUDE", event("purchase")),
        ]),
        audience("Overseas visitors", "Country is not India", 540, [
            clause("INCLUDE", {"notExpression": {"dimensionOrMetricFilter": {
                "fieldName": "country",
                "stringFilter": {"matchType": "EXACT", "value": "India"},
            }}}),
        ]),
        audience("Fresh mango viewers", "view_item for Alphonso/Hapus/Ratnagiri", 540, [
            clause("INCLUDE", {"andGroup": {"filterExpressions": [
                event("view_item"),
                {"orGroup": {"filterExpressions": [
                    {"dimensionOrMetricFilter": {
                        "fieldName": "itemName",
                        "stringFilter": {"matchType": "CONTAINS", "value": v},
                    }} for v in ("Alphonso", "Hapus", "Ratnagiri")
                ]}},
            ]}}),
        ]),
    ]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    load_dotenv()

    audiences = build()
    if args.dry_run:
        print(json.dumps(audiences, indent=2))
        return

    creds = service_account.Credentials.from_service_account_file(
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"], scopes=[SCOPE])
    creds.refresh(google.auth.transport.requests.Request())
    headers = {"Authorization": f"Bearer {creds.token}"}

    for body in audiences:
        r = requests.post(API, headers=headers, json=body, timeout=30)
        status = "OK  " if r.ok else "FAIL"
        print(status, body["displayName"], "" if r.ok else r.text)


if __name__ == "__main__":
    main()
