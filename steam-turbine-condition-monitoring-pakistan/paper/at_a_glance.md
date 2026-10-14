# At a glance · Condition Monitoring and Diagnostics for a Combined Cycle Plant in Pakistan

**What this is.** An open reference architecture for system design in physical AI. A condition monitoring and diagnostics platform for a rehabilitated 280 MW hydrogen-cooled steam turbine generator at a combined cycle plant in Pakistan: it reads the DCS, the vibration monitoring rack and the generator protection systems through a one-way path, ranks anomalies into prescribed actions for the shift operator, and runs entirely on the operator's own hardware. It is written for the plant's condition monitoring engineer and shift operators, the contractor's warranty engineer, and the OT and data engineers who would build and run it. The operator is described by class, never by name.

**The answer in numbers.**

| Part | The design |
|---|---|
| Sources | Eight named plant systems (DCS, the 3500 vibration monitoring rack, generator condition monitoring systems, document management, the programme schedule, the plant CMMS or EAM, SCADA, outage management) entering through four adapter families over a one-way OPC UA read |
| Object model | 10 typed objects, from the steam turbine and the new generator through the vibration rack to the condition anomaly alert, work order, calibration and test records and the people who act, published as JSON for reuse |
| Models | MOMENT-1 (MIT) for zero-shot anomaly detection over vibration, hydrogen, winding and process telemetry; IBM Granite 4.2 8B (Apache-2.0) for diagnostic notes and test-report drafts; no training run |
| Compute | One 48 GB PCIe inference GPU class card on ruggedised edge servers inside the plant perimeter, a PTP grandmaster time card and a one-way egress path; no cloud, because Pakistan has no hyperscaler region |
| Rollout | Three gated phases carrying 15 scope items, with a gate of 2 false alerts per week and thresholds tuned only on channels with provable history |
| Three-year cost | About 22,500 US dollars to own the site envelope over three years (21,600 to 23,400), about the same as the deepest three-year AWS commitment for one L40S card in the UAE region, which could not keep the read one-way in any case (Appendix A) |
| Human control | The platform advises and the protection layer trips: every alert carries a prescribed action a named shift operator acknowledges, and nothing writes to the DCS |

**Reuse it.** The object model, the model register and the figures are free to reuse under CC BY 4.0. Cite as DOI https://doi.org/10.5281/zenodo.23365092.

**Made with.** Reasoned on [CodeNinja Praxis](https://codeatoms.ai/praxis/), the CodeNinja Atoms platform for designing physical AI systems. The object model imports into [Hyper Ontology](https://codeatoms.ai/hyper-ontology/), which turns it into a living system. Both are in beta; access by request.
