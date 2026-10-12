# Hangar Form Cell: Dieless Robotic Sheet Metal From CAD to Certified Part Without Vendor Cloud

*V E R T I C A L - D R I V E N A R C H I T E C T U R E S · AV I AT I O N & A E R O S PA C E M A N U FA C T U R I N G · D E S I G N E D W I T H P R A X I S ·*

A vendor-independent dieless robotic sheet metal cell for a United States aircraft maintenance, repair and overhaul (MRO) facility that turns CAD into collision-free, springback-compensated toolpaths with in-process metrology and per-serial traceability, wholly inside the facility's own boundary.

For the maintenance lead accountable for structural spare production, hangar superintendents and quality and compliance leads, and the manufacturing, robotics, controls, metrology and platform engineers who would build and run it.

**Canonical page:** https://codeatoms.ai/dieless-sheet-metal-cell-aerospace-mro-us/
**Paper:** [PDF](paper/hangar-form-cell-dieless-robotic-sheet-metal-aerospace-mro-us.pdf) · [HTML](paper/hangar-form-cell-dieless-robotic-sheet-metal-aerospace-mro-us.html) · [Word](paper/hangar-form-cell-dieless-robotic-sheet-metal-aerospace-mro-us.docx) · [Appendix A, what ownership costs over three years](paper/appendix_a_cost.md)
**Licence:** CC BY 4.0. Cite the DOI on the release, or the canonical page.

## Abstract

*A Die Should Not Stand Between a Part and Flight*

A facility that maintains aircraft needs structural components, brackets, panels, skin sections and spare parts formed on demand, from CAD to a certified part, without part-specific dies, without long tooling lead times, and without any vendor cloud touching controlled technical data. It cannot answer that need today because one-off and low-volume parts depends on heavy, expensive hard tooling that must be designed, cut, stored and paid for before the first blank is bent, and because the dieless robotic alternatives on the market arrive with hosted reachback services and software the facility cannot own, which flight-critical provenance rules will not tolerate.

The design is a dual-arm synchronized dieless cell with generic interchangeable styli, an offline CAD-to- path and springback compensation stack the facility owns outright, and in-process metrology that closes the dimensional loop on the facility's own aluminium, steel and titanium sheet. Six source systems enter through two adapter families into an object model of fourteen objects that carries one Asset Administration Shell record per serialized part; five services and five surfaces run on the facility's own network, and one registered model executes at the cell edge. No artifact leaves the boundary, every disposition stays with a named authorized person, and provenance under the material and cybersecurity rules its contracts flow down is designed in from the first procurement.

The paper states the facility's problem and its documented cost, then the join failure across the systems the facility already runs. It fixes the constraints and what the design chose against, lays out the stack from sources to surfaces, defines the fourteen objects and where the human loop sits, walks the ingestion and event backbone, places each inference tier with its latency budget, registers the models, hardware classes and licenses, and plans a three-phase rollout gated by a written kill criterion on sacrificial blanks. It closes on ownership and on the Praxis chapter that traces every choice back to what justified it.

## The object model

`ontology/objects.json` holds the 14 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology.

| Kind | Objects |
|---|---|
| asset | Formed structural part, Sheet blank, Dieless cell, Robot arm, Forming stylus |
| record | Toolpath program, Formability analysis, In-process metrology scan, Force trace, Work order, Nonconformance |
| document | Part CAD model |
| person | Facility operator |
| system | Cell model service |

## The model and equipment register

`register/models.csv`, read from the paper's Table 4: every model, its licence and weight, every hardware class and sizing rule.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on Praxis, CodeNinja's platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
