# Industrial AI Reference Architecture for an Engine MRO Shop Floor in the United States

*VERTICAL-DRIVEN ARCHITECTURES · AVIATION & AEROSPACE MANUFACTURING · DESIGNED WITH CODENINJA PRAXIS · NOVEMBER 2026*

An [industrial AI reference architecture](https://codeatoms.ai/industrial-ai-reference-architecture/) for an aircraft engine maintenance, repair and overhaul shop in the United States: Critical Path Watch, one governed model of shop flow over seven systems of record, agents that draft the critical path, the workscope cascade and the vendor chase while named planners decide, a memory of confirmed outcomes that improves the next plan without training, and GLM 5.3 self hosted on one node of the shop's own hardware with nothing about the airlines' engines leaving its control.

**Canonical page:** https://codeatoms.ai/engine-mro-shop-us/
**Paper:** [PDF](paper/engine-mro-shop-us.pdf) · [HTML](paper/engine-mro-shop-us.html) · [Word](paper/engine-mro-shop-us.docx) · [Appendix A, what ownership costs over three years](paper/appendix_a_cost.md)
**DOI:** pending

**Licence:** CC BY 4.0. Cite the DOI on the release, or the canonical page.

## At a glance

| Part | The design |
|---|---|
| Sources | Seven read only systems of record, entering through one integration adapter family (one adapter per source, change data capture and interface reads, event by event) that carries the source system, record identifier and capture position onto every object: the maintenance and engineering system, the parts tracking and inventory system, the vendor repair order system, the material purchasing system, the inspection findings records, the test cell data and the customer workscope and contract terms; no cameras, no edge tier, and the single write path back into a system of record runs after a named approval with an audit trail |
| Object model | 15 typed objects with 16 typed links, from the engine, customer, workscope and gate through the module, part, inspection finding and disposition to the repair order, vendor, purchase order, material lot, build slot, test and release, with serialized part instances as the spine and US person access control fenced as a property on the objects, published as JSON for reuse |
| Models | GLM 5.3 open weights (GLM-5.3 bespoke licence permitting commercial use, fine tuning and redistribution; 753 billion parameters, 376 GB at INT4) for the agentic work surface, the cited conversational interface and ontology maintenance; gpt-oss-120b and BGE-M3 set aside as open work because their sources were not returned; no third party model service, nothing trained into weights |
| Compute | One node of eight 80 GB HBM class GPUs (640 GB) on vLLM in the shop's own server room on a segregated VLAN, holding 376 GB of INT4 weights with the 1.2 planning factor (452 GB) and 264 GB of headroom for concurrent planner sessions; Apache Kafka 4.4, Hyper Ontology, Harbor and Prometheus, Grafana and Loki beside it; no edge tier because nothing on the floor is sensed |
| Rollout | Two phases carrying 16 scope items (14 and 2), each closed by a gate, never a date: one engine type and its induction line for one quarter, gated on the governed shop ontology build proved on a week of production data and exited on a simulated high pressure turbine blade set failure drafted the same day; then the engine type extension path and the sovereign exit rehearsal; 14 requirements traced to items, headline measure engines released on the promised date with a nominal of 85 percent |
| Three-year cost | About 407,000 US dollars to own the node for three years (a range of 370,000 to 422,000: server, support and power at the national average commercial price), against about 448,000 to rent the same eight H100 cards on the deepest three year commitment in AWS US East (N. Virginia), a Compute Savings Plan all upfront, so ownership costs about nine tenths of it; about 600,000 on the three year EC2 Instance Savings Plan all upfront, about two thirds; and about 1.45 million on demand, a little over a quarter. Renting is a price reference only, because every rented option would carry customer, engine and vendor data and export controlled technical data out of the shop (Appendix A) |
| Human control | Agents draft and people decide, by name: the engine planner confirms the critical path draft, the customer program manager approves the workscope cascade and the airline notification, the materials manager approves the vendor chase or the alternative, and the quality queue checks record integrity; the disagreement path is built before the agreement path, agreement rates are logged, and every confirmed outcome is kept as memory the next plan reads |

**Made with.** Reasoned on [CodeNinja Praxis](https://codeatoms.ai/praxis/), the CodeNinja Atoms platform for designing physical AI systems. The object model imports into [Hyper Ontology](https://codeatoms.ai/hyper-ontology/), which turns it into a living system. Load it with the [hyper-ontology loader](../hyper-ontology-py/): `hyper-ontology show engine-mro-shop-us`. Both are in beta; access by request.

## Abstract

*Industrial AI in Engine Maintenance Must See the Critical Path*

An industrial AI reference architecture for an engine maintenance, repair and overhaul shop in the United States has to answer one concrete question that industrial AI in engine maintenance, arriving as dashboards, has not: which of the engines in work will miss its promised release date, and which part, vendor repair or build slot is holding it. It has not been answered because the answer is split across the maintenance and engineering system, the parts tracking system, the vendor repair order system and the workscope contract, and those four meet only when the date is missed; shops of this class carry hundreds of engines in work and tens of thousands of parts in flow at any time, in a year when turnaround on narrowbody engines runs to six months or more, and the fix for a part that goes late at the same vendor every quarter lives in a retiring planner's memory rather than in any system.

The design reads seven systems of record through one integration adapter family into a governed object model of fifteen objects joined by typed links, runs seven services, among them a critical path agent that drafts and a memory that improves the next plan without training, and presents four surfaces: a command center, an approval queue, a vendor queue and a quality queue. One model carries the agentic work surface and ontology maintenance, GLM 5.3 open weights, a frontier class model at 753 billion parameters, held by the shop itself under a licence that permits commercial use, fine tuning and redistribution, and served at INT4 on the shop's own hardware, one node of eight GPUs of the 80 GB HBM class, where 376 GB of weights leave room for the key value cache and activations; there is no edge tier and no third party model service, because the shop floor is watched through records rather than cameras.

The paper covers the industry problem and the join failure across the shop's systems, the constraints that shape the design, the stack from records to surfaces, the fifteen object model, the adapter tier and event backbone, the placement of inference on the shop's own servers, the model and its licence, the two phase rollout with its gates and measurements, who owns what the design builds, and finally how Praxis contextualized and reasoned the design, so that any choice in it can be traced back to the recorded reading that justified it.

## The object model

`ontology/objects.json` holds the 15 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology.

| Kind | Objects |
|---|---|
| asset | Engine, Module, Part, Material lot |
| record | Workscope, Gate, Disposition, Repair order, Purchase order, Build slot, Release |
| event | Inspection finding, Test |
| actor | Customer, Vendor |

## The model and equipment register

`register/models.csv`, read from the paper's model and equipment register (Table 4), the architecture table (Table 7) and chapters 6, 7 and 8: the one model held and the two set aside, the hardware class and sizing rule, the backbone, registry and observability products, and the patterns the design stands on.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on Praxis, CodeNinja's platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
