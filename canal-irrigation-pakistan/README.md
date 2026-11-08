# A Self-Improving AI System for Canal Irrigation Water Allocation in Pakistan

*VERTICAL-DRIVEN ARCHITECTURES · AGRICULTURE & EARTH OBSERVATION · DESIGNED WITH CODENINJA PRAXIS · NOVEMBER 2026*

A [self-improving AI system](https://codeatoms.ai/self-improving-ai-system/) for a provincial irrigation department in Pakistan, published as a sovereign reference architecture: Canal Share Ledger, one governed canal ontology of sixteen objects over eight read only sources, three drafting agents for shortfall, indent and dispute that named engineers confirm, memory in place of training, and open weights self hosted in the department's own circle server room.

**Canonical page:** https://codeatoms.ai/canal-irrigation-pakistan/
**Paper:** [PDF](paper/canal-irrigation-pakistan.pdf) · [HTML](paper/canal-irrigation-pakistan.html) · [Word](paper/canal-irrigation-pakistan.docx) · [Appendix A, what ownership costs over three years](paper/appendix_a_cost.md)
**DOI:** minted on release; cite the canonical page until then.

**Licence:** CC BY 4.0. Cite the DOI on the release, or the canonical page.

## At a glance

| Part | The design |
|---|---|
| Sources | Eight read only systems of record, entering through two adapter families (a telemetry adapter doing a direct historian read, and an integration adapter running an OCR pipeline with a human verification stage and a 2 percent failure gate on every batch) that stamp every item with its source, adapter, timestamp and verification state: the telemetry system, the barrage and head regulator gauge records, the indent and release ledgers, the rotation schedules per distributary, the gauge reader diaries, the complaint register and the revenue crop records among them; the platform never operates a gate and never writes into a system of record |
| Object model | 16 typed objects with 13 typed links, from the barrage, head regulator, main canal, distributary, reach, gate and outlet through the rotation, shortfall and season to the indent, release, complaint and crop area, with the telemetry reading and gauge reading as measures, built as a projection over the systems of record and published as JSON for reuse |
| Models | Frontier class open weights for the three drafting agents (shortfall, indent and dispute) and the command centre, self hosted for sovereignty; the operator names GLM 5.3 and the plan holds its FP8 arithmetic, but no weights are committed until the register verifies a model live; embedding, OCR and forecasting model classes for retrieval, handwritten Urdu and English ledgers and shortfall detection; no third party model service, nothing trained into weights |
| Compute | One node of eight 141 GB HBM cards (about 1,128 GB) in the department's circle server room, the held arithmetic for about 756 GB of FP8 weights, beside a 48 GB PCIe class site server for the small model tier; no edge tier, nothing served at a canal head. The node sits above the US advanced computing export threshold for a D:2, D:3 and D:4 destination, so the export licence determination runs first in phase one with an in country procurement route or colocation fallback named before any order |
| Rollout | Two phases carrying 17 scope items (16 and 1), each closed by a gate, never a date: a main canal prototype whose gate is the governed canal network ontology reconciled against one real week of telemetry and ledgers before any agent drafts, one main canal and its distributaries live for one cropping season, then extension to the other canals; baselines reconciled in the first month, headline measure the percent of tail outlets receiving their rotation share, nominal 85 percent, with days from shortfall onset to correction and complaints per distributary beside it |
| Three-year cost | About 636,000 US dollars to own the frontier node and the site server for three years (a range of 606,000 to 662,000: servers, support and power at the national uniform tariff), against about 773,000 to rent the same eight 141 GB cards and one 48 GB card on the deepest three year commitment in AWS Asia Pacific (Mumbai), so ownership costs about four fifths of it, and about 2.05 million on demand, against which ownership costs a little under a third. Renting is a price reference only, because AWS lists no region in Pakistan and every rented option would carry telemetry and ledgers across the border; the frontier footprint itself stands only when the register verifies a model (Appendix A) |
| Human control | Agents draft and people decide, by name: the controlling engineer confirms or rejects the drafted cause and correction before any gate instruction is drafted, the indent draft is approved before it goes to the national authority, and the dispute account is drafted from cited records for the officer to send; the gate stays a hand operation on telephone instructions, and every confirmed cause and accepted adjustment is kept as memory the next season reads |

**Made with.** Reasoned on [CodeNinja Praxis](https://codeatoms.ai/praxis/), the CodeNinja Atoms platform for designing physical AI systems. The object model imports into [Hyper Ontology](https://codeatoms.ai/hyper-ontology/), which turns it into a living system. Load it with the [hyper-ontology loader](../hyper-ontology-py/): `hyper-ontology show canal-irrigation-pakistan`. Both are in beta; access by request.

## Abstract

*A Shortfall Should Surface Within the Rotation, Not After the Complaint*

A provincial irrigation department in Pakistan needs one question answered continuously, and the self-improving AI system it asked for exists to answer it: did every distributary on the main canal receive its entitlement share this rotation, and if not, where, why and what should be done about it. It cannot answer the question today because the answer lives in pieces no system joins: telemetry measures what arrived at the main heads within minutes, the indent and release ledgers state what was asked for and released, the gauge reader diaries record what the field saw, and the complaint register is the first signal that a tail has gone short, usually after the crop is lost.

The design is a sovereign, self-improving allocation system for one main canal in its first season: eight source systems, two adapter families, a governed ontology of sixteen objects with typed links, six services, three surfaces and three drafting agents for shortfall, indent and dispute, each confirmed by a named engineer. Telemetry enters through a historian read and every paper source through an OCR pipeline with a human verification stage; together they feed one object model that is a projection over the systems of record, never a replacement of them. Improvement runs through memory rather than training: confirmed causes and accepted adjustments compound season over season, so the tails get their share more often without any model being trained on the fly. Everything runs on the operator's own hardware inside Pakistan, in the circle server room, with frontier class open weights self hosted for sovereignty; the model register stands open, with no weights committed until a model is verified live, and nothing about the canals leaves the country.

The paper covers the industry problem and the join failure across the existing systems, the constraints and scoping decisions, the stack, the object model, ingestion, inference placement, the open model register, the rollout in two phases with their gates and measurements, ownership of what the system builds, and finally how Praxis contextualized and reasoned the design.

## The object model

`ontology/objects.json` holds the 16 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology.

| Kind | Objects |
|---|---|
| asset | Barrage, Head Regulator, Reach, Gate, Outlet |
| site | Main Canal, Distributary |
| event | Rotation, Shortfall, Season |
| record | Indent, Release, Complaint, Crop Area |
| measure | Telemetry Reading, Gauge Reading |

## The model and equipment register

`register/models.csv`, read from the paper's model and equipment register (Table 4) and chapters 7 and 8: every model class and the candidate the operator names, every hardware class and sizing rule, and the patterns the design stands on. No weights are committed in the paper until the register verifies a model live, and the register says so row by row.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on Praxis, CodeNinja's platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
