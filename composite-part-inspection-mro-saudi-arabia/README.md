# Physical AI System Design for Composite Part Inspection in an Aviation MRO in Saudi Arabia

*VERTICAL-DRIVEN ARCHITECTURES · AVIATION & AEROSPACE MANUFACTURING · DESIGNED WITH CODENINJA PRAXIS · NOVEMBER 2026*

A [physical AI system design](https://codeatoms.ai/physical-ai-system-design/) for the composite repair shop of an aircraft maintenance, repair and overhaul provider in Saudi Arabia. Damage Draft: Sovereign AI Reference Architectures for Composite Repair in Aviation and Aerospace Manufacturing. Vision at the inspection bench and the scan station, one governed shop ontology of sixteen objects over six read only systems of record, three drafting agents that certifying engineers confirm and sign, and GLM 5.3 self hosted on one node inside the shop network.

**Canonical page:** https://codeatoms.ai/composite-part-inspection-mro-saudi-arabia/
**Paper:** [PDF](paper/composite-part-inspection-mro-saudi-arabia.pdf) · [HTML](paper/composite-part-inspection-mro-saudi-arabia.html) · [Word](paper/composite-part-inspection-mro-saudi-arabia.docx) · [Appendix A, what ownership costs over three years](paper/appendix_a_cost.md)
**DOI:** to be minted on release

**Licence:** CC BY 4.0. Cite the DOI or the canonical page.

## At a glance

| Part | The design |
|---|---|
| Sources | Six read only systems of record plus the bench and scan station cameras, entering through two adapter families (an integration adapter against the maintenance information system API and a file and document adapter for scanner exports and parseable manual content) that stamp every fact with its system, timestamp and extraction method: the maintenance information system, the scan equipment's image files, each customer's technical records with per customer isolation, the structural repair manuals under licence, the material and shelf life stock system and the quality findings log; nothing is ever written into a system of record |
| Object model | 16 typed objects with 12 typed links, from the customer, aircraft, part number and serialized part through the work order, task card, inspection and scan to the damage, damage class, allowable limit, repair scheme, material lot, technician qualification, finding and release, with the damage in the focal position and the serialized part carrying the shop's own states from Received to Released or Scrapped, published as JSON for reuse |
| Models | Six: GLM 5.3 (bespoke GLM-5.3 licence, 753B at FP8) for the three drafting agents (damage mapping, repair scheme, release paperwork), the command centre and ontology maintenance; Qwen3.8-27B dense multimodal (Apache-2.0) reading scans and bench photographs into structured damage; OWLv2 zero-shot detection and SAM 2.1 segmentation (Apache-2.0) at the bench; Anomalib (Apache-2.0) mapping subsurface anomalies on scan images; BGE-M3 (MIT) retrieval over manuals, records and confirmed maps; no third party model service, nothing trained into weights |
| Compute | Three tiers inside the shop network in Saudi Arabia: two fanless edge units of the octa core 6 TOPS NPU class at the inspection bench and the scan station; one 48 GB PCIe inference card on a shop server for the reader (about 28 GB at 8 bit) and the embedding model; one node of eight 141 GB HBM GPUs (1,128 GB) holding GLM 5.3's 753 GB of FP8 weights with a 1.2 planning factor, 904 GB. The node and the card are US origin accelerators for a D:3 and D:4 destination, so an export licence determination is a phase one checkpoint before any GPU is quoted |
| Rollout | Two phases carrying 18 scope items (17 and 1) across five workstreams, each closed by a gate, never a date: phase one on fan cowls and nacelle panels for one quarter, baseline first, then shadow mode, then a capability demonstration on reference panels, with the quality system change and the data protection assessment filed in parallel, and its exit gate a dev board run of the actual vision models on the 6 TOPS NPU class; phase two the extension to flight control surfaces and the remaining part families; measures are assessment hours per part, turnaround days, repeat findings on the same part type and rework after final inspection |
| Three-year cost | About 613,000 US dollars to own all three tiers for three years (a range of 583,000 to 639,000: about 570,000 for the node, about 42,000 for the site server and card, under 1,000 for the two edge units, with support and power at the national commercial electricity tariff), against about 773,000 to rent the node and the card on the deepest three year commitment in AWS Middle East (UAE), so ownership costs about four fifths of it, and about 2.06 million on demand, against which ownership costs about three tenths. Renting is a price reference only, because AWS lists no Saudi region on the day read and every rented option would carry customer records, scans and manual content across the border (Appendix A) |
| Human control | Agents map and draft and certifying engineers sign, by name: the certifying engineer confirms, amends or rejects the damage map and its classification, the design engineer approves or supersedes the repair scheme, material kit and qualification, and certifying staff sign the release; no agent classifies damage as repairable or releases a part; the disagreement path is built first and the count of engineer reports is published each week; every confirmed map and approved scheme is kept as memory the next assessment of the same part type reads |

**Made with.** Reasoned on [CodeNinja Praxis](https://codeatoms.ai/praxis/), the CodeNinja Atoms platform for designing physical AI systems. The object model imports into [Hyper Ontology](https://codeatoms.ai/hyper-ontology/), which turns it into a living system. Load it with the [hyper-ontology loader](../hyper-ontology-py/): `hyper-ontology show composite-part-inspection-mro-saudi-arabia`. Both are in beta; access by request.

## Abstract

*Physical AI System Design Begins at the Inspection Bench*

A physical AI system design for an aircraft maintenance, repair and overhaul provider in Saudi Arabia that repairs radomes, flight control surfaces, nacelle panels and fan cowls for commercial single aisle and wide body fleets starts from one question at the bench: does this damage on this part fall inside the allowable limit, and what has this part type suffered in the same place before? Today that question is assembled by hand from photographs stapled to a paper traveller, scan files stranded on the scanner's own computer and a findings log joined to nothing, so the same disbond on the same panel type is assessed from scratch every time, and no query the shop would recognize as simple can be run at all; the physical AI system design that would fix this must keep customer records, scan images and licensed manual content inside the shop's own network, on the operator's own hardware.

The design is a sovereign system of context built over the shop's existing systems of record: seven sources enter through two adapter families into a governed ontology of sixteen objects, five services run over that model, and eight surfaces carry the work to the people who sign; six models serve the whole, with zero-shot and anomaly vision models on sealed fanless edge units at one inspection bench and one scan station, a dense multimodal reader and a retrieval embedding model on a 48 GB-class site inference card, and a 753B-parameter frontier model served at FP8 on one node of eight 141 GB-class GPUs inside the shop network; three named agents draft damage maps, repair schemes and release paperwork while certifying engineers decide and sign, and every confirmed outcome is kept as memory the next decision reads rather than trained into weights.

The paper covers the industry problem and the join failure in the shop's systems, the constraints that shape the design, the stack and the object model, ingestion through adapters, the placement of inference, the models and their licenses, the rollout in two phases with their item counts and gates, and who owns what the design builds, before closing with how Praxis contextualized and reasoned the design from recorded reading.

## The object model

`ontology/objects.json` holds the 16 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology.

| Kind | Objects |
|---|---|
| actor | Customer |
| asset | Aircraft, Part (serialized), Material Lot |
| document | Part Number, Damage Class, Allowable Limit, Repair Scheme |
| record | Work Order, Task Card, Scan, Technician Qualification, Finding, Release |
| event | Inspection, Damage |

## The model and equipment register

`register/models.csv`, read from the paper's model and equipment register (Table 4) and chapters 7, 8 and 11: every model, its licence and weight, every hardware class and sizing rule, the sensing that feeds them, and the patterns the design stands on.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on Praxis, CodeNinja's platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
