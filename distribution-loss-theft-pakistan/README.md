# Sovereign AI Architecture for Distribution Loss and Theft Reduction in Pakistan

*VERTICAL-DRIVEN ARCHITECTURES · ENERGY & UTILITIES · DESIGNED WITH CODENINJA PRAXIS · NOVEMBER 2026*

A [sovereign AI architecture](https://codeatoms.ai/sovereign-ai-architecture/) for an electricity distribution company in Pakistan: one governed ontology of the network and its customers over seven read only systems of record, a loss agent, a tamper agent and a billing agent whose drafts named engineers and officers approve, and GLM 5.3 self hosted on one node in the operator's own data center. Energy & Utilities Watch: One Living Picture of the Operation.

**Canonical page:** https://codeatoms.ai/distribution-loss-theft-pakistan/
**Paper:** [PDF](paper/distribution-loss-theft-pakistan.pdf) · [HTML](paper/distribution-loss-theft-pakistan.html) · [Word](paper/distribution-loss-theft-pakistan.docx) · [Appendix A, what ownership costs over three years](paper/appendix_a_cost.md)
**DOI:** to be minted on release

**Licence:** CC BY 4.0. Cite the DOI on the release, or the canonical page.

## At a glance

| Part | The design |
|---|---|
| Sources | Seven read only systems of record, entering through one integration adapter family (a Kafka subscription for meter data, scheduled batch extracts for billing, energy audit, GIS and outage records, mapped connectors for the field app and the theft case register), each fact stamped with the system it came from: the customer information and billing system, the meter data management system, the energy audit records per feeder and transformer, the geographic information system of the network, the outage and complaint system, the meter reading and inspection app and the theft case register; the single write path out is the approved correction |
| Object model | 15 typed objects with 14 typed links, from the grid station, feeder, transformer, service connection and meter through the interval load, reading, billing account and tariff to the inspection, tamper event, theft case and recovery, with the agent draft and the approval that settles it; each anchored in one system of record and published as JSON for reuse |
| Models | GLM 5.3 (GLM-5.3 bespoke licence, 753B at FP8) for the loss, tamper and billing agents, the command center and ontology maintenance; BGE-M3 (MIT) for cited retrieval over tariff codes, meter numbers, PPC sections and inspection findings; Chronos-2 (Apache 2.0) forecasting each transformer's energy balance so the residual is the anomaly signal; no third party model service, nothing trained into weights |
| Compute | One node of eight 141 GB HBM GPUs (1,128 GB) holding 753 GB of FP8 weights with the 1.2 planning factor, 904 GB, plus one dual socket server with a 48 GB PCIe card for the embedder and the forecaster, both in an in-country sovereign data center or colocation on the operator's own hardware; no edge tier. The node is a 4A090 class item for a D:3 and D:4 destination, so the export licence determination precedes any card commitment, with a non US accelerator class held open |
| Rollout | Two phases carrying 16 scope items (15 and 1), each closed by a gate, never a date: one circle of feeders for one quarter against a measured baseline with unchanged control feeders, whose gate is the billing agent drafting corrections that land back through the recorded approval path, then the circle extension gate read on four numbers: transformer level loss, inspections per confirmed theft, case files accepted at the Grade 17 gate, and days from tamper event to inspection |
| Three-year cost | About 641,000 US dollars to own the node and the inference server for three years (a range of 615,000 to 667,000: servers, support and power at the regulator's uniform commercial tariff), against about 773,000 to rent the same cards on the deepest three year commitment in AWS Asia Pacific (Mumbai), so ownership costs about five sixths of it, and about 2.05 million on demand, against which ownership costs a little under a third. Renting is a price reference only, because AWS lists no Pakistan region and every rented option would carry customer and meter data across the border (Appendix A) |
| Human control | Agents draft and people decide, by name: the subdivision engineer approves the ranked causes and the inspection visits, the inspection officer approves the case file, the revenue officer approves the correction, and the Grade 17 officer signs the complaint; every approval carries the approver role, the officer grade, the timestamp, the artifact hash and a written reason, known answer probes police the approvers, and every confirmed cause and closed case is kept as the record the next ranking reads |

**Made with.** Reasoned on [CodeNinja Praxis](https://codeatoms.ai/praxis/), the CodeNinja Atoms platform for designing physical AI systems. The object model imports into [Hyper Ontology](https://codeatoms.ai/hyper-ontology/), which turns it into a living system. Load it with the [hyper-ontology loader](../hyper-ontology-py/): `hyper-ontology show distribution-loss-theft-pakistan`. Both are in beta; access by request.

## Abstract

*The Answer Already Exists in the Systems the Operation Runs*

A sovereign AI architecture for loss and theft reduction at an electricity distribution company in Pakistan: open weight models on the operator's own hardware in the country, reading its systems of record, with nothing about its customers leaving the country or reaching a foreign model service.

The design reads 7 source systems through 1 adapter family into one object model of 15 objects, runs 8 services over it and opens 5 surfaces to the people who decide, with 3 models placed where the data is. A sovereign, operator-owned platform that joins seven systems of record into one governed ontology of the network and its customers, computes each transformer's energy in against energy billed, and lets a loss agent, a tamper agent and a billing agent draft ranked causes, case files and corrections that subdivision engineers, inspection officers and revenue officers approve, with every confirmed outcome kept as a decision record that improves the next ranking, and every theft case ending in a court-ready Grade 17 complaint. Phase one runs one circle of feeders for one quarter against a measured baseline with unchanged control feeders, on GLM 5.3 self hosted in an in-country data center, gated on four numbers before any other circle is touched.

The paper covers the operation and the problem its systems cannot answer, the constraints, the stack, the object model, ingestion, inference placement, the models and their licenses, the rollout and its proof, ownership, and finally how Praxis contextualized and reasoned the design.

## The object model

`ontology/objects.json` holds the 15 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology.

| Kind | Objects |
|---|---|
| site | Grid Station |
| asset | Feeder, Transformer, Service Connection, Meter |
| measure | Interval Load |
| record | Reading, Billing Account, Tariff, Theft Case, Recovery |
| event | Inspection, Tamper Event, Approval |
| document | Agent Draft |

## The model and equipment register

`register/models.csv`, read from the paper's model and equipment register (Table 4) and chapters 4, 6, 7 and 8: every model, its licence and weight, every hardware class and sizing rule, the platform components, and the patterns the design stands on.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on Praxis, CodeNinja's platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
