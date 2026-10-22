"""READ-ONLY status check of your Google marketing links. Changes nothing.

    python google_assets_check.py

Checks: GA4 -> Google Ads link, Google Ads auto-tagging, Merchant Center link,
Business Profile (location) link. YouTube and Search Console cannot be read via API: check in the UI.
Needs the same .env as the other scripts (service-account JSON for GA4, OAuth values for Google Ads).
"""
import json
import os

import google.auth.transport.requests
import requests
from dotenv import load_dotenv
from google.ads.googleads.client import GoogleAdsClient
from google.oauth2 import service_account

load_dotenv()
PROPERTY = os.environ.get("GA4_PROPERTY_ID", "294116937")


def digits(v):
    return "".join(c for c in (v or "") if c.isdigit())


def say(name, status, detail=""):
    print(f"{status:<14} {name}" + (f"  - {detail}" if detail else ""))


# ---- GA4 -> Google Ads link
try:
    raw = os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON")
    creds = service_account.Credentials.from_service_account_info(
        json.loads(raw), scopes=["https://www.googleapis.com/auth/analytics.readonly"])
    creds.refresh(google.auth.transport.requests.Request())
    h = {"Authorization": "Bearer " + creds.token}
    r = requests.get(f"https://analyticsadmin.googleapis.com/v1alpha/properties/{PROPERTY}/googleAdsLinks", headers=h, timeout=30)
    links = r.json().get("googleAdsLinks", []) if r.ok else None
    if links is None:
        say("GA4 -> Google Ads link", "COULD NOT CHECK", r.text[:120])
    elif links:
        for l in links:
            say("GA4 -> Google Ads link", "OK", f"customer {l.get('customerId')} | personalised ads: {l.get('adsPersonalizationEnabled')}")
    else:
        say("GA4 -> Google Ads link", "NOT LINKED", "Admin > Product links > Google Ads links")
except Exception as e:
    say("GA4 -> Google Ads link", "COULD NOT CHECK", str(e)[:120])

# ---- Google Ads side
cfg = {"developer_token": os.environ["GOOGLE_ADS_DEVELOPER_TOKEN"], "client_id": os.environ["GOOGLE_ADS_CLIENT_ID"],
       "client_secret": os.environ["GOOGLE_ADS_CLIENT_SECRET"], "refresh_token": os.environ["GOOGLE_ADS_REFRESH_TOKEN"],
       "use_proto_plus": True}
if digits(os.environ.get("GOOGLE_ADS_LOGIN_CUSTOMER_ID")):
    cfg["login_customer_id"] = digits(os.environ["GOOGLE_ADS_LOGIN_CUSTOMER_ID"])
client = GoogleAdsClient.load_from_dict(cfg)
cid = digits(os.environ["GOOGLE_ADS_CUSTOMER_ID"])
svc = client.get_service("GoogleAdsService")


def q(gaql):
    return [r for b in svc.search_stream(customer_id=cid, query=gaql) for r in b.results]


def check(name, gaql, fmt, none_msg):
    try:
        rows = q(gaql)
        if rows:
            for r in rows:
                say(name, "OK", fmt(r))
        else:
            say(name, "NOT LINKED", none_msg)
    except Exception as e:
        say(name, "COULD NOT CHECK", str(e).replace("\n", " ")[:120])


check("Auto-tagging (gclid)", "SELECT customer.auto_tagging_enabled FROM customer",
      lambda r: "enabled" if r.customer.auto_tagging_enabled else "OFF - turn on in Google Ads > Admin > Account settings",
      "")
check("Merchant Center link",
      "SELECT product_link.merchant_center.merchant_center_id FROM product_link WHERE product_link.type = 'MERCHANT_CENTER'",
      lambda r: f"merchant {r.product_link.merchant_center.merchant_center_id}",
      "Google Ads > Tools > Linked accounts > Merchant Center")
check("Business Profile link",
      "SELECT asset_set.name, asset_set.status FROM asset_set WHERE asset_set.type = 'LOCATION_SYNC'",
      lambda r: f"{r.asset_set.name} ({r.asset_set.status.name})",
      "Google Ads > Tools > Linked accounts > Business Profile")
say("YouTube -> Google Ads", "CHECK IN UI", "Google Ads > Tools > Linked accounts > YouTube")
say("GA4 -> Search Console", "CHECK IN UI", "GA4 Admin > Product links > Search Console links")
