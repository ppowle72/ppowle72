# AI and fact pages audit (5 Oct 2026)

Read-only audit of nine live Shopify pages (these are pages, not theme files, so they are already live and are not changed by publishing the theme). Nothing on them was edited.

## How /llms.txt and /llms-full.txt are served
- Redirects exist: `/llms.txt` to `/pages/llms.txt` and `/llms-full.txt` to `/pages/llms-full.txt`. The pages are named `llms` and `llms-full` (no `.txt`), so these redirect targets may 404. Open both URLs in a browser. If they fail, change the redirect targets to `/pages/llms` and `/pages/llms-full`.
- Both pages use theme templates (`page.llms.liquid`, `page.llms-full.liquid`) that print their own fixed text and ignore the page body. The old templates were stale (Proveda, "Founded 2019", cart endpoints, "Global GAP", "certified organic"). Both are rewritten on the staged theme (v19.0). The page bodies in the admin are not shown by those templates.
- `/.well-known/ai-plugin.json` and `/.well-known/openapi.yaml` were listed in the old files. No redirect or file serves them in Shopify; the new files do not mention them.
- The `assets/llms.txt` file I edited is a theme asset; it is not served at `/llms.txt`.

## Per page
| Page | Verdict | Main issues |
|---|---|---|
| brand-facts | minor edit | "47,000+ customers" and "founded in 2017"; "15,000-17,000 pincodes"; leaked note "(your Devgad product page"; pin-code count conflicts with other pages |
| ai-commerce | needs edit | wrong WhatsApp (wa.me/918369048029); "cold-chain"; Rs.2,249-3,699; Brix "guaranteed per batch"; agent-purchase language |
| ai-products | needs edit | wrong WhatsApp; "BlueDart air"; same-day cut-off 2 PM (others say 12 noon); old prices; Brix |
| ai-faqs | needs edit | 2026 prices and season; 20,000+ pincodes; WELCOME10 code; `/cart/add?...ai_source=agent`; delivery times |
| ai-agent-navigation | rewrite | leaked editor notes in the body ("Pages > Add page ... Show HTML"); wrong WhatsApp; cart/add endpoints; prices |
| brix-ripening-index | needs edit | title says 18 to 22 Brix, body says 18 to 24; "2026" in title |
| alphonso-mango-season-2026 | rewrite | year-locked; weather and Brix claims for 2024 and 2025; prices; wrong WhatsApp |
| nri-mango-gift-india | needs edit | "2026"; prices with FX conversions; "20,000+ pincodes"; "1,000+ reviews"; "since 2019"; WhatsApp shown as the phone number |
| our-farmers | needs edit | wrong GI stem "AU/11054"; "Founded 2019"; "IoT Ripening Chambers", "AI Ripening chamber", cold-chain claims; 101 KB page |

## Conflicts across pages (pick one answer each)
- Founded: 2017 (brand-facts) vs 2019 (our-farmers, nri, old llms files).
- Customers: 12,000+ (homepage, Media Kit, llms), 47,000+ (brand-facts), 35,000+ (ANI release).
- Pincodes: 20,000+ vs 15,000-17,000 (and 22,000 in the ANI release).
- Same-day dispatch cut-off: 12 noon (most), 2 PM (ai-products).
- Delivery time: 24-48 hours, 1-3 days, 20-24 hours, 2-4 days, 4-24 hours within Mumbai.
- Ripening: "natural hay-bed in temperature-controlled rooms" (brand-facts) vs "IoT / AI ripening chambers" (our-farmers).
- WhatsApp: `+91 70830 75556` is correct; `+91 83690 48029` is the phone number. Wrong on ai-commerce, ai-products, ai-agent-navigation, season page, nri page.
- Brix: "18 to 24", "18 to 22", "16-20" (pulp); "guaranteed per batch" is not supported by data seen in this session.

## Safe fixes (no judgement needed; waiting for approval because these pages are live)
1. Replace `wa.me/918369048029` with `wa.me/917083075556` and WhatsApp labels showing 83690 48029.
2. Replace the "AU/11054" stem on our-farmers with AU/5974/GI/139/260 (Alphonso).
3. Remove leaked editor notes (ai-agent-navigation) and "(your Devgad product page" (brand-facts).
4. Fix the Brix title mismatch on brix-ripening-index.
Everything else needs a decision from the owner.
