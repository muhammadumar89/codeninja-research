# A Self-Improving AI System for Carrier Exception Handling in the United States

*VERTICAL-DRIVEN ARCHITECTURES · SUPPLY CHAIN & LOGISTICS · DESIGNED WITH CODENINJA PRAXIS · NOVEMBER 2026*

Lane Memory: A Sovereign AI Reference Architecture for Self-Improving Carrier Exception Handling in Supply Chain and Logistics. A [self-improving AI system](https://codeatoms.ai/self-improving-ai-system/) for a third party logistics provider in the United States: one governed freight ontology of sixteen objects over seven read only systems and the working threads, three drafting agents that named coordinators confirm, memory that compounds from every confirmed outcome, and GLM 5.3 self hosted on one node in the operator's own facility.

**Canonical page:** https://codeatoms.ai/carrier-exceptions-us/
**Paper:** [PDF](paper/carrier-exceptions-us.pdf) · [HTML](paper/carrier-exceptions-us.html) · [Word](paper/carrier-exceptions-us.docx) · [Appendix A, what ownership costs over three years](paper/appendix_a_cost.md)
**DOI:** assigned on release.

**Licence:** CC BY 4.0. Cite the DOI or the canonical page.

## At a glance

| Part | The design |
|---|---|
| Sources | Seven read only systems of record and the working threads, entering through one integration adapter family (change capture on the transactional systems, governed pulls on the feeds and threads) that stamps every record with provenance, ordering, the shipper's data terms and conformity to the model: the transportation management system, the carrier tracking and visibility platform, the appointment scheduling tool, the claims system, the carrier scorecards and contracts, the customer order feeds, and the email and chat threads where exceptions are worked; the design writes one thing, the approved appointment change request into the scheduling tool, and nothing else anywhere |
| Object model | 16 typed objects with 13 typed links, from the shipper, order, shipment, stop and appointment through the carrier, driver and tracking event to the exception, exception type, action, resolution, standing fix, claim, scorecard entry and exception coordinator, each anchored in the system that owns it, with three status vocabularies for the exception, the action and the resolution, and published as JSON for reuse |
| Models | GLM 5.3 (GLM-5.3 bespoke license, 753B at FP8) for the triage, recovery and review drafting, the command center's cited conversational interface and ontology maintenance; Qwen3.8 27B (Apache-2.0, FP8) at the site tier parsing years of threads and notes; Qwen3-Embedding 0.6B (Apache-2.0) for retrieval over threads, notes and resolutions; no third party model service, nothing trained into weights |
| Compute | One node of eight 141 GB HBM cards (1,128 GB) in the operator's own facility, holding 753 GB of FP8 weights with the 1.2 planning factor, 904 GB, and about 280 GB of KV ceiling for concurrent coordinator sessions; one 48 GB PCIe card in an air cooled server for the parsing and embedding models; no edge tier and no cameras, the trucks are seen through the tracking feeds the operator already owns |
| Rollout | Two phases carrying 18 scope items (17 and 1), each closed by a gate, never a date: a pilot quarter on one regional lane group whose gate is measured improvement in time to resolve and repeat exceptions against a baseline recorded before any draft reaches a coordinator, then the extension decision for the other lane groups; the 21 requirements map onto the 18 items |
| Three-year cost | About 606,000 US dollars to own both tiers for three years (a range of 577,000 to 665,000: the node, the card, support and power at national average prices), of which the node is about 591,000, against about 644,000 to rent the same hardware on the deepest three year commitment in AWS US East (N. Virginia), so ownership costs about 94 percent of it, and about 1.71 million on demand, against which ownership costs about a third. Renting is a price reference only, because every rented option would carry shippers' freight data and the threads out of the operator's facility (Appendix A) |
| Human control | Agents draft and coordinators decide, by name: the exception coordinator confirms the triage draft and approves the carrier message, the appointment change and the shipper notice, the operations manager approves each standing fix, the approver is recorded on the action object, and confirmations are tested with known answer probes and a weekly sample so that ground truth is a decision and not a reflex; every confirmed outcome becomes memory the next exception reads |

**Made with.** Reasoned on [CodeNinja Praxis](https://codeatoms.ai/praxis/), the CodeNinja Atoms platform for designing physical AI systems. The object model imports into [Hyper Ontology](https://codeatoms.ai/hyper-ontology/), which turns it into a living system. Load it with the [hyper-ontology loader](../hyper-ontology-py/): `hyper-ontology show carrier-exceptions-us`. Both are in beta; access by request.

## Abstract

*The Exception Desk Should Get Better Every Week*

A self-improving AI system for a third party logistics provider in the United States, one that manages truckload and less than truckload freight for shippers across a network of contracted carriers, must answer one question when an exception lands: what fixed this same exception, on this lane, with this carrier, at this consignee, the last time it happened? The answer exists, but it is buried in years of email and chat threads no system reads, held in the heads of coordinators whose knowledge leaves with them through a high turnover desk, and scattered across seven systems of record that never meet. Teams evaluating a self-improving AI system for logistics meet exactly this shape: the data is already inside the estate, the improvement loop is not, and shippers now measure the operator on time to resolve and on whether they were told before they asked.

The design reads seven source systems through one integration adapter family into a governed ontology of sixteen objects joined by typed links, projected never migrated, with a single gated write path into the scheduling tool behind coordinator approval. Eight services run on that ontology, delivering triage, recovery and review agents on two surfaces, the exception command center and the weekly recurring exception review. Three models carry the work: GLM 5.3 at FP8 on one node of eight GPUs of the 141 GB class in the operator's own facility, drafting for coordinators who confirm; a Qwen3.8 27B dense model at the site tier parsing threads and notes; and Qwen3-Embedding 0.6B for retrieval. Improvement runs on recursive memory loops over confirmed outcomes, never on training or fine tuning, so nothing about a shipper's freight leaves the operator's control and no weights change on the fly.

The paper covers the operation and the problem its systems cannot answer, the constraints, the stack, the object model, ingestion, inference placement, the models and their licenses, the rollout and its proof, ownership, and finally how Praxis contextualized and reasoned the design.

## The object model

`ontology/objects.json` holds the 16 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology.

| Kind | Objects |
|---|---|
| actor | Shipper, Carrier, Driver, Exception Coordinator |
| record | Order, Shipment, Stop, Appointment, Action, Resolution, Standing Fix, Claim, Scorecard Entry |
| event | Tracking Event, Exception |
| vocabulary | Exception Type |

## The model and equipment register

`register/models.csv`, read from the paper's model and equipment register (Table 4), its architecture table (Table 7) and chapters 7 and 8: every model, its license and weight, every hardware class and sizing rule, and the patterns the design stands on.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on Praxis, CodeNinja's platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
