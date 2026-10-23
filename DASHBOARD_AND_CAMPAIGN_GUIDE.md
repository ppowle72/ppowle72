# Dashboard + Diwali campaign: step by step, with every link

Work folder on your PC: `E:\Claude SEO tool\mango-seo-agent-v4.0`
Sign in as **alphonsomangoesin@gmail.com** for Google Ads and Data Studio, **ppowle1@gmail.com** for Cloud Console.

## A. Open the pages (PowerShell)
```powershell
cd "E:\Claude SEO tool\mango-seo-agent-v4.0"
Start-Process "https://lookerstudio.google.com/reporting/2af0d53a-b75b-4e6c-aee6-8c3ad72a26c0/page/JQxBG/edit"
Start-Process "https://ads.google.com/aw/overview?ocid=1201358296"
```

## B. Before anything: health check (PowerShell)
```powershell
python health_check.py
python gads_audiences.py
python gads_goals.py
```
Expect: no pending items except the campaign and the WhatsApp/newsletter links; the `Shopify CM ...` lists have sizes; PURCHASE is the only "yes".

## C. Dashboard (Data Studio): https://lookerstudio.google.com
Chart recipe: **Add a chart** > type > drag a box on the canvas > right panel **Setup**: Data source, Dimension, Metric.

1. **Date control (page 1):** Add a control > **Date range control** > click the canvas top right > right panel **Properties** > **Default date range** = **Last 28 days**. Copy it onto every page.
2. **Page 1 Overview** (source Alphonsomango.in): 5 scorecards (Sessions, Total users, Ecommerce purchases, Purchase revenue, Add to carts); time series Date x Sessions; table Country x Sessions.
3. **Page 2 Traffic sources** (Page > New page): table Session source / medium x Sessions, Total users, Add to carts, Ecommerce purchases; table Session campaign x Sessions; bar chart Session source / medium x Sessions; drop-down list on Session source / medium.
4. **Page 3 Shop funnel:** bar chart Sessions, Add to carts, Checkouts, Ecommerce purchases; table Item name x Items viewed, Items added to cart, Items purchased, Item revenue; calculated field `Cart abandonment` = `1 - (Ecommerce purchases / Add to carts)`.
5. **Page 4 Google Ads** (source Google Ads): scorecards Cost, Clicks, Impressions, Conversions, Conv. value; calculated field `ROAS` = `Conv. value / Cost`; table Campaign x Cost, Clicks, Conversions, Conv. value.
6. **Page 5 Search** (source Search console): table Query x Clicks, Impressions, URL CTR, Average position; table Landing page x Clicks, Impressions; time series Clicks x Date.
7. **Share:** Share > Manage access > add `ppowle1@gmail.com` as Editor; do the same for each data source (home page > Data sources tab). Weekly email: Share > Schedule delivery.

**Merchant Center in the dashboard:** Data Studio has no direct Merchant Center connector that I can confirm. Options: (a) product performance from the Google Ads connector (Shopping product fields); (b) Merchant Center > BigQuery data transfer (merchant ID 719656549) at https://console.cloud.google.com/bigquery/transfers, then add BigQuery as a data source. Option (b) may need billing enabled; start with (a).

## D. Diwali campaign by script (PowerShell)
1. Make a folder `ad_images` inside the work folder with: landscape 1.91:1 images (for example 1200x628), square 1:1 (1200x1200), portrait 4:5 (960x1200), and a square logo named `logo.png`. Each file under 5 MB.
2. Install and download:
```powershell
pip install pillow google-ads python-dotenv
curl.exe -L -o gads_demandgen.py https://raw.githubusercontent.com/ppowle72/ppowle72/claude/elegant-hypatia-dvxtwj/gads_demandgen.py
curl.exe -L -o demandgen_config.json https://raw.githubusercontent.com/ppowle72/ppowle72/claude/elegant-hypatia-dvxtwj/demandgen_config.example.json
notepad demandgen_config.json
```
3. In Notepad set `daily_budget_inr` (a real number), check `max_cpc_inr`, `images_folder`, the headlines and descriptions, and the audience names. Save.
4. Preview (asks Google to validate, creates nothing):
```powershell
python gads_demandgen.py
```
5. If it says VALID, create it paused:
```powershell
python gads_demandgen.py --apply
```
6. Open https://ads.google.com/aw/campaigns?ocid=1201358296, review the campaign, then enable it.
7. Check the toggle "Optimised targeting" on the ad group: turn it OFF if you want only your lists.

## E. Campaign by hand instead (Google Ads)
Campaigns > + New campaign > Sales > Demand Gen > Purchase goal only > Maximize clicks > budget > India, English and Hindi > audiences (target: Shopify CM - Abandoned Checkouts 30d, Email Subscribers, Never Purchased; exclude: Shopify CM - Repeat Buyers, All Converters, Purchasers of Alphonsomango.in) > creative > final URL `https://alphonsomango.in/collections/dry-fruits` (no UTM tags; auto-tagging handles Google Ads) > publish.

## F. After the campaign runs
```powershell
python gads_audiences.py
python gads_conversions.py
python health_check.py
```
