# The ontology package

Every paper folder carries `ontology/objects.json`. [Praxis](https://muhammadumar89.github.io/codeninja-research/praxis/), CodeNinja's platform for designing physical AI systems, writes it for every design. [Hyper Ontology](https://muhammadumar89.github.io/codeninja-research/hyper-ontology/), CodeNinja's ontology platform, imports it and stands the model up as a living ontology over the operator's own systems. Until Hyper Ontology publishes its import format, this file is the format, and the two will be kept in agreement.

To load, validate or convert a package (Mermaid, Cypher, JSON-LD), use the [hyper-ontology loader](hyper-ontology-py/).

## Shape

```json
{
  "package": "hyper-ontology/1",
  "designed_with": "Praxis",
  "implemented_with": "Hyper Ontology",
  "paper": {"title": "...", "url": "https://muhammadumar89.github.io/codeninja-research/<folder>/", "doi": "..."},
  "sector": "oil-and-gas",
  "country": "Pakistan",
  "objects": [
    {
      "id": "hse-incident",
      "label": "HSE Incident",
      "kind": "record",
      "anchored_in": "SAP EHS",
      "properties": ["Incident type", "Location", "Severity classification", "Root cause category", "Barrier status", "Reporting date"],
      "status_vocabulary": ["Reported", "Under investigation", "Investigation complete", "Closed"],
      "links": [{"to": "operational-site", "label": "occurs at"}, {"to": "work-order", "label": "opens"}]
    }
  ],
  "write_paths": ["adapter tier", "decision record"],
  "human_loop": "every anomaly event moves Raised, Explained, Recommendation issued, Approved or Rejected, Closed; each transition is made by a named person"
}
```

## Rules

- `kind` is one of `record`, `asset`, `document`, `person`, `event`, `system`, `site`, `material`, `actor`, `measure`.
- `anchored_in` names the system of record the object is read from, or is empty for an object born inside the platform.
- `links` are typed and directional. The reverse is implied.
- Nothing in the file names the operator. The leak check that gates the paper gates this file too.
- The file is CC BY 4.0 like the paper. An operator that imports it owns its instance.

## What an agent does with it

1. Read the paper to understand why the objects are what they are.
2. Import `objects.json` into Hyper Ontology to stand the model up.
3. Map each `anchored_in` system to an adapter, read only.
4. Keep the decision record in Engram.

Step 2 is the step this package exists for.
