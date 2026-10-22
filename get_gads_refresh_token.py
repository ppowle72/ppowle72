"""One-time helper: sign in with the Google account that owns the Google Ads account
and print a refresh token to paste into .env as GOOGLE_ADS_REFRESH_TOKEN.

Needs GOOGLE_ADS_CLIENT_ID and GOOGLE_ADS_CLIENT_SECRET in .env first.
Run:  python get_gads_refresh_token.py
"""
import os

from dotenv import load_dotenv
from google_auth_oauthlib.flow import InstalledAppFlow

load_dotenv()
cfg = {"installed": {
    "client_id": os.environ["GOOGLE_ADS_CLIENT_ID"],
    "client_secret": os.environ["GOOGLE_ADS_CLIENT_SECRET"],
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "redirect_uris": ["http://localhost"],
}}
flow = InstalledAppFlow.from_client_config(cfg, scopes=["https://www.googleapis.com/auth/adwords"])
creds = flow.run_local_server(port=0, prompt="consent", access_type="offline")
print("\nAdd this line to .env:\nGOOGLE_ADS_REFRESH_TOKEN=" + creds.refresh_token)
