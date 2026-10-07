"""The engineering blog: /blog/ lists every post, /blog/<slug>/ is one post.
One post = one Markdown file in blog/posts/<slug>.md (a JSON front matter block between
'---' lines, then the body) plus its figures in blog/<slug>/figures/. The cover tile is drawn
here (headless Chrome) so every post has a share image in the house style.
    python tools/blog.py        # site_index.py runs it first, then seo.py runs last
Structure follows the posts on the Palantir blog: tag chips, title, one-line subtitle, author,
date and reading time, a cover, prose in short sections with captioned figures, an author
block at the end.
"""
import html, json, re, datetime, subprocess, math
from pathlib import Path
import brand

ROOT = Path(__file__).resolve().parent.parent
BLOG = ROOT / "blog"
BASE = "https://codeatoms.ai"
E = lambda s: html.escape(str(s), quote=True)
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
AUTHORS = {"Umar Bilal": {"photo": f"{BASE}/about/img/muhammad-umar-bilal.jpg", "sameAs": "https://www.linkedin.com/in/muhammadumargiki/",
                          "url": f"{BASE}/about/#muhammad-umar-bilal"}}
INTRO = "Writing from the engineers building a sovereign AI operating system for the physical world."


# ---------------------------------------------------------------- markdown
def inline(s):
    s = E(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2">\1</a>', s)
    s = re.sub(r'(?<!href=")(?<!">)(https?://[^\s<]+?)([.,;)]?)(?=\s|$|<)', r'<a href="\1">\1</a>\2', s)
    return s


def slugify(t):
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")[:60]


def md_to_html(md, slug):
    out, i, L = [], 0, md.split("\n")
    toc = []
    while i < len(L):
        ln = L[i]
        if not ln.strip():
            i += 1; continue
        if ln.startswith("### "):
            out.append(f"<h3>{inline(ln[4:])}</h3>")
        elif ln.startswith("## "):
            t = ln[3:]; a = slugify(t); toc.append((a, t))
            out.append(f'<h2 id="{a}">{inline(t)}</h2>')
        elif ln.startswith("!["):
            m = re.match(r"!\[([^\]]*)\]\(([^)]+)\)", ln)
            alt, src = m.group(1), m.group(2)
            cap = ""
            if i + 2 < len(L) and L[i + 1] == "" and re.match(r"^\*[^*].*\*$", L[i + 2]):
                cap = L[i + 2][1:-1]; i += 2
            out.append(f'<figure><img src="{E(src)}" alt="{E(alt)}" width="2112" height="1014" loading="lazy" decoding="async">'
                       + (f"<figcaption>{inline(cap)}</figcaption>" if cap else "") + "</figure>")
        elif ln.startswith("|"):
            rows = []
            while i < len(L) and L[i].startswith("|"):
                rows.append([c.strip() for c in L[i].strip().strip("|").split("|")]); i += 1
            head, body = rows[0], [r for r in rows[1:] if not set("".join(r)) <= set("-: ")]
            cap = ""
            if out and out[-1].startswith('<p class="tcap">'):
                cap = out.pop()
            out.append('<div class="tw">' + cap + "<table><thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead><tbody>"
                       + "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in body) + "</tbody></table></div>")
            continue
        elif ln.startswith("- "):
            items = []
            while i < len(L) and L[i].startswith("- "):
                items.append(L[i][2:]); i += 1
            out.append("<ul>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ul>")
            continue
        elif re.match(r"^\*\*Table \d", ln):
            out.append(f'<p class="tcap">{inline(ln.strip("*"))}</p>')
        elif re.match(r"^\*\*.+\*\*$", ln):
            out.append(f'<p class="kicker">{inline(ln[2:-2])}</p>')
        else:
            out.append(f"<p>{inline(ln)}</p>")
        i += 1
    return "\n".join(out), toc


# ---------------------------------------------------------------- posts
def load():
    posts = []
    for f in sorted((BLOG / "posts").glob("*.md")):
        raw = f.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
        meta, body = json.loads(m.group(1)), m.group(2).strip()
        meta["slug"] = f.stem
        meta["body"] = body
        words = len(re.sub(r"[#*|!\[\]()-]", " ", body).split())
        meta["words"] = words
        meta["minutes"] = max(1, math.ceil(words / 230))
        meta["url"] = f"{BASE}/blog/{f.stem}/"
        posts.append(meta)
    return sorted(posts, key=lambda p: p["date"], reverse=True)


def nice_date(d):
    return datetime.date.fromisoformat(d).strftime("%B %-d, %Y")


def cover(p):
    """House-style cover tile, 1600x900 PNG, drawn once per post (redrawn if missing)."""
    out = BLOG / p["slug"] / "cover.png"
    if out.exists():
        return
    mark = re.search(r'<path fill-rule="evenodd" clip-rule="evenodd" d="([^"]+)" fill="#E31E30">', brand.LOGO).group(1)
    tag = " · ".join(p.get("tags", []))
    page = f"""<!doctype html><html><head><meta charset="utf-8">{brand.FONTS}<style>
html,body{{margin:0;width:1600px;height:900px;background:#0B0C10;overflow:hidden}}
.t{{position:absolute;inset:0;padding:92px 104px;box-sizing:border-box;display:flex;flex-direction:column;justify-content:space-between;color:#F2F2F0;font-family:'Inter Tight',Arial,sans-serif}}
.grid{{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.05) 1px,transparent 1px);background-size:80px 80px}}
.ring{{position:absolute;right:-180px;top:110px;width:760px;height:760px;border:1px solid rgba(217,195,163,.45);border-radius:50%}}
.ring.b{{right:-60px;top:230px;width:520px;height:520px;border-color:rgba(227,30,48,.55)}}
.top{{display:flex;align-items:center;gap:18px;font-family:'Geist Mono',monospace;font-size:22px;letter-spacing:.08em;text-transform:uppercase;color:#A3A6AE}}
.top svg{{height:30px}}.top b{{color:#D9C3A3;font-weight:400}}
h1{{font-weight:300;font-size:132px;line-height:.98;letter-spacing:-.04em;margin:0;max-width:11ch}}
.sub{{font-family:'Newsreader',Georgia,serif;font-weight:300;font-size:34px;line-height:1.3;color:rgba(242,242,240,.82);max-width:30ch;margin-top:28px}}
.bot{{display:flex;justify-content:space-between;font-family:'Geist Mono',monospace;font-size:20px;letter-spacing:.06em;text-transform:uppercase;color:#A3A6AE}}
</style></head><body><div class="grid"></div><div class="ring"></div><div class="ring b"></div><div class="t">
<div class="top"><svg viewBox="0 0 60 34"><path fill-rule="evenodd" d="{mark}" fill="#E31E30"/></svg><span>CodeNinja <b>Atoms</b> · {E(tag)}</span></div>
<div><h1>{E(p['title'])}</h1><div class="sub">{E(p.get('cover_line') or p['subtitle'].split(',')[0])}</div></div>
<div class="bot"><span>{E(p['author'])}</span><span>{E(nice_date(p['date']))}</span></div></div></body></html>"""
    tmp = BLOG / p["slug"] / "_cover.html"
    tmp.write_text(page, encoding="utf-8")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--window-size=1600,900",
                    "--virtual-time-budget=4000", f"--screenshot={out}", tmp.as_uri()], capture_output=True)
    tmp.unlink()


CSS = """
body{background:var(--paper)}html.js header.top:not(.solid):not(.open){background:rgba(11,12,16,.94);border-bottom-color:var(--rule-d)}
.wrapb{max-width:1080px;margin:0 auto;padding:132px var(--gutter) 96px}
.post{max-width:740px;margin:0 auto}
.tags{display:flex;gap:8px;flex-wrap:wrap;margin:0 0 22px}.tags a{font-family:var(--mono);font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink);text-decoration:none;border:1px solid var(--rule-l);padding:6px 10px}
.tags a:hover{border-color:var(--ink)}
.post h1{font-weight:400;font-size:clamp(38px,5vw,60px);line-height:1.04;letter-spacing:-.034em;color:var(--ink);margin:0 0 18px}
.post .dek{font-family:var(--serif);font-weight:300;font-size:clamp(20px,2.1vw,25px);line-height:1.42;color:var(--muted-l);margin:0 0 28px}
.byline{display:flex;align-items:center;gap:14px;padding:18px 0;border-top:1px solid var(--rule-l);border-bottom:1px solid var(--rule-l);margin-bottom:36px;font-size:14.5px;color:var(--muted-l)}
.byline img{width:44px;height:44px;border-radius:50%;object-fit:cover;filter:grayscale(1)}.byline b{color:var(--ink);font-weight:500}.byline a{color:inherit;text-decoration:none}
.coverimg{display:block;width:100%;height:auto;margin:0 0 44px}
.body{font-family:var(--serif);font-size:20px;line-height:1.66;color:#22232e}
.body p{margin:0 0 24px}.body a{color:var(--ink);text-decoration-thickness:1px;text-underline-offset:3px;overflow-wrap:anywhere}
.body h2{font-family:var(--sans);font-weight:500;font-size:clamp(26px,2.8vw,33px);line-height:1.15;letter-spacing:-.024em;color:var(--ink);margin:64px 0 18px}
.body h3{font-family:var(--sans);font-weight:500;font-size:21px;letter-spacing:-.012em;color:var(--ink);margin:40px 0 12px}
.body figure{margin:40px -60px}.body figure img{width:100%;height:auto;display:block;border:1px solid var(--rule-l);background:#fff}
.body figcaption{font-family:var(--sans);font-size:14px;line-height:1.5;color:var(--muted-l);margin:12px 60px 0}
.body .tw{overflow-x:auto;margin:32px 0}.body .tcap{font-family:var(--sans);font-weight:500;font-size:15px;color:var(--ink);margin:0 0 10px}
.body table{width:100%;border-collapse:collapse;font-family:var(--sans);font-size:15px;line-height:1.45}
.body th{font-family:var(--mono);font-weight:400;font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted-l);text-align:left;border-bottom:1px solid var(--ink);padding:10px 14px 10px 0}
.body td{border-bottom:1px solid var(--rule-l);padding:12px 14px 12px 0;vertical-align:top}.body td:first-child{color:var(--ink);font-weight:500}
.body ul{padding-left:20px;font-family:var(--sans);font-size:15px;line-height:1.55;color:var(--muted-l)}.body li{margin:0 0 8px}
.body .kicker{font-family:var(--sans);font-weight:500;font-size:clamp(24px,2.6vw,30px);letter-spacing:-.02em;color:var(--ink);margin:36px 0}
.authorbox{display:flex;gap:20px;align-items:flex-start;margin:64px 0 0;padding:28px 0;border-top:1px solid var(--ink)}
.authorbox img{width:72px;height:72px;border-radius:50%;object-fit:cover;filter:grayscale(1)}.authorbox p{margin:4px 0 0;font-size:15px;color:var(--muted-l)}.authorbox b{font-size:17px;color:var(--ink);font-weight:500}
.authorbox a{color:var(--ink)}
.idx h1{font-weight:300;font-size:clamp(44px,6vw,80px);line-height:1;letter-spacing:-.036em;color:var(--ink);margin:0 0 18px}
.idx .lead{font-family:var(--serif);font-weight:300;font-size:clamp(20px,2.2vw,26px);line-height:1.4;color:var(--muted-l);max-width:40ch;margin:0 0 28px}
.chips{display:flex;gap:8px;flex-wrap:wrap;margin:0 0 40px;padding-bottom:24px;border-bottom:1px solid var(--ink)}
.chips a{font-family:var(--mono);font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink);text-decoration:none;border:1px solid var(--rule-l);padding:7px 11px}.chips a.on{background:var(--ink);color:var(--paper);border-color:var(--ink)}
.row{display:grid;grid-template-columns:1fr 280px;gap:40px;padding:32px 0;border-bottom:1px solid var(--rule-l);text-decoration:none;color:inherit}
.row h2{font-weight:500;font-size:clamp(24px,2.6vw,32px);line-height:1.15;letter-spacing:-.024em;color:var(--ink);margin:6px 0 10px}
.row p{font-family:var(--serif);font-size:18px;line-height:1.45;color:var(--muted-l);margin:0 0 14px}.row small{font-size:13.5px;color:var(--muted-l)}
.row .m{font-family:var(--mono);font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted-l)}
.row img{width:100%;height:auto;display:block;aspect-ratio:16/9;object-fit:cover}
.row:hover h2{text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:4px}
@media (max-width:900px){.body figure{margin:32px 0}.body figcaption{margin:10px 0 0}}
@media (max-width:820px){.wrapb{padding:100px var(--gutter) 64px}.body{font-size:18px}.row{grid-template-columns:1fr;gap:16px}.row img{order:-1}}
"""


def nav():
    return [("Research", f"{BASE}/#research"), ("Sectors", f"{BASE}/sectors/"), ("Praxis", f"{BASE}/praxis/"), ("Hyper Ontology", f"{BASE}/hyper-ontology/"),
            ("Blog", f"{BASE}/blog/"), ("About", f"{BASE}/about/")]


def shell(path, title, desc, body, ld, og_image, og_type="website", extra_head=""):
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{BASE}/{path}">
<link rel="alternate" type="application/atom+xml" href="{BASE}/blog/feed.xml" title="CodeNinja Atoms engineering blog">
<meta property="og:type" content="{og_type}"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{BASE}/{path}">
<meta property="og:image" content="{E(og_image)}">{extra_head}
""" + "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in ld) + f"""{brand.FONTS}{brand.JS_FLAG}<style>{brand.CSS}{CSS}</style></head>
<body>{brand.header(BASE + "/", nav(), access=f"{BASE}/praxis/#access")}
<main class="light"><div class="wrapb">{body}</div></main>
<footer class="site"><div class="wrapf">{brand.footer_brand(BASE + "/")}<span>CodeNinja Atoms is a fully owned subsidiary of <a href="{brand.PARENT}">CodeNinja</a> · Posts are CC BY 4.0 · <a href="{BASE}/blog/feed.xml">RSS</a></span></div></footer>
{brand.SCRIPT}</body></html>"""


def post_page(p):
    body_html, _toc = md_to_html(p["body"], p["slug"])
    a = AUTHORS.get(p["author"], {})
    img = f"{p['url']}cover.png"
    tags = "".join(f'<a href="{BASE}/blog/#{slugify(t)}">{E(t)}</a>' for t in p.get("tags", []))
    byline = (f'<div class="byline">' + (f'<img src="{a["photo"]}" alt="{E(p["author"])}" width="44" height="44">' if a.get("photo") else "")
              + f'<div><b><a href="{a.get("url", "#")}">{E(p["author"])}</a></b><br>{E(p.get("author_role", ""))} · {nice_date(p["date"])} · {p["minutes"]} min read</div></div>')
    authorbox = (f'<div class="authorbox">' + (f'<img src="{a["photo"]}" alt="" width="72" height="72">' if a.get("photo") else "")
                 + f'<div><b>{E(p["author"])}</b><p>{E(p.get("author_role", ""))}. <a href="{a.get("url", BASE + "/about/")}">About the leadership</a>'
                 + (f' · <a href="{a["sameAs"]}" rel="noopener">LinkedIn</a>' if a.get("sameAs") else "") + "</p></div></div>")
    body = (f'<article class="post"><div class="tags">{tags}</div><h1>{E(p["title"])}</h1><p class="dek">{E(p["subtitle"])}</p>{byline}'
            f'<img class="coverimg" src="cover.png" alt="{E(p["title"])}" width="1600" height="900">'
            f'<div class="body">{body_html}</div>{authorbox}</article>')
    sources = re.findall(r"https?://[^\s)]+?(?=[.,;]?(?:\s|$))", p["body"].split("## Sources")[-1]) if "## Sources" in p["body"] else []
    ld = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": p["title"], "description": p["description"], "alternativeHeadline": p["subtitle"],
          "image": img, "url": p["url"], "mainEntityOfPage": p["url"], "datePublished": p["date"], "dateModified": p.get("updated", p["date"]),
          "inLanguage": "en", "wordCount": p["words"], "timeRequired": f"PT{p['minutes']}M", "keywords": p.get("tags", []),
          "articleSection": p.get("tags", ["Engineering"])[0], "license": "https://creativecommons.org/licenses/by/4.0/",
          "author": {"@type": "Person", "name": p["author"], "jobTitle": p.get("author_role", ""), "url": a.get("url"), "sameAs": a.get("sameAs"), "image": a.get("photo")},
          "publisher": {"@type": "Organization", "@id": f"{BASE}/#org", "name": "CodeNinja Atoms", "url": f"{BASE}/", "logo": {"@type": "ImageObject", "url": f"{BASE}/icon-512.png"}},
          "isPartOf": {"@type": "Blog", "@id": f"{BASE}/blog/#blog", "name": "CodeNinja Atoms engineering blog", "url": f"{BASE}/blog/"},
          "citation": sources}
    head = (f'<meta property="article:published_time" content="{p["date"]}"><meta property="article:author" content="{E(p["author"])}">'
            + "".join(f'<meta property="article:tag" content="{E(t)}">' for t in p.get("tags", [])))
    return shell(f"blog/{p['slug']}/", f"{p['title']} | CodeNinja Atoms Engineering Blog", p["description"], body, [ld], img, "article", head)


def index_page(posts):
    tags = sorted({t for p in posts for t in p.get("tags", [])})
    chips = '<a class="on" href="#all">All</a>' + "".join(f'<a id="{slugify(t)}" href="#{slugify(t)}">{E(t)}</a>' for t in tags)
    rows = "".join(f'<a class="row" href="{p["slug"]}/" data-tags="{E("|".join(p.get("tags", [])))}"><div><span class="m">{E(" · ".join(p.get("tags", [])))}</span>'
                   f'<h2>{E(p["title"])}</h2><p>{E(p["subtitle"])}</p><small>{E(p["author"])} · {nice_date(p["date"])} · {p["minutes"]} min read</small></div>'
                   f'<img src="{p["slug"]}/cover.png" alt="" width="1600" height="900" loading="lazy"></a>' for p in posts)
    body = f'<div class="idx"><p class="eyebrow">CodeNinja Atoms</p><h1>Engineering blog</h1><p class="lead">{E(INTRO)}</p><div class="chips">{chips}</div>{rows}</div>'
    body += """<script>(function(){function f(){var h=decodeURIComponent(location.hash.slice(1));document.querySelectorAll('.chips a').forEach(function(a){a.classList.toggle('on',a.getAttribute('href')==='#'+(h||'all'))});
document.querySelectorAll('.row').forEach(function(r){var t=r.getAttribute('data-tags').toLowerCase().replace(/[^a-z0-9|]+/g,'-');r.hidden=!!h&&h!=='all'&&t.split('|').indexOf(h)<0})}addEventListener('hashchange',f);f()})();</script>"""
    ld = {"@context": "https://schema.org", "@type": "Blog", "@id": f"{BASE}/blog/#blog", "name": "CodeNinja Atoms engineering blog", "url": f"{BASE}/blog/",
          "description": INTRO, "publisher": {"@id": f"{BASE}/#org"},
          "blogPost": [{"@type": "BlogPosting", "headline": p["title"], "url": p["url"], "datePublished": p["date"], "author": {"@type": "Person", "name": p["author"]}} for p in posts]}
    og = f"{posts[0]['url']}cover.png" if posts else f"{BASE}/assets/video/port-night.jpg"
    return shell("blog/", "Engineering Blog | CodeNinja Atoms", INTRO, body, [ld], og)


def feed(posts):
    today = datetime.date.today().isoformat()
    entries = "".join(f'  <entry><title>{E(p["title"])}</title><link href="{p["url"]}"/><id>{p["url"]}</id><updated>{p["date"]}T00:00:00Z</updated>'
                      f'<author><name>{E(p["author"])}</name></author><summary>{E(p["subtitle"])}</summary></entry>\n' for p in posts)
    return (f'<?xml version="1.0" encoding="utf-8"?>\n<feed xmlns="http://www.w3.org/2005/Atom"><title>CodeNinja Atoms engineering blog</title>'
            f'<link href="{BASE}/blog/"/><link rel="self" href="{BASE}/blog/feed.xml"/><id>{BASE}/blog/</id><updated>{today}T00:00:00Z</updated>\n{entries}</feed>\n')


def markdown_copy(p):
    head = [f"# {p['title']}", "", f"*{p['subtitle']}*", "", f"Canonical: {p['url']}", f"Author: {p['author']}, {p.get('author_role', '')}",
            f"Published: {p['date']}", "License: CC BY 4.0", "Publisher: CodeNinja Atoms (https://codeatoms.ai), a fully owned subsidiary of CodeNinja", ""]
    body = re.sub(r"\]\(figures/", f"]({p['url']}figures/", p["body"])
    return "\n".join(head) + body + "\n"


def main():
    posts = load()
    for p in posts:
        d = BLOG / p["slug"]
        d.mkdir(parents=True, exist_ok=True)
        cover(p)
        (d / "index.html").write_text(post_page(p), encoding="utf-8")
        (d / "index.md").write_text(markdown_copy(p), encoding="utf-8")
    (BLOG / "index.html").write_text(index_page(posts), encoding="utf-8")
    (BLOG / "feed.xml").write_text(feed(posts), encoding="utf-8")
    print(f"blog: {len(posts)} post(s): " + ", ".join(f"{p['slug']} ({p['minutes']} min)" for p in posts))
    return posts


if __name__ == "__main__":
    main()
