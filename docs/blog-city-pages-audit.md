# Blog and city-page audit (5 Oct 2026)

Source: Shopify articles and pages read through the Admin API. Nothing was published, hidden or redirected.

## City coverage
| City | Published now | Hidden draft ("-v2", ready to publish) |
|---|---|---|
| Bangalore | 5 overlapping posts (mango-south, alphonso) | `order-mangoes-online-bangalore-alphonsomango-delivery-v2` |
| Delhi NCR | page `/pages/alphonso-hapus-mango-in-delhi-ncr` plus 4 posts | `hapus-mango-in-delhi-v2`, `alphonso-mango-in-gurgaon-v2` |
| Mumbai | `mango-online-mumbai` plus several price posts | `mango-mumbai-v2`, `buy-alphonso-mangoes-online-v2` |
| Hyderabad | `mangoes-online-hyderabad-next-day-delivery` | `mango-delivery-in-hyderabad-v2` |
| Chennai | `mango-online-chennai` | `mango-online-chennai-v2` |
| Pune | `best-mangoes-in-pune-order-online`, `alphonso-mangoes-in-pune`, `mango-rate-in-pune-sweet-deals-unveiled` | `aamras-pune-v2` (aamras only) |
| Kolkata | price post only (`alphonso-mango-price-in-kolkata`) | `alphonso-mango-in-kolkata-v2` |
| Jaipur | none | `alphonso-mango-in-jaipur-v2` (blog ratnagirihapus) |
| Also hidden | | Ahmedabad, Indore, Nagpur, Goa |

## Ratnagiri vs Devgad
No published comparison. Hidden draft: `ratnagiri-and-devgad-hapus-v2` ("Ratnagiri vs Devgad Alphonso Mango: Full Comparison", blog `hapus`). Also hidden: `devgad-vs-sindhudurg-hapus`, `devgad-hapus-v2`.

## Before republishing the "-v2" drafts
1. Each v2 duplicates an older published post on the same topic. Publishing both splits ranking. Replace the old post's content with the v2 (keeping the old URL) or publish v2 and 301-redirect the old URL to it.
2. Check each draft for prices, "2026" wording and the entity (Powle Home Foods holds FSSAI/APEDA/GI AU/5974/GI/139/260; Proveda is not named until December 2026).
3. Check each draft for claims you cannot back up (Brix per batch, delivery times) and for Blue Dart / Delhivery / Ekart as the courier names. DTDC and Xpressbees only once live.
4. Add 2027 wording: the season starts on 1 February 2027.

## Near-duplicate price posts (merge candidates, blog `price` and `ratnagiri-hapus`)
`ratnagiri-hapus-mango-prices-ultimate-guide`, `ratnagiri-hapus-price-guide`, `discover-ratnagiri-alphonso-mango-price-varieties`, `unbeatable-ratnagiri-hapus-mango-price-in-mumbai`, `hapus-mango-rate-online`, `cost-of-alphonso-mangoes-in-mumbai`, `alphonso-mangoes-cost-online-vs-local-market`, `ratnagiri-hapus-aam-price`, `alphonso-mango-mumbai-price`, `alphonso-mango-price-in-india`, `buy-ratnagiri-hapus-online` and its same-titled twin `authentic-ratnagiri-hapus-mango-online-order-today`.
Suggested: keep one guide (`buy-ratnagiri-hapus-online`, refreshed for 2027), redirect the rest to it. Do this in Shopify admin (Online Store, Navigation, URL redirects) after you confirm the list.

## Pages that still say 2026
`alphonso-mango-season-2026`, `brix-ripening-index` ("2026 Guide"), `nri-mango-gift-india` ("2026"), `ai-products`, plus blog titles containing 2026. Update to 2027 once 2027 prices are set; the season start is 1 February 2027.

## llms.txt
Fixed on the staged theme: entity and GI number now match the schema, the stale price range is gone, logistics partners and the 2027 season start are added, and broken city links point to real posts. Still unverified: the WhatsApp number in `llms.txt` (+91 83690 48029) differs from the one on the site (+91 70830 75556); the "Brix 18 to 22 verified per batch" claim; `/blogs/guide/identify-fake-mango`, `/blogs/recipes/authentic-aamras-recipe` and `/blogs/healthy-mango/mango-glycemic-index` (not found in the article list); the `/pages/llms-full` template still names Proveda and an old founding year.
