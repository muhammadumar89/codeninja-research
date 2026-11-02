# Industrial Data Ontology for a Water Utility in the United States

*VERTICAL-DRIVEN ARCHITECTURES · ENERGY & UTILITIES · DESIGNED WITH CODENINJA PRAXIS · NOVEMBER 2026*

**Plant Context Grid: Industrial Ontologies for the Night a Duty Pump Trips**

An open reference architecture for physical AI system design in a water utility in the United States: one governed, self-hosted industrial data ontology over a municipal water utility's historian, maintenance, map, laboratory and permit records, sixteen objects over six read only sources, two open-weight models of United States origin on one air-cooled server of the utility's own hardware, and named staff deciding every draft.

**Canonical page:** https://codeatoms.ai/water-utility-ontology-us/
**DOI:** https://doi.org/10.5281/zenodo.23889772
**Paper:** [PDF](paper/water-utility-ontology-us.pdf) · [HTML](paper/water-utility-ontology-us.html) · [Word](paper/water-utility-ontology-us.docx) · [Appendix A, what ownership costs over three years](paper/appendix_a_cost.md)
**Licence:** CC BY 4.0. Cite the DOI on the release, or the canonical page.

## At a glance

| Part | The design |
|---|---|
| Sources | Six sources entering through three adapter families that stamp every fact with its source system, extraction method and timestamp: the historian, read only through a mirror in the demilitarized zone behind a hardware data diode, the CMMS, the GIS, the LIMS, the permit records and the condition sensing on pump and motor frames and at the starter panels; the platform holds no credentials in the control network, and its single write path ends at a confirmation record in memory |
| Object model | 16 typed objects with 14 typed links, from the treatment plant, well, distribution reservoir, pump station, lift station and pressure zone through the pump, pipe segment, PLC, RTU, tag and alarm to the work order, sampling point, lab result and permit limit, published as JSON for reuse |
| Models | gpt-oss-120b (Apache-2.0, 117B, MXFP4) for the agentic work surface: the tag mapping agent, the alarm context agent, the monthly compliance drafting agent and cited answers; Nomic Embed Text v2 MoE (Apache-2.0) for retrieval so every answer cites its record; United States origin weights for a state and local critical infrastructure buyer; no third party model service, nothing trained into weights |
| Compute | One air-cooled node of two 48 GB PCIe cards (96 GB, about 88 GB usable) in the utility's own server room, holding 58.4 GB of INT4 weights with a 1.2 planning factor, 70.1 GB; no inference at the stations or wells, and no data leaves the boundary. The room's power, cooling and rack space are confirmed at design and serving acceptance is gated on a measured load run |
| Rollout | Three gated phases carrying 16 scope items (5, 7, then 4) on one treatment plant and its distribution zone during the control system migration, held to the utility's own four baselines before the estate follows; both stated requirements covered |
| Three-year cost | About 59,000 US dollars to own the server for three years (a range of 57,000 to 61,000: server, two 48 GB cards, support and power at the United States average commercial tariff), against about 104,000 to rent the same card class on the deepest three-year commitment in AWS US East, so ownership costs a little under three fifths of it, and about 276,000 on demand. The lowest priced rented instance that holds the model, one 96 GB card of a different class, is about 33,000, against which ownership costs about 1.8 times as much. Renting is a price reference only, because every rented option would carry the utility's records outside its boundary (Appendix A) |
| Human control | Agents draft and named staff decide: the engineer confirms each tag mapping, the operator on shift confirms each alarm context pack, and the compliance manager approves the monthly permit report draft before any figure leaves the room; a monthly sampled audit of confirmed mappings logs the error rate, and a 15 minute staleness alarm on the historian mirror puts the command center into an explicit degraded mode |

**Made with.** Reasoned on [CodeNinja Praxis](https://codeatoms.ai/praxis/), the CodeNinja Atoms platform for designing physical AI systems. The object model imports into [Hyper Ontology](https://codeatoms.ai/hyper-ontology/), which turns it into a living system. Load it with the [hyper-ontology loader](../hyper-ontology-py/): `hyper-ontology show water-utility-ontology-us`. Both are in beta; access by request.

## Abstract

*Industrial Ontologies Answer a Question Six Records Keep Apart*

An industrial data ontology exists to answer the question a municipal water utility in the United States cannot answer today: when the duty pump at a station trips at two in the morning, which asset tripped, what work is open on it, and what the permit requires of the zone it feeds. The answer lives in records that never meet, because the historian holds the tag and the alarm, the maintenance system holds the asset number and the work order, the mapping system holds the pipe and the zone, the laboratory system holds the sample, and the permit files hold the limit, so answering means one person holding all of them in mind while the operators who can are retiring in the middle of a control system migration. The operator is a state and local critical infrastructure owner, which means the join must happen without data leaving its boundary and without any write path toward the control network.

The design is one governed object model of 16 objects, from the plant, well and distribution zone down to the tag, the alarm, the work order, the lab result and the permit limit, fed read-only from six sources through three adapter families, with the segregated control network reached only through a historian mirror behind a hardware data diode in a demilitarized zone. Seven services and four surfaces carry the work: a tag mapping confirmation queue, an alarm context pack, a monthly permit report draft, and a command center with a conversational interface that answers with citations. Three named agents propose and named staff decide, and memory keeps every confirmed mapping and resolved alarm. Two models run on the utility's own air-cooled server with two cards of the 48 GB PCIe class: gpt-oss-120b, 117 billion parameters at MXFP4, about 61 GB of weights, which with the 1.2 planning factor for cache and activations reaches 70.1 GB against the 96 GB the two cards hold, and an embedding model for retrieval with citations. Phase one covers one plant and its distribution zone, gated on the utility's own four baselines before the estate follows.

The paper covers the industry problem and the cost of the join failure, the constraints that shape everything downstream, the layered stack and its 16 objects, the adapter tier and the event backbone, where inference runs and why, the model register and the licenses that let the utility own its weights, the three gated phases with their item counts and measurements, who owns the intelligence the design builds, and finally how Praxis contextualized and reasoned the design, so that every choice can be traced to recorded reading.

## The object model

`ontology/objects.json` holds the 16 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology.

| Kind | Objects |
|---|---|
| site | Treatment Plant, Well, Distribution Reservoir, Pump Station, Lift Station, Pressure Zone |
| asset | Pump, Pipe Segment, PLC, RTU |
| measure | Tag |
| event | Alarm |
| record | Work Order, Sampling Point, Lab Result, Permit Limit |

## The model and equipment register

`register/models.csv`, read from the paper's model and equipment register (Table 4) and chapters 7 and 8: every model, its licence and weight, every hardware class and sizing rule.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on Praxis, CodeNinja's platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
