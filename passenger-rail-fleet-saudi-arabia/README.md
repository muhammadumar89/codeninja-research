# Sovereign AI Reference Architectures for Passenger Rail Fleet Maintenance in Saudi Arabia

*VERTICAL-DRIVEN ARCHITECTURES · RAIL & TRANSPORTATION · DESIGNED WITH CODENINJA PRAXIS · NOVEMBER 2026*

Fleet Condition Command: Industrial AI in Rail Maintenance the Operator Owns. One of the [sovereign AI reference architectures](https://codeatoms.ai/sovereign-ai-reference-architectures/) in the series: a system design for a national passenger and freight railway in Saudi Arabia that joins two builders' vocabularies into one governed model of the fleet, drafts depot and diagram decisions for named engineers to approve, and computes availability cleanly, on the operator's own hardware and weights inside its own boundary.

**Canonical page:** https://codeatoms.ai/passenger-rail-fleet-saudi-arabia/
**Paper:** [PDF](paper/passenger-rail-fleet-saudi-arabia.pdf) · [HTML](paper/passenger-rail-fleet-saudi-arabia.html) · [Word](paper/passenger-rail-fleet-saudi-arabia.docx) · [Appendix A, what ownership costs over three years](paper/appendix_a_cost.md)
**DOI:** to be minted on release

**Licence:** CC BY 4.0. Cite the DOI on the release, or the canonical page.

## At a glance

| Part | The design |
|---|---|
| Sources | Ten sources read in place, never written: eight systems of record of operator provenance (the builder's remote monitoring platform, the on board diagnostic logs, the maintenance management system, the depot work orders, the timetable and train running system, the track condition monitoring service, the spare parts stock system and the passenger incident log) and two depot camera feeds, entering through two adapter families (integration adapters over documented APIs, telemetry adapters for streams) that stamp provenance class, keep each builder's own vocabulary and carry per source clock offsets |
| Object model | 14 typed objects with their typed links, from the trainset, vehicle and serial numbered component through the diagnostic event, fault, work order, part, depot slot, diagram, journey, delay and incident to the two objects the design itself writes, the condition case and the agent draft; a projection over the builders' platforms and the operator's systems, never a copy, published as JSON for reuse |
| Models | A frontier class of open weights, self hosted for sovereignty, for the command centre's conversational reasoning, judging agent drafts and drafting diagram swaps; GLM 5.3 at FP8 is the named candidate (about 756 GB of weights on one node with roughly 280 GB of KV cache ceiling) and no row is committed until a person verifies it live; nothing is trained, fine tuned or distilled; no third party model service |
| Compute | One inference tier, the operator's existing in country data centre, on the 141 GB HBM class with eight GPUs per node (about 1,038 GB usable); one node holds the named candidate; no on vehicle compute and no edge tier in phase one; the node is ordered at engagement start because GPU lead time into the country is the one dependency that can idle every workstream, and Saudi Arabia is a D:3 and D:4 destination for which a 4A090 class node needs a US export licence (Appendix A) |
| Rollout | Two phases carrying 16 scope items (15 and 1), each earned at a gate, never a date: one route for one quarter, whose exit gate is the fleet ontology of trainset and work order bound to a week of real extracts from both builders with the joins proven before any agent is built, then passenger fleet rollout with the new builder's vocabulary as an onboarding item; baselines written at signature; the simulated traction converter drift cased, swapped out of its diagram and repaired before it fails in the desert |
| Three-year cost | About 570,000 US dollars to own the named node for three years (a range of 542,000 to 594,000: server, support and power at the national commercial electricity tariff), against about 751,000 to rent the same eight cards on the deepest three year commitment in AWS Middle East (UAE), so ownership costs about three quarters of it, and about 2.00 million on demand, against which ownership costs a little over a quarter. Renting is a price reference only, because AWS lists no Saudi region on the day read and every rented option would carry fleet data across the border (Appendix A) |
| Human control | Agents draft and people decide, by name: every condition case carries an approving fleet engineer and a recommended depot slot, every agent draft carries an approval state and a citation set, nothing reaches a depot slot or a diagram swap without a named person deciding, and the platform stays advisory and non vital, outside the safety case and inside the governance; every confirmed cause and accepted swap is kept as memory the next case reads |

**Made with.** Reasoned on [CodeNinja Praxis](https://codeatoms.ai/praxis/), the CodeNinja Atoms platform for designing physical AI systems. The object model imports into [Hyper Ontology](https://codeatoms.ai/hyper-ontology/), which turns it into a living system. Load it with the [hyper-ontology loader](../hyper-ontology-py/): `hyper-ontology show passenger-rail-fleet-saudi-arabia`. Both are in beta; access by request.

## Abstract

*A Drifting Converter Should Be Swapped Before the Desert Decides*

Sovereign AI reference architectures for passenger rail fleet maintenance in Saudi Arabia come down to one question this operation cannot answer today: which vehicle on the fleet is drifting toward failure, and what should be done about it before the timetable sends it back onto a long desert route. The operator's present estate cannot answer that question, because condition data arrives from the builder's platform in the builder's words, the depot closes work orders in its own, and the two meet only in a meeting, so a door fault seen on board three times this month is never joined to the work order that was closed last month for the same door. A locomotive whose traction converter is drifting is scheduled by the timetable rather than by its condition and fails in the desert; when a train is late, the control room and the depot each tell a different story; and the maintenance included terms of the new trainset contract will be measured against availability figures the operation cannot compute cleanly today.

The design reads ten named source systems through two adapter families into a governed ontology of fourteen objects joined by typed links; six services carry the work to four surfaces, the command centre's condition view, the diagram swap approval surface, the month end availability pack and the fleet engineer's approval surface; the model register carries no verified model row from this run, so the frontier class open weights behind the conversational work surface are open work to be verified live and then sized, and in phase one all compute runs centrally in the operator's existing in country data centre, with GPU capacity of the 141 GB HBM class procured against measured load and nothing about the trains leaving the operator's network.

The paper covers the industry problem and the join failure across the systems of record; the constraints, the layered stack, the fourteen object model, ingestion through adapters, the placement of inference inside the sovereign boundary, and the model and licence register; the two phase rollout with its item counts, gates, measurements and failure modes, and who owns what the design builds; and it closes with the chapter showing how Praxis contextualized and reasoned the design.

## The object model

`ontology/objects.json` holds the 14 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology.

| Kind | Objects |
|---|---|
| asset | Trainset, Vehicle, Component |
| event | Diagnostic event, Journey, Delay |
| record | Fault, Work order, Depot slot, Diagram, Incident, Condition case |
| material | Part |
| document | Agent draft |

## The model and equipment register

`register/models.csv`, read from the paper's model and equipment register (Table 4), the stack tables (Tables 3 and 7) and chapters 6 to 8: the model class and the named candidate, every hardware class and sizing rule, the sensing, the platform components and the patterns the design stands on.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on Praxis, CodeNinja's platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
