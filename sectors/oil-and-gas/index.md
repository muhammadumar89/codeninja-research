# Physical AI for oil and gas: questions answered

Canonical: https://codeatoms.ai/sectors/oil-and-gas/
License: CC BY 4.0
Publisher: CodeNinja Atoms (https://codeatoms.ai)

Wells, terminals and plants hold safety, inventory and process data in systems that were never joined, often on sites where the data may not leave the country.

## What does a physical AI system for oil and gas look like?

A complete physical AI design for oil and gas names what to sense, which existing systems to join, the object model that joins them, the models and hardware, the three-year cost and the person who approves every action. CodeNinja Atoms has published 2 such reference architectures for oil and gas, each free to reuse under CC BY 4.0. Sovereign HSE Watch (Pakistan): An open reference architecture for predicting HSE incidents at an oil and gas operator in Pakistan, on the operator's own hardware, with no data leaving the country and no third-party AI service in the serving path. Loop Integrity Watch (Pakistan): field hardware that rebuilds the signal path on three Modbus loops, and a governed inventory ontology that catches a flatlined or swapped radar gauge reading before the central inventory picture misleads anyone.

## Which AI models can an oil and gas operator run on its own hardware?

Each published oil and gas design names its models and why, and every model is open-weight or no model is used at all, so the operator can run it on hardware it owns. Sovereign HSE Watch: 6 self-hosted open-weight models, including GLM 5.3 (reasoning), Chronos-2 (forecasting), RF-DETR (vision), BGE-M3 (retrieval in English and Urdu) and PaddleOCR-VL 1.6 (scans). Loop Integrity Watch: None: every integrity check (stuck value, swap, distortion) is deterministic.

## How much compute and hardware does AI in oil and gas need?

The compute follows from the models: the published oil and gas designs size it as follows, from no new hardware to a full GPU node. Sovereign HSE Watch, frontier compute: One node of eight 141 GB HBM-class GPUs holds GLM 5.3 at FP8 (753 GB of weights, 904 GB with headroom). Sovereign HSE Watch, the hard dependency: 141 GB-class accelerators need a US export licence for Pakistan (Country Group D:4); the rollout's first gate confirms installed hardware first. Loop Integrity Watch, compute: Two containers on the operator's own site application server, inside its OT boundary. Loop Integrity Watch, field scope: 13 fuel tanks on 3 Modbus RTU loops; 3 booster installations engineered from a measured signal survey inside explosion proof junction boxes.

## Is it cheaper to own AI hardware or rent cloud GPUs in oil and gas?

Each oil and gas design prices three years of ownership in its Appendix A, with every price cited, against renting the same capacity from a cloud region at its deepest three-year commitment where hardware is bought. Sovereign HSE Watch: three-year cost, owned, About 670,000 US dollars with support and power at Pakistan's industrial tariff; three-year cost, rented, 1.1 to 2.8 million US dollars for the same GPUs in the nearest cloud region; no hyperscaler runs a region in Pakistan. Loop Integrity Watch: three-year cost, No compute to price; the field equipment is priced by OEM quotation against the survey (Appendix A).

## What ontology or object model does an oil and gas AI system need?

The object model is the part that makes the system an ontology rather than a pipeline: typed objects for the things in the oil and gas operation, with properties, status values and typed links. Every published design ships its object model as hyper-ontology/1 JSON that loads into Hyper Ontology. Sovereign HSE Watch: Operating Facility / Site, HSE Equipment, HSE Incident, Near Miss Report, Corrective Action, Inspection / Audit Record, HSE Document, Sensor Reading, Anomaly Event, Agent Recommendation, HSE Person, HSE Role. Loop Integrity Watch: Fuel Tank, Radar Tank Gauge (RTG), RTG Communication Loop, Modbus Booster (Repeater), Explosion Proof Junction Box, Gauge Reading, Data Quality Event, Central Inventory Picture, Loop Wiring As-Built, Service Order, Warranty and Support Record, OEM Authorization Letter, HSE Work Permit, Instrumentation Technician, Location Engineer.

## Who approves the decisions an AI system makes in oil and gas?

In every published oil and gas design a named person makes the decision that changes the physical world; the system prepares it. Sovereign HSE Watch: Every recommendation is approved or rejected by a named person; nothing executes on equipment. Loop Integrity Watch: Every data quality event is acknowledged and resolved by a named person; the location engineer signs acceptance.

## Sources

- [Sovereign HSE Watch: A Reference Architecture for Predictive Health, Safety and Environment Intelligence in Pakistan's Oil and Gas Operations](https://codeatoms.ai/sovereign-hse-pakistan/) (Pakistan), DOI https://doi.org/10.5281/zenodo.23119714
- [Loop Integrity Watch: Ending Distorted Radar Level Readings and Tank-to-Tank Swapping Across the Tank Farm](https://codeatoms.ai/tank-gauge-integrity-pakistan/) (Pakistan), DOI https://doi.org/10.5281/zenodo.23157967
