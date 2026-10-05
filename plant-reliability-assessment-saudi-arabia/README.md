# Reliability Atlas: A Plant Reliability Assessment Study the Operator Can Audit

*VERTICAL-DRIVEN ARCHITECTURES · ENERGY & UTILITIES · DESIGNED WITH PRAXIS · OCTOBER 2026*

An open reference architecture for a records-based reliability and availability assessment across the desalination and treatment plants of an energy and utilities operator in Saudi Arabia: three record sources joined into a thirteen-object reliability model the operator owns, auditable to ISO 55000, with no model to serve and no hardware to buy.

For the asset management and reliability lead accountable for plant availability, the plant and project managers who own the data and the decisions, and the reliability, data and platform engineers who would build and run it.

**Made with:** [Praxis](https://muhammadumar89.github.io/codeninja-research/praxis/) (design) and [Hyper Ontology](https://muhammadumar89.github.io/codeninja-research/hyper-ontology/) (living system). Load the object model with the [hyper-ontology loader](../hyper-ontology-py/): `hyper-ontology show plant-reliability-assessment-saudi-arabia`.

**Canonical page:** https://muhammadumar89.github.io/codeninja-research/plant-reliability-assessment-saudi-arabia/
**Paper:** [PDF](paper/reliability-atlas-plant-reliability-assessment-saudi-arabia.pdf) · [HTML](paper/reliability-atlas-plant-reliability-assessment-saudi-arabia.html) · [Word](paper/reliability-atlas-plant-reliability-assessment-saudi-arabia.docx) · [Appendix A, what ownership costs over three years](paper/appendix_a_cost.md)
**DOI:** [10.5281/zenodo.23157965](https://doi.org/10.5281/zenodo.23157965)
**Licence:** CC BY 4.0. Cite the DOI on the release, or the canonical page.

## Abstract

*Availability Should Be Argued From One Joined Record, Not Assembled Report by Report*

Which systems actually drive unavailability at each plant, whether installed sparing matches equipment criticality, and whether past root cause analyses (structured investigations into why major events happened) hold up under scrutiny: these are the questions the assessment must answer, and they cannot be answered today because each plant's work orders, trip history and design documents live in separate systems that were never joined, so every availability figure must be rebuilt by hand and defended without a traceable basis.

The design is a records-based reliability assessment anchored on one living reliability object model the operator owns: 3 source systems (plant CMMS, plant historian, O&M and design documentation) enter through 3 adapters (ops systems, telemetry and file and document families) into 13 objects spanning plants, trains, equipment, failure modes, work orders, downtime events, availability predictions and

targets, criticality indices, spare parts, major events, RCA reports and reliability programs, served by 5 services (data and site collection, governance, availability assessment, criticality and sparing, RCA validation) on 1 operating surface, with 0 models in the register because no inference workload is contracted; everything runs in the operator's own in-country environment, and the deliverable is an auditable study per ISO 55000 rather than a rented tool.

The paper states the problem and its documented cost, shows why no single system can answer the availability question, then works through the constraints, the layered stack, the object model, ingestion, inference placement (none is contracted), the empty model register, the phased rollout gated on the requirement's own milestones, and who owns what the study builds, closing with the Praxis chapter that traces every design choice to its recorded reasoning.

## The object model

`ontology/objects.json` holds the 13 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology.

| Kind | Objects |
|---|---|
| site | Plant |
| asset | Production train, Equipment |
| record | Failure mode, Work order, Availability prediction |
| event | Downtime event, Major event |
| measure | Availability target, Criticality index |
| document | RCA report, Reliability program |
| material | Spare part |

## The model and equipment register

`register/models.csv`, read from the paper's Table 4: every model, its licence and weight, every hardware class and sizing rule.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on Praxis, CodeNinja's platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
