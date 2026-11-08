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

Every published design is also listed as one of our [sovereign AI reference architectures](https://codeatoms.ai/sovereign-ai-reference-architectures/), with its sector, country, compute and three-year cost, and every object model is browsable among the [industrial ontology examples](https://codeatoms.ai/industrial-ontology-examples/).

Read each paper online through its link below; the PDF, the object model and the register sit in its folder. Releases carry a DOI through Zenodo; cite that.

## The dataset

Every design here is also a row in [CodeNinjatools/vertical-driven-architectures](https://huggingface.co/datasets/CodeNinjatools/vertical-driven-architectures): tables of designs, ontology objects, model choices, cost lines and full text, one row per paper, mirrored in [`dataset/`](dataset/). Agents query the tables; people read the papers.

## Papers

| Paper | Sector | Country | DOI |
|---|---|---|---|
| [Silicon Ledger: Ontologies for Semiconductor Design From Specification to Tapeout in Saudi Arabia](chip-design-ontology-saudi-arabia/) ([read online](https://codeatoms.ai/chip-design-ontology-saudi-arabia/)) | Semiconductors | Saudi Arabia | [10.5281/zenodo.23693146](https://doi.org/10.5281/zenodo.23693146) |
| [Sovereign AI Architecture for a Grid Control Room in Saudi Arabia](grid-control-room-saudi-arabia/) ([read online](https://codeatoms.ai/grid-control-room-saudi-arabia/)) | Energy and utilities | Saudi Arabia | [10.5281/zenodo.23889768](https://doi.org/10.5281/zenodo.23889768) |
| [Physical AI System Design for Wafer Defect Inspection in the United States](wafer-defect-inspection-us/) ([read online](https://codeatoms.ai/wafer-defect-inspection-us/)) | Semiconductors | United States | [10.5281/zenodo.23889770](https://doi.org/10.5281/zenodo.23889770) |
| [Industrial Data Ontology for a Water Utility in the United States](water-utility-ontology-us/) ([read online](https://codeatoms.ai/water-utility-ontology-us/)) | Energy and utilities | United States | [10.5281/zenodo.23889772](https://doi.org/10.5281/zenodo.23889772) |
| [Industrial AI for an Open Pit Mine Haul Fleet in Saudi Arabia](open-pit-mine-haul-fleet-saudi-arabia/) ([read online](https://codeatoms.ai/open-pit-mine-haul-fleet-saudi-arabia/)) | Mining | Saudi Arabia | [10.5281/zenodo.23889774](https://doi.org/10.5281/zenodo.23889774) |
| [Port Drone Watch: From Oil Sheen to Dispatched Work on the Port's Own Hardware in Germany](drone-detection-dispatch-port-germany/) ([read online](https://codeatoms.ai/drone-detection-dispatch-port-germany/)) | Maritime and ports | Germany | [10.5281/zenodo.23635729](https://doi.org/10.5281/zenodo.23635729) |
| [Depot Operating Object Model: Ontologies for Unifying Factory Systems at a United States Vehicle Rebuild Depot](factory-ontology-rebuild-depot-us/) ([read online](https://codeatoms.ai/factory-ontology-rebuild-depot-us/)) | Discrete manufacturing and automotive | United States | [10.5281/zenodo.23570177](https://doi.org/10.5281/zenodo.23570177) |
| [Feeder Firewatch: Live Ignition and Outage Risk for Every Distribution Feeder](wildfire-risk-distribution-us/) ([read online](https://codeatoms.ai/wildfire-risk-distribution-us/)) | Energy and utilities | United States | [10.5281/zenodo.23159328](https://doi.org/10.5281/zenodo.23159328) |
| [Terminal Pulse: Predicted Truck Turn Time and Live Yard Sight for a Container Terminal](truck-turn-container-terminal-us/) ([read online](https://codeatoms.ai/truck-turn-container-terminal-us/)) | Maritime and ports | United States | [10.5281/zenodo.23159331](https://doi.org/10.5281/zenodo.23159331) |
| [Sovereign HSE Watch: A Reference Architecture for Predictive Health, Safety and Environment Intelligence in Pakistan's Oil and Gas Operations](sovereign-hse-pakistan/) ([read online](https://codeatoms.ai/sovereign-hse-pakistan/)) | Oil and gas | Pakistan | [10.5281/zenodo.23119714](https://doi.org/10.5281/zenodo.23119714) |
| [Port Twin: One Governed Digital Twin for Every Asset, Feed and Dollar](port-digital-twin-us/) ([read online](https://codeatoms.ai/port-digital-twin-us/)) | Maritime and ports | United States | [10.5281/zenodo.23126431](https://doi.org/10.5281/zenodo.23126431) |
| [Structure Phase Watch: Live Production, Crane and Delivery Evidence for Every Pour on a Construction Site](structure-phase-construction-saudi-arabia/) ([read online](https://codeatoms.ai/structure-phase-construction-saudi-arabia/)) | Heavy industry and construction | Saudi Arabia | [10.5281/zenodo.23126448](https://doi.org/10.5281/zenodo.23126448) |
| [Steel Count Ledger: Independently Counted Production for Every Steel Mill in Pakistan](steel-production-count-pakistan/) ([read online](https://codeatoms.ai/steel-production-count-pakistan/)) | Heavy industry and construction | Pakistan | [10.5281/zenodo.23126563](https://doi.org/10.5281/zenodo.23126563) |
| [Factory Fire Watch: Read-Only Smart Fire Protection Monitoring for Every High-Risk Factory](factory-fire-monitoring-saudi-arabia/) ([read online](https://codeatoms.ai/factory-fire-monitoring-saudi-arabia/)) | Heavy industry and construction | Saudi Arabia | [10.5281/zenodo.23126565](https://doi.org/10.5281/zenodo.23126565) |
| [Industrial Ontology Examples: A Port Equipment and Berth Object Model in Saudi Arabia](port-equipment-berth-ontology-saudi-arabia/) ([read online](https://codeatoms.ai/port-equipment-berth-ontology-saudi-arabia/)) | Maritime and ports | Saudi Arabia | DOI pending |
| [Industrial Data Ontology for a Cold Chain From Plant to Store in the United States](cold-chain-ontology-us/) ([read online](https://codeatoms.ai/cold-chain-ontology-us/)) | Supply chain and logistics | United States | DOI pending |
| [A Self-Improving AI System for Cement Kiln Control in Saudi Arabia](cement-kiln-control-saudi-arabia/) ([read online](https://codeatoms.ai/cement-kiln-control-saudi-arabia/)) | Heavy industry and construction | Saudi Arabia | DOI pending |
| [Sovereign AI Reference Architectures for Passenger Rail Fleet Maintenance in Saudi Arabia](passenger-rail-fleet-saudi-arabia/) ([read online](https://codeatoms.ai/passenger-rail-fleet-saudi-arabia/)) | Rail and transportation | Saudi Arabia | DOI pending |
| [Sovereign AI Architecture for a Freight Corridor and Customs Clearance in Saudi Arabia](freight-corridor-customs-saudi-arabia/) ([read online](https://codeatoms.ai/freight-corridor-customs-saudi-arabia/)) | Supply chain and logistics | Saudi Arabia | DOI pending |
| [Sovereign AI Architecture for Distribution Loss and Theft Reduction in Pakistan](distribution-loss-theft-pakistan/) ([read online](https://codeatoms.ai/distribution-loss-theft-pakistan/)) | Energy and utilities | Pakistan | DOI pending |
| [Physical AI System Design for Composite Part Inspection in an Aviation MRO in Saudi Arabia](composite-part-inspection-mro-saudi-arabia/) ([read online](https://codeatoms.ai/composite-part-inspection-mro-saudi-arabia/)) | Aviation and aerospace manufacturing | Saudi Arabia | DOI pending |
| [A Self-Improving AI System for OT Vulnerability Management at a Utility in the United States](ot-vulnerability-utility-us/) ([read online](https://codeatoms.ai/ot-vulnerability-utility-us/)) | Energy and utilities | United States | DOI pending |
| [Industrial AI Reference Architecture for Tailings Storage Facility Monitoring in the United States](tailings-monitoring-us/) ([read online](https://codeatoms.ai/tailings-monitoring-us/)) | Mining | United States | DOI pending |
| [Industrial AI Reference Architecture for an Engine MRO Shop Floor in the United States](engine-mro-shop-us/) ([read online](https://codeatoms.ai/engine-mro-shop-us/)) | Aviation and aerospace manufacturing | United States | DOI pending |
| [Industrial AI Reference Architecture for Fertilizer Plant Reliability in Pakistan](fertilizer-plant-reliability-pakistan/) ([read online](https://codeatoms.ai/fertilizer-plant-reliability-pakistan/)) | Heavy industry and construction | Pakistan | DOI pending |
| [Physical AI System Design for a Mobile Robot Fulfilment Centre in Saudi Arabia](mobile-robot-fulfilment-centre-saudi-arabia/) ([read online](https://codeatoms.ai/mobile-robot-fulfilment-centre-saudi-arabia/)) | Warehousing and intralogistics | Saudi Arabia | DOI pending |
| [Sovereign AI Reference Architectures for a Remote Mine on a Satellite Link in Pakistan](remote-mine-satellite-pakistan/) ([read online](https://codeatoms.ai/remote-mine-satellite-pakistan/)) | Mining | Pakistan | DOI pending |
| [A Self-Improving AI System for Carrier Exception Handling in the United States](carrier-exceptions-us/) ([read online](https://codeatoms.ai/carrier-exceptions-us/)) | Supply chain and logistics | United States | DOI pending |
| [A Self-Improving AI System for Canal Irrigation Water Allocation in Pakistan](canal-irrigation-pakistan/) ([read online](https://codeatoms.ai/canal-irrigation-pakistan/)) | Agriculture and earth observation | Pakistan | DOI pending |
| [Physical AI System Design for Weld and Assembly Quality in a Vehicle Plant in Pakistan](weld-assembly-quality-vehicle-plant-pakistan/) ([read online](https://codeatoms.ai/weld-assembly-quality-vehicle-plant-pakistan/)) | Discrete manufacturing and automotive | Pakistan | DOI pending |

## Methods

| Paper | DOI |
|---|---|
| [How Praxis Designs Physical AI Systems](https://codeatoms.ai/praxis-method/) | [10.5281/zenodo.23132102](https://doi.org/10.5281/zenodo.23132102) |
| [From Reference Architecture to Living Ontology](https://codeatoms.ai/ontology-method/) | [10.5281/zenodo.23132104](https://doi.org/10.5281/zenodo.23132104) |

## For agents and developers

- [`mcp-server/`](mcp-server/): an MCP server that gives coding agents every design (`list_designs`, `get_design`, `read_paper`, `find`).
- [`hyper-ontology-py/`](hyper-ontology-py/): load, validate and convert any `ontology/objects.json` (Mermaid, Cypher, JSON-LD); format in [ONTOLOGY_PACKAGE.md](ONTOLOGY_PACKAGE.md).
- [`llms.txt`](https://codeatoms.ai/llms.txt) and the [dataset](https://huggingface.co/datasets/CodeNinjatools/vertical-driven-architectures).

## Licence

Text, figures and data: [CC BY 4.0](LICENSE). Cite the DOI or the paper URL.

## About CodeNinja

CodeNinja is a Middle Eastern American artificial intelligence lab focused on building self-improving systems. We are reinventing knowledge work to close the loop between vertical AI use cases and the generalized intelligence that fuels it, accelerating the path toward organizational superintelligence.
