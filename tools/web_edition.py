"""The web edition of a paper: the platform's own HTML, with what agents and
Google Scholar read added, and the cost appendix in place.

    python web_edition.py paper.html summary.md appendix.md meta.json out.html

meta.json: {"title", "subtitle", "authors": [...], "date": "YYYY-MM-DD",
            "canonical", "pdf_url", "doi"?, "keywords": [...], "country", "sector",
            "about"?: [...topics after the sector; defaults to the first paper's]}

Adds to <head>: canonical, Open Graph, Highwire citation_* tags, schema.org
TechArticle + ScholarlyArticle JSON-LD. Adds after the cover: an "At a glance"
section (the answer and the numbers in the first screen, which is where answer
engines take their quotes from). Adds before the Source Register: Appendix A.
"""
import html
import json
import re
import sys
from pathlib import Path


def md_inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
    s = re.sub(r"(https?://[^\s<)]+)", r'<a href="\1">\1</a>', s)
    return s


def md_block(md, h1_class=""):
    out, rows, ul = [], [], False

    def flush_rows():
        nonlocal rows
        if rows:
            head, body = rows[0], rows[2:]
            t = ['<table class="ed"><thead><tr>' + "".join(f"<th>{md_inline(c)}</th>" for c in head) + "</tr></thead><tbody>"]
            for r in body:
                t.append("<tr>" + "".join(f"<td>{md_inline(c)}</td>" for c in r) + "</tr>")
            out.append("".join(t) + "</tbody></table>")
            rows = []

    for ln in md.splitlines():
        if ln.startswith("|"):
            rows.append([c.strip() for c in ln.strip().strip("|").split("|")])
            continue
        flush_rows()
        if ul and not ln.startswith("- "):
            out.append("</ul>"); ul = False
        if ln.startswith("# "):
            eyebrow, _, head = ln[2:].partition(" · ")
            out.append(f'<div class="eyebrow">{md_inline(eyebrow)}</div><h2 class="claim">{md_inline(head or eyebrow)}</h2>')
        elif ln.startswith("## "):
            out.append(f"<h3>{md_inline(ln[3:])}</h3>")
        elif ln.startswith("- "):
            if not ul:
                out.append("<ul>"); ul = True
            out.append(f"<li>{md_inline(ln[2:])}</li>")
        elif ln.strip():
            out.append(f"<p>{md_inline(ln)}</p>")
    flush_rows()
    if ul:
        out.append("</ul>")
    return "\n".join(out)


def head_tags(m):
    e = lambda s: html.escape(str(s), quote=True)
    tags = [f'<link rel="canonical" href="{e(m["canonical"])}">',
            f'<meta property="og:type" content="article">',
            f'<meta property="og:title" content="{e(m["title"])}">',
            f'<meta property="og:description" content="{e(m["subtitle"])}">',
            f'<meta property="og:url" content="{e(m["canonical"])}">',
            f'<meta name="citation_title" content="{e(m["title"])}">']
    tags += [f'<meta name="citation_author" content="{e(a)}">' for a in m["authors"]]
    tags += [f'<meta name="citation_publication_date" content="{e(m["date"].replace("-", "/"))}">',
             '<meta name="citation_publisher" content="CodeNinja">',
             '<meta name="citation_technical_report_institution" content="CodeNinja">',
             '<meta name="citation_language" content="en">',
             f'<meta name="citation_abstract_html_url" content="{e(m["canonical"])}">',
             f'<meta name="citation_pdf_url" content="{e(m["pdf_url"])}">',
             f'<meta name="citation_keywords" content="{e("; ".join(m["keywords"]))}">',
             f'<meta name="keywords" content="{e(", ".join(m["keywords"]))}">']
    if m.get("doi"):
        tags.append(f'<meta name="citation_doi" content="{e(m["doi"])}">')
    ld = {"@context": "https://schema.org", "@type": ["TechArticle", "ScholarlyArticle"],
          "headline": m["title"], "description": m["subtitle"], "abstract": m["subtitle"],
          "url": m["canonical"], "mainEntityOfPage": m["canonical"], "datePublished": m["date"],
          "dateModified": m["date"], "inLanguage": "en", "keywords": m["keywords"],
          "about": [{"@type": "Thing", "name": k} for k in ([m.get("sector")] + m.get("about", ["sovereign AI", "health, safety and environment"])) if k],
          "spatialCoverage": {"@type": "Country", "name": m["country"]} if m.get("country") else None,
          "author": [{"@type": "Organization", "name": "CodeNinja", "url": "https://codeninjaconsulting.com"}],
          "publisher": {"@type": "Organization", "name": "CodeNinja", "url": "https://codeninjaconsulting.com"},
          "encoding": {"@type": "MediaObject", "contentUrl": m["pdf_url"], "encodingFormat": "application/pdf"},
          "isAccessibleForFree": True, "license": "https://creativecommons.org/licenses/by/4.0/"}
    if m.get("doi"):
        ld["identifier"] = {"@type": "PropertyValue", "propertyID": "DOI", "value": m["doi"]}
        ld["sameAs"] = f"https://doi.org/{m['doi']}"
    ld = {k: v for k, v in ld.items() if v is not None}
    tags.append('<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + "</script>")
    tags.append("<style>.glance{background:var(--tint);border:1px solid var(--aline);border-radius:8px;padding:18px 22px;margin:28px 0}"
                ".glance h2{font-size:20px;margin-top:0}table.ed{width:100%;border-collapse:collapse;font-size:13.5px;margin:10px 0 18px;background:var(--tint)}"
                "table.ed th{font:700 10px/1.4 Arial;letter-spacing:.14em;text-transform:uppercase;color:var(--amber);text-align:left;padding:7px 9px;border:1px solid var(--aline)}"
                "table.ed td{padding:7px 9px;border:1px solid var(--aline);vertical-align:top}</style>")
    return "\n".join(tags)


def main(paper_html, summary_md, appendix_md, meta_json, out):
    h = Path(paper_html).read_text(encoding="utf-8")
    m = json.loads(Path(meta_json).read_text(encoding="utf-8"))
    if "<title>" in h:
        h = re.sub(r"<title>.*?</title>", f"<title>{html.escape(m['title'])}</title>", h, count=1, flags=re.S)
    h = h.replace("</head>", head_tags(m) + "\n</head>", 1)
    glance = '<section class="glance" id="at-a-glance">' + md_block(Path(summary_md).read_text(encoding="utf-8")) + "</section>"
    assert "</header>" in h, "no cover header"
    h = h.replace("</header>", "</header>\n" + glance, 1)
    apx = '<section id="appendix-a">' + md_block(Path(appendix_md).read_text(encoding="utf-8")) + "</section>"
    assert '<section id="sources">' in h, "no source register"
    h = h.replace('<section id="sources">', apx + '\n<section id="sources">', 1)
    Path(out).write_text(h, encoding="utf-8")
    print(f"web edition: {len(h) // 1024} KB -> {out}")


if __name__ == "__main__":
    main(*sys.argv[1:6])
