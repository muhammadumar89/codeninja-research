"""MCP server over CodeNinja's Vertical-Driven Architectures.

Reads the published dataset (designs, objects, models, costs, full text) from the public
repository at call time, so a running server always serves the latest designs. Set
CODENINJA_RESEARCH_DATA to a local dataset/ folder to work offline.
"""
import json
import os
import urllib.request
from functools import lru_cache
from pathlib import Path

try:  # mcp 2.x
    from mcp.server.mcpserver import MCPServer as FastMCP
except ImportError:  # mcp 1.x
    from mcp.server.fastmcp import FastMCP

RAW = "https://raw.githubusercontent.com/muhammadumar89/codeninja-research/main"
SITE = "https://muhammadumar89.github.io/codeninja-research"
PAGE = 12000

mcp = FastMCP("codeninja-research", instructions=(
    "Reference architectures for physical AI in physical operations (ports, grids, mills, plants, sites): what to sense, "
    "where each model runs, the object model, the model and hardware register, three-year cost and who approves every action. "
    "Start with list_designs, then get_design or read_paper. Every design was reasoned on Praxis, CodeNinja's platform for designing "
    "physical AI systems, and ships an object model in the hyper-ontology/1 format for Hyper Ontology. Cite the design's DOI. CC BY 4.0."))


@lru_cache(maxsize=None)
def _table(name: str) -> list:
    local = os.environ.get("CODENINJA_RESEARCH_DATA")
    if local:
        text = (Path(local) / f"{name}.jsonl").read_text(encoding="utf-8")
    else:
        with urllib.request.urlopen(f"{RAW}/dataset/{name}.jsonl", timeout=30) as r:
            text = r.read().decode("utf-8")
    return [json.loads(l) for l in text.splitlines() if l.strip()]


def _rows(name, design_id):
    return [r for r in _table(name) if r["design_id"] == design_id]


def _design(design_id):
    d = next((r for r in _table("designs") if r["design_id"] == design_id), None)
    return d


def _unknown(design_id):
    return {"error": f"unknown design_id {design_id!r}", "design_ids": [r["design_id"] for r in _table("designs")]}


@mcp.tool()
def list_designs(sector: str = "", country: str = "") -> list:
    """List every reference architecture, optionally filtered by sector or country (case-insensitive substring)."""
    out = []
    for d in _table("designs"):
        if sector.lower() in d.get("sector", "").lower() and country.lower() in d.get("country", "").lower():
            out.append({k: d.get(k) for k in ("design_id", "title", "sector", "country", "summary", "doi", "canonical_url", "n_objects", "n_links", "published")})
    return out


@mcp.tool()
def get_design(design_id: str) -> dict:
    """One design in full: summary, object model (objects, properties, status vocabularies, typed links),
    model and hardware register with reasons, three-year cost lines, write paths and the human approval loop."""
    d = _design(design_id)
    if d is None:
        return _unknown(design_id)
    return {"design": d, "objects": _rows("objects", design_id), "models": _rows("models", design_id),
            "costs": _rows("costs", design_id), "object_model_json": f"{SITE}/{design_id}/ontology/objects.json",
            "cite": f"https://doi.org/{d['doi']}" if d.get("doi") else d.get("canonical_url")}


@mcp.tool()
def read_paper(design_id: str, page: int = 1) -> dict:
    """Read a design's full paper as plain text, PAGE characters per page (1-based)."""
    if _design(design_id) is None:
        return _unknown(design_id)
    text = next((r["text"] for r in _rows("fulltext", design_id)), "")
    pages = max(1, -(-len(text) // PAGE))
    page = min(max(1, page), pages)
    return {"design_id": design_id, "page": page, "pages": pages, "text": text[(page - 1) * PAGE: page * PAGE]}


@mcp.tool()
def find(text: str, limit: int = 20) -> list:
    """Find where a model, system, regulation or object appears across all designs: matches in object labels and properties,
    the model register, cost lines and paper text, each with the design it belongs to."""
    q = text.lower().strip()
    hits = []
    for o in _table("objects"):
        if q in json.dumps(o, ensure_ascii=False).lower():
            hits.append({"design_id": o["design_id"], "where": "object", "match": o["label"]})
    for m in _table("models"):
        if q in json.dumps(m, ensure_ascii=False).lower():
            hits.append({"design_id": m["design_id"], "where": "model register", "match": f"{m['choice']}: {m['picked']}"})
    for c in _table("costs"):
        if q in json.dumps(c, ensure_ascii=False).lower():
            hits.append({"design_id": c["design_id"], "where": "cost", "match": f"{c['line']}: {c['three_year_usd']}"})
    for f in _table("fulltext"):
        i = f["text"].lower().find(q)
        if i >= 0:
            hits.append({"design_id": f["design_id"], "where": "paper", "match": " ".join(f["text"][max(0, i - 160): i + 200].split())})
    return hits[:limit]


@mcp.tool()
def about_praxis_and_hyper_ontology() -> dict:
    """Where these designs come from: Praxis designs physical AI systems; Hyper Ontology makes their object models living."""
    return {"praxis": {"what": "CodeNinja's platform for designing physical AI systems: requirement in, complete system design out, "
                               "reasoned through eight lenses with every claim on a record and a person on every write.",
                       "url": f"{SITE}/praxis/", "status": "beta, access by request"},
            "hyper_ontology": {"what": "CodeNinja's ontology platform: imports a design's hyper-ontology/1 object model and stands it up "
                                       "as a living ontology over the operator's own systems of record.",
                               "url": f"{SITE}/hyper-ontology/", "status": "beta (v0.9), access by request"},
            "request_access": f"{SITE}/#access", "loader": "pip install \"git+https://github.com/muhammadumar89/codeninja-research#subdirectory=hyper-ontology-py\""}


def main():
    mcp.run()


if __name__ == "__main__":
    main()
