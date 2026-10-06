# Fodder Watch: Earth Observation That Turns Restricted-Crop Detections Into Enforceable Case Files

*VERTICAL-DRIVEN ARCHITECTURES · AGRICULTURE & EARTH OBSERVATION · DESIGNED WITH PRAXIS · OCTOBER 2026*

An open reference architecture for an 18-month sovereign earth observation service that screens every parcel for restricted green fodder and unlicensed cultivation for an agriculture and earth observation operator in Saudi Arabia: eight source systems, a fourteen-object ontology, and two open-weight models on one 48 GB inference node inside the Kingdom, with every case verified by a named inspector.

For the enforcement and compliance lead of an agriculture and earth observation operator in Saudi Arabia, their regional superintendents and inspectors, and the geospatial, data and platform engineers who would build and run it.

**Made with:** [Praxis](https://codeatoms.ai/praxis/) (design) and [Hyper Ontology](https://codeatoms.ai/hyper-ontology/) (living system). Load the object model with the [hyper-ontology loader](../hyper-ontology-py/): `hyper-ontology show restricted-crop-monitoring-saudi-arabia`.

**Canonical page:** https://codeatoms.ai/restricted-crop-monitoring-saudi-arabia/
**Paper:** [PDF](paper/fodder-watch-restricted-crop-earth-observation-saudi-arabia.pdf) · [HTML](paper/fodder-watch-restricted-crop-earth-observation-saudi-arabia.html) · [Word](paper/fodder-watch-restricted-crop-earth-observation-saudi-arabia.docx) · [Appendix A, what ownership costs over three years](paper/appendix_a_cost.md)
**DOI:** [10.5281/zenodo.23186675](https://doi.org/10.5281/zenodo.23186675)
**Licence:** CC BY 4.0. Cite the DOI on the release, or the canonical page.

## Abstract

*A Violation Should Be Seen From Orbit, Not at the Fuel Pump*

Which holdings are growing restricted green fodder or cultivating beyond the area their license allows, how many hectares are involved, and which of the three violator classes each holding falls into, so that penalties and the fuel and electricity conditions can be applied? The operator cannot answer this today because the national register, the crop license records and rounds of satellite and aerial imagery live in systems that never meet, and photo-interpretation reviews a sample of scenes rather than the whole sedimentary shelf.

The design joins eight named source systems, from the national agricultural register and license records to the mirrored Sentinel-2, Sentinel-1 and Landsat archive, through one integration adapter family onto an ontology of fourteen objects, which five services and two inspector-facing surfaces read. Two open-weight

models, an RF-DETR fine-tune and a zero-shot Chronos-2, run on a 48 GB GPU class inside the operator's in-Kingdom facility, screening every parcel and triaging so only the flagged minority reaches a human inspector, ending in verified case files and GIS layers published to the operator's own enforcement channel.

The paper opens with the industry problem and the join failure, then gives the constraints, the stack, the object model, ingestion, inference placement and the models and licenses in Part II. Part III gives the rollout in three phases with their gates and the ownership of everything the design builds. Part IV closes with how Praxis contextualized and reasoned the design, tracing every choice back to what was recorded.

## The object model

`ontology/objects.json` holds the 14 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology.

| Kind | Objects |
|---|---|
| site | Farm holding, Centre pivot / cultivated field |
| actor | Farm enterprise / large farmer |
| record | Crop licence (wheat / seasonal fodder), Water source (well) use licence, Green fodder ban control, Agricultural fuel / electricity service condition record, Imagery tasking order, Processed imagery product, Violation case file |
| event | Satellite image capture, Restricted-crop detection flag |
| person | Field inspector |
| system | Restricted-crop classifier |

## The model and equipment register

`register/models.csv`, read from the paper's Table 4: every model, its licence and weight, every hardware class and sizing rule.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on Praxis, CodeNinja's platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
