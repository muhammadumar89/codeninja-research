# Physical AI for energy and utilities: questions answered

Canonical: https://codeatoms.ai/sectors/energy-and-utilities/
License: CC BY 4.0
Publisher: CodeNinja Atoms (https://codeatoms.ai)

Grids and plants run on control systems, maintenance records and field crews that were never designed to share one picture of risk.

## What does a physical AI system for energy and utilities look like?

A complete physical AI design for energy and utilities names what to sense, which existing systems to join, the object model that joins them, the models and hardware, the three-year cost and the person who approves every action. CodeNinja Atoms has published 3 such reference architectures for energy and utilities, each free to reuse under CC BY 4.0. Grid Context Watch (United States): one system of context that sees every device on a utility's control networks, flags abnormal behaviour and assembles the evidence a NERC CIP audit asks for, on the operator's own hardware. Reliability Atlas (Saudi Arabia): a records-based reliability and availability assessment that joins each plant's work orders, trip history and design documents into one reliability object model the operator owns, so every availability figure, criticality rank and root cause finding traces to its source. Feeder Firewatch (United States): a live ignition and outage risk score for every distribution feeder segment, built on the cooperative's own hardware, with every de-energisation and fast-trip change approved by a named operator.

## Which AI models can an energy and utilities operator run on its own hardware?

Each published energy and utilities design names its models and why, and every model is open-weight or no model is used at all, so the operator can run it on hardware it owns. Grid Context Watch: GLM 5.2 (MIT) for reasoning and Qwen3-Embedding-0.6B (Apache-2.0) for retrieval; detection stays in the procured sensors. Reliability Atlas: None: the register is empty by design because no inference workload is contracted. Feeder Firewatch: Self-hosted open-weight models: GLM 5.2 under MIT (reasoning) on site, RF-DETR (vision) at the edge.

## How much compute and hardware does AI in energy and utilities need?

The compute follows from the models: the published energy and utilities designs size it as follows, from no new hardware to a full GPU node. Grid Context Watch, compute: One node of eight 141 GB HBM-class GPUs: 753 GB of FP8 weights, 904 GB with the 1.2 planning factor, against 1,128 GB. Grid Context Watch, boundary: Read only and one way out of the control networks; nothing writes into an electronic security perimeter, and no data leaves the operator. Reliability Atlas, compute: No hardware bought; the study runs on the operator's own in-country servers. Feeder Firewatch, frontier compute: One node of eight 141 GB HBM-class GPUs holds GLM 5.2 at FP8 (753 GB of weights, 904 GB with headroom). Feeder Firewatch, edge: Sealed industrial boxes at substations and on patrol trucks detect smoke and damaged equipment when cellular coverage drops.

## Is it cheaper to own AI hardware or rent cloud GPUs in energy and utilities?

Each energy and utilities design prices three years of ownership in its Appendix A, with every price cited, against renting the same capacity from a cloud region at its deepest three-year commitment where hardware is bought. Grid Context Watch: three-year cost, About 510,000 dollars to own the reasoning node, about four fifths the deepest three-year AWS commitment (Appendix A). Reliability Atlas: three-year cost, No hardware line to price: the cost is the assessment work itself (Appendix A). Feeder Firewatch: three-year cost, owned, About 841,000 US dollars with support and power at the Texas industrial power price; three-year cost, rented, 0.88 million to 1.92 million US dollars for the same GPUs around the clock; ownership costs about the same as the deepest three-year commitment (version 2); closed model break-even, The cheapest closed model matches the owned stack at about 41 users; above that, ownership is cheaper and the gap grows with every user.

## What ontology or object model does an energy and utilities AI system need?

The object model is the part that makes the system an ontology rather than a pipeline: typed objects for the things in the energy and utilities operation, with properties, status values and typed links. Every published design ships its object model as hyper-ontology/1 JSON that loads into Hyper Ontology. Grid Context Watch: Substation, OT Asset, Network Sensor, Anomaly Alert, Investigation Case, Vulnerability Finding, Detection Rule, Threat Intelligence Item, Pcap Evidence Record, CIP Evidence Artefact, OT Security Analyst, SIEM, Energy management system, Substation data platform. Reliability Atlas: Plant, Production train, Equipment, Failure mode, Work order, Downtime event, Availability prediction, Availability target, Criticality index, RCA report, Major event, Spare part, Reliability program. Feeder Firewatch: Substation, Feeder, Feeder segment, Pole, Recloser, Meter, Pole inspection record, Outage event, Feeder segment ignition risk score, Red flag warning, Wildfire camera station, Field crew, Work order, PSPS decision record.

## Who approves the decisions an AI system makes in energy and utilities?

In every published energy and utilities design a named person makes the decision that changes the physical world; the system prepares it. Grid Context Watch: Every triage, case and risk acceptance carries a named OT security analyst; agents draft, the analyst decides. Reliability Atlas: Predictions are accepted only by a named reviewer and RCA reports validated only by a named engineer. Feeder Firewatch: Every public safety power shutoff (PSPS) recommendation becomes a decision record a named operator approves or declines; the design never opens or closes a recloser.

## Sources

- [Grid Context Watch: One system of context for OT Security and NERC CIP Evidence](https://codeatoms.ai/ot-security-cip-evidence-us/) (United States), DOI https://doi.org/10.5281/zenodo.23157957
- [Reliability Atlas: A Plant Reliability Assessment Study the Operator Can Audit](https://codeatoms.ai/plant-reliability-assessment-saudi-arabia/) (Saudi Arabia), DOI https://doi.org/10.5281/zenodo.23157965
- [Feeder Firewatch: Live Ignition and Outage Risk for Every Distribution Feeder](https://codeatoms.ai/wildfire-risk-distribution-us/) (United States), DOI https://doi.org/10.5281/zenodo.23159328
