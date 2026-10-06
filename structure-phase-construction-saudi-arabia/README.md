# OCTOBER 2026 Structure Phase Watch: Live Production, Crane and Delivery Evidence for Every

*V E R T I C A L - D R I V E N A R C H I T E C T U R E S · H E AV Y I N D U S T R Y & C O N S T R U C T I O N · D E S I G N E D W I T H P R A X I S ·*

Pour on a Construction Site One live model of the structure phase that joins precast production, crane utilisation and truck flow into a single picture, forecasts schedule slips three days out and shows safety breaches as they happen, for a heavy industry and construction operator in Saudi Arabia.

For the construction director accountable for the structure phase, the planning, crane coordination and HSE leads beside them, and the platform, data integration and computer vision engineers who would build and run it.


**Made with:** [Praxis](https://codeatoms.ai/praxis/) (design) and [Hyper Ontology](https://codeatoms.ai/hyper-ontology/) (living system). Load the object model with the [hyper-ontology loader](../hyper-ontology-py/): `hyper-ontology show structure-phase-construction-saudi-arabia`.

**Canonical page:** https://codeatoms.ai/structure-phase-construction-saudi-arabia/
**Paper:** [PDF](paper/structure-phase-watch-construction-saudi-arabia.pdf) · [HTML](paper/structure-phase-watch-construction-saudi-arabia.html) · [Word](paper/structure-phase-watch-construction-saudi-arabia.docx) · [Appendix A, what ownership costs over three years](paper/appendix_a_cost.md)
**DOI:** [10.5281/zenodo.23126448](https://doi.org/10.5281/zenodo.23126448) (all versions: [10.5281/zenodo.23126447](https://doi.org/10.5281/zenodo.23126447))
**Licence:** CC BY 4.0. Cite the DOI on the release, or the canonical page.

## Abstract

*A Slip Should Be Forecast Three Days Out, Not Found at the Thursday Meeting*

Why is the structure phase slipping, and where is the struck by and dropped load exposure that causes both delay and injury? Today the joint venture cannot answer either question while it can still act: precast curing state lives in a casting bed spreadsheet, planned lifts live in a separate Excel schedule, truck movements live on paper gate logs, and the owner's Primavera P6 baseline lives with the planning team, so a slip is discovered at the weekly look ahead meeting a week after it begins, and near misses reach HSE on incident forms filed the next day.

The design joins twelve source systems through three adapter families into fifteen objects the joint venture owns: the precast register, the lift schedule, the gate flow, the crane logs and the owner's baseline become one live model of the structure phase, watched by edge cameras at the gate, laydown

areas and crane zones. Eight services and six surfaces run on joint venture servers in the site data room, with detection at solar powered edge nodes and reasoning in country, so a slip is forecast three days early, a breach is seen while it happens, five models carry the load, and every re-sequencing output stays a recommendation a named person approves.

The paper opens with the problem and the join failure that keeps four systems blind together, then lays out the constraints, the stack, the object model, ingestion, inference placement and the model and equipment register, before turning to rollout in three phases with gates, ownership of everything the design builds, and the closing chapter on how Praxis contextualized and reasoned the design.

## The object model

`ontology/objects.json` holds the 15 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology.

| Kind | Objects |
|---|---|
| asset | Tower crane (TC-01 to TC-14), Crawler crane (6 units), Casting bed, Precast unit, Flatbed or mixer truck |
| record | Batch ticket, P6 activity (owner baseline or fragnet), Permit to work, Incident or observation form |
| event | Gate movement, Delivery window, Lift schedule entry, Pour |
| person | Worker |
| site | Work zone (Zone A to D) |

## The model and equipment register

`register/models.csv`, read from the paper's Table 4: every model, its licence and weight, every hardware class and sizing rule.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on Praxis, CodeNinja's platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
