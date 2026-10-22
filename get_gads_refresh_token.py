"""One-time helper: gets a Google Ads OAuth refresh token and writes the three
GOOGLE_ADS_CLIENT_ID / CLIENT_SECRET / REFRESH_TOKEN values into .env for you.

1. In Google Cloud > Auth Platform > Clients > mango-ads, click "Download JSON".
2. Put that client_secret_*.json file in this folder.
3. Run:  python get_gads_refresh_token.py client_secret_XXXX.json
4. Open the printed link in the browser profile signed in as the Google Ads user.
"""
import json
import os
import sys

from google_auth_oauthlib.flow import InstalledAppFlow

if len(sys.argv) != 2:
    sys.exit("Usage: python get_gads_refresh_token.py client_secret_XXXX.json")

with open(sys.argv[1], encoding="utf-8") as f:
    info = json.load(f)
client = info.get("installed") or info.get("web")
if not client:
    sys.exit("That JSON is not an OAuth client file (no 'installed' section).")
print("Client ID starts:", client["client_id"][:14], "| ends:", client["client_id"][-28:])

flow = InstalledAppFlow.from_client_secrets_file(sys.argv[1], scopes=["https://www.googleapis.com/auth/adwords"])
creds = flow.run_local_server(
    port=0, prompt="consent", access_type="offline", open_browser=False,
    authorization_prompt_message="\nOpen this link in the browser profile signed in as alphonsomangoesin@gmail.com:\n{url}\n")

new = {
    "GOOGLE_ADS_CLIENT_ID": client["client_id"],
    "GOOGLE_ADS_CLIENT_SECRET": client["client_secret"],
    "GOOGLE_ADS_REFRESH_TOKEN": creds.refresh_token,
}
lines = []
if os.path.exists(".env"):
    with open(".env", encoding="utf-8") as f:
        lines = [l.rstrip("\n") for l in f if not any(l.startswith(k + "=") for k in new)]
lines += [f"{k}={v}" for k, v in new.items()]
with open(".env", "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")
print("\nDone. Wrote GOOGLE_ADS_CLIENT_ID, GOOGLE_ADS_CLIENT_SECRET and GOOGLE_ADS_REFRESH_TOKEN to .env")
