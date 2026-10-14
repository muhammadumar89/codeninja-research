# Turbine Island Watch: Condition Monitoring and Diagnostics for a Combined Cycle Plant in Pakistan

*VERTICAL-DRIVEN ARCHITECTURES · ENERGY & UTILITIES · DESIGNED WITH CODENINJA PRAXIS · OCTOBER 2026*

A condition monitoring and diagnostics platform for a rehabilitated 280 MW hydrogen-cooled steam turbine generator at a combined cycle plant in Pakistan: it reads the DCS, the vibration monitoring rack and the generator protection systems through a one-way path, ranks anomalies into prescribed actions for the shift operator, and runs entirely on the operator's own hardware.

For the plant's condition monitoring engineer and shift operators, the contractor's warranty engineer, and the OT and data engineers who would build and run it.

**Canonical page:** https://codeatoms.ai/steam-turbine-condition-monitoring-pakistan/
**DOI:** https://doi.org/10.5281/zenodo.23365092
**Paper:** [PDF](paper/turbine-island-watch-steam-turbine-condition-monitoring-pakistan.pdf) · [HTML](paper/turbine-island-watch-steam-turbine-condition-monitoring-pakistan.html) · [Word](paper/turbine-island-watch-steam-turbine-condition-monitoring-pakistan.docx) · [Appendix A, what the compute costs over three years](paper/appendix_a_cost.md)
**Licence:** CC BY 4.0. Cite the DOI on the release, or the canonical page.

## At a glance

| Part | The design |
|---|---|
| Sources | Eight named plant systems (DCS, the 3500 vibration monitoring rack, generator condition monitoring systems, document management, the programme schedule, the plant CMMS or EAM, SCADA, outage management) entering through four adapter families over a one-way OPC UA read |
| Object model | 10 typed objects, from the steam turbine and the new generator through the vibration rack to the condition anomaly alert, work order, calibration and test records and the people who act, published as JSON for reuse |
| Models | MOMENT-1 (MIT) for zero-shot anomaly detection over vibration, hydrogen, winding and process telemetry; IBM Granite 4.2 8B (Apache-2.0) for diagnostic notes and test-report drafts; no training run |
| Compute | One 48 GB PCIe inference GPU class card on ruggedised edge servers inside the plant perimeter, a PTP grandmaster time card and a one-way egress path; no cloud, because Pakistan has no hyperscaler region |
| Rollout | Three gated phases carrying 15 scope items, with a gate of 2 false alerts per week and thresholds tuned only on channels with provable history |
| Three-year cost | About 22,500 US dollars to own the site envelope over three years (21,600 to 23,400), about the same as the deepest three-year AWS commitment for one L40S card in the UAE region, which could not keep the read one-way in any case (Appendix A) |
| Human control | The platform advises and the protection layer trips: every alert carries a prescribed action a named shift operator acknowledges, and nothing writes to the DCS |

**Made with.** Reasoned on CodeNinja Praxis; the object model imports into Hyper Ontology.

## The object model

`ontology/objects.json` holds the 10 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology.

| Kind | Objects |
|---|---|
| asset | Steam Turbine STG-1, New Steam Turbine Generator (280 MW, 20 kV hydrogen-cooled), 3500 Vibration Monitoring Rack |
| event | Condition Anomaly Alert |
| record | Condition Work Order, Instrument Calibration Record, Commissioning and Performance Test Record |
| actor | Shift Operator (Employer's operational personnel), Warranty Engineer (Contractor, DLP) |
| measure | STG-1 Availability (RTR-derived) |

## The model and equipment register

`register/models.csv`, read from the paper's Table 4: every model, its licence and weight, every hardware class and sizing rule.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on CodeNinja Praxis, the CodeNinja Atoms platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
