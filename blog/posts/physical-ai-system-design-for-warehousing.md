---
{
 "title": "Physical AI System Design for Warehousing and Intralogistics: What the Published Designs Already Answer",
 "subtitle": "No warehousing design has been published in this series yet. Nine of the eighteen open reference architectures already answer the questions a warehouse or distribution center asks first: one picture of the operation from the systems it already runs, dock and yard turn time, people and vehicles seen on camera, fleet and fixed equipment condition, fire and life safety, counting what leaves, and what a records only study can settle before any sensor is bought.",
 "author": "CodeNinja Atoms",
 "author_role": "Research distribution",
 "author_url": "https://codeatoms.ai/about/",
 "date": "2026-10-16",
 "tags": [
  "Engineering",
  "Warehousing",
  "Sovereign AI"
 ],
 "audience": "For a warehouse or distribution center's operations, safety or engineering lead, and the engineers who would build with them, deciding what a first physical AI system should hold.",
 "description": "A warehousing and intralogistics sector guide built from nine published open reference architectures: which design answers a governed twin of the operation from existing systems, truck turn time at the gate and yard, people and vehicles on camera, fleet fault logic and fixed equipment condition, read only fire and life safety monitoring, independent counting of what leaves and a records only reliability study, what every one of them keeps constant, and what a first warehousing design would have to name.",
 "cluster": "warehousing and intralogistics",
 "cover_line": "Nine of the eighteen open reference architectures already answer the first questions a warehouse asks"
}
---

A warehouse asks the same first questions whether it is a distribution center in the United States or a cross dock in Saudi Arabia: what is happening across the building right now in one picture, why the trucks at the dock are waiting, who is walking where the forklifts drive, which conveyor or sorter drive is about to stop, is the fire protection actually armed, and how much left the building against what the system says shipped. The series on this site holds no warehousing design yet. It holds eighteen open reference architectures in other sectors, and nine of them are written for an operation that asks one of those questions in another setting. This guide reads them as a warehouse operator would, using only what each paper says.

## The map

| The warehouse's question | The published design that answers it | Where it was written for |
|---|---|---|
| One picture of the operation from the systems it already runs | [Port Twin](https://codeatoms.ai/port-digital-twin-us/) | A landlord port authority in the United States |
| Why the trucks at the dock and yard are waiting | [Terminal Pulse](https://codeatoms.ai/truck-turn-container-terminal-us/) and [Structure Phase Watch](https://codeatoms.ai/structure-phase-construction-saudi-arabia/) | A container terminal in the United States; a construction site in Saudi Arabia |
| Who is near the forklifts and yard vehicles | [Pit Camera Watch](https://codeatoms.ai/test-site-camera-monitoring-us/) and [Terminal Pulse](https://codeatoms.ai/truck-turn-container-terminal-us/) | A vehicle proving ground in the United States; a container terminal in the United States |
| Which vehicle in the fleet is raising a fault | [Consist Watch](https://codeatoms.ai/rail-fleet-condition-monitoring-us/) | A 225 car commuter rail fleet in the United States |
| Which conveyor or sorter drive is about to fail | [Turbine Island Watch](https://codeatoms.ai/steam-turbine-condition-monitoring-pakistan/) | A combined cycle power plant in Pakistan |
| Is the fire protection armed | [Factory Fire Watch](https://codeatoms.ai/factory-fire-monitoring-saudi-arabia/) | High risk factories in Saudi Arabia |
| How much product left the building | [Steel Count Ledger](https://codeatoms.ai/steel-production-count-pakistan/) | Steel mills in Pakistan, counted for a public authority |
| What the records already prove | [Reliability Atlas](https://codeatoms.ai/plant-reliability-assessment-saudi-arabia/) | Desalination and treatment plants in Saudi Arabia |

## One picture from the systems already running

Port Twin is the design to read when the problem is that every dashboard is a slice. It binds eight operational systems, five live sensor feeds and one finance backbone into a thirteen object model with the berth as the focal object, joined through three adapter families and one event backbone. The rule a warehouse will recognise is the boundary: the twin shows, and pilots, berth planners, engineers and finance staff decide in their own systems, with nothing written back into a system of record. The only model in the register is one self hosted open weight embedding model, BGE-M3, for document retrieval, about 1.1 GB of weights on virtual machines the port already runs, so no equipment is bought. For a distribution center, the warehouse management system, the transport management system, the yard system and the building's sensors take the places of the port's systems, and the dock door takes the place of the berth; the pattern of a read only twin over owned systems carries across unchanged.

## Dock and yard turn time

Terminal Pulse predicts truck turn time two hours out at a container terminal and watches the yard live. The paper's own numbers frame the problem a dock office knows: turn time averages 54 minutes and spikes above 90, and the causes live in separate systems, so planners stitch them together at the morning and afternoon operations meetings and a spike is explained hours after the trucks felt it. The design joins eleven systems, among them the terminal operating system, the gate system, two crane management systems, reefer monitoring, railroad switch lists, cameras and weather and tide feeds, into twelve objects that include the truck visit, the gate lane, the yard block and the transfer zone. Five self hosted open models carry the work: GLM 5.3 for reasoning, Chronos-2 for forecasting, Qwen3-Embedding-0.6B for retrieval, and RF-DETR with Roboflow trackers for vision. Two choices transfer directly to a dock. The first rollout gate proves or redirects the yard side hypothesis using gate OCR data the operator already holds, before anything else is built. And the surfaces warn and propose while the named planner acts inside the terminal operating system; write back into that system is a second phase option gated on labour and IT sign off. The owned stack is costed at about 722,000 US dollars over three years. The operator in this paper is an illustrative scenario, not a customer.

Structure Phase Watch adds the inbound side: gate movements and delivery windows are objects in its model, read from haulage GPS, gate logs and biometric turnstiles, and every delivery window it drafts is a recommendation recorded with the approver. Its open item of 13 October is the one any camera estate on a loading apron will meet: the paper names dust, glare and heat as what degrades the lenses, and the answer recorded on its page is a cleaning rota plus a confidence drop on a fixed reference target in each camera's view that opens a work order for a named person, with the camera's health held in the object model as a record someone owns.

## People and vehicles on camera

Pit Camera Watch is a fully on premises camera system for a vehicle proving ground: 40 to 60 poles of thermal and visible camera heads, 80 to 120 streams, recorded on an N+1 pair of open source recorders holding 30 days of footage on local disk inside an isolated network. Its human rule is the conservative one a warehouse safety office may want first. Booth operators watch and decide, nothing raises an automated alarm, and only the safety office can export a clip. The one model, D-FINE under Apache-2.0 at about 8 to 124 MB of weights, searches the archive after the fact for a test vehicle, a support vehicle or a pedestrian; it is not in the live safety path. For aisles and docks, the same shape gives an investigation a searchable archive the operator owns without putting a model between a person and a near miss.

Terminal Pulse is the live counterpart. Its model holds a yard person, a transfer zone and a safety event, its detectors and trackers run in fanless enclosures at the yard blocks, gate and quay, no safety reflex crosses a network hop, and the named safety supervisor acknowledges every safety event. A warehouse choosing between the two is choosing whether the cameras search the past or watch the present, and both papers show what each choice costs in hardware and in human workload.

## Fleet faults: the operator's own logic, executed on the vehicle

Consist Watch monitors 225 commuter rail cars, and the part a forklift or tugger fleet can take is where the logic runs. An onboard module reads 64 named signals per car, 32 digital and 32 analog plus an accelerometer and GPS, and executes the operator's own fault logic table verbatim at the car. Telemetry rides the vehicle's existing cellular routers, a named mechanical desk controller owns every active fault in that territory, and alerts reach named recipient groups by severity. No training run was needed: Chronos-2 handles analog anomaly detection and seasonal trending, and a self hosted open weight reasoning model carries the work surface over the fleet ontology. A truck maker already publishes the fault codes for its vehicles; this design says where to execute them and who owns the result.

## Conveyors and sortation: advise, never trip

Turbine Island Watch reads a rehabilitated steam turbine generator through a one way path from the control system, the vibration monitoring rack and the generator protection systems. Three of its rules transfer to a conveyor drive, a sorter or a stacker crane without change. The read is one way and nothing writes to the control system. The platform advises and the protection layer trips, so every alert carries a prescribed action that a named shift operator acknowledges. And the rollout gate is a number: two false alerts per week, with thresholds tuned only on channels that have provable history. MOMENT-1 detects anomalies zero shot and no training run is needed. The compute is one 48 GB inference card on ruggedised edge servers inside the plant perimeter, costed at about 22,500 US dollars to own over three years.

## Fire and life safety, read only

Factory Fire Watch gives live visibility of fire alarm panels, fire pumps, fire water tanks and energy meters across an operator's highest risk sites, read through panel contacts, PLC inputs and LoRaWAN into an IoT platform hosted in the Kingdom, with never a write path into certified life safety equipment. No server or GPU is bought. The field equipment per site is about 2,600 to 3,200 US dollars in list prices, and a monitoring officer acknowledges or escalates every safety critical alert. The paper's framing suits a high bay building well: a sensor that has stopped reporting still reads as normal, so the design treats silence as a failure to be surfaced. For a distribution center and its sprinkler pumps, the design is the same read only estate with the sites renamed.

## Counting what leaves the building

Steel Count Ledger puts cameras and one sealed GPU industrial PC at every installation point, counts product as it is made, and publishes the counts through a one way link into one record the authority owns. Counting survives a slow wide area link because it happens at the edge, tracker models keep one item from counting twice, and the weighbridge feed serves as acceptance ground truth. Every discrepancy case is judged by a named revenue field officer; the system counts and reconciles and never assesses, and the mill never edits a count. The same pattern counts pallets or cases at an outbound dock door against what the warehouse management system says shipped, with the detector fine tuned per product type and site as the paper describes.

## What the records already prove

Reliability Atlas is the design to read before any sensor is bought. It joins each plant's work orders, trip history and design documents through three read only adapters, as exports rather than live interfaces, into a reliability object model the operator owns. Availability is computed by Monte Carlo simulation on reliability block diagrams built from each plant's own failure study, auditable to ISO 55000, with predictions accepted only by a named reviewer and root cause reports validated only by a named engineer. The model register is empty by design, no hardware is bought, and the study runs on the operator's own in country servers. A warehouse with a maintenance system and years of conveyor and sorter downtime records can run this study first and let it decide which of the designs above it needs second.

## What every one of them keeps constant

Across all nine, four things do not vary. The system runs on hardware the operator controls, or in a cloud or region the operator chose. A named person owns every decision, and nothing executes on equipment. The object model is published as JSON in the hyper-ontology/1 format, so a warehouse can read the exact objects and links before building any of its own. And the cost is computed the same way in every appendix, from the paper's own sizing with every price cited, so the own or rent question has one answer per design rather than a slogan; the comparison across designs is in [Own or Rent the GPUs](https://codeatoms.ai/blog/own-or-rent-the-gpus/).

## What a first warehousing design would have to name

None of the nine holds a storage location, a pick face, an order line, a dock door, a forklift or a pedestrian aisle as an object, and none holds slotting: which item belongs in which location, and why. Terminal Pulse holds a yard block and a container, which is the nearest shape, but no published design reasons over where stock should sit. A first warehousing design adds that object model, and the near miss between a person and a vehicle in an aisle with it. It is the design the [co-build page for warehousing and intralogistics](https://codeatoms.ai/co-build/warehousing-and-intralogistics/) is open for: the operator brings the operation, the systems that already hold its records and one engineer who knows the building; the published designs above are the proof of what comes out.

## Use the designs

Every object model named here is in the paper's package as `ontology/objects.json`, and the same rows are in the [Vertical-Driven Architectures dataset](https://huggingface.co/datasets/CodeNinjatools/vertical-driven-architectures) and served live by the [codeninja-research MCP server](https://github.com/muhammadumar89/codeninja-research/tree/main/mcp-server), so a coding agent can ask which published design holds a truck visit or a safety event object and read why. Each paper is citable by its DOI on its page. All were reasoned on [CodeNinja Praxis](https://codeatoms.ai/praxis/) and their object models import into [Hyper Ontology](https://codeatoms.ai/hyper-ontology/).

## About CodeNinja

CodeNinja is a Middle Eastern-American artificial intelligence lab focused on building self-improving systems. We are reinventing knowledge work to close the loop between vertical AI use cases and the generalized intelligence that fuels it, accelerating the path toward organizational superintelligence.
