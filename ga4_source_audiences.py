"""Create one GA4 audience per traffic source so each channel can be measured and retargeted.
PREVIEW by default; skips audiences that already exist.

    python ga4_source_audiences.py            # shows the plan
    python ga4_source_audiences.py --apply    # creates them
"""
import argparse
import json
import os

import google.auth.transport.requests
import requests
from dotenv import load_dotenv
from google.oauth2 import service_account

load_dotenv()
PROPERTY = os.environ.get("GA4_PROPERTY_ID", "294116937")
API = f"https://analyticsadmin.googleapis.com/v1alpha/properties/{PROPERTY}/audiences"
# (name, GA4 field, match, value)
SOURCES = [
    ("Visitors: Instagram 90d", "sessionSource", "CONTAINS", "instagram"),
    ("Visitors: Facebook 90d", "sessionSource", "CONTAINS", "facebook"),
    ("Visitors: LinkedIn 90d", "sessionSource", "CONTAINS", "linkedin"),
    ("Visitors: YouTube 90d", "sessionSource", "CONTAINS", "youtube"),
    ("Visitors: WhatsApp 90d", "sessionSource", "CONTAINS", "whatsapp"),
    ("Visitors: Email 90d", "sessionMedium", "EXACT", "email"),
    ("Visitors: Paid social 90d", "sessionMedium", "EXACT", "paid_social"),
]


def body(name, field, match, value):
    return {"displayName": name, "description": f"{field} {match} {value}", "membershipDurationDays": 90,
            "filterClauses": [{"clauseType": "INCLUDE", "simpleFilter": {
                "scope": "AUDIENCE_FILTER_SCOPE_ACROSS_ALL_SESSIONS",
                "filterExpression": {"andGroup": {"filterExpressions": [{"orGroup": {"filterExpressions": [
                    {"dimensionOrMetricFilter": {"fieldName": field,
                                                 "stringFilter": {"matchType": match, "value": value}}}]}}]}}}}]}


ap = argparse.ArgumentParser()
ap.add_argument("--apply", action="store_true")
args = ap.parse_args()
for s in SOURCES:
    print(f"  {s[0]:<28} {s[1]} {s[2]} '{s[3]}'")
if not args.apply:
    raise SystemExit("\nPreview only. Re-run with --apply to create them.")

creds = service_account.Credentials.from_service_account_info(
    json.loads(os.environ["GOOGLE_SERVICE_ACCOUNT_JSON"]), scopes=["https://www.googleapis.com/auth/analytics.edit"])
creds.refresh(google.auth.transport.requests.Request())
h = {"Authorization": "Bearer " + creds.token}
have = {a["displayName"] for a in requests.get(API, headers=h, timeout=30).json().get("audiences", [])}
for s in SOURCES:
    if s[0] in have:
        print("SKIP", s[0], "(exists)")
        continue
    r = requests.post(API, headers=h, json=body(*s), timeout=30)
    print("OK  " if r.ok else "FAIL", s[0], "" if r.ok else r.text[:200])
