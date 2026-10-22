# Physical AI for warehousing and intralogistics: questions answered

Canonical: https://codeatoms.ai/sectors/warehousing-and-intralogistics/
License: CC BY 4.0
Publisher: CodeNinja Atoms (https://codeatoms.ai)



## What does a physical AI system for warehousing and intralogistics look like?

A complete physical AI design for warehousing and intralogistics names what to sense, which existing systems to join, the object model that joins them, the models and hardware, the three-year cost and the person who approves every action. CodeNinja Atoms has published 1 such reference architecture for warehousing and intralogistics, each free to reuse under CC BY 4.0. Warehouse Twin Command (United States): An open reference architecture for system design in physical AI. A live digital twin of four distribution centers run by a warehousing and intralogistics operator in the United States: one object model projected over the warehouse, labor and yard systems the operation already runs, kept true by nightly reconciliation against the WMS, producing weekly slotting recommendations, dock and yard schedules and on-site safety vision on the existing cameras, with every action drafted for a person to approve.

## Which AI models can a warehousing and intralogistics operator run on its own hardware?

Each published warehousing and intralogistics design names its models and why, and every model is open-weight or no model is used at all, so the operator can run it on hardware it owns. Warehouse Twin Command: Mistral Large 3 675B (Apache-2.0) for the site manager assistant; Qwen3.8-27B (Apache-2.0) for assistant continuity at each site; RF-DETR N to L (Apache-2.0) and OC-SORT (MIT) for safety vision; BGE-M3 (MIT) for retrieval; no face recognition, no re-identification, no training run.

## How much compute and hardware does AI in warehousing and intralogistics need?

The compute follows from the models: the published warehousing and intralogistics designs size it as follows, from no new hardware to a full GPU node. Warehouse Twin Command, compute: At each site, one industrial edge server with one 48 GB PCIe inference card running vision in Triton and the site model under vLLM; centrally, one 141 GB HBM class node of eight cards, on the operator's own hardware.

## Is it cheaper to own AI hardware or rent cloud GPUs in warehousing and intralogistics?

Each warehousing and intralogistics design prices three years of ownership in its Appendix A, with every price cited, against renting the same capacity from a cloud region at its deepest three-year commitment where hardware is bought. Warehouse Twin Command: three-year cost, About 597,000 US dollars to own the twelve cards (510,000 to 689,000) before the four edge chassis, which are priced by quotation; renting the same cards in AWS US East runs about 1.86 million on demand and about 699,000 on the deepest three-year commitment (Appendix A).

## What ontology or object model does a warehousing and intralogistics AI system need?

The object model is the part that makes the system an ontology rather than a pipeline: typed objects for the things in the warehousing and intralogistics operation, with properties, status values and typed links. Every published design ships its object model as hyper-ontology/1 JSON that loads into Hyper Ontology. Warehouse Twin Command: Distribution Center, Dock Door, Yard Trailer, Storage Slot, SKU, Open Order, Pick Task, Associate, Labor Shift, Camera Zone, Safety Event, Forklift, Shift Lead, Slotting Recommendation.

## Who approves the decisions an AI system makes in warehousing and intralogistics?

In every published warehousing and intralogistics design a named person makes the decision that changes the physical world; the system prepares it. Warehouse Twin Command: Every slotting move states walking saved and move labor before a person approves it; every safety event becomes a clip a supervisor reviews, and analytics never act as a safety-rated stop.

## Sources

- [Warehouse Twin Command: Live Slotting, Docks, Yards and Safety Vision for Warehousing and Intralogistics in the United States](https://codeatoms.ai/warehouse-digital-twin-us/) (United States), DOI https://doi.org/10.5281/zenodo.23556416
