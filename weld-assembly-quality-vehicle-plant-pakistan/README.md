# Physical AI System Design for Weld and Assembly Quality in a Vehicle Plant in Pakistan

*VERTICAL-DRIVEN ARCHITECTURES · DISCRETE MANUFACTURING & AUTOMOTIVE · DESIGNED WITH CODENINJA PRAXIS · NOVEMBER 2026*

A physical AI system design for weld and assembly quality in a vehicle plant in Pakistan, published under the series title Discrete Manufacturing & Automotive Watch: One Living Picture of the Operation. A sovereign reference architecture for a vehicle assembly company starting production of new energy vehicles: triggered cameras and edge units at the body shop, trim and underbody station exits checking every body, one governed plant ontology of sixteen objects over six read only sources, three agents that named inspectors and managers confirm, and GLM 5.3 self hosted on one node in the plant's own server room.

**Canonical page:** https://codeatoms.ai/weld-assembly-quality-vehicle-plant-pakistan/
**Paper:** [PDF](paper/weld-assembly-quality-vehicle-plant-pakistan.pdf) · [HTML](paper/weld-assembly-quality-vehicle-plant-pakistan.html) · [Word](paper/weld-assembly-quality-vehicle-plant-pakistan.docx) · [Appendix A, what ownership costs over three years](paper/appendix_a_cost.md)
**DOI:** assigned on release.

**Licence:** CC BY 4.0. Cite the DOI on the release, or the canonical page.

## At a glance

| Part | The design |
|---|---|
| Sources | Six read only systems of record, entering through one integration adapter family (Debezium change data capture from the MES and QMS databases, collectors for controller and rig logs, one way transfer out of a network zone) that owns a contract per source, resolves identity once with lineage and stamps every event from the PTP grandmaster: the manufacturing execution system, the robot and weld controller logs, the torque tool controllers, the end of line test rigs, the quality management system and the supplier parts receiving records; the single write path back is the approved record into the quality management system |
| Object model | 16 typed objects with 13 typed links, from the vehicle, body, station and operation through the weld point, sealer bead, torque result, part and supplier lot to the defect, defect class, repair ticket, audit finding and corrective action, with the body shop quality inspector and the quality manager; identity from the body number and MES genealogy rather than tracking, published as JSON for reuse |
| Models | GLM 5.3 (GLM-5.3 bespoke licence, 753B at FP8) as the agentic work surface and the ontology's maintainer, drafting weld checks, supplier lot traces and cited conversational answers; D-FINE (Apache-2.0) at INT8 on the edge NPU for weld spot, part, clip, connector and fastener presence; Anomalib 2.7.0 (Apache-2.0) for sealer bead anomalies fitted on the plant's own good beads; BGE-M3 (MIT) at FP16 for retrieval and citations; no third party model service, nothing trained into weights |
| Compute | Three tiers in the plant: fanless industrial edge units on an octa core 6 TOPS NPU SoC rated minus 40 to 85 C beside 5 MP global shutter GigE Vision cameras at five station exits; one air cooled 48 GB PCIe inference server in the plant server room; one node of eight 141 GB HBM GPUs (1,128 GB) holding 753 GB of FP8 weights with the 1.2 planning factor, 904 GB. Pakistan sits in Country Groups D:2, D:3 and D:4, so the US export licence determination for the accelerator classes is a phase one checkpoint before anything is quoted |
| Rollout | One phase carrying 15 items across six workstreams and covering the 18 requirements, closed by a gate, never a date: trim and underbody presence checking running on every body and vehicle that passes; every check in shadow mode beside the manual inspection it supports; baseline frozen from the end of line test rigs; false flag budget under 10 per inspector per shift; paint shop and end of line cameras held for the phase after, gated on phase one evidence |
| Three-year cost | About 572,000 US dollars to own the node for three years (a range of 542,000 to 610,000: server, support and power at the national industrial tariff), against about 751,000 to rent the same eight cards on the deepest three year commitment in AWS Asia Pacific (Mumbai), so ownership costs about three quarters of it, and about 2.00 million on demand, against which ownership costs a little over a quarter. Renting is a price reference only, because AWS lists no region in Pakistan and every rented option would carry images, process data and the parent's standards out of the plant (Appendix A) |
| Human control | Agents check and draft, people decide, by name: the body shop quality inspector confirms or dismisses every flagged weld point or missing clip at the station terminal, the quality manager approves every repair ticket draft and opens every corrective action; no agent stops a line or rejects a supplier lot, and every confirmation and dismissal is kept as memory the next check reads |

**Made with.** Reasoned on [CodeNinja Praxis](https://codeatoms.ai/praxis/), the CodeNinja Atoms platform for designing physical AI systems. The object model imports into [Hyper Ontology](https://codeatoms.ai/hyper-ontology/), which turns it into a living system. Load it with the [hyper-ontology loader](../hyper-ontology-py/): `hyper-ontology show weld-assembly-quality-vehicle-plant-pakistan`. Both are in beta; access by request.

## Abstract

*The Answer Already Exists in the Systems the Operation Runs*

A [physical AI system design](https://codeatoms.ai/physical-ai-system-design/) for weld and assembly quality in a vehicle plant in Pakistan starts from the auditor's question: when the parent's auditors ask why a body shop defect rate rose on a given day, the plant rebuilds the answer by hand across the robot logs, the torque records and the inspection sheets.

The design reads 6 source systems through 1 adapter family into one object model of 16 objects, runs 6 services over it and opens 5 surfaces to the people who decide, with 4 models placed where the data is. This design puts triggered cameras and edge units on the CodeNinja on device AI stack at the body shop, trim and underbody station exits, checks every body against the weld point list and the sealer bead with Apache-2.0 detectors the operator owns, and lands every result in a governed plant ontology built from the MES, controller logs, torque tools, end of line rigs, QMS and receiving records. Agents draft, people decide, memory improves the next check without training, and the whole thing, including GLM 5.3 on one 141 GB class node in the plant's own server room, stays inside the plant network in Pakistan.

The paper covers the operation and the problem its systems cannot answer, the constraints, the stack, the object model, ingestion, inference placement, the models and their licenses, the rollout and its proof, ownership, and finally how Praxis contextualized and reasoned the design.

## The object model

`ontology/objects.json` holds the 16 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology.

| Kind | Objects |
|---|---|
| site | Station |
| asset | Vehicle, Body, Part |
| event | Operation, Defect |
| measure | Weld point, Sealer bead, Torque result |
| record | Supplier lot, Defect class, Repair ticket, Audit finding, Corrective action |
| actor | Body shop quality inspector, Quality manager |

## The model and equipment register

`register/models.csv`, read from the paper's model and equipment register (Table 4), the architecture table (Table 7) and chapters 7 and 8: every model, its licence and weight, every hardware class and sizing rule, and the patterns the design stands on.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on Praxis, CodeNinja's platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
