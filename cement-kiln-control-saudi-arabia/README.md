# A Self-Improving AI System for Cement Kiln Control in Saudi Arabia

*VERTICAL-DRIVEN ARCHITECTURES · HEAVY INDUSTRY & CONSTRUCTION · DESIGNED WITH CODENINJA PRAXIS · NOVEMBER 2026*

Heavy Industry & Construction Watch: One Living Picture of the Operation. A [self-improving AI system](https://codeatoms.ai/self-improving-ai-system/) for one kiln line at a cement company in Saudi Arabia: a governed ontology of sixteen objects over the plant's seven systems of record, three named agents that draft causes, setpoints and handovers for operators and supervisors to confirm, memory that compounds every confirmed outcome without ever changing weights, and GLM 5.3 self hosted on one node in the company's own data centre in the country.

**Canonical page:** https://codeatoms.ai/cement-kiln-control-saudi-arabia/
**Paper:** [PDF](paper/cement-kiln-control-saudi-arabia.pdf) · [HTML](paper/cement-kiln-control-saudi-arabia.html) · [Word](paper/cement-kiln-control-saudi-arabia.docx) · [Appendix A, what ownership costs over three years](paper/appendix_a_cost.md)
**DOI:** assigned on release.

**Licence:** CC BY 4.0. Cite the DOI on the release, or the canonical page.

## At a glance

| Part | The design |
|---|---|
| Sources | Seven read only systems of record, entering through three adapter families (integration, telemetry and ops systems) behind a one-way boundary that stamps every record with its provenance and receipt time: the distributed control system and its historian, the laboratory system, the fuel and alternative fuel feed records, the kiln shell scanner, the maintenance management system, the shift log and the production reporting system; the platform never writes to the control system |
| Object model | 16 typed objects, from the kiln line, equipment, tag and setpoint through the recipe, raw meal lot, fuel lot and clinker sample to the upset, operator action, shell scan, work order and shift, with the control room operator, shift supervisor and production manager, held as a projection over the systems of record and published as JSON for reuse |
| Models | GLM 5.3 (GLM-5.3 bespoke licence, 753B at FP8) for cause drafting, handover drafting, ontology maintenance and the command centre's cited answers; Chronos-2 (Apache-2.0) forecasting the stable band on the streaming tags to raise the drift trigger; BGE-M3 (MIT) embedding past upsets, shift logs and maintenance history in Arabic and English; no third party model service, nothing trained into weights |
| Compute | One node of eight 141 GB HBM accelerators (1,128 GB) in the company's own data centre in Saudi Arabia, holding 753 GB of FP8 weights with a 1.2 planning factor, 904 GB; a plant GPU server of one or two PCIe cards for the forecast and embedding models; a sealed fanless industrial edge unit at the plant. The node is a 4A090 class item for a D:3 and D:4 destination, so an export licence determination comes before the order, with two 80 GB class nodes as the fallback shape |
| Rollout | Two phases carrying 17 scope items (16 and 1) against 18 requirements, each closed by a gate, never a date: one kiln line at one plant for one quarter, whose gate stands the setpoint agent up with drafts flowing to a named approver and a controlled on and off comparison of thermal energy per tonne of clinker; then extension to further lines and plants on that evidence; the sector precedent that read 4.1 percent in a continuous month and 2.2 percent under a controlled comparison sets the honesty bar |
| Three-year cost | About 570,000 US dollars to own the frontier node for three years (a range of 542,000 to 594,000: server, support and power at the national commercial electricity tariff), against about 751,000 to rent the same eight cards on the deepest three year commitment in AWS Middle East (UAE), so ownership costs about three quarters of it, and about 2.00 million on demand, against which ownership costs a little over a quarter. Renting is a price reference only, because AWS lists no Saudi region on the day read and every rented option would carry plant data across the border (Appendix A) |
| Human control | Agents draft and people decide, by name: the control room operator confirms the upset agent's cause and recovery draft, the shift supervisor approves the setpoint agent's draft, and the production manager confirms the shift agent's handover and its energy and quality comparison; drafts run in shadow before anyone approves them, and every confirmation or rejection is kept as the memory the next shift reads |

**Made with.** Reasoned on [CodeNinja Praxis](https://codeatoms.ai/praxis/), the CodeNinja Atoms platform for designing physical AI systems. The object model imports into [Hyper Ontology](https://codeatoms.ai/hyper-ontology/), which turns it into a living system. Load it with the [hyper-ontology loader](../hyper-ontology-py/): `hyper-ontology show cement-kiln-control-saudi-arabia`. Both are in beta; access by request.

## Abstract

*The Answer Already Exists in the Systems the Operation Runs*

A self-improving AI system for kiln control at a cement company in Saudi Arabia: open weight models on the company's own hardware in the country, reading its systems of record and getting better at advising the kiln every shift from what operators confirm worked, on one governed ontology of the kiln line, its equipment, tags, setpoints, recipes, raw meal lots, fuel lots, clinker samples, upsets, operator actions, shell scans, work orders and shifts, each fact tied to its source system.

The design reads 10 source systems through 3 adapter families into one object model of 16 objects, runs 7 services over it and opens 3 surfaces to the people who decide, with 3 models placed where the data is. A sovereign, read-only advisory system for one kiln line: a governed ontology over the plant's seven systems of record, three named agents that draft causes, setpoints and handovers for people to confirm, and memory that compounds confirmed outcomes without ever changing weights. Phase one runs one line for one quarter against a measured baseline, gated on an on/off comparison in the units the national energy efficiency program itself collects.

The paper covers the operation and the problem its systems cannot answer, the constraints, the stack, the object model, ingestion, inference placement, the models and their licenses, the rollout and its proof, ownership, and finally how Praxis contextualized and reasoned the design.

## The object model

`ontology/objects.json` holds the 16 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology.

| Kind | Objects |
|---|---|
| site | Kiln line |
| asset | Equipment |
| measure | Tag, Setpoint, Shell scan |
| record | Recipe, Raw meal lot, Fuel lot, Clinker sample and quality result, Work order, Shift |
| event | Upset, Operator action |
| actor | Control room operator, Shift supervisor, Production manager |

## The model and equipment register

`register/models.csv`, read from the paper's model and equipment register (Table 4) and chapters 7 and 8: every model, its licence and weight, every hardware class and sizing rule, and the patterns the design stands on.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on Praxis, CodeNinja's platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
