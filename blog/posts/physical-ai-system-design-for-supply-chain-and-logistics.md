---
{
 "title": "Physical AI System Design for Supply Chain and Logistics: What the Published Designs Already Answer",
 "subtitle": "No supply chain design has been published in this series yet. Eight of the eighteen open reference architectures already answer the questions a logistics network asks first: one picture across the nodes from the systems they already run, gate and yard turn time, whether a terminal's inventory reading can be trusted, which vehicle in the fleet is raising a fault, what is connected to the control networks at each site, counting what moves, incidents before they happen, and what a records only study can settle before any sensor is bought.",
 "author": "CodeNinja Atoms",
 "author_role": "Research distribution",
 "author_url": "https://codeatoms.ai/about/",
 "date": "2026-10-19",
 "tags": [
  "Engineering",
  "Supply Chain",
  "Sovereign AI"
 ],
 "audience": "For a logistics operator, carrier, terminal or distribution network's operations, fleet, safety or OT security lead, and the engineers who would build with them, deciding what a first physical AI system should hold.",
 "description": "A supply chain and logistics sector guide built from eight published open reference architectures: which design answers a governed twin across nodes from existing systems, truck turn time at the gate and yard, deterministic inventory integrity at a fuel terminal, fleet fault logic executed on the vehicle, OT security monitoring with compliance evidence, independent counting of what moves, incident prediction on self hosted models and a records only reliability study, what every one of them keeps constant, and what a first supply chain design would have to name.",
 "cluster": "supply chain and logistics",
 "cover_line": "Eight of the eighteen open reference architectures already answer the first questions a logistics network asks"
}
---

A logistics network asks the same first questions whether it runs terminals and distribution centers in the United States or a fuel and freight corridor in Pakistan: what is happening across every node right now in one picture, why the trucks at the gate are waiting, whether the inventory a terminal reports is the inventory it holds, which vehicle in the fleet is about to fail, what is connected to the control networks at each site and can that be proven, how much moved against what the records say moved, and which site is drifting toward an incident. The series on this site holds no supply chain design yet. It holds eighteen open reference architectures in other sectors, and eight of them are written for an operation that asks one of those questions at a single node. This guide reads them as a network operator would, using only what each paper says. A guide for the building itself, the warehouse and its docks, aisles and conveyors, is [Physical AI System Design for Warehousing and Intralogistics](https://codeatoms.ai/blog/physical-ai-system-design-for-warehousing/); this one reads the network between the buildings.

## The map

| The network's question | The published design that answers it | Where it was written for |
|---|---|---|
| One picture across the nodes from the systems they already run | [Port Twin](https://codeatoms.ai/port-digital-twin-us/) | A landlord port authority in the United States |
| Why the trucks at the gate and yard are waiting | [Terminal Pulse](https://codeatoms.ai/truck-turn-container-terminal-us/) | A container terminal in the United States |
| Whether a terminal's inventory reading can be trusted | [Loop Integrity Watch](https://codeatoms.ai/tank-gauge-integrity-pakistan/) | A fuel terminal in Pakistan |
| Which vehicle in the fleet is raising a fault | [Consist Watch](https://codeatoms.ai/rail-fleet-condition-monitoring-us/) | A 225 car commuter rail fleet in the United States |
| What is on the control networks at each site, and the evidence an audit asks for | [Grid Context Watch](https://codeatoms.ai/ot-security-cip-evidence-us/) | An energy and utilities operator in the United States |
| How much moved, counted independently | [Steel Count Ledger](https://codeatoms.ai/steel-production-count-pakistan/) | Steel mills in Pakistan, counted for a public authority |
| Which site is drifting toward an incident | [Sovereign HSE Watch](https://codeatoms.ai/sovereign-hse-pakistan/) | An oil and gas operator in Pakistan |
| What the records already prove | [Reliability Atlas](https://codeatoms.ai/plant-reliability-assessment-saudi-arabia/) | Desalination and treatment plants in Saudi Arabia |

## One picture across the nodes

Port Twin is the design to read when the problem is that every dashboard is a slice. It binds 8 operational systems, 5 live sensor feeds and 1 finance backbone into 13 typed objects and 13 links with the berth as the focal object, joined through three adapter families and one event backbone. The rule a network operator will recognise is the boundary: the twin shows, and pilots, berth planners, engineers and finance staff decide in their own systems, with nothing written back into a system of record. The only model in the register is one self hosted open model, BGE-M3, for document retrieval, about 1.1 GB of fp16 weights on the port's existing enterprise virtual machines, so no equipment is bought. For a logistics network, the transport management system, the warehouse management systems, the telematics feed and the finance system take the places of the port's systems; the pattern of a read only twin over owned systems carries across unchanged, and the object at the centre is the one the network chooses, a shipment, a load or a lane.

## Gate and yard turn time

Terminal Pulse predicts truck turn time two hours out at a container terminal and watches the yard live. The paper's own numbers frame the problem every gate office knows: turn time averages 54 minutes and spikes above 90, and the causes live in separate systems, so planners stitch them together at the morning and afternoon operations meetings and a spike is explained hours after the trucks felt it. The design joins eleven systems, among them the terminal operating system, the gate system, two crane management systems, reefer monitoring, railroad switch lists, cameras and weather and tide feeds, into twelve objects that include the truck visit, the gate lane, the yard block and the transfer zone. Five self hosted open models carry the work: GLM 5.3 for reasoning, Chronos-2 for forecasting, Qwen3-Embedding-0.6B for retrieval, and RF-DETR with Roboflow trackers for vision. Two choices transfer directly to a distribution center's yard or a cross dock gate. The first rollout gate proves or redirects the yard side hypothesis using gate OCR data the operator already holds, before anything else is built. And the surfaces warn and propose while the named planner acts inside the terminal operating system; write back into that system is a second phase option gated on labour and IT sign off. The owned stack is costed at about 722,000 US dollars over three years. The operator in this paper is an illustrative scenario, not a customer.

## Terminal inventory that fails loudly

Loop Integrity Watch answers a question every bulk terminal in a fuel or chemical supply chain shares: is the level reading arriving at the central host continuous, undistorted and attributed to the right tank. The paper names the failure an inventory planner will know, a flatlined gauge reads as a plausible low level and a swapped gauge makes two tanks trade identities, and either one sends a wrong number into every replenishment decision downstream. The design covers 13 fuel tanks on 3 Modbus RTU loops, with 3 booster installations engineered from a measured signal survey inside explosion proof junction boxes, and a governed inventory ontology of 15 typed objects with the fuel tank as the focal object, joined from 2 named source systems through 1 integration adapter family. The model register is empty: every integrity check (stuck value, swap, distortion) is deterministic. The compute is two containers on the operator's own site application server, inside its OT boundary, and every data quality event is acknowledged and resolved by a named person, with the location engineer signing acceptance.

## Fleet faults: the operator's own logic, executed on the vehicle

Consist Watch monitors 225 commuter rail cars, and the part a truck, trailer or locomotive fleet can take is where the logic runs. An onboard module reads 64 named signals per car, 32 digital and 32 analog plus an accelerometer and GPS, and executes the operator's own fault logic table verbatim at the car. Telemetry rides the vehicle's existing cellular routers, a named mechanical desk controller owns every active fault in that territory, and alerts reach named recipient groups by severity. No training run was needed: Chronos-2 handles analog anomaly detection and seasonal trending, and a self hosted open weight reasoning model carries the work surface over the fleet ontology. Centrally it runs on one 141 GB HBM GPU class node in a contractor-hosted US cloud, about 625,000 US dollars for three years on the deepest AWS commitment in US East. A truck maker already publishes the fault codes for its vehicles; this design says where to execute them and who owns the result.

## The control networks at every site, with the evidence

Grid Context Watch is the design for the question an OT security lead and a compliance lead ask together, and a network of terminals, pipelines and automated sites asks it once per site: what is connected to the control networks, whether anything on them is behaving abnormally, and whether that can be proven with evidence when the auditor arrives. It joins 10 source systems, among them the SIEM, an OT detection tool, an IT monitoring platform, the energy management system and the substation data platform, through 2 adapter families into 14 typed objects and 14 links with the OT asset as the focal object, including the vulnerability finding, the detection rule, the pcap evidence record and the CIP evidence artefact. The boundary is read only and one way out of the control networks, and no data leaves the operator. GLM 5.2 (MIT) reasons and Qwen3-Embedding-0.6B (Apache-2.0) retrieves, on one node of eight 141 GB HBM class GPUs; owning that node costs about 510,000 dollars over three years, about four fifths the deepest three-year AWS commitment. Every triage, case and risk acceptance carries a named OT security analyst; agents draft, the analyst decides. The paper's evidence artefacts are written for NERC CIP; a pipeline or terminal operator puts its own security directive in that place, and the shape of control networks watched one way and proven by record carries across.

## Counting what moves

Steel Count Ledger puts IP66 HDR cameras and one sealed GPU industrial PC at every installation point, counts product as it is made, and publishes the counts through a one way link into one record the authority owns. Counting survives a slow wide area link because it happens at the edge, tracker models keep one item from counting twice, and the weighbridge feed serves as acceptance ground truth. Every discrepancy case is judged by a named revenue field officer; the system counts and reconciles and never assesses, and the mill never edits a count. For a supply chain, the same pattern gives an independent count at every handover point, a dock door, a weighbridge or a gate, against what the shipping record says moved, with the detector fine tuned per product type and site as the paper describes.

## Incidents before they happen

Sovereign HSE Watch predicts health, safety and environment incidents by joining 8 systems: SAP EHS, PM and QM; SCADA; fire and gas; Vision AI cameras; SQL databases; scanned files; and the identity provider. Its 12 typed objects include the HSE incident, the near miss report, the corrective action, the sensor reading, the anomaly event and the agent recommendation, which is the shape a network of depots and terminals already keeps on paper and in separate tools, site by site. Six self hosted open weight models carry the work, including GLM 5.3 for reasoning, Chronos-2 for forecasting, RF-DETR for vision, BGE-M3 for retrieval and PaddleOCR-VL 1.6 for scans, with GLM 5.3 held at FP8 on one node of eight 141 GB HBM class GPUs (753 GB of weights, 904 GB with headroom). Every recommendation is approved or rejected by a named person, and nothing executes on equipment.

## What the records already prove

Reliability Atlas is the design to read before any sensor is bought. It joins each plant's work orders, trip history and design documents through 3 read only adapters, as exports rather than live interfaces, into a reliability object model of 13 typed objects the operator owns, among them the equipment, the failure mode, the downtime event, the criticality index and the spare part. Availability is computed by Monte Carlo simulation on reliability block diagrams built from each plant's own failure study, auditable to ISO 55000, with predictions accepted only by a named reviewer and root cause reports validated only by a named engineer. The model register is empty by design, no hardware is bought, and the study runs on the operator's own in country servers. A network with a maintenance system and years of downtime records for its cranes, conveyors, pumps and vehicles can run this study first and let it decide which of the designs above it needs second.

## What every one of them keeps constant

Across all eight, four things do not vary. The system runs on hardware the operator controls, or in a cloud or region the operator chose. A named person owns every decision, and nothing executes on equipment. The object model is published as JSON in the hyper-ontology/1 format, so a logistics operator can read the exact objects and links before building any of its own. And the cost is computed the same way in every appendix, from the paper's own sizing with every price cited, so the own or rent question has one answer per design rather than a slogan; the comparison across designs is in [Own or Rent the GPUs](https://codeatoms.ai/blog/own-or-rent-the-gpus/), and every design is listed by pattern among the [sovereign AI reference architectures](https://codeatoms.ai/sovereign-ai-reference-architectures/).

## What a first supply chain design would have to name

None of the eight holds a shipment, a load, a lane, a carrier, a purchase order or a delivery appointment as an object, and none reasons across two nodes at once. Terminal Pulse holds a truck visit and Port Twin holds a berth, which are the nearest shapes, but each stops at its own fence. No published design follows a load from one site to the next, or explains why a delivery that left on time arrived late. A first supply chain design adds that object model, and the join between the nodes with it. It is the design the [co-build page for supply chain and logistics](https://codeatoms.ai/co-build/supply-chain-and-logistics/) is open for: the operator brings the operation, the systems that already hold its records and one engineer who knows the network; the published designs above are the proof of what comes out.

## Use the designs

Every object model named here is in the paper's package as `ontology/objects.json`, and the same rows are in the [Vertical-Driven Architectures dataset](https://huggingface.co/datasets/CodeNinjatools/vertical-driven-architectures) and served live by the [codeninja-research MCP server](https://github.com/muhammadumar89/codeninja-research/tree/main/mcp-server), so a coding agent can ask which published design holds a truck visit or a fuel tank object and read why. Each paper is citable by its DOI on its page. All were reasoned on [CodeNinja Praxis](https://codeatoms.ai/praxis/) and their object models import into [Hyper Ontology](https://codeatoms.ai/hyper-ontology/).

## About CodeNinja

CodeNinja is a Middle Eastern-American artificial intelligence lab focused on building self-improving systems. We are reinventing knowledge work to close the loop between vertical AI use cases and the generalized intelligence that fuels it, accelerating the path toward organizational superintelligence.
