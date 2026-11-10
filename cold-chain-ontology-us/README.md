# Industrial Data Ontology for a Cold Chain From Plant to Store in the United States

*VERTICAL-DRIVEN ARCHITECTURES · SUPPLY CHAIN & LOGISTICS · DESIGNED WITH CODENINJA PRAXIS · NOVEMBER 2026*

Lot Thread: Industrial AI for Cold Chain Traceability From Plant to Store. An industrial data ontology for a refrigerated and frozen food manufacturer in the United States: one governed model of a lot's journey across five custodians, sixteen objects over eight read only systems of record, three drafting agents that a named analyst, quality manager and regulatory lead confirm, and GLM 5.3 self hosted on one node in the operator's own server room.

**Canonical page:** https://codeatoms.ai/cold-chain-ontology-us/
**Paper:** [PDF](paper/cold-chain-ontology-us.pdf) · [HTML](paper/cold-chain-ontology-us.html) · [Word](paper/cold-chain-ontology-us.docx) · [Appendix A, what ownership costs over three years](paper/appendix_a_cost.md)
**DOI:** [10.5281/zenodo.24048543](https://doi.org/10.5281/zenodo.24048543)

**Licence:** CC BY 4.0. Cite the DOI or the canonical page.

## At a glance

| Part | The design |
|---|---|
| Sources | Eight read only systems of record across five custodians, entering through three adapter families (an integration adapter on change data capture, a telemetry adapter for reefer and dock readings, an EDI adapter for retailer notices and partner files) that stamp every fact with its source system and its source key: the plant manufacturing execution system, the operator's own and third party cold store warehouse management systems, the carriers' reefer telematics, the transportation management system, the retailers' receiving notices, the quality hold and release system and the recall and complaint register; each partner feed is gated on written data terms, and no adapter exposes a write path |
| Object model | 16 typed objects with 13 typed links, from the product, lot, pallet and case through the critical tracking event, custodian, location, dock, truck and reefer reading to the excursion, hold, release, complaint, receipt and traceability record, held as a projection over the systems of record rather than a copy of them and published as JSON for reuse; the pallet is the hinge where the five vocabularies meet |
| Models | GLM 5.3, named by the operator, as the frontier class open weight work surface for the mapping, excursion and trace agents and the cited conversational interface, under a license whose attribution notice and managed service trigger counsel reviews before hosting; document reading and embedding entries by class on an air cooled PCIe server; no entry survived live verification on this run, so the register holds catalog entries and the commitment waits on a verified row; nothing is trained or fine tuned, improvement runs through the memory of confirmed joins |
| Compute | One central tier in the operator's existing server room in the United States: one node of eight 141 GB HBM cards (1,128 GB) drawing about 10 kW, holding 756 GB of FP8 weights with about 280 GB of KV cache headroom; no compute in freezers, on docks or in trucks, because readings arrive as partner data; inbound feeds only, no egress path, updates through the Harbor registry |
| Rollout | Two phases carrying 16 scope items (7 and 9), each closed by a gate, never a date: a Foundation phase that builds the ontology, the explicit identifier mapping and the ingest normalisation, then a Phase One Corridor running one product family through one plant, one cold store and one retailer for one quarter; the exit gate is a lot's full record in hours instead of a week (nominal 4.0 hours), lots joined end to end, excursions joined to exposed lots within the hour, and a rehearsed dock door event in which the retailer is told before the truck arrives; the mapping agent runs in shadow mode with a measured acceptance rate before any credit is taken |
| Three-year cost | About 591,000 US dollars to own the node for three years (a range of 546,000 to 615,000: node, support and power at the national average commercial or industrial price), against about 625,000 to rent the same eight cards on the deepest three year commitment in AWS US East (N. Virginia), so ownership costs about nine tenths of it, and about 1.66 million on demand, against which ownership costs about a third. Renting is a price reference only, because every rented option would carry product, lot and partner data out of the operator's hardware (Appendix A) |
| Human control | Agents draft and people decide, by name: the traceability analyst confirms every identifier join the mapping agent drafts, the quality manager approves every hold the excursion agent recommends and acts in the quality hold and release system, the regulatory affairs lead sends every trace record the trace agent drafts; no agent places or lifts a hold or sends a record to a regulator, an escalation view surfaces unacknowledged excursions, and every confirmed join is kept as memory the next join reads |

**Made with.** Reasoned on [CodeNinja Praxis](https://codeatoms.ai/praxis/), the CodeNinja Atoms platform for designing physical AI systems. The object model imports into [Hyper Ontology](https://codeatoms.ai/hyper-ontology/), which turns it into a living system. Load it with the [hyper-ontology loader](../hyper-ontology-py/): `hyper-ontology show cold-chain-ontology-us`. Both are in beta; access by request.

## Abstract

*A Lot's Journey Should Take Hours, Not a Week and Three Phone Calls*

An industrial data ontology for a cold chain from plant to store in the United States has to answer one question: when a retailer reports a soft case, which pallets shared its dock time and its truck, and when the federal food traceability rule asks, can the lot's whole journey be produced within twenty four hours. Today the operator cannot answer either within a day, because its chain has five custodians and five vocabularies: a pallet is a lot in the plant, a license plate in the warehouse, a shipment line in transport, a receipt in the retailer's notice and a case in a complaint. A temperature excursion on a dock is logged by the warehouse while the truck's telematics logs a different one an hour later, and neither is joined to the lot that sat on the dock. The quality managers hold the mapping between the vocabularies in their heads, which is why producing a record takes a week and three phone calls and why the rule's compliance date of July 2028 finds the operation unprepared.

The design reads eight named systems of record, from the plant manufacturing execution system to the recall and complaint register, through three adapter families: an integration adapter for change data capture, a telemetry adapter for reefer and dock readings, and an EDI adapter for retailer notices and file routes. Everything lands in one governed object model of sixteen objects with typed links, from Lot and Pallet through Dock, Truck, Excursion and Hold to the trace record the rule asks for, held as a projection over the systems of record rather than a copy of them. Six services, from ontology and identifiers through the command center to the phase one corridor, expose four surfaces: an excursion and hold approval queue, a mapping exception queue, a trace queue and an escalation view. The model register is deliberately empty, because no open weight model survived live verification on this run; the work surface commits frontier class open weights self hosted for sovereignty, to be sized when a verified entry stands in the register. All of it runs on the operator's own hardware in the United States, and no product, lot or partner data leaves that boundary.

The paper covers the industry problem and the regulatory regimes behind it, the join failure across the five vocabularies, the constraints and scoping decisions, the stack from systems of record to surfaces, the object model and its typed links, ingestion through adapters, where serving sits and why no edge inference exists, the empty model register and what it will take to fill it, the two phase rollout with its gates, measurements, failure modes and open questions, who owns what the design builds, and finally how Praxis contextualized and reasoned the design.

## The object model

`ontology/objects.json` holds the 16 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology.

| Kind | Objects |
|---|---|
| material | Product, Lot, Case |
| asset | Pallet, Truck |
| event | Critical Tracking Event, Excursion |
| site | Location, Dock |
| actor | Custodian |
| measure | Reefer Reading |
| record | Hold, Release, Complaint, Traceability Record |
| document | Receipt |

## The model and equipment register

`register/models.csv`, read from the paper's model and equipment register (Table 4), the architecture table (Table 7) and chapters 6, 7 and 8: the named model and its license terms, the hardware class and sizing rule, the sensing classes, the backbone and adapter products, and the patterns the design stands on.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on Praxis, CodeNinja's platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
