"""One-time helper: sign in with the Google account that owns the Google Ads account
and print a refresh token to paste into .env as GOOGLE_ADS_REFRESH_TOKEN.

Needs GOOGLE_ADS_CLIENT_ID and GOOGLE_ADS_CLIENT_SECRET in .env first.
Run:  python get_gads_refresh_token.py
"""
import os

from dotenv import load_dotenv
from google_auth_oauthlib.flow import InstalledAppFlow

load_dotenv()
cid = os.environ["GOOGLE_ADS_CLIENT_ID"].strip().strip('"').strip("'")
csec = os.environ["GOOGLE_ADS_CLIENT_SECRET"].strip().strip('"').strip("'")
print("Using client ID starting:", cid[:20], "... length", len(cid))
print("Client ID should start 566751527087- and end .apps.googleusercontent.com:", cid.startswith("566751527087-") and cid.endswith(".apps.googleusercontent.com"))
cfg = {"installed": {
    "client_id": cid,
    "client_secret": csec,
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "redirect_uris": ["http://localhost"],
}}
flow = InstalledAppFlow.from_client_config(cfg, scopes=["https://www.googleapis.com/auth/adwords"])
creds = flow.run_local_server(port=0, prompt="consent", access_type="offline", open_browser=False,
                              authorization_prompt_message="\nCopy this link into the browser profile signed in as alphonsomangoesin@gmail.com:\n{url}\n")
print("\nAdd this line to .env:\nGOOGLE_ADS_REFRESH_TOKEN=" + creds.refresh_token)
