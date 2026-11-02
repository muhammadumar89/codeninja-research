# Sovereign AI Architecture for a Grid Control Room in Saudi Arabia

*VERTICAL-DRIVEN ARCHITECTURES · ENERGY & UTILITIES · DESIGNED WITH CODENINJA PRAXIS · NOVEMBER 2026*

Energy & Utilities Watch: One Living Picture of the Operation. A sovereign reference architecture for a national grid operator's control room in Saudi Arabia: one governed grid ontology of sixteen objects over ten read only sources, four drafting agents that named engineers and supervisors confirm, and GLM 5.3 self hosted on one node in the operator's own data center.

**Canonical page:** https://codeatoms.ai/grid-control-room-saudi-arabia/
**Paper:** [PDF](paper/grid-control-room-saudi-arabia.pdf) · [HTML](paper/grid-control-room-saudi-arabia.html) · [Word](paper/grid-control-room-saudi-arabia.docx) · [Appendix A, what ownership costs over three years](paper/appendix_a_cost.md)
**DOI:** https://doi.org/10.5281/zenodo.23889768

**Licence:** CC BY 4.0. Cite the DOI on the release, or the canonical page.

## At a glance

| Part | The design |
|---|---|
| Sources | Ten read only systems of record, entering through three adapter families (telemetry, integration and ERP) behind a one-way replicated boundary that stamps every fact with the system it came from: SCADA and EMS, the outage management system, meter data management, the asset and maintenance system, the protection settings databases, the procedure library in Arabic and English, and weather services among them; the platform never sends a control command and never writes into a system of record |
| Object model | 16 typed objects with 13 typed links, from the substation, transmission line, busbar, transformer, breaker and protection relay through the alarm and grid event to the switching program, planned outage, shift log and operating procedure, with the weather cell, connected customer, control engineer and shift supervisor, seeded by the CIM export from the EMS network model and published as JSON for reuse |
| Models | GLM 5.3 (GLM-5.3 bespoke licence, 753B at FP8) for all four drafting agents (alarm triage, switching programs, handover and the sequence of events), the command center and ontology maintenance; BGE-M3 (MIT) for Arabic and English retrieval so every answer cites its procedure or record; no third party model service, nothing trained into weights |
| Compute | One node of eight 141 GB HBM cards (1,128 GB) in the operator's own data center in the Kingdom, holding 753 GB of FP8 weights with a 1.2 planning factor, 904 GB; BGE-M3 on the platform zone's rack server class; no edge tier. The node is a 4A090 class item for a D:3 and D:4 destination, so an export licence determination naming the end user is a phase one checkpoint before the order |
| Rollout | Three phases carrying 18 scope items (15, 2 and 1), each closed by a gate, never a date: a pre-summer build and replay whose gate is the switching program drafting agent run end to end on replayed records, one regional control center live through one summer, then extension gates for every control center; baselines frozen before go-live, headline measure trip to first correct action |
| Three-year cost | About 570,000 US dollars to own the node for three years (a range of 542,000 to 594,000: server, support and power at the national commercial electricity tariff), against about 751,000 to rent the same eight cards on the deepest three year commitment in AWS Middle East (UAE), so ownership costs about three quarters of it, and about 2.00 million on demand, against which ownership costs a little over a quarter. Renting is a price reference only, because AWS lists no Saudi region on the day read and every rented option would carry grid data across the border (Appendix A) |
| Human control | Agents draft and people decide, by name: the control engineer confirms the alarm triage ranking, the shift supervisor approves every switching program draft, the incoming supervisor approves the handover, and the event analysis is prepared for the protection engineer; disagreement is a first class path faster than agreement, and every confirmation is kept as memory the next shift reads |

**Made with.** Reasoned on [CodeNinja Praxis](https://codeatoms.ai/praxis/), the CodeNinja Atoms platform for designing physical AI systems. The object model imports into [Hyper Ontology](https://codeatoms.ai/hyper-ontology/), which turns it into a living system. Load it with the [hyper-ontology loader](../hyper-ontology-py/): `hyper-ontology show grid-control-room-saudi-arabia`. Both are in beta; access by request.

## Abstract

*The Answer Already Exists in the Systems the Operation Runs*

A sovereign AI architecture for the control room of a national grid operator in Saudi Arabia: a knowledge system on one governed ontology of substations, busbars, lines, transformers, breakers, protection relays, alarms, events, switching programs, planned outages, procedures, shift logs, connected customers and weather cells, each fact tied to its source system.

The design reads 10 source systems through 3 adapter families into one object model of 16 objects, runs 8 services over it and opens 4 surfaces to the people who decide, with 2 models placed where the data is. A sovereign system of context for one regional control center: a governed grid ontology built from the network model and the systems of record behind a one-way replicated boundary, four drafting agents for alarm triage, switching programs, handover and the sequence of events, whose drafts control engineers and supervisors confirm and approve, GLM 5.3 self hosted on one 141 GB class node in the operator's own Kingdom data center, and a summer trial gated on frozen baselines from trip to first correct action. Nothing is trained into weights, no control command is ever sent, and every fact, draft and approval traces to its source system and a named person.

The paper covers the operation and the problem its systems cannot answer, the constraints, the stack, the object model, ingestion, inference placement, the models and their licenses, the rollout and its proof, ownership, and finally how Praxis contextualized and reasoned the design.

## The object model

`ontology/objects.json` holds the 16 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology.

| Kind | Objects |
|---|---|
| site | Substation |
| asset | Transmission Line, Busbar, Transformer, Breaker, Protection Relay |
| event | Alarm, Grid Event |
| record | Switching Program, Planned Outage, Shift Log |
| document | Operating Procedure |
| measure | Weather Cell |
| actor | Connected Customer, Control Engineer, Shift Supervisor |

## The model and equipment register

`register/models.csv`, read from the paper's model and equipment register (Table 4) and chapters 7 and 8: every model, its licence and weight, every hardware class and sizing rule, and the patterns the design stands on.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on Praxis, CodeNinja's platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
