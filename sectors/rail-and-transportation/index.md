# Physical AI for rail and transportation: questions answered

Canonical: https://codeatoms.ai/sectors/rail-and-transportation/
License: CC BY 4.0
Publisher: CodeNinja Atoms (https://codeatoms.ai)



## What does a physical AI system for rail and transportation look like?

A complete physical AI design for rail and transportation names what to sense, which existing systems to join, the object model that joins them, the models and hardware, the three-year cost and the person who approves every action. CodeNinja Atoms has published 2 such reference architectures for rail and transportation, each free to reuse under CC BY 4.0. Consist Watch (United States): An open reference architecture for system design in physical AI. A real time condition monitoring system for a 225-car commuter fleet in the United States: onboard modules read 64 named signals per car and execute the operator's own fault-logic table at the car, telemetry rides the car system's existing cellular routers to a contractor-hosted US cloud, and severity-ranked faults reach the mechanical desk and the yard through one fleet ontology. Wayside Trend Watch (United States): An open reference architecture for system design in physical AI. A predictive maintenance system for a freight railroad in the United States: the 29 wayside detectors the railroad already runs are trended per axle, keyed to serialized bearings, wheelsets and traction motors, and joined to work orders, interchange records and digitized contractor track reports in one object model, so the mechanical and track teams act on one ranked queue days or weeks before a single-reading stop alarm.

## Which AI models can a rail and transportation operator run on its own hardware?

Each published rail and transportation design names its models and why, and every model is open-weight or no model is used at all, so the operator can run it on hardware it owns. Consist Watch: Mistral Large 3 675B (Apache-2.0, self-hosted with vLLM) for the agentic work surface over the fleet ontology; Chronos-2 (Apache-2.0) for analog anomaly detection and seasonal trending; no training run. Wayside Trend Watch: gpt-oss-120b (Apache-2.0, self-hosted with vLLM) for the ranked queue and the ontology-maintaining agents; Chronos-2 (Apache-2.0) for zero-shot per-axle trend forecasting; D-FINE and PP-OCRv6 (Apache-2.0) for defect detection and reporting-mark OCR at the portal; no training run.

## How much compute and hardware does AI in rail and transportation need?

The compute follows from the models: the published rail and transportation designs size it as follows, from no new hardware to a full GPU node. Consist Watch, compute: At the car, an EN 50155 and IEC 60571 module (8 by 8 by 8 inches, IP62, 24 to 48 VDC, CFR 238 materials); centrally, one 141 GB HBM GPU class node in a contractor-hosted US cloud. Wayside Trend Watch, compute: At the new four-camera yard-entry portal, an octa-core NPU edge box sized from its streams, so only detections, OCR strings and short evidence frames cross a cellular link that drops for hours; centrally, one 141 GB HBM GPU class card in one node in the railroad's own data center, holding the 65.2 GB checkpoint with a 1.2 planning factor and about 63 GB to spare.

## Is it cheaper to own AI hardware or rent cloud GPUs in rail and transportation?

Each rail and transportation design prices three years of ownership in its Appendix A, with every price cited, against renting the same capacity from a cloud region at its deepest three-year commitment where hardware is bought. Consist Watch: three-year cost, About 625,000 US dollars to run the eight-card node for three years on the deepest AWS commitment in US East, about three eighths of the 1.66 million on demand; the 225 modules are priced by quotation (Appendix A). Wayside Trend Watch: three-year cost, About 54,000 US dollars to own the central card for three years (a range of 52,000 to 57,000, card, support and power, host server by quotation), against about 625,000 dollars to rent the smallest AWS instance that holds one such card on the deepest three-year commitment in US East and about 1.66 million on demand; the edge box, portal cameras and pilot locomotive sensing are priced by quotation (Appendix A).

## What ontology or object model does a rail and transportation AI system need?

The object model is the part that makes the system an ontology rather than a pipeline: typed objects for the things in the rail and transportation operation, with properties, status values and typed links. Every published design ships its object model as hyper-ontology/1 JSON that loads into Hyper Ontology. Consist Watch: Commuter car, Onboard monitoring module, Car system router, Digital input channel, Analog input channel, Active fault, Fault history record, Alert notification, Mechanical desk controller, Yard employee, Control center mechanical desk, Yard office, Slippery rail hotspot, Notification recipient group. Wayside Trend Watch: Freight Car, Locomotive, Axle Bearing (Roller Bearing), Wheelset, Traction Motor, Wayside Detector, Track Segment, Detector Reading, Trend Flag, Work Order, Track Geometry Exception, Rail Flaw Indication, AAR Interchange Record, Train.

## Who approves the decisions an AI system makes in rail and transportation?

In every published rail and transportation design a named person makes the decision that changes the physical world; the system prepares it. Consist Watch: The module executes the operator's own fault logic verbatim; a named mechanical desk controller owns every active fault in that car's territory, and alerts go by severity to named recipient groups. Wayside Trend Watch: The system advises and never acts: it touches no signal, train control or PTC system, the single-reading stop alarm to the dispatcher is unchanged, and a named person decides every set out and every slow order.

## Sources

- [Consist Watch: Executing the Operator's Own Fault Logic Across a 225-Car Commuter Fleet](https://codeatoms.ai/rail-fleet-condition-monitoring-us/) (United States), DOI https://doi.org/10.5281/zenodo.23365118
- [Wayside Trend Watch: Predictive Maintenance From Wayside Detectors for a Freight Railroad in the United States](https://codeatoms.ai/wayside-detector-trending-rail-us/) (United States), DOI https://doi.org/10.5281/zenodo.23556421
