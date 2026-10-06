# Product SEO and structured-data analysis (6 Oct 2026)

Data: `product-seo-audit.csv` (120 products, 96 active, 24 drafts). Proposed fixes: `product-seo-proposals.csv` (44 products).

## Title and meta findings (96 active products)
| Check | Result |
|---|---|
| No meta title set (Shopify falls back to the product title) | 17 |
| No meta description | 1 (Amba Modak) |
| Effective title over 60 characters (cut off in Google) | 10, eight of them cashew products at 78-87 characters |
| Meta description over 160 characters | 9 (cashews 266-288, Chilgoza 172) |
| Title without "buy / online / price" intent word | 19 |
| Truncated title | Ajwa Dates ("...near m") |
| 24 drafts | includes `hapus-mango`, two test products; keep out of the sitemap |

## What to change
1. Meta title: 50-60 characters, pattern `Buy <product + local name> Online | AlphonsoMango.in`. Put the main keyword first and the Hindi/Marathi name in brackets.
2. Meta description: 120-155 characters with a price ("from ₹x"), delivery area and one proof point (FSSAI licensed). Do not repeat the title.
3. Product title (H1): keep it natural; the long keyword-stuffed cashew titles belong in the meta title only, shortened.
4. Description: every product already has at least 80 words; add a short FAQ block (3 questions) to the top sellers so the FAQ is visible on the page.
5. Product type: 12 spellings for the same thing (`nut`, `cashew nuts`, `Cashew Nuts`, `dry fruit`, `Dried Fruits`). Standardise them; the schema `category` and Merchant Center product category read this field.

## Structured data still missing or weak, by product group
| Group | Gap | Fix |
|---|---|---|
| All products | No aggregateRating/review unless Judge.me has data | Collect reviews; schema emits them automatically once `reviews.rating` exists. Never add placeholder ratings. |
| All products | No GTIN (GS1 too costly) | Keep `identifier_exists = no` in Merchant Center; MPN = SKU. |
| Dates, cashews, dry fruits | `size` is the weight, no origin or grade | Add metafields `custom.origin_country`, `custom.grade` (W180/W240/W320, Mazafati/Medjool) and render them as `additionalProperty`. |
| Cashews | Konkan origin and grade are only in the title | `countryOfOrigin` plus grade metafield. |
| Packaged food | No nutrition or ingredients | `custom.ingredients` is supported already; add `nutrition` (calories per 100 g) for dates and nuts where you have lab or label data. |
| Fresh mangoes | areaServed was only "India" | v1.3.0 now lists 34 states/UTs and 46 cities taken from the Blue Dart PIN list. |
| Out-of-season products (32 with 0 stock) | Marked OutOfStock | Use `custom.fulfillment_status = preorder` only when you really take pre-orders. |

## Area served
`areaServed` is not used by Google for rich results; it helps AI answers ("do you deliver Alphonso to Nagpur?"). Source: `assets/mango-pincodes.json` (4,769 PIN codes, Blue Dart, 22 Sep 2026) joined to India Post districts: 418 districts, 34 states/UTs (`blue-dart-served-districts.csv`). Only fresh mangoes are restricted to this list; every other product ships to all Indian PIN codes.
