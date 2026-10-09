# Merchant Center audit from the product export (6 Oct 2026)

Source: `merchant_center_products_2026-10-06_01-49-30.zip` (763 rows, 504 unique offers in English and 259 in Hindi, 103 product pages). Row-level data: `merchant-center-offers-en.csv`. Proposed titles: `merchant-feed-title-proposals.csv`.

## 1. Two feeds sell the same products with different data
| | Feed label `INR_1239712001` | Feed label `IN` |
|---|---|---|
| Source | Shopify Google & YouTube app, India market (market ID 1239712001 is your India market) | Older Shopify sync for India |
| English rows | 259 | 245 |
| In stock / out of stock | 170 / 89 | 222 / 23 |

- 167 variants appear in both feeds. 10 have different prices (for example Alphonso pulp 850 g: Shopify and the `IN` feed say ₹590, the `INR_` feed says ₹749; Ratnagiri medium: ₹2,099 vs ₹2,999). 7 have different availability.
- 78 `IN` rows are for variants that no longer exist in the `INR_` feed (28 of them saffron). 74 of these are marked "in stock".
- 12 of 15 mango offers in the `IN` feed say "in stock" while Shopify shows the mangoes as sold out. Google can show a price and "in stock" that your site does not honour. This can lead to price/availability mismatch disapprovals.
- The `IN` feed also has rows with no brand (49), no product category (57) and no condition (77). They carry only a bare product name.

Fix (in Merchant Center, Settings, Data sources):
1. Open both Shopify sources. Keep the one that matches Shopify's current prices after a full resync (in Shopify admin, Google & YouTube app, Settings, re-sync products), and turn off or delete the other. India is your primary market, so the `INR_1239712001` source is the one to keep.
2. After 24 hours export products again and send me the new file. I will compare it with Shopify.

## 2. Product attributes
| Issue | Rows | Fix |
|---|---|---|
| brand missing | 49 | Set vendor `AlphonsoMango.in` on every product; disappears with the stale `IN` rows |
| google product category missing | 57 | Mainly modak, wadi, aam papad, mango cubes, malawi mango, saffron, some cashews. Set the category in the Google & YouTube app |
| condition missing | 77 | Set `new` |
| MPN is a product name (for example "Ole Kaju", "Sweet Tamarind") | ~60 | MPN must be a part number. Use the SKU (the variants already have `custom.mpn` = SKU on mangoes) or remove it |
| rating | 1 row only | Send Judge.me product ratings to Google through Judge.me's Google Shopping integration |
| shipping | 50 rows have `IN::` (no price/service) | Set shipping at account level: free shipping India, 1 to 3 days |
| titles | most | Promotional text ("Buy ... Online", "Order Now", pipes). See proposals file |

## 3. GTIN without GS1
- Every variant has an SKU (checked: none missing) and none has a barcode.
- Google does not require a GTIN for unbranded or own-brand produce. Send `identifier_exists = no`, `brand = AlphonsoMango.in` and `mpn = SKU`. Do not invent a GTIN and do not copy another company's barcode.
- Only buy GS1 codes if you later register the brand with a marketplace that demands them. Check GS1 India for small-business or per-code options before buying a full membership.
- SKU scheme if you add new products: `AM-<PRODUCT>-<PACK>` for example `AM-CASH-W320-250G`. Keep existing SKUs as they are because orders and apps reference them.

## 4. Size labels (variant names)
The offers show at least five different size labels for the same grade: "135 to 180", "150 to 180", "180 to 200", "180 to 220", "180 to 225", "200 to 225". Decide one table (suggested: Small 150-180, Medium 180-220, Large 225-250, Extra Large 250-275, Jumbo 275-300 g) and use it in Shopify variant names, the metafield `custom.fruit_size_range`, the website and every page.

## 5. Stock and fulfilment status
- Inventory on mango variants is hugely negative (for example Ratnagiri -4.5 million). They show as sold out because stock tracking is on with "deny". Reset to real counts before 1 Feb 2027.
- Each mango variant also has the metafield `custom.fulfillment_status = out_of_stock`. The product schema reads it. Change it to `in_stock` (or `preorder`) when the season opens, or the schema will keep saying out of stock even when Shopify allows purchase.

## 6. Duplicate products
`alphonso-mango-order-online` ("Buy Ratnagiri Hapus Mango Online - 1 Dozen") is a second Ratnagiri-like product with the same sizes. It competes with `ratnagiri-alphonso-mango`. Decide whether to merge it or keep it out of Google (use a collection exclusion in the Google & YouTube app).
