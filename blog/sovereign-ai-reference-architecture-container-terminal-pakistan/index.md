# A Sovereign AI Reference Architecture for a Container Terminal in Pakistan

*The requirement, in the operator's own voice: one governed ontology of every box from discharge to gate, named agents that draft the chases and the stack moves while planners decide, and open weight models on hardware the operator owns in the country.*

Canonical: https://codeatoms.ai/blog/sovereign-ai-reference-architecture-container-terminal-pakistan/
Author: CodeNinja Atoms, Research distribution
Published: 2026-11-09
License: CC BY 4.0
Publisher: CodeNinja Atoms (https://codeatoms.ai), a fully owned subsidiary of CodeNinja
A sovereign AI reference architecture, for a container terminal, is a complete system design the operator owns end to end: open weight models running on hardware inside the country, reasoning over the terminal's own systems of record, with nothing about customers' cargo leaving the country or reaching a foreign model service. This post publishes the requirement we put to [CodeNinja Praxis](https://codeatoms.ai/praxis/) for such a system: a container terminal operator at a major seaport in Pakistan, described by class only, under pressure from the government's programme to cut container dwell time by two thirds. The architectures that answer requirements like this one are collected on the [sovereign AI reference architectures](https://codeatoms.ai/sovereign-ai-reference-architectures/) page.

## Why a container terminal

A container terminal moves boxes between ships, the yard and the road gate, with the customs authority clearing cargo on the premises and off dock yards taking the overflow. Terminals of this class in Pakistan see container dwell of around a week against a national target of two days, gate queues that stretch into the city, and periodic backlogs of hundreds of boxes that make the news. Trucks now need tracking devices fitted before they can carry cargo out, which has added hours to gate turnaround.

Every box that overstays has a reason, and the operator learns it late: a release the shipping line has not sent, a customs hold nobody chased, a consignee who has not booked a truck, a yard stack that buries the box under newer arrivals. The gate backs up when the yard cannot deliver boxes in appointment order, and the yard cannot plan when it does not know which boxes will clear today.

The planners know the lines, the agents and the cargo types that overstay most. None of that knowledge is written anywhere, so each planner starts the shift from a fresh list. And when the trade bodies or the port authority ask why a box took nine days to leave, the answer is assembled from four systems by hand.

## The systems of record

There are seven: the terminal operating system, the gate operating system and its cameras, the customs authority's clearance messages, the shipping lines' manifests and releases, the yard equipment telematics, the truck appointment system and the off dock transfer log. Every fact the system uses is tied back to one of them.

## What the operator asks for

1. **A sovereign AI reference architecture.** Open weight models on hardware the operator owns in Pakistan, reading the terminal's systems and the customs authority's messages, with nothing about customers' cargo leaving the country or reaching a foreign model service.
2. **One model of the operation.** A governed ontology of vessel call, container, consignee, agent, line, release, customs state, hold, yard position, stack, appointment, truck, gate transaction, dwell and off dock transfer, each fact tied to its source system, so one box has one story from discharge to gate.
3. **Named agents that draft, planners who decide.** An overstay agent, triggered by a box passing half its free time without a clearance step, drafts the chase to the line, the agent or the authority and the recommended off dock transfer, approved by the yard planner. A stack agent, triggered by the next day's clearances, drafts the housekeeping moves that put tomorrow's deliveries on top, approved by the yard superintendent. A gate agent, triggered by an appointment queue crossing its threshold, drafts the lane and slot changes for the gate supervisor to approve.
4. **Memory.** Every confirmed overstay cause and every accepted housekeeping plan is kept, so the next plan is better, without training a model on the fly.
5. **A command centre** for the planning team, with boxes ranked by dwell and cause, chases open, housekeeping drafts, gate queue state, agent drafts awaiting approval, and a conversational interface that answers with citations.
6. **The model named.** Reasoning runs on GLM 5.3 open weights, self hosted on the operator's own hardware in Pakistan.

## The rules that bind

- **In country.** Cargo, customer and gate camera data never leave the operator's network. Models are open weights on hardware the operator owns. No third party model service.
- **Rules.** The port authority's concession terms, the customs authority's clearance rules and message formats, the national data protection rules for gate cameras and drivers, and the shipping lines' data terms. The design names the approvals it needs.
- **Systems first.** The system reads from the terminal, gate and customs systems. No agent moves a box, releases a hold or changes an appointment without a named approval.
- **People decide.** Agents watch and draft; planners and supervisors confirm.

## What success looks like

Phase one covers import containers on one yard block and one gate complex for one quarter, measured against a baseline of median dwell days, boxes over seven days, housekeeping moves per delivered box and gate turnaround minutes. The event the design is tested on is a shipping line's release file arriving late for forty boxes due out tomorrow: seen, chased, and the stack replanned overnight so the morning appointments still clear.

## What makes it a sovereign reference architecture

Three things separate this from a terminal analytics product bought off the shelf.

The data never leaves. Cargo manifests name customers and their goods, and gate cameras record trucks and drivers. All of it stays on the operator's network in Pakistan, and the models that reason over it are open weights on hardware the operator owns, never a third party model service that another jurisdiction can switch off or read.

The design is owned, not rented. The architecture must say what runs where on the operator's hardware, the hardware class and size, and the three year cost, so the operator can buy, run and replace every part of it. That is what makes it a reference: another terminal in the country facing the same dwell targets can take the same design.

The authority can audit it. Because every fact in the ontology is tied to its source system, an overstay chase or a housekeeping plan can be explained line by line to a planner, to the port authority and to the trade bodies asking why a box took nine days.

## Questions the design must answer

1. What runs where on the operator's hardware, the hardware class and size, and the three year cost computed from the models' own weights.
2. How the terminal ontology is built from the operator's systems and the authority's messages, and kept current move by move.
3. How an overstay chase and a housekeeping plan are explained to a planner and to the port authority.
4. How confirmed outcomes become memory that improves the next plan.
5. Phase one's gates for extending to export containers and the other yard blocks.

The published designs this requirement sits beside are collected as [physical AI system design](https://codeatoms.ai/physical-ai-system-design/) and as [sovereign AI reference architectures](https://codeatoms.ai/sovereign-ai-reference-architectures/). Every object model is in the [Vertical-Driven Architectures dataset](https://huggingface.co/datasets/CodeNinjatools/vertical-driven-architectures).

## About CodeNinja

CodeNinja is a Middle Eastern-American artificial intelligence lab focused on building self-improving systems. We are reinventing knowledge work to close the loop between vertical AI use cases and the generalized intelligence that fuels it, accelerating the path toward organizational superintelligence.
