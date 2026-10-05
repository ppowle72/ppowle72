# Backlink profiles: alphonsomango.in vs dhanshefarm.com (5 Oct 2026)

Sources you supplied: Ahrefs backlinks for alphonsomango.in (1,985), Ahrefs backlinks for dhanshefarm.com (1,146, revised file), SEMrush backlinks for alphonsomango.in (28,762). The Ahrefs files carry Ahrefs' own "Is spam" flag. The SEMrush file does not, so for SEMrush I describe patterns instead. The two tools index very different sets of links (1,985 vs 28,762), mostly because SEMrush has crawled thousands of directory pages that Ahrefs skips. Neither export shows traffic or rankings effects, so nothing here proves a link helped or hurt.

Files: `alphonsomango-backlinks-nonspam.csv`, `alphonsomango-ahrefs-spam-flagged.csv`, `alphonsomango-semrush-backlinks-by-domain.csv`, `alphonsomango-semrush-freeblog-network-links.csv`, `dhanshefarm-backlinks-nonspam.csv`.

## Side by side (Ahrefs)
| | alphonsomango.in | dhanshefarm.com |
|---|---|---|
| Backlinks | 1,985 | 1,146 |
| Flagged spam by Ahrefs | 1,300 (65%) | 1,099 (96%) |
| Not flagged | **685** | **47** |
| Not flagged with Domain Rating 20+ | 397 | 17 |
| ... 40+ | 230 | 13 |
| ... 60+ | 75 | 6 |
| ... 80+ | 30 | 1 |
| Links to the homepage | 1,133 | 1,142 |
| Nofollow among the not-flagged links | 31% | 30% |

We have roughly 14 times as many real links as Dhanshe Farm and far more from high-rating domains. Dhanshe's profile is almost entirely spam, so its ranking is not coming from links.

## What is good in our profile
Wikipedia ("Aamras recipe", Domain Rating 97), Wikiwand, DBpedia, Crunchbase, Razorpay, Shopify Community, StoreLeads, YourStory (a followed link with the anchor "Powle Home Foods", Domain Rating 85) and many directory and profile sites. Be realistic about them: about a third are nofollow, and many high-rating ones are profile, forum, university-blog or wiki pages (Docker Hub, about.me, Sketchfab, Wakelet, Diigo, university sites). They support brand and entity recognition, which helps AI answers, but they pass little keyword ranking power. We have almost no editorial links from news or food publications.

## Your press mentions are not showing up as links
None of the 12 press URLs you confirmed (NDTV, NDTV Web Stories, The Economic Times, ANI, LatestLY, The Better India x2, Fructidor, Inc42, LBB x2, the Ministry post) appear as a backlink to alphonsomango.in in either Ahrefs or SEMrush. Only YourStory does. Since you checked that those pages name AlphonsoMango.in, Powle Home Foods and Prashant Powle, they are probably **unlinked mentions** (or too new for the tools). One lookalike to avoid: `livemint24.com` in the Ahrefs list is not Mint, so do not describe it as Mint.

Action: ask each publisher to turn the brand name into a link to https://alphonsomango.in/. An editorial link from NDTV, ANI or The Better India is worth more than all the directory links combined. I put the press section live on the staged theme (see below).

## The risk in our profile
SEMrush shows 28,762 backlinks from 3,256 domains, and they look manufactured:
- **Quality:** median Authority Score 0. Only 22 links score 30 or more and none score 50 or more. 25,418 score exactly 0.
- **Concentration:** four directory domains hold 11,312 links (39%): homedirectory.biz (3,971), unique-listing.com (2,777), justdirectory.org (2,374), classdirectory.org (2,190). 28 domains with 50 or more links each account for 15,938 links.
- **Repeated exact-match anchors:** "Khajoor" (6,162 links), "buy ajwa dates online *" (2,777), "mango rate in delhi per kg" (2,374). These three anchors are 39% of all links.
- **Where they point:** the Medjool dates page (6,883 links), the Ajwa dates page (3,515), the Delhi mango-price blog post (2,378) and the saffron page (1,291). Few go to the homepage (2,888).
- **Blog-network posts:** 61 links from 30 keyword-named free-blog subdomains (activoblog.com, blogolenta.com, ageeksblog.com, blog-gold.com and others) with anchors like "Devgad Alphonso Mango" and "Alphonso Mango Online Order page". Listed in `alphonsomango-semrush-freeblog-network-links.csv`.
- **Churn:** 5,311 of the 28,762 links (18%) are already lost.
- **Ahrefs:** 641 of its 1,985 links are templated SEO-seller pages (the same SEOExpress and "Domain Report" pages seen on Dhanshe Farm's profile). Those are probably auto-generated when a domain is submitted to link-selling tools, not links we chose. The directory and free-blog links are different: they look deliberately built.

**Who built them?** I cannot tell from the data. If an SEO vendor or agency built the directory and free-blog links, you should know and stop paying for it. If you did not, they may be a scraper or a negative-SEO attempt.

**Is it hurting rankings?** No evidence of that here: the site ranks first to third for its core terms. Google says it mostly ignores low-quality links. The risk is a manual action if the pattern looks like manipulation.
1. Open Google Search Console, Security and manual actions, Manual actions, and confirm there is none.
2. Compare Search Console's Links report with these exports.
3. Do not bulk-disavow by default. Google advises disavowing only when you have a manual action or built the links and cannot get them removed. If you decide to, the domain lists are in the CSVs and the decision is yours.
4. If a vendor built the links, stop that work and keep the records.
5. Put effort into real links instead: press, food and farm blogs, and supplier or partner listings.

## Related sites that link to us
These came out of the SEMrush data and need your confirmation:
- **ratnagirihapus.store**, which I had listed as a competitor, links to our Hapus mango product page from at least 15 archive and tag pages between Nov 2022 and Sep 2026 (SEMrush first and last seen dates), with the anchor "alphonso mango".
- **ratnagirihapus.shop** (Authority Score 46) links to alphonsomango.in between Mar and Jul 2026, with anchors including "Proveda Superfoods Pvt Ltd at alphonsomango.in", "Enquire Corporate Hapus Gifting", and "Buy Hapus — ₹599/Dozen".
- **ratnagirimango.in** also appears in the data for the name Proveda (in its URL or anchor text; the export does not say which).

Are these your sister sites? If yes, they are not competitors, and the cross-links should be reviewed (they may look like a link network). Two follow-ups if they are yours:
- The ₹599 a dozen shown in those anchors does not match alphonsomango.in's live prices (from ₹1,849 a dozen). Keep prices consistent across sites.
- Your homepage and schema name **Powle Home Foods** as the operator, and the theme notes say Proveda Superfoods is a separate entity whose FSSAI and GST are pending. If Proveda now operates alphonsomango.in, tell me and I will revisit the entity statements. I will not change them without your word.

## Changes made to the staged theme
- The "Press and media" section is switched on (you confirmed the links name the brand). The 12 links are loaded.
