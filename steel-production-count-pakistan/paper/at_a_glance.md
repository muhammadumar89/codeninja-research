# At a glance · Independently counted production for every steel mill in Pakistan

**What this is.** An open reference architecture for system design in physical AI: cameras and a GPU industrial PC at every casting strand and cooling bed count billets, ingots, rebars and girders as they are made, publish the counts through a one-way link into one record the authority owns, and let revenue officers reconcile counted against declared production. It is written for the director accountable for production monitoring and for the edge, vision and platform engineers who would build it. The operator is described by class, never by name.

**The answer in numbers.**

| Part | The design |
|---|---|
| Sources joined | The counting estate itself, the weighbridge, declared production filings and the authority's case system, through one adapter family |
| Object model | 14 typed objects and 12 links, with the production count event as the focal object, published as JSON for reuse |
| Models | 3 self-hosted open models: RF-DETR (detection, fine-tuned per product type and mill), Roboflow trackers (identity across camera fields), GLM 5.3 (compliance work surface) |
| Edge | One sealed GPU industrial PC and IP66 HDR cameras per installation point; counting survives a slow wide-area link |
| Frontier compute | One node of eight 141 GB HBM-class GPUs holds GLM 5.3 at FP8 (753 GB of weights, 904 GB with headroom), in a dedicated data center behind an export licence checkpoint |
| Three-year cost, owned | About 4,445,000 US dollars for 300 installation points, of which the counting kits are 2,832,000 and cannot be rented; owning the frontier node costs about 686,000 against 751,000 on AWS's deepest three-year plan |
| Closed model break-even | The cheapest closed model matches the owned node at about 33 users; above that, ownership is cheaper |
| Human control | Every discrepancy case is judged by a named revenue field officer; the system counts and reconciles, it never assesses, and the mill never edits a count |
| The hard dependency | 141 GB-class accelerators need a US export licence for Pakistan (Country Group D:4); the node is ordered only once a licence naming the end user holds |

**Reuse it.** The object model, the model register and the figures are free to reuse under CC BY 4.0.
