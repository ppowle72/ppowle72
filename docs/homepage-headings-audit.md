# alphonsomango.in homepage: heading audit (H1 to H6)

Method: the live site is network-blocked, so this is derived from the Shopify theme source (template order, section settings and the section/snippet Liquid), on the "HOME SEO v1" theme. Tags the theme does not reveal are marked "not verified". Competitor headings could not be read (their sites are blocked), so there is no competitor heading comparison.

## Current outline, in page order
| Level | Text | Section |
|---|---|---|
| **H1** | Buy GI Tagged Alphonso Mango | slideshow (the only H1) |
| H2 | Where to buy Alphonso mango online in India | direct-answer (new) |
| H2 | Buy Alphonso Mangoes Online India: Ratnagiri & Devgad GI Tagged | featured collection (10 products) |
| H2 | Shop by Categories | collection list |
| ~~H3~~ **H2 (changed)** | Buy Premium Ratnagiri Alphonso Mango Online \| Fresh Hapus Aam Delivery | rich text |
| H2 | Our Dates Collection | featured collection (16 products) |
| H2 | 100% authentic Ratnagiri Alphonso Mangoes | countdown banner |
| H2 | Why Buy Alphonso Mangoes from AlphonsoMango.in? | media with text |
| H2 | We serve hundreds of new customers every week. | media with text |
| H2 | How to order Alphonso mango or Hapus mango online in 3 steps | SEO content (new) |
| H2 | Ratnagiri vs Devgad Alphonso: price and comparison | SEO content (new) |
| H2 | Order mangoes online in Bangalore, Mumbai, Delhi NCR, Hyderabad, Chennai, Pune and Kolkata | SEO content (new) |
| H2 | Who sells these mangoes | SEO content (new) |
| H2 | Alphonso mango FAQ (10 questions as expandable items, not headings) | SEO content (new) |
| "Customers are saying" | Judge.me carousel | tag not verified |
| H2 | Alphonso Mango Recipes & Exclusive Community Offers | rich text (no text under it) |
| H2 | Blogs | featured blog |
| H2 (x up to 6) | each blog post title | article cards |
| H3 | Join our community to get exclusive offers, original recipes | newsletter |
| H2 (x4) | Quick links, Mangoes, Partners, Follow us on | footer |

Disabled sections that render nothing: the first slide, the top countdown banner, and the testimonials section.

## Counts
H1: 1. H2: 14 in the main content, up to 6 blog titles, 4 in the footer. H3: 1 (after my change; it was 2). H4 to H6: 0. Product and collection cards use paragraph tags, not headings, so the 26 product titles are not in the outline.

## What is fine
- One H1, first on the page, matching the main keyword. It comes from a slide setting, so it vanishes if that slide is disabled or its heading cleared.
- No skipped levels. The announcement bar is not a heading.
- Sections use CSS classes (h3, h4) for size while keeping H2 for structure. That is correct.
- No empty headings are output.

## Problems and what to do
| # | Issue | Fix | Status |
|---|---|---|---|
| 1 | H3 "Buy Premium Ratnagiri Alphonso Mango Online \| Fresh Hapus Aam Delivery" sits right after the H2 "Shop by Categories" but is really a standalone, keyword-rich tagline | Make it H2 | **Done** (in the staged template) |
| 2 | Blog post titles are H2, the same level as the "Blogs" heading above them | Change `article-card.liquid` titles to H3 on the homepage card only. The same snippet runs on the blog index, where H2 is right, so this needs a parameter, not a blanket edit | Not done (needs a snippet change you should approve) |
| 3 | "We serve hundreds of new customers every week." is a tagline in an H2 and the claim isn't verified. The paragraph under it also repeats "Buy Authentic Alphonso Mangoes Direct from the Farm" twice | Make the H2 "Buy Authentic Alphonso Mangoes Direct from the Farm" and keep the customer claim only if you can support it | Not done: it is your wording and claim |
| 4 | "Alphonso Mango Recipes & Exclusive Community Offers" is an H2 with no text under it | Fill the block (link to recipes) or remove the section | Not done: your content |
| 5 | Newsletter tagline is an H3 after the blog H2s | Make it a styled paragraph | Low impact, not done |
| 6 | Footer headings are H2 and the "Follow us on" block holds phone, WhatsApp and email, not social links | Rename to "Contact" and use H3 or a styled label | Low impact, not done |
| 7 | Custom CSS on the media-with-text and countdown sections targets h3/h4/h5 with `!important`, but those sections output H2 | Remove the dead rules | Cosmetic |
| 8 | Judge.me "Customers are saying" heading tag is not visible in the theme | Check the app block in the browser | Not verified |
| 9 | Heavy repetition of "Alphonso / Ratnagiri / Buy" across about six H2s | Keep, but vary with the buying phrases the data supports (see below) | Partly done in the new H2s |

## Target outline (what the heading set should become)
- H1: Buy GI Tagged Alphonso Mango (keep)
- H2 Where to buy Alphonso mango online in India
- H2 Buy Alphonso Mangoes Online India: Ratnagiri & Devgad GI Tagged, then the product grid (card titles stay paragraphs)
- H2 Shop by Categories
- H2 Buy Premium Ratnagiri Alphonso Mango Online | Fresh Hapus Aam Delivery
- H2 How to order Alphonso mango or Hapus mango online in 3 steps
- H2 Ratnagiri vs Devgad Alphonso: price and comparison (H3s for "Price per dozen" and "Compare Ratnagiri and Devgad" would be a valid next refinement)
- H2 Order mangoes online in Bangalore, Mumbai, Delhi NCR, Hyderabad, Chennai, Pune and Kolkata
- H2 Who sells these mangoes
- H2 Alphonso mango FAQ (with question text as H3 only if you want each question indexed as a heading; the expandable `details` pattern is fine for AI and FAQ markup)
- H2 Blogs, then blog titles as H3
- Footer: contact label, not a page-level H2

## Why H4 to H6 are absent, and whether to add them
There is no content depth that needs them on a homepage. Adding empty H4 to H6 for show would hurt accessibility. If you add price tables and FAQs as separate sections, use H3 for sub-parts, not H4 to H6.
