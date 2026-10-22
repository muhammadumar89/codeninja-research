# Industrial ontology examples

Canonical: https://codeatoms.ai/industrial-ontology-examples/
License: CC BY 4.0
Publisher: CodeNinja Atoms (https://codeatoms.ai)

An industrial ontology is a typed model of a physical operation: its assets, records, events and people as objects, each with properties, status values and named links to the others, anchored in the systems that already hold the data. Below are 21 published industrial ontology examples, 288 objects and 268 links in all, one per real operation across 9 sectors. Each downloads as hyper-ontology/1 JSON under CC BY 4.0.

## Wayside Trend Watch (rail and transportation, United States)

Design: https://codeatoms.ai/wayside-detector-trending-rail-us/ · JSON: https://codeatoms.ai/wayside-detector-trending-rail-us/ontology/objects.json

- Freight Car (asset, in Railinc Umler registry and the railroad's CMMS master data)
- Locomotive (asset, in the railroad's maintenance system (CMMS/EAM) locomotive master data)
- Axle Bearing (Roller Bearing) (asset, in the railroad's maintenance system (CMMS/EAM) master data, keyed to the serialized component)
- Wheelset (asset, in the railroad's maintenance system (CMMS/EAM) master data, keyed to the serialized component)
- Traction Motor (asset, in the railroad's maintenance system (CMMS/EAM) locomotive master data)
- Wayside Detector (asset, in wayside detector network)
- Track Segment (asset, in the railroad's track charts)
- Detector Reading (measure, in wayside detector network)
- Trend Flag (record)
- Work Order (record, in railroad maintenance system (CMMS/EAM))
- Track Geometry Exception (record, in contractor geometry reports, digitized into the pipeline)
- Rail Flaw Indication (record, in contractor rail flaw reports, digitized into the pipeline)
- AAR Interchange Record (record, in Railinc Umler and interchange services (read only))
- Train (event, in wayside detector network)

## Warehouse Twin Command (warehousing and intralogistics, United States)

Design: https://codeatoms.ai/warehouse-digital-twin-us/ · JSON: https://codeatoms.ai/warehouse-digital-twin-us/ontology/objects.json

- Distribution Center (site, in the WMS site master)
- Dock Door (asset, in the yard management spreadsheet, until the dock and yard module becomes the yard system of record)
- Yard Trailer (asset, in the yard management spreadsheet, until the dock and yard module becomes the yard system of record)
- Storage Slot (asset, in the warehouse management system)
- SKU (material, in the warehouse management system)
- Open Order (record, in the warehouse management system)
- Pick Task (record, in the warehouse management system)
- Associate (person, in the labor management system)
- Labor Shift (record, in the labor management system)
- Camera Zone (asset, in the video management system)
- Safety Event (event)
- Forklift (asset)
- Shift Lead (person)
- Slotting Recommendation (record)

## Pipeline Integrity Watch (oil and gas, United States)

Design: https://codeatoms.ai/pipeline-integrity-gas-transmission-us/ · JSON: https://codeatoms.ai/pipeline-integrity-gas-transmission-us/ontology/objects.json

- Compressor Station (site, in CMMS)
- Meter Station (site, in Historian)
- Pipeline Segment (asset)
- Compressor Unit (asset)
- OT Device (asset)
- Pipeline Controller (actor)
- Alarm (event, in Alarm and event stream)
- Leak or Abnormal Operation Event (event)
- Remote Access Session (event)
- Work Order (record, in CMMS)
- Security Directive Control (record)
- Historian (system)
- CMMS (system)
- Hazardous Area Classification (document)

## Turbine Island Watch (energy and utilities, Pakistan)

Design: https://codeatoms.ai/steam-turbine-condition-monitoring-pakistan/ · JSON: https://codeatoms.ai/steam-turbine-condition-monitoring-pakistan/ontology/objects.json

- Steam Turbine STG-1 (asset, in the DCS)
- New Steam Turbine Generator (280 MW, 20 kV hydrogen-cooled) (asset, in the DCS)
- 3500 Vibration Monitoring Rack (asset, in the DCS)
- Condition Anomaly Alert (event, in Hyper Ontology)
- Condition Work Order (record, in Document Management System)
- Instrument Calibration Record (record, in Document Management System)
- Commissioning and Performance Test Record (record, in Document Management System)
- Shift Operator (Employer's operational personnel) (actor, in the DCS)
- Warranty Engineer (Contractor, DLP) (actor, in Document Management System)
- STG-1 Availability (RTR-derived) (measure, in the DCS)

## Consist Watch (rail and transportation, United States)

Design: https://codeatoms.ai/rail-fleet-condition-monitoring-us/ · JSON: https://codeatoms.ai/rail-fleet-condition-monitoring-us/ontology/objects.json

- Commuter car (asset)
- Onboard monitoring module (asset)
- Car system router (asset)
- Digital input channel (measure)
- Analog input channel (measure)
- Active fault (event)
- Fault history record (record)
- Alert notification (record)
- Mechanical desk controller (actor)
- Yard employee (person)
- Control center mechanical desk (site)
- Yard office (site)
- Slippery rail hotspot (record)
- Notification recipient group (actor)

## Hangar Form Cell (aviation and aerospace manufacturing, United States)

Design: https://codeatoms.ai/dieless-sheet-metal-cell-aerospace-mro-us/ · JSON: https://codeatoms.ai/dieless-sheet-metal-cell-aerospace-mro-us/ontology/objects.json

- Formed structural part (asset)
- Sheet blank (asset)
- Dieless cell (asset)
- Robot arm (asset)
- Forming stylus (asset)
- Toolpath program (record)
- Part CAD model (document, in CAD import, read only)
- Formability analysis (record)
- In-process metrology scan (record)
- Force trace (record)
- Work order (record, in the production systems, read only)
- Nonconformance (record)
- Facility operator (person)
- Cell model service (system)

## Corridor Guard (oil and gas, Pakistan)

Design: https://codeatoms.ai/dc-interference-gas-pipelines-pakistan/ · JSON: https://codeatoms.ai/dc-interference-gas-pipelines-pakistan/ontology/objects.json

- 8-inch Line (asset)
- 10-inch Loop Line (asset)
- Original Anode Bed (asset)
- TEG Unit (asset)
- Anode 1 (MP-3.40) (asset)
- Anode 2 (MP-6.97) (asset)
- Insulating Joints PFIJ (asset)
- Electrode Station (asset)
- HVDC Transmission System (system, in the direct current system's configuration record, read only)
- CP Test Point (asset)
- Cathodic Protection System (system)
- Soil Investigation Report (document, in the operator's data package, read only)
- Detail of Available Data for Assessment (document, in the operator's data package, read only)
- DC Interference Assessment (record)
- Mitigation Measure (record)

## Pit Camera Watch (discrete manufacturing and automotive, United States)

Design: https://codeatoms.ai/test-site-camera-monitoring-us/ · JSON: https://codeatoms.ai/test-site-camera-monitoring-us/ontology/objects.json

- Test Site (site)
- Camera Pole (asset, in the recorder's configuration under site change control)
- Camera Head (asset, in the recorder's configuration under site change control)
- Underground Fiber Run (asset, in the recorder's configuration under site change control)
- Safety Gate (asset, in the recorder's configuration under site change control)
- Operator Booth Display (asset, in the recorder's configuration under site change control)
- Recorder Server (system, in the recorder's configuration under site change control)
- 30-Day Footage Archive (record, in the recorder's configuration under site change control)
- Incident/Accident Record (record, in the recorder's configuration under site change control)
- Booth Operator (person, in the operator's identity policy)
- Gate Officer (person, in the operator's identity policy)
- Safety Office Reviewer (person, in the operator's identity policy)
- Vehicle Under Test (asset, in the operator's test schedule)
- Test Cycle (event, in the operator's test schedule)
- Power and Fiber Assessment Package (document, in the power and fiber works assessment process, read only)

## Baseline (agriculture and earth observation, United States)

Design: https://codeatoms.ai/vegetation-mapping-lidar-us/ · JSON: https://codeatoms.ai/vegetation-mapping-lidar-us/ontology/objects.json

- Mapping Site (site, in the operator's ArcGIS Enterprise)
- Land Unit (site, in the operator's ArcGIS Enterprise)
- Watercourse (asset, in the operator's ArcGIS Enterprise)
- Dam (asset, in the operator's ArcGIS Enterprise)
- Flight Mission (event, in the survey firm's flight log)
- 4-Band Aerial Camera System (asset, in the survey firm)
- QL1 LiDAR Sensor System (asset, in the survey firm)
- GNSS/IMU Georeferencing Chain (system, in the survey firm)
- Multispectral Orthoimagery Product (record, in the operator's ArcGIS Enterprise)
- Classified LAS Point Cloud (record, in the operator's ArcGIS Enterprise)
- Bare-Earth and Highest-Hit DEMs (record, in the operator's ArcGIS Enterprise)
- QA/QC Accuracy Report (document, in the survey firm's QA)
- Professional Services Agreement (document, in the operator's contract records)
- Monthly Itemized Invoice (document, in the operator's accounts)
- Contractor Project Manager (person, in the survey firm)
- Operator Project Manager (person, in the operator's directory)

## Fodder Watch (agriculture and earth observation, Saudi Arabia)

Design: https://codeatoms.ai/restricted-crop-monitoring-saudi-arabia/ · JSON: https://codeatoms.ai/restricted-crop-monitoring-saudi-arabia/ontology/objects.json

- Farm holding (site, in the national agricultural register)
- Centre pivot / cultivated field (site, in the operator's geospatial databases)
- Farm enterprise / large farmer (actor, in the national agricultural register)
- Crop licence (wheat / seasonal fodder) (record, in the crop license records)
- Water source (well) use licence (record, in the crop license records)
- Green fodder ban control (record, in the council resolutions behind the restriction)
- Agricultural fuel / electricity service condition record (record, in fuel supplier and electricity utility coordination)
- Imagery tasking order (record, in the imagery adapter)
- Satellite image capture (event, in the mirrored Sentinel-2, Sentinel-1 and Landsat archive)
- Processed imagery product (record, in the imagery pipeline)
- Restricted-crop detection flag (event, in the screening service)
- Violation case file (record, in the enforcement channel)
- Field inspector (person, in the operator's directory)
- Restricted-crop classifier (system, in the model registry)

## Field Ledger (agriculture and earth observation, Pakistan)

Design: https://codeatoms.ai/farm-data-dashboard-pakistan/ · JSON: https://codeatoms.ai/farm-data-dashboard-pakistan/ontology/objects.json

- Farm Site (site, in the operator's farm register)
- Field (site, in the operator's farm register)
- Crop Cycle (event, in the operator's farm records)
- Sensor Device (asset, in the site sensor feeds)
- Sensor Reading (measure, in the site sensor feeds)
- Historical Dataset (document, in the big data and analytics repository (BDAR))
- Publication (document, in the big data and analytics repository (BDAR))
- Dashboard User (person, in the operator's directory)
- Access Role (record, in the dashboard's role-based access control)
- Alert (event, in the dashboard)
- Report (document, in the dashboard)
- Data Source Connection (system, in the adapter tier)

## Loop Integrity Watch (oil and gas, Pakistan)

Design: https://codeatoms.ai/tank-gauge-integrity-pakistan/ · JSON: https://codeatoms.ai/tank-gauge-integrity-pakistan/ontology/objects.json

- Fuel Tank (asset, in centralized gauging software)
- Radar Tank Gauge (RTG) (asset, in centralized gauging software)
- RTG Communication Loop (asset, in loop wiring records)
- Modbus Booster (Repeater) (asset, in the service order)
- Explosion Proof Junction Box (asset, in site hazardous-area register)
- Gauge Reading (measure, in centralized gauging software)
- Data Quality Event (event, in the integrity monitor)
- Central Inventory Picture (system, in the system of context)
- Loop Wiring As-Built (document, in loop wiring records)
- Service Order (record, in the operator's procurement record)
- Warranty and Support Record (record, in the service order)
- OEM Authorization Letter (document, in the OEM)
- HSE Work Permit (record, in the operator's HSE permit system)
- Instrumentation Technician (person, in the service provider's roster)
- Location Engineer (person, in the operator's directory)

## Reliability Atlas (energy and utilities, Saudi Arabia)

Design: https://codeatoms.ai/plant-reliability-assessment-saudi-arabia/ · JSON: https://codeatoms.ai/plant-reliability-assessment-saudi-arabia/ontology/objects.json

- Plant (site, in the operator's plant register)
- Production train (asset, in plant historian)
- Equipment (asset, in the plant CMMS)
- Failure mode (record, in the plant failure studies)
- Work order (record, in the plant CMMS)
- Downtime event (event, in plant historian)
- Availability prediction (record, in the study)
- Availability target (measure, in the contract and study targets)
- Criticality index (measure, in the study)
- RCA report (document, in plant exports and document packs)
- Major event (event, in plant exports and document packs)
- Spare part (material, in the plant CMMS)
- Reliability program (document, in plant exports and document packs)

## Grid Context Watch (energy and utilities, United States)

Design: https://codeatoms.ai/ot-security-cip-evidence-us/ · JSON: https://codeatoms.ai/ot-security-cip-evidence-us/ontology/objects.json

- Substation (site, in OT monitoring platform inventory (to be created))
- OT Asset (asset, in OT monitoring platform inventory)
- Network Sensor (asset, in the procured OT monitoring sensors)
- Anomaly Alert (event, in OT monitoring platform detection store)
- Investigation Case (record, in the system of context)
- Vulnerability Finding (record, in OT monitoring platform)
- Detection Rule (record, in OT monitoring platform)
- Threat Intelligence Item (document, in collective and sector intelligence feeds)
- Pcap Evidence Record (record, in sensor capture store)
- CIP Evidence Artefact (document, in the system of context)
- OT Security Analyst (person, in the operator's directory)
- SIEM (system, in SIEM)
- Energy management system (system, in energy management system)
- Substation data platform (system, in substation data platform export)

## Structure Phase Watch (heavy industry and construction, Saudi Arabia)

Design: https://codeatoms.ai/structure-phase-construction-saudi-arabia/ · JSON: https://codeatoms.ai/structure-phase-construction-saudi-arabia/ontology/objects.json

- Tower crane (TC-01 to TC-14) (asset, in Excel lift schedule)
- Crawler crane (6 units) (asset, in crawler crane telematics)
- Casting bed (asset, in casting bed register and QC release spreadsheet)
- Precast unit (asset, in casting bed register and QC release spreadsheet)
- Flatbed or mixer truck (asset, in haulage contractor GPS portal)
- Batch ticket (record, in batch plant SCADA)
- P6 activity (owner baseline or fragnet) (record, in Primavera P6)
- Permit to work (record, in paper permit to work system)
- Incident or observation form (record, in incident and observation forms)
- Gate movement (event, in paper gate logs)
- Delivery window (event, in Primavera P6)
- Lift schedule entry (event, in Excel lift schedule)
- Pour (event, in Primavera P6)
- Worker (person, in biometric turnstiles)
- Work zone (Zone A to D) (site, in Primavera P6)

## Steel Count Ledger (heavy industry and construction, Pakistan)

Design: https://codeatoms.ai/steel-production-count-pakistan/ · JSON: https://codeatoms.ai/steel-production-count-pakistan/ontology/objects.json

- Steel melting and re-rolling unit (site, in mill register)
- Installation point (asset, in the operator's central production record)
- Industrial PC (asset, in the operator's central production record)
- Production count event (event, in the operator's central production record)
- Product type (Billets, Ingots, Rebars, Girders) (material, in the operator's central production record)
- Declared production (record, in the mill's filings)
- Discrepancy case (record, in the operator's central production record)
- Revenue field officer (actor, in the authority's staff directory)
- Audit team (actor, in the authority's staff directory)
- Steel mill staff (person, in mill register)
- Tamper or offline alert (event, in the operator's central production record)
- Daily uptime record (measure, in the operator's central production record)
- Product calibration record (record, in the operator's central production record)
- Weighbridge record (record, in the mill's weighbridge)

## Port Twin (maritime and ports, United States)

Design: https://codeatoms.ai/port-digital-twin-us/ · JSON: https://codeatoms.ai/port-digital-twin-us/ontology/objects.json

- Berth (asset, in Port Community System)
- Navigation channel (asset, in GIS estate)
- Subsurface utility layer (asset, in GIS estate)
- Environmental sensor feed (asset, in sensor telemetry)
- Parcel / facility (asset, in GIS estate and the lease register)
- Bathymetric survey surface (record, in survey archive)
- Utility gap record (record, in the twin's own records)
- Capital project (record, in the finance backbone)
- Inspection record (record, in the inspection system)
- Vessel movement record (event, in AIS and the Port Community System)
- Truck movement record (event, in gate system)
- PCS message (event, in Port Community System)
- Engineering document (document, in document management system)

## Factory Fire Watch (heavy industry and construction, Saudi Arabia)

Design: https://codeatoms.ai/factory-fire-monitoring-saudi-arabia/ · JSON: https://codeatoms.ai/factory-fire-monitoring-saudi-arabia/ontology/objects.json

- High-risk factory (site, in the operator's factory register)
- Fire alarm control panel (asset, in the factory's fire alarm control panel)
- Fire pump (asset, in the pump controller)
- Fire water tank (asset, in site survey)
- Tank level transmitter (asset, in the operator's IoT platform)
- Energy meter (CT set) (asset, in the operator's IoT platform)
- LoRaWAN gateway (asset, in the operator's IoT platform)
- Monitored point (measure, in the operator's IoT platform)
- Safety-critical alert (event, in the operator's IoT platform)
- Audit log record (record, in the operator's IoT platform)
- Periodic monitoring round (record, in the mobile monitoring tool)
- Preventive maintenance visit (record, in the maintenance schedule)
- Technical personnel (person, in the operator's staff directory)
- Monitoring officer (actor, in the operator's staff directory)

## Feeder Firewatch (energy and utilities, United States)

Design: https://codeatoms.ai/wildfire-risk-distribution-us/ · JSON: https://codeatoms.ai/wildfire-risk-distribution-us/ontology/objects.json

- Substation (site, in SCADA)
- Feeder (asset, in GIS)
- Feeder segment (asset, in GIS)
- Pole (asset, in GIS)
- Recloser (asset, in SCADA)
- Meter (asset, in AMI head end)
- Pole inspection record (record, in pole inspection spreadsheet)
- Outage event (event, in outage management system)
- Feeder segment ignition risk score (measure, in risk model store)
- Red flag warning (event, in weather and mesonet subscription)
- Wildfire camera station (asset, in wildfire camera vendor portal)
- Field crew (actor, in work management system)
- Work order (record, in work management system)
- PSPS decision record (record, in originates in this design (no upstream system))

## Terminal Pulse (maritime and ports, United States)

Design: https://codeatoms.ai/truck-turn-container-terminal-us/ · JSON: https://codeatoms.ai/truck-turn-container-terminal-us/ontology/objects.json

- Vessel Call (event, in terminal operating system)
- Container (material, in terminal operating system)
- Yard Block (site, in terminal operating system)
- RTG (asset, in crane management system (OEM))
- Ship to Shore Crane (asset, in crane management system (OEM))
- Truck Visit (event, in gate operating system)
- Gate Lane (asset, in gate operating system)
- Rail Cut (record, in railroad switch lists)
- Reefer Plug (asset, in reefer monitoring system)
- Yard Person (person, in access control and TWIC readers)
- Transfer Zone (site, in terminal operating system)
- Safety Event (record, in incident document system)

## Sovereign HSE Watch (oil and gas, Pakistan)

Design: https://codeatoms.ai/sovereign-hse-pakistan/ · JSON: https://codeatoms.ai/sovereign-hse-pakistan/ontology/objects.json

- Operating Facility / Site (asset)
- HSE Equipment (asset, in SAP PM)
- HSE Incident (record, in SAP EHS)
- Near Miss Report (record)
- Corrective Action (record, in SAP)
- Inspection / Audit Record (record, in SAP QM)
- HSE Document (document)
- Sensor Reading (event, in SCADA historian)
- Anomaly Event (event, in raised by a detection model)
- Agent Recommendation (event, in raised by an agent)
- HSE Person (person, in the operator's identity provider)
- HSE Role (person, in the operator's identity provider)

