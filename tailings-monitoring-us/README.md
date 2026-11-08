# Industrial AI Reference Architecture for Tailings Storage Facility Monitoring in the United States

*VERTICAL-DRIVEN ARCHITECTURES · MINING · DESIGNED WITH CODENINJA PRAXIS · NOVEMBER 2026*

An [industrial AI reference architecture](https://codeatoms.ai/industrial-ai-reference-architecture/) for a mining company's high consequence tailings storage facility in the United States: one governed facility ontology of fifteen objects over eight read only systems of record, three drafting agents whose drafts the tailings engineer and the engineer of record confirm, and gpt-oss-120b self hosted on one node of eight 80 GB GPUs in the site server room.

**Canonical page:** https://codeatoms.ai/tailings-monitoring-us/
**Paper:** [PDF](paper/tailings-monitoring-us.pdf) · [HTML](paper/tailings-monitoring-us.html) · [Word](paper/tailings-monitoring-us.docx) · [Appendix A, what ownership costs over three years](paper/appendix_a_cost.md)
**DOI:** not yet minted

**Licence:** CC BY 4.0. Cite the canonical page, or the DOI once it is minted.

## At a glance

| Part | The design |
|---|---|
| Sources | Eight read only systems of record, entering through two adapter families (a telemetry adapter for the historian's live feed and an integration adapter for everything else) that record every source's provenance class and read direction: the instrumentation data logger network and its historian, the satellite radar deformation reports, the daily inspection app, the trigger action response plan, the engineer of record's reports and drawings, the deposition and raise plans, the water balance model and the regulator's correspondence; the platform never writes into a system of record and the existing trigger action response plan alarm path keeps firing untouched |
| Object model | 15 typed objects with 12 typed links, from the embankment section, raise and instrument through the reading, trigger level, trigger, inspection observation, deposition event, pond level and radar survey to the pattern draft, response draft and regulator submission, with the engineer of record and the water balance model, anchored on the engineer of record's section definitions and published as JSON for reuse |
| Models | gpt-oss-120b (Apache-2.0, 116.8B total and 5.1B active parameters, MXFP4) for the pattern, response and reporting agents, the work surface and ontology maintenance; Granite Tiny Time Mixers (Apache-2.0) screening readings at the edge; Chronos-2 (Apache-2.0) building trend baselines with rainfall and pond level as covariates; Nomic Embed Text v2 MoE (Apache-2.0) for retrieval with citations; all four US origin, all self hosted, nothing trained into weights |
| Compute | Three tiers on the owner's own hardware: on-device edge units at the logger network on CPU class hardware, a site tier beside the GPU node, and one node of eight 80 GB GPUs (640 GB) in the site server room holding 58.4 GB of INT4 weights with a 1.2 planning factor, 70.1 GB; the node draws about 10 kW, so a room survey precedes any order, with an in-country colocation room as the fallback; the hardware stays in the United States, so no export control question arises |
| Rollout | Three phases carrying 15 scope items (12, 2 and 1), each closed by a gate, never a date: one embankment section bound into the ontology for two quarters of record, a run phase that hardens the platform and hands over, then scale out to every section; judged against the owner's four measures (triggers explained with a confirmed context within a day, false trigger rate, days to assemble a section's story, findings raised from data the team had not seen) with a false trigger rate gate and an alert budget per engineer per shift |
| Three-year cost | About 456,000 US dollars to own the node for three years (a range of 437,000 to 496,000: server, support and power at the national average industrial and commercial prices), against about 544,000 to rent the same eight cards on the deepest three year commitment in AWS US East (N. Virginia), so ownership costs about five sixths of it, and about 1.45 million on demand, against which ownership costs a little under a third. Renting is a price reference only, because every rented option would carry instrument, survey and inspection data off the owner's hardware (Appendix A) |
| Human control | Agents draft and people decide, by name: the tailings engineer confirms every pattern draft, the responsible tailings facility engineer approves every response draft, and the engineer of record reviews the surveillance report and approves every regulator submission before it is filed; the review board and the regulator read the section stories through read only views; every confirmed pattern and its outcome is kept as memory the next trigger is read against |

**Made with.** Reasoned on [CodeNinja Praxis](https://codeatoms.ai/praxis/), the CodeNinja Atoms platform for designing physical AI systems. The object model imports into [Hyper Ontology](https://codeatoms.ai/hyper-ontology/), which turns it into a living system. Load it with the [hyper-ontology loader](../hyper-ontology-py/): `hyper-ontology show tailings-monitoring-us`. Both are in beta; access by request.

## Abstract

*One Section Deserves One Story Before Anyone Asks for It*

When an engineer types industrial AI reference architecture for mining into a search box, the question underneath is the one this operation cannot answer today: what is actually happening in one section of a high-consequence tailings embankment in the United States, and is it drifting toward a trigger? The facility holds more readings than ever and the same two engineers reading them, because a piezometer that rises slowly over a month lives in the historian without being joined to the deposition that moved the beach toward it, the rain that fell, the inclinometer two hundred feet away or the radar survey from last quarter. Thresholds in the trigger action response plan fire on single instruments, so operators learn to expect alarms and the pattern that matters hides among them, while the daily inspection app records what the operator saw in words nobody searches.

The design is a sovereign system of context for one high-consequence tailings facility: a governed ontology of 15 objects and their typed links joins 8 named source systems through 2 adapter families, so that one embankment section has one story. Six services serve 5 surfaces, from the trend and trigger view the operators watch to the read-only review view the review board reads. Three drafting agents, a pattern agent, a response agent and a reporting agent, run on gpt-oss-120b, 117B parameters at INT4, 58.4 GB of weights held on one node of eight 80 GB GPUs in the site server room, with anomaly screening on edge units at the logger network and everything on the owner's own hardware. The system improves by memory of confirmed patterns rather than by training, the existing alarm path stays untouched, and the engineer of record holds every interpretation; phase one covers one embankment section for two quarters against the owner's stated measures.

The paper covers the industry problem and the join failure across the existing systems, the constraints and scoping decisions, the layered stack from sources to surfaces, the object model with its typed links, ingestion through adapters, the placement of inference and what never crosses the boundary, the four models and the licenses that let the owner hold their weights, the rollout in three phases with their gates and failure modes, and who owns what the design builds, closing with the chapter on how Praxis contextualized and reasoned the design.

## The object model

`ontology/objects.json` holds the 15 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology.

| Kind | Objects |
|---|---|
| asset | Embankment Section, Instrument |
| event | Raise, Trigger, Deposition Event |
| measure | Reading, Pond Level |
| record | Trigger Level, Inspection Observation, Pattern Draft, Response Draft |
| document | Radar Survey, Regulator Submission |
| actor | Engineer of Record |
| system | Water Balance Model |

## The model and equipment register

`register/models.csv`, read from the paper's model and equipment register (Table 4) and chapters 6, 7 and 8: every model, its licence and weight, every hardware class and sizing rule, the stack components the design names, and the patterns the design stands on.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on Praxis, CodeNinja's platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
