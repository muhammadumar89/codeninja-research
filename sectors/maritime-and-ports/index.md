# Physical AI for maritime and ports: questions answered

Canonical: https://codeatoms.ai/sectors/maritime-and-ports/
License: CC BY 4.0
Publisher: CodeNinja Atoms (https://codeatoms.ai)

Terminals and port authorities run gates, cranes, yards and finance on separate systems, so nobody sees the whole flow of a box or a truck.

## What does a physical AI system for maritime and ports look like?

A complete physical AI design for maritime and ports names what to sense, which existing systems to join, the object model that joins them, the models and hardware, the three-year cost and the person who approves every action. CodeNinja Atoms has published 2 such reference architectures for maritime and ports, each free to reuse under CC BY 4.0. Port Twin (United States): one authoritative digital twin that binds a port's operational systems, live sensor feeds and finance backbone into a thirteen-object ontology, self-hosted on the port's own virtual machines inside the continental United States. Terminal Pulse (United States): truck turn time predicted two hours out and yard congestion seen live, at a container terminal, on the operator's own hardware with no outbound connection.

## Which AI models can a maritime and ports operator run on its own hardware?

Each published maritime and ports design names its models and why, and every model is open-weight or no model is used at all, so the operator can run it on hardware it owns. Port Twin: One self-hosted open model, BGE-M3, for document retrieval; no generative model and no token stream. Terminal Pulse: 5 self-hosted open models: GLM 5.3 (reasoning), Chronos-2 (forecasting), Qwen3-Embedding-0.6B (retrieval), RF-DETR (vision), Roboflow trackers.

## How much compute and hardware does AI in maritime and ports need?

The compute follows from the models: the published maritime and ports designs size it as follows, from no new hardware to a full GPU node. Port Twin, compute: No equipment bought: about 1.1 GB of fp16 weights on the port's existing enterprise virtual machines. Port Twin, boundary: Everything runs inside the continental United States on infrastructure the port already operates; no hosted document AI service in the path. Terminal Pulse, frontier compute: One node of eight 141 GB HBM-class GPUs holds GLM 5.3 at FP8 (753 GB of weights, 904 GB with headroom), at about 10 kW. Terminal Pulse, edge: Fanless IP-rated enclosures at the yard blocks, gate and quay; no safety reflex crosses a network hop.

## Is it cheaper to own AI hardware or rent cloud GPUs in maritime and ports?

Each maritime and ports design prices three years of ownership in its Appendix A, with every price cited, against renting the same capacity from a cloud region at its deepest three-year commitment where hardware is bought. Port Twin: three-year cost, No hardware line to price: the design adds software and integration work to servers the port already runs. Terminal Pulse: three-year cost, owned, About 722,000 US dollars with support and power at the US industrial power price; three-year cost, rented, 0.99 million to 2.52 million US dollars for the same GPUs around the clock; ownership is about four fifths the deepest three-year commitment (version 2); closed model break-even, The cheapest closed model matches the owned stack at about 35 users; above that, ownership is cheaper and the gap grows with every user.

## What ontology or object model does a maritime and ports AI system need?

The object model is the part that makes the system an ontology rather than a pipeline: typed objects for the things in the maritime and ports operation, with properties, status values and typed links. Every published design ships its object model as hyper-ontology/1 JSON that loads into Hyper Ontology. Port Twin: Berth, Navigation channel, Subsurface utility layer, Environmental sensor feed, Parcel / facility, Bathymetric survey surface, Utility gap record, Capital project, Inspection record, Vessel movement record, Truck movement record, PCS message, Engineering document. Terminal Pulse: Vessel Call, Container, Yard Block, RTG, Ship to Shore Crane, Truck Visit, Gate Lane, Rail Cut, Reefer Plug, Yard Person, Transfer Zone, Safety Event.

## Who approves the decisions an AI system makes in maritime and ports?

In every published maritime and ports design a named person makes the decision that changes the physical world; the system prepares it. Port Twin: The twin shows; pilots, berth planners, engineers and finance staff decide in their own systems, and nothing writes back into a system of record. Terminal Pulse: Surfaces warn and propose; the named planner acts in the terminal operating system and the named safety supervisor acknowledges every safety event.

## Sources

- [Port Twin: One Governed Digital Twin for Every Asset, Feed and Dollar](https://codeatoms.ai/port-digital-twin-us/) (United States), DOI https://doi.org/10.5281/zenodo.23126431
- [Terminal Pulse: Predicted Truck Turn Time and Live Yard Sight for a Container Terminal](https://codeatoms.ai/truck-turn-container-terminal-us/) (United States), DOI https://doi.org/10.5281/zenodo.23159331
