"""Append one paper's rows to the Vertical-Driven Architectures dataset.

    python3 tools/dataset_rows.py <paper folder>

Reads the folder the packager built (ontology/objects.json, register/models.csv,
paper/appendix_a_cost.md, paper/at_a_glance.md, index.html for the metadata,
the PDF for the full text) and appends to dataset/*.jsonl at the repo root:

  designs.jsonl   one row per paper
  objects.jsonl   one row per ontology object
  models.jsonl    one row per model or hardware choice
  costs.jsonl     one row per cost line in Appendix A
  fulltext.jsonl  one row per paper, the whole text as Markdown-ish plain text

A paper already present (same design_id) is replaced, never duplicated.
The dataset is the paper with its tables pulled out: nothing here is written
that the paper does not say.
"""
import csv
import html
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "dataset"


def meta_of(index_html: Path) -> dict:
    h = index_html.read_text(encoding="utf-8")
    g = lambda n: html.unescape((re.search(rf'<meta name="{n}" content="([^"]*)"', h) or [None, ""])[1])
    og = lambda n: html.unescape((re.search(rf'<meta property="og:{n}" content="([^"]*)"', h) or [None, ""])[1])
    ld = re.search(r'<script type="application/ld\+json">(.*?)</script>', h, re.S)
    j = json.loads(ld.group(1)) if ld else {}
    return {"title": g("citation_title"), "description": og("description"), "date": g("citation_publication_date").replace("/", "-"),
            "doi": g("citation_doi"), "canonical_url": g("citation_abstract_html_url") or og("url"),
            "keywords": [k.strip() for k in g("citation_keywords").split(";") if k.strip()],
            "country": (j.get("spatialCoverage") or {}).get("name", ""), "sector": next((a.get("name") for a in j.get("about", []) if a.get("name") not in ("sovereign AI", "health, safety and environment")), "")}


def costs_of(md: Path) -> list:
    rows, section = [], ""
    for ln in md.read_text(encoding="utf-8").splitlines():
        if ln.startswith("## "):
            section = ln[3:].strip()
        if ln.startswith("|") and not re.match(r"^\|\s*-", ln):
            cells = [c.strip() for c in ln.strip().strip("|").split("|")]
            if len(cells) >= 3 and cells[0] not in ("Line", "Option", "Model", "Part"):
                rows.append({"section": section, "line": cells[0].strip("*"), "basis": cells[1], "three_year_usd": cells[2].strip("*")})
    return rows


def fulltext_of(pdf: Path) -> str:
    t = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True, text=True).stdout
    t = "\n".join(ln for ln in t.replace("\f", "\n").splitlines() if not re.fullmatch(r"\s*\d{1,3}\s*", ln))
    return re.sub(r"\n{3,}", "\n\n", t)


def upsert(path: Path, rows: list, key: str, design_id: str):
    old = []
    if path.exists():
        old = [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]
    kept = [r for r in old if r.get(key) != design_id]
    path.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in kept + rows), encoding="utf-8")
    return len(rows)


def main(folder):
    f = Path(folder).resolve()
    OUT.mkdir(exist_ok=True)
    design_id = f.name
    m = meta_of(f / "index.html")
    pkg = json.loads((f / "ontology" / "objects.json").read_text(encoding="utf-8"))
    pdf = next(iter(sorted((f / "paper").glob("*.pdf"))))
    reg = list(csv.DictReader(open(f / "register" / "models.csv", encoding="utf-8")))
    costs = costs_of(f / "paper" / "appendix_a_cost.md") if (f / "paper" / "appendix_a_cost.md").exists() else []
    objs = pkg["objects"]
    designs = [{"design_id": design_id, "title": m["title"], "summary": m["description"], "sector": m["sector"] or pkg.get("sector", ""),
                "country": m["country"] or pkg.get("country", ""), "published": m["date"], "doi": m["doi"], "canonical_url": m["canonical_url"],
                "designed_with": pkg.get("designed_with", "Praxis"), "implemented_with": pkg.get("implemented_with", "Hyper Ontology"),
                "n_objects": len(objs), "n_links": sum(len(o.get("links", [])) for o in objs), "n_models": sum(1 for r in reg if re.search(r"model|detector|tracking|forecast|embedding|ocr", r.get("choice", ""), re.I)),
                "keywords": m["keywords"], "licence": "CC-BY-4.0", "write_paths": pkg.get("write_paths", []), "human_loop": pkg.get("human_loop", "")}]
    objects = [{"design_id": design_id, "object_id": o["id"], "label": o["label"], "kind": o["kind"], "anchored_in": o.get("anchored_in", ""),
                "properties": o.get("properties", []), "status_vocabulary": o.get("status_vocabulary", []),
                "links": o.get("links", [])} for o in objs]
    models = [{"design_id": design_id, "choice": r.get("choice", ""), "picked": r.get("picked", ""), "why": r.get("why", "")} for r in reg]
    cost_rows = [dict(design_id=design_id, **c) for c in costs]
    full = [{"design_id": design_id, "title": m["title"], "text": fulltext_of(pdf)}]
    n = {k: upsert(OUT / f"{k}.jsonl", v, "design_id", design_id) for k, v in
         (("designs", designs), ("objects", objects), ("models", models), ("costs", cost_rows), ("fulltext", full))}
    print(f"{design_id}: " + ", ".join(f"{k} {v}" for k, v in n.items()))


if __name__ == "__main__":
    main(sys.argv[1])
