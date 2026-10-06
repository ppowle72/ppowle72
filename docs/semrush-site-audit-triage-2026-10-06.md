# Semrush Site Audit triage (crawl of 6 Oct 2026, health 80%, 100 pages crawled)

| Issue | Count | Verdict | Action |
|---|---|---|---|
| Structured data invalid: LocalBusiness missing `address` on 4 city articles | 4 | Real | Removed the LocalBusiness node from each article's inline JSON-LD. A delivery city is not a business location. |
| Structured data invalid: HowTo missing `step` (how-to-ripen-alphonso-mangoes-at-home) | 1 | Real | Theme added an empty HowTo to every article in the "how" blog and to one ripening page; removed in `global-schema.liquid` (HowTo rich results no longer exist in Google). |
| Structured data invalid: Product / Merchant listing on `/pages/ai-products` (no price, no image) | 15 | Real | Six hand-written Product entries replaced by plain catalogue links (ListItem). This also removed a hard-coded 4.61 rating (271 reviews) that was not tied to live review data. |
| Robots.txt "format error": `Content-Signal: search=yes, ai-input=yes, ai-train=yes` | 1 | False alarm | This is Cloudflare's valid Content Signals directive. Google ignores lines it does not know and Semrush's parser flags it. Keep it. (`ai-train=yes` was your earlier choice; change it to `no` if you want to opt out of training.) |
| 80 internal resources blocked by robots.txt | 80 | False alarm | All 80 are `/checkouts/internal/preloads.js`, a Shopify checkout script that rendering does not need. Leave it. |
| 215 resources formatted as page link | 215 | Ignore | Review-photo and product-image links (117 Judge.me, 93 own CDN). Harmless. |
| 40 links with no anchor text | 40 | Low | 32 are on `/pages/privacy-policy`, 5 on `/pages/ai-products` (image or icon links), 3 on blog index pages. Fix only if you want a clean report. |
| hreflang conflict: `/collections/cashew-nuts/Cashew-Nuts` | 1 | Low | A tag-filtered duplicate URL with no self-referencing hreflang; its canonical already points to the main collection. Ignore. |
| 152 external links broken, 3 internal links broken, 2 pages returning 4XX, 72 permanent redirects | n/a | Needs the export | Not included in the files sent. Export these four from Semrush (Issues > the issue > Export) and the broken internal links and 4XX pages can be fixed with redirects. |

Counts in the screenshots show 22 errors and 414 warnings in the crawl, many carried from older crawls; the issues above are the ones in the four exports.
