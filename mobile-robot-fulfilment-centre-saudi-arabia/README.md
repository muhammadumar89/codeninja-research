# Physical AI System Design for a Mobile Robot Fulfilment Centre in Saudi Arabia

*VERTICAL-DRIVEN ARCHITECTURES · WAREHOUSING & INTRALOGISTICS · DESIGNED WITH CODENINJA PRAXIS · NOVEMBER 2026*

A [physical AI system design](https://codeatoms.ai/physical-ai-system-design/) for a robotic fulfilment centre in Saudi Arabia: Robot Field Watch, a sovereign system that detects people inside the robot field, fallen totes and blocked lanes on the cameras the building already runs, joins each detection to the robots, waves and shifts it affects in one governed ontology of fifteen objects over six read only systems of record, and drafts the zone slowdowns, clearance tasks and handovers that named supervisors approve, with GLM 5.3 self hosted on one node in the site data room.

**Canonical page:** https://codeatoms.ai/mobile-robot-fulfilment-centre-saudi-arabia/
**Paper:** [PDF](paper/mobile-robot-fulfilment-centre-saudi-arabia.pdf) · [HTML](paper/mobile-robot-fulfilment-centre-saudi-arabia.html) · [Word](paper/mobile-robot-fulfilment-centre-saudi-arabia.docx) · [Appendix A, what ownership costs over three years](paper/appendix_a_cost.md)
**DOI:** not yet assigned

**Licence:** CC BY 4.0. Cite the canonical page, or the DOI once the release carries one.

## At a glance

| Part | The design |
|---|---|
| Sources | Six read only systems of record, entering through one family of integration adapters (change data capture for the transactional systems, stream ingest for the cameras) that stamps every message with its source, time and adapter version: the warehouse management system, the robot fleet orchestration system, the warehouse control system, the labour management system, the incident and near miss log and the building's camera recorders; the platform never drives a robot, never issues a motion command and never writes into a system of record |
| Object model | 15 typed objects with 13 typed links, from the zone, robot, charging bay, pick station and camera view through the tote, order wave, shift, incursion and stall to the person role, near miss, corrective action, agent draft and edge unit, so a query walks from a person at a gate to the orders their presence delayed; published as JSON for reuse |
| Models | Five: RF-DETR (small) (Apache-2.0) per frame on the edge NPUs for person detection; Grounding DINO Swin-T (Apache-2.0) on evidence frames for fallen totes, cages and blocked lanes; the Roboflow trackers (Apache-2.0) with re-identification switched off; BGE-M3 (MIT) for Arabic and English cited retrieval; GLM 5.3 (GLM-5.3 bespoke licence, 753B at FP8) for the three drafting agents, ontology maintenance and the command centre; no third party model service, nothing trained into weights |
| Compute | Three tiers inside the building: camera group edge units on an industrial grade octa core SoC with a 6 TOPS NPU beside the reused cameras, counted only after a dev board measurement on the real substreams; site servers on CPU for ingest, the backbone, the ontology, the embedder and the open vocabulary classifier; and one node of eight 141 GB HBM accelerators (1,128 GB) in the site data room holding 753 GB of FP8 weights with a 1.2 planning factor, 904 GB. The node is a 4A090 class item for a D:3 and D:4 destination, so an export licence determination is a phase one procurement gate before the order |
| Rollout | Three phases carrying 16 scope items (4, 11 and 1), each closed by a gate, never a date: camera reuse verification with six gates per view and detection gates passed with recorded evidence at the worst hour; one robot field zone and its pick stations live for one quarter against the operator's own baselines (incursions per thousand robot hours, stoppage minutes per shift, time from stall to clearance, orders per labour hour); then the whole field and the next site, earned by that evidence |
| Three-year cost | About 569,000 US dollars to own the node for three years (a range of 541,000 to 594,000: server, support and power at the national commercial electricity tariff), against about 751,000 to rent the same eight cards on the deepest three year commitment in AWS Middle East (UAE), so ownership costs about three quarters of it, and about 2.00 million on demand, against which ownership costs a little over a quarter. Renting is a price reference only, because the design keeps frames, weights and memory inside the building and AWS lists no Saudi region on the day read; the edge units and site servers are not priced because the paper does not count or size them (Appendix A) |
| Human control | Agents detect and draft, people decide, by name: the shift supervisor approves the incursion agent's zone slow down and supervisor call, the fleet controller approves the stall agent's clearance task and reroute request, the operations manager confirms the shift agent's handover; execution is manual, every approval is logged with its reasoning, known answer probes measure whether approvers are rubber stamping, and people appear in the record as anonymous presence with a role, never as an identity |

**Made with.** Reasoned on [CodeNinja Praxis](https://codeatoms.ai/praxis/), the CodeNinja Atoms platform for designing physical AI systems. The object model imports into [Hyper Ontology](https://codeatoms.ai/hyper-ontology/), which turns it into a living system. Load it with the [hyper-ontology loader](../hyper-ontology-py/): `hyper-ontology show mobile-robot-fulfilment-centre-saudi-arabia`. Both are in beta; access by request.

## Abstract

*A Near Miss Should Surface in Seconds, Not in Days*

A physical AI system design for a warehousing and intralogistics operator in Saudi Arabia that runs a robotic e-commerce fulfilment centre of roughly 400,000 square feet with more than 250 autonomous mobile robots and needs one question answered continuously: who and what is inside the robot field right now, and what is that doing to throughput and safety. Today that question cannot be answered because the answer is scattered across six systems of record that were never built to join: the robot fleet orchestration system holds stall codes but not causes, the warehouse management system holds waves but not field state, and the incident and near miss log records people entering the field days after the event, if at all.

The design joins those six sources through one adapter family of read only integration adapters into a governed object model of fifteen objects, served by ten services and six surfaces, with five models: RF-DETR small detectors run on the edge units of the CodeNinja on device AI stack watching the existing cameras, Grounding DINO and BGE-M3 run on the site servers beside the ontology, motion only trackers run at the edge, and GLM 5.3 is self hosted in the site data room on one node of eight 141 GB class GPUs. Every frame, detection, weight and memory record stays inside the building, and named incursion, stall and shift agents draft zone slowdowns, clearance tasks and handovers that supervisors and the fleet controller approve and execute manually.

The paper covers the problem and the join failure, the constraints and the stack, the object model, ingestion, inference placement, and the models with their licenses, then the rollout in three phases from one zone for one quarter to the whole field and the next site, ownership of what the system produces, and finally how Praxis contextualized and reasoned the design.

## The object model

`ontology/objects.json` holds the 15 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology.

| Kind | Objects |
|---|---|
| site | Zone |
| asset | Robot, Charging Bay, Pick Station, Camera View |
| material | Tote |
| event | Order Wave, Shift, Incursion, Stall |
| actor | Person Role |
| record | Near Miss, Corrective Action, Agent Draft |
| system | Edge Unit |

## The model and equipment register

`register/models.csv`, read from the paper's model and equipment register (Table 4) and chapters 6, 7 and 8: every model, its licence and weight, every hardware class and sizing rule, the sensing, the runtimes and the patterns the design stands on.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on Praxis, CodeNinja's platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
