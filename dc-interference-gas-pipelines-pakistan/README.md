# Corridor Guard: Validated DC Interference Assessment and Mitigation for Every Gas Pipeline Near the Electrode Station

*VERTICAL-DRIVEN ARCHITECTURES · OIL & GAS · DESIGNED WITH PRAXIS · OCTOBER 2026*

A validation-first study design that digitises, field-verifies and models the interference a high-voltage direct current electrode system imposes on the operator's transmission and distribution gas pipelines in Pakistan, and turns it into a safe-distance assessment, a priced mitigation strategy and a re-runnable model handed over on the operator's own hardware.

For the Corrosion Control lead accountable for pipeline integrity, the cathodic protection and DC interference engineers, and the data, GIS and modelling engineers who would build and run it.

**Canonical page:** https://codeatoms.ai/dc-interference-gas-pipelines-pakistan/
**Paper:** [PDF](paper/corridor-guard-dc-interference-assessment-gas-pipelines-pakistan.pdf) · [HTML](paper/corridor-guard-dc-interference-assessment-gas-pipelines-pakistan.html) · [Word](paper/corridor-guard-dc-interference-assessment-gas-pipelines-pakistan.docx) · [Appendix A, what ownership costs over three years](paper/appendix_a_cost.md)
**Licence:** CC BY 4.0. Cite the DOI on the release, or the canonical page.

## Abstract

*A Safe Distance Must Be Argued From Validated Records*

The operation needs one answer argued end to end: how much direct current from a nearby high-voltage direct current electrode station shifts the pipe-to-soil potential of its transmission and distribution gas pipelines, where that shift pushes cathodic protection outside its criterion, and what mitigation with what bill of quantities restores it. It cannot be answered today because the corridor's evidence is scattered across scanned survey sheets, coating reports, layouts and soil investigations with no recorded provenance, the supplied soil figure is a single quoted value for ground the records themselves describe

as layered and variable, and no calibrated interference model exists, while the governing terms make every data error the contractor's cost and release payment only after the final report.

Corridor Guard designs the work as a validation-first, three-phase study on a deliberately small stack: two named sources, the operator's own data package and the direct current system's stated configuration, entering through one integration adapter family into a governed validation register of fifteen objects with provenance carried on every attribute, served by six services and read through three surfaces, with one open-weight document parser doing the digitisation. Everything runs inside the operator's own estate on a single site-tier server: the parser turns scans into keyed values, the interference model is built and calibrated in validated commercial software against field readings, and the re-runnable model package is handed over on the operator's own hardware with no copy left outside the boundary.

The paper sets out the problem and the corridor scenario, the join failure across the supplied records, the four constraints the governing clauses impose, the stack, the fifteen-object model, ingestion through the adapter tier, inference placement inside the estate, the model and its license, the three gated phases with their item counts and exit criteria, ownership of everything the study produces, and finally how Praxis contextualized and reasoned the design.

## The object model

`ontology/objects.json` holds the 15 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology.

| Kind | Objects |
|---|---|
| asset | The 8-inch line, The 10-inch loop line, The original anode bed, TEG Unit, Anode 1 (MP-3.40), Anode 2 (MP-6.97), Insulating Joints PFIJ, The electrode station, CP Test Point |
| system | HVDC Transmission System, Cathodic Protection System |
| document | Soil Investigation Report, Detail of Available Data for Assessment |
| record | DC Interference Assessment, Mitigation Measure |

## The model and equipment register

`register/models.csv`, read from the paper's Table 4: every model, its licence and weight, every hardware class and sizing rule.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on Praxis, CodeNinja's platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
