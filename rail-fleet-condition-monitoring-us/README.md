# Consist Watch: Executing the Operator's Own Fault Logic Across a 225-Car Commuter Fleet

*VERTICAL-DRIVEN ARCHITECTURES · RAIL & TRANSPORTATION · DESIGNED WITH CODENINJA PRAXIS · OCTOBER 2026*

A real time condition monitoring system for a 225-car commuter fleet in the United States: onboard modules read 64 named signals per car and execute the operator's own fault-logic table at the car, telemetry rides the car system's existing cellular routers to a contractor-hosted US cloud, and severity-ranked faults reach the mechanical desk and the yard through one fleet ontology.

For the railroad's mechanical desk and fleet engineering leads, and the embedded, telemetry and data engineers who would build and run it.

**Canonical page:** https://codeatoms.ai/rail-fleet-condition-monitoring-us/
**DOI:** https://doi.org/10.5281/zenodo.23365118
**Paper:** [PDF](paper/consist-watch-rail-fleet-condition-monitoring-us.pdf) · [HTML](paper/consist-watch-rail-fleet-condition-monitoring-us.html) · [Word](paper/consist-watch-rail-fleet-condition-monitoring-us.docx) · [Appendix A, what the compute costs over three years](paper/appendix_a_cost.md)
**Licence:** CC BY 4.0. Cite the DOI on the release, or the canonical page.

## At a glance

| Part | The design |
|---|---|
| Sources | One named system, the car system on every car (64 named signals: 32 digital at 0 to 48 VDC, 32 analog, plus a 3-axis accelerometer and GPS), entering through one integration adapter family |
| Object model | 14 typed objects, from the car, its monitoring module and its channels through the active fault, fault history and alert notification to the mechanical desk controller, the yard and the recipient groups, published as JSON for reuse |
| Models | Mistral Large 3 675B (Apache-2.0, self-hosted with vLLM) for the agentic work surface over the fleet ontology; Chronos-2 (Apache-2.0) for analog anomaly detection and seasonal trending; no training run |
| Compute | At the car, an EN 50155 and IEC 60571 module (8 by 8 by 8 inches, IP62, 24 to 48 VDC, CFR 238 materials); centrally, one 141 GB HBM GPU class node in a contractor-hosted US cloud |
| Rollout | Three phases carrying 17 scope items: a 3-car prototype, the 222-car fleet rollout, then service operations, with 13 months of history over 64 signals per car |
| Three-year cost | About 625,000 US dollars to run the eight-card node for three years on the deepest AWS commitment in US East, about three eighths of the 1.66 million on demand; the 225 modules are priced by quotation (Appendix A) |
| Human control | The module executes the operator's own fault logic verbatim; a named mechanical desk controller owns every active fault in that car's territory, and alerts go by severity to named recipient groups |

**Made with.** Reasoned on CodeNinja Praxis; the object model imports into Hyper Ontology.

## The object model

`ontology/objects.json` holds the 14 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology.

| Kind | Objects |
|---|---|
| asset | the operator's car, Onboard monitoring module, The car system |
| measure | Digital input channel, Analog input channel |
| event | Active fault |
| record | Fault history record, Alert notification, Slippery rail hotspot |
| actor | Mechanical desk controller, Notification recipient group |
| person | Yard employee |
| site | the control center mechanical desk, the yard office |

## The model and equipment register

`register/models.csv`, read from the paper's Table 4: every model, its licence and weight, every hardware class and sizing rule.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on CodeNinja Praxis, the CodeNinja Atoms platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
