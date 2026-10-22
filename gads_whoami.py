"""Shows which Google Ads accounts your OAuth login can reach, and the IDs in .env.
Changes nothing.   python gads_whoami.py
"""
import os

from dotenv import load_dotenv
from google.ads.googleads.client import GoogleAdsClient

load_dotenv()
cfg = {
    "developer_token": os.environ["GOOGLE_ADS_DEVELOPER_TOKEN"],
    "client_id": os.environ["GOOGLE_ADS_CLIENT_ID"],
    "client_secret": os.environ["GOOGLE_ADS_CLIENT_SECRET"],
    "refresh_token": os.environ["GOOGLE_ADS_REFRESH_TOKEN"],
    "use_proto_plus": True,
}
print("CUSTOMER_ID in .env      :", os.environ.get("GOOGLE_ADS_CUSTOMER_ID"))
print("LOGIN_CUSTOMER_ID in .env:", os.environ.get("GOOGLE_ADS_LOGIN_CUSTOMER_ID"))
client = GoogleAdsClient.load_from_dict(cfg)
res = client.get_service("CustomerService").list_accessible_customers()
print("\nAccounts this login can open directly:")
for rn in res.resource_names:
    cid = rn.split("/")[1]
    try:
        cfg2 = dict(cfg, login_customer_id=cid)
        c2 = GoogleAdsClient.load_from_dict(cfg2)
        row = next(iter(c2.get_service("GoogleAdsService").search(
            customer_id=cid,
            query="SELECT customer.id, customer.descriptive_name, customer.manager, customer.status FROM customer LIMIT 1")))
        c = row.customer
        print(f"  {cid} | {c.descriptive_name} | manager={c.manager} | {c.status.name}")
    except Exception as e:
        print(f"  {cid} | (could not read details: {str(e)[:80]})")
