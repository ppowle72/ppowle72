"""Create a PAUSED Google Ads Demand Gen retargeting campaign from demandgen_config.json.

    pip install pillow google-ads python-dotenv
    python gads_demandgen.py              # PREVIEW: checks the config, your images and audiences, then asks
                                          # Google to validate the whole campaign WITHOUT creating anything
    python gads_demandgen.py --apply      # creates it, PAUSED (it cannot spend until you enable it)

One ad is created per entry in "ads" (one product page each). The campaign, budget, ad group, audiences, images and ads are sent in ONE request: if anything is
wrong, nothing is created. Images in the folder are sorted by shape: landscape 1.91:1, square 1:1,
portrait 4:5; files whose name starts with "logo" are the logo (square).
Uses the same .env as the other gads_*.py scripts.
"""
import argparse
import json
import os
import sys
import time

from dotenv import load_dotenv
from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException
from PIL import Image

LANG = {"en": "languageConstants/1000", "hi": "languageConstants/1023", "mr": "languageConstants/1101"}
INDIA = "geoTargetConstants/2356"
MAX_BYTES = 5 * 1024 * 1024


def digits(v):
    return "".join(c for c in (v or "") if c.isdigit())


def load_config(path):
    if not os.path.exists(path):
        sys.exit(f"{path} not found. Copy demandgen_config.example.json to {path} and fill it in.")
    with open(path, encoding="utf-8") as f:
        c = json.load(f)
    errs = []
    if not c.get("campaign_name"):
        errs.append("campaign_name is empty")
    if not c.get("daily_budget_inr") or c["daily_budget_inr"] <= 0:
        errs.append("daily_budget_inr must be set to a real amount (it is 0)")
    if not c.get("max_cpc_inr") or c["max_cpc_inr"] <= 0:
        errs.append("max_cpc_inr must be set (it caps what one click can cost)")
    if len(c.get("business_name", "")) > 25 or not c.get("business_name"):
        errs.append("business_name must be 1 to 25 characters")
    ads = c.get("ads")
    if not ads:  # old single-ad format
        ads = [{k: c[k] for k in ("name", "final_url", "images_folder", "headlines", "descriptions") if k in c}]
        c["ads"] = ads
    for i, a in enumerate(ads, 1):
        tag = f"ad {i} ({a.get('name', '?')})"
        a.setdefault("name", f"ad {i}")
        if not str(a.get("final_url", "")).startswith("https://alphonsomango.in"):
            errs.append(f"{tag}: final_url must start with https://alphonsomango.in")
        h, d = a.get("headlines", []), a.get("descriptions", [])
        if not 3 <= len(h) <= 5:
            errs.append(f"{tag}: give 3 to 5 headlines")
        if not 1 <= len(d) <= 5:
            errs.append(f"{tag}: give 1 to 5 descriptions")
        errs += [f"{tag}: headline too long ({len(x)}>40): {x}" for x in h if len(x) > 40]
        errs += [f"{tag}: description too long ({len(x)}>90): {x}" for x in d if len(x) > 90]
        if not a.get("images_folder"):
            errs.append(f"{tag}: images_folder missing")
    if errs:
        sys.exit("Config problems:\n  - " + "\n  - ".join(errs))
    return c


def scan_images(folder, logo_file=None):
    if not os.path.isdir(folder):
        sys.exit(f"images_folder not found: {folder}")
    out = {"landscape": [], "square": [], "portrait": [], "logo": []}
    for fn in sorted(os.listdir(folder)):
        p = os.path.join(folder, fn)
        if not fn.lower().endswith((".png", ".jpg", ".jpeg")):
            continue
        if os.path.getsize(p) > MAX_BYTES:
            print(f"  skip {fn}: larger than 5 MB")
            continue
        w, h = Image.open(p).size
        r = w / h
        if fn.lower().startswith("logo"):
            kind, ok = "logo", 0.95 <= r <= 1.05 and w >= 128
        elif 1.7 <= r <= 2.1:
            kind, ok = "landscape", w >= 600 and h >= 314
        elif 0.95 <= r <= 1.05:
            kind, ok = "square", w >= 300
        elif 0.75 <= r <= 0.85:
            kind, ok = "portrait", w >= 480 and h >= 600
        else:
            print(f"  skip {fn}: shape {w}x{h} is not 1.91:1, 1:1 or 4:5")
            continue
        if not ok:
            print(f"  skip {fn}: too small for {kind} ({w}x{h})")
            continue
        out[kind].append(p)
        print(f"  {kind:<9} {fn} ({w}x{h})")
    if not out["logo"] and logo_file and os.path.exists(logo_file):
        out["logo"].append(logo_file)
        print(f"  logo      {os.path.basename(logo_file)} (shared)")
    for k in ("landscape", "square", "logo"):
        if not out[k]:
            sys.exit(f"Need at least one {k} image in {folder}")
    return {k: v[:5] for k, v in out.items()}


def build_operations(client, cid, cfg, list_rn, images, ts):
    """Return (ops, names, index_of_campaign_op). Temporary negative IDs link the resources together."""
    ops, names = [], []
    en = client.enums
    budget_rn = client.get_service("CampaignBudgetService").campaign_budget_path(cid, -1)
    campaign_rn = client.get_service("CampaignService").campaign_path(cid, -2)
    ad_group_rn = client.get_service("AdGroupService").ad_group_path(cid, -3)

    def add(name):
        mo = client.get_type("MutateOperation")
        ops.append(mo)
        names.append(name)
        return mo

    b = add("budget").campaign_budget_operation.create
    b.resource_name = budget_rn
    b.name = f"{cfg['campaign_name']} budget {ts}"
    b.amount_micros = int(cfg["daily_budget_inr"] * 1_000_000)
    b.delivery_method = en.BudgetDeliveryMethodEnum.STANDARD
    b.explicitly_shared = False

    c = add("campaign").campaign_operation.create
    campaign_idx = len(ops) - 1
    c.resource_name = campaign_rn
    c.name = cfg["campaign_name"]
    c.status = en.CampaignStatusEnum.PAUSED
    c.advertising_channel_type = en.AdvertisingChannelTypeEnum.DEMAND_GEN
    c.campaign_budget = budget_rn
    c.target_spend.cpc_bid_ceiling_micros = int(cfg["max_cpc_inr"] * 1_000_000)  # = Maximize clicks
    c.contains_eu_political_advertising = en.EuPoliticalAdvertisingStatusEnum.DOES_NOT_CONTAIN_EU_POLITICAL_ADVERTISING
    c.geo_target_type_setting.positive_geo_target_type = en.PositiveGeoTargetTypeEnum.PRESENCE

    cc = add("location India").campaign_criterion_operation.create
    cc.campaign = campaign_rn
    cc.location.geo_target_constant = INDIA
    for code in cfg.get("languages", ["en"]):
        cc = add(f"language {code}").campaign_criterion_operation.create
        cc.campaign = campaign_rn
        cc.language.language_constant = LANG[code]

    ag = add("ad group").ad_group_operation.create
    ag.resource_name = ad_group_rn
    ag.name = f"{cfg['campaign_name']} - ad group"
    ag.campaign = campaign_rn
    ag.status = en.AdGroupStatusEnum.ENABLED
    if cfg.get("optimized_targeting") is not None:
        ag.optimized_targeting_enabled = bool(cfg["optimized_targeting"])

    for nm in cfg["target_lists"]:
        x = add(f"target {nm}").ad_group_criterion_operation.create
        x.ad_group = ad_group_rn
        x.user_list.user_list = list_rn[nm]
    for nm in cfg["exclude_lists"]:
        x = add(f"exclude {nm}").ad_group_criterion_operation.create
        x.ad_group = ad_group_rn
        x.negative = True
        x.user_list.user_list = list_rn[nm]

    tmp = -10
    for ai, ad_cfg in enumerate(cfg["ads"]):
        asset_rn = {}
        for kind, paths in images[ai].items():
            for p in paths:
                tmp -= 1
                a = add(f"{ad_cfg['name']}: image {os.path.basename(p)}").asset_operation.create
                a.resource_name = client.get_service("AssetService").asset_path(cid, tmp)
                a.name = f"{cfg['campaign_name']} {ad_cfg['name']} {os.path.basename(p)} {ts}"
                with open(p, "rb") as f:
                    a.image_asset.data = f.read()
                asset_rn[(kind, p)] = a.resource_name

        aga = add(f"ad: {ad_cfg['name']}").ad_group_ad_operation.create
        aga.ad_group = ad_group_rn
        aga.status = en.AdGroupAdStatusEnum.ENABLED
        ad = aga.ad
        ad.name = f"{cfg['campaign_name']} - {ad_cfg['name']}"
        ad.final_urls.append(ad_cfg["final_url"])
        d = ad.demand_gen_multi_asset_ad
        target = {"landscape": d.marketing_images, "square": d.square_marketing_images,
                  "portrait": d.portrait_marketing_images, "logo": d.logo_images}
        for (kind, _p), rn in asset_rn.items():
            img = client.get_type("AdImageAsset")
            img.asset = rn
            target[kind].append(img)
        for h in ad_cfg["headlines"]:
            t = client.get_type("AdTextAsset")
            t.text = h
            d.headlines.append(t)
        for x in ad_cfg["descriptions"]:
            t = client.get_type("AdTextAsset")
            t.text = x
            d.descriptions.append(t)
        d.business_name = cfg["business_name"]
        d.call_to_action_text = cfg.get("call_to_action", "Shop now")
    return ops, names, campaign_idx


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--config", default="demandgen_config.json")
    args = ap.parse_args()
    load_dotenv()
    cfg = load_config(args.config)
    print("Config OK:", cfg["campaign_name"], f"| Rs {cfg['daily_budget_inr']}/day | max click Rs {cfg['max_cpc_inr']}")
    images = []
    for a in cfg["ads"]:
        print(f"Images for {a['name']}:")
        images.append(scan_images(a["images_folder"], cfg.get("logo_file")))

    gcfg = {"developer_token": os.environ["GOOGLE_ADS_DEVELOPER_TOKEN"], "client_id": os.environ["GOOGLE_ADS_CLIENT_ID"],
            "client_secret": os.environ["GOOGLE_ADS_CLIENT_SECRET"], "refresh_token": os.environ["GOOGLE_ADS_REFRESH_TOKEN"],
            "use_proto_plus": True}
    if digits(os.environ.get("GOOGLE_ADS_LOGIN_CUSTOMER_ID")):
        gcfg["login_customer_id"] = digits(os.environ["GOOGLE_ADS_LOGIN_CUSTOMER_ID"])
    client = GoogleAdsClient.load_from_dict(gcfg)
    cid = digits(os.environ["GOOGLE_ADS_CUSTOMER_ID"])
    svc = client.get_service("GoogleAdsService")

    def q(s):
        return [r for b in svc.search_stream(customer_id=cid, query=s) for r in b.results]

    cur = q("SELECT customer.currency_code FROM customer")[0].customer.currency_code
    if cur != "INR":
        sys.exit(f"Account currency is {cur}, not INR. Budget amounts in the config are in the account currency; adjust and retry.")
    safe = cfg["campaign_name"].replace("'", "\\'")
    if q(f"SELECT campaign.id FROM campaign WHERE campaign.name = '{safe}' AND campaign.status != 'REMOVED'"):
        sys.exit(f"A campaign named '{cfg['campaign_name']}' already exists. Change campaign_name.")

    lists = {r.user_list.name: (r.user_list.resource_name, r.user_list.size_for_search)
             for r in q("SELECT user_list.name, user_list.resource_name, user_list.size_for_search FROM user_list")}
    list_rn, missing = {}, []
    print("Audiences:")
    for role, names in (("target ", cfg["target_lists"]), ("exclude", cfg["exclude_lists"])):
        for nm in names:
            if nm in lists:
                list_rn[nm] = lists[nm][0]
                print(f"  {role} {nm} ({lists[nm][1]} users)")
            else:
                missing.append(nm)
    if missing:
        sys.exit("These audience lists do not exist in Google Ads (check the exact names): " + ", ".join(missing))

    ops, names, campaign_idx = build_operations(client, cid, cfg, list_rn, images, str(int(time.time())))
    req = client.get_type("MutateGoogleAdsRequest")
    req.customer_id = cid
    req.mutate_operations.extend(ops)
    req.validate_only = not args.apply
    print(f"\n{'CREATING' if args.apply else 'VALIDATING (nothing is created)'}: {len(ops)} operations")
    try:
        resp = svc.mutate(request=req)
    except GoogleAdsException as e:
        print("\nGoogle rejected it, so nothing was created:")
        for err in e.failure.errors:
            idx = err.location.field_path_elements[0].index if err.location.field_path_elements else None
            print(f"  - [{names[idx] if idx is not None and idx < len(names) else '?'}] {err.message}")
        sys.exit(1)
    if not args.apply:
        print("\nVALID. Google would accept this campaign. Run again with --apply to create it (paused).")
        return
    rn = resp.mutate_operation_responses[campaign_idx].campaign_result.resource_name
    print("\nCreated PAUSED campaign:", rn)
    print("Open Google Ads > Campaigns, review it, then enable it when you are ready.")


if __name__ == "__main__":
    main()
