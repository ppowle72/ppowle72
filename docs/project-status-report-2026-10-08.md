# alphonsomango.in SEO project: status report (8 Oct 2026)

Branch: `claude/homepage-seo-keyword-ranking-6in5p7` (PR #1 open, everything below that is in the repo is pushed). Live-store changes were made through Shopify directly; themes are never published from here.

## 1. Where the store stands right now
- **Live theme:** "HOME SEO v5 - HowTo removal" (checked just now).
- **Not published yet:** v6 and **v7 "HOME SEO v7 - Season 2027"**. v7 is the one to publish (it contains v6's HowTo fix plus the 2027 season schema, out-of-stock fresh-mango offers and the live price table for Devgad and Kesar).
- All page, product and article edits below are already live (they do not depend on the theme).

## 2. Done

### Theme and structured data
- Product schema: size, offer, price fixes for all products; city and area-served data for fresh mangoes; Grade and Country-of-origin properties; invalid JSON-LD (GSC "unparsable" and "missing size") fixed; empty FAQ shells and empty HowTo removed; LocalBusiness without address removed from 4 city articles.
- Season labels 2026 to 2027 in `global-schema.liquid`; fresh-mango offers marked out of stock until 1 Feb 2027 (in v7, not yet live).
- Live price tokens (`[[am:price:...]]`) for pages and articles; live price table on `/collections/mangoes`; buying-guide block on 6 product pages (Devgad and Kesar added in v7).
- robots.txt: filtered URL rule added. Delivery wording unified (one rule).

### Pages and products on Shopify
- AI pages (ai-commerce, ai-products, ai-faqs, NRI gifting, season page, ai-agent-navigation, llms, llms-full, Delhi NCR): prices now live tokens, "Season 2026" wording moved to 2027, season page keeps the 2026 harvest report and adds a 2027 opening notice.
- Products: 44 meta titles/descriptions plus 8 mango products updated; cashew grade metafield created; Devgad and Kesar descriptions: 2027 wording, hard-coded price tables removed, Kesar out-of-stock line and NRI figures corrected; mango cubes description fixed.
- Redirects created for two broken article URLs.

### Articles (978 scanned across 53 blogs, 490 needed a fix)
- **Pre-order, pre-book, waitlist and "pre-season booking" wording** replaced with: "The 2027 mango season starts on 1 February 2027, and fresh mangoes are out of stock until then." / cards "Out of stock until 1 February 2027": 217 articles in waves A01 to A24 plus the 26 you named (25 edited).
- **Unverified "48 villages" count removed:** 247 articles in waves B01 to B28 (246 written, 1 false match).
- Blocked or approval-held writes (nine articles plus later ones) were all retried after your approval and written.
- **FSSAI number corrected** in `devgad-hapus` (22110001060083 to 10020022011783, 5 places).
- **Stray WhatsApp number 91676 68899 removed** from `devgad-hapus-online` and `devgad-hapus` (replaced by +91 70830 75556). Kept numbers: +91 70830 75556 and +91 83690 48029.
- Spongy-tissue article reworded; 4 city articles lost LocalBusiness; several articles got hidden `<!---->` markers stripped.

### Research and plans (in `docs/`)
- Product SEO audit and 44 meta proposals, Semrush keyword plan (408 keywords), Ahrefs DR/UR improvement plan, disavow candidates (193 domains), Semrush site-audit triage, blog queue for the Mango SEO Agent (64 clusters, 7 batches), Blue Dart delivery coverage (4,769 PINs), article cleanup list.
- Mango SEO Agent indexing report read: 98 of 100 inspected URLs indexed; core web vitals fail on mobile for all 11 measured pages.

## 3. Pending: decisions only you can make
1. **Publish theme v7** (then run the Rich Results Test on `/blogs/how/how-to-ripen-alphonso-mangoes-at-home` and check the Devgad and Kesar product pages).
2. **Season Pass / subscription:** `/pages/monthly-pass`, the Season Pass article and the subscription-box article are published, but no pass product or subscription plan exists, so nothing can be bought. My suggestion: prepaid Season Box opening 1 Feb 2027. Need: unpublish now or later; prepaid box or true subscription; weeks, dozens per delivery, discount.
3. **"Mango Bonds for a 10% interest rate"** line in `fresh-alphonso-mangoes-home-delivery-near-me`: recommend removal.
4. **"organic" wording** (about 30 articles): reword?
5. **Claims to approve or remove:** customer counts (47,000+, 47,961), "since 2019/2020/2017", "55 villages" and other village counts, Kurla store, Narayan Peth store and "100 cities", About page store claim, "only GI-certified online store", "free delivery/shipping", pin-code counts, "20–24 hours", "real-time authenticity verification" WhatsApp line.
6. **Articles to unpublish or rewrite:** `alphonso-mango-in-new-zealand`, `cherry-price-in-india`, `mango-season`, `best-fruit-for-building-muscle`, `health-benefits-of-black-raisins`, `ratnagiri-hapus-price-guide`, `alphonso-mango-subscription-box-monthly-delivery-plan-2026`.
7. **Other open facts:** `devgad-hapus` also says "98 villages" and "45,000+ hectares"; Hindi and Gujarati spongy-tissue translations still carry old scanner claims; partner farm stays unnamed.

## 4. Pending: work I can do once you say go
- **Season wording clean-up in articles:** 2026 titles and headings, "March–June" seasons that conflict with 1 Feb 2027, "Updated September 2026" stamps, 2026 `priceValidUntil` and `dateModified` in schema, InStock offers on out-of-stock mangoes.
- **Buy Now / Order Now buttons and "available now" lines** on out-of-stock mangoes.
- **Hard-coded prices to live tokens** in about 20 articles.
- **Delivery wording** to the one approved sentence in articles.
- **Placeholders and typos:** "[FOUNDER: …]" notes, `VIDEO_ID`, leaked AI first lines, Google-search links in place of real links, broken links (`goa-cashews`, `healthy-dates-khajur`), garbled text.
- **Season Box** draft product and page, redirects, launch article.
- **Core Web Vitals:** needs a PageSpeed report for `/products/saffron-kesar` (mobile) to find the slow scripts.
- **Mango SEO Agent:** import the blog queue (needs the agent folder zip or a sample queue file; `E:\` path is not reachable from here).

## 5. Pending: needs a date or a person
- Before 1 Feb 2027: reset negative inventory counts on mango variants; replace "out of stock" messaging as the season opens; publish the Season Box if chosen.
- Semrush: exclude `wa.me` from the audit; USD/AED conversions; the "Pairi ₹2,799" line.
- Indexing: `/pages/horeca` unknown to Google (request indexing, link from footer); re-inspect `/blogs/hapus/devgad-mangoes` (earlier network error).
- Homepage countdown `end_date` "2026-06-03" in `templates/index.json`: check whether it still shows.
- Link building and DR plan (Razorpay, NDTV, Better India, CN Traveller, ET): outreach is yours; assets (price index, carbide test guide, season calendar) can be built by me.

## 6. Limits to know about
- Article edits were checked by re-reading or script comparison after writing; not every article got a byte-level diff (listed in the cleanup list). Hidden comment markers and some special spaces were normalised.
- Some early articles had anchor ids renamed (listed in the cleanup list).
- Hundreds of articles still contain stale 2025 or 2026 statements that I deliberately did not rewrite without your wording decisions.
- Full detail: `docs/article-cleanup-list-2026-10-08.md`.
