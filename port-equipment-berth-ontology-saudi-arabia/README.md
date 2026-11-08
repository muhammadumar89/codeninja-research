# Industrial Ontology Examples: A Port Equipment and Berth Object Model in Saudi Arabia

*VERTICAL-DRIVEN ARCHITECTURES · MARITIME & PORTS · DESIGNED WITH CODENINJA PRAXIS · NOVEMBER 2026*

One of the [industrial ontology examples](https://codeatoms.ai/industrial-ontology-examples/) in the Vertical-Driven Architectures series, under the working title Maritime & Ports Watch: One Living Picture of the Operation. A governed industrial ontology of a container terminal's berths, equipment and moves in Saudi Arabia: sixteen objects over eight read only systems of record, kept current move by move, three drafting agents that named managers confirm, and GLM 5.3 self hosted on one node in the operator's own machine room.

**Canonical page:** https://codeatoms.ai/port-equipment-berth-ontology-saudi-arabia/
**Paper:** [PDF](paper/port-equipment-berth-ontology-saudi-arabia.pdf) · [HTML](paper/port-equipment-berth-ontology-saudi-arabia.html) · [Word](paper/port-equipment-berth-ontology-saudi-arabia.docx) · [Appendix A, what ownership costs over three years](paper/appendix_a_cost.md)
**DOI:** not yet minted; cite the canonical page.

**Licence:** CC BY 4.0. Cite the DOI once it is minted on the release, or the canonical page.

## At a glance

| Part | The design |
|---|---|
| Sources | Eight read only systems of record, entering through two adapter families (an integration adapter over APIs and read only views, a telemetry adapter into the time series store behind a hardware data diode) that stamp every event with its source, provenance class and read time: the terminal operating system, the vessel scheduling and berth planning tool, the crane and equipment control systems, the maintenance management system, equipment telematics, the port authority's vessel traffic and berth window data, the civil works and commissioning records and the safety incident register; the single write path back is a named approval into the maintenance system or the berth plan, never into a control system |
| Object model | 16 typed objects in six kinds with 13 typed links, from the berth, quay section and yard block through the ship to shore crane, yard crane, straddle carrier and equipment component, the vessel call, berth window, fault, move and incident, the work order and commissioning record, the box and the productivity measure, each anchored in one system of record and published as JSON for reuse |
| Models | GLM 5.3 (GLM-5.3 bespoke licence, 753B at FP8) for the three drafting agents (productivity, equipment, commissioning), the command centre and ontology maintenance; GLM-5.3-Flash (MIT, 320B total, 18B active, multimodal) reading the builders' commissioning drawings and pages on the terminal tier; BGE-M3 (MIT) for retrieval whose sparse leg keeps container numbers and fault codes exact; no third party model service, nothing trained into weights |
| Compute | One node of eight 141 GB HBM cards (1,128 GB) in the operator's own machine room in the Kingdom, holding 753 GB of FP8 weights with a 1.2 planning factor, 904 GB, 375 GB beside the weights; a two socket air cooled server class for the terminal tier; no edge tier committed (continuous crane sensing is offered and priced separately). The node is a 4A090 class item for a D:3 and D:4 destination, so an export licence determination naming the importer of record is a phase one start item |
| Rollout | Three phases carrying 18 scope items (15, 2 and 1), each closed by a gate, never a date: two berths, their cranes and yard blocks for one quarter with the object model proven on one week of production joins before any agent runs and the commissioning agent as the exit gate, then the whole terminal with the continuous crane sensing option as its gate, then the group's other ports; 21 requirements read against the build at every gate; baselines frozen on berth moves per hour, faults joined to a vessel call effect within the shift, days to commission a new crane's records and hours spent reconciling names |
| Three-year cost | About 570,000 US dollars to own the node for three years (a range of 542,000 to 594,000: server, support and power at the national commercial electricity tariff), against about 751,000 to rent the same eight cards on the deepest three year commitment in AWS Middle East (UAE), so ownership costs about three quarters of it, and about 2.00 million on demand, against which ownership costs a little over a quarter. Renting is a price reference only, because AWS listed no Saudi region on the day read and every rented option would carry cargo, vessel and equipment data across the border (Appendix A) |
| Human control | Agents draft and people decide, by name: the operations manager confirms the productivity agent's ranked causes, the engineering manager approves the equipment agent's work order and berth plan effect, and the expansion project engineer approves the commissioning agent's objects; approval latency is instrumented and known answer probes sit in the draft queue from day one, and every confirmation is kept as the memory the next trace reads |

**Made with.** Reasoned on [CodeNinja Praxis](https://codeatoms.ai/praxis/), the CodeNinja Atoms platform for designing physical AI systems. The object model imports into [Hyper Ontology](https://codeatoms.ai/hyper-ontology/), which turns it into a living system. Load it with the [hyper-ontology loader](../hyper-ontology-py/): `hyper-ontology show port-equipment-berth-ontology-saudi-arabia`. Both are in beta; access by request.

## Abstract

*The Answer Already Exists in the Systems the Operation Runs*

Berth productivity drops and nobody can say whether the cause was the crane's hydraulic fault, the yard block that could not keep up, the vessel's stowage or the berth window the authority granted; this paper, one of the industrial ontology examples in this series, is a port equipment and berth object model that lets a container terminal operator in Saudi Arabia answer that question.

The design reads 9 source systems through 2 adapter families into one object model of 16 objects, runs 10 services over it and opens 4 surfaces to the people who decide, with 3 models placed where the data is. A governed industrial ontology of the terminal's berths, equipment and moves, built from the operator's eight named systems of record and kept current move by move, with three drafting agents (productivity, equipment, commissioning) whose outputs managers confirm and which write back only through named approvals. Reasoning runs on GLM 5.3 open weights self hosted by a container terminal operator in Saudi Arabia on one 141 GB HBM class node, with a kept record of decisions and outcomes that the next decision reads, memory improving every next trace without training.

The paper covers the operation and the problem its systems cannot answer, the constraints, the stack, the object model, ingestion, inference placement, the models and their licenses, the rollout and its proof, ownership, and finally how Praxis contextualized and reasoned the design.

## The object model

`ontology/objects.json` holds the 16 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology.

| Kind | Objects |
|---|---|
| site | Berth, Quay Section, Yard Block |
| asset | Ship to Shore Crane, Yard Crane, Straddle Carrier, Equipment Component |
| event | Vessel Call, Berth Window, Fault, Move, Incident |
| record | Work Order, Commissioning Record |
| material | Box |
| measure | Productivity Measure |

## The model and equipment register

`register/models.csv`, read from the paper's model and equipment register (Table 4) and chapters 4, 6 and 7: every model, its licence and weight, every hardware class and sizing rule, the committed signals, the offered sensing tier, and the patterns the design stands on.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on Praxis, CodeNinja's platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
