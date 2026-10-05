# Merchant Center readiness (5 Oct 2026)

Merchant Center data could not be pulled: the Supermetrics connection works (account "AlphonsoMango.in", ID 719656549) but the Supermetrics trial expired on 2026-05-11, so every data query is refused. Options: upgrade Supermetrics, or export from Merchant Center (Products > Diagnostics, and Performance) and send the files.

Instead, the Shopify side was read (first 50 active products, updated most recently). Findings:

## Stock counts on the mango products
- `ratnagiri-alphonso-mango`: total inventory -4,533,187 (single variants as low as -4,246,328). `alphonso-mango-order-online`: -150,052. `devgad-alphonso-mango`: -117. `kesar-mango`: -70. `ole-kaju...`: -397.
- All use "stop selling when out of stock", so they show as sold out, which is correct off-season. But these numbers are not real counts. Before 1 Feb 2027 set real positive stock per variant, or Merchant Center and the homepage will keep showing "sold out".

## Barcodes (GTIN)
- Every product has a blank barcode. That is acceptable for unbranded food only if the feed sends `identifier_exists = no`. If the AlphonsoMango.in brand is registered with GS1, add GTINs.

## Prices
- Mango per-dozen prices in Shopify: 1,849 / 2,099 / 2,499 / 2,699 / 2,999 (2 dozen small 3,499). The AI pages and the old llms files still show 2,249-3,699, which does not match the feed.

## Product titles
- Many titles are keyword strings with promotional words ("Buy ... Online Today", "Order Now", "Buy Saffron Online | Keshar"). Merchant Center can flag promotional text in titles. Use clean feed titles (for example "Ratnagiri Alphonso Mango, 1 Dozen (GI Tagged)").

## Possible policy risks
- "10 g (pregnancy pack)" saffron variant, "Vitamins & Supplements" type on moringa powder, and health claims on the camphor listing may trigger health-claim review in Shopping.

## Other
- SKUs begin with "PROV-" (Proveda). Harmless, but they show the other entity name in the feed.
- Size labels differ: Ratnagiri medium "180 to 220 g", Devgad medium "180 to 225 g", Devgad jumbo "275 g and above". Make them identical.
- The Worker `am-agent-readiness` serves `/merchant-feed.xml` from KV; confirm Merchant Center uses that same address and that its prices match Shopify.
