# At a glance · One flight of imagery and LiDAR for vegetation mapping in the United States

**What this is.** An open reference architecture for system design in physical AI: one summer flight of 3-inch 4-band orthoimagery and USGS Quality Level 1 LiDAR, with every tile, point cloud and elevation model bound into a site ontology, so the next season starts from a comparison instead of rediscovery. It is written for the operator's project manager, its GIS and stewardship leads, and the geospatial and data engineers who would build it. The operator is described by class, never by name.

**The answer in numbers.**

| Part | The design |
|---|---|
| Acquisition | One manned flight within a week either side of 1 July; 3-inch 4-band (red, green, blue, near infrared) orthoimagery and Quality Level 1 LiDAR at a minimum of 8 pulses per square meter |
| Sources joined | 4 named sources through 2 adapter families |
| Object model | 16 typed objects, with the flight mission as the focal object, published as JSON for reuse |
| Models | None: vegetation analysis stays with the operator's own analysts |
| Ground | The operator's ArcGIS Enterprise; nothing runs in a cloud the operator does not control |
| Three-year cost | No compute to price; the acquisition is priced by the survey firm against the operator's own task table (Appendix A) |
| Human control | The operator's project manager accepts each deliverable against the QA/QC accuracy report |

**Reuse it.** The object model, the model register and the figures are free to reuse under CC BY 4.0. Cite as DOI https://doi.org/10.5281/zenodo.23186673.

**Made with.** Reasoned on [Praxis](https://codeatoms.ai/praxis/), CodeNinja's platform for designing physical AI systems. The object model imports into [Hyper Ontology](https://codeatoms.ai/hyper-ontology/), which turns it into a living system. Both are in beta; access by request.
