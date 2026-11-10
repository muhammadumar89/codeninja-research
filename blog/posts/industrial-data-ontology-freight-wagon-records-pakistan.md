---
{
 "title": "An Industrial Data Ontology for Freight Wagon Records in Pakistan",
 "subtitle": "The requirement, in the operator's own voice: one governed model of the freight wagon fleet built from paper registers and builders' files, named agents that draft and officers who decide, and open weight models self hosted in Pakistan.",
 "author": "CodeNinja Atoms",
 "author_role": "Research distribution",
 "author_url": "https://codeatoms.ai/about/",
 "date": "2026-11-09",
 "tags": [
  "Engineering",
  "Rail",
  "Industrial data ontology"
 ],
 "audience": "For mechanical department engineers at a rail freight operator, and the engineers and coding agents who would build an industrial data ontology with them.",
 "description": "Industrial data ontology for freight wagon records in Pakistan: the requirement, the systems of record, the agents, the rules and the questions a design must answer.",
 "cover_photo": "wagons.jpg",
 "cover_position": "right center",
 "cover_credit": "Photo by Paul Seling on Pexels (https://www.pexels.com/photo/12327462/), Pexels License",
 "cover_line": "A requirement for an industrial data ontology",
 "cluster": "ontologies",
 "owned_keyword": "ontologies"
}
---

An industrial data ontology, for a freight wagon fleet, is one governed model of what a wagon is and what happens to it, filled from the operator's own registers and files, with every fact tied to the register page, ledger entry or builder's document it came from. This post publishes the requirement we put to [CodeNinja Praxis](https://codeatoms.ai/praxis/) for such a model: a rail freight operator in Pakistan, described by class, asking for a single queryable truth about its wagons where today there are paper registers in many hands. How we define and build these models is on the [industrial data ontology](https://codeatoms.ai/industrial-data-ontology/) page.

## Why a wagon fleet

The operator's freight fleet carries petroleum, containers, coal, fertilizer, wheat and rock phosphate across a national network. Public reporting on the operator puts its freight business at over eight million tonnes moved last financial year, and hundreds of new high capacity wagons are being inducted in 2026, some imported and some built locally, alongside an ageing legacy fleet. Wagons are maintained at divisional sick lines and periodically overhauled at central workshops, and the new wagons arrive from two builders with their own documentation and spares.

Each wagon has a history of examinations, repairs, wheel turnings, brake overhauls and component changes. That history exists, but it lives in workshop registers, divisional ledgers and, for the newest wagons, the builders' delivery files. So the operator cannot answer a simple question about a wagon. Which wagons of one batch have had a bogie component changed twice. Which wagons are due for periodic overhaul this quarter, and where are they. Which wagons were in the consist of the last three derailments. Each answer is a week of clerks' work across several workshops and ledgers kept in different words.

Two pressures make this urgent. New wagons are arriving with warranty terms the operator cannot enforce, because it cannot produce the maintenance history the builder asks for within the notice period. And the supervisors who know each workshop's registers by heart are retiring, taking the index in their heads with them.

## The systems of record

The rolling stock register, the workshop job cards and registers, the divisional examination books, the stores ledgers for components and spares, the builders' delivery and warranty documents, the train running records, and the accident and derailment inquiry files. Every fact the system holds is tied back to one of them, with its date and the workshop that wrote it.

## What the operator asks for

1. **An industrial data ontology** of the freight fleet, owned by the operator: one governed model of what a wagon is and what happens to it, filled from the registers and the builders' files, with open weight models on the operator's own hardware in the country reading the paper and the ledgers, and nothing about the fleet leaving the country or reaching a foreign model service.
2. **The ontology itself.** Wagon, wagon type, batch, builder, bogie, wheelset, brake assembly, coupler, component serial, examination, repair, overhaul, job card, store issue, warranty claim, consist, journey, incident and location, each fact tied to its source register, page or file.
3. **Named agents that draft, officers who decide.** A register reading agent, triggered by a scanned register page or a builder's file, drafts the wagon facts it contains in the ontology's terms with the page cited, confirmed by the workshop records clerk. An overhaul due agent, triggered by month start, drafts the wagons due for periodic overhaul with their last known location and open repairs, approved by the divisional mechanical engineer. A warranty agent, triggered by a component failure on a new wagon, drafts the claim with the maintenance history the builder requires, approved by the chief mechanical engineer's office.
4. **Memory.** Every confirmed reading and every accepted claim is kept, so the next register page and the next claim are read better, without training a model on the fly.
5. **A command centre** for the mechanical department: the fleet by type, batch, overhaul status and location, registers digitised by workshop, agent drafts awaiting confirmation, and a conversational interface that answers in English and Urdu with citations to the register page.
6. **The model named.** Reasoning runs on GLM 5.3 open weights, self hosted on the operator's own hardware in Pakistan.

## The rules that bind

- **In country.** Fleet records never leave the operator's network. Models are open weights on hardware the operator owns. No third party model service.
- **Rules.** The railway's general and subsidiary rules on rolling stock examination, the public procurement rules that govern the builders' contracts and warranties, the national data protection rules for staff records appearing in the registers, and the audit requirements of the national audit office. The design names the approvals it needs.
- **Registers remain the record.** The ontology cites the register. It does not replace it until the department says so, and no agent closes a job card or files a claim without a named approval.
- **People decide.** Agents read and draft. Clerks, engineers and officers confirm.

## What success looks like

Phase one covers one wagon type, the new high capacity wagons from both builders, and the two workshops that maintain them, for one quarter. It is measured against a baseline of days to answer a wagon history question, overhaul due lists produced on time, warranty claims accepted by the builders, and register pages digitised with confirmed accuracy. The event the design is tested on is a bogie component failing on a wagon from the newest batch, with the full history drafted from the registers and the claim filed within the builder's notice period.

## What makes it an industrial data ontology

Three things separate this from a document scanning project.

The objects are typed, not imaged. A scanned register is a picture of a fact. The ontology holds the fact itself, a wheel turning on a named wagon on a date at a named workshop, as an object a query can reach, with the scan as its citation. More patterns of this kind are collected as [industrial ontology examples](https://codeatoms.ai/industrial-ontology-examples/).

The model is owned and governed by the operator. The vocabulary of wagon, batch, overhaul and claim is the operator's own, written down once and enforced everywhere, so two workshops that kept the same fact in different words now write it the same way.

The ontology is where agents and people meet. Every agent drafts in the ontology's terms and every officer confirms against the cited page, so each confirmed reading becomes memory that improves the next one, in context, never by retraining weights.

## Questions the design must answer

1. What runs where on the operator's hardware, the hardware class and size, and the three year cost computed from the models' own weights.
2. How the ontology is built from paper registers, ledgers and builders' files and kept current job card by job card.
3. How a register reading and a warranty draft are explained to a clerk and to the audit office.
4. How confirmed outcomes become memory that improves the next reading.
5. Phase one's gates for extending to the legacy fleet and the other workshops.

The published designs that already answer parts of this, asset registers and maintenance history among them, are collected as [physical AI system design](https://codeatoms.ai/physical-ai-system-design/) and as [sovereign AI reference architectures](https://codeatoms.ai/sovereign-ai-reference-architectures/). Every object model is in the [Vertical-Driven Architectures dataset](https://huggingface.co/datasets/CodeNinjatools/vertical-driven-architectures).

## About CodeNinja

CodeNinja is a Middle Eastern-American artificial intelligence lab focused on building self-improving systems. We are reinventing knowledge work to close the loop between vertical AI use cases and the generalized intelligence that fuels it, accelerating the path toward organizational superintelligence.
