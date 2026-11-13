# Industrial AI

Canonical: https://codeatoms.ai/industrial-ai/
License: CC BY 4.0
Publisher: CodeNinja Atoms (https://codeatoms.ai)

Industrial AI is AI put to work inside industrial operations: plants, grids, mines, pipelines, rail, ports and factories. It reads the operation's own systems of record and sensors, joins them in one object model, reasons over that model with open-weight models running on the operator's hardware, and puts each decision in front of the person who owns it. CodeNinja Atoms has published 44 industrial AI designs, one per real operation, across 12 sectors in the United States (19), Saudi Arabia (13), Pakistan (11), Germany (1), with 643 typed objects between them.

## Industrial AI use cases by sector

| Sector | Countries | Industrial AI use cases |
|---|---|---|
| Energy and utilities | Pakistan, Saudi Arabia, United States | [A Self-Improving AI System for OT Vulnerability Management at a Utility in the United States](https://codeatoms.ai/ot-vulnerability-utility-us/), [Sovereign AI Architecture for Distribution Loss and Theft Reduction in Pakistan](https://codeatoms.ai/distribution-loss-theft-pakistan/), [Industrial Data Ontology for a Water Utility in the United States](https://codeatoms.ai/water-utility-ontology-us/), [Sovereign AI Architecture for a Grid Control Room in Saudi Arabia](https://codeatoms.ai/grid-control-room-saudi-arabia/), [Turbine Island Watch](https://codeatoms.ai/steam-turbine-condition-monitoring-pakistan/), [Reliability Atlas](https://codeatoms.ai/plant-reliability-assessment-saudi-arabia/), [Grid Context Watch](https://codeatoms.ai/ot-security-cip-evidence-us/), [Feeder Firewatch](https://codeatoms.ai/wildfire-risk-distribution-us/) |
| Heavy industry and construction | Pakistan, Saudi Arabia | [Industrial AI Reference Architecture for Fertilizer Plant Reliability in Pakistan](https://codeatoms.ai/fertilizer-plant-reliability-pakistan/), [A Self-Improving AI System for Cement Kiln Control in Saudi Arabia](https://codeatoms.ai/cement-kiln-control-saudi-arabia/), [Structure Phase Watch](https://codeatoms.ai/structure-phase-construction-saudi-arabia/), [Steel Count Ledger](https://codeatoms.ai/steel-production-count-pakistan/), [Factory Fire Watch](https://codeatoms.ai/factory-fire-monitoring-saudi-arabia/) |
| Agriculture and earth observation | Pakistan, Saudi Arabia, United States | [A Self-Improving AI System for Canal Irrigation Water Allocation in Pakistan](https://codeatoms.ai/canal-irrigation-pakistan/), [Baseline](https://codeatoms.ai/vegetation-mapping-lidar-us/), [Fodder Watch](https://codeatoms.ai/restricted-crop-monitoring-saudi-arabia/), [Field Ledger](https://codeatoms.ai/farm-data-dashboard-pakistan/) |
| Maritime and ports | Germany, Saudi Arabia, United States | [Industrial Ontology Examples](https://codeatoms.ai/port-equipment-berth-ontology-saudi-arabia/), [Port Drone Watch](https://codeatoms.ai/drone-detection-dispatch-port-germany/), [Port Twin](https://codeatoms.ai/port-digital-twin-us/), [Terminal Pulse](https://codeatoms.ai/truck-turn-container-terminal-us/) |
| Oil and gas | Pakistan, United States | [Pipeline Integrity Watch](https://codeatoms.ai/pipeline-integrity-gas-transmission-us/), [Corridor Guard](https://codeatoms.ai/dc-interference-gas-pipelines-pakistan/), [Loop Integrity Watch](https://codeatoms.ai/tank-gauge-integrity-pakistan/), [Sovereign HSE Watch](https://codeatoms.ai/sovereign-hse-pakistan/) |
| Aviation and aerospace manufacturing | Saudi Arabia, United States | [Industrial AI Reference Architecture for an Engine MRO Shop Floor in the United States](https://codeatoms.ai/engine-mro-shop-us/), [Physical AI System Design for Composite Part Inspection in an Aviation MRO in Saudi Arabia](https://codeatoms.ai/composite-part-inspection-mro-saudi-arabia/), [Hangar Form Cell](https://codeatoms.ai/dieless-sheet-metal-cell-aerospace-mro-us/) |
| Discrete manufacturing and automotive | Pakistan, United States | [Physical AI System Design for Weld and Assembly Quality in a Vehicle Plant in Pakistan](https://codeatoms.ai/weld-assembly-quality-vehicle-plant-pakistan/), [Depot Operating Object Model](https://codeatoms.ai/factory-ontology-rebuild-depot-us/), [Pit Camera Watch](https://codeatoms.ai/test-site-camera-monitoring-us/) |
| Mining | Pakistan, Saudi Arabia, United States | [Industrial AI Reference Architecture for Tailings Storage Facility Monitoring in the United States](https://codeatoms.ai/tailings-monitoring-us/), [Sovereign AI Reference Architectures for a Remote Mine on a Satellite Link in Pakistan](https://codeatoms.ai/remote-mine-satellite-pakistan/), [Industrial AI for an Open Pit Mine Haul Fleet in Saudi Arabia](https://codeatoms.ai/open-pit-mine-haul-fleet-saudi-arabia/) |
| Rail and transportation | Saudi Arabia, United States | [Sovereign AI Reference Architectures for Passenger Rail Fleet Maintenance in Saudi Arabia](https://codeatoms.ai/passenger-rail-fleet-saudi-arabia/), [Wayside Trend Watch](https://codeatoms.ai/wayside-detector-trending-rail-us/), [Consist Watch](https://codeatoms.ai/rail-fleet-condition-monitoring-us/) |
| Supply chain and logistics | Saudi Arabia, United States | [Sovereign AI Architecture for a Freight Corridor and Customs Clearance in Saudi Arabia](https://codeatoms.ai/freight-corridor-customs-saudi-arabia/), [Industrial Data Ontology for a Cold Chain From Plant to Store in the United States](https://codeatoms.ai/cold-chain-ontology-us/), [A Self-Improving AI System for Carrier Exception Handling in the United States](https://codeatoms.ai/carrier-exceptions-us/) |
| Semiconductors | Saudi Arabia, United States | [Physical AI System Design for Wafer Defect Inspection in the United States](https://codeatoms.ai/wafer-defect-inspection-us/), [Silicon Ledger](https://codeatoms.ai/chip-design-ontology-saudi-arabia/) |
| Warehousing and intralogistics | Saudi Arabia, United States | [Physical AI System Design for a Mobile Robot Fulfilment Centre in Saudi Arabia](https://codeatoms.ai/mobile-robot-fulfilment-centre-saudi-arabia/), [Warehouse Twin Command](https://codeatoms.ai/warehouse-digital-twin-us/) |

## The architecture of industrial AI

Every published design follows the same seven layers, bottom up. Across the 44 designs the object model layer holds 643 objects and 560 typed links, the inference layer names 127 open-weight model choices, and 44 of 44 designs name the person who approves each action. The sovereign boundary is what makes it sovereign: every layer runs on hardware the operator owns or controls, in its own country, with no third-party AI service in the serving path.

| Layer | What it holds |
|---|---|
| 1. Sources | the systems of record the operation already runs, read only; they stay the system of record |
| 2. Sensing | cameras, detectors and instruments, existing or added, sized from the streams they produce |
| 3. Adapters | one family per kind of source, owning its contract, retries and ordering; the only way data enters |
| 4. Object model | the operation as typed objects, properties and links (an ontology), held on infrastructure the operator controls |
| 5. Inference | open-weight models only, placed at the edge, the site or one in-country node by latency and link loss |
| 6. Services | what the design computes over the object model: forecasts, detections, joins, evidence |
| 7. Surfaces | where people see the result and a named person decides; actions are written one way into the owning system |

- [Industrial AI reference architecture](https://codeatoms.ai/industrial-ai-reference-architecture/): every design by sector
- [Industrial data ontology](https://codeatoms.ai/industrial-data-ontology/): the data model
