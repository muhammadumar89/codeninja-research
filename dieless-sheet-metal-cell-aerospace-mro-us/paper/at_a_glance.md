# At a glance · Dieless robotic sheet metal for an aircraft MRO facility in the United States

**What this is.** An open reference architecture for system design in physical AI: a vendor-independent dieless robotic sheet metal cell that takes an aircraft structural part from CAD to a certified, serialized part with collision-free springback-compensated toolpaths, in-process metrology and a per-serial traceability record, wholly inside the facility's own boundary with no vendor cloud. It is written for the maintenance lead accountable for structural spare production and for the manufacturing, robotics, controls, metrology and platform engineers who would build and run it. The operator is described by class, never by name.

**The answer in numbers.**

| Part | The design |
|---|---|
| Sources | Six, read-only through two adapter families: CAD import, the operator's own sensors, third-party software interfaces, the production systems, the quality records system and cell control telemetry over MTConnect |
| Object model | 14 typed objects held as Asset Administration Shells, from sheet blank, robot arm and stylus through toolpath program and metrology scan to nonconformance and work order, one joined record per serialized part, published as JSON for reuse |
| Models | Anomalib 2.7.0 (Apache-2.0) for surface and geometric anomaly detection on formed panels, and Chronos-Bolt (Apache-2.0) for force-trace baselines, both on the cell edge box; no language model committed |
| Compute | A fanless industrial inference computer in the cell panel and an eight-card 48 GB PCIe inference server in the facility, joined one way across a hardware data diode; an OCP Time Card grandmaster orders every stream |
| Rollout | Three phases carrying 18 items: a validation prototype on sacrificial blanks under a written kill criterion, the production cell, then a steel and titanium limits investigation before any production claim |
| Three-year cost | About 202,000 to 220,000 US dollars to own the priced classes over three years, the scanner and the server most of it; the two compute tiers alone cost about two fifths of the deepest three-year AWS commitment for eight L40S cards, which the offline requirement rules out anyway (Appendix A) |
| Human control | A named facility operator releases every program, an authorized person dispositions every nonconformance, and the certified safety function admits no software verdict as a control input |

**Reuse it.** The object model, the model register and the figures are free to reuse under CC BY 4.0. Cite as DOI https://doi.org/10.5281/zenodo.23308095.

**Made with.** Reasoned on [CodeNinja Praxis](https://codeatoms.ai/praxis/), the CodeNinja Atoms platform for designing physical AI systems. The object model imports into [Hyper Ontology](https://codeatoms.ai/hyper-ontology/), which turns it into a living system. Both are in beta; access by request.
