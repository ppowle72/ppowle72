# Plan to raise Domain Rating (DR 33) and URL Rating (UR 15)

Data read for this plan: Ahrefs overview (6 Oct 2026), Ahrefs Content Explorer export (811 rows, query "alphonsomango.in"), Ahrefs organic keywords (720 rows), Semrush Keyword Magic export (30,003 rows).

## 1. What the Content Explorer export actually contains
| Group | Pages | Domains | What to do |
|---|---|---|---|
| Your own pages (Ahrefs lists them because they contain the domain name) | 409 | 1 | Ignore |
| Proxy and mirror copies of your site (sc.hkex.com.hk, sc.sie.gov.hk, translate.*, norefs, linkbuddy) | 25 | 4 | Not real links; ignore |
| Site analysers, review scrapers, coupon sites (pr-cy, siteprice, leadsleap, smartcustomer, intodns, report-uri) | 59 | 15 | Not worth effort |
| Bookmark, directory and "story" network pages with titles like "Order Alphonso Mango Online" | about 60 | about 45 | Looks like old bulk link building. See `disavow-candidates.txt` |
| Genuine editorial or business mentions | about 14 | about 12 | **The real asset base, see section 2** |

So the headline "1.9M backlinks all time, 9.5K referring domains" is mostly noise. Only about a dozen quality mentions are visible in this export, which is why DR is 33.

## 2. Quality mentions to protect and convert (check each for a live, followed link)
| Source | DR | Page | Action |
|---|---|---|---|
| economictimes.indiatimes.com | 91 | Mango orchard owners, wholesalers (news) | Check whether it links; if only a name mention, ask for a link to the site |
| razorpay.com (2 pages) | 90 | Magic Checkout case study, Alphonso Mango | Confirm the link goes to the homepage; ask for a link to the Ratnagiri product page. Easiest high-DR win, a partner already wrote about you |
| food.ndtv.com | 89 | "Do the mangoes you eat contain carbide?" | Pitch the carbide-free test guide as a source; ask for a link where you are named |
| mid-day.com | 80 | Brand media article, Ratnagiri and Devgad | Brand-media is often nofollow or sponsored; check and add a normal editorial follow-up |
| thebetterindia.com | 77 | Order organic mangoes from farms across India | Ask for the link to be updated to the current product URLs |
| cntraveller.in | 74 | Farm-fresh mango home delivery services | Ask to be added or relinked for the 2027 season |
| hindustanbytes.com, thedailybeat.in | 47, 42 | Malawi mangoes (duplicate press release) | Fine as a record; do not repeat this route |
| catalog.in | 66 | Company listing | Keep NAP (name, address, phone) consistent with the site |

How to check a link quickly in Ahrefs: Site Explorer > Backlinks, filter "Dofollow" and "Link type: Content", or open each page and search for `alphonsomango.in`. If you send me the Backlinks export I will classify them for you.

## 3. Plan, in order of payoff
**Month 1: fix and reclaim (no new content needed)**
1. Ask Razorpay, NDTV Food, The Better India, CN Traveller and Economic Times contacts for link updates. Target: 6 new or corrected links.
2. Ahrefs > Backlinks > Broken: send me that export. Every backlink pointing to a 404 gets a 301 redirect (I will build the CSV, as with the price posts).
3. Claim consistent business listings with the same name, address and phone: Google Business Profile, Bing Places, Justdial, Sulekha, IndiaMART, TradeIndia. These are citations, not DR boosters, but they feed AI answers.
4. Remove the "stores in Mumbai, Pune, Ahmedabad, Delhi" claim from About unless true. Wrong location claims hurt trust and local results.

**Months 2 to 4: earn links with assets worth citing**
5. **Alphonso Price Index 2027:** weekly price by grade (Small to Jumbo), from your own sales data, with a chart. Journalists link to numbers. Our live-price tokens already keep the table current.
6. **Carbide test guide with video** (partner-farm footage). NDTV already covers the topic; offer your guide and a quote.
7. **Season calendar and GI authenticity checker** (Ratnagiri vs Devgad, how to read a GI certificate). Evergreen linkable page.
8. **Press release for the 1 Feb 2027 season opening** with the Press & Media page. Pitch food and business desks about 3 weeks before. Use real expert quotes only.
9. Expert-quote platforms (Qwoted, Featured, Muck Rack, local journalist WhatsApp lists): answer food and agriculture queries as the founder. Aim for 2 to 3 links a month.

**Months 3 to 6: partners and communities**
10. Razorpay-style case studies: ask Shopify partners, Judge.me, Blue Dart, Cloudflare and your payment/logistics partners for a customer story.
11. Agricultural bodies and food associations: APEDA, Maharashtra State Agricultural Marketing Board, mango growers' associations, GI authorised-user lists (these are real, high-trust, often .gov.in or .org).
12. Food bloggers and recipe creators for the Aamras season (gift a box, no paid links, ask for an honest review with a link).

**Do not**: buy bookmark, directory or "story" links, publish more syndicated press releases on low-quality sites, or use duplicate Malawi-style releases.

## 4. Raising UR (internal page strength)
UR is page-level. Your homepage carries most of it (UR 15 and 15.9K of 33.9K estimated monthly organic visits).
- Link every price, product and city page from the homepage and the mango collection with descriptive anchors ("Ratnagiri Alphonso mango price", not "click here").
- Fix cannibalisation: "hapus mango price" ranks with 3 URLs (homepage, product, /pages/alphonso-mango). Keep the product as the target and add a canonical-style internal link from the others.
- Put a price table and a buy block on the highest-traffic blog pages (they currently send readers away). Highest: `/blogs/raisins/kismis`, `/blogs/spices/elaichi`, `/blogs/faq/how-many-mangoes-in-1-kg`, `/blogs/alphonso-mango/mango-tree-lifespan`.
- Each new link you earn should land on a product or the price index page, not only the homepage.

## 5. Disavow
`disavow-candidates.txt` lists 193 domains from bookmark, directory and proxy networks. Google normally ignores such links, so upload it only if you did not create them, they were paid for, or Search Console shows a manual action. Review the list first.

## 6. Realistic targets
DR is logarithmic. From DR 33, +5 points usually needs roughly 40 to 80 new referring domains of DR 40+ in 6 months. A target of DR 38 to 40 by August 2027 and 20 to 30 quality referring domains is realistic with the steps above.
