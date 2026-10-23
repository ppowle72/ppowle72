"""Remove the GA4 -> Google Ads link to the CLOSED account 438-078-6949. PREVIEW by default.

    python ga4_unlink_closed.py            # shows the link it would delete
    python ga4_unlink_closed.py --apply    # deletes it
Only the link whose customerId is 4380786949 is touched; 415-561-5429 is left alone.
"""
import argparse
import json
import os

import google.auth.transport.requests
import requests
from dotenv import load_dotenv
from google.oauth2 import service_account

load_dotenv()
PROP = os.environ.get("GA4_PROPERTY_ID", "294116937")
CLOSED = "4380786949"
ap = argparse.ArgumentParser()
ap.add_argument("--apply", action="store_true")
args = ap.parse_args()

creds = service_account.Credentials.from_service_account_info(
    json.loads(os.environ["GOOGLE_SERVICE_ACCOUNT_JSON"]), scopes=["https://www.googleapis.com/auth/analytics.edit"])
creds.refresh(google.auth.transport.requests.Request())
H = {"Authorization": "Bearer " + creds.token}
r = requests.get(f"https://analyticsadmin.googleapis.com/v1alpha/properties/{PROP}/googleAdsLinks", headers=H, timeout=30)
links = r.json().get("googleAdsLinks", [])
for l in links:
    print(l.get("customerId"), "|", l.get("name"))
target = [l for l in links if l.get("customerId", "").replace("-", "") == CLOSED]
if not target:
    raise SystemExit("\nNo link to the closed account found. Nothing to do.")
if not args.apply:
    raise SystemExit(f"\nPreview: would delete {target[0]['name']}. Re-run with --apply.")
d = requests.delete(f"https://analyticsadmin.googleapis.com/v1alpha/{target[0]['name']}", headers=H, timeout=30)
print("\nDeleted" if d.ok else "FAIL", target[0]["name"], "" if d.ok else d.text[:200])
