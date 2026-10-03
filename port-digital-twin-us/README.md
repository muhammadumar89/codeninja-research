# Port Twin: One Governed Digital Twin for Every Asset, Feed and Dollar A Port-owned system of context that binds eight operational systems, five live sensor feeds

*VERTICAL-DRIVEN ARCHITECTURES · MARITIME & PORTS · DESIGNED WITH PRAXIS · OCTOBER 2026*

and one finance backbone into a single authoritative digital twin, self-hosted inside the Continental United States boundary the port's own requirements set.

For the port's information technology director, the digital twin program lead and the GIS, integration and data engineers who would build and run it.

**Canonical page:** https://muhammadumar89.github.io/codeninja-research/port-digital-twin-us/
**Paper:** [PDF](paper/port-twin-governed-digital-twin-landlord-port-authority-us.pdf) · [HTML](paper/port-twin-governed-digital-twin-landlord-port-authority-us.html) · [Word](paper/port-twin-governed-digital-twin-landlord-port-authority-us.docx) · [Appendix A, what ownership costs over three years](paper/appendix_a_cost.md)
**DOI:** [10.5281/zenodo.23126431](https://doi.org/10.5281/zenodo.23126431) (all versions: [10.5281/zenodo.23126430](https://doi.org/10.5281/zenodo.23126430))
**Licence:** CC BY 4.0. Cite the DOI on the release, or the canonical page.

## Abstract

*A Port Should See Its Land, Water and Money in One Picture*

The port needs one authoritative answer to a question it can only answer in fragments today: what is happening on its land and water right now, how deep the channel and berths really are, where every lease and expense lands, and which inspection, drawing or project belongs to which asset. The operation's own description of its problem is the honest one: critical information is spread across disconnected systems, maps, spreadsheets, databases and paper records, so every dashboard is a slice and every executive view is a reconciliation exercise performed by hand. No existing system holds the join, because each one was built to run a function, not to hold the port's shared picture.

The design is a system of context: one governed, Port-owned ontology of thirteen objects projected over the Port Community System, the Esri-based GIS environment, finance and real estate systems, an AIS feed, terminal and gate systems, environmental sensor telemetry, pilot navigation software and the document store, joined through three adapter families and one event backbone, and published back as

ArcGIS services so all ten required capabilities arrive as ten services and seven surfaces the Port operates independently. Every component is self-hosted inside the Continental United States boundary the port's requirements themselves set, and the only model in the register is one open-weight embedding model that runs on existing enterprise virtualization, so there is no GPU cluster to buy and no data residency question to argue.

The paper follows the build in order: the industry problem and the join failure across the port's systems; the four constraints, the layered stack, the thirteen-object model, the adapter tier and event backbone, inference placement, and the single model and its license; then the four-phase rollout with its gates, requirement coverage and failure modes, and the ownership position that transfers everything to the Port; the conclusion, and finally the chapter on how Praxis contextualized and reasoned this design.

## The object model

`ontology/objects.json` holds the 13 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology.

| Kind | Objects |
|---|---|
| asset | Berth, Navigation channel, Subsurface utility layer, Environmental sensor feed, Parcel / facility |
| record | Bathymetric survey surface, Utility gap record, Capital project, Inspection record |
| event | Vessel movement record, Truck movement record, PCS message |
| document | Engineering document |

## The model and equipment register

`register/models.csv`, read from the paper's Table 4: every model, its licence and weight, every hardware class and sizing rule.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on Praxis, CodeNinja's platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
