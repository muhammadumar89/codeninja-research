"""Memos: /memos/ lists them, /memos/<slug>/ is one memo.

A memo is a signed letter from CodeNinja's leadership, not a blog post: no tags, no reading
time, no chrome. One file in memos/posts/<slug>.md (JSON front matter between '---' lines,
then the body). The newest memo's `banner` line is what the site-wide announcement bar
carries, which is why this module runs before every other page is written.
    python tools/memos.py       # site_index.py runs it first, then seo.py runs last
"""
import datetime, html, json, re, subprocess
from pathlib import Path
import brand
import blog  # markdown converter, author cards and date helper are shared

ROOT = Path(__file__).resolve().parent.parent
MEM = ROOT / "memos"
BASE = "https://codeatoms.ai"
E = lambda s: html.escape(str(s), quote=True)
INTRO = ("Memos from the people building CodeNinja. Longer arguments about how systems for the "
         "physical world should be built, and why we build ours the way we do.")


def load():
    out = []
    for f in sorted((MEM / "posts").glob("*.md")):
        raw = f.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
        meta, body = json.loads(m.group(1)), m.group(2).strip()
        meta.update(slug=f.stem, body=body, url=f"{BASE}/memos/{f.stem}/",
                    words=len(re.sub(r"[#*|!\[\]()]", " ", body).split()))
        out.append(meta)
    return sorted(out, key=lambda p: p["date"], reverse=True)


def banner():
    """(sentence, link text, href) for the site-wide bar, from the newest memo. None if no memos."""
    ms = load()
    if not ms:
        return None
    m = ms[0]
    line = m.get("banner") or f"Read our memo, {m['title']}"
    # the memo's own title is the underlined link, the rest is plain, as a letter announcement reads
    if m["title"] in line:
        before, _, after = line.partition(m["title"])
        return (before, m["title"], after, m["url"])
    return (line + " ", m["title"], "", m["url"])


CSS = """
body{background:var(--paper)}html.js header.top:not(.solid):not(.open){background:rgba(11,12,16,.94);border-bottom-color:var(--rule-d)}
.wrapm{max-width:760px;margin:0 auto;padding:132px var(--gutter) 112px}
.memo .eyebrow{margin:0 0 26px}
.memo h1{font-family:var(--sans);font-weight:300;font-size:clamp(40px,5.4vw,72px);line-height:1.02;letter-spacing:-.035em;color:var(--ink);margin:0 0 22px;max-width:16ch}
.memo .dek{font-family:var(--serif);font-weight:300;font-size:clamp(21px,2.2vw,27px);line-height:1.38;color:var(--muted-l);margin:0 0 40px;max-width:46ch}
.memo .from{display:flex;align-items:center;gap:14px;border-top:1px solid var(--ink);border-bottom:1px solid var(--rule-l);padding:18px 0;margin:0 0 56px;font-size:15px;color:var(--muted-l)}
.memo .from img{width:46px;height:46px;border-radius:50%;object-fit:cover;flex:none}
.memo .from b{display:block;color:var(--ink);font-weight:500;font-size:16px}
.memo .body{font-size:19.5px;line-height:1.68;color:rgba(30,31,43,.9)}
.memo .body p{margin:0 0 26px;max-width:68ch}
.memo .body h2{font-family:var(--sans);font-weight:400;font-size:clamp(23px,2.3vw,30px);line-height:1.15;letter-spacing:-.022em;color:var(--ink);margin:64px 0 20px;padding-top:26px;border-top:1px solid var(--rule-l);max-width:30ch}
.memo .body h3{font-weight:500;font-size:19px;color:var(--ink);margin:36px 0 10px}
.memo .body strong{font-weight:500;color:var(--ink)}
.memo .body a{color:var(--ink);text-decoration-thickness:1px;text-underline-offset:3px}
.memo .body ul,.memo .body ol{margin:0 0 26px;padding-left:22px}.memo .body li{margin:0 0 10px}
.memo .body blockquote{margin:32px 0;padding-left:22px;border-left:2px solid var(--ink);font-family:var(--serif);font-size:22px;line-height:1.45;color:var(--ink)}
.sign{margin:72px 0 0;padding-top:28px;border-top:1px solid var(--ink)}
.sign .nm{font-family:var(--serif);font-size:27px;color:var(--ink);line-height:1.2}
.sign .rl{font-family:var(--mono);font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted-l);margin-top:10px}
.after{border-top:1px solid var(--rule-l);margin-top:56px;padding-top:24px;font-size:15px;color:var(--muted-l)}.after a{color:var(--ink)}
.mlist{list-style:none;padding:0;margin:48px 0 0;border-top:1px solid var(--ink)}
.mlist li{padding:28px 0;border-bottom:1px solid var(--rule-l)}
.mlist .d{font-family:var(--mono);font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted-l)}
.mlist h2{font-weight:400;font-size:clamp(26px,3vw,38px);line-height:1.08;letter-spacing:-.025em;margin:10px 0 10px}
.mlist h2 a{color:var(--ink);text-decoration:none}.mlist h2 a:hover{text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:5px}
.mlist p{margin:0;color:var(--muted-l);font-size:17px;line-height:1.55;max-width:60ch}
.mlist small{display:block;margin-top:12px;font-family:var(--mono);font-size:10.5px;letter-spacing:.05em;text-transform:uppercase;color:var(--muted-l)}
@media (max-width:820px){.wrapm{padding:104px var(--gutter) 72px}.memo .body{font-size:18px}}
"""


def shell(path, title, desc, body, ld, og_image):
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{BASE}/{path}">
<meta property="og:type" content="article"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{BASE}/{path}">
<meta property="og:image" content="{E(og_image)}">
""" + "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in ld) + f"""{brand.FONTS}{brand.JS_FLAG}<style>{brand.CSS}{CSS}</style></head>
<body>{brand.header(BASE + "/")}
<main class="light"><div class="wrapm">{body}</div></main>
<footer class="site"><div class="wrapf">{brand.footer_brand(BASE + "/")}{brand.footer_links(BASE + "/")}<span>CodeNinja Atoms is a fully owned subsidiary of <a href="{brand.PARENT}">CodeNinja</a> · Memos are CC BY 4.0</span></div></footer>
{brand.SCRIPT}</body></html>"""


def memo_page(m):
    body_html, _ = blog.md_to_html(m["body"], m["slug"])
    a = blog.AUTHORS.get(m["author"], {})
    photo = f'<img src="{a["photo"]}" alt="" width="46" height="46">' if a.get("photo") else ""
    body = (f'<article class="memo"><p class="eyebrow">Memo · CodeNinja</p><h1>{E(m["title"])}</h1>'
            f'<p class="dek">{E(m["subtitle"])}</p>'
            f'<div class="from">{photo}<div><b>{E(m["author"])}</b>{E(m.get("author_role", ""))} · {blog.nice_date(m["date"])}</div></div>'
            f'<div class="body">{body_html}</div>'
            f'<div class="sign"><p class="nm">{E(m["author"])}</p><p class="rl">{E(m.get("author_role", ""))}</p></div>'
            f'<p class="after">CodeNinja is a Middle Eastern American artificial intelligence lab and system of context company. '
            f'We build sovereign systems that enterprises own, harden and run inside their own perimeter, and '
            f'<a href="{BASE}/praxis/">Praxis</a>, the platform that designs them. '
            f'<a href="{BASE}/memos/">All memos</a></p></article>')
    ld = [{"@context": "https://schema.org", "@type": "Article", "headline": m["title"], "alternativeHeadline": m["subtitle"],
           "description": m["description"], "url": m["url"], "mainEntityOfPage": m["url"], "image": f"{m['url']}cover.png",
           "datePublished": m["date"], "dateModified": m.get("updated", m["date"]), "inLanguage": "en", "wordCount": m["words"],
           "license": "https://creativecommons.org/licenses/by/4.0/", "genre": "memo",
           "author": {"@type": "Person", "name": m["author"], "jobTitle": m.get("author_role", ""), "url": a.get("url"), "sameAs": a.get("sameAs")},
           "publisher": {"@type": "Organization", "@id": f"{BASE}/#org", "name": "CodeNinja Atoms", "url": f"{BASE}/"}}]
    return shell(f"memos/{m['slug']}/", f'{m["title"]} | A memo from CodeNinja', m["description"], body, ld, f"{m['url']}cover.png")


def markdown_copy(m):
    """The memo as Markdown for agents and answer engines, alongside the page."""
    return (f'# {m["title"]}\n\n{m["subtitle"]}\n\nA memo by {m["author"]}, {m.get("author_role", "")}, {blog.nice_date(m["date"])}.\n'
            f'Canonical: {m["url"]}\nLicense: CC BY 4.0\nPublisher: CodeNinja Atoms (https://codeatoms.ai)\n\n{m["body"]}\n')


def index_page(ms):
    rows = "".join(f'<li><p class="d">{blog.nice_date(m["date"])}</p><h2><a href="{m["url"]}">{E(m["title"])}</a></h2>'
                   f'<p>{E(m["subtitle"])}</p><small>{E(m["author"])} · {E(m.get("author_role", ""))}</small></li>' for m in ms)
    body = (f'<article class="memo"><p class="eyebrow">Memos</p><h1>Memos</h1><p class="dek">{E(INTRO)}</p>'
            f'<ul class="mlist">{rows}</ul></article>')
    ld = [{"@context": "https://schema.org", "@type": "CollectionPage", "name": "Memos", "url": f"{BASE}/memos/",
           "description": INTRO, "publisher": {"@id": f"{BASE}/#org"},
           "hasPart": [{"@type": "Article", "headline": m["title"], "url": m["url"], "datePublished": m["date"]} for m in ms]}]
    return shell("memos/", "Memos | CodeNinja Atoms", INTRO, body, ld, f"{BASE}/assets/video/port-night.jpg")


def main():
    ms = load()
    if not ms:
        print("memos: none"); return
    for m in ms:
        d = MEM / m["slug"]
        d.mkdir(parents=True, exist_ok=True)
        _cover(m, d)
        (d / "index.html").write_text(memo_page(m), encoding="utf-8")
        (d / "index.md").write_text(markdown_copy(m), encoding="utf-8")
    (MEM / "index.html").write_text(index_page(ms), encoding="utf-8")
    print(f"memos: {len(ms)} ({', '.join(m['slug'] for m in ms)})")


def _cover(m, d):
    """Letterhead style share card, drawn once."""
    out = d / "cover.png"
    if out.exists():
        return
    mark = re.search(r'<path fill-rule="evenodd" clip-rule="evenodd" d="([^"]+)" fill="#E31E30">', brand.LOGO).group(1)
    page = f"""<!doctype html><html><head><meta charset="utf-8">{brand.FONTS}<style>
html,body{{margin:0;width:1600px;height:900px;background:#0B0C10;overflow:hidden}}
.t{{position:absolute;inset:0;padding:96px 110px;box-sizing:border-box;display:flex;flex-direction:column;justify-content:space-between;color:#F2F2F0;font-family:'Inter Tight',Arial,sans-serif}}
.grid{{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.05) 1px,transparent 1px);background-size:80px 80px}}
.rule{{position:absolute;left:110px;right:110px;top:188px;height:1px;background:rgba(242,242,240,.35)}}
.top{{display:flex;align-items:center;gap:18px;font-family:'Geist Mono',monospace;font-size:22px;letter-spacing:.08em;text-transform:uppercase;color:#A3A6AE}}
.top svg{{height:30px}}.top b{{color:#D9C3A3;font-weight:400}}
h1{{font-weight:300;font-size:120px;line-height:.98;letter-spacing:-.04em;margin:0;max-width:13ch}}
.sub{{font-family:'Newsreader',Georgia,serif;font-weight:300;font-size:34px;line-height:1.3;color:rgba(242,242,240,.82);max-width:32ch;margin-top:30px}}
.bot{{display:flex;justify-content:space-between;font-family:'Geist Mono',monospace;font-size:20px;letter-spacing:.06em;text-transform:uppercase;color:#A3A6AE}}
</style></head><body><div class="grid"></div><div class="rule"></div><div class="t">
<div class="top"><svg viewBox="0 0 60 34"><path fill-rule="evenodd" d="{mark}" fill="#E31E30"/></svg><span>CodeNinja <b>Atoms</b> · Memo</span></div>
<div><h1>{E(m['title'])}</h1><div class="sub">{E(m.get('cover_line') or m['subtitle'])}</div></div>
<div class="bot"><span>{E(m['author'])}, {E(m.get('author_role',''))}</span><span>{E(blog.nice_date(m['date']))}</span></div></div></body></html>"""
    tmp = d / "_cover.html"
    tmp.write_text(page, encoding="utf-8")
    subprocess.run([blog.CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--window-size=1600,900",
                    "--virtual-time-budget=4000", f"--screenshot={out}", tmp.as_uri()], capture_output=True)
    tmp.unlink()


if __name__ == "__main__":
    main()
