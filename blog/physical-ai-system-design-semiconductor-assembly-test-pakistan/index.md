# A Physical AI System Design for a Semiconductor Assembly and Test Line in Pakistan

*The requirement, in the operator's own voice: edge units that read the inspection cameras at every critical station, one governed ontology of the line, named agents that classify and trace while engineers decide, and memory that makes every confirmed outcome improve the next one.*

Canonical: https://codeatoms.ai/blog/physical-ai-system-design-semiconductor-assembly-test-pakistan/
Author: CodeNinja Atoms, Research distribution
Published: 2026-11-09
License: CC BY 4.0
Publisher: CodeNinja Atoms (https://codeatoms.ai), a fully owned subsidiary of CodeNinja
A physical AI system design, for a semiconductor assembly and test line, is one where the system's eyes sit at the stations themselves: edge units beside the bonders, moulders and markers read the inspection cameras as packages pass, classify what they see, and feed one governed model of the line that agents reason over and engineers decide from. This post publishes the requirement we put to [CodeNinja Praxis](https://codeatoms.ai/praxis/) for such a system: a semiconductor assembly and test operator in Pakistan, described by class only, building a new outsourced semiconductor assembly and test (OSAT) line under the national semiconductor roadmap, with its first packaging and test line commissioning in 2026. The published designs of this kind are collected on the [physical AI system design](https://codeatoms.ai/physical-ai-system-design/) page.

## Why an assembly and test line

Wafers arrive diced from fabs abroad. The line attaches die to substrates or lead frames, wire bonds or flip chip bonds them, moulds, marks and singulates the packages, then tests them electrically and inspects them before shipment. The pilot line is sized for a few hundred thousand packages a month in the first year across two or three package families, with a path to tens of millions a year if anchor customers commit.

Back end yield is decided by things that are hard to see and easy to miss: a lifted wire, a cracked die edge, a void under the die attach, a smeared mark, a bent lead. The inspection stations image every package, but they raise far more alerts than a small quality team can review, and a tuned rule that catches one package family misses the next. When an anchor customer rejects a lot, engineers rebuild the story by hand across the bonder log, the mould recipe, the test bin map and the inspection images, which takes days and often ends without a confirmed cause.

This is a new line with a new team. The judgement of the few experienced engineers hired from abroad lives in their heads and leaves with them. A physical AI system is how that judgement becomes a property of the line instead of a property of the people.

## The systems of record

The manufacturing execution system, the equipment data collection on each bonder, moulder and tester, the automated optical inspection stations' own result databases, the test cell's data logs, the quality management system and the customer return log. Every fact the system uses is tied back to one of them.

## What the operator asks for

1. **Physical AI at the station.** Edge units beside the die attach, wire bond, mould and marking stations, on the CodeNinja on device AI stack, that read the inspection cameras as packages pass, classify each defect candidate and keep nothing but the classified result and the evidence frame. The design says which stations get a camera, what each camera looks for and what runs on the unit.
2. **One model of the line.** A governed ontology of lot, substrate, die, package, station, recipe, bonder head, mould tool, inspection run, defect, defect class, test bin, hold, customer return and corrective action, each fact tied to its source system.
3. **Named agents that draft, engineers who decide.** A classification agent, triggered by a new defect candidate, proposes the class with its evidence frame, confirmed by the quality engineer. An excursion agent, triggered by a defect rate crossing its control limit on one station, traces the likely recipe, tool or material lot and drafts a hold, approved by the process engineer. A return agent, triggered by a customer return, assembles the lot's full history and drafts the eight discipline report for the quality manager to approve.
4. **Memory.** Every confirmed class and every traced cause is kept so the next classification and the next trace are better, without training a model on the fly.
5. **A command centre** for the quality and process team with station defect rates, open holds, agent drafts and a conversational interface that answers with citations.
6. **The model named.** Reasoning runs on GLM 5.3 open weights, self hosted on the operator's own servers in Pakistan.

## The rules that bind

- **Inside the plant.** Customer die images, recipes and test data never leave the operator's network. Models are open weights on hardware the operator owns. No third party model service.
- **Rules.** The anchor customers' confidentiality and data protection terms, the export control conditions attached to the equipment and die the line receives, the national data protection rules, and the automotive and consumer quality standards the customers audit against. The design names the approvals it needs.
- **Systems first.** Read from the execution system, the inspection databases and the equipment logs. No agent places or releases a hold without a named approval.
- **People decide.** Agents classify and draft; engineers confirm.

## What success looks like

The first phase covers one package family on one line for one quarter, measured against a baseline of false alert rate, escapes found at final test or by the customer, time from excursion onset to hold, and engineer review hours per lot. The event the design is tested on is one wire bonder drifting and producing lifted wires across three lots, caught at the station, traced and held before the lots reach test.

## What makes it a physical AI system design

Three things separate this from an inspection dashboard.

The intelligence is at the machine. The edge unit beside the bonder classifies the frame while the package is still in reach, so an excursion is caught at the station where it starts, not at final test or at the customer, lots later.

The physical line and the record of it are one model. A lifted wire is not an image in one database and a bin code in another; it is a defect, on a package, from a bonder head, under a recipe, inside a lot, and the agents trace along those relations the way an experienced engineer would.

The outcome feeds back. Every class the quality engineer confirms and every cause the process engineer accepts is written into memory that the next classification and the next trace must read, so the line's judgement compounds with every lot instead of leaving with the engineers who carry it.

## Questions the design must answer

1. Which stations carry cameras, what runs on each edge unit and on the plant servers, and the hardware class, size and three year cost of each, computed from the models' own weights.
2. How the line ontology is built from the operator's systems and kept current lot by lot.
3. How a classification and an excursion trace are explained to an engineer and to a customer auditor.
4. How confirmed outcomes become memory that improves the next result.
5. The first phase's gates for extending to the next package family and the next line.

The published designs that already answer parts of this, vision at the station and plant quality among them, are collected as [physical AI system design](https://codeatoms.ai/physical-ai-system-design/) and as [sovereign AI reference architectures](https://codeatoms.ai/sovereign-ai-reference-architectures/). Every object model is in the [Vertical-Driven Architectures dataset](https://huggingface.co/datasets/CodeNinjatools/vertical-driven-architectures).

## About CodeNinja

CodeNinja is a Middle Eastern-American artificial intelligence lab focused on building self-improving systems. We are reinventing knowledge work to close the loop between vertical AI use cases and the generalized intelligence that fuels it, accelerating the path toward organizational superintelligence.
