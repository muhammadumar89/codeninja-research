# Loop Integrity Watch: Ending Distorted Radar Level Readings and Tank-to-Tank Swapping Across the Tank Farm

*VERTICAL-DRIVEN ARCHITECTURES · OIL & GAS · DESIGNED WITH PRAXIS · OCTOBER 2026*

An open reference architecture that restores continuous, undistorted radar tank gauge readings from thirteen fuel tanks at an oil and gas operator in Pakistan: three booster installations engineered from a signal survey on three Modbus loops, and a governed fifteen-object inventory ontology on the operator's own server that detects distortion and swapping.

For the instrumentation and control lead accountable for tank gauging, the location engineer and HSE supervisor beside them, and the instrumentation, integration and platform engineers who would build and run it.

**Made with:** [Praxis](https://codeatoms.ai/praxis/) (design) and [Hyper Ontology](https://codeatoms.ai/hyper-ontology/) (living system). Load the object model with the [hyper-ontology loader](../hyper-ontology-py/): `hyper-ontology show tank-gauge-integrity-pakistan`.

**Canonical page:** https://codeatoms.ai/tank-gauge-integrity-pakistan/
**Paper:** [PDF](paper/loop-integrity-watch-radar-tank-gauge-integrity-fuel-terminal-pakistan.pdf) · [HTML](paper/loop-integrity-watch-radar-tank-gauge-integrity-fuel-terminal-pakistan.html) · [Word](paper/loop-integrity-watch-radar-tank-gauge-integrity-fuel-terminal-pakistan.docx) · [Appendix A, what ownership costs over three years](paper/appendix_a_cost.md)
**DOI:** [10.5281/zenodo.23157967](https://doi.org/10.5281/zenodo.23157967)
**Licence:** CC BY 4.0. Cite the DOI on the release, or the canonical page.

## Abstract

*Distorted Radar Level Readings Should Fail Loudly, Not Silently*

The question the operation needs answered every hour is whether the radar tank gauge readings arriving in the central gauging host are continuous, undistorted and attributed to the right tank. Today it cannot be answered: the gauges sit on serial Modbus loops whose signal health is invisible, a flatlined gauge reads as a plausible low level, and a swapped gauge makes two tanks trade identities, so distortion and swapping surface only when the central inventory picture disagrees with physical stock, long after the field signal failed.

The design pairs field hardware with a governed ontology. Two named source systems, the centralized gauging host and the radar tank gauges, enter through one integration adapter family into an object

model of fifteen objects, served by seven services and one operating surface, with zero learned models because every integrity check is deterministic. Three booster installations, engineered from a measured signal survey inside explosion proof junction boxes, rebuild the signal path on three loops; the ontology service and integrity monitor run as two containers on the operator's own site application server, inside the operator's own OT boundary, projecting a central inventory picture over the gauging host without replacing it.

The paper proceeds from the problem and the join failure across existing systems, through the constraints the requirement itself imposes, the stack, the fifteen-object model, ingestion through the adapter, inference placement on the operator's server, an honestly empty model register, the rollout phases with their gates, and ownership of what is built, closing with the chapter on how the design was reasoned on Praxis.

## The object model

`ontology/objects.json` holds the 15 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology.

| Kind | Objects |
|---|---|
| asset | Fuel Tank, Radar Tank Gauge (RTG), RTG Communication Loop, Modbus Booster (Repeater), Explosion Proof Junction Box |
| measure | Gauge Reading |
| event | Data Quality Event |
| system | Central Inventory Picture |
| document | Loop Wiring As-Built, OEM Authorization Letter |
| record | Service Order, Warranty and Support Record, HSE Work Permit |
| person | Instrumentation Technician, Location Engineer |

## The model and equipment register

`register/models.csv`, read from the paper's Table 4: every model, its licence and weight, every hardware class and sizing rule.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on Praxis, CodeNinja's platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
