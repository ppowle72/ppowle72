"""Create the GA4 audience 'Maps / Business Profile visitors' (people who arrive via the
Business Profile link tagged utm_campaign=gbp). PREVIEW by default.

    python ga4_gbp_audience.py            # shows what it would create
    python ga4_gbp_audience.py --apply    # creates it (skips if it already exists)
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
NAME = "Maps / Business Profile visitors"
BODY = {
    "displayName": NAME,
    "description": "Sessions from the Business Profile link (utm_campaign=gbp)",
    "membershipDurationDays": 90,
    "filterClauses": [{"clauseType": "INCLUDE", "simpleFilter": {
        "scope": "AUDIENCE_FILTER_SCOPE_ACROSS_ALL_SESSIONS",
        "filterExpression": {"andGroup": {"filterExpressions": [{"orGroup": {"filterExpressions": [
            {"dimensionOrMetricFilter": {"fieldName": "sessionCampaignName",
                                         "stringFilter": {"matchType": "EXACT", "value": "gbp"}}}]}}]}}}}],
}

ap = argparse.ArgumentParser()
ap.add_argument("--apply", action="store_true")
args = ap.parse_args()
print(json.dumps(BODY, indent=2))
if not args.apply:
    raise SystemExit("\nPreview only. Re-run with --apply to create it.")

creds = service_account.Credentials.from_service_account_info(
    json.loads(os.environ["GOOGLE_SERVICE_ACCOUNT_JSON"]), scopes=["https://www.googleapis.com/auth/analytics.edit"])
creds.refresh(google.auth.transport.requests.Request())
h = {"Authorization": "Bearer " + creds.token}
existing = [a["displayName"] for a in requests.get(API, headers=h, timeout=30).json().get("audiences", [])]
if NAME in existing:
    raise SystemExit(f"\nAlready exists: {NAME}. Nothing created.")
r = requests.post(API, headers=h, json=BODY, timeout=30)
print("\nOK" if r.ok else "FAIL", NAME, "" if r.ok else r.text)
