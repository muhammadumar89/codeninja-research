# At a glance · Validated DC interference assessment for gas pipelines in Pakistan

**What this is.** An open reference architecture for system design in physical AI: a validation-first study that digitises an operator's scanned pipeline records, verifies the corridor in the field, calibrates a direct current interference model in validated software and hands the re-runnable model over on the operator's own hardware, so every safe distance ships with its evidence. It is written for the corrosion control lead accountable for pipeline integrity and for the cathodic protection, GIS and modelling engineers who would build and run it. The operator is described by class, never by name.

**The answer in numbers.**

| Part | The design |
|---|---|
| Sources | Two: the operator's furnished data package (alignments, coatings, soils, test points, insulating joints) and the HVDC system's stated configuration, entering through one integration adapter family |
| Object model | 15 typed objects with provenance on every attribute, from the two lines and their insulating joints through the electrode station and test points to the interference assessment and each mitigation measure, published as JSON for reuse |
| Model | PaddleOCR-VL 1.6, about 0.9 billion parameters, Apache-2.0, digitising scanned surveys with two-keyer human reconciliation; the interference physics stays in validated commercial software (CDEGS or COMSOL class) |
| Compute | One server-class host of the 48 GB PCIe inference GPU class inside the operator's estate; no field compute, no cloud, nothing crosses the boundary |
| Rollout | Three gated phases carrying 15 items: data validation, DC modelling and simulation, mitigation strategy and handover, calibrated against bipolar-baseline readings with the 1.3 kA monopolar return modelled as a conservative envelope |
| Three-year cost | About 19,500 US dollars to own the host over three years (18,700 to 20,200), about four fifths of the deepest three-year AWS commitment for one L40S card, which could not keep the data in Pakistan in any case (Appendix A) |
| Human control | A named corrosion control engineer closes every discrepancy and accepts every assessment; no value enters the register without provenance and no safe distance ships without its evidence |

**Reuse it.** The object model, the model register and the figures are free to reuse under CC BY 4.0. Cite as DOI https://doi.org/10.5281/zenodo.23308093.

**Made with.** Reasoned on [CodeNinja Praxis](https://codeatoms.ai/praxis/), the CodeNinja Atoms platform for designing physical AI systems. The object model imports into [Hyper Ontology](https://codeatoms.ai/hyper-ontology/), which turns it into a living system. Both are in beta; access by request.
