"""One-command health check of your whole Google marketing setup. READ-ONLY, changes nothing.

    python health_check.py

Checks: GA4 reachable, GA4 Data API + which UTM sources have traffic (last 7 days), GA4 audiences,
GA4->Ads links, Google Ads account/campaigns/goals/audience-list sizes, Search Console access.
Ends with a PENDING list. Looker Studio sources cannot be listed by API with a personal Gmail login:
check them in Looker Studio > Resource > Manage added data sources.
"""
import json
import os

import google.auth.transport.requests
import requests
from dotenv import load_dotenv
from google.ads.googleads.client import GoogleAdsClient
from google.oauth2 import service_account

load_dotenv()
PROP = os.environ.get("GA4_PROPERTY_ID", "294116937")
pending = []


def head(t):
    print(f"\n=== {t} ===")


def ok(m):
    print("  OK     ", m)


def bad(m, fix=""):
    print("  PROBLEM", m)
    pending.append(m + (f"  -> {fix}" if fix else ""))


def info(m):
    print("  info   ", m)


# ---------- GA4 / Search Console via service account
SCOPES = ["https://www.googleapis.com/auth/analytics.readonly", "https://www.googleapis.com/auth/webmasters.readonly"]
H = None
try:
    creds = service_account.Credentials.from_service_account_info(json.loads(os.environ["GOOGLE_SERVICE_ACCOUNT_JSON"]), scopes=SCOPES)
    creds.refresh(google.auth.transport.requests.Request())
    H = {"Authorization": "Bearer " + creds.token}
    info("service account: " + creds.service_account_email)
except Exception as e:
    bad("Service account login failed: " + str(e)[:100])

if H:
    head("GA4 property")
    try:
        r = requests.get(f"https://analyticsadmin.googleapis.com/v1beta/properties/{PROP}", headers=H, timeout=30)
        ok(f"{r.json().get('displayName')} (property {PROP}, currency {r.json().get('currencyCode')})") if r.ok else bad("GA4 property not reachable: " + r.text[:100])
    except Exception as e:
        bad("GA4 property check failed: " + str(e)[:80])

    head("GA4 Data API: traffic by source / medium (last 7 days)")
    try:
        body = {"dateRanges": [{"startDate": "7daysAgo", "endDate": "today"}], "dimensions": [{"name": "sessionSourceMedium"}],
                "metrics": [{"name": "sessions"}], "orderBys": [{"metric": {"metricName": "sessions"}, "desc": True}], "limit": 30}
        r = requests.post(f"https://analyticsdata.googleapis.com/v1beta/properties/{PROP}:runReport", headers=H, json=body, timeout=30)
        if not r.ok:
            bad("GA4 Data API not working: " + r.json().get("error", {}).get("message", r.text)[:140],
                "enable 'Google Analytics Data API' at console.cloud.google.com/apis/library/analyticsdata.googleapis.com")
        else:
            rows = [(x["dimensionValues"][0]["value"], x["metricValues"][0]["value"]) for x in r.json().get("rows", [])]
            for k, v in rows[:15]:
                print(f"           {v:>6}  {k}")
            for want in ["instagram", "facebook", "linkedin", "youtube", "google / organic", "whatsapp", "newsletter"]:
                if not any(want in k.lower() for k, _ in rows):
                    pending.append(f"No traffic yet from '{want}' in the last 7 days (link not pasted, or nobody clicked)")
            ok(f"{len(rows)} sources have traffic") if rows else bad("No sessions in the last 7 days")
    except Exception as e:
        bad("GA4 Data API check failed: " + str(e)[:80])

    head("GA4 audiences")
    try:
        r = requests.get(f"https://analyticsadmin.googleapis.com/v1alpha/properties/{PROP}/audiences?pageSize=200", headers=H, timeout=30)
        names = [a["displayName"] for a in r.json().get("audiences", [])] if r.ok else []
        ok(f"{len(names)} audiences") if names else bad("Could not list GA4 audiences")
        for want in ["Basket abandoners 90d", "Checkout starters 90d", "Item viewers 90d", "Non-purchasers 90d", "Past purchasers 540d",
                     "Overseas visitors", "Fresh mango viewers", "Maps / Business Profile visitors", "Visitors: Instagram 90d",
                     "Visitors: Facebook 90d", "Visitors: LinkedIn 90d", "Visitors: YouTube 90d", "Visitors: Email 90d"]:
            if want not in names:
                bad("Missing GA4 audience: " + want)
    except Exception as e:
        bad("Audience check failed: " + str(e)[:80])

    head("GA4 -> Google Ads links")
    try:
        r = requests.get(f"https://analyticsadmin.googleapis.com/v1alpha/properties/{PROP}/googleAdsLinks", headers=H, timeout=30)
        for l in r.json().get("googleAdsLinks", []):
            ok(f"customer {l.get('customerId')} | personalised ads {l.get('adsPersonalizationEnabled')}")
            if l.get("customerId", "").replace("-", "") == "4380786949":
                bad("GA4 is still linked to the CLOSED account 438-078-6949", "GA4 Admin > Product links > Google Ads links > delete it")
    except Exception as e:
        bad("Link check failed: " + str(e)[:80])

    head("Search Console (service account access; Looker Studio uses YOUR login instead)")
    try:
        r = requests.get("https://www.googleapis.com/webmasters/v3/sites", headers=H, timeout=30)
        sites = [s["siteUrl"] for s in r.json().get("siteEntry", [])] if r.ok else []
        info("service account can see: " + (", ".join(sites) if sites else "no sites (this is fine for Looker Studio)"))
    except Exception as e:
        info("not checked: " + str(e)[:60])

# ---------- Google Ads
head("Google Ads")
try:
    cfg = {"developer_token": os.environ["GOOGLE_ADS_DEVELOPER_TOKEN"], "client_id": os.environ["GOOGLE_ADS_CLIENT_ID"],
           "client_secret": os.environ["GOOGLE_ADS_CLIENT_SECRET"], "refresh_token": os.environ["GOOGLE_ADS_REFRESH_TOKEN"], "use_proto_plus": True}
    login = "".join(c for c in os.environ.get("GOOGLE_ADS_LOGIN_CUSTOMER_ID", "") if c.isdigit())
    if login:
        cfg["login_customer_id"] = login
    client = GoogleAdsClient.load_from_dict(cfg)
    cid = "".join(c for c in os.environ["GOOGLE_ADS_CUSTOMER_ID"] if c.isdigit())
    svc = client.get_service("GoogleAdsService")

    def q(s):
        return [r for b in svc.search_stream(customer_id=cid, query=s) for r in b.results]

    c = q("SELECT customer.descriptive_name, customer.status, customer.auto_tagging_enabled FROM customer")[0].customer
    ok(f"{c.descriptive_name} ({c.status.name}); auto-tagging {'ON' if c.auto_tagging_enabled else 'OFF'}")
    if not c.auto_tagging_enabled:
        bad("Auto-tagging is OFF", "Google Ads > Admin > Account settings")
    camps = q("SELECT campaign.name FROM campaign WHERE campaign.status = 'ENABLED'")
    ok(f"{len(camps)} enabled campaigns") if camps else bad("No enabled campaigns (audiences have nothing to attach to)", "build the January campaign")
    goals = [g.customer_conversion_goal.category.name for g in q("SELECT customer_conversion_goal.category, customer_conversion_goal.biddable FROM customer_conversion_goal WHERE customer_conversion_goal.biddable = TRUE")]
    ok("bidding goals: " + ", ".join(goals))
    if goals != ["PURCHASE"]:
        bad("Account-default goals are not only PURCHASE: " + ", ".join(goals), "python gads_goals.py --apply")
    lists = q("SELECT user_list.name, user_list.size_for_search FROM user_list")
    big = [(l.user_list.name, l.user_list.size_for_search) for l in lists if l.user_list.size_for_search]
    info(f"{len(lists)} audience lists; with members: " + (", ".join(f"{n} ({s})" for n, s in big) or "none yet"))
    if not big:
        bad("All audience lists are still size 0", "wait for traffic; re-run weekly")
except Exception as e:
    bad("Google Ads check failed: " + str(e).replace("\n", " ")[:160])

head("Looker Studio (check by hand)")
info("Open https://lookerstudio.google.com > your report > Resource > Manage added data sources")
info("Expect: Google Analytics (Alphonsomango.in), Google Ads (415-561-5429), Search Console (alphonsomango.in)")
info("Credentials column must say 'Owner' or your account, not 'Needs reauthorisation'")

head("PENDING")
for i, p in enumerate(pending, 1):
    print(f"  {i}. {p}")
if not pending:
    print("  nothing: all checks passed")
