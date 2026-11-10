---
{
 "title": "A Sovereign AI Architecture for Refinery Operations Knowledge in Saudi Arabia",
 "subtitle": "The requirement, in the operator's own voice: one governed ontology of the whole refinery, named agents that draft and shift engineers who decide, open weight models self hosted in country, and memory that makes every trip analysis better than the last.",
 "author": "CodeNinja Atoms",
 "author_role": "Research distribution",
 "author_url": "https://codeatoms.ai/about/",
 "date": "2026-11-09",
 "tags": [
  "Engineering",
  "Oil and gas",
  "Sovereign AI architecture"
 ],
 "audience": "For shift engineers, process safety and turnaround teams at an integrated refinery, and the engineers and coding agents who would build a sovereign AI architecture with them.",
 "description": "Sovereign AI architecture for refinery operations knowledge in Saudi Arabia: the requirement, the systems of record, the agents, the rules that bind and the questions a design must answer.",
 "cover_photo": "refinery.jpg",
 "cover_position": "center",
 "cover_credit": "Photo by 龔 月強 on Pexels (https://www.pexels.com/photo/5884386/), Pexels License",
 "cover_line": "A requirement for a sovereign AI architecture",
 "cluster": "sovereign AI",
 "owned_keyword": "sovereign AI"
}
---

A sovereign AI architecture, for a refinery, is one the operator owns end to end: open weight models running on hardware the operator controls inside Saudi Arabia, reading the refinery's own systems of record, with nothing about the plant leaving the country or reaching a foreign model service. This post publishes the requirement we put to [CodeNinja Praxis](https://codeatoms.ai/praxis/) for such a system: a refining operator in Saudi Arabia, described by class alone, that wants the judgement of its best shift engineers turned into operations knowledge the whole plant can use. The published designs of this kind are collected as [sovereign AI architecture](https://codeatoms.ai/sovereign-ai-architecture/) reference pages.

## Why a refinery

The refinery runs crude distillation, hydrocracking, hydrotreating, reforming, sulphur recovery and utilities around the clock, with a control room per complex and a shift engineer responsible for each. Refineries of this class process several hundred thousand barrels a day, by public reporting on plants of the class in the country, and run a major turnaround every few years with thousands of contractor workers on site.

The shift engineers are asked questions no single system answers. Why did the hydrocracker trip in the same way twice this year. What did the last turnaround find in this exchanger bank. Which procedure change was made after the last sulphur unit upset, and did it work. The answers exist, in the historian, in a shift log, in a change record and in an incident report, and a good engineer spends a night shift joining them.

The urgency is generational. Half the senior shift engineers retire within five years, and the new engineers inherit the systems but not the judgement. During a turnaround the problem doubles: thousands of findings arrive in days, and the engineers who can read them are out on the plant.

## The systems of record

The distributed control system and its historian, the alarm and event journal, the operating procedures and shift logs, the maintenance management system, the management of change records, the incident and near miss system, the laboratory information system and the turnaround planning system. Every fact the system uses is tied back to one of them.

## What the operator asks for

1. **A sovereign AI architecture owned by the operator.** Open weight models on the operator's own hardware in the country, reading the systems of record, with nothing about the plant leaving the country or reaching a foreign model service.
2. **One model of the plant.** A governed ontology of unit, equipment, tag, alarm, procedure, shift log entry, work order, change, incident, lab result, finding and turnaround task, each fact tied to its source system, so an exchanger has one history across the historian, the work orders and the findings.
3. **Named agents that draft, engineers who decide.** A trip analyst, triggered by a unit trip, drafts the sequence of events with the matching earlier trips and the changes made since, confirmed by the shift engineer. A handover agent, triggered by shift end, drafts the handover from the alarms, logs and work orders of the shift for the outgoing engineer to confirm. A findings agent, triggered by a turnaround inspection finding, drafts the matching history and the recommended disposition for the turnaround engineer to approve.
4. **Memory.** Every confirmed cause and every accepted disposition is kept so the next analysis is better, without training a model on the fly.
5. **A command centre** for shift engineers, showing open trips, handovers, findings waiting and agent drafts, with a conversational interface that answers with citations.
6. **The model named.** Reasoning runs on GLM 5.3 open weights, self hosted on the operator's own hardware in Saudi Arabia.

## The rules that bind

- **In country.** Plant data never leaves the operator's network. Models are open weights on hardware the operator owns. No third party model service.
- **Rules.** The national critical infrastructure cybersecurity controls for operational technology, the process safety management rules, the operator's own management of change procedure, and the national data protection law. The design names the approvals it needs.
- **Read only on control systems.** The architecture reads the historian and journals through the existing one way path. It never writes to the control system, and no agent changes a setpoint, a procedure or a work order without a named approval.
- **People decide.** Agents draft; engineers confirm.

## What success looks like

The first phase covers one complex and its control room for one quarter, including the turnaround if it falls in the quarter, measured against a baseline of hours to a confirmed trip sequence, handover completeness, repeat trips with the same cause, and findings dispositioned per day during the turnaround. The simulated event the design is tested on is a hydrocracker recycle compressor trip at night, with the matching trip from last year and the change made after it found and shown to the shift engineer within minutes.

## What makes it a sovereign AI architecture

Three things separate this from a cloud analytics subscription.

The weights live with the plant. Reasoning runs on open weight models on hardware the operator owns inside Saudi Arabia, so the capability cannot be priced up, switched off or routed abroad by a vendor, and nothing about the plant crosses the border to a model service.

The knowledge is the operator's object model, not a vendor's index. The ontology of units, tags, procedures, changes, incidents and findings is governed by the operator and tied fact by fact to the systems of record, so it outlives any one supplier and any one model.

The judgement stays auditable and in country. Every confirmed cause and accepted disposition is a cited record an engineer and a process safety auditor can read, kept as memory on the same sovereign hardware, so the plant's hardest earned knowledge accumulates where it was earned.

## Questions the design must answer

1. What runs where on the operator's hardware, the hardware class and size, and the three year cost computed from the models' own weights.
2. How the plant ontology is built from the systems of record and kept current shift by shift.
3. How a trip sequence and a finding disposition are explained to a shift engineer and to a process safety auditor.
4. How confirmed outcomes become memory that improves the next analysis.
5. The first phase's gates for extending to the other complexes.

The published designs that already answer parts of this, refinery and process plant operations among them, are collected as [physical AI system design](https://codeatoms.ai/physical-ai-system-design/) and as [sovereign AI reference architectures](https://codeatoms.ai/sovereign-ai-reference-architectures/). Every object model is in the [Vertical-Driven Architectures dataset](https://huggingface.co/datasets/CodeNinjatools/vertical-driven-architectures).

## About CodeNinja

CodeNinja is a Middle Eastern-American artificial intelligence lab focused on building self-improving systems. We are reinventing knowledge work to close the loop between vertical AI use cases and the generalized intelligence that fuels it, accelerating the path toward organizational superintelligence.
