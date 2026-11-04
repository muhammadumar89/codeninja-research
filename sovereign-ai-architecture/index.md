# Sovereign AI architecture

Canonical: https://codeatoms.ai/sovereign-ai-architecture/
License: CC BY 4.0
Publisher: CodeNinja Atoms (https://codeatoms.ai)

A sovereign AI architecture is a way of building AI so that the models, the data and the compute all stay under the control of the operator that runs them: open weights models, self hosted in the operator's own country, on hardware it owns or controls, with no third party AI service anywhere in the serving path. It is built in seven layers, from the systems of record at the bottom to the screens where a named person decides at the top. CodeNinja Atoms has published 28 worked designs in this architecture, across 11 sectors in the United States (14), Saudi Arabia (7), Pakistan (6), Germany (1).

## The seven layers of a sovereign AI architecture

| Layer | What it does | Held by | In the published designs |
|---|---|---|---|
| 1. Sources | The databases and control systems the operation already runs. The architecture reads them and never replaces them. | the operator, unchanged | all 28 designs |
| 2. Sensing | Cameras, detectors and instruments, the ones in place plus any the design adds, sized from the data they send. | the operator, at its sites | all 28 designs |
| 3. Adapters | One adapter per kind of source. Each owns its contract, its retries and its ordering, and is the only door data comes in by. | the operator, in its country | all 28 designs |
| 4. Object model | The operation held as typed objects, properties and links: the ontology every model and person works from. | the operator, on its own infrastructure | 397 objects and 360 typed links across 28 designs |
| 5. Inference | Open weights models only, placed at the edge, at the site or on one node in the country, by latency and by what happens when the link drops. | the operator, self hosted | 70 open weights model choices |
| 6. Services | What the architecture computes over the object model: forecasts, detections, joins and the evidence behind each. | the operator, in its country | all 28 designs |
| 7. Surfaces | Where people read the result and a named person decides. Approved actions are written one way back into the system that owns them. | a named person at the operator | 28 of 28 designs name the person who approves |

## Sovereign AI architecture patterns

| Pattern | Hardware | Designs | Which |
|---|---|---|---|
| Frontier reasoning node | Eight 141 GB GPUs run a frontier open weights model at FP8, on a node the operator owns or one hosted in its country. | 15 | [Physical AI System Design for Wafer Defect Inspection in the United States](https://codeatoms.ai/wafer-defect-inspection-us/), [Industrial AI for an Open Pit Mine Haul Fleet in Saudi Arabia](https://codeatoms.ai/open-pit-mine-haul-fleet-saudi-arabia/), [Sovereign AI Architecture for a Grid Control Room in Saudi Arabia](https://codeatoms.ai/grid-control-room-saudi-arabia/), [Silicon Ledger](https://codeatoms.ai/chip-design-ontology-saudi-arabia/), [Wayside Trend Watch](https://codeatoms.ai/wayside-detector-trending-rail-us/), [Warehouse Twin Command](https://codeatoms.ai/warehouse-digital-twin-us/), [Pipeline Integrity Watch](https://codeatoms.ai/pipeline-integrity-gas-transmission-us/), [Port Drone Watch](https://codeatoms.ai/drone-detection-dispatch-port-germany/), [Consist Watch](https://codeatoms.ai/rail-fleet-condition-monitoring-us/), [Grid Context Watch](https://codeatoms.ai/ot-security-cip-evidence-us/), [Structure Phase Watch](https://codeatoms.ai/structure-phase-construction-saudi-arabia/), [Steel Count Ledger](https://codeatoms.ai/steel-production-count-pakistan/), [Feeder Firewatch](https://codeatoms.ai/wildfire-risk-distribution-us/), [Terminal Pulse](https://codeatoms.ai/truck-turn-container-terminal-us/), [Sovereign HSE Watch](https://codeatoms.ai/sovereign-hse-pakistan/) |
| One inference card | One 48 GB inference card, up to one server of eight, at the site or in the country. No frontier model is needed. | 7 | [Industrial Data Ontology for a Water Utility in the United States](https://codeatoms.ai/water-utility-ontology-us/), [Depot Operating Object Model](https://codeatoms.ai/factory-ontology-rebuild-depot-us/), [Turbine Island Watch](https://codeatoms.ai/steam-turbine-condition-monitoring-pakistan/), [Hangar Form Cell](https://codeatoms.ai/dieless-sheet-metal-cell-aerospace-mro-us/), [Corridor Guard](https://codeatoms.ai/dc-interference-gas-pipelines-pakistan/), [Pit Camera Watch](https://codeatoms.ai/test-site-camera-monitoring-us/), [Fodder Watch](https://codeatoms.ai/restricted-crop-monitoring-saudi-arabia/) |
| No new compute | The design runs on servers and software the operator already has. Nothing new is bought. | 6 | [Baseline](https://codeatoms.ai/vegetation-mapping-lidar-us/), [Field Ledger](https://codeatoms.ai/farm-data-dashboard-pakistan/), [Loop Integrity Watch](https://codeatoms.ai/tank-gauge-integrity-pakistan/), [Reliability Atlas](https://codeatoms.ai/plant-reliability-assessment-saudi-arabia/), [Port Twin](https://codeatoms.ai/port-digital-twin-us/), [Factory Fire Watch](https://codeatoms.ai/factory-fire-monitoring-saudi-arabia/) |

## What makes an AI architecture sovereign

- **Open weights only.** Every model in every one of the 28 designs is open weights, with its licence named. No closed model serves a request.
- **In country.** Inference, the object model and the data stay in the operator's country, on hardware it owns or controls.
- **Read, never replace.** The architecture reads the systems the operation already runs and writes back only what a named person approved.

## Worked designs in a sovereign AI architecture

| Design | Sector | Country | Pattern | DOI |
|---|---|---|---|---|
| [Industrial Data Ontology for a Water Utility in the United States](https://codeatoms.ai/water-utility-ontology-us/) | energy and utilities | United States | One inference card | 10.5281/zenodo.23889772 |
| [Physical AI System Design for Wafer Defect Inspection in the United States](https://codeatoms.ai/wafer-defect-inspection-us/) | semiconductors | United States | Frontier reasoning node | 10.5281/zenodo.23889770 |
| [Industrial AI for an Open Pit Mine Haul Fleet in Saudi Arabia](https://codeatoms.ai/open-pit-mine-haul-fleet-saudi-arabia/) | mining | Saudi Arabia | Frontier reasoning node | 10.5281/zenodo.23889774 |
| [Sovereign AI Architecture for a Grid Control Room in Saudi Arabia](https://codeatoms.ai/grid-control-room-saudi-arabia/) | energy and utilities | Saudi Arabia | Frontier reasoning node | 10.5281/zenodo.23889768 |
| [Silicon Ledger](https://codeatoms.ai/chip-design-ontology-saudi-arabia/) | semiconductors | Saudi Arabia | Frontier reasoning node | 10.5281/zenodo.23693146 |
| [Wayside Trend Watch](https://codeatoms.ai/wayside-detector-trending-rail-us/) | rail and transportation | United States | Frontier reasoning node | 10.5281/zenodo.23556421 |
| [Warehouse Twin Command](https://codeatoms.ai/warehouse-digital-twin-us/) | warehousing and intralogistics | United States | Frontier reasoning node | 10.5281/zenodo.23556416 |
| [Pipeline Integrity Watch](https://codeatoms.ai/pipeline-integrity-gas-transmission-us/) | oil and gas | United States | Frontier reasoning node | 10.5281/zenodo.23556374 |
| [Depot Operating Object Model](https://codeatoms.ai/factory-ontology-rebuild-depot-us/) | discrete manufacturing and automotive | United States | One inference card | 10.5281/zenodo.23570177 |
| [Port Drone Watch](https://codeatoms.ai/drone-detection-dispatch-port-germany/) | maritime and ports | Germany | Frontier reasoning node | 10.5281/zenodo.23635729 |
| [Turbine Island Watch](https://codeatoms.ai/steam-turbine-condition-monitoring-pakistan/) | energy and utilities | Pakistan | One inference card | 10.5281/zenodo.23365092 |
| [Consist Watch](https://codeatoms.ai/rail-fleet-condition-monitoring-us/) | rail and transportation | United States | Frontier reasoning node | 10.5281/zenodo.23365118 |
| [Hangar Form Cell](https://codeatoms.ai/dieless-sheet-metal-cell-aerospace-mro-us/) | aviation and aerospace manufacturing | United States | One inference card | 10.5281/zenodo.23308095 |
| [Corridor Guard](https://codeatoms.ai/dc-interference-gas-pipelines-pakistan/) | oil and gas | Pakistan | One inference card | 10.5281/zenodo.23308093 |
| [Pit Camera Watch](https://codeatoms.ai/test-site-camera-monitoring-us/) | discrete manufacturing and automotive | United States | One inference card | 10.5281/zenodo.23296077 |
| [Baseline](https://codeatoms.ai/vegetation-mapping-lidar-us/) | agriculture and earth observation | United States | No new compute | 10.5281/zenodo.23186673 |
| [Fodder Watch](https://codeatoms.ai/restricted-crop-monitoring-saudi-arabia/) | agriculture and earth observation | Saudi Arabia | One inference card | 10.5281/zenodo.23186675 |
| [Field Ledger](https://codeatoms.ai/farm-data-dashboard-pakistan/) | agriculture and earth observation | Pakistan | No new compute | 10.5281/zenodo.23186671 |
| [Loop Integrity Watch](https://codeatoms.ai/tank-gauge-integrity-pakistan/) | oil and gas | Pakistan | No new compute | 10.5281/zenodo.23157967 |
| [Reliability Atlas](https://codeatoms.ai/plant-reliability-assessment-saudi-arabia/) | energy and utilities | Saudi Arabia | No new compute | 10.5281/zenodo.23157965 |
| [Grid Context Watch](https://codeatoms.ai/ot-security-cip-evidence-us/) | energy and utilities | United States | Frontier reasoning node | 10.5281/zenodo.23157957 |
| [Structure Phase Watch](https://codeatoms.ai/structure-phase-construction-saudi-arabia/) | heavy industry and construction | Saudi Arabia | Frontier reasoning node | 10.5281/zenodo.23126448 |
| [Steel Count Ledger](https://codeatoms.ai/steel-production-count-pakistan/) | heavy industry and construction | Pakistan | Frontier reasoning node | 10.5281/zenodo.23126563 |
| [Port Twin](https://codeatoms.ai/port-digital-twin-us/) | maritime and ports | United States | No new compute | 10.5281/zenodo.23126431 |
| [Factory Fire Watch](https://codeatoms.ai/factory-fire-monitoring-saudi-arabia/) | heavy industry and construction | Saudi Arabia | No new compute | 10.5281/zenodo.23126565 |
| [Feeder Firewatch](https://codeatoms.ai/wildfire-risk-distribution-us/) | energy and utilities | United States | Frontier reasoning node | 10.5281/zenodo.23159328 |
| [Terminal Pulse](https://codeatoms.ai/truck-turn-container-terminal-us/) | maritime and ports | United States | Frontier reasoning node | 10.5281/zenodo.23159331 |
| [Sovereign HSE Watch](https://codeatoms.ai/sovereign-hse-pakistan/) | oil and gas | Pakistan | Frontier reasoning node | 10.5281/zenodo.23119714 |

See also: [sovereign AI reference architectures](https://codeatoms.ai/sovereign-ai-reference-architectures/), [industrial ontology examples](https://codeatoms.ai/industrial-ontology-examples/), [industrial AI reference architecture](https://codeatoms.ai/industrial-ai-reference-architecture/), [physical AI system design](https://codeatoms.ai/physical-ai-system-design/), [self-improving AI system](https://codeatoms.ai/self-improving-ai-system/), [industrial data ontology](https://codeatoms.ai/industrial-data-ontology/).
