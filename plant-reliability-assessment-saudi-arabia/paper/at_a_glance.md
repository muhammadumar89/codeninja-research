# At a glance · An auditable plant reliability assessment in Saudi Arabia

**What this is.** An open reference architecture for system design in physical AI: a records-based reliability and availability assessment that joins each plant's work orders, trip history and design documents into one reliability object model the operator owns, so every availability figure, criticality rank and root cause finding traces to its source. It is written for the asset management and reliability lead and for the reliability, data and platform engineers who would build it. The operator is described by class, never by name.

**The answer in numbers.**

| Part | The design |
|---|---|
| Sources joined | 3 record sources (plant CMMS, plant historian, O&M and design documentation) through 3 read-only adapters, as exports rather than live interfaces |
| Object model | 13 typed objects and the typed links Figure 4 draws, published as JSON for reuse |
| Models | None: the register is empty by design because no inference workload is contracted |
| Method | Availability by Monte Carlo simulation on reliability block diagrams built from each plant's own failure study, auditable to ISO 55000 |
| Compute | No hardware bought; the study runs on the operator's own in-country servers |
| Three-year cost | No hardware line to price: the cost is the assessment work itself (Appendix A) |
| Human control | Predictions are accepted only by a named reviewer and RCA reports validated only by a named engineer |

**Reuse it.** The object model, the model register and the figures are free to reuse under CC BY 4.0. Cite as DOI https://doi.org/10.5281/zenodo.23157965.

**Made with.** Reasoned on [Praxis](https://muhammadumar89.github.io/codeninja-research/praxis/), CodeNinja's platform for designing physical AI systems. The object model imports into [Hyper Ontology](https://muhammadumar89.github.io/codeninja-research/hyper-ontology/), which turns it into a living system. Both are in beta; access by request.
