"""Search and AI retrieval pass over the whole site. Runs LAST, after every generator
(site_index.py calls it), and is idempotent: everything it adds sits between markers.

What it does, page by page:
  - points inline base64 figures at the figure files already on disk (or writes them), so a
    design page drops from ~2 MB of HTML to tens of KB; lazy-loads every figure after the first
  - head block: icons, manifest, theme colour, robots directives, Open Graph image and site
    name, Twitter card, markdown alternate, BreadcrumbList; enriches the design TechArticle with
    image, publisher identity and series
  - design and method pages get the site bar (home and nav) and a footer of related designs
  - paper copies (*/paper/*.html) get a canonical to their design page
Site-wide: robots.txt (AI crawlers welcome), 404.html, site.webmanifest, image sitemap,
index.md per design, llms-full.txt, and the llms.txt full-text section.
    python tools/seo.py
"""
import base64, hashlib, html, io, json, re
from pathlib import Path
import brand

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://codeatoms.ai"
ORG_ID = f"{BASE}/#org"
SITE_ID = f"{BASE}/#website"
SKIP = {"tools", "mcp-server", "hyper-ontology-py", "assets", "dataset", ".git", ".github", "methods"}
H0, H1 = "<!--seo-->", "<!--/seo-->"
# Search engine ownership tokens (public by design). Google verifies by the file google5c8034f5c559d4ab.html at the root.
VERIFY = '<meta name="msvalidate.01" content="C0BA30668F739D132B60D2147D569A8E">'
B0, B1 = "<!--atoms-bar-->", "<!--/atoms-bar-->"
F0, F1 = "<!--atoms-foot-->", "<!--/atoms-foot-->"
E = lambda s: html.escape(str(s), quote=True)
AI_AGENTS = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-User", "Claude-SearchBot", "anthropic-ai",
             "PerplexityBot", "Perplexity-User", "Google-Extended", "Applebot", "Applebot-Extended", "Bingbot", "CCBot",
             "Amazonbot", "meta-externalagent", "DuckAssistBot", "cohere-ai", "MistralAI-User", "YouBot"]


def meta(h, name, prop=False):
    a = "property" if prop else "name"
    m = re.search(rf'<meta {a}="{re.escape(name)}" content="([^"]*)"', h)
    return html.unescape(m.group(1)) if m else ""


def strip_block(h, a, b):
    return re.sub(re.escape(a) + r".*?" + re.escape(b), "", h, flags=re.S)


def designs():
    out = []
    for d in sorted(ROOT.iterdir()):
        if d.name in SKIP or not (d / "ontology" / "objects.json").exists() or not (d / "index.html").exists():
            continue
        pkg = json.loads((d / "ontology" / "objects.json").read_text(encoding="utf-8"))
        h = (d / "index.html").read_text(encoding="utf-8")
        t = meta(h, "citation_title") or re.search(r"<title>(.*?)</title>", h, re.S).group(1)
        out.append({"slug": d.name, "title": html.unescape(t), "sector": pkg.get("sector", "").replace("-", " "),
                    "country": pkg.get("country", ""), "doi": meta(h, "citation_doi")})
    return out


# ---------------------------------------------------------------- figures
def deinline(h, folder, absolute):
    figs = {}
    for f in sorted((folder / "figures").glob("*")) if (folder / "figures").exists() else []:
        if f.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp"):
            figs[hashlib.md5(f.read_bytes()).hexdigest()] = f.name

    def rep(m):
        ext, data = m.group(1), base64.b64decode(m.group(2))
        md5 = hashlib.md5(data).hexdigest()
        name = figs.get(md5)
        if not name:
            name = f"inline_{md5[:12]}.{'jpg' if ext == 'jpeg' else ext}"
            (folder / "figures").mkdir(exist_ok=True)
            (folder / "figures" / name).write_bytes(data)
            figs[md5] = name
        return f'src="{(BASE + "/" + folder.name + "/") if absolute else ""}figures/{name}"'

    return re.sub(r'src="data:image/(png|jpeg|jpg|webp);base64,([A-Za-z0-9+/=\s]+)"', rep, h)


def size_imgs(h, folder):
    """width/height on figure images (no layout shift), lazy after the first."""
    try:
        from PIL import Image
    except ImportError:
        Image = None
    n = [0]

    def rep(m):
        tag = m.group(0)
        n[0] += 1
        src = re.search(r'src="([^"]+)"', tag)
        if Image and src and "width=" not in tag:
            p = src.group(1).replace(f"{BASE}/{folder.name}/", "")
            f = folder / p
            if f.exists():
                w, hh = Image.open(f).size
                tag = tag.replace("<img ", f'<img width="{w}" height="{hh}" ', 1)
        if n[0] == 1:
            tag = tag.replace(' loading="lazy"', "")
        elif "loading=" not in tag:
            tag = tag.replace("<img ", '<img loading="lazy" ', 1)
        if "decoding=" not in tag:
            tag = tag.replace("<img ", '<img decoding="async" ', 1)
        return tag

    return re.sub(r"<img [^>]*>", rep, h)


# ---------------------------------------------------------------- head
def head_block(kind, url, title, desc, image, crumbs, md):
    t = [H0,
         '<link rel="icon" href="/favicon.ico" sizes="48x48"><link rel="icon" href="/favicon.svg" type="image/svg+xml">',
         '<link rel="apple-touch-icon" href="/apple-touch-icon.png"><link rel="manifest" href="/site.webmanifest"><meta name="theme-color" content="#0B0C10">',
         '<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">' if kind != "copy" else "",
         '<meta property="og:site_name" content="CodeNinja Atoms"><meta property="og:locale" content="en_US">',
         f'<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{E(title)}"><meta name="twitter:description" content="{E(desc)}">']
    if image:
        t.append(f'<meta property="og:image" content="{E(image)}"><meta property="og:image:alt" content="{E(title)}"><meta name="twitter:image" content="{E(image)}">')
    if kind == "home":
        t.append(VERIFY)
    if md:
        t.append(f'<link rel="alternate" type="text/markdown" href="{md}" title="Markdown">')
    if crumbs:
        bl = {"@context": "https://schema.org", "@type": "BreadcrumbList",
              "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(crumbs)]}
        t.append(f'<script type="application/ld+json">{json.dumps(bl, ensure_ascii=False)}</script>')
    t.append(H1)
    return "".join(x for x in t if x)


def enrich_article(h, image, slug):
    def rep(m):
        try:
            j = json.loads(m.group(1))
        except ValueError:
            return m.group(0)
        types = j.get("@type") if isinstance(j.get("@type"), list) else [j.get("@type")]
        if not ({"TechArticle", "ScholarlyArticle"} & set(types)):
            return m.group(0)
        j["publisher"] = {"@type": "Organization", "@id": ORG_ID, "name": "CodeNinja Atoms", "url": f"{BASE}/",
                          "logo": {"@type": "ImageObject", "url": f"{BASE}/icon-512.png"},
                          "parentOrganization": {"@type": "Organization", "name": "CodeNinja", "url": brand.PARENT}}
        j["isPartOf"] = [{"@id": SITE_ID}, {"@type": "CreativeWorkSeries", "name": "Vertical-Driven Architectures", "url": f"{BASE}/#research"}]
        if image:
            j["image"] = image
        j.setdefault("license", "https://creativecommons.org/licenses/by/4.0/")
        j.setdefault("isAccessibleForFree", True)
        return f'<script type="application/ld+json">{json.dumps(j, ensure_ascii=False)}</script>'

    return re.sub(r'<script type="application/ld\+json">(.*?)</script>', rep, h, flags=re.S)


def inject_head(h, block):
    h = strip_block(h, H0, H1)
    return h.replace("</head>", block + "</head>", 1)


# ---------------------------------------------------------------- bar and footer
BAR_CSS = (".atoms-bar{position:sticky;top:0;z-index:50;display:flex;align-items:center;gap:22px;padding:12px 24px;background:#0B0C10;border-bottom:1px solid rgba(255,255,255,.12);"
           "font:400 13.5px/1.2 'Inter Tight','Helvetica Neue',Arial,sans-serif}.atoms-bar a{color:rgba(242,242,240,.8);text-decoration:none}.atoms-bar a:hover{color:#fff}"
           ".atoms-bar .logo{height:17px;width:auto;display:block}.atoms-bar a.brand{display:flex;align-items:center;gap:8px}.atoms-bar span.atoms{font-weight:700;font-size:18px;color:#D9C3A3}"
           ".atoms-bar nav{display:flex;gap:20px;margin-left:auto;flex-wrap:wrap;align-items:center}.atoms-bar nav a.join{background:#fff;color:#111218;padding:7px 12px}.atoms-bar nav a.join:hover{background:#E6E6E3}"
           ".atoms-foot{background:#0B0C10;color:#A3A6AE;padding:48px 24px;font:400 14px/1.6 'Inter Tight','Helvetica Neue',Arial,sans-serif;margin-top:64px}"
           ".atoms-foot .w{max-width:1100px;margin:0 auto}.atoms-foot h2{color:#F2F2F0;font-weight:400;font-size:22px;margin:0 0 16px;letter-spacing:-.02em;border:0;padding:0}"
           ".atoms-foot ul{list-style:none;margin:0 0 28px;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:10px 28px}"
           ".atoms-foot li{border-top:1px solid rgba(255,255,255,.14);padding-top:10px}.atoms-foot a{color:#F2F2F0}.atoms-foot small{display:block;color:#A3A6AE}"
           "@media (max-width:640px){.atoms-bar{padding:10px 16px;gap:12px}.atoms-bar nav{gap:12px;font-size:12.5px}.atoms-foot{padding:36px 16px}}"
           "@media print{.atoms-bar,.atoms-foot{display:none}}")


def bar():
    nav = [("Research", f"{BASE}/#research"), ("Praxis", f"{BASE}/praxis/"), ("Hyper Ontology", f"{BASE}/hyper-ontology/"), ("Data", f"{BASE}/#data"), ("Blog", f"{BASE}/blog/"), ("About", f"{BASE}/about/")]
    return (f'{B0}<style>{BAR_CSS}</style><div class="atoms-bar"><a class="brand" href="{BASE}/" aria-label="CodeNinja Atoms home">{brand.LOGO}<span class="atoms">Atoms</span></a>'
            f'<nav aria-label="CodeNinja Atoms">' + "".join(f'<a href="{u}">{t}</a>' for t, u in nav) + f'<a href="{brand.SIGNIN}">Sign in</a><a class="join" href="{brand.SIGNUP}">Join the Praxis beta</a></nav></div>{B1}')


def foot(slug, ds):
    me = next((d for d in ds if d["slug"] == slug), None)
    others = [d for d in ds if d["slug"] != slug]
    if me:
        others.sort(key=lambda d: (d["sector"] != me["sector"], d["country"] != me["country"], d["title"]))
    items = "".join(f'<li><a href="{BASE}/{d["slug"]}/">{E(d["title"].split(":")[0])}</a><small>{E(d["sector"])} · {E(d["country"])}</small></li>' for d in others[:6])
    sec = (f'<p>Questions engineers ask about AI in {E(me["sector"])}, answered: <a href="{BASE}/sectors/{me["sector"].replace(" and ", "-and-").replace(" ", "-")}/">physical AI for {E(me["sector"])}</a>.</p>' if me else "")
    return (f'{F0}<footer class="atoms-foot"><div class="w"><h2>More reference architectures</h2><ul>{items}</ul>{sec}'
            f'<p>Part of <a href="{BASE}/">CodeNinja Atoms</a>, a sovereign AI operating system for the physical world. Designed on <a href="{BASE}/praxis/">Praxis</a>, made living with '
            f'<a href="{BASE}/hyper-ontology/">Hyper Ontology</a>. Pages, papers, object models and data are CC BY 4.0. CodeNinja Atoms is a fully owned subsidiary of <a href="{brand.PARENT}">CodeNinja</a>.</p>'
            f"</div></footer>{F1}")


def add_bar_foot(h, slug, ds):
    h = strip_block(strip_block(h, B0, B1), F0, F1)
    h = re.sub(r"(<body[^>]*>)", lambda m: m.group(1) + bar(), h, count=1)
    return h.replace("</body>", foot(slug, ds) + "</body>", 1)


# ---------------------------------------------------------------- markdown
def to_markdown(h, url, title, doi, pdf):
    from markdownify import markdownify
    body = h[h.find("<body"):]
    body = strip_block(strip_block(body, B0, B1), F0, F1)
    body = re.sub(r"<(script|style|svg|nav)\b.*?</\1>", "", body, flags=re.S)
    md = markdownify(body, heading_style="ATX", bullets="-")
    md = re.sub(r"\n{3,}", "\n\n", md).strip()
    head = [f"# {title}", "", f"Canonical: {url}"]
    if doi:
        head.append(f"DOI: https://doi.org/{doi}")
    if pdf:
        head.append(f"PDF: {pdf}")
    head += ["License: CC BY 4.0", "Publisher: CodeNinja Atoms (https://codeatoms.ai), a fully owned subsidiary of CodeNinja", ""]
    return "\n".join(head) + "\n" + md + "\n"


# ---------------------------------------------------------------- site files
def site_files(ds):
    robots = ["# codeatoms.ai: every page, paper, object model and dataset here is CC BY 4.0.",
              "# Search engines, AI search and AI assistants are welcome to crawl, cite and train on it.", "",
              "User-agent: *", "Allow: /", ""]
    for a in AI_AGENTS:
        robots += [f"User-agent: {a}", "Allow: /", ""]
    robots += [f"Sitemap: {BASE}/sitemap.xml", ""]
    (ROOT / "robots.txt").write_text("\n".join(robots), encoding="utf-8")
    (ROOT / "site.webmanifest").write_text(json.dumps({
        "name": "CodeNinja Atoms", "short_name": "Atoms", "description": "A sovereign AI operating system for the physical world.",
        "start_url": "/", "display": "browser", "background_color": "#0B0C10", "theme_color": "#0B0C10",
        "icons": [{"src": "/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, indent=1), encoding="utf-8")
    links = "".join(f'<li><a href="/{d["slug"]}/">{E(d["title"].split(":")[0])}</a> · {E(d["sector"])} · {E(d["country"])}</li>' for d in ds)
    (ROOT / "404.html").write_text(f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Page not found | CodeNinja Atoms</title><meta name="robots" content="noindex">
<link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="icon" href="/favicon.ico" sizes="48x48">{brand.FONTS}
<style>body{{margin:0;background:#F5F5F3;color:#1E1F2B;font:400 16px/1.6 'Inter Tight',Arial,sans-serif}}.w{{max-width:880px;margin:0 auto;padding:72px 24px}}
h1{{font-weight:300;font-size:clamp(36px,6vw,64px);letter-spacing:-.03em;margin:0 0 12px}}ul{{padding:0;list-style:none}}li{{border-top:1px solid rgba(30,31,43,.14);padding:10px 0}}a{{color:#1E1F2B}}</style></head>
<body><style>{BAR_CSS}</style>{bar()}<div class="w"><h1>This page moved or never existed.</h1><p>Every reference architecture on CodeNinja Atoms is listed below. Start at the <a href="/">home page</a>, or read <a href="/praxis/">Praxis</a> and <a href="/hyper-ontology/">Hyper Ontology</a>.</p><ul>{links}</ul></div></body></html>""", encoding="utf-8")


def image_sitemap(ds):
    p = ROOT / "sitemap.xml"
    s = p.read_text(encoding="utf-8")
    s = re.sub(r"<image:image>.*?</image:image>", "", s, flags=re.S)
    if "xmlns:image" not in s:
        s = s.replace('xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"', 'xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1"', 1)
    for d in ds:
        figs = sorted((ROOT / d["slug"] / "figures").glob("figure_*.png"))
        if not figs:
            continue
        imgs = "".join(f"<image:image><image:loc>{BASE}/{d['slug']}/figures/{f.name}</image:loc></image:image>" for f in figs)
        s = s.replace(f"<loc>{BASE}/{d['slug']}/</loc>", f"<loc>{BASE}/{d['slug']}/</loc>{imgs}", 1)
    p.write_text(s, encoding="utf-8")


def llms_full(mds):
    intro = ["# CodeNinja Atoms: full text", "",
             "> CodeNinja Atoms is building a sovereign AI operating system for the physical world. This file holds the full text of every reference architecture and method paper on https://codeatoms.ai, one after another, in Markdown. CC BY 4.0. A fully owned subsidiary of CodeNinja.", ""]
    (ROOT / "llms-full.txt").write_text("\n".join(intro) + "\n\n---\n\n".join(mds), encoding="utf-8")
    p = ROOT / "llms.txt"
    s = strip_block(p.read_text(encoding="utf-8"), "<!--full-->", "<!--/full-->").rstrip() + "\n"
    s += ("\n<!--full-->\n## Full text\n\n- [llms-full.txt](" + BASE + "/llms-full.txt): every paper on the site in one Markdown file\n"
          "- Each design page also has a Markdown copy at its address plus `index.md`, for example " + BASE + "/wildfire-risk-distribution-us/index.md\n"
          "- [About CodeNinja Atoms](" + BASE + "/about/): mission and executive leadership\n<!--/full-->\n")
    p.write_text(s, encoding="utf-8")


# ---------------------------------------------------------------- main
def main():
    ds = designs()
    dslugs = {d["slug"] for d in ds}
    mds, stats = [], []
    pages = [p for p in ROOT.glob("*/index.html") if p.parent.name not in SKIP] + [ROOT / "index.html"] + sorted(ROOT.glob("sectors/*/index.html")) + sorted(ROOT.glob("blog/*/index.html"))
    copies = [p for p in ROOT.glob("*/paper/*.html") if p.parent.parent.name not in SKIP]
    for p in sorted(pages):
        h = strip_block(p.read_text(encoding="utf-8"), H0, H1)
        before = len(h)
        folder = p.parent
        slug = "" if folder == ROOT else folder.relative_to(ROOT).as_posix()
        url = f"{BASE}/{slug + '/' if slug else ''}"
        title = html.unescape((re.search(r"<title>(.*?)</title>", h, re.S) or [None, "CodeNinja Atoms"])[1])
        desc = meta(h, "description")
        kind = "design" if slug in dslugs else ("method" if slug.endswith("-method") else ("home" if not slug else ("sector" if slug.startswith("sectors/") else ("post" if slug.startswith("blog/") else "page"))))
        if kind in ("design", "method"):
            h = deinline(h, folder, absolute=False)
            h = size_imgs(h, folder)
        own_image = meta(h, "og:image", prop=True)
        image = own_image
        if not image:
            f1 = folder / "figures" / "figure_01.png"
            image = f"{url}figures/figure_01.png" if f1.exists() else f"{BASE}/assets/video/port-night.jpg"
        crumbs = [("CodeNinja Atoms", f"{BASE}/")]
        if kind == "design":
            crumbs += [("Research", f"{BASE}/#research"), (meta(h, "citation_title").split(":")[0] or title.split(":")[0], url)]
        elif kind == "post":
            crumbs += [("Blog", f"{BASE}/blog/"), (title.split("|")[0].strip(), url)]
        elif kind == "sector":
            crumbs += [("Sectors", f"{BASE}/sectors/"), (title.split(":")[0].split("|")[0].strip(), url)]
        elif slug:
            crumbs += [(title.split(":")[0].split("|")[0].strip(), url)]
        else:
            crumbs = []
        md = "index.md" if kind in ("sector", "post") and (folder / "index.md").exists() else None
        if kind in ("sector", "post") and md:
            mds.append((folder / "index.md").read_text(encoding="utf-8"))
        if kind in ("design", "method"):
            h = enrich_article(h, image if kind == "design" else None, slug)
            h = add_bar_foot(h, slug, ds)
            md = "index.md"
            doc = to_markdown(h, url, meta(h, "citation_title") or title, meta(h, "citation_doi"), meta(h, "citation_pdf_url"))
            (folder / "index.md").write_text(doc, encoding="utf-8")
            mds.append(doc)
        h = inject_head(h, head_block(kind, url, title, desc, "" if own_image else image, crumbs, md))
        p.write_text(h, encoding="utf-8")
        stats.append((str(p.relative_to(ROOT)), before // 1024, len(h) // 1024))
    for p in sorted(copies):
        h = p.read_text(encoding="utf-8")
        before = len(h)
        folder = p.parent.parent
        h = deinline(h, folder, absolute=True)
        h = size_imgs(h, folder)
        if '<link rel="canonical"' not in h:
            h = h.replace("</head>", f'<link rel="canonical" href="{BASE}/{folder.name}/"></head>', 1)
        h = inject_head(h, head_block("copy", f"{BASE}/{folder.name}/", "", "", "", [], None))
        p.write_text(h, encoding="utf-8")
        stats.append((str(p.relative_to(ROOT)), before // 1024, len(h) // 1024))
    site_files(ds)
    image_sitemap(ds)
    llms_full(mds)
    for s in stats:
        if s[1] != s[2]:
            print(f"{s[0]:72} {s[1]:6} KB -> {s[2]:5} KB")
    print(f"seo: {len(pages)} pages, {len(copies)} paper copies, {len(mds)} markdown copies, llms-full.txt {len(''.join(mds)) // 1024} KB")


if __name__ == "__main__":
    main()
