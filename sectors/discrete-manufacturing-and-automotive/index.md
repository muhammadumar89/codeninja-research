# Physical AI for discrete manufacturing and automotive: questions answered

Canonical: https://codeatoms.ai/sectors/discrete-manufacturing-and-automotive/
License: CC BY 4.0
Publisher: CodeNinja Atoms (https://codeatoms.ai)

Vehicles and people share plant roads, test tracks and yards, and the cameras, gates and test schedules that should prove who was where are usually separate systems.

## What does a physical AI system for discrete manufacturing and automotive look like?

A complete physical AI design for discrete manufacturing and automotive names what to sense, which existing systems to join, the object model that joins them, the models and hardware, the three-year cost and the person who approves every action. CodeNinja Atoms has published 1 such reference architecture for discrete manufacturing and automotive, each free to reuse under CC BY 4.0. Pit Camera Watch (United States): a fully on-premises camera monitoring system that puts every turn, crossing, pit entry and access point of a vehicle proving ground on footage the operator owns, with exportable clips and camera uptime it can prove.

## Which AI models can a discrete manufacturing and automotive operator run on its own hardware?

Each published discrete manufacturing and automotive design names its models and why, and every model is open-weight or no model is used at all, so the operator can run it on hardware it owns. Pit Camera Watch: D-FINE, Apache-2.0, for retrospective search over the archive (test vehicle, support vehicle, pedestrian); about 8 to 124 MB of weights.

## How much compute and hardware does AI in discrete manufacturing and automotive need?

The compute follows from the models: the published discrete manufacturing and automotive designs size it as follows, from no new hardware to a full GPU node. Pit Camera Watch, compute: One 48 GB L40S-class card per recorder host, in the conditioned server room; nothing at the poles.

## Is it cheaper to own AI hardware or rent cloud GPUs in discrete manufacturing and automotive?

Each discrete manufacturing and automotive design prices three years of ownership in its Appendix A, with every price cited, against renting the same capacity from a cloud region at its deepest three-year commitment where hardware is bought. Pit Camera Watch: three-year cost, About 474,000 to 871,000 US dollars to own over three years, mostly camera heads; the two recorder hosts alone cost about four fifths of the deepest three-year AWS commitment, and there is no per camera license at any pole count (Appendix A).

## What ontology or object model does a discrete manufacturing and automotive AI system need?

The object model is the part that makes the system an ontology rather than a pipeline: typed objects for the things in the discrete manufacturing and automotive operation, with properties, status values and typed links. Every published design ships its object model as hyper-ontology/1 JSON that loads into Hyper Ontology. Pit Camera Watch: The site, Camera Pole, Camera Head, Underground Fiber Run, Safety Gate, Operator Booth Display, Server (the operator's own system), 30-Day Footage Archive, Incident/Accident Record, The site Operator, Gate Officer, Safety Office Reviewer, Vehicle Under Test, Test Cycle, The operator's own system Power/Fiber assessment package.

## Who approves the decisions an AI system makes in discrete manufacturing and automotive?

In every published discrete manufacturing and automotive design a named person makes the decision that changes the physical world; the system prepares it. Pit Camera Watch: Booth operators watch and decide; nothing raises an automated alarm; only the safety office can export a clip.

## Sources

- [Pit Camera Watch: An On-Premises Camera Monitoring System for Every Turn, Crossing and Pit Entry on the Test Site](https://codeatoms.ai/test-site-camera-monitoring-us/) (United States), DOI https://doi.org/10.5281/zenodo.23295991
