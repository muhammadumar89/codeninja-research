# Warehouse Twin Command: Live Slotting, Docks, Yards and Safety Vision for Warehousing and Intralogistics in the United States

*VERTICAL-DRIVEN ARCHITECTURES · WAREHOUSING & INTRALOGISTICS · DESIGNED WITH CODENINJA PRAXIS · OCTOBER 2026*

An open reference architecture for a warehouse digital twin in the United States, in warehousing and intralogistics: a fourteen-object model projected over the WMS, labor and yard systems of four distribution centers, weekly slotting and dock and yard scheduling a person approves, safety vision on the existing cameras processed at each site, and every model on open weights the operator owns.

**Canonical page:** https://codeatoms.ai/warehouse-digital-twin-us/
**DOI:** https://doi.org/10.5281/zenodo.23556416
**Paper:** [PDF](paper/warehouse-twin-command-warehouse-digital-twin-us.pdf) · [HTML](paper/warehouse-twin-command-warehouse-digital-twin-us.html) · [Word](paper/warehouse-twin-command-warehouse-digital-twin-us.docx) · [Appendix A, what ownership costs over three years](paper/appendix_a_cost.md)
**Licence:** CC BY 4.0. Cite the DOI on the release, or the canonical page.

## At a glance

| Part | The design |
|---|---|
| Sources | Five named systems (warehouse management, labor management, the yard spreadsheet, video management and a carrier appointment source), entering through one integration adapter family; only the yard spreadsheet is replaced |
| Object model | 14 typed objects and 14 typed links, from the distribution center, dock door and yard trailer through slot, SKU, order, pick task and associate to the safety event, camera zone and slotting recommendation, published as JSON for reuse |
| Models | Mistral Large 3 675B (Apache-2.0) for the site manager assistant; Qwen3.8-27B (Apache-2.0) for assistant continuity at each site; RF-DETR N to L (Apache-2.0) and OC-SORT (MIT) for safety vision; BGE-M3 (MIT) for retrieval; no face recognition, no re-identification, no training run |
| Compute | At each site, one industrial edge server with one 48 GB PCIe inference card running vision in Triton and the site model under vLLM; centrally, one 141 GB HBM class node of eight cards, on the operator's own hardware |
| Rollout | Two phases carrying 19 scope items: a one-site pilot of 17 items across six workstreams, gated on yard trailer staging and carrier wait time, then 2 items to aggregate and roll out to the remaining three sites |
| Three-year cost | About 597,000 US dollars to own the twelve cards (510,000 to 689,000) before the four edge chassis, which are priced by quotation; renting the same cards in AWS US East runs about 1.86 million on demand and about 699,000 on the deepest three-year commitment (Appendix A) |
| Human control | Every slotting move states walking saved and move labor before a person approves it; every safety event becomes a clip a supervisor reviews, and analytics never act as a safety-rated stop |

**Made with.** Reasoned on CodeNinja Praxis; the object model imports into Hyper Ontology.

## The object model

`ontology/objects.json` holds the 14 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology. It joins the [industrial ontology examples](https://codeatoms.ai/industrial-ontology-examples/).

| Kind | Objects |
|---|---|
| site | Distribution Center |
| asset | Dock Door, Yard Trailer, Storage Slot, Camera Zone, Forklift |
| material | SKU |
| record | Open Order, Pick Task, Labor Shift, Slotting Recommendation |
| person | Associate, Shift Lead |
| event | Safety Event |

## The model and equipment register

`register/models.csv`, read from the paper's Table 4: every model, its licence and weight, every hardware class and sizing rule.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on CodeNinja Praxis, the CodeNinja Atoms platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
