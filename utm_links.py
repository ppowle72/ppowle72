"""Build tagged links for every channel. Writes utm_links.csv; nothing is sent anywhere.

    python utm_links.py                         # links to the home page
    python utm_links.py https://alphonsomango.in/collections/mangoes
Rules baked in: lowercase, no spaces, one name per channel.
"""
import csv
import sys
from urllib.parse import urlencode

BASE = sys.argv[1] if len(sys.argv) > 1 else "https://alphonsomango.in/"
ROWS = [  # channel, where to paste it, source, medium, campaign
    ("Instagram bio", "Instagram profile website field", "instagram", "social", "bio"),
    ("Instagram story/post", "Link sticker / caption", "instagram", "social", "organic_post"),
    ("Instagram ads", "Meta Ads Manager > ad URL", "instagram", "paid_social", "mango_season"),
    ("Facebook page", "Page website / button link", "facebook", "social", "page"),
    ("Facebook ads", "Meta Ads Manager > ad URL", "facebook", "paid_social", "mango_season"),
    ("LinkedIn page", "Company page website", "linkedin", "social", "page"),
    ("LinkedIn post", "Post link", "linkedin", "social", "organic_post"),
    ("YouTube description", "Video / channel link", "youtube", "video", "channel"),
    ("WhatsApp broadcast", "Broadcast / catalog link", "whatsapp", "messaging", "broadcast"),
    ("Email newsletter", "Email tool buttons", "newsletter", "email", "monthly"),
    ("Google Maps / Business Profile", "Business Profile website field", "google", "organic", "gbp"),
]
with open("utm_links.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["channel", "paste_into", "url"])
    for ch, where, s, m, c in ROWS:
        url = BASE + ("&" if "?" in BASE else "?") + urlencode({"utm_source": s, "utm_medium": m, "utm_campaign": c})
        w.writerow([ch, where, url])
        print(f"{ch:<32} {url}")
print("\nSaved utm_links.csv. Do NOT tag Google Ads links: auto-tagging handles them.")
