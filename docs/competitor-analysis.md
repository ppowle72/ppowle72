# Competitor homepage comparison: what was verified and what was not

## Read this first
The cloud environment's network policy blocks every competitor domain (rqdfarm.in, aamrai.com, foodwalas.com, devgadmango.com, ratnagirialphonsomango.com, ratnagirifarms.com) and Google's developer docs. Both `WebFetch` and `curl` were denied, and `WebSearch` returns only summaries, not People Also Ask boxes or AI Overview citations.

So **no competitor homepage was actually read.** There are no verified word counts, headings, schema types or on-page elements for any competitor. Everything below comes from search-result titles and snippets only, and is labelled that way. Nothing here should be treated as a measurement.

## Who surfaced (search results only)
| Site | Why it surfaced | Verified from snippets only |
|---|---|---|
| rqdfarm.in | Product pages for "order alphonso mangoes online" and "alphonso mango price per dozen"; city pages | Ratnagiri/Devgad Hapus, pan-India delivery, "no carbide" claim, size grades A/C/Jumbo with gram ranges, 4-dozen boxes, city URLs such as `/alphonso-mangoes/pune` and `/agra` |
| aamrai.com | Dominated "order alphonso mangoes online" and "buy alphonso mango online india", mostly through blog posts | GI-tagged Ratnagiri/Devgad, organic certifications named (NPOP, NOP, JAS), haystack ripening, buying-guide posts ("Dos and Don'ts of Buying Alphonso Mangoes Online", "Ratnagiri vs Devgad") |
| foodwalas.com | Separate Ratnagiri and Devgad product pages | GI tag, farmer-sourced, Devgad dozen from about ₹1,550 in a snippet |
| devgadmango.com | Devgad farmer co-operative; ranks for "how to identify real alphonso" and Ratnagiri vs Devgad | Blog-style content, Devgad origin |
| ratnagirialphonsomango.com, ratnagirifarms.com, agrophonics.com | Appeared only for an extended search | Titles only |

alphonsomango.in itself surfaced for "buy alphonso mango online india" and "alphonso mango online" through a blog post and `/collections/mangoes`.

## What the search evidence does support (patterns, not homepage facts)
1. **Informational content earns commercial-query visibility.** aamrai.com's visibility for "buy alphonso mango online india" is mostly blog URLs: buying guides and comparisons.
2. **Grade-specific product pages.** rqdfarm.in puts size grade and gram range in product titles and URLs.
3. **Origin-specific product pages.** Foodwalas and AAMRAI split Ratnagiri and Devgad into separate pages. We already do this (`/products/ratnagiri-alphonso-mango`, `/products/devgad-alphonso-mango`).
4. **City pages on one URL pattern.** rqdfarm.in uses `/alphonso-mangoes/{city}`, including smaller cities.
5. **Certification-led trust copy.** GI (Foodwalas), organic NPOP/NOP/JAS (AAMRAI), "no carbide / naturally ripened" (RQD, AAMRAI).
6. **Content gap:** "difference between ratnagiri and devgad hapus" returned weak results in search, so a clear answer page has little competition.

## Where this leaves the homepage (our side is verified from the Shopify theme)
| Element | alphonsomango.in after this PR | Competitor status |
|---|---|---|
| Visible prices | Live per-dozen table by size | not verified |
| Ratnagiri vs Devgad comparison + verdict | Table + FAQ answer | AAMRAI/Devgad Mango/RQD rank with blog posts on it |
| FAQ | 10 visible questions, matching FAQPage JSON-LD | not verified |
| Order steps | 3-step block | not verified |
| City section | Six metros named, free delivery | RQD has per-city pages |
| Certifications on page | FSSAI, APEDA, GI AU numbers in body text | GI/NPOP claims in snippets |
| Grade/size detail | Size ranges in the price table | RQD puts grades in URLs |

## What we are still missing (gaps worth building)
1. **City landing pages** (`/pages/...` or blog posts) for Mumbai, Bangalore, Chennai, Kolkata, Delhi, Hyderabad, each with local delivery time, price table and FAQ. The homepage only has one paragraph. The theme already has city blog templates in the schema, so check what exists before adding more.
2. **A standalone "Ratnagiri vs Devgad Alphonso" article** targeting "difference between ratnagiri and devgad hapus" and linking back to the homepage table.
3. **A "how to identify real Alphonso" buying guide** (competitors rank for this; we have the GI authorisation numbers to back it).
4. **Grade/size detail in product titles** (e.g. gram range in the product title) as RQD does.
5. **Pre-order / season-alert capture** while fresh fruit is out of stock. I did not add this because I don't know if you take pre-orders.

## To get the real homepage comparison
Choose one:
- **Allow the domains.** In the cloud environment menu in the session title bar, choose Edit, then Network access. Either broaden access or use Custom and add the competitor domains plus Google's developer docs under Allowed domains, keeping the default package-manager list. See https://code.claude.com/docs/en/cloud-environments#network-access. Then ask me to re-run it.
- **Paste data.** View-source HTML of each competitor homepage, or a Screaming Frog crawl export, and I will fill in headings, word counts and schema types.
