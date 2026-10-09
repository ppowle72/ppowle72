# Free Merchant Center reporting (no Supermetrics)

Uses Google's own Merchant API from a Google Sheet. Cost: nothing. You sign in with the Google account that owns Merchant Center account 719656549.

## Set up (about 15 minutes)
1. Create a Google Sheet named "Merchant Center report". Extensions, Apps Script.
2. In the Apps Script editor: replace `Code.gs` with the file here; open Project Settings, tick "Show appsscript.json manifest file", and replace its contents with `appsscript.json` here.
3. Google Cloud: open https://console.cloud.google.com, create (or pick) a project, enable "Merchant API" (APIs & Services, Library). Copy the project number.
4. Apps Script, Project Settings, "Google Cloud Platform (GCP) Project", Change project, paste the project number.
5. Reload the Sheet. Menu "Merchant Center", "1. Register (run once)" and approve the permissions. Then "2. Pull everything now".
6. Menu "3. Create daily trigger" for a daily refresh at 7 am IST.

## What you get
- `Products`: every offer with price, availability, brand, MPN, approved and disapproved countries, issue count.
- `Issues`: every item-level issue with code, severity, attribute and Google's help link (this is the list that shows "missing size" and similar).
- `Performance`: 90-day clicks, impressions and CTR per product.
- `Summary`: totals.

## Optional: send a daily summary to AdPulse
Set `ADPULSE_URL` in `CONFIG` to your collector's `/e` address. It posts one `merchant_center_snapshot` event (counts only) that your `adpulse-collector` Worker stores in its events table. The Worker is not changed.

## Limits and notes
- The script is an untested draft. If a call fails, the Sheet shows the error text from Google; check the field names in the Merchant API reference.
- A stronger option for large history is the BigQuery Data Transfer Service connector for Merchant Center (free transfer, small BigQuery cost).
- Alternatively export from Merchant Center manually (Products, Diagnostics) and send me the files.
