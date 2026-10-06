"""hyper-ontology: load, validate and convert hyper-ontology/1 packages.

A package is the object model of one system design: typed objects, their properties and
status vocabularies, the system of record each is anchored in, and typed directional links.
Praxis writes one for every design it reasons; Hyper Ontology imports it and stands it up as
a living ontology over the operator's own systems.

    from hyper_ontology import load, validate, to_mermaid, to_cypher
    pkg = load("https://codeatoms.ai/port-digital-twin-us/ontology/objects.json")
    assert not validate(pkg)
    print(to_mermaid(pkg))
"""
from .core import FORMAT, KINDS, Package, load, validate, summary, to_mermaid, to_cypher, to_jsonld, traverse

__all__ = ["FORMAT", "KINDS", "Package", "load", "validate", "summary", "to_mermaid", "to_cypher", "to_jsonld", "traverse"]
__version__ = "0.1.0"
