# Baseline: One Flight of 4 Band Orthoimagery and LiDAR for Vegetation Mapping

*VERTICAL-DRIVEN ARCHITECTURES · AGRICULTURE & EARTH OBSERVATION · DESIGNED WITH PRAXIS · OCTOBER 2026*

An open reference architecture for a one-flight acquisition of 3-inch 4-band orthoimagery and USGS Quality Level 1 LiDAR over the site of an agriculture and earth observation operator in the United States, with every deliverable bound into a sixteen-object site ontology the operator's staff analyze in their own GIS.

For the operator's project manager, its GIS and stewardship leads, and the data, geospatial and platform engineers who would build and run it.

**Made with:** [Praxis](https://codeatoms.ai/praxis/) (design) and [Hyper Ontology](https://codeatoms.ai/hyper-ontology/) (living system). Load the object model with the [hyper-ontology loader](../hyper-ontology-py/): `hyper-ontology show vegetation-mapping-lidar-us`.

**Canonical page:** https://codeatoms.ai/vegetation-mapping-lidar-us/
**Paper:** [PDF](paper/baseline-orthoimagery-lidar-vegetation-mapping-us.pdf) · [HTML](paper/baseline-orthoimagery-lidar-vegetation-mapping-us.html) · [Word](paper/baseline-orthoimagery-lidar-vegetation-mapping-us.docx) · [Appendix A, what ownership costs over three years](paper/appendix_a_cost.md)
**DOI:** [10.5281/zenodo.23186673](https://doi.org/10.5281/zenodo.23186673)
**Licence:** CC BY 4.0. Cite the DOI on the release, or the canonical page.

## Abstract

*A Flight Should Leave Behind More Than Files*

The question this operation needs answered is what vegetation and terrain conditions exist across its site during the narrow summer window around 1 July, and whether every acre inside the mapping boundary was flown, processed, verified and accepted to specification. Today it cannot answer that from its own records: past aerial deliveries arrive as tile archives, point clouds and invoices that no staff member can join to units, flight missions, sensor systems or seasons, so each flight season starts with rediscovery instead of comparison, and the record of what was flown, on which day, with which sensor and at what accuracy lives in scattered documents rather than in one queryable model.

The design is a one-year, one-flight acquisition of 3-inch 4-band orthoimagery and USGS QL1 LiDAR inside the July 2025 window, handed over as publish-ready files under the agreement's terms, with every deliverable bound into a living 16-object site ontology the operator owns outright. Four named sources

enter through 2 adapter families into the object model, 5 services carry the work from boundary confirmation to handover, and 1 operating surface gives staff the joined view; 0 models are served because vegetation analysis stays with the operator's own analysts. The acquisition runs on a manned aircraft flown by the survey firm, processing runs in the survey firm's own pipeline, the object model is anchored in the operator's ArcGIS Enterprise, and nothing runs in a cloud the operator does not control.

The paper proceeds in order: the industry problem and the fixed flight window; the join failure across past deliverables; the four constraints and the scoping decisions; the stack from aircraft to archive; the 16- object model and where the human loop sits; ingestion through the 2 adapter families; inference placement, which is deliberately empty of compute; models and licenses, where the register holds zero models by choice; the 4-phase rollout with its gates and 31-requirement coverage; ownership of the record; and the Praxis chapter that traces every choice back to what justified it.

## The object model

`ontology/objects.json` holds the 16 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology.

| Kind | Objects |
|---|---|
| site | The site, The unit |
| asset | Watercourse, Dam, 4-Band Aerial Camera System, QL1 LiDAR Sensor System |
| event | Flight Mission |
| system | GNSS/IMU Georeferencing Chain |
| record | Multispectral Orthoimagery Product, Classified LAS Point Cloud, Bare-Earth and Highest-Hit DEMs |
| document | QA/QC Accuracy Report, Professional Services Agreement, Monthly Itemized Invoice |
| person | Contractor Project Manager, Operator Project Manager |

## The model and equipment register

`register/models.csv`, read from the paper's Table 4: every model, its licence and weight, every hardware class and sizing rule.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on Praxis, CodeNinja's platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
