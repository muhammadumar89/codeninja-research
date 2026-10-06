# Field Ledger: An Open Source Agriculture Data Dashboard the Operator Fully Owns

*VERTICAL-DRIVEN ARCHITECTURES · AGRICULTURE & EARTH OBSERVATION · DESIGNED WITH PRAXIS · OCTOBER 2026*

An open reference architecture for an ontology-anchored, open-source agriculture data dashboard for an agriculture and earth observation operator in Pakistan: site sensor feeds, historical datasets and a big data and analytics repository joined into a twelve-object model in PostgreSQL with PostGIS on the operator's own servers, handed over with source code and full intellectual property.

For the program director accountable for the federal agriculture productivity pilot, the farm operations and data managers who will use the dashboard, and the data, integration and platform engineers who would build and run it.

**Made with:** [Praxis](https://codeatoms.ai/praxis/) (design) and [Hyper Ontology](https://codeatoms.ai/hyper-ontology/) (living system). Load the object model with the [hyper-ontology loader](../hyper-ontology-py/): `hyper-ontology show farm-data-dashboard-pakistan`.

**Canonical page:** https://codeatoms.ai/farm-data-dashboard-pakistan/
**Paper:** [PDF](paper/field-ledger-agriculture-data-dashboard-pakistan.pdf) · [HTML](paper/field-ledger-agriculture-data-dashboard-pakistan.html) · [Word](paper/field-ledger-agriculture-data-dashboard-pakistan.docx) · [Appendix A, what ownership costs over three years](paper/appendix_a_cost.md)
**DOI:** [10.5281/zenodo.23186671](https://doi.org/10.5281/zenodo.23186671)
**Licence:** CC BY 4.0. Cite the DOI on the release, or the canonical page.

## Abstract

*One Dashboard Cannot Answer What Three Systems Hold Apart*

The operation needs one question answered: for any farm, any crop cycle and any season, what do the sensor feeds, the historical datasets and the big data and analytics repository say together, and can a named person drill down, export and report on the answer under role-based access? Today it cannot be answered, because the live site sensor feeds, the historical datasets and the repository live in separate systems whose formats, volumes, refresh rates and interfaces are not stated anywhere in the requirement, so no single view, however well charted, can reconcile them until the integration contracts themselves are discovered.

The design is a milestone-phased, open-source agriculture data dashboard built as an ontology-first integration: three source systems, the site sensor feeds, the historical datasets and the big data and

analytics repository, enter through two adapter families into a twelve-object ontology projected as a versioned schema inside an open-source PostgreSQL database with PostGIS, running on the operator's own on-premises servers. Six services, from data integration and foundation through dashboard and analytics, security and access, operations and handover, feed two surfaces: the agriculture data food security dashboard and an administration console. No model is committed this run; the analytics are deterministic aggregations, drill-down and reporting, and every figure the dashboard shows is reproducible from the operator's own data.

The paper sets out the problem and the join failure across the three systems, then the design: the contract- constraints, the layered stack, the object model with one object in its recorded form, ingestion through the adapter tier, where aggregation runs and why the model register is honestly empty. Part III covers the four-milestone rollout with fifteen items, exit gates and failure modes, and who owns what is built. Part IV closes with how the design was produced on Praxis, so every choice traces back to what justified it.

## The object model

`ontology/objects.json` holds the 12 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology.

| Kind | Objects |
|---|---|
| site | The site, The field |
| event | Crop Cycle, Alert |
| asset | Sensor Device |
| measure | Sensor Reading |
| document | Historical Dataset, Publication, Report |
| person | Dashboard User |
| record | Access Role |
| system | Data Source Connection |

## The model and equipment register

`register/models.csv`, read from the paper's Table 4: every model, its licence and weight, every hardware class and sizing rule.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on Praxis, CodeNinja's platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
