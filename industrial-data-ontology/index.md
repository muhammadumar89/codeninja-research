# Industrial data ontology

Canonical: https://codeatoms.ai/industrial-data-ontology/
License: CC BY 4.0
Publisher: CodeNinja Atoms (https://codeatoms.ai)

An industrial data ontology is a typed model of the data an industrial operation already holds: each asset, record, event, site and person becomes an object with properties and status values, anchored in the system of record that holds its data, and joined to the others by typed links. CodeNinja Atoms has published 44 industrial data ontologies, one per real operation across 12 sectors in the United States (19), Saudi Arabia (13), Pakistan (11), Germany (1): 643 objects, 2177 properties and 560 links, 556 of the 643 objects anchored in a named source system. Each is hyper-ontology/1 JSON under CC BY 4.0.

All 643 objects as one table: objects.jsonl in https://huggingface.co/datasets/CodeNinjatools/vertical-driven-architectures · format: https://codeatoms.ai/developer/reference/hyper-ontology-1/

## What an industrial data ontology holds

| Kind | Objects | What it is | Examples from the published models |
|---|---|---|---|
| record | 180 | what the operation writes down: work orders, tickets, findings, calibrations | Disposition, Incident/Accident Record, Work order |
| asset | 155 | equipment and other physical things the operation owns and maintains | Formed structural part, Commuter car, Operating Facility / Site |
| event | 90 | something that happens at a time: an alarm, a fault, a mission | Flight Mission, Condition Anomaly Alert, Active fault |
| actor | 47 | a role that acts on the operation: a desk, a crew, an officer | Control room operator, Mechanical desk controller, Customer |
| site | 46 | a place the operation runs: a station, a field, a centre | Compressor Station, Distribution Center, Farm holding |
| measure | 38 | a reading, sample or score taken from the operation | Monitored point, Detector Reading, Criticality index |
| document | 35 | a report, letter or dataset the operation keeps | QA/QC Accuracy Report, Shift log entry, Agent draft |
| person | 20 | a named job a person holds: the one who reads, decides or approves | Shift Lead, Instrumentation Technician, Worker |
| system | 16 | a software or control system the model names as an object in its own right | HVDC Transmission System, Edge Gateway, Data Source Connection |
| material | 15 | stock that moves through the operation: parts, wafers, containers | Consignment, Spare part, Wafer |
| vocabulary | 1 |  | Exception type |

## The parts of an industrial data ontology

| Part | What it is | In the published models |
|---|---|---|
| Object | one thing the operation tracks, with a kind | 643 objects across 44 models |
| Properties | what the operation records about the object | 2177 properties |
| Anchor | the system of record that already holds the object's data; the ontology reads it and never replaces it | 556 of 643 objects name one |
| Status vocabulary | the fixed values the object's state can take | 161 of 643 objects carry one |
| Typed links | typed relations to other objects in the same model | 560 links, 536 of them named |

## Every published industrial data ontology

| Design | Sector | Country | Objects | Links | Anchored | JSON | DOI |
|---|---|---|---|---|---|---|---|
| [Physical AI System Design for Weld and Assembly Quality in a Vehicle Plant in Pakistan](https://codeatoms.ai/weld-assembly-quality-vehicle-plant-pakistan/) | discrete manufacturing and automotive | Pakistan | 16 | 12 | 14 of 16 | https://codeatoms.ai/weld-assembly-quality-vehicle-plant-pakistan/ontology/objects.json |  |
| [Industrial AI Reference Architecture for Tailings Storage Facility Monitoring in the United States](https://codeatoms.ai/tailings-monitoring-us/) | mining | United States | 15 | 12 | 14 of 15 | https://codeatoms.ai/tailings-monitoring-us/ontology/objects.json |  |
| [Sovereign AI Reference Architectures for a Remote Mine on a Satellite Link in Pakistan](https://codeatoms.ai/remote-mine-satellite-pakistan/) | mining | Pakistan | 15 | 13 | 15 of 15 | https://codeatoms.ai/remote-mine-satellite-pakistan/ontology/objects.json |  |
| [Industrial Ontology Examples](https://codeatoms.ai/port-equipment-berth-ontology-saudi-arabia/) | maritime and ports | Saudi Arabia | 16 | 13 | 16 of 16 | https://codeatoms.ai/port-equipment-berth-ontology-saudi-arabia/ontology/objects.json |  |
| [Sovereign AI Reference Architectures for Passenger Rail Fleet Maintenance in Saudi Arabia](https://codeatoms.ai/passenger-rail-fleet-saudi-arabia/) | rail and transportation | Saudi Arabia | 14 | 12 | 14 of 14 | https://codeatoms.ai/passenger-rail-fleet-saudi-arabia/ontology/objects.json |  |
| [A Self-Improving AI System for OT Vulnerability Management at a Utility in the United States](https://codeatoms.ai/ot-vulnerability-utility-us/) | energy and utilities | United States | 16 | 13 | 16 of 16 | https://codeatoms.ai/ot-vulnerability-utility-us/ontology/objects.json |  |
| [Physical AI System Design for a Mobile Robot Fulfilment Centre in Saudi Arabia](https://codeatoms.ai/mobile-robot-fulfilment-centre-saudi-arabia/) | warehousing and intralogistics | Saudi Arabia | 15 | 13 | 15 of 15 | https://codeatoms.ai/mobile-robot-fulfilment-centre-saudi-arabia/ontology/objects.json |  |
| [Sovereign AI Architecture for a Freight Corridor and Customs Clearance in Saudi Arabia](https://codeatoms.ai/freight-corridor-customs-saudi-arabia/) | supply chain and logistics | Saudi Arabia | 15 | 11 | 12 of 15 | https://codeatoms.ai/freight-corridor-customs-saudi-arabia/ontology/objects.json |  |
| [Industrial AI Reference Architecture for Fertilizer Plant Reliability in Pakistan](https://codeatoms.ai/fertilizer-plant-reliability-pakistan/) | heavy industry and construction | Pakistan | 14 | 10 | 14 of 14 | https://codeatoms.ai/fertilizer-plant-reliability-pakistan/ontology/objects.json |  |
| [Industrial AI Reference Architecture for an Engine MRO Shop Floor in the United States](https://codeatoms.ai/engine-mro-shop-us/) | aviation and aerospace manufacturing | United States | 15 | 16 | 15 of 15 | https://codeatoms.ai/engine-mro-shop-us/ontology/objects.json |  |
| [Sovereign AI Architecture for Distribution Loss and Theft Reduction in Pakistan](https://codeatoms.ai/distribution-loss-theft-pakistan/) | energy and utilities | Pakistan | 15 | 14 | 13 of 15 | https://codeatoms.ai/distribution-loss-theft-pakistan/ontology/objects.json |  |
| [Physical AI System Design for Composite Part Inspection in an Aviation MRO in Saudi Arabia](https://codeatoms.ai/composite-part-inspection-mro-saudi-arabia/) | aviation and aerospace manufacturing | Saudi Arabia | 16 | 12 | 12 of 16 | https://codeatoms.ai/composite-part-inspection-mro-saudi-arabia/ontology/objects.json |  |
| [Industrial Data Ontology for a Cold Chain From Plant to Store in the United States](https://codeatoms.ai/cold-chain-ontology-us/) | supply chain and logistics | United States | 16 | 13 | 15 of 16 | https://codeatoms.ai/cold-chain-ontology-us/ontology/objects.json |  |
| [A Self-Improving AI System for Cement Kiln Control in Saudi Arabia](https://codeatoms.ai/cement-kiln-control-saudi-arabia/) | heavy industry and construction | Saudi Arabia | 16 | 10 | 13 of 16 | https://codeatoms.ai/cement-kiln-control-saudi-arabia/ontology/objects.json |  |
| [A Self-Improving AI System for Carrier Exception Handling in the United States](https://codeatoms.ai/carrier-exceptions-us/) | supply chain and logistics | United States | 16 | 13 | 16 of 16 | https://codeatoms.ai/carrier-exceptions-us/ontology/objects.json |  |
| [A Self-Improving AI System for Canal Irrigation Water Allocation in Pakistan](https://codeatoms.ai/canal-irrigation-pakistan/) | agriculture and earth observation | Pakistan | 16 | 13 | 14 of 16 | https://codeatoms.ai/canal-irrigation-pakistan/ontology/objects.json |  |
| [Industrial Data Ontology for a Water Utility in the United States](https://codeatoms.ai/water-utility-ontology-us/) | energy and utilities | United States | 16 | 14 | 16 of 16 | https://codeatoms.ai/water-utility-ontology-us/ontology/objects.json | 10.5281/zenodo.23889772 |
| [Physical AI System Design for Wafer Defect Inspection in the United States](https://codeatoms.ai/wafer-defect-inspection-us/) | semiconductors | United States | 16 | 12 | 13 of 16 | https://codeatoms.ai/wafer-defect-inspection-us/ontology/objects.json | 10.5281/zenodo.23889770 |
| [Industrial AI for an Open Pit Mine Haul Fleet in Saudi Arabia](https://codeatoms.ai/open-pit-mine-haul-fleet-saudi-arabia/) | mining | Saudi Arabia | 16 | 13 | 12 of 16 | https://codeatoms.ai/open-pit-mine-haul-fleet-saudi-arabia/ontology/objects.json | 10.5281/zenodo.23889774 |
| [Sovereign AI Architecture for a Grid Control Room in Saudi Arabia](https://codeatoms.ai/grid-control-room-saudi-arabia/) | energy and utilities | Saudi Arabia | 16 | 13 | 14 of 16 | https://codeatoms.ai/grid-control-room-saudi-arabia/ontology/objects.json | 10.5281/zenodo.23889768 |
| [Silicon Ledger](https://codeatoms.ai/chip-design-ontology-saudi-arabia/) | semiconductors | Saudi Arabia | 16 | 13 | 13 of 16 | https://codeatoms.ai/chip-design-ontology-saudi-arabia/ontology/objects.json | 10.5281/zenodo.23693146 |
| [Wayside Trend Watch](https://codeatoms.ai/wayside-detector-trending-rail-us/) | rail and transportation | United States | 14 | 13 | 13 of 14 | https://codeatoms.ai/wayside-detector-trending-rail-us/ontology/objects.json | 10.5281/zenodo.23556421 |
| [Warehouse Twin Command](https://codeatoms.ai/warehouse-digital-twin-us/) | warehousing and intralogistics | United States | 14 | 14 | 10 of 14 | https://codeatoms.ai/warehouse-digital-twin-us/ontology/objects.json | 10.5281/zenodo.23556416 |
| [Pipeline Integrity Watch](https://codeatoms.ai/pipeline-integrity-gas-transmission-us/) | oil and gas | United States | 14 | 13 | 4 of 14 | https://codeatoms.ai/pipeline-integrity-gas-transmission-us/ontology/objects.json | 10.5281/zenodo.23556374 |
| [Depot Operating Object Model](https://codeatoms.ai/factory-ontology-rebuild-depot-us/) | discrete manufacturing and automotive | United States | 14 | 13 | 14 of 14 | https://codeatoms.ai/factory-ontology-rebuild-depot-us/ontology/objects.json | 10.5281/zenodo.23570177 |
| [Port Drone Watch](https://codeatoms.ai/drone-detection-dispatch-port-germany/) | maritime and ports | Germany | 15 | 14 | 15 of 15 | https://codeatoms.ai/drone-detection-dispatch-port-germany/ontology/objects.json | 10.5281/zenodo.23635729 |
| [Turbine Island Watch](https://codeatoms.ai/steam-turbine-condition-monitoring-pakistan/) | energy and utilities | Pakistan | 10 | 10 | 10 of 10 | https://codeatoms.ai/steam-turbine-condition-monitoring-pakistan/ontology/objects.json | 10.5281/zenodo.23365092 |
| [Consist Watch](https://codeatoms.ai/rail-fleet-condition-monitoring-us/) | rail and transportation | United States | 14 | 13 | 0 of 14 | https://codeatoms.ai/rail-fleet-condition-monitoring-us/ontology/objects.json | 10.5281/zenodo.23365118 |
| [Hangar Form Cell](https://codeatoms.ai/dieless-sheet-metal-cell-aerospace-mro-us/) | aviation and aerospace manufacturing | United States | 14 | 14 | 2 of 14 | https://codeatoms.ai/dieless-sheet-metal-cell-aerospace-mro-us/ontology/objects.json | 10.5281/zenodo.23308095 |
| [Corridor Guard](https://codeatoms.ai/dc-interference-gas-pipelines-pakistan/) | oil and gas | Pakistan | 15 | 9 | 3 of 15 | https://codeatoms.ai/dc-interference-gas-pipelines-pakistan/ontology/objects.json | 10.5281/zenodo.23308093 |
| [Pit Camera Watch](https://codeatoms.ai/test-site-camera-monitoring-us/) | discrete manufacturing and automotive | United States | 15 | 13 | 14 of 15 | https://codeatoms.ai/test-site-camera-monitoring-us/ontology/objects.json | 10.5281/zenodo.23296077 |
| [Baseline](https://codeatoms.ai/vegetation-mapping-lidar-us/) | agriculture and earth observation | United States | 16 | 14 | 16 of 16 | https://codeatoms.ai/vegetation-mapping-lidar-us/ontology/objects.json | 10.5281/zenodo.23186673 |
| [Fodder Watch](https://codeatoms.ai/restricted-crop-monitoring-saudi-arabia/) | agriculture and earth observation | Saudi Arabia | 14 | 14 | 14 of 14 | https://codeatoms.ai/restricted-crop-monitoring-saudi-arabia/ontology/objects.json | 10.5281/zenodo.23186675 |
| [Field Ledger](https://codeatoms.ai/farm-data-dashboard-pakistan/) | agriculture and earth observation | Pakistan | 12 | 12 | 12 of 12 | https://codeatoms.ai/farm-data-dashboard-pakistan/ontology/objects.json | 10.5281/zenodo.23186671 |
| [Loop Integrity Watch](https://codeatoms.ai/tank-gauge-integrity-pakistan/) | oil and gas | Pakistan | 15 | 15 | 15 of 15 | https://codeatoms.ai/tank-gauge-integrity-pakistan/ontology/objects.json | 10.5281/zenodo.23157967 |
| [Reliability Atlas](https://codeatoms.ai/plant-reliability-assessment-saudi-arabia/) | energy and utilities | Saudi Arabia | 13 | 14 | 13 of 13 | https://codeatoms.ai/plant-reliability-assessment-saudi-arabia/ontology/objects.json | 10.5281/zenodo.23157965 |
| [Grid Context Watch](https://codeatoms.ai/ot-security-cip-evidence-us/) | energy and utilities | United States | 14 | 14 | 14 of 14 | https://codeatoms.ai/ot-security-cip-evidence-us/ontology/objects.json | 10.5281/zenodo.23157957 |
| [Structure Phase Watch](https://codeatoms.ai/structure-phase-construction-saudi-arabia/) | heavy industry and construction | Saudi Arabia | 15 | 12 | 15 of 15 | https://codeatoms.ai/structure-phase-construction-saudi-arabia/ontology/objects.json | 10.5281/zenodo.23126448 |
| [Steel Count Ledger](https://codeatoms.ai/steel-production-count-pakistan/) | heavy industry and construction | Pakistan | 14 | 12 | 14 of 14 | https://codeatoms.ai/steel-production-count-pakistan/ontology/objects.json | 10.5281/zenodo.23126563 |
| [Port Twin](https://codeatoms.ai/port-digital-twin-us/) | maritime and ports | United States | 13 | 13 | 13 of 13 | https://codeatoms.ai/port-digital-twin-us/ontology/objects.json | 10.5281/zenodo.23126431 |
| [Factory Fire Watch](https://codeatoms.ai/factory-fire-monitoring-saudi-arabia/) | heavy industry and construction | Saudi Arabia | 14 | 12 | 14 of 14 | https://codeatoms.ai/factory-fire-monitoring-saudi-arabia/ontology/objects.json | 10.5281/zenodo.23126565 |
| [Feeder Firewatch](https://codeatoms.ai/wildfire-risk-distribution-us/) | energy and utilities | United States | 14 | 12 | 14 of 14 | https://codeatoms.ai/wildfire-risk-distribution-us/ontology/objects.json | 10.5281/zenodo.23159328 |
| [Terminal Pulse](https://codeatoms.ai/truck-turn-container-terminal-us/) | maritime and ports | United States | 12 | 11 | 12 of 12 | https://codeatoms.ai/truck-turn-container-terminal-us/ontology/objects.json | 10.5281/zenodo.23159331 |
| [Sovereign HSE Watch](https://codeatoms.ai/sovereign-hse-pakistan/) | oil and gas | Pakistan | 12 | 14 | 9 of 12 | https://codeatoms.ai/sovereign-hse-pakistan/ontology/objects.json | 10.5281/zenodo.23119714 |

See also: [sovereign AI reference architectures](https://codeatoms.ai/sovereign-ai-reference-architectures/), [industrial ontology examples](https://codeatoms.ai/industrial-ontology-examples/), [industrial AI reference architecture](https://codeatoms.ai/industrial-ai-reference-architecture/), [physical AI system design](https://codeatoms.ai/physical-ai-system-design/), [self-improving AI system](https://codeatoms.ai/self-improving-ai-system/).
