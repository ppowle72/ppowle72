"""Add the tagged shop link to the top of every video description on your YouTube channel.
PREVIEW by default; changes nothing without --apply. Videos that already have a utm_source=youtube link are skipped.

    python yt_descriptions.py client_secret_2_XXXX.json            # preview
    python yt_descriptions.py client_secret_2_XXXX.json --apply    # edit descriptions

First run opens a sign-in link: use the Google account that OWNS the channel (the YouTube Data API v3
must be enabled in the same Cloud project, and that account must be a Test user). A token is saved in
yt_token.json so later runs do not ask again. Needs: pip install requests google-auth-oauthlib
"""
import argparse
import json
import os
import sys

import requests
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]
LINK = "https://alphonsomango.in/?utm_source=youtube&utm_medium=video&utm_campaign=video_description"
LINE = f"Order Alphonso mangoes: {LINK}"
TOKEN = "yt_token.json"
API = "https://www.googleapis.com/youtube/v3"

ap = argparse.ArgumentParser()
ap.add_argument("client_secret")
ap.add_argument("--apply", action="store_true")
ap.add_argument("--limit", type=int, default=0, help="only the newest N videos")
args = ap.parse_args()

creds = None
if os.path.exists(TOKEN):
    creds = Credentials.from_authorized_user_file(TOKEN, SCOPES)
if not creds or not creds.valid:
    if creds and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(args.client_secret, SCOPES)
        creds = flow.run_local_server(port=0, open_browser=False, prompt="consent",
                                      authorization_prompt_message="\nOpen this link signed in as the CHANNEL OWNER:\n{url}\n")
    with open(TOKEN, "w") as f:
        f.write(creds.to_json())
H = {"Authorization": "Bearer " + creds.token}

ch = requests.get(f"{API}/channels", headers=H, params={"part": "snippet,contentDetails", "mine": "true"}, timeout=30).json()
if not ch.get("items"):
    sys.exit("This account has no channel. Sign in as the channel owner. Response: " + json.dumps(ch)[:300])
print("Channel:", ch["items"][0]["snippet"]["title"])
uploads = ch["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

ids, page = [], None
while True:
    r = requests.get(f"{API}/playlistItems", headers=H, timeout=30,
                     params={"part": "contentDetails", "playlistId": uploads, "maxResults": 50, "pageToken": page}).json()
    ids += [i["contentDetails"]["videoId"] for i in r.get("items", [])]
    page = r.get("nextPageToken")
    if not page:
        break
if args.limit:
    ids = ids[:args.limit]

todo = []
for i in range(0, len(ids), 50):
    r = requests.get(f"{API}/videos", headers=H, params={"part": "snippet", "id": ",".join(ids[i:i + 50])}, timeout=30).json()
    for v in r.get("items", []):
        d = v["snippet"].get("description", "")
        if "utm_source=youtube" in d:
            continue
        todo.append(v)

print(f"{len(ids)} videos, {len(todo)} need the link\n")
for v in todo:
    print("  -", v["snippet"]["title"][:70])
if not args.apply:
    sys.exit("\nPreview only. Re-run with --apply to edit descriptions. Each update uses 50 API quota units.")

ok = bad = 0
for v in todo:
    s = v["snippet"]
    body = {"id": v["id"], "snippet": {"title": s["title"], "categoryId": s["categoryId"],
                                       "description": LINE + "\n\n" + s.get("description", "")}}
    for k in ("tags", "defaultLanguage"):  # keep them; omitted fields get cleared by the API
        if k in s:
            body["snippet"][k] = s[k]
    r = requests.put(f"{API}/videos", headers={**H, "Content-Type": "application/json"},
                     params={"part": "snippet"}, data=json.dumps(body), timeout=30)
    ok += r.ok
    bad += not r.ok
    print("OK  " if r.ok else "FAIL", s["title"][:60], "" if r.ok else r.text[:150])
print(f"\nDone: {ok} updated, {bad} failed.")
