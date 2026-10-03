# Sovereign HSE Watch: Predictive Risk

*VERTICAL-DRIVEN ARCHITECTURES · OIL & GAS · DESIGNED WITH PRAXIS · OCTOBER 2026*

and Early Warning on an HSE Control and Command Platform A sovereign, on-premises HSE control and command platform that unifies an oil and gas operator's fragmented safety data across Pakistan into one living ontology, turning incidents, sensors, cameras and documents into predictive early warnings, cited guidance and human-approved action.

For the HSE director, department leads and site superintendents, and the data, platform, OT and machine learning engineers who would build and run it.

**Canonical page:** https://muhammadumar89.github.io/codeninja-research/sovereign-hse-pakistan/
**Paper:** [PDF](paper/sovereign-hse-platform-pakistan-oil-and-gas.pdf) · [HTML](paper/sovereign-hse-platform-pakistan-oil-and-gas.html) · [Word](paper/sovereign-hse-platform-pakistan-oil-and-gas.docx) · [Appendix A, what ownership costs over three years](paper/appendix_a_cost.md)
**DOI:** [10.5281/zenodo.23117038](https://doi.org/10.5281/zenodo.23117038) (all versions: [10.5281/zenodo.23117037](https://doi.org/10.5281/zenodo.23117037))
**Licence:** CC BY 4.0. Cite the DOI.

## Abstract

*HSE Risk Should Be Predicted Daily, Not Reconstructed After the Incident*

The question the HSE department needs answered every day is which emerging risks are forming across its facilities and where the next incident is most likely, so that prevention happens before the event rather than investigation after it. Today it cannot be answered: HSE information sits fragmented across enterprise systems, relational databases, real-time control streams and manual files, so emerging risks surface slowly, incidents cannot be predicted from precursor signals, and lessons from past events are hard to retrieve at the moment a similar condition reappears. The design is a sovereign HSE control and command platform built entirely on the operator's own infrastructure as a system of context: eight named sources, including the ERP suite of environment, health and safety, maintenance and quality modules, the SCADA historian, the fire and gas system, the existing Vision AI camera estate, SQL databases, flat files and scanned records, and the operator's identity provider, enter only through four adapter families into one HSE ontology of twelve typed objects, above which run five services and four surfaces: anomaly detection and forecasting on site GPUs beside the cameras and historian, a cited retrieval assistant grounded in the operator's own policies and recognized standards, a control room dashboard, and an agentic work surface whose frontier reasoning model runs on one eight-GPU node inside the same Pakistani boundary, so weights, footage, embeddings and audit logs never leave it. The paper opens with the industry problem and the join failure across existing systems, then presents the design in six chapters: constraints, the layered stack, the object model, ingestion through adapters, inference placement and the latency budget, and the models and licenses that decide what the operator can own; Part III covers the three-phase rollout with its seventeen items and exit gates, and ownership of everything the design builds; it closes with the conclusion and Chapter 11, which explains how Praxis contextualized and reasoned the design.

## The object model

`ontology/objects.json` holds the 12 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology.

| Kind | Objects |
|---|---|
| asset | Operating Facility / Site, HSE Equipment |
| record | HSE Incident, Near Miss Report, Corrective Action, Inspection / Audit Record |
| document | HSE Document |
| event | Sensor Reading, Anomaly Event, Agent Recommendation |
| person | HSE Person, HSE Role |

## The model and equipment register

`register/models.csv`, read from the paper's Table 4: every model, its licence and weight, every hardware class and sizing rule.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on Praxis, CodeNinja's platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
