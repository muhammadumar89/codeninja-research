# At a glance · Warehouse Twin Command: Live Slotting, Docks, Yards and Safety Vision for Warehousing and Intralogistics in the United States

**What this is.** An open reference architecture for system design in physical AI. A live digital twin of four distribution centers run by a warehousing and intralogistics operator in the United States: one object model projected over the warehouse, labor and yard systems the operation already runs, kept true by nightly reconciliation against the WMS, producing weekly slotting recommendations, dock and yard schedules and on-site safety vision on the existing cameras, with every action drafted for a person to approve. It is written for the network operations director, the site and safety managers, and the data, platform, ontology and vision engineers who would build and run it. The operator is described by class, never by name.

**The answer in numbers.**

| Part | The design |
|---|---|
| Sources | Five named systems (warehouse management, labor management, the yard spreadsheet, video management and a carrier appointment source), entering through one integration adapter family; only the yard spreadsheet is replaced |
| Object model | 14 typed objects and 14 typed links, from the distribution center, dock door and yard trailer through slot, SKU, order, pick task and associate to the safety event, camera zone and slotting recommendation, published as JSON for reuse |
| Models | Mistral Large 3 675B (Apache-2.0) for the site manager assistant; Qwen3.8-27B (Apache-2.0) for assistant continuity at each site; RF-DETR N to L (Apache-2.0) and OC-SORT (MIT) for safety vision; BGE-M3 (MIT) for retrieval; no face recognition, no re-identification, no training run |
| Compute | At each site, one industrial edge server with one 48 GB PCIe inference card running vision in Triton and the site model under vLLM; centrally, one 141 GB HBM class node of eight cards, on the operator's own hardware |
| Rollout | Two phases carrying 19 scope items: a one-site pilot of 17 items across six workstreams, gated on yard trailer staging and carrier wait time, then 2 items to aggregate and roll out to the remaining three sites |
| Three-year cost | About 597,000 US dollars to own the twelve cards (510,000 to 689,000) before the four edge chassis, which are priced by quotation; renting the same cards in AWS US East runs about 1.86 million on demand and about 699,000 on the deepest three-year commitment (Appendix A) |
| Human control | Every slotting move states walking saved and move labor before a person approves it; every safety event becomes a clip a supervisor reviews, and analytics never act as a safety-rated stop |

**Reuse it.** The object model, the model register and the figures are free to reuse under CC BY 4.0. Cite the canonical page, https://codeatoms.ai/warehouse-digital-twin-us/, or the DOI on the release.

**Made with.** Reasoned on [CodeNinja Praxis](https://codeatoms.ai/praxis/), the CodeNinja Atoms platform for designing physical AI systems. The object model imports into [Hyper Ontology](https://codeatoms.ai/hyper-ontology/), which turns it into a living system. Both are in beta; access by request.
