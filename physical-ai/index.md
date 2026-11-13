# Physical AI

Canonical: https://codeatoms.ai/physical-ai/
License: CC BY 4.0
Publisher: CodeNinja Atoms (https://codeatoms.ai)

Physical AI is AI that senses the physical world, reasons about it and acts in it. Cameras, instruments and machines feed it; a typed model of the operation (an ontology) holds what it knows; open-weight models reason over that model; and a named person approves every action that changes the physical world. Where generative AI works on text, physical AI works on plants, fleets, grids, ports, mines and fields. CodeNinja Atoms has published 44 open physical AI designs for real operations across 12 sectors in the United States (19), Saudi Arabia (13), Pakistan (11), Germany (1), each free to reuse under CC BY 4.0.

## What physical AI does, sector by sector

| Sector | Countries | Designs |
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

## How a physical AI system is designed

- [Physical AI system design](https://codeatoms.ai/physical-ai-system-design/): the method and the six decisions
- [Sovereign AI reference architectures](https://codeatoms.ai/sovereign-ai-reference-architectures/): every design with compute and cost
- [Industrial ontology examples](https://codeatoms.ai/industrial-ontology-examples/): the object models

## Where physical AI runs

| Pattern | What runs where | Designs |
|---|---|---|
| Frontier reasoning node | eight 141 GB HBM-class GPUs holding an open-weight frontier model at FP8, owned or hosted in the country | 28 |
| One inference card | 48 GB PCIe inference cards, from one card to one eight-card server, at the site or in the country; no frontier model | 7 |
| No new compute | the design runs on servers or software the operator already owns; nothing to buy | 9 |
