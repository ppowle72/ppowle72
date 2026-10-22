# Alphonso Mango: Google marketing setup (complete guide)

Accounts: GA4 property `294116937` (Powle Home Foods / Alphonsomango.in), Google Ads `415-561-5429`.
Run every script from `E:\Claude SEO tool\mango-seo-agent-v4.0`. All download with:
`curl.exe -L -o NAME.py https://raw.githubusercontent.com/ppowle72/ppowle72/claude/elegant-hypatia-dvxtwj/NAME.py`

## 1. Status

| Item | State |
|---|---|
| GA4 audiences (7 + Past purchasers) | Created, syncing to Google Ads |
| Google Ads API login (OAuth) | Working |
| Account-default goal | Purchase only (verified) |
| Primary purchase action | Google Shopping App Purchase |
| festivetreat.com purchase action | Removed |
| Enabled campaigns | None yet |
| Audience sizes | 0 (new), `Purchasers of Alphonsomango.in` = 180 |
| Disengaged / High-value purchasers | Created in UI |
| Maps + source audiences (Instagram, Facebook, LinkedIn, YouTube, WhatsApp, Email, Paid social) | Created in GA4 |
| UTM links pasted | Done: Instagram, Facebook, LinkedIn, YouTube (channel links and 2 video descriptions), Business Profile |
| UTM links still to do | WhatsApp Business, Mailchimp/email buttons, Meta ads |
| 6 dead Universal Analytics goals | Remove in UI (optional) |
| Looker Studio dashboard | Not built yet |
| Profile reviews | Later |

## 2. Scripts and when to use them

| Script | Purpose | Changes anything? |
|---|---|---|
| `google_assets_check.py` | Status of GA4/Ads/Merchant/Business Profile links, auto-tagging | No |
| `utm_links.py` | Builds tagged links for every channel into `utm_links.csv` | No |
| `ga4_gbp_audience.py` | Audience: visitors from Google Maps / Business Profile | `--apply` |
| `ga4_source_audiences.py` | One audience per source (Instagram, Facebook, LinkedIn, YouTube, WhatsApp, Email, Paid social) | `--apply` |
| `gads_audiences.py` | Lists audiences/campaigns; `--apply` adds them to Search as Observation | `--apply` |
| `gads_goals.py` | Keeps Purchase as the only account-default goal | `--apply` |
| `gads_conversions.py` | Lists conversion actions | No |

Order for new work: `google_assets_check.py` -> `utm_links.py` -> `ga4_gbp_audience.py --apply` -> `ga4_source_audiences.py --apply`.
Run each `--apply` script ONCE. Re-running audience scripts skips existing audiences, but older ones (`ga4_audiences.py`) would duplicate.

## 3. UTM rules (use exactly these, all lowercase)

`utm_source` = the platform, `utm_medium` = the type, `utm_campaign` = the specific effort.

| Channel | utm_source | utm_medium | utm_campaign |
|---|---|---|---|
| Instagram bio / posts | instagram | social | bio, organic_post |
| Instagram ads | instagram | paid_social | mango_season |
| Facebook page / posts | facebook | social | page |
| Facebook ads | facebook | paid_social | mango_season |
| LinkedIn | linkedin | social | page, organic_post |
| YouTube | youtube | video | channel |
| WhatsApp | whatsapp | messaging | broadcast |
| Email | newsletter | email | monthly |
| Google Maps / Business Profile | google | organic | gbp |
| Google Ads | no UTM; auto-tagging (gclid) does it | | |

Never put UTMs on links inside your own website. Run `python utm_links.py` for ready-made URLs.

## 4. Manual steps no script can do

1. Paste the tagged links into each profile (Instagram bio, Facebook page, LinkedIn page, YouTube, WhatsApp, Business Profile website field).
2. Link accounts in Google Ads > Tools > Linked accounts: Business Profile, Merchant Center, YouTube.
3. GA4 > Admin > Product links > Search Console links.
4. Optional: remove the 6 dead Universal Analytics goals in Goals > Conversions.
5. Turn on auto-tagging if `google_assets_check.py` says it is OFF (Google Ads > Admin > Account settings).
6. Link Meta (Instagram/Facebook) ads manually with the UTM links above; Meta does not tag for you.

## 5. Retargeting plan (build in January for the pre-booking offer)

- Campaign: Demand Gen, goal Sales, conversion goal Purchase only, small daily budget, Maximize Clicks to start.
- Target: Basket abandoners 90d, Checkout starters 90d, Item viewers 90d, plus source audiences (Instagram, Facebook, LinkedIn, Maps).
- Exclude: Purchasers of Alphonsomango.in, Past purchasers 540d.
- Locations: India for the main campaign; overseas separate using Overseas visitors.
- Lists need roughly 100 users for Display/Demand Gen and 1,000 for Search. Check `python gads_audiences.py` weekly.

## 6. Weekly routine

1. `python gads_audiences.py` (sizes and campaigns)
2. GA4 > Reports > Acquisition > Traffic acquisition (check each source)
3. After campaigns run: `python gads_conversions.py`

## 7. Security

- `.env` and `client_secret_*.json` hold live secrets. Never share or commit them.
- The OAuth app is in Testing: the refresh token expires after 7 days of inactivity or when revoked. If a Google Ads script says `invalid_grant`, rerun `get_gads_refresh_token.py client_secret_2_*.json`.
