# At a glance · An open-source agriculture data dashboard in Pakistan

**What this is.** An open reference architecture for system design in physical AI: one dashboard that joins a farm's live sensor feeds, its historical datasets and a big data and analytics repository into one object model, so any farm, crop cycle or season can be drilled into, exported and reported on under role-based access. It is written for the program director of a federal agriculture productivity pilot and for the data, integration and platform engineers who would build it. The operator is described by class, never by name.

**The answer in numbers.**

| Part | The design |
|---|---|
| Sources joined | 3: the site sensor feeds, the historical datasets and the big data and analytics repository, through 2 adapter families |
| Object model | 12 typed objects, from farm site and field to crop cycle, sensor reading and alert, published as JSON for reuse |
| Models | None: the analytics are deterministic aggregations, drill-down and reporting |
| Stack | Open-source PostgreSQL with PostGIS on the operator's own servers; source code and full intellectual property handed over |
| Three-year cost | No hardware line to price: the cost is the integration and software work (Appendix A) |
| Human control | Every alert is acknowledged by a named user under a role the operator assigns |

**Reuse it.** The object model, the model register and the figures are free to reuse under CC BY 4.0. Cite as DOI https://doi.org/10.5281/zenodo.23186671.

**Made with.** Reasoned on [Praxis](https://codeatoms.ai/praxis/), CodeNinja's platform for designing physical AI systems. The object model imports into [Hyper Ontology](https://codeatoms.ai/hyper-ontology/), which turns it into a living system. Both are in beta; access by request.
