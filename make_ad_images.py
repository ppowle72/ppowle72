"""Turn ONE product photo into the three shapes Demand Gen needs (nothing is cropped: the photo is
centred on a white background), or make the square logo.

    python make_ad_images.py medjool.jpg ad_images\\medjool        # writes landscape / square / portrait
    python make_ad_images.py --logo mylogo.png ad_images\\logo.png  # writes a 512x512 square logo
Needs: pip install pillow
"""
import argparse
import os

from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument("source")
ap.add_argument("out")
ap.add_argument("--logo", action="store_true", help="make a square logo; 'out' is then a file name")
args = ap.parse_args()


def on_canvas(img, w, h, margin=0.92):
    scale = min(w * margin / img.width, h * margin / img.height)
    im = img.resize((max(1, int(img.width * scale)), max(1, int(img.height * scale))), Image.LANCZOS)
    canvas = Image.new("RGB", (w, h), (255, 255, 255))
    if im.mode in ("RGBA", "LA"):
        canvas.paste(im, ((w - im.width) // 2, (h - im.height) // 2), im.convert("RGBA"))
    else:
        canvas.paste(im.convert("RGB"), ((w - im.width) // 2, (h - im.height) // 2))
    return canvas


src = Image.open(args.source)
if args.logo:
    on_canvas(src, 512, 512).save(args.out, "PNG")
    print("wrote", args.out)
else:
    os.makedirs(args.out, exist_ok=True)
    for name, size in (("landscape.jpg", (1200, 628)), ("square.jpg", (1200, 1200)), ("portrait.jpg", (960, 1200))):
        p = os.path.join(args.out, name)
        on_canvas(src, *size).save(p, "JPEG", quality=90)
        print("wrote", p)
