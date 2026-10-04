# Homepage keyword gaps, what was added, and the ranking plan

Sources: SEMrush (211 homepage rows), Ahrefs (homepage rows from 2 files), Ubersuggest (29 keywords), plus the verified ratnagirihapus.store homepage. Competitor keyword data is **not** available (the competitor sites are blocked from this environment and none of the exports cover a competitor), so "competition gap" below means gaps in on-page terms against the one competitor homepage I could read, plus patterns seen in search results. Full list of homepage keywords with 100+ searches a month that the homepage text did not literally contain at analysis time: `homepage-keyword-gaps.csv` (144 keywords).

## 1. What was missing from the homepage (by theme)
| Theme | Examples (monthly volume, current best homepage position) | Action |
|---|---|---|
| **Price per kg** | alphonso mango 1 kg price (3,600, pos 21), alphonso mango price per kg (880, pos 14), alphonso mango rate (480, pos 7) | **Added.** A per-kg column in the live price table, plus a per-kg sentence in the FAQ answer |
| **"Online / order" buying phrases** | mangos online (4,400, pos 14), mango online order (880, pos 11), order alphonso mango (590, pos 1), online mango shopping (1,300, pos 9) | **Added.** "How to order Alphonso mango online in 3 steps", "order mangoes online in India" in the delivery text |
| **Price + variety** | ratnagiri alphonso mango price (480, pos 6), hapus mango price in india (480, pos 24), devgad hapus mango price (480, pos 53) | Covered by the price tables and the H2 "Ratnagiri vs Devgad Alphonso: price and comparison". Watch these three first |
| **Regional names and spellings** | hapus amba (720, pos 1), hapoos aam (320, pos 2), alphanso mango (700), alfonso mango (450) | **Added** to the FAQ "Is Hapus the same as Alphonso?" (names Hapus, Hafus, Hapoos, Alfonso, Alphanso, Alphonse) |
| **Cities** | alphonso mango bangalore (320, pos 1), in mumbai (320, pos 1), price in mumbai (260, pos 1) | Homepage already ranks 1 for these. Delivery text now names 11 cities from your order data. City pages are the next step |
| **Other varieties** | payari/pairi mango (1,300 pos 1; 2,400 pos 9), kesar mango price (1,900, pos 6) | Rank on product pages. Homepage text now names Gir Kesar and Pairi (Payari). No more homepage space needed |
| **Out of scope for the homepage** | Saffron/kesar queries (27,100, 9,900, 8,100) rank on blog and product pages; "mango pulp" (9,900) ranks pos 55 on a recipe blog while the pulp product ranks 1 for "alphonso mango pulp" | Leave on their own pages. Put a pulp link on the homepage (done: "Order mango pulp (all year)") and fix the pulp blog/product internal linking |
| **Not worth adding** | monsoon mangoes, hansom, brazil nuts online, mango images, mango juice | Low intent or off-topic |

## 2. Cannibalization to fix
For "alphonso mango" (49,500/mo), the homepage ranks 1-3, but `/collections/frontpage` (pos 4) and blog posts (pos 11, 14) also rank. Do not add more homepage copy for this term. Instead link those blog posts and the collection back to the homepage and the two product pages so one URL wins.

## 3. Competition gaps (limits stated)
Verified source: ratnagirihapus.store homepage (see `competitor-analysis.md`).
| They have, we lack | Our response |
|---|---|
| Press logos ("Featured in") | Add if you have real coverage |
| 10 video testimonials | Add a customer-video block if you have clips |
| Prominent trust numbers (customers, pincodes, delivery days) | Supply verified numbers; I did not invent any |
| "Alphonso Mango in Cities" hub page | Build a cities hub and city pages (order: Bangalore, Delhi NCR/Gurgaon, Mumbai/Thane, Hyderabad, Chennai, Pune, Kolkata, Jaipur) |
| We have, they lack | FAQ + FAQPage schema, direct answer, order steps, comparison table, price-per-kg, H1 aligned to the main keyword |

Dhanshi Farms (dhanshefarm.com), RQD Farm, AAMRAI, Foodwalas, Devgad Mango: **not analysed** (blocked). RQD's size-grade product pages and city URLs, and AAMRAI's buying-guide blog posts, are seen only in search results.

## 4. What was added to the homepage (all staged on the unpublished "HOME SEO v1" theme)
1. ~45-word direct answer under the hero (live stock and season line).
2. "How to order Alphonso mango online in 3 steps": Select Grade, Add to Cart, Same-day Dispatch (in season, before 12 noon IST).
3. Live price table per dozen for Ratnagiri and Devgad, with an approximate Ratnagiri per-kg column (price divided by mid-weight of each size band; about ₹857 to ₹934 per kg at current prices).
4. Ratnagiri vs Devgad comparison table.
5. Delivery paragraph naming Bangalore, Mumbai, Delhi, Gurgaon, Noida, Hyderabad, Chennai, Pune, Kolkata, Jaipur, Ahmedabad (from your Shopify billing-city data).
6. Powle Home Foods entity paragraph with FSSAI, APEDA and GI authorisation numbers.
7. 10-question visible FAQ with matching FAQPage JSON-LD, plus a WebPage node (dateModified from a setting, speakable).
8. Removed the stale Season 2026 Event and the hidden FAQPage.

## 5. How the ranking improves, in order
1. **Publish the theme** and set the title and meta description (Shopify admin, Preferences).
2. **Fix CLS (0.27, failing) and LCP (2.3 s)** from the theme notes. Competitive terms ("mango online india", pos 6, KD 51) need passing Core Web Vitals.
3. **Re-check at 2, 4 and 8 weeks** in one rank tool: alphonso mango 1 kg price, mangos online, devgad hapus, ratnagiri hapus mango, mango online order. These are the terms the new content targets.
4. **Build city pages and a cities hub**, then a Ratnagiri vs Devgad article and a "how to identify real Alphonso" guide. Link all of them to the homepage.
5. **Add press and video proof** when you have real material.
6. **Keep numbers honest:** refresh the "Content last reviewed" date each quarter, and keep out-of-stock messaging truthful in the off-season.
7. **Expect seasonality.** Fresh mangoes are sold out until about February, so compare against the same weeks last year, not last month.

## 6. Allowing the competitor domains
There is no command to run. Per the environment docs this is a settings screen: cloud environment menu in the session title bar, Edit, Network access, Custom, then Allowed domains. Paste this list (keep the default package managers):

`ratnagirihapus.store, www.ratnagirihapus.store, dhanshefarm.com, www.dhanshefarm.com, rqdfarm.in, www.rqdfarm.in, aamrai.com, www.aamrai.com, foodwalas.com, www.foodwalas.com, devgadmango.com, www.devgadmango.com, ratnagirialphonsomango.com, ratnagirifarms.com, agrophonics.com, developers.google.com`

Then start a new session. The setting did not take effect inside this running session.
