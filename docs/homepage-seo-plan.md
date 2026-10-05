# alphonsomango.in homepage: keyword analysis and action plan

Data used: Ubersuggest (29 homepage keywords), SEMrush (211 homepage rows, 161 unique keywords; the two SEMrush files are byte-identical), Ahrefs (2 files, homepage rows only: 140 + 273). The Ahrefs exports arrived with a damaged UTF-16 header and mixed tab/comma quoting. I recovered all 2,948 and 5,940 rows and filtered to `alphonsomango.in/`. Blank "current position" in Ahrefs means a keyword that dropped out of the top results, not a parsing error.

Full 29-keyword table with all three tools and before/after mention counts: `keyword-map-ubersuggest-29.csv`.

## 1. What the data says

The three tools disagree because they use different locations, devices and dates. The same keyword, "alphonso mango", reads position 13 (Ubersuggest), 2-3 (Ahrefs) and 1-2 (SEMrush, organic). Treat positions as a range and track one source consistently.

**Already top 3 in SEMrush (protect, do not rewrite around them):** alphonso mango (49.5k/mo), hapus mango (14.8k), hapus aam, ratnagiri mango, ratnagiri alphonso mango, alphonso mango online, alphonso aam.

**Quick wins: homepage ranks 4-24, high volume, low-to-medium difficulty (SEMrush organic)**

| Keyword | Pos | Volume | KD | What moves it |
|---|---|---|---|---|
| mangos online | 14 | 4,400 | 22 | "buy mango online in India" copy + collection links |
| alphonso mango 1 kg price | 21 | 3,600 | 10 | live price-per-dozen table (added) |
| devgad hapus | 24 | 2,400 | 14 | Devgad column and comparison table (added) |
| ratnagiri hapus mango | 7 | 1,900 | 21 | named in comparison + intro (added) |
| mango online / mango online india | 9 / 6 | 1,900 | 37 / 51 | commercial narrative, internal links |
| order mangoes online | 18 | 1,300 | 19 | 3-step order flow (added) |
| buy mango online | 14 | 1,300 | 30 | order flow + city paragraph (added) |
| ratnagiri hapus | 8 | 1,300 | 40 | comparison table |

**AI Overview / question keywords (21 homepage keywords trigger an AI Overview):** what is alphonso mango, where is alphonso mango from, alphonso mango price per dozen, season, delivery. All are now visible FAQ answers with matching FAQPage schema.

## 2. Gaps found on the live homepage template

Text in `templates/index.json` is about 630 words. Before this change: no prices, no FAQ, no purchase steps, no comparison table, 0 mentions of the operating company, FSSAI, GI authorisation, or 5 of the 6 target cities. 16 of the 29 Ubersuggest keywords appeared zero times. The stale `Event` "Season 2026" node and a hidden FAQPage with old prices (₹2,249-3,699) sat in the homepage schema while live prices are ₹1,849-2,999.

## 3. Changes made (staged, not published)

Applied to unpublished theme "HOME SEO v1 - direct answer, FAQ, live prices (Claude, 4 Oct)", a duplicate of the live theme, so nothing else differs from live. Source copies are in `shopify-theme/`. See also `competitor-analysis.md` and `schema-aeo-geo-matrix.md`.

| File | Change |
|---|---|
| `sections/home-direct-answer.liquid` (new) | ~45-word direct answer under the hero, H2, live stock/season line |
| `sections/home-seo-content.liquid` (new) | 3-step buy flow, live price table (reads variant prices), Ratnagiri vs Devgad table, six-city delivery paragraph, entity paragraph, 10-question visible FAQ, WebPage + FAQPage JSON-LD |
| `templates/index.json` | adds both sections; replaces the "2026 Season" heading with an evergreen one |
| `snippets/global-schema.liquid` | removes the stale homepage `Event` and hidden `FAQPage` (the visible FAQ now owns FAQPage) |

The hero already renders the H1; new sections start at H2.

## 4. Where this deliberately differs from the brief

1. **Proveda Superfoods is not named.** `global-schema.liquid` documents that Proveda is a separate legal entity with FSSAI/GST pending, and that FSSAI 10020022011783, APEDA 225579 and GI AU/5974/GI/139/260 belong to **Powle Home Foods**. Pairing Proveda with those numbers would be a false claim. If Proveda now holds its own licences, say so and it is a one-line change.
2. **No `SearchAction`.** It was removed earlier as invalid and Google retired the sitelinks search box. No `buy_url/cart_url/export_form_url` parameters: those endpoints don't exist. Instead the WebPage node carries a valid `OrderAction` and `ViewAction`.
3. **`dateModified` is a setting, not "now".** Update "Content last reviewed" quarterly after re-checking prices and season copy.
4. **No fabricated freshness or availability.** Every fresh-mango variant is currently sold out (off-season, today is 4 Oct 2026). The page says so and points to mango pulp (in stock). "Same-day dispatch" is worded "in season, before 12 noon IST", matching the existing shipping schema cutoff.
5. **Prices are live Liquid, not typed numbers.**

## 5. Still to do (not possible from this environment)

1. **Title and meta description** are set in Shopify admin (Online Store, Preferences). Suggested title: `Buy Alphonso Mango Online India | GI Tagged Ratnagiri & Devgad Hapus` (≤60 chars). Description: `Buy GI-tagged Ratnagiri & Devgad Alphonso mangoes online in India. Carbide-free, free delivery to Mumbai, Bangalore, Delhi & more. FSSAI licensed.`
2. **Preview, then publish** the "HOME SEO v1" theme from Shopify admin (publishing is blocked from this environment).
3. **Product grid images at 350w with srcset, LCP < 1.5 s:** the field data in the theme notes shows LCP 2.3 s and CLS 0.27 (failing). I could not measure the site from here (the egress proxy blocks alphonsomango.in). Run PageSpeed on the preview URL; the new sections contain no images so they add no LCP or CLS risk.
4. **Mismatched facts to confirm:** the product pages' own schema and FAQ still quote 2026 prices elsewhere (`global-schema.liquid` article FAQ: ₹2,249-3,699). Refresh them when the 2027 season prices are set.
5. **Track:** pick one rank source, record baseline, and check at 4 and 8 weeks. Off-season traffic will dip regardless; compare year over year.

## Trust line and press section (added 5 Oct 2026)
- **Trust line:** "12,000+ customers have bought from us, online and at our shop." appears under the direct answer (editable in that section's settings) and in the "Who sells these mangoes" paragraph. Basis: your statement that offline shop customers are in addition to the online base. The online figure is verified in Shopify (5,896 customers and 8,215 orders over the last three years). The offline portion is your figure and I cannot verify it, so keep your own records. If the number changes, update both places.
- **Press and media section:** built as a separate section (`home-press.liquid`) with 12 link blocks from your list, **switched off** in the template. I could not open the publishers from the build environment to confirm that each page mentions alphonsomango.in or its founder, and a few entries look like they may not be coverage of the brand (the Ministry/DD News Facebook post, the Inc42 company-profile page, the Fructidor price article, the LBB Mumbai guide, the two NDTV carbide-tips articles). Before switching it on in the theme editor, open each link and keep only those that name AlphonsoMango.in, Powle Home Foods or Prashant Powle. The AI-written note at the top of your second list ("While search indexes currently surface...") was not used and should never be published.
- **Video proof:** no video links were supplied. Send YouTube or Instagram links to the testimonial or farm videos and I will add a video block.
