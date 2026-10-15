# Physical AI System Design for Mining: What the Published Designs Already Answer

*No mining design has been published in this series yet. Eight of the eighteen open reference architectures already answer the questions a mine asks first: people and vehicles on haul roads, mobile fleet and fixed plant condition, incidents before they happen, fire and life safety, counting what leaves the plant, and what a records-only study can settle before any sensor is bought.*

Canonical: https://codeatoms.ai/blog/physical-ai-system-design-for-mining/
Author: CodeNinja Atoms, Research distribution
Published: 2026-10-15
License: CC BY 4.0
Publisher: CodeNinja Atoms (https://codeatoms.ai), a fully owned subsidiary of CodeNinja
A mine asks the same first questions whether it is an open pit in Saudi Arabia or an underground operation in the United States: who is near a haul truck right now, which machine is about to fail, which shift is drifting toward an incident, is the fire protection at the plant actually armed, and how much ore left the gate against what was declared. The series on this site holds no mining design yet. It holds eighteen open reference architectures in eight other sectors, and eight of them are written for an operation that asks one of those questions in another setting. This guide reads them as a mining operator would, using only what each paper says.

## The map

| The mine's question | The published design that answers it | Where it was written for |
|---|---|---|
| Who is near the vehicles on the haul road | [Pit Camera Watch](https://codeatoms.ai/test-site-camera-monitoring-us/) and [Structure Phase Watch](https://codeatoms.ai/structure-phase-construction-saudi-arabia/) | A vehicle proving ground in the United States; a construction site in Saudi Arabia |
| Which mobile machine is about to fail | [Consist Watch](https://codeatoms.ai/rail-fleet-condition-monitoring-us/) | A 225-car commuter rail fleet in the United States |
| Which fixed plant is about to fail | [Turbine Island Watch](https://codeatoms.ai/steam-turbine-condition-monitoring-pakistan/) | A combined cycle power plant in Pakistan |
| Which shift is drifting toward an incident | [Sovereign HSE Watch](https://codeatoms.ai/sovereign-hse-pakistan/) | An oil and gas operator in Pakistan |
| Is the fire protection armed | [Factory Fire Watch](https://codeatoms.ai/factory-fire-monitoring-saudi-arabia/) | High-risk factories across industrial cities in Saudi Arabia |
| How much product left the gate | [Steel Count Ledger](https://codeatoms.ai/steel-production-count-pakistan/) | Steel mills in Pakistan, counted for a public authority |
| What the records already prove | [Reliability Atlas](https://codeatoms.ai/plant-reliability-assessment-saudi-arabia/) | Desalination and treatment plants in Saudi Arabia |

## People and vehicles on the haul road

Pit Camera Watch is a fully on-premises camera system for a vehicle proving ground: 40 to 60 poles of fixed thermal and visible camera heads on new underground fiber, 80 to 120 streams, recorded on an N+1 pair of open-source recorders holding 30 days of footage on local disk inside an isolated network. The design's human rule is the one a mine's safety office will recognise. Booth operators watch and decide, nothing raises an automated alarm, and only the safety office can export a clip. The one model in the register, an Apache-2.0 detector of about 8 to 124 MB, searches the archive after the fact for a test vehicle, a support vehicle or a pedestrian; it does not sit in the live safety path. For a haul road, the same shape holds: the footage is the operator's, the retrospective search is what an investigation runs, and the decision about a near miss stays with a person.

Structure Phase Watch adds the part a pit needs and a proving ground does not: edge compute in the field. Its five solar powered edge nodes sit at the gate, the laydown area, the crane slew zone, the batch plant and the haul road, and every breach alert is confirmed, dismissed or escalated by the HSE officer. Its open item of 13 October is the most mining-relevant sentence in the series: the paper names dust, glare and heat as what degrades the camera lenses, and the answer recorded on the paper's page is both a cleaning rota set by the site's dust season and a confidence drop on a fixed reference target in each camera's view that opens a work order for a named person, with the camera's health held in the object model as a record someone owns.

## Mobile fleet: the operator's own fault logic, executed at the machine

Consist Watch monitors 225 commuter rail cars. The part a mining fleet can take verbatim is where the logic runs. An onboard module reads 64 named signals per car, 32 digital and 32 analog plus an accelerometer and GPS, and executes the operator's own fault-logic table at the car. Telemetry rides the vehicle's existing cellular routers, and severity-ranked faults reach a named mechanical desk controller who owns every active fault in that territory, with alerts routed by severity to named recipient groups. The module is specified to the rail standards for shock, vibration and temperature. A haul truck's manufacturer already publishes the fault codes; this design says where to execute them, who owns the result, and that no training run was needed: an open-weight time series model handles analog anomaly detection and seasonal trending, and a self-hosted open-weight reasoning model carries the agentic work surface over the fleet ontology.

## Fixed plant: advise, never trip

Turbine Island Watch reads a rehabilitated steam turbine generator through a one-way path from the distributed control system, the vibration monitoring rack and the generator protection systems. Three of its rules transfer to a mill, a crusher or a conveyor drive without change. The read is one-way and nothing writes back to the control system. The platform advises and the protection layer trips, so every alert carries a prescribed action that a named shift operator acknowledges. And the rollout gate is a number: two false alerts per week, with thresholds tuned only on channels that have provable history. The compute is one 48 GB inference card on ruggedised edge servers inside the plant perimeter, costed at about 22,500 US dollars to own over three years.

## Incidents before they happen

Sovereign HSE Watch predicts health, safety and environment incidents at an oil and gas operator by joining eight systems: the enterprise HSE, maintenance and quality modules, SCADA, fire and gas, vision cameras, SQL databases, scanned files and the identity provider. Every recommendation is approved or rejected by a named person and nothing executes on equipment. It runs six self-hosted open-weight models on one node of eight 141 GB HBM-class GPUs, and its first rollout gate is not a model but a licence: 141 GB-class accelerators need a US export licence for Pakistan, so the rollout confirms installed hardware before anything else. A mine in the same country group inherits that gate unchanged, and a mine in Saudi Arabia reads the Structure Phase Watch appendix for the equivalent arithmetic.

## Fire and life safety, read only

Factory Fire Watch gives live visibility of fire alarm panels, fire pumps, fire water tanks and energy meters across an operator's highest-risk sites, read through panel contacts, PLC inputs and LoRaWAN into an IoT platform hosted in the Kingdom, with never a write path into certified life-safety equipment. No server or GPU is bought. The field equipment per site is about 2,600 to 3,200 US dollars in list prices, and a monitoring officer acknowledges or escalates every safety-critical alert. For a processing plant and a camp, the design is the same read-only estate with the sites renamed.

## Counting what leaves the plant

Steel Count Ledger puts cameras and one sealed GPU industrial PC at every casting strand and cooling bed, counts product as it is made, and publishes the counts through a one-way link into one record the authority owns. Counting survives a slow wide-area link because it happens at the edge. Every discrepancy case is judged by a named revenue field officer; the system counts and reconciles and never assesses, and the mill never edits a count. The same pattern counts trucks at a weighbridge or product at a load-out, with the detector fine-tuned per product type and site as the paper describes.

## What the records already prove

Reliability Atlas is the design to read before any sensor is bought. It joins each plant's work orders, trip history and design documents through three read-only adapters, as exports rather than live interfaces, into a reliability object model the operator owns. Availability is computed by Monte Carlo simulation on reliability block diagrams built from each plant's own failure study, auditable to ISO 55000, with predictions accepted only by a named reviewer and root cause reports validated only by a named engineer. The model register is empty by design, no hardware is bought, and the study runs on the operator's own in-country servers. A mine with a maintenance system and a historian can run this study first and let it decide which of the designs above it needs second.

## What every one of them keeps constant

Across all eight, four things do not vary. The system runs on hardware the operator controls, or in a cloud the operator chose in its own country; the papers for Pakistan say plainly that no hyperscaler runs a region there. A named person owns every decision, and nothing executes on equipment. The object model is published as JSON in the hyper-ontology/1 format, so a mine can read the exact objects and links before building any of its own. And the cost is computed the same way in every appendix, from the paper's own sizing with every price cited, so the own or rent question has one answer per design rather than a slogan; the comparison across designs is in [Own or Rent the GPUs](https://codeatoms.ai/blog/own-or-rent-the-gpus/).

## What a first mining design would have to name

None of the eight holds a haul truck, a light vehicle, a haul road segment or a pedestrian exclusion zone as an object, and none holds a near miss between them. That is the object model a first mining design adds, and it is the design the [co-build page for mining](https://codeatoms.ai/co-build/mining/) is open for: the operator brings the operation, the systems that already hold its records and one engineer who knows the site; the published designs above are the proof of what comes out.

## Use the designs

Every object model named here is in the paper's package as `ontology/objects.json`, and the same rows are in the [Vertical-Driven Architectures dataset](https://huggingface.co/datasets/CodeNinjatools/vertical-driven-architectures) and served live by the [codeninja-research MCP server](https://github.com/muhammadumar89/codeninja-research/tree/main/mcp-server), so a coding agent can ask which published design holds a monitoring module or a fault history object and read why. Each paper is citable by its DOI on its page. All were reasoned on [CodeNinja Praxis](https://codeatoms.ai/praxis/) and their object models import into [Hyper Ontology](https://codeatoms.ai/hyper-ontology/).

## About CodeNinja

CodeNinja is a Middle Eastern-American artificial intelligence lab focused on building self-improving systems. We are reinventing knowledge work to close the loop between vertical AI use cases and the generalized intelligence that fuels it, accelerating the path toward organizational superintelligence.
