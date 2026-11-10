---
{
 "title": "A Self-Improving AI System for a Gas Compressor Fleet in Saudi Arabia",
 "subtitle": "The requirement, in the operator's own voice: one governed ontology of every compression train, named agents that draft and people who decide, and a loop that learns from every closed work order through memory, never by retraining weights.",
 "author": "CodeNinja Atoms",
 "author_role": "Research distribution",
 "author_url": "https://codeatoms.ai/about/",
 "date": "2026-11-02",
 "tags": [
  "Engineering",
  "Oil and gas",
  "Self-improving AI system"
 ],
 "audience": "For reliability and maintenance engineers at a gas processing plant, and the engineers and coding agents who would build a self-improving AI system with them.",
 "description": "Self-improving AI system for a gas compressor fleet in Saudi Arabia: the requirement, the outcome loop, the agents, the rules and the questions a design must answer.",
 "cover_photo": "gas-plant.jpg",
 "cover_position": "right center",
 "cover_credit": "Photo by Yuri Shkoda on Pexels (https://www.pexels.com/photo/13100561/), Pexels License",
 "cover_line": "A requirement for a self-improving AI system",
 "cluster": "self-improving system",
 "owned_keyword": "self-improving system"
}
---

A self-improving AI system, for a gas compressor fleet, is one that gets measurably better at maintenance decisions every time a work order closes, because what was predicted and what was actually found are written back into the context it reasons with, never into retrained weights. This post publishes the requirement we put to [CodeNinja Praxis](https://codeatoms.ai/praxis/) for such a system: a large gas processing operator in Saudi Arabia, described by class only, deciding when to inspect, extend or overhaul its compression trains. The way Praxis itself is run as one is on the [self-improving AI system](https://codeatoms.ai/self-improving-ai-system/) page.

## Why a compressor fleet

Compression is the heart of a gas plant: trains of centrifugal compressors driven by gas turbines and large electric motors run around the clock. Every maintenance decision on a train, inspect now or extend, overhaul or repair, is made by a reliability engineer reading the historian, the vibration system, oil results and old inspection reports by hand.

When the inspection is done, what was found, worse than expected, better, or a different fault, is written into a work order and rarely flows back into the next decision. So the same judgement is relearned train by train, the best engineers' knowledge stays in their heads, and the fleet carries both unnecessary inspections and surprise trips.

An unplanned trip cuts plant throughput and can flare gas. An unnecessary inspection takes a train offline for days. Refurbishment capacity is limited, so every overhaul slot matters. A published 2026 maintenance case study from this class of operator showed that moving from fixed maker intervals to an extend and inspect approach, reading exhaust temperature, compressor discharge, bearing temperature, load, vibration, inlet filter differential pressure and trip logs, extended inspection intervals by 20 to 34 percent on one frame family.

## The systems of record

The plant historian, the vibration and machinery protection system, the maintenance management system, the lube oil laboratory, inspection reports and the makers' service bulletins. Every fact the system uses is tied back to one of them.

## What the operator asks for

1. **A self-improving AI system.** One governed ontology of plant, compression train, compressor, driver, component, sensor tag, reading, trip, inspection, finding, work order, interval decision and service bulletin, each fact tied to its source.
2. **A loop that improves from outcomes.** Every work order outcome, what was predicted and what was found, is written to memory and changes the next recommendation. The system improves loop by loop through memory, never by retraining weights.
3. **Named agents that draft, people who decide.** A condition agent, triggered by a new reading pattern or a trip, ranks each train's risk with its evidence, confirmed by the reliability engineer. An interval agent, triggered by an upcoming scheduled inspection, drafts extend or inspect with the evidence and past outcomes, approved by the maintenance superintendent. An outcome agent, triggered when a work order closes, compares prediction with finding and drafts the lesson into memory, confirmed by the maintenance planner.
4. **Sensing at the edge.** Continuous sensing on the critical trains, route based collection for the rest, at the edge on the CodeNinja on device AI stack.
5. **A command centre** for the reliability team, and a conversational interface whose answers cite their records.
6. **The model named.** Reasoning runs on GLM 5.3 open weights, self hosted in the operator's own data centre in Saudi Arabia.

## The rules that bind

- **Sovereign.** All plant data and models stay in Saudi Arabia on hardware the operator controls. No third party model service. Operational networks stay separated.
- **Rules.** The national cybersecurity controls for operational technology, the Personal Data Protection Law, process safety management, and the operator's own engineering standards and permit to work. The design names the approvals it needs.
- **Read first.** No agent changes a maintenance plan, a protection setting or a work order without a named approval.
- **People decide.**

## What success looks like

The first phase covers one plant's gas turbine driven compressor trains for twelve months, measured against a baseline of unplanned trips, inspections performed versus deferred with no adverse finding, the prediction hit rate on closed work orders, and overhaul slots used. The event the design is tested on is one compressor train tripping on high bearing temperature.

## What makes it self-improving

Three things separate this from a condition monitoring dashboard.

The outcome is recorded against the prediction. When a work order closes, the outcome agent puts the finding next to what the condition and interval agents said before the inspection. That pair is the learning signal.

The lesson changes context, not weights. The confirmed lesson becomes a memory entry that the next recommendation for any similar train must read and cite. Nothing is trained into the model, so every change is a document a reliability engineer can read.

The loop is auditable. Because every lesson is a record with an author, a date and the work order it came from, a bad lesson can be found and retired, and the prediction hit rate on closed work orders shows loop by loop whether the system is actually getting better.

## Questions the design must answer

1. How the fleet ontology is built from the historian and maintenance systems.
2. How each work order outcome changes the next recommendation, measurably, without training a model.
3. What sensing and edge hardware the critical trains need, sized and costed.
4. How the loop is audited so a bad lesson can be found and retired.
5. The first phase's gates for extending to every plant.

The published designs that already answer parts of this, rotating equipment condition monitoring and plant reliability among them, are collected as [physical AI system design](https://codeatoms.ai/physical-ai-system-design/) and as [sovereign AI reference architectures](https://codeatoms.ai/sovereign-ai-reference-architectures/). Every object model is in the [Vertical-Driven Architectures dataset](https://huggingface.co/datasets/CodeNinjatools/vertical-driven-architectures).

## About CodeNinja

CodeNinja is a Middle Eastern-American artificial intelligence lab focused on building self-improving systems. We are reinventing knowledge work to close the loop between vertical AI use cases and the generalized intelligence that fuels it, accelerating the path toward organizational superintelligence.
