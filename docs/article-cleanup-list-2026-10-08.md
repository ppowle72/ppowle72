# Article cleanup list (8 Oct 2026)

Compiled from the reports of every agent that edited articles in the "pre-order and 48 villages" pass.
All batches (A01 to A24, B01 to B28) are included. This is the final version for the pre-order and village-count pass.

## What the pass changed (done, live on Shopify)
- Pre-order, pre-book, pre-season booking and waitlist sentences about fresh mangoes became: "The 2027 mango season starts on 1 February 2027, and fresh mangoes are out of stock until then." Cards now read "Out of stock until 1 February 2027".
- The unverified "48 villages" count was removed (wording now "villages across Ratnagiri and Devgad", "our source villages", "Konkan villages").
- Season Pass sentences were removed where they appeared as one sentence; the Season Pass article itself was NOT touched.
- Articles covered: the 26 you named (25 edited, Season Pass article left alone), 217 articles with pre-order wording (waves A01 to A24, all done) and 247 articles with a village count (waves B01 to B28, all done). One article in wave B (`fresh-blueberry-price-per-kg`) was a false match and was not written.

## How the edits were checked (and where the check was weaker)
- Most articles were compared with the live text by script or by eye after writing. Several batches had no byte-level check; they were read by eye.
- Still checked by eye only: `mango-mist`, `buy-almonds-online` (B18). Ask if you want them diffed by script.
- Special (non-breaking) spaces became ordinary spaces in many articles. Invisible.
- Empty hidden comment markers (`<!---->`) were stripped from: `ratnagiri-hapus-price-guide`, `hapus-mango-online`, `mango-chunda-recipe`, `best-mangoes-in-pune-order-online`, `exclusive-deals-on-mangoes-online-best-price-offer`, `ratnagiri-hafoos`, `order-ratnagiri-hapus-amba-online`, `mango-madness-delicious-mango-recipes`, `alphonso-mango-in-india`, `mango-smoothie-for-baby`, `mango-rate-in-pune-sweet-deals-unveiled`, `buy-ratnagiri-hapus-amba-mango-bliss-from-konkan`.
- Three FAQ anchor ids were renamed by early agents (links to the old anchors would no longer scroll): `hapus-mango-in-delhi-v2` (two FAQ ids), `alphonso-mango-nagpur-v2` and `kesar-mango-peti` (FAQ ids). Later agents were told not to rename ids.
- Slips made and fixed during the run (each live for a short time): the `nri-mango-gift-india` page (truncated body, then a wrong link, final correct), `best-kesar-mango-online-deals` (truncated, rewritten), and stray classes or typos in a handful of articles, all rewritten and re-checked.

## 1. Decisions needed from you (claims I cannot verify or that carry risk)
1. **Season Pass article** `what-is-season-pass-for-alphonso-mango` (id 30398021678): entirely about a Season Pass, weekly boxes and pre-order options. Remove, unpublish or rewrite? Not edited.
2. **Subscription / pass claims (checked 8 Oct):** `/pages/monthly-pass` and the Season Pass article are published, but there is no pass or subscription product and no subscription plan on the store, so nothing can be bought. Recommendation: unpublish or replace with a prepaid Season Box launching 1 Feb 2027. Details: `alphonso-mango-subscription-box-monthly-delivery-plan-2026` (whole page is a stale 2026 subscription offer with subscribe links), `devgad-mangoes-in-mumbai-delicious-delight` ("Monthly Mango Pass" link and "Automated Purchases & Subscriptions" section), `buy-mango-for-breakfast` ("weekly mango delivery subscription for families"). Do these products exist?
3. **FSSAI number: FIXED (8 Oct).** `devgad-hapus` quoted 22110001060083 in five places (two in schema data). It now says 10020022011783, the number used in about 1,300 other places. Checked by re-fetch and reading, not a byte diff. Still open in that article: "98 villages", "45,000+ hectares", "organic" wording and "Season 2026" text.
3b. **Phone numbers: DECIDED (8 Oct).** Keep only +91 70830 75556 and +91 83690 48029. The third number 91676 68899 was in two articles (`devgad-hapus-online`, `devgad-hapus`) and is replaced by +91 70830 75556 in both (checked by script comparison). My earlier scan of all 978 articles found it nowhere else; it is in no page or theme file. Note: the brand WhatsApp +91 70830 75556 itself appears in none of the other articles; +91 83690 48029 appears in 28.
4. **Financial claim:** `fresh-alphonso-mangoes-home-delivery-near-me` says "Invest in Mango Bonds for a 10% interest rate". Recommend removing.
5. **The word "organic"** (no certification). Articles using it: `organic-mango` (title, headings, schema, alt text), `organic-mangoes-online-1`, `order-ratnagiri-hapus-amba-online`, `shop-devgad-hapus-mango-store-pune-maharashtra` ("100% organic"), `devgad-alphonso-mangoes-online-mumbai` ("certified organic" repeated), `order-strawberries-online` (16 times), `devgad-hapus` ("Organic Farming", "Devgad Organic"), `buy-hapus-ratnagiri-online`, `best-website-to-buy-devgad-alphonso-mangoes-online`, `alphonso-mango-online-purchase`, `mango-near-me-v2`, `mangoes-alphonso-ratnagiri-online`, `indian-mango-online`, `ratnagirimangoes-sweet-juicy`, `mango-madness-delicious-mango-recipes`, `buy-mangos-online`, `ordering-mangoes-online`, `indian-mango-buy-online-alphonsomango-in-order-now`, `alphonso-mango-fruit-order-online-fresh-and-delicious`, `selection-storage-and-ripening`, `how-mango-is-good-for-health`, `how-many-mango-trees-per-acre`, `order-alphonso-mango-online-top-10-reasons-to-indulge`, `mango-a-day-keep-doctor-away` (schema "GI-certified organic"), `best-hapus-mango-price-online-exclusive-deals`, `buy-ratnagiri-hapus-amba-mango-bliss-from-konkan`, `mango-leaves-health-benefit`, `mango-tree-lifespan`, `mango-rate-in-pune-sweet-deals-unveiled`, `mango-chunda-recipe`, `hapus-mango-online`, `fresh-mango-near-me`, `pairi-mango-online-convenient-delicious`, `mango-export-from-india`, `buy-fresh-fruit-mango-taste-the-tropical-flavor`, `alphonso-mango-online-udaipur` and others. Reword all?
6. **Customer counts:** "47,000+" / "47,961" customers appears in many articles (e.g. `aam-meaning-in-english`, `hapus-aam`, `mango-species`, `langra-mango`, `chausa-mango`, `origin-of-hapus-v2`, `mango-website`, `mango-leaves`, `best-mango-in-the-world`, `mango-tree-lifespan`, `amrakhand-mango-shrikhand`, `mango-for-infants`). Also "since 2019", "since 2020" and (in `llms-full`) 2017 for the founding year. Which wording is approved?
7. **Village counts:** "55 villages" / "55 named villages" (dozens of articles), "55+", "24 villages" (`devgad-mangoes`), "98 villages" (`devgad-hapus`), "48 orchards" (`devgad-mango`). Decide one approved sentence; the pass only removed "48".
8. **Store and location claims:** "Kurla store" (`mango-mumbai-store`), "Narayan Peth store" and "over 100 cities" (`shop-devgad-hapus-mango-store-pune-maharashtra`), About page "stores in Mumbai, Pune, Ahmedabad and Delhi", "we photograph every batch and track detection rates" sentence. Do these exist?
9. **Other claims to verify:** "We are the only online store that is GI tag certified" (`discover-the-best-ratnagiri-hapus-store-online`); delivery "anywhere in the world" and "year-round" (`indian-mango-buy-online-great-deals-await-you`, `alphonso-mango-online-noida`); "free delivery", "free shipping", "damage-free guarantee"; pin-code counts that disagree (600+, 300+, 15–17k, 19,500+, nearly 20,000); "20–24 hours" to metros.
10. **Unpublish or rewrite:** `alphonso-mango-in-new-zealand` (2024 dates, "now arriving", links to other domains), `cherry-price-in-india` (off-topic, founder placeholder), `mango-season` (whole 2026 season article), `best-fruit-for-building-muscle` and `health-benefits-of-black-raisins` (garbled text), `ratnagiri-hapus-price-guide` (leaked AI line, stale tables).
11. **Hindi / Gujarati translations of the spongy-tissue article** still carry the old scanner claims. Clear them?

## 2. Visible leftovers that should be fixed (high impact)
- **Founder placeholders visible to readers:** `hapus-amba-in-marathi-v2` ("[FOUNDER: …]", also an English sentence inside Marathi text), `kesar-mango-peti`, `hapus-aam-v2`, `hapus-amba-peti-what-is-inside-a-mango-box` (three notes), `jaiphal-nutmeg-uses-benefits-buying-guide` (two), `keri-no-ras-aamras-recipe`, `cherry-price-in-india`. Also `VIDEO_ID` and "Replace SHORT_ID" in `best-devgad-mango-online-order-now` (embed and video schema).
- **Leaked AI text at the top:** `ratnagiri-hapus-price-guide`, `mango-rate-in-pune-sweet-deals-unveiled`, a stray paragraph in `best-website-to-buy-devgad-alphonso-mangoes-online`.
- **Links to Google search pages instead of your pages:** `best-mangoes-in-pune-order-online` (including the contents links), `order-ratnagiri-hapus-amba-online`, `buy-ratnagiri-hapus-amba-mango-bliss-from-konkan`, `mango-rate-in-pune-sweet-deals-unveiled`.
- **Broken or wrong links:** `goa-cashews` (stray %20 in two links), `healthy-dates-khajur` (`aphonsomango.in`), `hapus-mango-ratnagiri` (malformed `https:/`), links to other domains in `discover-the-best-ratnagiri-hapus-store-online`, `order-alphonso-mango-online-top-10-reasons-to-indulge`, `alphonso-mango-in-new-zealand`, `discover-the-best-seasonal-fruits-for-every-time-of-the-year` (zamaorganics.com).
- **Typos and garbled text:** "Proashant Powle" (`alphonso-mango-online-mumbai`), "a brand of Powle Home Foods The operation" (`dried-figs-nutrition-facts`, `lucknow` article too), "Buy Buy Kesar Mango Online Online" (`kesar-mango-peti`), "It’It'scked with vitamins" (`mango-for-dessert`), garbled phrases in `indian-mango-online`, `best-fruit-for-building-muscle`, `health-benefits-of-black-raisins`; broken styles `border:1dd`, `border:1pxonso`, `border:1px dd`.
- **Buy Now / Order Now buttons and "order before the season closes" lines on out-of-stock mangoes** (fresh mangoes are out of stock until 1 Feb 2027): `mango-reseller` (cards say "In Stock"), `alphonso-mango-in-gurgaon`, `online-mango-delivery-in-jaipur`, `buy-mango-online`, `mango-home-delivery`, `hapus-mango-in-delhi`, `lucknow` articles, `alphonso-mango-nagpur`, `mango-leaves`, `mango-for-infants`, `mango-tree-lifespan`, `amrakhand-mango-shrikhand`, `iron-in-mango-uncovering-the-best-source-of-iron`, `fresh-mango-near-me`, `online-mango-purchase`, `unlocking-the-power-of-mango-for-health` and many more.
- **Lines that still read as "available now":** "Two varieties are available … right now" (several city articles), "We are currently shipping A+ Grade Alphonso" (Gurgaon), `mango-season` ("season is officially here").
- **Cards still saying "season opens March 2025/2026":** `origin-of-hapus` (two), `nutrition-facts-about-mangoes` (two), `authentic-ratna-alphonso-mango-buy-online`.
- **Not pre-order but close:** "join the waiting list" / "register for notification" style lines, "Diwali advance booking" (`alphonso-mango-gift-box-online-corporate-personal-gifting-2026`), "Orders placed outside March–June … confirmed for the next season" (`mango-is-our-national-fruit`, `benefits-of-mango-leaves`).

## 3. Stale year and season wording still in articles
- **2026 in titles or headings:** `indian-mangoes-for-export`, `apeda-certified-mango-exporters-india` (several "2026" sections), `alphonso-mango-exporter-mumbai` and `how-to-export-mango-from-india` ("Order 2026 Alphonso Mango Export Mumbai"), `devgad-mango`, `devgad-hapus`, `calcium-in-mango-unveiling-nutritional-facts`, `mango-for-acid-reflux`, `discover-ratnagiri-alphonso-mango-price-varieties`, `buy-mango-peti-online-v2`, `price-of-dates-per-kg-v2`, `alphonso-mango-price-in-2024`, `body-building-diet` (2025), `aam-mango-the-exquisite-taste` and others.
- **Season windows that conflict with "season starts 1 February 2027":** "March–June", "April–June", "mid-March to mid-June", "Not available July through February/March/January", "restocks March onwards" (hundreds of mentions). Suggest one template sentence for all.
- **"Updated 29 / 30 September 2026", "Updated 1 October 2026" lines.**
- **Schema:** `priceValidUntil` 2026-12-30 and `dateModified` 2026-06-30 in schema blocks across dozens of articles; products marked InStock or at old prices while fresh mangoes are out of stock (`buy-ratnagiri-hapus-online`, `best-devgad-mango-online-order-now`, `discover-ratnagiri-alphonso-mango-price-varieties`, `devgad-hapus`, `devgad-mangoes-in-mumbai-delicious-delight`, `mango-tree-height`, `how-to-identify-authentic-hapus-mango`); cashew InStock flag in `a-guide-to-storing-mangoes`.
- **Press and lab dates:** "Economic Times June 2026" interview mentions in many articles and an "April 2025 / 5 April 2025" residue report (some articles say 1 April 2025); "The 2025 season was difficult" paragraphs. Confirm what is true and make them consistent.
- **Conflicting product facts:** Kesar "ripe in July" (`authentic-kesar-amba-online-taste-the-difference`), Alphonso compared to "a banana at 18 to 24 °Brix" (`why-mango-is-called-king-of-fruits`), Devgad Brix 16–22 vs 18–24, "hot-water treatment" no / yes across articles, Devgad vs Sindhudurg.

## 4. Hard-coded prices (should become live tokens or be removed)
`mango-wholesale` (both blogs), `a-guide-to-storing-mangoes`, `aam-papad-recipe`, `mango-fruit`, `alphonso-mango-price-in-india` (three different ranges in one article), `mangoes-online-bangalore`, `mango-online-rate`, `aam-churan-amchur`, `hapus-mango-rate-online`, `how-many-mangoes-in-1-kg`, `iron-in-mango-uncovering-the-best-source-of-iron`, `alphonso-mango-in-bhubaneswar`, `buy-hapus-ratnagiri-online`, `how-to-identify-authentic-hapus-mango` (InStock ₹1200), `body-building-diet`, `cost-of-alphonso-mangoes-in-mumbai`, `mango-for-sale`, `best-fruit-for-building-muscle`, and the schema offers in many articles. Delivery claims in these also differ.

## 5. Delivery wording that differs from your single delivery rule
Approved text: "Orders placed before 12 noon IST (Monday to Saturday) are dispatched the same day. Delivery takes 1 to 3 days for most PIN codes and 1 to 2 days to most metros, depending on your PIN code."
Differing versions found across articles: cut-offs of 10 AM, 11 AM, 2 PM, 3 PM, 4 PM; "weekdays" or "business days"; "20–24 hours" to metros; "same-day dispatch"; "next-day delivery"; "5 to 10 days" international. No article carries the exact sentence except those written from your template.

## 6. Waitlist or notify wording left on purpose
"Notify me" and "sign up for restock alerts" prompts were left because they are notifications, not pre-orders (for example `mango-poha`, `buy-mango-online-fresh-mangoes-for-sale`, `mango-online-chennai`, `lucknow`). Say if you want them removed too.

## 7. Items outside the article pass that are still open
- **v7 theme** ("HOME SEO v7 - Season 2027", unpublished, id 164738924801) is ready for you to publish. After publishing, run the Rich Results Test on `/blogs/how/how-to-ripen-alphonso-mangoes-at-home` and open Devgad and Kesar product pages to check the live price table.
- **Homepage countdown:** `templates/index.json` has `end_date` "2026-06-03" (check whether it is still displayed).
- **Page content:** "free delivery" in several schema FAQs in `global-schema.liquid`; `llms-full` has internal notes and conflicting founding years; Delhi NCR and AI pages were updated.
- **Kesar and Devgad product pages:** NRI figures and hard-coded prices were removed; hard-coded "$27 / AED 99 / £21" is gone. Any `#pricing` links pointing to the old anchor will no longer scroll.
- **Inventory:** negative stock counts on mango variants must be reset before 1 February 2027.
- **Mango SEO Agent:** the blog queue (`docs/blogqueue-commercial-keywords.csv/.json`) is not imported; I need the agent folder as a zip or a sample queue file.
- **Semrush:** exclude `wa.me` from the audit; USD/AED price conversions; the "Pairi ₹2,799" line.
- **Core Web Vitals:** all 11 measured pages fail on mobile (saffron product page worst); needs a PageSpeed report to find the slow scripts.
- **Indexing:** `/pages/horeca` is unknown to Google; request indexing and link it from the footer; re-run inspection for `/blogs/hapus/devgad-mangoes` (network error).
- **Not scanned:** blogs other than "how" were scanned in this pass (978 articles in 53 blogs); product descriptions beyond Devgad and Kesar and collection pages were not.

## 8. Findings added from the last batches (B23, B26, B27)
- **More pass / subscription links:** `alphonso-mango-shop-near-me-best-deals-in-town` links "Alphonso season" to `/pages/monthly-pass` (same page as in `devgad-mangoes-in-mumbai-delicious-delight`). Does `/pages/monthly-pass` exist?
- **Named person:** `mango-fun-facts`, `alphanso-mango` and several others name Prashant Powle personally. Confirm that is intended (the partner farm is not named anywhere).
- **Judgement calls in the pass:** `mango-puree` ("Pawas, Velneshwar, and 46 further Konkan villages" now "…and other Konkan villages"); `aamrai-mangoes` ("48 such orchards" drop); `alphonso-mangoes-in-the-box` and a few waitlist cards changed to the 2027 line; `dasheri-mango` lost a garbled "₹0 … 47,961 customers" sentence; `mango-wholesale` lost its waitlist sentences.
- **Typos and garbled text still live:** "revolurevolutionizedapus", "wibroadeach", "aa loyal" (`best-quality-mango-delivery-online-order-now`); "Powle Home Foods, a brand under Powle Home Foods We hold" (several); unfinished sentence "This section is a " (`alphanso-mango`); `border:1pxindo` (`why-alphonso-mango-is-costly`).
- **Prices and season text still stale in:** `why-alphonso-mango-is-costly` (11 a.m. cut-off, "dispatch our first box in November", 2026 price dates), `mango-puree` ("opens April 2025" twice, "We do not ship July through March"), `aamrai` (₹599–₹1,699), `mango-delivery-in-mumbai` and `alphanso-mango` (April–June, "Order by mid-May", 10 AM cut-off), `mangos` ("Season: February to June" next to a March–June voice answer), `mango-in-the-third-trimester` ("We do not ship July through January"), `mango-modak` (availability April–June).
- **Notify-me wording left on purpose:** `mango-delivery-in-mumbai`, `alphanso-mango`, `mango-modak`, `sweet-and-juicy-mango-madness-unveiled`.
- **Delivery wording:** more differing versions ("next-day delivery", "same-day delivery before 12:00 noon", "weekdays with a 12:00 noon cut-off") in `order-fresh-mango-in-delhi-online-now`, `mangos`, `mango-fun-facts`, `mango-delivery-in-mumbai`.

## 9. Final totals
- Articles scanned: 978 in 53 blogs; 490 matched.
- Named 26: 25 edited; 1 (Season Pass) waiting for your decision.
- Wave A (pre-order wording): 217 articles, all written.
- Wave B (village count only): 247 matched; 246 written, 1 false match (`fresh-blueberry-price-per-kg`), plus 3 waitlist or pre-register fixes found in wave B (`alphonso-mangoes-allahabad`, `mango-delivery-by-post-office`, others) done.
- Retried after approval prompts: `dry-fruit-store-near-me`, `devgad-alphonso-mangoes-online-mumbai`, `mango-for-breakfast`, six articles in B13: all written.

## 10. Findings from batch B28 (last batch)
- `mango-online-mumbai`: all four product cards say InStock in schema; "same-day or next-day delivery"; a "(2025)" price table.
- `mango-festival-in-mumbai`: title says "2024"; "Two products below are available right now" while Amba Wadi is out of stock; "Notify Me" button; "Order before the season ends"; broken style `border:1pxdd`; "Orders placed in July or later will not be fulfilled".
- `authentic-ratnagiri-alphonso-mango-online-order-now`: "free shipping in big cities", "next-day delivery", "usually from March to May", "Buy ... before stocks run out", widget products with empty src and title, author heading "Bhimseni Kapoor" while the author card says Prashant Powle.
- `alphonso-mango-online-coimbatore`: "Buy Now" on a card that says "Currently out of stock"; Kesar and cashew offers valid until 2026-12-30; "Delivery in 1–3 days"; season text "late February to mid-June" vs "February–May" in its table.
- `almonds-empty-stomach`: voice answer says "roughly 84 calories" while the body says about 98–100 kcal.

## 11. Combined rebuilt-article pass (C01 to C55 and E01 to E17), finished 9 October 2026

Scope: every article that needed the 48-villages restore, the season wording, button/availability, live price token, delivery sentence and placeholder fixes. First pass C01 to C55 (about 490 articles) and the season-only pass E01 to E17 (150 articles, some skipped as non-mango). All writes went straight to Shopify through articleUpdate. No theme was published.

How it was checked: each written body was re-queried and compared with the intended text by script (whitespace and non-breaking spaces ignored), every ld+json block parsed after swapping price tokens for numbers, tag balance and class-attribute sequences were checked. Batches that could only be read through at first (C21, C24, C31, C32, C34, C36 to C39 and a few single articles) were re-scanned by script afterwards.

### 11.1 Articles that need a decision or a rewrite
- `alphonso-mango-myths-facts` (592663773441): the original already starts mid-sentence; voice answer, contents and intro are missing. Not touched.
- `alphonso-mangoes-in-amritsar-punjab` (383615205422): original has a fragment after the ld+json and is missing the intro, contents and product section. Not touched.
- `how-to-make-mango-pulp` (the original, not v2): table header (`<table>`/`<tr>`) missing at the start. Preserved as found.
- `alphonso-mango-in-new-zealand`, `cherry-price-in-india`, `best-fruit-for-building-muscle`, `ratnagiri-hapus-price-guide`: on the earlier unpublish-or-rewrite list; they were cleaned with the same rules but still need your decision.
- `test-a`: looks like a test page; consider unpublishing.
- `mango-for-pcos` (590408...): the live body had been replaced after the earlier pass by a shorter rewrite; the pass was applied on top of that version.
- Several other live bodies had been rewritten between the earlier pass and this one (for example `hafooz-mango-premium-quality`, `buying-farm-fresh-mangoes-online`, `mango-price-in-delhi`); the live body was used as the base each time.

### 11.2 Facts that still conflict with "48 coastal villages"
- Breakdowns that do not add up to 48: PCMC (14 + 13 + 24 + 5), Dubai (11 + 20 + 17 + 9 + 13), Cuttack (45 other villages, derived), green-mango-online-delivery (5+9, 5+8, 5+19, 2+3), buy-alphonso-mango-online (about 51 names listed).
- Other village numbers left: 11 / 14 / 16 / 17 / 18 / 19 / 20 / 21 / 24 "other villages", "50+ other villages" (taste-the-best, mumbai-mango-market, pudding), "80+ sustainable villages" (exporters), "98 villages across Devgad taluka" (devgad-hapus).
- Tamil, Hindi, Marathi and Gujarati articles: numbers changed only; the "Sindhudurg" wording in the Tamil one is unchanged.

### 11.3 Delivery wording still contradicting the approved sentence
- "15,000 to 17,000 serviceable pin codes", "19,000+", "20,000+", "500+ / 900+ additional pin codes", "300+ via BlueDart": mostly removed where inside replaced sentences; still present in cherry-fruit-online (5), alphonso-fruit, alphonso-mango-online-jaipur/aurangabad, mangoes-processing-and-packaging, indian-mango-varieties, best-places-to-buy-mangoes-online and several others.
- "Harvested and shipped within 24 hours", "48 to 72 hours of harvest", "same day dispatch" style lines are kept as supply-chain facts and need a decision.
- ld+json headlines and breadcrumb names that mirror titles still say "1-3 Day Delivery", "Delivered 1-3 Days", "Next Day ...", or carry hard-coded "from ₹1,849"; titles were left alone.
- Courier lists (BlueDart, Delhivery, Ekart, XpressBees) remain beside the Blue Dart sentence in a number of articles.

### 11.4 Prices and tokens
- `data-price` and `data-price-max` card attributes are still hard-coded in many articles. In a few (buy-alphonso-mangoes-online-v2, amrakhand-mango-shrikhand-v2, ratnagiri-alphonso-mangoes-v2, aamras-recipe-v2, buy-premium-kungumapoo-saffron...) they were switched to price tokens. This sandbox cannot reach the public site, so please check one rendered page: if tokens inside attributes do not render, those attributes must go back to plain numbers.
- Tokens inside ld+json strings (lowPrice / highPrice) are used widely; same check applies (view page source on one product article).
- Devgad ld+json `lowPrice/highPrice` 1849 / 5499 still hard-coded in a few articles where only Ratnagiri was mapped. Kesar 999 / 1699 likewise.
- "half dozen" wording remains in several places while the first variant (token :1) is one dozen.
- Pairi ₹2,799 and similar single-variety prices not mapped.
- Non-mango prices left on purpose: cashew, chia, flax, pulp, saffron, nutmeg, dates.

### 11.5 Season and stock wording left on purpose
- Kesar, Pairi, Dasheri, Langra, Chausa, Malawi windows ("March to June", "May to July", "April to June") were not touched.
- Peak or harvest statements ("peak March to May", "first fruit mid-March", "Late March") were kept as Alphonso harvest facts; some now sit beside a 1 February start.
- "Add to cart" steps remain in many how-to-order lists; "Notify me" buttons and "Currently out of stock" lines remain in a few; frozen-alphonso-mango-candy still has an Aamras waitlist card.
- "Order Now" remains inside the Devgad product title (ld+json, alt text, filenames).
- Past-season text (2025 and 2026 reports, Economic Times June 2026, April 2025 lab report) was not relabelled.
- Typos kept as found: "Proashant Powle" (alphonso-mango-online-mumbai), "border:1px dolor #ddd", "border:1pxonso", "padding:0.6vim", "Powle Home Foods We hold".

### 11.6 Small things changed beyond the plain rules (worth a glance)
- cost-of-alphonso-mangoes-in-mumbai: phone +91-9167-401-401 replaced by +91 70830 75556; "Last Verified March 2026" set to 8 October 2026.
- alphonso-mango-gift-box-...-2026: Mother's Day set to May 9, 2027; gift-box prices replaced by "See the current price on the product page"; delivery table replaced; "Diwali advance booking" removed.
- delivery-period-for-mangoes: region-by-region transit list replaced by the approved delivery sentence.
- alphonso-mango-price: transit-time table removed; several articles had transit lists removed.
- mango-fruit-online-purchase and similar: leaked "Here is the completely cleaned..." lines removed (exclusive-deals, ratnagiri-hapus-price-guide, best-website-to-buy-devgad...).
- `[FOUNDER: ...]` paragraphs removed from cherry-price-in-india, hapus-amba-in-marathi-v2, kesar-mango-peti, akrod-akhrot-walnut, keri-no-ras, blueberries-online, uric-acid guide and others.
- Malawi price tokens used on best-mango-in-the-world card and ld+json.

### 11.7 /pages/horeca (published 9 October 2026)
- Fresh-mango offers set to OutOfStock, valid until 2027-06-30; delivery wording replaced with the approved Blue Dart sentence; hotel names (The Oberoi, The Trident, JW Marriott, Taj Group of Hotels) added with "supplied to" wording; cards show "average price ₹600 per kg (contact for final contract rates)".
- Client purchase orders are confidential and are not stored in the repo or shown on the site.
- Open: schema `shippingRate` 0 (free shipping) on each offer is still unconfirmed; page template `luxury-mango-dessert` is not in the live theme, so the page uses the default page template - check how it renders; hero image `Alphonso_mango_in_Hotels.png` should be checked for logos.
