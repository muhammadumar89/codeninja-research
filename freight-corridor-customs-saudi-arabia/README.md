# Sovereign AI Architecture for a Freight Corridor and Customs Clearance in Saudi Arabia

*VERTICAL-DRIVEN ARCHITECTURES · SUPPLY CHAIN & LOGISTICS · DESIGNED WITH CODENINJA PRAXIS · NOVEMBER 2026*

A [sovereign AI architecture](https://codeatoms.ai/sovereign-ai-architecture/) for a national freight and logistics operator in Saudi Arabia, first written as Corridor Command: Industrial AI for the Whole Consignment Story: one governed corridor ontology of fifteen objects over seven read only systems of record, three drafting agents that named planners, controllers and service desk agents approve, and open weights on one node in the operator's own data center.

**Canonical page:** https://codeatoms.ai/freight-corridor-customs-saudi-arabia/
**Paper:** [PDF](paper/freight-corridor-customs-saudi-arabia.pdf) · [HTML](paper/freight-corridor-customs-saudi-arabia.html) · [Word](paper/freight-corridor-customs-saudi-arabia.docx) · [Appendix A, what ownership costs over three years](paper/appendix_a_cost.md)
**DOI:** to be minted on release

**Licence:** CC BY 4.0. Cite the DOI on the release, or the canonical page.

## At a glance

| Part | The design |
|---|---|
| Sources | Seven read only systems of record entering through two adapter families (the integration adapter on Debezium with Apache Camel and the telemetry adapter) that guarantee lineage, ordering and staleness flags: the rail operations and yard management system, the transport management system, the customs authority's declaration and clearance interfaces, the port community system feeds, the haulier telematics feeds, the container tracking system and the customer service case log; no agent files, amends, re books or cancels a declaration or booking, and the design never writes into a system of record |
| Object model | 15 typed objects with 11 typed links, from the consignment, container and declaration through the train, wagon, road leg and haulier to the terminal, dry port, handover slot, exception and customer case, with the corridor planner, yard controller and service desk agent as actors; a projection over the seven systems joined on the container number, never a copy, published as JSON for reuse |
| Models | GLM 5.3 (class open weights, self hosted, frontier class) named by the requirement for the command center that answers questions about a consignment with citations, with GLM 5.2 under MIT as the licence fallback; the register commits no model row until a live verification passes; no third party model service, nothing trained into weights |
| Compute | One node of eight 141 GB HBM cards in the operator's own in-country data center, holding about 756 GB of FP8 weights on about 1,038 GB of usable memory with about 280 GB of KV cache ceiling, planned at about ten kilowatts; no edge tier, no cameras, no new field sensing. The node is a 4A090 class item for a D:3 and D:4 destination, so an export licence determination against ECCN 3A090 and 4A090 is a phase zero checkpoint before any GPU class is quoted |
| Rollout | Three phases carrying 17 scope items (2, 14 and 1), each closed by a gate, never a date: baseline and approvals, whose gate is the residency approvals closed and the baseline recorded; one corridor between one seaport and one dry port through one measured quarter, whose exit gate is source system bindings and lineage proven on one real week of production data; then extension gates to the other corridors; headline measure dry port dwell in hours against a nominal of 96, with stalled declarations, missed connections and answered questions counted beside it |
| Three-year cost | About 569,000 US dollars to own the node for three years (a range of 541,000 to 594,000: server, support and power at the national commercial electricity tariff), against about 751,000 to rent the same eight cards on the deepest three year commitment in AWS Middle East (UAE), so ownership costs about three quarters of it, and about 2.00 million on demand, against which ownership costs a little over a quarter. Renting is a price reference only, because AWS listed no Saudi region on the day read and every rented option would carry cargo, customer and declaration data across the border (Appendix A) |
| Human control | Agents draft and people decide, by name: the corridor planner approves the stall chase and the revised handover slot, the yard controller approves every re booking, and the service desk agent sends the cited answer; approval authority is a property of the actor objects, a per shift alert budget is agreed before thresholds are set, the action rate is itself a gate, and every confirmed stall cause and accepted re booking is kept as memory the next plan reads |

**Made with.** Reasoned on [CodeNinja Praxis](https://codeatoms.ai/praxis/), the CodeNinja Atoms platform for designing physical AI systems. The object model imports into [Hyper Ontology](https://codeatoms.ai/hyper-ontology/), which turns it into a living system. Load it with the [hyper-ontology loader](../hyper-ontology-py/): `hyper-ontology show freight-corridor-customs-saudi-arabia`. Both are in beta; access by request.

## Abstract

*Where a Box Is Should Not Take Six Systems to Answer*

A sovereign AI architecture for a freight corridor in Saudi Arabia starts from the one question the operation needs answered continuously: where is this consignment, and when will it clear. It cannot be answered today because the answer lives in six systems of record carrying six identifiers, and it is assembled by hand by a planner whenever a consignee asks. Corridors of more than two thousand kilometers mix rail legs with road legs run by contracted hauliers, each consignment crossing the port terminal, the customs authority's clearance system, the operator's rail yard, a haulier, the dry port and the consignee, while the authority's single declaration transit with pre clearance and smart inspection now runs on some lanes of a national truck fleet of around half a million vehicles. Dwell at the dry port grows when a declaration stalls, and the stall is learned from the consignee rather than from the systems; a late road leg is visible in telematics but never joined to the train it will miss.

The design is a sovereign corridor and customs system built for a national freight and logistics operator in Saudi Arabia: seven read-only source systems, two adapter families covering integration and telemetry, fifteen objects in one governed object model, seven services covering governance, baselines, the ontology, agents and approvals, the sovereign platform, memory and the command center, and three surfaces consisting of the command center, the connection view and the answer queue. Every part runs on the owner's own central node in its in-country data center, on open weights the owner holds, with no edge inference and no third party model service, so cargo, consignee and declaration data never leave the country. The model register carries no committed weights on this plan: no open weight model survived this run's live verification, so the choice of weights is recorded open work with its sizing line, the inference cluster class (GPU nodes for 300B to 1T parameter open weight models), held ready rather than fixed.

The paper covers the industry problem and the join failure across the six systems, the constraints and the scoping decisions they force, the layered stack and the fifteen-object model of the consignment story, the adapter tier and event backbone that feed it, the placement of all reasoning on the owner's central node, the model register and the licenses that decide what the owner can own, the three phases with their item counts and gates, and who owns the intelligence the system produces, closing with the chapter on how Praxis contextualized and reasoned the design.

## The object model

`ontology/objects.json` holds the 15 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology.

| Kind | Objects |
|---|---|
| site | Terminal, Dry Port |
| asset | Container, Wagon |
| record | Consignment, Declaration, Train, Road Leg, Handover Slot, Customer Case |
| event | Exception |
| actor | Haulier, Corridor Planner, Yard Controller, Service Desk Agent |

## The model and equipment register

`register/models.csv`, read from the paper's model and equipment register (Table 4), the architecture register (Table 7) and chapters 6 to 8: the model the requirement names and its licence fallback, the hardware class and its sizing rules, the export licence checkpoint, the platform components chosen by name or by class, and the patterns the design stands on.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on Praxis, CodeNinja's platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
