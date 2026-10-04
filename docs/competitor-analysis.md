# Competitor homepage comparison: what was verified and what was not

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
