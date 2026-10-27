# Silicon Ledger: Ontologies for Semiconductor Design From Specification to Tapeout in Saudi Arabia

*VERTICAL-DRIVEN ARCHITECTURES · SEMICONDUCTORS · DESIGNED WITH CODENINJA PRAXIS · OCTOBER 2026*

An open reference architecture for physical AI system design in semiconductors in Saudi Arabia: one governed, self-hosted model of a fabless chip design company's design record, sixteen objects over five source systems, three open-weight models on one node of the company's own hardware, and engineers approving every check.

**Canonical page:** https://codeatoms.ai/chip-design-ontology-saudi-arabia/
**DOI:** https://doi.org/10.5281/zenodo.23693146
**Paper:** [PDF](paper/chip-design-ontology-saudi-arabia.pdf) · [HTML](paper/chip-design-ontology-saudi-arabia.html) · [Word](paper/chip-design-ontology-saudi-arabia.docx) · [Appendix A, what ownership costs over three years](paper/appendix_a_cost.md)
**Licence:** CC BY 4.0. Cite the DOI on the release, or the canonical page.

## At a glance

| Part | The design |
|---|---|
| Sources | Five systems, entering through one integration adapter family that stamps every fact with the tool, file and revision it came from: the shared specification drives, the requirements site, the version control system, the bug records and the vendor design tool suites, all read only; the one write is the approval-gated path into version control |
| Object model | 16 typed objects with 13 typed links, from the specification section and requirement through the design block, interface, signal and design assumption to the verification check, test, coverage result, bug, waiver and design revision, with the engineer, verification lead, expert lesson and foundry handoff, published as JSON for reuse |
| Models | GLM 5.3 (bespoke licence, 753B at FP8) for the agentic work surface: the spec agent, the check agent and cited answers; BGE-M3 (MIT) for embedding and retrieval so every answer cites its record; PaddleOCR-VL 1.6 (Apache-2.0) for specification parsing at ingestion; no third party model service, nothing trained into weights |
| Compute | One node of eight 141 GB HBM cards (1,128 GB) in the company's own server room, holding 753 GB of FP8 weights with a 1.2 planning factor, 904 GB, at roughly ten kilowatts; no edge estate. The node is a 4A090 item for a D:4 destination, so a BIS licence determination is a phase one checkpoint, and the platform runs on the company's existing hardware until it lands. Nothing crosses outward |
| Rollout | Two phases carrying 18 scope items (15, then 3) behind one gate: one design block and one specification revision cycle governed from specification to tapeout, with one interface requirement change traced to everything that implements it and everything that proves it; all six stated requirements covered |
| Three-year cost | About 569,000 US dollars to own the node for three years (a range of 541,000 to 594,000: server, support and power at the Saudi commercial electricity tariff), against about 751,000 to rent the same eight cards on the deepest three-year commitment in AWS Middle East (UAE), so ownership costs about three quarters of it, and about 2.00 million on demand, against which ownership costs a little over a quarter. Renting is a price reference only, because AWS lists no Saudi region on the day read and every rented option would carry design records across the border (Appendix A) |
| Human control | Agents draft and engineers decide: an engineer confirms each extracted requirement before it is used, with the rejection rate as a phase one gate; the verification lead approves every drafted check before it enters the regression, escalating to the senior verification expert after five working days; a reconciliation job after every sync cycle flags stale impact lists and keeps them out of citations |

**Made with.** Reasoned on [CodeNinja Praxis](https://codeatoms.ai/praxis/), the CodeNinja Atoms platform for designing physical AI systems. The object model imports into [Hyper Ontology](https://codeatoms.ai/hyper-ontology/), which turns it into a living system. Load it with the [hyper-ontology loader](../hyper-ontology-py/): `hyper-ontology show chip-design-ontology-saudi-arabia`. Both are in beta; access by request.

## Abstract

*Ontologies for Semiconductor Design Should Trace Proof, Not Just Text*

Ontologies for semiconductor design exist to answer one question that a fabless chip design company in Saudi Arabia cannot answer today: which requirements carry proof, and what does one interface change on one block actually touch? The operator's record is scattered across shared specification drives, a requirements site, a version control system, a bug tracker and the vendor design tool suites, and no one of them joins the rest, so traceability is rebuilt by hand at every revision while a chip specification runs to hundreds of pages and keeps changing; the gaps surface late, as bugs found after tapeout rather than as checks that never existed, in an industry where trade secret theft and research security enforcement have shown what design data is worth (Reuters 2020; Bloomberg 2020).

The design joins five source systems, the shared specification drives, the version control system, the requirements site, the bug records and the vendor design tool suites, through one adapter family of integration adapters into a governed model of sixteen objects carrying the tool, file and revision each fact came from, handed over by eight services onto three surfaces, a command center for the verification lead, a cited conversational interface over the design record, and a capture surface for expert reasoning; three models do the work, GLM 5.3 as the agentic work surface on one node of eight 141 GB HBM-class GPUs on the company's own hardware in Saudi Arabia, BGE-M3 for embedding and retrieval so every answer cites its record, and PaddleOCR-VL 1.6 for specification parsing at ingestion, with no third party model service anywhere in the path.

Part I states the problem and the join failure behind it; Part II sets the constraints, then the stack, the sixteen-object model, ingestion through adapters, inference placement and the models with their licenses; Part III gives the two-phase rollout with its item counts, gates, failure modes and the ownership of what is built; and Part IV closes with how Praxis contextualized and reasoned the design, so that every choice in this paper traces back to recorded reading.

Readers weighing industrial ontology examples will find every object and typed link in chapter 5.

## The object model

`ontology/objects.json` holds the 16 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology.

| Kind | Objects |
|---|---|
| document | Specification Section |
| record | Requirement, Design Assumption, Verification Check, Test, Bug, Waiver, Expert Lesson |
| asset | Design Block, Interface, Signal |
| event | Design Revision, Foundry Handoff |
| actor | Engineer, Verification Lead |
| measure | Coverage Result |

## The model and equipment register

`register/models.csv`, read from the paper's model and hardware register (Table 4) and chapters 7 and 8: every model, its licence and weight, every hardware class and sizing rule.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on Praxis, CodeNinja's platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
