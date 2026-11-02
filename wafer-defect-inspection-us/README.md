# Physical AI System Design for Wafer Defect Inspection in the United States

*VERTICAL-DRIVEN ARCHITECTURES · SEMICONDUCTORS · DESIGNED WITH CODENINJA PRAXIS · NOVEMBER 2026*

Fab Defect Watch: Ontologies for Semiconductor Defect Classification at the Edge. An open reference architecture for physical AI system design in semiconductors in the United States: defect images classified on sealed edge units at the inspection tools, one governed fab ontology of sixteen objects over five systems of record, GLM 5.3 open weights self hosted inside the fab, and named engineers confirming every class and approving every hold.

**Canonical page:** https://codeatoms.ai/wafer-defect-inspection-us/
**DOI:** https://doi.org/10.5281/zenodo.23889770
**Paper:** [PDF](paper/wafer-defect-inspection-us.pdf) · [HTML](paper/wafer-defect-inspection-us.html) · [Word](paper/wafer-defect-inspection-us.docx) · [Appendix A, what ownership costs over three years](paper/appendix_a_cost.md)
**Licence:** CC BY 4.0. Cite the DOI on the release, or the canonical page.

## At a glance

| Part | The design |
|---|---|
| Sources | Five systems of record and the tool interfaces at the edge, eight sources in all, entering through one integration adapter family over SECS/GEM, GEM300 and EDA interfaces onto an Apache Kafka (KRaft) backbone: the manufacturing execution system, the yield management system, the inspection tools' own defect databases, the equipment data collection system and the statistical process control system, all read only; the one write back is an approved hold or disposition through the manufacturing execution system interface |
| Object model | 16 typed objects with 12 typed links, from the wafer and lot through the process step, tool, chamber, recipe and inspection run to the defect, defect class, wafer map signature, excursion, hold and corrective action, with the defect review engineer, yield engineer and process owner, published as JSON for reuse |
| Models | GLM 5.3 open weights for the work surface, self hosted inside the fab: reasoning for the three named agents and cited answers, unsized until a verified register row stands; an unsupervised anomaly model fitted on the fab's own normal images on the CodeNinja on-device AI stack at the tool; no third party model service, nothing trained into weights |
| Compute | At the tool, one octa core 6 TOPS NPU edge SoC unit per inspection tool group in a fanless sealed cleanroom enclosure, held to a 60 percent headroom gate. In the fab's server room, the 141 GB HBM GPU class, eight GPUs per node, one node for GLM 5.3 at FP8. Nothing crosses the fab perimeter |
| Rollout | Two phases carrying 18 scope items (17, then 1): one etch module for one quarter, gated on classification quality on the fab's own images, joins proven on one real week of production data and a named approval on every hold, measured as time from excursion onset to hold against a nominal of 4.0 hours; 1 of 1 requirement covered |
| Three-year cost | About 576,000 US dollars to own the reasoning node for three years (a range of 551,000 to 623,000: server, support and power at the United States average industrial or commercial price), against about 625,000 to rent the same eight cards on the deepest three year commitment in AWS US East (N. Virginia), so ownership costs about nine tenths of it, and about 1.66 million on demand, against which ownership costs about a third. Renting is a price reference only, because every rented option would carry fab data out of the fab (Appendix A) |
| Human control | Agents draft and engineers decide: the defect review engineer confirms each proposed defect class, the yield engineer approves every drafted hold, and the process owner approves every release, rework or scrap; a hold placed or released without a recorded named approval is refused in code and audited per hold, and every supporting engineer is screened for deemed export before access |

**Made with.** Reasoned on [CodeNinja Praxis](https://codeatoms.ai/praxis/), the CodeNinja Atoms platform for designing physical AI systems. The object model imports into [Hyper Ontology](https://codeatoms.ai/hyper-ontology/), which turns it into a living system. Load it with the [hyper-ontology loader](../hyper-ontology-py/): `hyper-ontology show wafer-defect-inspection-us`. Both are in beta; access by request.

## Abstract

*Ontologies for Semiconductor Defect Classification Decide Yield*

When a wafer map shows a ring signature, physical AI system design has to give a wafer fab in the United States one answer: which chamber drifted, when it started, and which lots it touched before anyone noticed. Ontologies for semiconductor defect classification are how the industry names the missing piece, because no single system of record can walk from a defect image to a lot, a tool, a chamber, a recipe and a control limit in one trace. The manufacturing execution system knows the lot and the hold, the yield management system knows the signature, the inspection tools' own databases hold the images, the equipment data collection system holds the chamber telemetry, and the statistical process control system holds the limits, but the join that the question demands is done by engineers reading screens, and the cost shows up as hours between excursion onset and hold.

The design runs wholly inside the fab boundary on the operator's own hardware. Sealed fanless edge units next to the optical inspection and electron microscope review tools classify defect images as they arrive on the CodeNinja on-device AI stack; one adapter family joins eight sources into one governed fab ontology of sixteen objects, from wafer, lot and process step through tool, chamber, recipe, inspection run, defect, defect class and wafer map signature to excursion, hold, corrective action and the three approving roles; seven services and five surfaces carry three named agents, a classification agent drafting on a review image, an excursion agent drafting a hold when a wafer map signature crosses a control limit, and a disposition agent drafting release, rework or scrap for a held lot, each confirmed by a defect review engineer, a yield engineer or a process owner; and the model register holds zero verified weights, with reasoning intended for GLM 5.3 open weights self hosted inside the fab once a verified row stands in the register.

The paper covers the industry problem and the join failure across five systems of record, the constraints that sovereignty and the tools-first rule impose, the layered stack, the sixteen object model and its typed links, ingestion through one adapter family, where inference runs and what happens when the link or the update path fails, the honestly open model register, the two phase rollout with its item counts, gates and the excursion to hold time it measures, who owns what the system produces, and it closes with how Praxis contextualized and reasoned the design.

Readers weighing industrial ontology examples will find every object and typed link in chapter 5.

## The object model

`ontology/objects.json` holds the 16 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology.

| Kind | Objects |
|---|---|
| material | Wafer, Lot |
| event | Process Step, Inspection Run, Defect, Excursion |
| asset | Tool, Chamber |
| record | Recipe, Defect Class, Hold, Corrective Action |
| measure | Wafer Map Signature |
| actor | Defect Review Engineer, Yield Engineer, Process Owner |

## The model and equipment register

`register/models.csv`, read from the paper's model and equipment register (Table 4) and chapters 3, 7 and 8: every model, every hardware class and the sizing rule.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on Praxis, CodeNinja's platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
