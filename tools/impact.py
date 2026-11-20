"""Impact Studies: the home page section that shows the newest CodeNinja Atoms videos (Umar, 20 Nov 2026).

Replaces the home page "Watch it work" film. Layout follows a news grid: a left rail with the eyebrow,
sector chips and a "See all" button that opens the YouTube channel, and a three column grid of cards
(thumbnail, date and length, title, sector tags). Six cards show; the chips filter across every video.

Each build refreshes the list from the channel page when online and caches it in impact/videos.json,
so a build without a network still renders. Thumbnails are copied into assets/impact/ (our own videos).
    python tools/impact.py      # refresh the cache and thumbnails
"""
import html, json, re, urllib.request
from pathlib import Path
import brand

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "impact" / "videos.json"
THUMBS = ROOT / "assets" / "impact"
CHANNEL = dict(brand.SOCIAL)["YouTube"]
SHOW = 6
E = lambda s: html.escape(str(s), quote=True)
UA = {"User-Agent": "Mozilla/5.0", "Accept-Language": "en"}

# Sector tags read from the title, first match wins per tag group.
TAGS = [("Ports", r"\bport|pier|berth|container"), ("Rail", r"\brail"), ("Utilities", r"utilit|power line|wildfire|grid"),
        ("Mining", r"mining|tailings|mine\b"), ("Aviation", r"aircraft|aviation|\bmro\b"), ("Logistics", r"warehouse|cold chain|logistic"),
        ("Food", r"listeria|food"), ("Energy", r"pipeline|\bgas\b|oil"), ("Defense", r"defen[cs]e|depot"), ("Water", r"\bwater")]


def _get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=20).read().decode("utf-8", "replace")


def fetch():
    """The channel's videos, newest first: id, title, date (YYYY-MM-DD), seconds."""
    page = _get(CHANNEL + "/videos")
    data = json.loads(re.search(r"var ytInitialData = (\{.*?\});</script>", page).group(1))
    ids, seen = [], set()

    def walk(o):
        if isinstance(o, dict):
            v = o.get("videoRenderer")
            if v and v["videoId"] not in seen:
                seen.add(v["videoId"]); ids.append((v["videoId"], "".join(r["text"] for r in v["title"]["runs"])))
            lv = o.get("lockupViewModel")
            if lv and lv.get("contentId") and lv["contentId"] not in seen:
                seen.add(lv["contentId"])
                ids.append((lv["contentId"], lv.get("metadata", {}).get("lockupMetadataViewModel", {}).get("title", {}).get("content", "")))
            for x in o.values(): walk(x)
        elif isinstance(o, list):
            for x in o: walk(x)
    walk(data)
    old = {v["id"]: v for v in load()}
    out = []
    for vid, title in ids:
        if vid in old:
            v = dict(old[vid]); v["title"] = title or v["title"]; out.append(v); continue
        w = _get(f"https://www.youtube.com/watch?v={vid}")
        d = re.search(r'"publishDate":"(\d{4}-\d\d-\d\d)', w)
        s = re.search(r'"lengthSeconds":"(\d+)"', w)
        out.append({"id": vid, "title": title, "date": d.group(1) if d else "", "seconds": int(s.group(1)) if s else 0})
    out.sort(key=lambda v: v["date"], reverse=True)  # stable: channel order breaks ties
    return out


def load():
    try:
        return json.loads(CACHE.read_text())
    except Exception:
        return []


def thumbs(videos):
    THUMBS.mkdir(parents=True, exist_ok=True)
    for v in videos:
        f = THUMBS / f"{v['id']}.jpg"
        if f.exists():
            continue
        for q in ("maxresdefault", "hqdefault"):
            try:
                f.write_bytes(urllib.request.urlopen(urllib.request.Request(f"https://i.ytimg.com/vi/{v['id']}/{q}.jpg", headers=UA), timeout=20).read())
                break
            except Exception:
                pass


def refresh():
    try:
        vids = fetch()
        if vids:
            CACHE.parent.mkdir(exist_ok=True)
            CACHE.write_text(json.dumps(vids, indent=1, ensure_ascii=False))
    except Exception as e:
        print("impact: channel refresh failed, using cache:", type(e).__name__)
    vids = load()
    thumbs(vids)
    return vids


def clean(t):
    return re.sub(r"\s*\|\s*Sovereign AI\s*$", "", t).strip()


def tags(t):
    return [n for n, rx in TAGS if re.search(rx, t, re.I)][:2] or ["Physical AI"]


CSS = """
.impact{scroll-margin-top:100px;background:var(--paper);color:var(--ink);border-top:1px solid var(--rule-l)}
.impact .igrid{max-width:none;display:grid;grid-template-columns:minmax(220px,1fr) 3fr;border-bottom:1px solid var(--rule-l)}
.impact .rail{padding:56px 32px 56px var(--gutter);position:sticky;top:96px;align-self:start}
.impact .eyb{font-family:var(--mono);font-size:12px;letter-spacing:.08em;text-transform:uppercase;margin:0 0 36px;display:flex;align-items:center;gap:10px}
.impact .eyb::before{content:"";width:9px;height:9px;background:var(--ink)}
.impact .rail h2{font-weight:300;font-size:clamp(28px,2.6vw,40px);line-height:1.05;letter-spacing:-.03em;margin:0 0 28px}
.impact .ichips{display:flex;flex-direction:column;align-items:flex-start;gap:10px;margin:0 0 36px}
.impact .ichips button{font:400 12px/1 var(--mono);letter-spacing:.06em;text-transform:uppercase;padding:9px 12px;border:1px solid transparent;background:rgba(30,31,43,.07);color:var(--ink);cursor:pointer}
.impact .ichips button:hover{border-color:var(--ink)}.impact .ichips button[aria-pressed="true"]{background:transparent;border-color:var(--ink)}
.impact .cards{display:grid;grid-template-columns:repeat(3,1fr);gap:0;margin:0;padding:0;border:0}
.impact .ic{border-left:1px solid var(--rule-l);border-top:1px solid var(--rule-l);padding:32px 28px 40px;color:var(--ink);text-decoration:none;display:flex;flex-direction:column}
.impact .ic:nth-child(-n+3){border-top:0}
.impact .ic[hidden]{display:none}
.impact .ic .im{position:relative;aspect-ratio:16/9;overflow:hidden;background:#111;margin-bottom:22px}
.impact .ic img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .5s ease}
.impact .ic:hover img{transform:scale(1.03)}
.impact .ic .play{position:absolute;left:14px;bottom:14px;width:40px;height:40px;border-radius:50%;background:rgba(255,255,255,.92);display:grid;place-items:center}
.impact .ic .play::after{content:"";border-left:11px solid var(--ink);border-top:7px solid transparent;border-bottom:7px solid transparent;margin-left:3px}
.impact .ic .meta{font-family:var(--mono);font-size:12px;letter-spacing:.06em;color:var(--muted-l);margin:0 0 12px}
.impact .ic h3{font-weight:400;font-size:clamp(18px,1.5vw,22px);line-height:1.22;letter-spacing:-.018em;margin:0 0 20px}
.impact .ic:hover h3{text-decoration:underline;text-underline-offset:3px;text-decoration-thickness:1px}
.impact .ic .tg{margin-top:auto;display:flex;gap:8px;flex-wrap:wrap}
.impact .ic .tg span{font-family:var(--mono);font-size:11.5px;letter-spacing:.06em;text-transform:uppercase;padding:8px 11px;background:rgba(30,31,43,.07)}
@media (max-width:1100px){.impact .cards{grid-template-columns:repeat(2,1fr)}.impact .ic:nth-child(-n+3){border-top:1px solid var(--rule-l)}.impact .ic:nth-child(-n+2){border-top:0}}
@media (max-width:760px){.impact .igrid{grid-template-columns:1fr}.impact .rail{position:static;padding:56px var(--gutter) 28px}
.impact .ichips{flex-direction:row;flex-wrap:wrap}.impact .cards{grid-template-columns:1fr}.impact .ic{border-left:0;padding:28px var(--gutter) 36px}
.impact .ic:nth-child(-n+2){border-top:1px solid var(--rule-l)}.impact .ic:first-child{border-top:0}}
"""

JS = """<script>(function(){var s=document.getElementById('impact');if(!s)return;var N=%d,bs=s.querySelectorAll('.ichips button'),cs=s.querySelectorAll('.ic');
function show(t){var n=0;cs.forEach(function(c){var ok=t==='all'||(' '+c.dataset.t+' ').indexOf(' '+t+' ')>-1;c.hidden=!(ok&&n<N);if(ok&&n<N)n++;});
bs.forEach(function(b){b.setAttribute('aria-pressed',b.dataset.t===t?'true':'false')});}
bs.forEach(function(b){b.addEventListener('click',function(){show(b.dataset.t)})});})();</script>""" % SHOW


def section(videos=None, prefix=""):
    vids = load() if videos is None else videos
    if not vids:
        return ""
    counts = {}
    for v in vids:
        for t in tags(v["title"]):
            counts[t] = counts.get(t, 0) + 1
    chips = ['<button type="button" data-t="all" aria-pressed="true">Latest</button>'] + [
        f'<button type="button" data-t="{E(t.lower().replace(" ", "-"))}" aria-pressed="false">{E(t)}</button>'
        for t, _ in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:7]]
    cards = []
    for i, v in enumerate(vids):
        tg = tags(v["title"])
        d = v["date"].replace("-", ".")
        m = max(1, round(v["seconds"] / 60)) if v.get("seconds") else 0
        meta = f"{d} • {m} MIN WATCH" if m else d
        cards.append(
            f'<a class="ic" href="https://www.youtube.com/watch?v={E(v["id"])}" target="_blank" rel="noopener" data-t="{E(" ".join(t.lower().replace(" ", "-") for t in tg))}"{" hidden" if i >= SHOW else ""}>'
            f'<div class="im"><img src="{prefix}assets/impact/{E(v["id"])}.jpg" alt="" loading="lazy" width="1280" height="720"><i class="play" aria-hidden="true"></i></div>'
            f'<p class="meta">{E(meta)}</p><h3>{E(clean(v["title"]))}</h3><div class="tg">{"".join(f"<span>{E(t)}</span>" for t in tg)}</div></a>')
    return (f'<section id="impact" class="impact" aria-label="Impact Studies"><div class="igrid"><div class="rail"><p class="eyb">Videos</p>'
            f'<h2>Impact Studies</h2>'
            f'<div class="ichips">{"".join(chips)}</div><a class="btn dark" href="{CHANNEL}" target="_blank" rel="noopener">See all</a></div>'
            f'<div class="cards">{"".join(cards)}</div></div></section>{JS}')


def ld(videos=None):
    vids = (load() if videos is None else videos)[:SHOW]
    return {"@context": "https://schema.org", "@type": "ItemList", "name": "CodeNinja Atoms Impact Studies",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "item": {
                "@type": "VideoObject", "name": clean(v["title"]), "description": clean(v["title"]),
                "thumbnailUrl": f"https://codeatoms.ai/assets/impact/{v['id']}.jpg", "uploadDate": v["date"],
                "duration": f"PT{v['seconds'] // 60}M{v['seconds'] % 60}S", "embedUrl": f"https://www.youtube.com/embed/{v['id']}",
                "url": f"https://www.youtube.com/watch?v={v['id']}"}} for i, v in enumerate(vids)]}


if __name__ == "__main__":
    v = refresh()
    print(len(v), "videos;", sum((THUMBS / f"{x['id']}.jpg").exists() for x in v), "thumbnails")
