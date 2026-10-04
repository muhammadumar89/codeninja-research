import json
import re
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path

FORMAT = "hyper-ontology/1"
KINDS = ("record", "asset", "document", "person", "event", "system", "site", "material", "actor", "measure")
INDEX = "https://muhammadumar89.github.io/codeninja-research/"


@dataclass
class Package:
    raw: dict
    source: str = ""
    objects: list = field(default_factory=list)

    @property
    def title(self): return (self.raw.get("paper") or {}).get("title", "")
    @property
    def doi(self): return (self.raw.get("paper") or {}).get("doi", "")
    @property
    def country(self): return self.raw.get("country", "")
    @property
    def sector(self): return self.raw.get("sector", "")
    def by_id(self): return {o["id"]: o for o in self.objects}
    def links(self):
        return [(o["id"], l.get("label", ""), l["to"]) for o in self.objects for l in o.get("links", [])]


def load(src) -> Package:
    """A path, a URL, a dict, or a design slug from the CodeNinja research index."""
    if isinstance(src, dict):
        raw, where = src, "<dict>"
    else:
        s = str(src)
        if re.fullmatch(r"[a-z0-9-]+", s) and not Path(s).exists():
            s = f"{INDEX}{s}/ontology/objects.json"
        if s.startswith(("http://", "https://")):
            with urllib.request.urlopen(s, timeout=30) as r:
                raw = json.loads(r.read().decode("utf-8"))
        else:
            raw = json.loads(Path(s).read_text(encoding="utf-8"))
        where = s
    return Package(raw=raw, source=where, objects=list(raw.get("objects", [])))


def validate(pkg: Package) -> list:
    """Problems as plain sentences; an empty list means the package is valid."""
    p, raw = [], pkg.raw
    if raw.get("package") != FORMAT:
        p.append(f"package is {raw.get('package')!r}, expected {FORMAT!r}")
    if not pkg.objects:
        p.append("the package holds no objects")
    ids = [o.get("id") for o in pkg.objects]
    for d in sorted({i for i in ids if ids.count(i) > 1}):
        p.append(f"object id {d!r} appears more than once")
    known = set(ids)
    for o in pkg.objects:
        oid = o.get("id", "?")
        for k in ("id", "label", "kind"):
            if not o.get(k):
                p.append(f"object {oid!r} has no {k}")
        if o.get("kind") and o["kind"] not in KINDS:
            p.append(f"object {oid!r} has kind {o['kind']!r}, not one of {', '.join(KINDS)}")
        if not isinstance(o.get("properties", []), list):
            p.append(f"object {oid!r}: properties must be a list")
        for l in o.get("links", []):
            if l.get("to") not in known:
                p.append(f"object {oid!r} links to {l.get('to')!r}, which is not an object in the package")
    return p


def summary(pkg: Package) -> str:
    kinds = {}
    for o in pkg.objects:
        kinds.setdefault(o.get("kind", "?"), []).append(o.get("label", o.get("id")))
    lines = [pkg.title or pkg.source, f"{len(pkg.objects)} objects, {len(pkg.links())} typed links"
             + (f", {pkg.sector.replace('-', ' ')}, {pkg.country}" if pkg.country else "")]
    if pkg.doi:
        lines.append(f"DOI {pkg.doi}")
    for k in sorted(kinds):
        lines.append(f"  {k}: {', '.join(kinds[k])}")
    anchors = sorted({o.get("anchored_in") for o in pkg.objects if o.get("anchored_in")})
    if anchors:
        lines.append(f"  anchored in: {', '.join(anchors)}")
    if pkg.raw.get("human_loop"):
        lines.append(f"  human loop: {pkg.raw['human_loop']}")
    return "\n".join(lines)


def _node(oid): return re.sub(r"[^A-Za-z0-9_]", "_", oid)


def to_mermaid(pkg: Package) -> str:
    """A Mermaid class diagram: one class per object, its properties, and the typed links."""
    out = ["classDiagram"]
    for o in pkg.objects:
        out.append(f'  class {_node(o["id"])}["{o.get("label", o["id"]).replace(chr(34), "")}"] {{')
        out.append(f"    <<{o.get('kind', '')}>>")
        for prop in o.get("properties", [])[:8]:
            out.append("    " + re.sub(r"[{}<>\"]", "", prop))
        out.append("  }")
    for a, label, b in pkg.links():
        out.append(f"  {_node(a)} --> {_node(b)} : {label or 'links to'}")
    return "\n".join(out)


def _cy(s): return str(s).replace("\\", "\\\\").replace("'", "\\'")


def to_cypher(pkg: Package) -> str:
    """Cypher that loads the model's schema into a graph: one :ObjectType node per object, its
    properties and status vocabulary as lists, and a :LINKS relationship per typed link."""
    out = ["CREATE CONSTRAINT object_type_id IF NOT EXISTS FOR (t:ObjectType) REQUIRE t.id IS UNIQUE;"]
    for o in pkg.objects:
        props = "[" + ", ".join(f"'{_cy(p)}'" for p in o.get("properties", [])) + "]"
        status = "[" + ", ".join(f"'{_cy(s)}'" for s in o.get("status_vocabulary", [])) + "]"
        out.append(f"MERGE (t:ObjectType {{id: '{_cy(o['id'])}'}}) SET t.label = '{_cy(o.get('label', ''))}', t.kind = '{_cy(o.get('kind', ''))}', "
                   f"t.anchored_in = '{_cy(o.get('anchored_in', ''))}', t.properties = {props}, t.status_vocabulary = {status};")
    for a, label, b in pkg.links():
        out.append(f"MATCH (a:ObjectType {{id: '{_cy(a)}'}}), (b:ObjectType {{id: '{_cy(b)}'}}) MERGE (a)-[:LINKS {{label: '{_cy(label)}'}}]->(b);")
    return "\n".join(out)


def to_jsonld(pkg: Package) -> dict:
    """The model as JSON-LD with schema.org and RDFS terms, for triple stores and search."""
    base = (pkg.raw.get("paper") or {}).get("url", "urn:hyper-ontology:") .rstrip("/") + "#"
    graph = []
    for o in pkg.objects:
        graph.append({"@id": base + o["id"], "@type": "rdfs:Class", "rdfs:label": o.get("label", ""),
                      "hyper:kind": o.get("kind", ""), "hyper:anchoredIn": o.get("anchored_in", ""),
                      "hyper:property": o.get("properties", []), "hyper:status": o.get("status_vocabulary", [])})
    for a, label, b in pkg.links():
        graph.append({"@id": f"{base}{a}--{re.sub(r'[^a-z0-9]+', '-', (label or 'links-to').lower())}--{b}", "@type": "rdf:Property",
                      "rdfs:label": label, "rdfs:domain": {"@id": base + a}, "rdfs:range": {"@id": base + b}})
    return {"@context": {"rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#", "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
                         "hyper": "https://muhammadumar89.github.io/codeninja-research/hyper-ontology/#"},
            "@graph": graph}


def traverse(pkg: Package, start: str, depth: int = 2) -> list:
    """Every path of typed links from one object, up to `depth` hops, in either direction:
    the reach a query on the living ontology has from that object."""
    adj = {}
    for a, label, b in pkg.links():
        adj.setdefault(a, []).append((label, b, "->"))
        adj.setdefault(b, []).append((label, a, "<-"))
    paths, frontier = [], [[start]]
    for _ in range(depth):
        nxt = []
        for path in frontier:
            for label, other, d in adj.get(path[-1], []):
                if other in path[::2]:
                    continue
                p = path + [f"{d}[{label}]", other]
                paths.append(p); nxt.append(p)
        frontier = nxt
    return [" ".join(p) for p in paths]
