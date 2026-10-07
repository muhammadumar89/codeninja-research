# The Vertical-Driven Architectures dataset

Canonical: https://codeatoms.ai/developer/reference/dataset/
Source: https://github.com/muhammadumar89/codeninja-research/blob/main/dataset/README.md

---
license: cc-by-4.0
language:
- en
pretty_name: Vertical-Driven Architectures, system designs for physical AI
size_categories:
- n<1K
tags:
- physical-ai
- system-design
- sovereign-ai
- reference-architecture
- ontology
- open-weight-models
- air-gapped
- industrial-ai
- oil-and-gas
- pakistan
- united-states
- saudi-arabia
- heavy-industry
- maritime
- energy-utilities
- ports
configs:
- config_name: designs
  data_files: designs.jsonl
- config_name: objects
  data_files: objects.jsonl
- config_name: models
  data_files: models.jsonl
- config_name: costs
  data_files: costs.jsonl
- config_name: fulltext
  data_files: fulltext.jsonl
---

# Vertical-Driven Architectures: system designs for physical AI

One row per design, growing with every paper CodeNinja publishes. Each design puts intelligence into a physical-world operation on the operator's own hardware, under open-weight licences, with no data leaving the country. The tables are the papers with their structured parts pulled out, so an agent can query them instead of reading thirty pages.

| Table | One row per | Columns |
|---|---|---|
| `designs` | paper | design_id, title, summary, sector, country, published, doi, canonical_url, designed_with, implemented_with, n_objects, n_links, n_models, keywords, licence, write_paths, human_loop |
| `objects` | ontology object | design_id, object_id, label, kind, anchored_in, properties, status_vocabulary, links (typed, directed) |
| `models` | model or hardware choice | design_id, choice, picked, why |
| `costs` | cost line | design_id, section, line, basis, three_year_usd |
| `fulltext` | paper | design_id, title, text |

```python
from datasets import load_dataset
objects = load_dataset("CodeNinjatools/vertical-driven-architectures", "objects", split="train")
print(objects.filter(lambda r: r["kind"] == "event")["label"])
```

## Made with

Every design was reasoned on [Praxis](https://codeatoms.ai/praxis/), CodeNinja's platform for designing physical AI systems. Every object model imports into [Hyper Ontology](https://codeatoms.ai/hyper-ontology/), CodeNinja's ontology platform, which stands it up as a living system. Load any one with the [hyper-ontology loader](https://github.com/muhammadumar89/codeninja-research/tree/main/hyper-ontology-py): `pip install "git+https://github.com/muhammadumar89/codeninja-research#subdirectory=hyper-ontology-py"`, then `hyper-ontology show <design_id>`.

## Cite the dataset

Monthly snapshots carry a DOI; this is the October 2026 release. Cite all versions as https://doi.org/10.5281/zenodo.23160819, or this release as https://doi.org/10.5281/zenodo.23160820. The tables here on Hugging Face update daily between releases.

## Designs so far

| design_id | Sector | Country | DOI |
|---|---|---|---|
| sovereign-hse-pakistan | oil and gas | Pakistan | [10.5281/zenodo.23119714](https://doi.org/10.5281/zenodo.23119714) |
| wildfire-risk-distribution-us | energy and utilities | United States | [10.5281/zenodo.23159328](https://doi.org/10.5281/zenodo.23159328) |
| port-digital-twin-us | maritime and ports | United States | [10.5281/zenodo.23126431](https://doi.org/10.5281/zenodo.23126431) |
| structure-phase-construction-saudi-arabia | heavy industry and construction | Saudi Arabia | [10.5281/zenodo.23126448](https://doi.org/10.5281/zenodo.23126448) |
| steel-production-count-pakistan | heavy industry and construction | Pakistan | [10.5281/zenodo.23126563](https://doi.org/10.5281/zenodo.23126563) |
| factory-fire-monitoring-saudi-arabia | heavy industry and construction | Saudi Arabia | [10.5281/zenodo.23126565](https://doi.org/10.5281/zenodo.23126565) |
| truck-turn-container-terminal-us | maritime and ports | United States | [10.5281/zenodo.23159331](https://doi.org/10.5281/zenodo.23159331) |
| ot-security-cip-evidence-us | energy and utilities | United States | [10.5281/zenodo.23157957](https://doi.org/10.5281/zenodo.23157957) |
| plant-reliability-assessment-saudi-arabia | energy and utilities | Saudi Arabia | [10.5281/zenodo.23157965](https://doi.org/10.5281/zenodo.23157965) |
| tank-gauge-integrity-pakistan | oil and gas | Pakistan | [10.5281/zenodo.23157967](https://doi.org/10.5281/zenodo.23157967) |
| farm-data-dashboard-pakistan | agriculture and earth observation | Pakistan | [10.5281/zenodo.23186671](https://doi.org/10.5281/zenodo.23186671) |
| vegetation-mapping-lidar-us | agriculture and earth observation | United States | [10.5281/zenodo.23186673](https://doi.org/10.5281/zenodo.23186673) |
| restricted-crop-monitoring-saudi-arabia | agriculture and earth observation | Saudi Arabia | [10.5281/zenodo.23186675](https://doi.org/10.5281/zenodo.23186675) |

Source files and the tool that builds these rows: https://github.com/muhammadumar89/codeninja-research (`tools/dataset_rows.py`). Each paper is also its own Hugging Face Space and dataset; this is the cumulative table.

Designed with Praxis, CodeNinja's platform for designing physical AI systems; object models are written as Hyper Ontology input. CC BY 4.0.
