# At a glance · OT security monitoring and NERC CIP evidence for a utility in the United States

**What this is.** An open reference architecture for system design in physical AI: one system of context that sees every device on a utility's control networks, flags abnormal behaviour and assembles the evidence a NERC CIP audit asks for, on the operator's own hardware. It is written for the OT security and CIP compliance leads and for the platform, network and integration engineers who would build it. The operator is described by class, never by name.

**The answer in numbers.**

| Part | The design |
|---|---|
| Sources joined | 10 source systems, including the SIEM, an OT detection tool, an IT monitoring platform, the energy management system and the substation data platform, through 2 adapter families |
| Object model | 14 typed objects and 14 links, with the OT asset as the focal object, published as JSON for reuse |
| Models | GLM 5.2 (MIT) for reasoning and Qwen3-Embedding-0.6B (Apache-2.0) for retrieval; detection stays in the procured sensors |
| Compute | One node of eight 141 GB HBM-class GPUs: 753 GB of FP8 weights, 904 GB with the 1.2 planning factor, against 1,128 GB |
| Boundary | Read only and one way out of the control networks; nothing writes into an electronic security perimeter, and no data leaves the operator |
| Three-year cost | About 510,000 dollars to own the reasoning node, about four fifths the deepest three-year AWS commitment (Appendix A) |
| Human control | Every triage, case and risk acceptance carries a named OT security analyst; agents draft, the analyst decides |

**Reuse it.** The object model, the model register and the figures are free to reuse under CC BY 4.0. Cite as DOI https://doi.org/10.5281/zenodo.23157957.

**Made with.** Reasoned on [Praxis](https://muhammadumar89.github.io/codeninja-research/praxis/), CodeNinja's platform for designing physical AI systems. The object model imports into [Hyper Ontology](https://muhammadumar89.github.io/codeninja-research/hyper-ontology/), which turns it into a living system. Both are in beta; access by request.
