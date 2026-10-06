# At a glance · Restricted-crop monitoring from orbit in Saudi Arabia

**What this is.** An open reference architecture for system design in physical AI: an 18-month earth observation service that screens every parcel for restricted green fodder and cultivation beyond the licensed area, checks each detection against the holding's licence, and turns the confirmed ones into case files an inspector can act on. It is written for the enforcement and compliance lead and for the geospatial, data and platform engineers who would build it. The operator is described by class, never by name.

**The answer in numbers.**

| Part | The design |
|---|---|
| Sources joined | 8 source systems, from the national agricultural register and licence records to a mirrored Sentinel-2, Sentinel-1 and Landsat archive, through 1 integration adapter family |
| Object model | 14 typed objects, from farm holding and licence to detection flag and case file, published as JSON for reuse |
| Models | RF-DETR fine-tuned per region and Chronos-2 zero-shot, both Apache-2.0, about 0.55 GB of weights together |
| Compute | One 48 GB L40S-class inference node inside the Kingdom; the card class needs a US export licence |
| Three-year cost | About 15,200 dollars to own the node, about two thirds the deepest three-year AWS commitment, and renting would move the data outside the Kingdom (Appendix A) |
| Human control | Every flag is verified on the ground by a named field inspector before a case file opens |

**Reuse it.** The object model, the model register and the figures are free to reuse under CC BY 4.0. Cite as DOI https://doi.org/10.5281/zenodo.23186675.

**Made with.** Reasoned on [Praxis](https://codeatoms.ai/praxis/), CodeNinja's platform for designing physical AI systems. The object model imports into [Hyper Ontology](https://codeatoms.ai/hyper-ontology/), which turns it into a living system. Both are in beta; access by request.
