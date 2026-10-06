# At a glance · Radar tank gauge integrity for a fuel terminal in Pakistan

**What this is.** An open reference architecture for system design in physical AI: field hardware that rebuilds the signal path on three Modbus loops, and a governed inventory ontology that catches a flatlined or swapped radar gauge reading before the central inventory picture misleads anyone. It is written for the instrumentation and control lead, the location engineer and HSE supervisor, and the engineers who would build it. The operator is described by class, never by name.

**The answer in numbers.**

| Part | The design |
|---|---|
| Field scope | 13 fuel tanks on 3 Modbus RTU loops; 3 booster installations engineered from a measured signal survey inside explosion proof junction boxes |
| Sources joined | 2 named source systems, the centralized gauging host and the radar tank gauges, through 1 integration adapter family |
| Object model | 15 typed objects, with the fuel tank as the focal object, published as JSON for reuse |
| Models | None: every integrity check (stuck value, swap, distortion) is deterministic |
| Compute | Two containers on the operator's own site application server, inside its OT boundary |
| Three-year cost | No compute to price; the field equipment is priced by OEM quotation against the survey (Appendix A) |
| Human control | Every data quality event is acknowledged and resolved by a named person; the location engineer signs acceptance |

**Reuse it.** The object model, the model register and the figures are free to reuse under CC BY 4.0. Cite as DOI https://doi.org/10.5281/zenodo.23157967.

**Made with.** Reasoned on [Praxis](https://codeatoms.ai/praxis/), CodeNinja's platform for designing physical AI systems. The object model imports into [Hyper Ontology](https://codeatoms.ai/hyper-ontology/), which turns it into a living system. Both are in beta; access by request.
