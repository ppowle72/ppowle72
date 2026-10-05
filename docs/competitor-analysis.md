# Competitor homepage comparison (verified 5 Oct 2026)

**Update:** network access to competitor sites now works, so this section replaces the earlier "blocked/unverified" notes. Every homepage below was loaded in a headless browser (JavaScript executed) and its headings, word count, schema and on-page elements were read directly. Full H1 to H6 outlines for all 16 sites: `competitor-homepage-headings.md`. Keyword positions from your SEMrush exports are in the second half of this file.

Not reachable: aamwalla.com (origin error 522), konkanbag.com, ratnagirimango.com, ratnagirihapus.in, madhurambruhat.com, kokanheart.com, and `ratnagirhapus.store` (typo; the real site is ratnagirihapus.store). mangobazar.in is a parked domain. `ratnagirialphonso.com` is **your own blog** (author Prashant Powle), not a competitor.

Not mango competitors, ignore for benchmarking: konkanfoodbazar.com (Konkan snacks), foodwalas.com (sweets marketplace), agrophonics.com (imported frozen fruit).

## What each direct competitor's homepage does
| Site | H1 | Words | Schema found | Notable on-page elements |
|---|---|---|---|---|
| **rqdfarm.in** (strongest) | Buy Fresh Alphonso Mangoes Online Directly from the Farm | 2,075 | Product, AggregateRating, FAQPage, LocalBusiness, Organization, WebSite | 28 H2s, order steps, FAQ, 16 cities named, "no carbide" and "naturally ripened" repeated (11 times each), GI mentioned 10 times; H3 sections for Ratnagiri, Devgad, gift boxes, bulk and corporate orders, mango products; also sells Dasheri and Gir Kesar |
| **aamrai.com** | Buy Organic Alphonso Mangoes Online, Order the Best Ratnagiri Alphonso (Hapus) Mango with Home Delivery across India | 938 | Article, WebPage, Organization (minimal) | H2 "How to Identify Original Alphonso Mango" with H3s "Chemically Ripened Mango" and "Naturally Ripened Alphonso"; "organic" used 16 times; meta mentions GAP-certified farms |
| **ratnagirihapus.store** | Alphonso Mango Pulp | 1,107 | Organization, WebSite, SiteNavigationElement | 52 H2s (mostly product titles), prices and star ratings on cards, press logos, 10 video testimonials, 10% first-order code |
| **dhanshefarm.com** | Get Your Aam Directly From Farm (the H1 appears twice) | 556 | none found | JavaScript app; H2s: Choose Your Perfect Pack, First-Time User Offer, Taste the Real Alphonso This Season, Loved by Customers, Ethical & Responsible Farming; H3 "2,500+ Happy Customers"; title tag is just "Dhanshe's Farm" |
| **devgadmango.com** | 100% Authentic Devgad Alphonso Mangoes | 557 | none | H2 "100 + Cities We Serve, all over India" naming 15 cities; H3 "How to Identify Original Devgad Alphonso Mango?"; no meta description |
| **ratnagirifarms.com** | The Real Alphonso. Straight From Our Farm. | 343 | none | "Grown with Care, Not with Chemicals"; FSSAI mentioned; no schema |
| **kriparamfruitwala.com** | no H1 | 1,177 | Product, AggregateRating, GroceryStore, MerchantReturnPolicy | H3 "40 Years of Service", "20k+ customers", corporate clients, gift baskets, 12 cities named |
| **devgadhapoosamba.com** | From. Farms of Devgad Jamsande! | 548 | Article, Organization (minimal) | Boxes by the dozen ("10 Dozen (120 Fruits)", minimum 5 dozen), H3 delivery to Mumbai, Navi Mumbai, Thane, Kalyan Dombivli |
| **thehapusamba.com** | The King of Mangoes | 144 | none | Peti boxes of 5 to 8 dozen listed by fruit size (251 g down to 175 g) |
| madovermangoes.in | none | 121 | Organization, WebSite | Thin page; "Chemical free mangoes", "Original Alphonso" |
| ratnagirialphonsomango.com | none | 619 | Organization, WebPage | Generic store; GI mentioned 6 times |
| maldamango.com | none | 972 | FAQPage, LocalBusiness | Noida store, long educational H2s, 22 H4 FAQ questions; not Alphonso-focused |

## Where alphonsomango.in stands after this PR (our figures are from the theme source, not a render)
| Element | alphonsomango.in | Competitor range |
|---|---|---|
| H1 matches the buying keyword | "Buy GI Tagged Alphonso Mango Online in India" (staged) | rqdfarm, aamrai, devgadmango do; ratnagirihapus.store does not |
| Words on homepage | about 1,750 (template text plus new sections, excluding product cards) | 121 to 2,075; only rqdfarm is comparable |
| Direct-answer block | yes | none have one |
| FAQ with FAQPage schema | 10 questions, markup matches the page | rqdfarm, maldamango, agrophonics only |
| Order steps | yes (3 steps) | rqdfarm only |
| Live price table / per-kg | yes | none |
| Ratnagiri vs Devgad comparison table | yes | none |
| "How to identify original Alphonso" | yes (added) | aamrai and devgadmango |
| Cities named | 11 (from your order data) | rqdfarm 16, devgadmango 15, kriparam 12 |
| Schema | Organization, WebSite, LocalBusiness, ItemList, WebPage, FAQPage | Product and AggregateRating only at rqdfarm and kriparamfruitwala |
| Press logos, video testimonials, customer-count trust band | **no** | ratnagirihapus.store (press, video), dhanshefarm ("2,500+"), kriparam ("20k+", "40 years") |
| Gifting / bulk / corporate section on the homepage | yes (added) | rqdfarm, kriparam, ratnagirihapus.store |

## What was added because of this comparison
1. **"How to identify original Alphonso mango"** section (origin and licence, aroma, colour, feel and size, pulp), as aamrai and devgadmango do. Uses your own GI and FSSAI numbers.
2. **H1 changed** to "Buy GI Tagged Alphonso Mango Online in India" (staged).
3. A short "Gifting and bulk orders" block linking the gifting, business-partnership and reseller pages (all three exist).

## What I did not add, and why
- **"Organic" claims.** Aamrai says GAP-certified and uses "organic" 16 times. Your theme says chemical-free and carbide-free only. Do not say organic without certification.
- **Customer-count trust band.** Your Shopify data supports it (8,215 orders and 5,896 customers over the last three years, 8,163 of those orders in India), but counts can include repeat orders and gifts. Tell me the wording you want ("5,800+ customers" or similar) and I will add it.
- **Press logos and video testimonials.** Need real material from you.
- **Offer codes** (ratnagirihapus.store's 10% code, Dhanshe's first-time offer). Your decision.


## Dhanshe Farm backlink profile (Ahrefs export, 5 Oct 2026)
Source: your `dhanshefarm.com-backlinks-subdomains` export (1,146 backlinks, each from a different referring host). Decoded from the damaged export; classification below is my heuristic (anchor text and page titles that mention backlinks, guest posts, DR/DA, PBN, SEO services, plus link-seller domains), so treat the percentages as approximate. Lists: `dhanshefarm-backlink-domains.csv` (all hosts) and `dhanshefarm-backlinks-nonspam.csv` (the 39 non-spam links).

| Measure | Result |
|---|---|
| Backlinks | 1,146 from 1,146 different hosts |
| Pointing at the homepage | 1,140 (99.5%) |
| Link-seller / auto-generated "domain report" pages | about 1,107 (97%), median Domain Rating 0.7 |
| Other links | 39 |
| HTTP status of linking pages | 964 OK, 175 redirects, 4 not found |

**What the 39 real links are:** app-store and app-directory listings (appbrain.com, indusappstore.com, chrome-stats.com, appshunter.io), brand and store directories (brandfetch.com, storeleads.app, "Wix Stores in Nagpur"), a scam-checker page (scam-detector.com), a Google link (google.co.in, DR 91), a wedding-menu article (weddingaffair.co.in) and a Hindi film article (thereviewgeek.com, probably an unrelated mention), plus a few domain-listing sites. There is **no news, press, blog or editorial coverage** of dhanshefarm.com in the profile.

**What the spam links look like:** pages from SEO-service sites (SEOExpress, many `.shop` and `.click` domains with names like "ranklinkpro" and "buyseobacklinks") whose text is a template with the site's name inserted ("Grow Organic Search Traffic with High Quality SEO Links dhanshefarm.com", a fake testimonial repeated 342 times). Those are not links Dhanshe chose; they appear when a site's name is submitted to or scraped by link-selling tools. Some of them may have been bought. Either way they carry almost no value and can carry risk.

**What this means for us**
1. Dhanshe Farm's #1 position for "hapus mango online" is **not** explained by a strong editorial link profile. Its real links are app-store listings and directories. Possible helpers I cannot verify from here: its app, Google Business Profile or local signals (it is based in Nagpur), brand searches, and low competition for that exact phrase (keyword difficulty 22).
2. Do **not** copy its link-building. Bulk link-seller pages are exactly what Google's spam systems discount or penalise.
3. Our link position is better in kind if the press coverage you listed is real and links to us: editorial links from news sites are worth more than all of Dhanshe's 1,107 junk links. Verify those, and see what Ahrefs shows for alphonsomango.in's own referring domains (not uploaded yet; send that export and I will compare the two properly).
4. Cheap, real wins that Dhanshe's genuine profile suggests: an Android/iOS app listing if you have an app, brand-asset listings (Brandfetch), and complete business-directory profiles.

## One finding that doesn't fit the on-page story
dhanshefarm.com ranks first for "hapus mango online" (about 750 est. visits), yet its page is a JavaScript app with a short title ("Dhanshe's Farm"), no schema and 556 words. Its backlink profile (section above) is 97% link-seller spam plus a few app and directory listings, so neither on-page work nor links clearly explains the rank. Treat it as unexplained and do not copy its tactics.

## Your own site: ratnagirialphonso.com
Its homepage uses H6 for 88 post titles and H4 for 22 other items, with only two H2s. That is a heading-structure problem worth fixing in that theme, but it is outside this PR.

---

# Earlier work (kept for reference)

## Earlier notes (superseded where they say "blocked")

## Read this first
Update: the homepage of **ratnagirihapus.store is now verified** from the page source you pasted (cached by the site on 3 Oct 2026). The other competitors are still unverified because the cloud environment's network policy blocks every competitor domain (rqdfarm.in, aamrai.com, foodwalas.com, devgadmango.com, ratnagirialphonsomango.com, ratnagirifarms.com) and Google's developer docs. Both `WebFetch` and `curl` were denied, and `WebSearch` returns only summaries, not People Also Ask boxes or AI Overview citations.

So **no competitor homepage was actually read.** There are no verified word counts, headings, schema types or on-page elements for any competitor. Everything below comes from search-result titles and snippets only, and is labelled that way. Nothing here should be treated as a measurement.

## Who surfaced (search results only)
| Site | Why it surfaced | Verified from snippets only |
|---|---|---|
| rqdfarm.in | Product pages for "order alphonso mangoes online" and "alphonso mango price per dozen"; city pages | Ratnagiri/Devgad Hapus, pan-India delivery, "no carbide" claim, size grades A/C/Jumbo with gram ranges, 4-dozen boxes, city URLs such as `/alphonso-mangoes/pune` and `/agra` |
| aamrai.com | Dominated "order alphonso mangoes online" and "buy alphonso mango online india", mostly through blog posts | GI-tagged Ratnagiri/Devgad, organic certifications named (NPOP, NOP, JAS), haystack ripening, buying-guide posts ("Dos and Don'ts of Buying Alphonso Mangoes Online", "Ratnagiri vs Devgad") |
| foodwalas.com | Separate Ratnagiri and Devgad product pages | GI tag, farmer-sourced, Devgad dozen from about ₹1,550 in a snippet |
| devgadmango.com | Devgad farmer co-operative; ranks for "how to identify real alphonso" and Ratnagiri vs Devgad | Blog-style content, Devgad origin |
| ratnagirialphonsomango.com, ratnagirifarms.com, agrophonics.com | Appeared only for an extended search | Titles only |

alphonsomango.in itself surfaced for "buy alphonso mango online india" and "alphonso mango online" through a blog post and `/collections/mangoes`.

## What the search evidence does support (patterns, not homepage facts)
1. **Informational content earns commercial-query visibility.** aamrai.com's visibility for "buy alphonso mango online india" is mostly blog URLs: buying guides and comparisons.
2. **Grade-specific product pages.** rqdfarm.in puts size grade and gram range in product titles and URLs.
3. **Origin-specific product pages.** Foodwalas and AAMRAI split Ratnagiri and Devgad into separate pages. We already do this (`/products/ratnagiri-alphonso-mango`, `/products/devgad-alphonso-mango`).
4. **City pages on one URL pattern.** rqdfarm.in uses `/alphonso-mangoes/{city}`, including smaller cities.
5. **Certification-led trust copy.** GI (Foodwalas), organic NPOP/NOP/JAS (AAMRAI), "no carbide / naturally ripened" (RQD, AAMRAI).
6. **Content gap:** "difference between ratnagiri and devgad hapus" returned weak results in search, so a clear answer page has little competition.

## Where this leaves the homepage (our side is verified from the Shopify theme)
| Element | alphonsomango.in after this PR | Competitor status |
|---|---|---|
| Visible prices | Live per-dozen table by size | not verified |
| Ratnagiri vs Devgad comparison + verdict | Table + FAQ answer | AAMRAI/Devgad Mango/RQD rank with blog posts on it |
| FAQ | 10 visible questions, matching FAQPage JSON-LD | not verified |
| Order steps | 3-step block | not verified |
| City section | Six metros named, free delivery | RQD has per-city pages |
| Certifications on page | FSSAI, APEDA, GI AU numbers in body text | GI/NPOP claims in snippets |
| Grade/size detail | Size ranges in the price table | RQD puts grades in URLs |

## What we are still missing (gaps worth building)
1. **City landing pages** (`/pages/...` or blog posts) for Mumbai, Bangalore, Chennai, Kolkata, Delhi, Hyderabad, each with local delivery time, price table and FAQ. The homepage only has one paragraph. The theme already has city blog templates in the schema, so check what exists before adding more.
2. **A standalone "Ratnagiri vs Devgad Alphonso" article** targeting "difference between ratnagiri and devgad hapus" and linking back to the homepage table.
3. **A "how to identify real Alphonso" buying guide** (competitors rank for this; we have the GI authorisation numbers to back it).
4. **Grade/size detail in product titles** (e.g. gram range in the product title) as RQD does.
5. **Pre-order / season-alert capture** while fresh fruit is out of stock. I did not add this because I don't know if you take pre-orders.

## To get the real homepage comparison
Choose one:
- **Allow the domains.** In the cloud environment menu in the session title bar, choose Edit, then Network access. Either broaden access or use Custom and add the competitor domains plus Google's developer docs under Allowed domains, keeping the default package-manager list. See https://code.claude.com/docs/en/cloud-environments#network-access. Then ask me to re-run it.
- **Paste data.** View-source HTML of each competitor homepage, or a Screaming Frog crawl export, and I will fill in headings, word counts and schema types.


---

## Verified: ratnagirihapus.store homepage (from the HTML you pasted)
Platform: WordPress + WooCommerce + Elementor (Storefront theme), Yoast SEO, Schema & Structured Data for WP plugin.

| Item | What the page source shows |
|---|---|
| Title tag | "Alphonso Mango Online Store \| Fresh Ratnagiri Hapus Delivered" |
| Meta description | "Buy fresh Alphonso mango online. Authentic Ratnagiri Hapus, GI-tagged, naturally ripened & delivered across India." |
| H1 | One H1, and it is "Alphonso Mango Pulp" (the first product block). The hero is image-only banners with no text. |
| H2 sections | "Get 10% Off On Alphonso Mango \| Use Code: MyFirstOrder", Shop By Category, Super Jumbo Alphonso Mango, Ratnagiri Alphonso Mango, Devgad Alphonso Mango, Ratnagiri & Devgad Alphonso Mango Peti, Kesar Mango, Ratnagiri Payari Mango, Customers Testimonials, Featured In, Blogs. Some blocks (cashews, "About" text, Konkan Tour) are hidden on every device. |
| H3 trust block ("Why Ratnagiri Hapus Store?") | Naturally ripened, no carbide; "20K+ Happy Customers" (yearly supply to 8000+ customers); delivery in 8K+ pincodes / 800+ cities and towns; delivery in 2 to 5 days |
| Prices on homepage | Yes, as ranges per product, e.g. Ratnagiri Small ₹1,949-3,899, Large ₹1,999-3,999, Jumbo ₹2,199-4,399, Super Jumbo ₹2,599-5,199; Devgad the same; Peti ₹7,999-8,999; pulp ₹600-1,200 |
| Stock | Fresh-mango products carry "Out Of Stock" badges right now (off-season), same as us |
| Ratings | Star ratings per product (4.6 to 5.0) from a reviews plugin |
| Trust | "Featured In" press logos (Lokmat, TV9 Marathi, Hello Entrepreneurs, The Startup Story); ten video testimonials; FSSAI 11524996000006; GI "AU/11054/GI/139/1264"; CIN; company named as DWBL Consumer Products Private Limited |
| Content | Three blog cards (July-August 2026), including "What is Alphonso Mango?" and "Alphonso Mango: Complete Guide" |
| Navigation | Footer links to "Alphonso Mango In Cities" hub, corporate gifting, export enquiry, mango pulp supply, recipes, mango news, FAQ, order tracking |
| Schema output | SiteNavigationElement, WebSite, Organization (legalName "Ratnagiri Hapus Store"). No FAQPage, Product, ItemList or LocalBusiness on the homepage |
| FAQ / direct answer / order steps / comparison table / city text on the homepage | None |

### Head-to-head with alphonsomango.in (after this PR)
| Element | alphonsomango.in | ratnagirihapus.store |
|---|---|---|
| H1 matches the main keyword | Yes ("Buy GI Tagged Alphonso Mango") | No (H1 is "Alphonso Mango Pulp") |
| Direct-answer block | Yes | No |
| Visible FAQ + FAQPage schema | 10 questions | None |
| Order steps | Yes | No |
| Ratnagiri vs Devgad table | Yes | Separate product blocks only |
| Live price table | Yes | Price ranges per card |
| City text on homepage | Yes (11 cities named) | Hub page link only |
| Press / media logos | **No** | **Yes** |
| Video testimonials | **No** | **Yes (10)** |
| Reviews/ratings shown on homepage | Judge.me carousel (check it renders) | Star ratings on cards |
| Customer-count and pincode claims | In footer/schema only | Prominent trust block |
| Blog cards on homepage | Yes | Yes (3) |
| Homepage schema | Organization, WebSite, LocalBusiness, ItemList, WebPage, FAQPage | Navigation, WebSite, Organization |

**Observation to check, not a conclusion:** the GI authorisation number "AU/11054/GI/139/1264" appears in ratnagirihapus.store's footer under DWBL Consumer Products Private Limited. Your theme notes attribute the same number to Proveda Superfoods Pvt Ltd. Please verify who holds it against the GI certificate before any page claims it.

### What this competitor shows we should add
1. **A "Featured in" press strip**, if you have real coverage to show.
2. **Video testimonials or a short customer video block.**
3. **A prominent trust band**: your own verified numbers (customers served, pincodes, delivery time). I used no counts because none are verified in the theme; supply the real figures.
4. **A cities hub page** linked from the footer and homepage (see below).

## Dhanshi Farms
I could not analyse it: its domain was not given and it is not reachable from this container. Send the exact domain (and paste the source, as you did for ratnagirihapus.store), or allow it under Network access and I will fetch it.

## Cities that actually order (your Shopify data, last 730 days, billing city)
Source: ShopifyQL on the connected store. Billing city is not always delivery city (gifts ship elsewhere). Spellings are merged below.

| Rank | City / cluster | Orders | Notes |
|---|---|---|---|
| 1 (tie) | **Bengaluru / Bangalore** | 740 | 636 "Bengaluru" + 104 "Bangalore"; the largest single city, level with the whole Delhi NCR cluster below |
| 1 (tie) | **Delhi NCR** (Delhi, Gurgaon/Gurugram, Noida, Ghaziabad, Faridabad) | 741 across areas | New/South/West/South West Delhi and Delhi 313; Gurgaon + Gurugram 256; Gautam Buddha Nagar 69; Ghaziabad 62; Faridabad 41. Billing records split NCR into many labels, which hides how big it is |
| 3 | **Mumbai + Thane** | 530 | Mumbai 357, Thane 108, Mumbai Suburban 65 |
| 4 | Hyderabad | 182 | |
| 5 | Chennai (+ Kanchipuram) | 143 (+45) | |
| 6 | Pune | 135 | |
| 7 | Kolkata | 91 | |
| 8 | Jaipur | 87 | |
| 9 | Ahmedabad | 58 | |
| 10-12 | Lucknow 50, Nagpur 44, Indore 40 | | |

By state: Maharashtra 949, Karnataka 918, Delhi 438, Haryana 367, Uttar Pradesh 343, Tamil Nadu 310, Telangana 295, West Bengal 208, Rajasthan 191, Gujarat 169.

**What changed because of this:** the homepage delivery text and FAQ now name Bangalore, Mumbai, Delhi NCR (Gurgaon, Noida), Hyderabad, Chennai, Kolkata, Pune, Jaipur and Ahmedabad, not just the six in the original brief. Gurgaon/NCR and Pune were missing, and Bangalore and Delhi NCR are the two biggest markets.

**City-page build order (best revenue first):** Bangalore, Delhi NCR/Gurgaon, Mumbai/Thane, Hyderabad, Chennai, Pune, Kolkata, Jaipur.

## How to allow the competitor domains
1. In Claude Code on the web, open the **cloud environment menu in the session's title bar** and choose **Edit**.
2. Open **Network access**. Either pick a broader access level, or choose **Custom** and add these under **Allowed domains**, keeping the default list of package managers:
   `ratnagirihapus.store`, `rqdfarm.in`, `aamrai.com`, `foodwalas.com`, `devgadmango.com`, `ratnagirialphonsomango.com`, `ratnagirifarms.com`, `agrophonics.com`, the Dhanshi Farms domain, and `developers.google.com`. Add `www.` variants if a site redirects to them.
3. Save. Docs: https://code.claude.com/docs/en/cloud-environments#network-access
4. **Start a new session** (or restart this one) so the container picks up the change. A test in this session right after your edit still showed every competitor domain blocked, so the new setting probably applies only to a fresh container. Then ask me to re-run the comparison.


---

## Update: SEMrush data for aamrai.com and dhanshefarm.com (homepage keywords)
Correction: the Dhanshe Farm domain is **dhanshefarm.com** (the earlier "dhanshifarms.com" was wrong). Source: the two SEMrush organic-position exports you uploaded (aamrai.com: 931 rows, dated Jul-Oct 2026; dhanshefarm.com: 320 rows, Sep 2026). I filtered to homepage URLs, matched them to our homepage positions (SEMrush organic and Ahrefs), and saved the full tables:
`competitor-homepage-keywords-aamrai.csv`, `competitor-homepage-keywords-dhanshefarm.csv`, `keyword-gaps-vs-aamrai.csv`, `keyword-gaps-vs-dhanshefarm.csv`.

Still not possible: reading either homepage (blocked), so their headings (H1 to H6), word counts and schema remain unverified.

### How the homepages compare on shared keywords
| | aamrai.com | dhanshefarm.com |
|---|---|---|
| Homepage organic keywords in the export | 102 | 61 |
| Homepage organic traffic (SEMrush est.) | about 900 | about 1,190 |
| Keywords where our homepage ranks higher | 44 | 30 |
| Keywords where they rank higher | 6 (mostly brand and tiny terms) | 9 |
| Keywords they rank for and we don't rank for on the homepage | 13 (mostly brand terms: amrai, mr mango; and raw/collector mango) | 8 (brand terms: savani farms, farmse) |
| Their best single homepage keyword | its brand term "amrai" (pos 3, about 310 visits) drives most of it; among buying terms, "order alphonso mangoes online" is pos 2 and about 50 visits | **hapus mango online, pos 1 (about 750 est. visits)** |

Dhanshe Farm's homepage earns most of its traffic from a few buying-intent Hapus phrases at positions 1-3. It is a small, focused page, and it outranks our homepage on those phrases.

### Where they beat our homepage (real buying keywords, not brand terms)
| Keyword | Volume | Their homepage pos | Our homepage pos | Our best page |
|---|---|---|---|---|
| hapus mango online | 1,600 | 1 (Dhanshe) / 7 (Aamrai) | not ranking | pos 1 on another URL |
| buy hapus mango | 590 | 1 (Dhanshe) | not ranking | pos 2 on another URL |
| order alphonso mangoes online | 590 | 1 (Dhanshe) / 2 (Aamrai) | not ranking | pos 4 on another URL |
| ratnagiri hapus | 1,300 | 3 (Dhanshe) | 8 | pos 1 on another URL |
| order mangoes online | 1,300 | 14 (Dhanshe) | 18 | pos 10 |
| best place to buy mangoes online | 320 | 11 (Dhanshe) | 17 | 17 |
| online mango delivery | 320 | 13 (Dhanshe) | 16 | 16 |
| farm fresh mangoes | 480 | 3 (Dhanshe) | not ranking | pos 65 |
| fresh alphonso mango | 210 | 1 (Dhanshe) | 2 | 2 |
| best alphonso mangoes in india | 140 | 3 (Dhanshe) | 7 | 7 |
| devgad hapoos | 1,900 | 6 (Dhanshe category page) | not ranking | 37 |

**What we added for these** (staged on the unpublished theme): "Hapus mango" in the order-steps heading, "buy Hapus mango online" and "best place to buy mangoes online in India" in the delivery paragraph, "online mango delivery", "premium Alphonso mangoes", and "Devgad Hapoos" in the comparison intro. The homepage should now compete for these instead of leaving them to other pages.

**What we did not add:** "organic mango" and "organic mangoes online" (390 to 1,900 searches). Our theme says chemical-free and carbide-free, not certified organic, and Aamrai holds organic certifications. Claiming organic without certification is a compliance risk. Also skipped: brand terms and tree/farm terms.

### Gaps that are not homepage work (site-wide, they rank top 10 for 500+ searches; we rank nowhere in the top 30)
- Aamrai: other varieties (chausa/chaunsa 8,100 and 4,400, malihabad and malihabadi 1,300 and 590, bambaiya aam 590) and non-mango products (cape gooseberry 14,800, Mahabaleshwar strawberry 3,600). These are range decisions, not copy fixes. If you sell or plan to sell Chausa or Dasheri, a collection page is the route.
- Dhanshe Farm: only one gap, "devgad hapoos" (1,900). It ranks at 37 for us; the comparison intro now names it.

### What this changes about the plan
1. We already lead on most core buying terms ("alphonso mango online", "buy alphonso mango", "mango online india", "mango fruit online"). Protect those, do not rewrite them.
2. Dhanshe Farm shows the value of a tight page. Its homepage is category-led (Ratnagiri and Devgad pages as `/products?category=...`) and ranks 1 for "hapus mango online" and "order alphonso mangoes online". We rank 1 and 4 for those on other pages, so the fix is to make the homepage carry the same wording and to internally link the better-ranking page, not to add a new page.
3. Check Hapus-phrase positions at 2, 4 and 8 weeks after publishing.
