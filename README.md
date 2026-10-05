# CodeNinja Atoms

Reference architectures for autonomy in physical operations. Every design here is sovereign: it runs on the operator's own hardware, under open-weight licences, with no data leaving the country. Praxis designs them, Hyper Ontology implements the object model, Engram keeps the record of decisions.

Each folder is one paper and carries the same five things:

| File | What it is |
|---|---|
| `paper/*.pdf` | the paper, with a cost appendix where the design prices its own hardware |
| `README.md` | the abstract, who the paper is for, and the one-page design |
| `ontology/objects.json` | the object model as Hyper Ontology input: every object, its properties, status vocabulary and typed links |
| `register/models.csv` | the model and equipment register: each model, licence, placement, weight at each precision |
| `figures/` | the paper's figures, redrawn with the operator described by class, never by name |

Read each paper online through its link below; the PDF, the object model and the register sit in its folder. Releases carry a DOI through Zenodo; cite that.

## The dataset

Every design here is also a row in [CodeNinjatools/vertical-driven-architectures](https://huggingface.co/datasets/CodeNinjatools/vertical-driven-architectures): tables of designs, ontology objects, model choices, cost lines and full text, one row per paper, mirrored in [`dataset/`](dataset/). Agents query the tables; people read the papers.

## Papers

| Paper | Sector | Country | DOI |
|---|---|---|---|
| [Feeder Firewatch: Live Ignition and Outage Risk for Every Distribution Feeder](wildfire-risk-distribution-us/) ([read online](https://muhammadumar89.github.io/codeninja-research/wildfire-risk-distribution-us/)) | Energy and utilities | United States | [10.5281/zenodo.23159328](https://doi.org/10.5281/zenodo.23159328) |
| [Terminal Pulse: Predicted Truck Turn Time and Live Yard Sight for a Container Terminal](truck-turn-container-terminal-us/) ([read online](https://muhammadumar89.github.io/codeninja-research/truck-turn-container-terminal-us/)) | Maritime and ports | United States | [10.5281/zenodo.23159331](https://doi.org/10.5281/zenodo.23159331) |
| [Sovereign HSE Watch: A Reference Architecture for Predictive Health, Safety and Environment Intelligence in Pakistan's Oil and Gas Operations](sovereign-hse-pakistan/) ([read online](https://muhammadumar89.github.io/codeninja-research/sovereign-hse-pakistan/)) | Oil and gas | Pakistan | [10.5281/zenodo.23119714](https://doi.org/10.5281/zenodo.23119714) |
| [Port Twin: One Governed Digital Twin for Every Asset, Feed and Dollar](port-digital-twin-us/) ([read online](https://muhammadumar89.github.io/codeninja-research/port-digital-twin-us/)) | Maritime and ports | United States | [10.5281/zenodo.23126431](https://doi.org/10.5281/zenodo.23126431) |
| [Structure Phase Watch: Live Production, Crane and Delivery Evidence for Every Pour on a Construction Site](structure-phase-construction-saudi-arabia/) ([read online](https://muhammadumar89.github.io/codeninja-research/structure-phase-construction-saudi-arabia/)) | Heavy industry and construction | Saudi Arabia | [10.5281/zenodo.23126448](https://doi.org/10.5281/zenodo.23126448) |
| [Steel Count Ledger: Independently Counted Production for Every Steel Mill in Pakistan](steel-production-count-pakistan/) ([read online](https://muhammadumar89.github.io/codeninja-research/steel-production-count-pakistan/)) | Heavy industry and construction | Pakistan | [10.5281/zenodo.23126563](https://doi.org/10.5281/zenodo.23126563) |
| [Factory Fire Watch: Read-Only Smart Fire Protection Monitoring for Every High-Risk Factory](factory-fire-monitoring-saudi-arabia/) ([read online](https://muhammadumar89.github.io/codeninja-research/factory-fire-monitoring-saudi-arabia/)) | Heavy industry and construction | Saudi Arabia | [10.5281/zenodo.23126565](https://doi.org/10.5281/zenodo.23126565) |

## Methods

| Paper | DOI |
|---|---|
| [How Praxis Designs Physical AI Systems](https://muhammadumar89.github.io/codeninja-research/praxis-method/) | [10.5281/zenodo.23132102](https://doi.org/10.5281/zenodo.23132102) |
| [From Reference Architecture to Living Ontology](https://muhammadumar89.github.io/codeninja-research/ontology-method/) | [10.5281/zenodo.23132104](https://doi.org/10.5281/zenodo.23132104) |

## For agents and developers

- [`mcp-server/`](mcp-server/): an MCP server that gives coding agents every design (`list_designs`, `get_design`, `read_paper`, `find`).
- [`hyper-ontology-py/`](hyper-ontology-py/): load, validate and convert any `ontology/objects.json` (Mermaid, Cypher, JSON-LD); format in [ONTOLOGY_PACKAGE.md](ONTOLOGY_PACKAGE.md).
- [`llms.txt`](https://muhammadumar89.github.io/codeninja-research/llms.txt) and the [dataset](https://huggingface.co/datasets/CodeNinjatools/vertical-driven-architectures).

## Licence

Text, figures and data: [CC BY 4.0](LICENSE). Cite the DOI or the paper URL.

## About CodeNinja

CodeNinja is a Middle Eastern American artificial intelligence lab focused on building self-improving systems. We are reinventing knowledge work to close the loop between vertical AI use cases and the generalized intelligence that fuels it, accelerating the path toward organizational superintelligence.
