# Sovereign AI Reference Architectures for a Remote Mine on a Satellite Link in Pakistan

*VERTICAL-DRIVEN ARCHITECTURES · MINING · DESIGNED WITH CODENINJA PRAXIS · NOVEMBER 2026*

Sovereign AI reference architectures for a remote copper and gold mine on a satellite link in Pakistan (Mining Watch: One Living Picture of the Operation): one governed site ontology of fifteen objects over read mirrors of seven systems of record, three drafting agents that named supervisors approve, memory that survives crew rotation, and GLM 5.3 self hosted on one node inside the fence that answers with the link down. This design is one of CodeNinja's [sovereign AI reference architectures](https://codeatoms.ai/sovereign-ai-reference-architectures/).

**Canonical page:** https://codeatoms.ai/remote-mine-satellite-pakistan/
**Paper:** [PDF](paper/remote-mine-satellite-pakistan.pdf) · [HTML](paper/remote-mine-satellite-pakistan.html) · [Word](paper/remote-mine-satellite-pakistan.docx) · [Appendix A, what ownership costs over three years](paper/appendix_a_cost.md)
**DOI:** assigned at release.

**Licence:** CC BY 4.0. Cite the DOI on the release, or the canonical page.

## At a glance

| Part | The design |
|---|---|
| Sources | Seven read only systems of record on site, entering through two adapter families (integration for record extracts, telemetry for tag and telematics streams) over an event backbone that stamps every fact with its source system and the time the site last saw it: project controls, construction management and permit to work, equipment telematics and maintenance, camp and workforce management, health, safety and environment, supply and logistics tracking, and the site historian for power and water; the corporate estate abroad is the eighth source, a sync target and never a dependency; nothing writes into a system of record |
| Object model | 15 typed objects with 13 typed links, from the construction area and pad through the work package, permit, crew and worker to the equipment unit, fault, work order, part, convoy and consignment, with camp occupancy, incident and utility tag, each anchored in exactly one system of record and published as JSON for reuse |
| Models | GLM 5.3 (GLM-5.3 bespoke licence, 753B at FP8) for the three drafting agents (permits, equipment, convoys), the command centre's cited conversational interface and ontology maintenance; BGE-M3 (MIT) for retrieval over permits, work orders, faults and maintenance histories; no third party model service, nothing trained into weights |
| Compute | One node of eight 141 GB HBM cards (1,128 GB) in the site server room on the mine's own power, holding 753 GB of FP8 weights with 375 GB beside them; BGE-M3 on the same node; no edge tier, the rugged tablets in the field run nothing. The node is a 4A090 class item for a D:2, D:3 and D:4 destination, so an export licence determination naming the end user is the first phase one checkpoint, with an in country colocation fallback if the path closes |
| Rollout | One phase of 17 scope items across six workstreams, closed by a gate, never a date: a simulated link drop day with the satellite egress severed, on which the pilot area resolves a dozer fault, a permit clash and a late convoy entirely from site memory; one construction area and its heavy fleet for one quarter; four baselines measured from the site's own records before any claim (permit conflicts found at the pad, equipment hours lost to parts not on site, convoy days late, and the time a new supervisor needs to answer what is open on a pad) |
| Three-year cost | About 572,000 US dollars to own the node for three years (a range of 548,000 to 597,000: server, support and power at the national industrial tariff as a reference, since the mine generates its own power), against about 751,000 to rent the same eight cards on the deepest three year commitment in AWS Asia Pacific (Mumbai), so ownership costs about three quarters of it, and about 2.00 million on demand, against which ownership costs a little over a quarter. Renting is a price reference only: AWS lists no region in Pakistan, and no rented node answers with the link down (Appendix A) |
| Human control | Agents draft and supervisors decide, by name: the area supervisor confirms the permit agent's shift start draft of open permits, conflicts and expired isolations per pad, the maintenance planner approves the equipment agent's work order and parts check, and the logistics lead approves the convoy agent's re sequencing; no agent issues a permit, closes an isolation or dispatches a convoy; every confirmation is recorded against the owning system's record and kept as memory the next shift reads |

**Made with.** Reasoned on [CodeNinja Praxis](https://codeatoms.ai/praxis/), the CodeNinja Atoms platform for designing physical AI systems. The object model imports into [Hyper Ontology](https://codeatoms.ai/hyper-ontology/), which turns it into a living system. Load it with the [hyper-ontology loader](../hyper-ontology-py/): `hyper-ontology show remote-mine-satellite-pakistan`. Both are in beta; access by request.

## Abstract

*The Answer Already Exists in the Systems the Operation Runs*

Sovereign AI reference architectures for a remote copper and gold mine on a satellite link in Pakistan: the operator's corporate systems live in data centers abroad and reach the site over that link, so when the link degrades the site works blind, with permits issued on paper, equipment faults logged after the shift and a convoy's position known when it arrives.

The design reads 8 source systems through 2 adapter families into one object model of 15 objects, runs 8 services over it and opens 4 surfaces to the people who decide, with 2 models placed where the data is. A sovereign system of context for a remote copper and gold mine in Pakistan: one governed ontology over read mirrors of the site's seven systems of record, three drafting agents (permits, equipment, convoys) whose drafts named people approve, memory that survives crew rotation, and a command center that runs fully on site through satellite outages with GLM 5.3 self hosted on one 141 GB class node. Phase one is one construction area and its heavy fleet for one quarter, gated on the site answering a simulated link-drop day, on which a dozer fault, a permit clash and a late convoy arrive together, entirely from its own memory.

The paper covers the operation and the problem its systems cannot answer, the constraints, the stack, the object model, ingestion, inference placement, the models and their licenses, the rollout and its proof, ownership, and finally how Praxis contextualized and reasoned the design.

## The object model

`ontology/objects.json` holds the 15 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology.

| Kind | Objects |
|---|---|
| site | Construction area, Pad |
| record | Work package, Permit, Work order |
| actor | Crew, Worker |
| asset | Equipment unit, Convoy |
| event | Fault, Incident |
| material | Part, Consignment |
| measure | Camp occupancy, Utility tag |

## The model and equipment register

`register/models.csv`, read from the paper's model and equipment register (Table 4) and chapters 4, 6, 7 and 8: every model, its licence and weight, every hardware class and sizing rule, the backbone, registry and identity choices, and the patterns the design stands on.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on Praxis, CodeNinja's platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
