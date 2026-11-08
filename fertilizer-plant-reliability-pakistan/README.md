# Industrial AI Reference Architecture for Fertilizer Plant Reliability in Pakistan

*VERTICAL-DRIVEN ARCHITECTURES · HEAVY INDUSTRY & CONSTRUCTION · DESIGNED WITH CODENINJA PRAXIS · NOVEMBER 2026*

An [industrial AI reference architecture](https://codeatoms.ai/industrial-ai-reference-architecture/) for a fertilizer manufacturer in Pakistan whose ammonia and urea complex is cycled by gas supply suspensions: one governed plant ontology of fourteen objects over eight read only systems of record and a hardware data diode, three drafting agents that named superintendents and engineers confirm, and GLM 5.3 self hosted on one node on the operator's own hardware in the country. Cycle Watch: Sovereign AI Reference Architectures for Plant Reliability in Pakistan is the generator's own title for the design.

**Canonical page:** https://codeatoms.ai/fertilizer-plant-reliability-pakistan/
**Paper:** [PDF](paper/fertilizer-plant-reliability-pakistan.pdf) · [HTML](paper/fertilizer-plant-reliability-pakistan.html) · [Word](paper/fertilizer-plant-reliability-pakistan.docx) · [Appendix A, what ownership costs over three years](paper/appendix_a_cost.md)
**DOI:** none yet; cite the canonical page.

**Licence:** CC BY 4.0. Cite the DOI once it is minted, or the canonical page.

## At a glance

| Part | The design |
|---|---|
| Sources | Twelve sources once sensing is counted: eight systems of record named by the operator and read only (the distributed control system and its historian, the maintenance management system, the inspection and corrosion monitoring records, the vibration monitoring system on the large compressors, the laboratory system, the shift log, the turnaround planning system and the gas supply notice that triggers the restart agent), the fixed camera lanes at the reformer top deck, the synthesis compressor train and the bagging plant lane, and a citation check on conversational answers; four adapter families cross the OT boundary through a hardware data diode carrying a one way file transfer, and nothing writes back |
| Object model | 14 typed objects with 10 typed links, from the process unit and equipment through the historian tag, trip, restart and thermal cycle to the work order, inspection finding, corrosion reading, vibration reading, lab result, shift log entry, turnaround task and restart plan, with Equipment as the focal object, anchored on the equipment master and refreshed shift by shift, published as JSON for reuse |
| Models | GLM 5.3 (GLM-5.3 bespoke licence, 753B at FP8) for the restart, cycle damage and turnaround drafting agents and the cited conversational interface; Chronos-2 (Apache-2.0) forecasting historian tags and thermal cycle stress residuals on the site server; BGE-M3 (MIT) embedding work orders, findings, readings and shift log entries for cited retrieval; vision models on Frigate NVR and ONNX Runtime for steam plume, flange leak, operator, scaffold and fire or smoke; no third party model service, nothing trained into weights |
| Compute | One node of eight 141 GB HBM cards (1,128 GB) on new dedicated in country hardware the operator owns, holding 753 GB of FP8 weights with a 1.2 planning factor, 904 GB; an air cooled site server inside the plant for Chronos-2, BGE-M3 and vision; a hardware data diode on the OT boundary and an OCP Time Card grandmaster for time. The node is a 4A090 class item for a destination in Country Groups D:2, D:3 and D:4, so an ECCN 3A090 and 4A090 licence determination is a phase one checkpoint before any card is quoted, with an approved in country data centre held as the fallback |
| Rollout | Five phases carrying 16 scope items (4, 3, 6, 2 and 1), each closed by a gate, never a date: Foundation and Boundary, Ontology and Memory (gate: the governed ontology of the cycled plant), Agents and Command Centre (gate: the cycle damage agent ranking stress), Phase One Pilot on the ammonia front end and the synthesis compressor train for one quarter including at least one restart, gated on four frozen baselines (hours from gas restoration to stable production, trips per restart, inspections brought forward with a confirmed finding, reliability engineer hours per failure investigation), then Extension Design to the urea unit and utilities behind its own gate; restart drafts run in shadow beside the standing written procedure until measured agreement |
| Three-year cost | About 572,000 US dollars to own the node for three years (a range of 542,000 to 610,000: server, support and power at the national industrial tariff), against about 751,000 to rent the same eight cards on the deepest three year commitment in AWS Asia Pacific (Mumbai), so ownership costs about three quarters of it, and about 2.00 million on demand, against which ownership costs a little over a quarter. Renting is a price reference only, because AWS lists no region in Pakistan and every rented option would carry plant data across the border (Appendix A) |
| Human control | Agents draft and people decide, by name: the shift superintendent confirms every step of the restart plan, the reliability engineer approves the cycle damage draft and the inspections it brings forward, the turnaround manager approves the scope additions, and report packs for the insurer's engineer leave only through a controlled export path after a disclosure review; every status change carries a named person and a timestamp, and every confirmation is kept as memory the next restart reads, never as a weight update |

**Made with.** Reasoned on [CodeNinja Praxis](https://codeatoms.ai/praxis/), the CodeNinja Atoms platform for designing physical AI systems. The object model imports into [Hyper Ontology](https://codeatoms.ai/hyper-ontology/), which turns it into a living system. Load it with the [hyper-ontology loader](../hyper-ontology-py/): `hyper-ontology show fertilizer-plant-reliability-pakistan`. Both are in beta; access by request.

## Abstract

*An Industrial AI Reference Architecture for Plant Reliability Begins With the Cycle Count*

An industrial AI reference architecture for plant reliability exists to answer one question this operation cannot answer today: what several gas suspension restarts in 2026 have done to the reformer tubes, the synthesis compressor and the seal history of a plant in Pakistan designed to run steadily between annual turnarounds. Each stop and hot restart costs days of production and stresses equipment built for continuous duty, and the hidden cost of every thermal cycle only surfaces at the turnaround, while the reliability engineers rebuild each failure's history by hand across the historian, the work orders and the inspection files, and the engineers who remember the last five restarts are retiring. The records needed to answer the question already sit in the plant's systems of record, but they are joined after the failure rather than read together before the next restart.

The design reads twelve source systems one way, through four adapter families and across a hardware data diode, into a governed object model of fourteen objects linked by typed relations; five services run three drafting agents, for restart plans, cycle damage and turnaround scope, onto three surfaces for the reliability team, with every draft confirmed by a named superintendent. Three models carry the reasoning: Chronos-2 forecasts historian tags and thermal cycle stress residuals, and BGE-M3 embeds work orders, findings and shift log entries for cited retrieval, both on the site's air cooled inference server, while GLM 5.3, a 753B parameter frontier model held at FP8, runs the command center on one node of eight 141 GB class GPUs on dedicated in country hardware, so nothing about the plant leaves the country and nothing ever writes to the control system.

The paper covers the industry problem and the join failure, the constraints that shape everything downstream, the stack, the object model, ingestion through adapters, inference placement, the models and their licenses, the rollout with its five phases, sixteen items and gates, ownership of what the design builds, and it closes with the chapter on how Praxis contextualized and reasoned this design.

## The object model

`ontology/objects.json` holds the 14 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology.

| Kind | Objects |
|---|---|
| asset | Process Unit, Equipment |
| measure | Historian Tag, Corrosion Reading, Vibration Reading |
| event | Trip, Restart, Thermal Cycle |
| record | Work Order, Inspection Finding, Lab Result, Turnaround Task |
| document | Shift Log Entry, Restart Plan |

## The model and equipment register

`register/models.csv`, read from the paper's model and equipment register (Table 4), the layer by layer architecture (Table 7) and chapters 6 and 7: every model, its licence and weight, every hardware class and sizing rule, the runtimes and platform services, and the patterns the design stands on.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on Praxis, CodeNinja's platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
