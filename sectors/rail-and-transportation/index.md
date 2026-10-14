# Physical AI for rail and transportation: questions answered

Canonical: https://codeatoms.ai/sectors/rail-and-transportation/
License: CC BY 4.0
Publisher: CodeNinja Atoms (https://codeatoms.ai)



## What does a physical AI system for rail and transportation look like?

A complete physical AI design for rail and transportation names what to sense, which existing systems to join, the object model that joins them, the models and hardware, the three-year cost and the person who approves every action. CodeNinja Atoms has published 1 such reference architecture for rail and transportation, each free to reuse under CC BY 4.0. Consist Watch (United States): An open reference architecture for system design in physical AI. A real time condition monitoring system for a 225-car commuter fleet in the United States: onboard modules read 64 named signals per car and execute the operator's own fault-logic table at the car, telemetry rides the car system's existing cellular routers to a contractor-hosted US cloud, and severity-ranked faults reach the mechanical desk and the yard through one fleet ontology.

## Which AI models can a rail and transportation operator run on its own hardware?

Each published rail and transportation design names its models and why, and every model is open-weight or no model is used at all, so the operator can run it on hardware it owns. Consist Watch: Mistral Large 3 675B (Apache-2.0, self-hosted with vLLM) for the agentic work surface over the fleet ontology; Chronos-2 (Apache-2.0) for analog anomaly detection and seasonal trending; no training run.

## How much compute and hardware does AI in rail and transportation need?

The compute follows from the models: the published rail and transportation designs size it as follows, from no new hardware to a full GPU node. Consist Watch, compute: At the car, an EN 50155 and IEC 60571 module (8 by 8 by 8 inches, IP62, 24 to 48 VDC, CFR 238 materials); centrally, one 141 GB HBM GPU class node in a contractor-hosted US cloud.

## Is it cheaper to own AI hardware or rent cloud GPUs in rail and transportation?

Each rail and transportation design prices three years of ownership in its Appendix A, with every price cited, against renting the same capacity from a cloud region at its deepest three-year commitment where hardware is bought. Consist Watch: three-year cost, About 625,000 US dollars to run the eight-card node for three years on the deepest AWS commitment in US East, about three eighths of the 1.66 million on demand; the 225 modules are priced by quotation (Appendix A).

## What ontology or object model does a rail and transportation AI system need?

The object model is the part that makes the system an ontology rather than a pipeline: typed objects for the things in the rail and transportation operation, with properties, status values and typed links. Every published design ships its object model as hyper-ontology/1 JSON that loads into Hyper Ontology. Consist Watch: the operator's car, Onboard monitoring module, The car system, Digital input channel, Analog input channel, Active fault, Fault history record, Alert notification, Mechanical desk controller, Yard employee, the control center mechanical desk, the yard office, Slippery rail hotspot, Notification recipient group.

## Who approves the decisions an AI system makes in rail and transportation?

In every published rail and transportation design a named person makes the decision that changes the physical world; the system prepares it. Consist Watch: The module executes the operator's own fault logic verbatim; a named mechanical desk controller owns every active fault in that car's territory, and alerts go by severity to named recipient groups.

## Sources

- [Consist Watch: Executing the Operator's Own Fault Logic Across a 225-Car Commuter Fleet](https://codeatoms.ai/rail-fleet-condition-monitoring-us/) (United States), DOI https://doi.org/10.5281/zenodo.23365118
