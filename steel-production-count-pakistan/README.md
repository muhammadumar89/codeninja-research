# OCTOBER 2026 Steel Count Ledger: Independently Counted Production for Every Steel Mill

*V E R T I C A L - D R I V E N A R C H I T E C T U R E S · H E AV Y I N D U S T R Y & C O N S T R U C T I O N · D E S I G N E D W I T H P R A X I S ·*

in Pakistan An ontology-anchored production monitoring system that counts billets, ingots, rebars and girders at the point they are made, publishes the counts into one operator-owned record, and lets revenue officers reconcile counted against declared production for a heavy industry and construction operator in Pakistan.

For the director of the operator's audit unit, the revenue field officers and audit leads who decide discrepancies, and the edge, vision and platform engineers who would build and run it.


**Made with:** [Praxis](https://codeatoms.ai/praxis/) (design) and [Hyper Ontology](https://codeatoms.ai/hyper-ontology/) (living system). Load the object model with the [hyper-ontology loader](../hyper-ontology-py/): `hyper-ontology show steel-production-count-pakistan`.

**Canonical page:** https://codeatoms.ai/steel-production-count-pakistan/
**Paper:** [PDF](paper/steel-count-ledger-production-monitoring-steel-mills-pakistan.pdf) · [HTML](paper/steel-count-ledger-production-monitoring-steel-mills-pakistan.html) · [Word](paper/steel-count-ledger-production-monitoring-steel-mills-pakistan.docx) · [Appendix A, what ownership costs over three years](paper/appendix_a_cost.md)
**DOI:** [10.5281/zenodo.23126563](https://doi.org/10.5281/zenodo.23126563) (all versions: [10.5281/zenodo.23126562](https://doi.org/10.5281/zenodo.23126562))
**Licence:** CC BY 4.0. Cite the DOI on the release, or the canonical page.

## Abstract

*A Production Count Should Be Observed at the Point of Making, Not Taken on Trust*

How much steel did each melting and re-rolling unit in Pakistan actually produce this shift, this week, this filing period? The bid behind this design exists because the question cannot be answered today: production figures reach the authority as declarations from the mills themselves, the sector's structural gaps in tax compliance and revenue leakage are documented in the requirement's own background, and no independent instrumentation stands between the caster and the tax return. Once a bundle of rebars leaves the cooling bed, the only count that exists is the one the producer volunteers.

The design is an ontology-anchored production monitoring system built around three sources, one adapter family, fourteen objects, seven services, three surfaces and three models. IP66 cameras and

GPU industrial PCs at every installation point count product on edge detection models the operator owns, with tracker models keeping one billet from counting twice; counts publish near-real-time over VPN through a hardware data diode into a single operator-owned production model; laser counting heads and the weighbridge feed serve as alternative sensing and acceptance ground truth; and revenue officers and audit teams reconcile counted against declared production on a workbench and an agentic work surface, the latter served by a frontier open-weight model in a dedicated data center because the GPU class it needs is export controlled for Pakistan.

The paper opens with the industry problem and the join failure across mill-side systems, states the constraints the bid and the mill floor impose, then walks the layered stack, the fourteen-object model, ingestion through adapters and the event backbone, inference placement from the installation point to the data center, and the models and licenses that decide what the operator can own. Part three sets out the rollout in three phases with item counts and exit gates, ownership of what the design builds, and the paper closes with the chapter on how Praxis contextualized and reasoned the design.

## The object model

`ontology/objects.json` holds the 14 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology.

| Kind | Objects |
|---|---|
| site | Steel melting and re-rolling unit |
| asset | Installation point, Industrial PC |
| event | Production count event, Tamper or offline alert |
| material | Product type (Billets, Ingots, Rebars, Girders) |
| record | Declared production, Discrepancy case, Product calibration record, Weighbridge record |
| actor | Revenue field officer, Audit team |
| person | Steel mill staff |
| measure | Daily uptime record |

## The model and equipment register

`register/models.csv`, read from the paper's Table 4: every model, its licence and weight, every hardware class and sizing rule.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on Praxis, CodeNinja's platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
