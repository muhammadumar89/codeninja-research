# Physical AI for discrete manufacturing and automotive: questions answered

Canonical: https://codeatoms.ai/sectors/discrete-manufacturing-and-automotive/
License: CC BY 4.0
Publisher: CodeNinja Atoms (https://codeatoms.ai)

Vehicles and people share plant roads, test tracks and yards, and the cameras, gates and test schedules that should prove who was where are usually separate systems.

## What does a physical AI system for discrete manufacturing and automotive look like?

A complete physical AI design for discrete manufacturing and automotive names what to sense, which existing systems to join, the object model that joins them, the models and hardware, the three-year cost and the person who approves every action. CodeNinja Atoms has published 2 such reference architectures for discrete manufacturing and automotive, each free to reuse under CC BY 4.0. Pit Camera Watch (United States): a fully on-premises camera monitoring system that puts every turn, crossing, pit entry and access point of a vehicle proving ground on footage the operator owns, with exportable clips and camera uptime it can prove. Depot Operating Object Model (United States): An open reference architecture for system design in physical AI, built on ontologies for unifying factory systems at a government vehicle rebuild depot in the United States, where the inference server that runs it costs about 67,000 US dollars to own over three years. One operating object model joins the production control, inventory, maintenance and test cell systems, which never shared a key, so that a power pack failing its scripted test run can be traced the same day to the part lots, the machine that cut them and that machine's condition, and forward to the rework and the schedule it displaces. Every machine interface stays read only, and each release waits on a named person's sign-off.

## Which AI models can a discrete manufacturing and automotive operator run on its own hardware?

Each published discrete manufacturing and automotive design names its models and why, and every model is open-weight or no model is used at all, so the operator can run it on hardware it owns. Pit Camera Watch: D-FINE, Apache-2.0, for retrospective search over the archive (test vehicle, support vehicle, pedestrian); about 8 to 124 MB of weights. Depot Operating Object Model: gpt-oss-120b (Apache-2.0, US origin, self-hosted with vLLM) for the agentic work surface and ontology maintenance; Chronos-2 (Apache-2.0) for zero-shot machine condition forecasting and residual anomaly detection; nomic-embed-text-v2-moe (Apache-2.0) for retrieval over work orders, maintenance and test reports; no training run.

## How much compute and hardware does AI in discrete manufacturing and automotive need?

The compute follows from the models: the published discrete manufacturing and automotive designs size it as follows, from no new hardware to a full GPU node. Pit Camera Watch, compute: One 48 GB L40S-class card per recorder host, in the conditioned server room; nothing at the poles. Depot Operating Object Model, compute: Fanless DIN-rail edge boxes beside each machine group and at the test cell, their class fixed by a phase one measurement of the vibration load; centrally, two cards of the 48 GB PCIe class air cooled in the depot's own server room on its existing power, holding the 65.2 GB checkpoint with a 1.2 planning factor, about 78.2 GB against roughly 88 GB usable.

## Is it cheaper to own AI hardware or rent cloud GPUs in discrete manufacturing and automotive?

Each discrete manufacturing and automotive design prices three years of ownership in its Appendix A, with every price cited, against renting the same capacity from a cloud region at its deepest three-year commitment where hardware is bought. Pit Camera Watch: three-year cost, About 474,000 to 871,000 US dollars to own over three years, mostly camera heads; the two recorder hosts alone cost about four fifths of the deepest three-year AWS commitment, and there is no per camera license at any pole count (Appendix A). Depot Operating Object Model: three-year cost, About 67,000 US dollars to own the two-card server for three years (a range of 62,000 to 70,000: server, support and power), against about 104,000 dollars to rent the same card class on the deepest three-year commitment in US East and about 276,000 on demand; the cheapest rental that holds the model, one 96 GB card, is about 33,000 on that commitment, so ownership is chosen for the boundary, not the price, and renting is a price reference only because data and weights stay in the government's environment; edge boxes, sensors, cameras, time card and switches are priced by quotation (Appendix A).

## What ontology or object model does a discrete manufacturing and automotive AI system need?

The object model is the part that makes the system an ontology rather than a pipeline: typed objects for the things in the discrete manufacturing and automotive operation, with properties, status values and typed links. Every published design ships its object model as hyper-ontology/1 JSON that loads into Hyper Ontology. Pit Camera Watch: Test Site, Camera Pole, Camera Head, Underground Fiber Run, Safety Gate, Operator Booth Display, Recorder Server, 30-Day Footage Archive, Incident/Accident Record, Booth Operator, Gate Officer, Safety Office Reviewer, Vehicle Under Test, Test Cycle, Power and Fiber Assessment Package. Depot Operating Object Model: Power Pack, Vehicle Hull, Machine Tool, Power Pack Test Cell, Machine Sensor, Edge Gateway, Production Work Order, Maintenance Work Order, Schedule Proposal, Part Lot, Test Run, Run Report, Operator Role, Condition Indicator.

## Who approves the decisions an AI system makes in discrete manufacturing and automotive?

In every published discrete manufacturing and automotive design a named person makes the decision that changes the physical world; the system prepares it. Pit Camera Watch: Booth operators watch and decide; nothing raises an automated alarm; only the safety office can export a clip. Depot Operating Object Model: The system proposes and a person commits: the test cell operator signs every release or return, a planner approves every maintenance work order and accepts, modifies or declines every schedule proposal, and no machine, test cell or site control is ever written to.

## Sources

- [Pit Camera Watch: An On-Premises Camera Monitoring System for Every Turn, Crossing and Pit Entry on the Test Site](https://codeatoms.ai/test-site-camera-monitoring-us/) (United States), DOI https://doi.org/10.5281/zenodo.23296077
- [Depot Operating Object Model: Ontologies for Unifying Factory Systems at a United States Vehicle Rebuild Depot](https://codeatoms.ai/factory-ontology-rebuild-depot-us/) (United States), DOI https://doi.org/10.5281/zenodo.23570177
