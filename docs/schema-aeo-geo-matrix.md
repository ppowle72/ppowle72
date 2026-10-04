# Schema and answer-engine coverage for the homepage

Verification note: Google's own docs were network-blocked in this environment. Statements about which types Google still supports come from third-party sources reading search results and are marked **unverified**. Re-check developers.google.com before relying on them.

## What the homepage emits now
| Layer | Source file | Types |
|---|---|---|
| Sitewide | `snippets/global-schema.liquid` | Organization (legalName Powle Home Foods, certifications, sameAs, contact points, areaServed cities), WebSite, Person (founder) |
| Homepage | `snippets/global-schema.liquid` | ItemList (featured products), LocalBusiness + OnlineStore |
| Homepage (new) | `sections/home-seo-content.liquid` | WebPage (dateModified from setting, speakable, OrderAction, ViewAction), FAQPage (10 questions generated from the visible FAQ) |
| Removed | | Stale `Event` "Season 2026" and the hidden FAQPage with out-of-date prices |

## Channel by channel
| Channel | What serves it | Status |
|---|---|---|
| **SEO** | Direct answer + H2 narrative with target phrases, live price table, comparison table, internal links to both product pages | Done (staged) |
| **AEO / featured snippets** | ~45-word direct answer; question-form headings; tables; numbered steps | Done |
| **People Also Ask** | 10 visible FAQ questions covering what/where/price/season/delivery/authenticity/Ratnagiri vs Devgad/Hapus naming/origin check/damage policy | Done. Add more questions only after checking the live PAA box in a browser |
| **AI Overviews (AIO)** | Same visible answers; factual, dated, entity-consistent (Powle Home Foods, GI numbers) | No special AIO markup is documented (unverified from Google). Content clarity and consistency are the lever |
| **Voice search** | `speakable` on the direct-answer paragraph (`.home-answer__text`) | Done. Speakable support is limited, so the short answer text is the real asset |
| **GEO / LLM citation** | Entity facts in body copy, `llms.txt` and `llms-full.txt` already in the theme, consistent Organization graph | Existing + body copy added. Keep `llms.txt` prices in sync with the live price table |
| **Local / regional** | LocalBusiness + six named cities in copy and FAQ | Done on the homepage; city landing pages still to build |
| **Merchant listings** | Product-level Offer, shipping and return markup already exists in `global-schema.liquid` | Existing. Needs Merchant Center to be useful (not checked) |

## Honest limits
- **FAQPage rich results.** Third-party sources report Google stopped showing FAQ rich results in May 2026 (unverified). The FAQPage JSON-LD is kept for machines and assistants, but the visible answers are what matter, and they match the markup exactly.
- **No SearchAction, no custom buy/cart/export "Action" URLs.** Not valid or not real endpoints. `OrderAction` and `ViewAction` point to real URLs.
- **No `AggregateRating` or `Review` on the homepage.** Only Judge.me product-level ratings that are backed by real reviews belong in schema.
- **No HowTo schema.** Google retired HowTo rich results; the 3-step flow is plain visible content.
- **`dateModified`** comes from the "Content last reviewed" setting, not the current date. Update it when prices and season copy are re-checked.

## Ranking action plan (in priority order)
1. **Publish the duplicated theme** after preview. This is the biggest on-page change (630 words with no prices or FAQ, now answered content).
2. **Set the homepage title and meta description** in Shopify admin (Preferences). Suggested title: `Buy Alphonso Mango Online India | GI Tagged Ratnagiri & Devgad Hapus`.
3. **Fix Core Web Vitals.** Theme notes show field CLS 0.27 (failing) and LCP 2.3 s. Rankings for competitive terms like "mango online" (pos 6-9, KD 37-51) depend on it. Check the product grid images (`srcset` to 350w) and the hero (`fetchpriority="high"`) on the preview with PageSpeed.
4. **Build the Ratnagiri vs Devgad article and city pages** (see `competitor-analysis.md`) and link them from the homepage.
5. **Refresh stale 2026 prices** in product, article and `llms.txt` copy when 2027 prices are set; off-season, keep "sold out until next season" messaging truthful.
6. **Measure.** Record baseline positions in one tool, check at 4 and 8 weeks, and compare year over year because the product is seasonal.
