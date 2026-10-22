"""Create the GA4 audiences via the Admin API (v1alpha).

Setup (run on your PC, from the Mango SEO agent folder):
    pip install google-auth requests python-dotenv
    python ga4_audiences.py --dry-run     # prints payloads, creates nothing
    python ga4_audiences.py               # creates them

Credentials: uses GOOGLE_SERVICE_ACCOUNT_JSON (inline JSON) from .env if set,
otherwise GOOGLE_APPLICATION_CREDENTIALS from .env if set, otherwise the
google-service-account*.json file in the same folder. That service account needs Editor access on the GA4 property.
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


def wrap(expr):
    """GA4 needs and_group -> or_group -> leaf filter at the top level."""
    return {"andGroup": {"filterExpressions": [{"orGroup": {"filterExpressions": [expr]}}]}}


def clause(kind, expr):
    if "andGroup" not in expr:
        expr = wrap(expr)
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
        audience("Past purchasers 540d", "Anyone who purchased; seed for January pre-booking and lookalikes", 540, [
            clause("INCLUDE", event("purchase")),
        ]),
        audience("Overseas visitors", "Country is not India", 540, [
            clause("INCLUDE", {"notExpression": {"dimensionOrMetricFilter": {
                "fieldName": "country",
                "stringFilter": {"matchType": "EXACT", "value": "India"},
            }}}),
        ]),
        audience("Fresh mango viewers", "view_item for Alphonso/Hapus/Ratnagiri", 540, [
            clause("INCLUDE", {"andGroup": {"filterExpressions": [
                {"orGroup": {"filterExpressions": [event("view_item")]}},
                {"orGroup": {"filterExpressions": [
                    {"dimensionOrMetricFilter": {
                        "fieldName": "itemName",
                        "stringFilter": {"matchType": "CONTAINS", "value": v},
                    }} for v in ("Alphonso", "Hapus", "Ratnagiri")
                ]}},
            ]}}),
        ]),
    ]


def load_credentials():
    """Prefer inline GOOGLE_SERVICE_ACCOUNT_JSON from .env, else a key file."""
    raw = os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON")
    if raw:
        return service_account.Credentials.from_service_account_info(json.loads(raw), scopes=[SCOPE])
    return service_account.Credentials.from_service_account_file(find_key_file(), scopes=[SCOPE])


def find_key_file():
    """Use .env path if set, else the google-service-account*.json next to this script."""
    path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS") or os.environ.get("GOOGLE_SERVICE_ACCOUNT_FILE")
    if path and os.path.isfile(path):
        return path
    here = os.path.dirname(os.path.abspath(__file__))
    for name in sorted(os.listdir(here)):
        if name.lower().startswith("google-service-account") and name.lower().endswith(".json"):
            return os.path.join(here, name)
    raise SystemExit("No service-account JSON found. Set GOOGLE_APPLICATION_CREDENTIALS in .env.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    load_dotenv()

    audiences = build()
    if args.dry_run:
        print(json.dumps(audiences, indent=2))
        return

    creds = load_credentials()
    creds.refresh(google.auth.transport.requests.Request())
    headers = {"Authorization": f"Bearer {creds.token}"}

    for body in audiences:
        r = requests.post(API, headers=headers, json=body, timeout=30)
        status = "OK  " if r.ok else "FAIL"
        print(status, body["displayName"], "" if r.ok else r.text)


if __name__ == "__main__":
    main()
