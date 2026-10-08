# Blog queue: commercial and buying-intent keywords (for the Mango SEO Agent)

Files: `blogqueue-commercial-keywords.csv` and `blogqueue-commercial-keywords.json` (same content, 64 rows in 7 batches of 10, ordered by opportunity). Run one batch at a time. Source: Semrush Keyword Magic (India) joined to Ahrefs rankings, 6 Oct 2026.

## What is in the queue
- Only commercial and transactional keywords: price, buy, order, online, near me, best (buying), delivery, bulk, gifting, city plus mango.
- Keywords already ranking in the top 3 are excluded (defend them with the product pages, do not write a competing blog).
- Informational-only keywords (recipes, nutrition, benefits) are excluded.
- Each row is a cluster: one primary keyword plus up to six secondary keywords, so one blog serves one buying topic. Do not write one blog per keyword.

## Columns
`batch`, `queue_no`, `status` (queued / written / published), `intent`, `primary_keyword`, `secondary_keywords` (use these naturally in headings, FAQ and body), `cluster_monthly_volume`, `primary_kd`, `current_position`, `priority_tier` (1 Alphonso family, 2 other varieties, 3 generic, 4 city), `link_cta_to` (the product or collection the blog must link to with the exact keyword as anchor text), `suggested_title`, `suggested_slug`, `shopify_blog` (blog handle to publish in).

## Rules for every blog (the agent must follow these)
1. **One cluster, one blog.** Check the slug and primary keyword against existing articles before writing; skip if a blog already targets it.
2. **Buying page first.** Put a price table or a short "price today" block above the fold, then a clear order link to `link_cta_to`. Use the live-price tokens below, never typed prices.
3. **Live prices:** (active once theme v4 or later is published) blog bodies run through the same token system as the AI pages. Write `[[am:price:ratnagiri-alphonso-mango:1]]` for the 1-dozen Small price, `...:2` Medium, `:3` Large, `:4` Extra Large, `:5` Jumbo, and `[[am:min:HANDLE]]` / `[[am:max:HANDLE]]` for ranges. Supported handles: ratnagiri-alphonso-mango, devgad-alphonso-mango, alphonso-mango-order-online, kesar-mango, pairi-mango, dasheri-mango-online, totapuri-mango, malgova-mango, salem-mango, malawi-mango, alphonso-mango-pulp, alphonso-mango-cubes, aamras-ambyacha-ras.
4. **Structure:** a direct 40-60 word answer at the top, H2s that use the secondary keywords, a 5 to 7 question FAQ written for buyers (price, delivery time, how to order, season, packing, returns), 1,000 to 1,500 words, one image with descriptive alt text.
5. **Delivery wording (use exactly):** "Orders placed before 12 noon IST (Monday to Saturday) are dispatched the same day. Delivery takes 1 to 3 days for most PIN codes and 1 to 2 days to most metros, depending on your PIN code. Fresh mangoes are delivered by Blue Dart to more than 4,700 PIN codes."
6. **Season wording:** "The 2027 mango season starts on 1 February 2027." Fresh mangoes are shown as out of stock until then; never say "available now" for them.
7. **City blogs:** use only cities in the Blue Dart list (`blue-dart-served-districts.csv`); say the delivery time is by PIN code.
8. **Facts the blog may use:** Powle Home Foods, FSSAI 10020022011783, APEDA 225579, GI Authorised User AU/5974/GI/139/260 (Alphonso) and AU/6932 (Devgad), Ratnagiri and Devgad farms, sourcing from 48 coastal villages of Ratnagiri and Devgad (villages near the seashore; confirmed by the owner 8 Oct 2026), natural hay-bed ripening, no calcium carbide, Blue Dart, WhatsApp +91 70830 75556 and +91 83690 48029 (use only these two numbers).
9. **Never write:** "organic" (no certification), scanning accuracy or "AI scanned" claims, "stores in Mumbai/Pune/Ahmedabad/Delhi", "free delivery to 20,000+ pincodes", "24-48 hours", customer counts, "keto-friendly", health claims, or any price typed by hand.
10. **Publish checklist:** title under 60 characters with the primary keyword first, meta description 120-155 characters with "buy" or "price", one internal link to `link_cta_to` with the exact keyword anchor, 2 more internal links to related products, do not paste your own JSON-LD into the body (the theme already outputs the article schema; a hand-written block with raw HTML in a string is what caused the Search Console parse errors).

## Running a batch
Take the rows where `batch` equals the number you are running and `status` is `queued`. After publishing, set the row to `published` and paste the live URL. Re-run Ahrefs/Semrush rank checks 4 weeks later; if the primary keyword is not in the top 20, add a second internal link from the highest-traffic related page.

## Where this should live
No Mango SEO Agent or blog queue exists in your Cloudflare account (workers: adpulse-collector, am-agent-readiness, agent-markdown, apple-pay-verification; KV: am-merchant-feed). The agent is somewhere else (a Sheet, an app or a separate project). Tell me where, and I will import the CSV or JSON in the format it expects.
