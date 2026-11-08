# Sovereign AI Architecture for Distribution Loss and Theft Reduction in Pakistan

Canonical: https://codeatoms.ai/distribution-loss-theft-pakistan/
DOI: https://doi.org/10.5281/zenodo.24048559
PDF: https://codeatoms.ai/distribution-loss-theft-pakistan/paper/distribution-loss-theft-pakistan.pdf
License: CC BY 4.0
Publisher: CodeNinja Atoms (https://codeatoms.ai), a fully owned subsidiary of CodeNinja

VERTICAL-DRIVEN ARCHITECTURES · ENERGY & UTILITIES · DESIGNED WITH PRAXIS · NOVEMBER 2026

# Sovereign AI Architecture for Distribution Loss and Theft Reduction in Pakistan

Energy & Utilities Watch: One Living Picture of the Operation

Muhammad Umar, Cofounder, CodeNinja

For the leaders accountable for energy & utilities operations, their supervisors, and the data and platform engineers who would build and run it.

---

Vertical-Driven Architectures is a CodeNinja series of system designs. Every design in the series is driven by a real-world problem and scenario in a single industry, and every one is designed on Praxis, CodeNinja's platform for designing physical AI systems. Operations are described by class, never by name.

At a glance

## Sovereign AI Architecture for Distribution Loss and Theft Reduction in Pakistan

**What this is.** An open reference architecture for system design in physical AI, built for an electricity distribution company in Pakistan that serves several million customers through hundreds of grid stations and thousands of feeders, where owning the inference hardware that runs it costs about 641,000 US dollars over three years. When a transformer's monthly energy balance crosses its threshold, the design joins the smart meter interval load, the tamper events, the billing history, the network topology and the inspection record into one argument, so the subdivision engineer sees the ranked causes, the inspection officer opens a case file already populated with the load history and the billing record, and the revenue officer approves the correction. The models run entirely on the operator's own hardware in the country under the regulator's performance standards, the national data protection rules, the electricity theft laws and export control on the GPU node. It is written for the leaders accountable for loss reduction, their subdivision engineers and officers, and the data and platform engineers who would build and run it. The operator is described by class, never by name.

**The answer in numbers.**

| Part | The design |
| --- | --- |
| Sources | Seven read only systems of record, entering through one integration adapter family (a Kafka subscription for meter data, scheduled batch extracts for billing, energy audit, GIS and outage records, mapped connectors for the field app and the theft case register), each fact stamped with the system it came from: the customer information and billing system, the meter data management system, the energy audit records per feeder and transformer, the geographic information system of the network, the outage and complaint system, the meter reading and inspection app and the theft case register; the single write path out is the approved correction |
| Object model | 15 typed objects with 14 typed links, from the grid station, feeder, transformer, service connection and meter through the interval load, reading, billing account and tariff to the inspection, tamper event, theft case and recovery, with the agent draft and the approval that settles it; each anchored in one system of record and published as JSON for reuse |
| Models | GLM 5.3 (GLM-5.3 bespoke licence, 753B at FP8) for the loss, tamper and billing agents, the command center and ontology maintenance; BGE-M3 (MIT) for cited retrieval over tariff codes, meter numbers, PPC sections and inspection findings; Chronos-2 (Apache 2.0) forecasting each transformer's energy balance so the residual is the anomaly signal; no third party model service, nothing trained into weights |
| Compute | One node of eight 141 GB HBM GPUs (1,128 GB) holding 753 GB of FP8 weights with the 1.2 planning factor, 904 GB, plus one dual socket server with a 48 GB PCIe card for the embedder and the forecaster, both in an in-country sovereign data center or colocation on the operator's own hardware; no edge tier. The node is a 4A090 class item for a D:3 and D:4 destination, so the export licence determination precedes any card commitment, with a non US accelerator class held open |
| Rollout | Two phases carrying 16 scope items (15 and 1), each closed by a gate, never a date: one circle of feeders for one quarter against a measured baseline with unchanged control feeders, whose gate is the billing agent drafting corrections that land back through the recorded approval path, then the circle extension gate read on four numbers: transformer level loss, inspections per confirmed theft, case files accepted at the Grade 17 gate, and days from tamper event to inspection |
| Three-year cost | About 641,000 US dollars to own the node and the inference server for three years (a range of 615,000 to 667,000: servers, support and power at the regulator's uniform commercial tariff), against about 773,000 to rent the same cards on the deepest three year commitment in AWS Asia Pacific (Mumbai), so ownership costs about five sixths of it, and about 2.05 million on demand, against which ownership costs a little under a third. Renting is a price reference only, because AWS lists no Pakistan region and every rented option would carry customer and meter data across the border (Appendix A) |
| Human control | Agents draft and people decide, by name: the subdivision engineer approves the ranked causes and the inspection visits, the inspection officer approves the case file, the revenue officer approves the correction, and the Grade 17 officer signs the complaint; every approval carries the approver role, the officer grade, the timestamp, the artifact hash and a written reason, known answer probes police the approvers, and every confirmed cause and closed case is kept as the record the next ranking reads |

**Reuse it.** The object model, the model register and the figures are free to reuse under CC BY 4.0. Cite as <https://codeatoms.ai/distribution-loss-theft-pakistan/.>

**Made with.** Reasoned on [CodeNinja Praxis](<https://codeatoms.ai/praxis/>), the CodeNinja Atoms platform for designing physical AI systems. The object model imports into [Hyper Ontology](<https://codeatoms.ai/hyper-ontology/>), which turns it into a living system. Load it with the [hyper-ontology loader](../hyper-ontology-py/): `hyper-ontology show distribution-loss-theft-pakistan`. Both are in beta; access by request.

ABSTRACT

## The Answer Already Exists in the Systems the Operation Runs

A sovereign AI architecture for loss and theft reduction at an electricity distribution company in Pakistan: open weight models on the operator's own hardware in the country, reading its systems of record, with nothing about its customers leaving the country or reaching a foreign model service.

The design reads 7 source systems through 1 adapter family into one object model of 15 objects, runs 8 services over it and opens 5 surfaces to the people who decide, with 3 models placed where the data is. A sovereign, operator-owned platform that joins seven systems of record into one governed ontology of the network and its customers, computes each transformer's energy in against energy billed, and lets a loss agent, a tamper agent and a billing agent draft ranked causes, case files and corrections that subdivision engineers, inspection officers and revenue officers approve, with every confirmed outcome kept as a decision record that improves the next ranking, and every theft case ending in a court-ready Grade 17 complaint. Phase one runs one circle of feeders for one quarter against a measured baseline with unchanged control feeders, on GLM 5.3 self hosted in an in-country data center, gated on four numbers before any other circle is touched.

The paper covers the operation and the problem its systems cannot answer, the constraints, the stack, the object model, ingestion, inference placement, the models and their licenses, the rollout and its proof, ownership, and finally how Praxis contextualized and reasoned the design.

---

![Figure 1. Energy & Utilities Watch on one page: the sources the operation already runs, one object model, what it computes, and the person who decides.](https://codeatoms.ai/distribution-loss-theft-pakistan/figures/figure_01.png)

Figure 1. Energy & Utilities Watch on one page: the sources the operation already runs, one object model, what it computes, and the person who decides.

## Contents

Each chapter is tagged for the reader it serves most directly: Executive, Team Lead, FDE, Reference.

|  |  |  |
| --- | --- | --- |
|  | Abstract · The Answer Already Exists in the Systems the Operation Runs | Executive |
| PART I · THE PROBLEM | | |
| 1 | [A Daily Question Goes Unanswered in the Systems That Hold the Data](#ch1) | Executive |
| 2 | [Every System Sees One Slice of the Operation](#ch2) | ExecutiveTeam Lead |
| PART II · THE DESIGN | | |
| 3 | [Four Constraints Shape Everything Downstream](#ch3) | Team Lead |
| 4 | [One Stack Runs From the Systems of Record to the Surfaces](#ch4) | Team LeadFDE |
| 5 | [Fifteen Objects Turn Operational Data Into One Argument](#ch5) | FDE |
| 6 | [Every Source Enters Through an Adapter, Never Directly](#ch6) | FDE |
| 7 | [Inference Belongs Where the Data Is](#ch7) | FDE |
| 8 | [The License Decides What the Operator Can Own](#ch8) | FDEExecutive |
| PART III · THE ROLLOUT | | |
| 9 | [Shadow Mode Comes Before Any Flag Is Trusted](#ch9) | Team LeadExecutive |
| 10 | [The Intelligence Should Stay with the Operation That Produced It](#ch10) | Executive |
| PART IV · HOW IT WAS DESIGNED | | |
|  | Conclusion · The Pattern Repeats Wherever Systems of Record Do Not Meet | Executive |
| 11 | [How Praxis Contextualized and Reasoned This Design](#ch11) | Team LeadFDE |
|  | [Sources](#sources) | Reference |

PART I · CHAPTER 1

## A Daily Question Goes Unanswered in the Systems That Hold the Data

The operation holds every fact the question needs and no system answers it.

The abstract posed the question and promised a sovereign AI architecture that answers it inside the operator's boundary. This chapter states the question precisely, prices the cost of leaving it unanswered, and fixes the scenario the design must serve.

### 1.1  The Question and the Data It Requires

The operation needs one question answered every day for every transformer: why does the energy that entered leave a gap between what was measured in and what was billed downstream, and what should the inspection team do about it today. The data that answers it sits in four places at once. The energy entering each transformer comes from the feeder-head and transformer metering; the energy billed to every service connection downstream sits in the billing system; the topology that ties a meter to a transformer to a feeder sits in the geographic information system; and the human record of tamper events, inspections and closed cases sits in three further systems. The answer must also satisfy several regimes at once: the national program replacing every conventional meter by the end of 2026, a government-ordered technical audit of billing systems now under way, privatisation preparations that place every process under external scrutiny, and theft prosecutions brought under the Penal Code section for electricity theft, filed as a Grade 17 complaint before the Electricity Utilities Court. Those regimes constrain the means as well as the ends, because the operator's requirement is explicit that nothing about its consumers may leave the country or reach a foreign model service.

### 1.2  The Documented Cost of the Problem

The direct cost is stated in the operator's own requirement: companies of this class lose a large share of the energy they buy to technical losses, theft and unbilled supply, and the sector's distribution losses ran to hundreds of billions of rupees in the last financial year. The cost of mishandling the data that would fix it is documented publicly. A utility in North America paid a 2.7 million dollar penalty after a vendor exposed its data (Natlawreview 2018), and a Japanese utility was issued business improvement recommendations by its market surveillance commission after consumer information obtained through a third party was leaked and accessed (Chuden 2023). Energy sector operators are explicit targets of state-sponsored cyber actors (CISA 2022), and a regulator elsewhere has opened a board inquiry into a cybersecurity incident at a power company (Nserbt 2025). Any architecture that sends consumption records abroad to a hosted model service carries exactly this class of exposure, which is why the boundary is a cost line here and not a slogan.

### 1.3  The Operation as a Scenario

The operator is an electricity distribution company in Pakistan, described by class only. It distributes power through hundreds of grid stations and thousands of feeders to several million consumers, and it knows its losses by feeder a month late and by transformer almost never. The people in the loop are subdivision engineers who own feeders, inspection officers and field teams who visit meters and transformers, revenue officers who own billing corrections, and the Grade 17 officer who signs each theft complaint; the loss reduction team works from a command center, and all compute runs in an in-country data center or colocation on the operator's own hardware. The physical environments are the field, where inspections happen and photographs are taken, and that data center, where every model runs. The regulatory ground combines the meter replacement program, the billing audit, privatisation conditions and the Penal Code theft route through the Electricity Utilities Court. The design counts seven named systems of record, the roles listed above, and places counted as grid stations, feeders, transformers, circles, subdivisions and courts; phase one runs one circle of feeders for one quarter before any other circle is touched.

PART I · CHAPTER 2

## Every System Sees One Slice of the Operation

Each system of record sees its own part of the answer and none sees the whole.

Chapter 1 fixed the question and the regimes it must satisfy. This chapter walks the seven systems of record one by one and shows that each holds one slice of the answer and none holds the whole.

### 2.1  What Each System Sees

The consumer information and billing system sees every account with its billed units, tariff and arrears, but it cannot say which transformer feeds the premises or whether the billed units match the energy that reached it. The meter data management system sees interval load and tamper events for every smart meter, but not the billing history of the account behind that meter or what an inspection later found there. The energy audit records hold the loss percent per feeder each month and almost never per transformer, and they carry no tamper events, no inspections and no case outcomes. The geographic information system holds the topology from meter to transformer to feeder to grid station, which is the skeleton of every energy balance, but it holds no measurement at all. The outage and complaint system records outages and complaints with times and places, which is what separates a supply problem from theft, yet it cannot join either to the meters and accounts affected. The meter reading and inspection app holds field findings and photographs, but the team using it arrives without the tamper alarms or the billing history that would tell it where to look. The theft case register holds case numbers, penal sections and recovery amounts, while the evidence that would have made each case defensible was never joined to it. Figure 2 sets these seven views side by side, converging on the question none of them can answer alone.

![Figure 2. Seven systems, each seeing one part of the answer. The question needs all of them in one place at once.](https://codeatoms.ai/distribution-loss-theft-pakistan/figures/figure_02.png)

Figure 2. Seven systems, each seeing one part of the answer. The question needs all of them in one place at once.

### 2.2  What None of Them See Together

No system joins energy in against energy billed at transformer level with the tamper record, the inspection record and the topology in one argument, and that join is the whole answer. In practice a feeder losing a third of its energy has hundreds of possible causes: a tampered meter, an illegal connection, an overloaded transformer, a wrong meter multiplier, a reading never taken. Because no system ranks those causes, field teams are sent on hunches, tampering events reported by the meters are never joined to billing history or the inspection record, and case files are assembled by hand and fall apart on paperwork. The engineers who know which neighbourhoods and which hours the losses come from are retiring or leaving ahead of privatisation, so the tacit knowledge that once substituted for the join is walking out of the building.

PART II · CHAPTER 3

## Four Constraints Shape Everything Downstream

The goals, the scoping decisions and the exclusions were fixed before any component was chosen.

Chapter 2 showed the join failure: seven systems, seven slices, no shared argument. This chapter fixes the goals and the exclusions that every component choice downstream had to satisfy.

### 3.1  Sovereignty Is a Boundary, Not a Preference

The first goal is that the operator owns the intelligence it produces: open-weight models served on its own hardware inside the country, reading its systems of record, with nothing about its consumers leaving the country or reaching a foreign model service. This is hard in this industry because the hardware itself is governed: export controls turn on total processing performance, so the GPU class a frontier model needs requires a license determination before any card is committed for Pakistan, with a non-US accelerator class held open as the alternative. Hosted model services are ruled out twice over, by the operator's own requirement and by the documented cost of utility data exposure abroad (Natlawreview 2018).

### 3.2  One Governed Model of the Network and Its Consumers

The second goal is a single governed ontology joining all seven systems of record, so that a query can walk from a feeder through its transformers to a meter, its readings, its tamper events and its closed cases. This is hard because no packaged connector set exists for the seven systems of a distribution company of this class: each connector is built as real work, and billing and network records change on their own cycles, so the design must choose carefully which systems are worth streaming and which are worth batching.

### 3.3  Every Decision Carries a Name, and Every Outcome Feeds the Next Ranking

The third goal is that agents draft and people decide: subdivision engineers, inspection officers and revenue officers approve every ranked cause, case file and correction, and every confirmed outcome is kept as a decision record that the next ranking reads, without training a model on the fly. This is hard because approvals degrade into rubber-stamping as trust builds, and rubber-stamped approvals logged as ground truth poison what the next ranking learns from; the design therefore polices its own approvers with known-answer probes and steps an agent class back to shadow mode when the upheld rate falls.

### 3.4  Proof Before Scale

The fourth goal is a measured claim before expansion: phase one runs one circle of feeders for one quarter against a measured baseline, with unchanged control feeders, and gates any extension on four numbers. This is hard because privatisation pressure rewards fast numbers, while only untouched control feeders make the numbers defensible before the billing audit; the discipline of not touching the other circles is the price of a causal claim.

### 3.5  Scoping Decisions

Three decisions fixed the design's shape before any component was chosen, and each bought something at a stated cost. Table 1 records them.

Table 1 · Scoping Decisions

| Decision | What it buys | What it costs |
| --- | --- | --- |
| Run phase one on one circle of feeders for one quarter, against a measured baseline with unchanged control feeders | A causal claim that survives the billing audit and privatisation scrutiny | No other circle is touched until four gate numbers clear |
| Serve open-weight models in country on the operator's own hardware | A boundary no foreign model service ever crosses | An export-license checkpoint before any GPU is committed, with a non-US accelerator class held open |
| Keep every confirmed cause and closed case as a decision record the next ranking reads | Improvement without training on the fly, as the requirement demands | Rankings inherit the quality of past approvals, so probes must police the approvers |

### 3.6  What the Design Chose Against

Each major choice excluded an alternative for a stated reason, and several whole areas were excluded outright. Table 2 records the rejections and closes with what is out of scope and why: no control path is touched, meters come from the national program, filing and prosecution rest with the authorized officer and the Electricity Utilities Court, and the hardware and data center belong to the operator.

Table 2 · What the Design Chose Against

| Where | What was picked | Instead of, and why |
| --- | --- | --- |
| Ingestion | Event streams for meter and tamper data, batch extracts for billing, energy audit, GIS and outage records | Live event streams on all seven systems; billing and network records change on their own cycles, and streaming them adds connector risk without improving a monthly transformer balance |
| Improvement | A kept record of confirmed causes and closed cases, with consumer identifiers minimized | Fine-tuning the work-surface model or training a theft classifier on historical labels; the requirement rules out training on the fly, and past labels are biased by where inspections happened to be sent |
| Model serving | GLM 5.3 at FP8 on one node of the 141 GB GPU class | BF16 serving on two nodes; FP8 halves the weights to about 756 GB so one node holds them, and doubling the hardware doubles export-license exposure for an accuracy gain the ranking and drafting tasks have not been shown to need |
| Sensing and edge compute | None in the field; the platform reads the meters and their head end from the data center | Cameras and edge nodes; the sensing already exists at the meters, and every added device widens the maintenance and export surface |
| Out of scope | SCADA integration, meter installation, model training, prosecution and recovery, transaction advisory, hardware and infrastructure, third-party license fees, historic data migration, estate-wide training, round the clock support | Any of those inclusions; no control loop is entered, meters arrive under the national program, the complaint pack ends at the Grade 17 signature, and the operator owns the machines the platform runs on |

PART II · CHAPTER 4

## One Stack Runs From the Systems of Record to the Surfaces

Systems of record below, one object model in the middle, services and surfaces above.

Chapter 3 fixed the constraints: the country's boundary around every byte, the join before the analytics, a named officer behind every action, and a measured gate before any extension. This chapter turns those constraints into a stack of named components, each of which the operator can hold, inspect and replace.

### 4.1  Why the Pattern Fits

The pattern is the three layers with one direction of dependence that a [sovereign AI architecture](https://codeatoms.ai/sovereign-ai-architecture/) for a utility converges on. Below sit the seven systems of record exactly as they run today, named in full in Table 3: the billing, meter data, energy audit, geographic network, outage, field inspection and theft case systems. None is replaced and none is bypassed. In the middle sits one object model, fifteen objects with typed links, each anchored in exactly one system of record, holding the join no single system can make. Above it sit the applications and agents: eight services that compute each transformer's energy in against energy billed, rank causes, draft case files and corrections and record approvals, and five surfaces that put those drafts in front of the subdivision engineers, inspection officers and revenue officers who decide.

The pattern fits because the operator's problem is a join failure, not a sensing failure: the meters already report tampering and the registers already record cases, but no system can answer which transformer, which cause, which case in one question. A middle layer that owns the join lets every system keep its role while the intelligence compounds above it, and because the agents only draft and the officers approve, nothing above the object model ever writes to a system of record directly. Figure 3 shows the layered stack with its counts: seven sources, one adapter family, fifteen objects, three models, eight services and five surfaces.

![Figure 3. The layered stack: 7 sources, 1 adapter family, 15 objects, 8 services and 5 surfaces.](https://codeatoms.ai/distribution-loss-theft-pakistan/figures/figure_03.png)

Figure 3. The layered stack: 7 sources, 1 adapter family, 15 objects, 8 services and 5 surfaces.

Table 3 · The Stack, Stage by Stage

| Stage | What it is responsible for | How |
| --- | --- | --- |
| Sources | Holding the billing, metering, audit, network, outage, field and case records the platform reads | Seven systems of record: the customer information and billing system, the meter data management system, the energy audit records per feeder and transformer, the geographic information system of the network, the outage and complaint system, the meter reading and inspection app, the theft case register |
| Sensing | Producing the live signals the design runs on | Smart meters and feeder-head meters delivering interval load and tamper events into the meter data management system |
| Adapters | Owning every contract between a source and the object model; nothing enters any other way | One integration adapter family: a Kafka subscription for meter data, scheduled batch extracts for billing, energy audit, GIS and outage records, mapped connectors for the field app and the theft case register |
| Object model | Holding the join as fifteen objects with typed links, each anchored in one system of record | The network and customer ontology service on an ontology or graph store, with interval load in the time series store beside it |
| Inference | Running the three models inside the sovereign boundary | GLM 5.3 at FP8 on vLLM across one node of the frontier inference cluster class (GPU nodes for 300B to 1T parameter open weight models); BGE-M3 and Chronos-2 on the on site inference server class |
| Services | Computing, ranking, drafting, recording and measuring | Eight services: network and customer ontology, loss analytics, loss and theft agents, approvals and audit, improvement, the command center, sovereign platform, measurement |
| Surfaces | Putting drafts, evidence and boards in front of the people who decide | Five surfaces: the approval queue and loss boards, the case file queue, the correction queue, the printable complaint pack, the command center |

### 4.2  The Stack Stage by Stage

Table 3 walks the stack stage by stage, from the records the operator already holds to the surfaces its people already work at, naming the component responsible at each stage.

### 4.3  A Reusable Pattern

A team carrying a similar brief reuses the shape and swaps the contents. Keep the direction of dependence: sources untouched below, one adapter tier owning every contract, one governed object model holding the join, agents that draft and never act, approvals recorded as objects carrying a hash and a written reason, and all inference inside a boundary the organization owns. Swap the seven sources for the industry's own records, the fifteen objects for its assets and measures, the energy-balance ranking for its own decision, and the models for whatever the license terms and hardware permit. What is never swapped is the rule the stack stands on: nothing above the adapters may know a source's schema, and nothing below the object model may know an agent exists.

Table 7 · Architecture, Layer by Layer

| Layer | Component | Choice | Why |
| --- | --- | --- | --- |
| Event streaming and messaging | by class, no product named | Product | Apache Kafka |
| The ontology or graph store | by class, no product named | Class | An ontology or graph store class, fixed by what the fifteen objects and their links demand |
| Time series and telemetry storage | TimescaleDB on PostgreSQL | Class | Interval load volume for several hundred thousand meters is the bulk of the design's storage and its rate is not yet stated; the shelf holds the InfluxDB 3, TimescaleDB and QuestDB comparison for exactly this OT telemetry case, and the choice is committed at design against the measured interval rate. |
| Video ingest, recording and management | by class, no product named | Not needed | No cameras anywhere in this design; the sensing is smart meter interval data, tamper events and the records of seven systems of record. |
| Edge model serving | by class, no product named | Not needed | No edge compute; all inference runs in the sovereign data center on the operator's own hardware. |
| On site language model serving | by class, no product named | Product | VLLM |
| Object tracking and trajectory forecasting | by class, no product named | Not needed | No video and no moving object tracking; the trajectories here are loss trends over time, served by the time series model. |
| Edge orchestration of containers | by class, no product named | Not needed | No edge nodes to orchestrate; the platform runs as standard containers in the sovereign data center. |
| An air gapped artifact and model registry | by class, no product named | Product | Harbor |
| Labelling and retraining | by class, no product named | Not needed | Under system of context nothing is trained, fine tuned or distilled into weights: confirmed causes and closed cases become the record the next ranking reads, and the requirement asks for exactly that ('without training a model on the fly'). |
| Time synchronisation across sensors and systems | by class, no product named | Product | Chrony |
| Observability of the running system | by class, no product named | Product | Prometheus |

PART II · CHAPTER 5

## Fifteen Objects Turn Operational Data Into One Argument

The object model is the join the systems never made.

Chapter 4 placed one object model at the center of the stack and gave every other layer its reason: the adapters feed it, the services read it, the surfaces show it. This chapter opens the model itself, object by object and link by link.

### 5.1  Every Object and Its Typed Links

The model holds fifteen objects: the grid station as its one site; the feeder, the distribution transformer, the service connection and the meter as assets; the interval load as its one measure; the reading, the billing account, the tariff, the theft case and the recovery as records; the inspection, the tamper event and the approval as events; and the agent draft as the document the whole loop turns on. Each is anchored in exactly one system of record, so provenance sits on every object's face: the transformer's energy in and energy billed come from the energy audit records, the meter's seal state from the meter data management system, the theft case's court and PPC section from the theft case register.

The typed links are what make the model an argument rather than a filing system. A grid station supplies feeders; a feeder is metered at its head and carries transformers; each transformer serves service connections; each connection carries a meter and is billed under a tariff; a meter reports interval load, yields readings and raises tamper events; an inspection visits a meter; a tamper event opens a theft case; a theft case yields a recovery; and an approval settles an agent draft. Figure 4 shows every object and every link, with the transformer at the center in navy.

One traversal across those links answers the question field teams actually ask: every transformer on a feeder whose monthly loss percent crossed its threshold, the tamper events its meters raised in the same window, what was billed to the connections it serves, and which inspections already visited. That question crosses four systems of record, and a document store can answer it only if the words co-occur in one document, which they never do, because the tamper event lives in one system, the billing history in another and the inspection findings in a third. Table 8, printed by the platform, records each object with the system it is anchored in and its typed links.

![Figure 4. The fifteen objects of the model and the typed links that let a query reach across them.](https://codeatoms.ai/distribution-loss-theft-pakistan/figures/figure_04.png)

Figure 4. The fifteen objects of the model and the typed links that let a query reach across them.

Table 8 · The Object Model

| Object | Anchored in | Typed links |
| --- | --- | --- |
| Grid Station | The geographic information system of the network | supplies: Feeder |
| Feeder | The geographic information system of the network | carries: Transformer; metered by: Meter |
| Transformer | The energy audit records per feeder and transformer | serves: Service Connection |
| Service Connection | The customer information and billing system | carries: Meter; billed under: Tariff |
| Meter | The meter data management system | reports: Interval Load; yields: Reading; raises: Tamper Event |
| Interval Load | The meter data management system | no typed link recorded |
| Reading | The customer information and billing system | no typed link recorded |
| Billing Account | The customer information and billing system | priced by: Tariff |
| Tariff | The customer information and billing system | no typed link recorded |
| Inspection | The meter reading and inspection app | visits: Meter |
| Tamper Event | The meter data management system | opens: Theft Case |
| Theft Case | The theft case register | yields: Recovery |

### 5.2  The Human Loop and the Hosting Posture

The loop lives inside the model, not around it. Every agent draft is an object carrying its draft type, ranked causes, evidence citations, model version and confidence, and its status moves through drafted, approved, amended, rejected and expired; every approval is an object carrying the approver role, the officer grade, the timestamp, the artifact hash and the written reason, and the hash ties the approval to the exact draft text it settled. The surfaces are where the loop is worked: the command center where the loss reduction team sees feeders and transformers by loss, the approval queue, the case file queue, the correction queue and the printable complaint pack.

The hosting posture follows the requirement. The model and every service above it run in an in-country sovereign data center or colocation on the operator's own hardware; identity is held by Keycloak inside the boundary; there are no external links; and no consumer record leaves the country or reaches a foreign model service. The single write path out of the platform is the approved correction: reading and multiplier corrections land in the customer information and billing system, and approved theft cases land in the theft case register, each through the adapter tier and each traceable to the approval object that authorized it.

### 5.3  One Object in Its Recorded Form

The grid station record below shows the id, label, kind, anchor, properties and links the platform prints for every object; the tamper event, which carries the design's sharpest signal, the meter's own report that something was done to it, is recorded the same way.

```
{ "id": "grid-station", "label": "Grid station", "kind": "site", "anchored_in": "The geographic information system of the network", "properties": [ "Grid station code", "Voltage level", "Feeders supplied", "Circle", "Subdivision" ], "status_vocabulary": [], "links": [ { "to": "feeder", "label": "supplies" } ] }
```

PART II · CHAPTER 6

## Every Source Enters Through an Adapter, Never Directly

Nothing reaches the object model except through an adapter that owns its contract.

Chapter 5 described what the object model holds. This chapter describes how data gets into it: seven sources, one adapter family, and a backbone that keeps every event ordered, buffered and inside the country.

### 6.1  Seven Sources and Their Provenance

All seven sources are the operator's own commercial systems of record, provenance class operator, read direction only: the customer information and billing system, the meter data management system, the energy audit records per feeder and transformer, the geographic information system of the network, the outage and complaint system, the meter reading and inspection app and the theft case register. Each earns its place: billed units and tariffs are half of every transformer's energy balance, interval load and tamper events are the live sensing, the audit records are what the computed balances are validated against, the geographic system ties meters to transformers to feeders to stations, outage and complaint context separates supply problems from theft in the rankings, the field app is where approved inspections land and findings and photographs return as evidence, and closed cases are what the next ranking learns from.

The transport is split deliberately, as Figure 5 shows. The meter data management system is read through a Kafka subscription, because interval load and tamper events lose their value if they wait for a batch; billing, energy audit, geographic and outage records arrive as scheduled batch extracts, because they change on their own cycles and streaming them would add connector risk without improving a monthly transformer balance; and the field app and the theft case register are reached through mapped connectors built for their interfaces, because no packaged connector set for a distribution operator's records exists on any shelf.

![Figure 5. The 7 named systems, the adapter path each one takes, and the object model they all map into.](https://codeatoms.ai/distribution-loss-theft-pakistan/figures/figure_05.png)

Figure 5. The 7 named systems, the adapter path each one takes, and the object model they all map into.

### 6.2  What the Adapter Tier Guarantees

The adapter tier owns every contract, and the guarantee is absolute: no service reads a source directly, and no source is written except through an approved correction path. Each adapter maps the source's schema onto the object model, normalizes units and timestamps, and carries the meter multiplier through untouched, because a wrong multiplier is itself one of the ranked causes, not something to silently correct. Every extract is minimized to the agreed fields, stamped with its provenance, and written idempotently so a re-handed over event collapses rather than duplicates. Each feed carries a freshness window with stale and flatline detection: a stale feed flags its drafts and holds them, and the staleness is visible on the command center, so no ranking rides on data nobody noticed had stopped.

Minimization is defense, not courtesy. A leak of consumer information through an operational system drew business improvement recommendations from a market surveillance commission in another utility (Chuden 2023), and a vendor data exposure cost a utility a seven-figure penalty (Natlawreview 2018); both were records leaving through a path nobody owned. Here every path is owned by one adapter, every extract stays inside the country, and every field in it is agreed.

### 6.3  The Event Backbone

Apache Kafka is the backbone. Interval load and tamper events travel on topics partitioned by meter number, so ordering holds per meter, which is the ordering a balance and a tamper join need; delivery is at least once, and the adapters' idempotent writes make re-delivery harmless. Buffering absorbs the bursts a head end produces after an outage, and replication inside the in-country data center means a broker loss does not lose a tamper event. Updates arrive the same way everything else does, as versioned images through the Harbor registry and never over an open link; Chrony keeps the clocks aligned so an event joins to the right billing period; and Prometheus watches consumer lag, so a feed falling behind is seen before it goes stale.

PART II · CHAPTER 7

## Inference Belongs Where the Data Is

Each tier runs what its data and its link can carry.

Chapter 6 described how seven systems of record enter through one adapter family, as event streams for the meter data and as scheduled batch extracts for the billing, audit, geographic, outage and case records. This chapter fixes where the inference over that data runs, and what the arithmetic of that placement obliges.

### 7.1  Each Tier and Its Arithmetic

All inference runs in one place: an in-country sovereign data center or colocation, on hardware the operator owns. There is no edge tier, because the smart meters and their head end already exist and the platform reads them from the data center rather than adding compute beside them; there is no hosted tier, because the operator's own requirement is that nothing about its consumers leaves the country or reaches a foreign model service. What the design carries instead is three serving classes inside that one boundary, and Figure 6 shows each tier, what runs on it and what crosses the boundary to reach it: a frontier node for the work surface model, and a dual-socket server with a 48 GB PCIe inference GPU that hosts the embedder and the forecaster together.

The frontier tier carries GLM 5.3, whose filed parameter count is 753 billion. At FP8, one byte per parameter, that is 753 GB of weights; the 1.2 planning factor for KV cache and activations lifts what the GPUs must hold to 904 GB. One node of eight GPUs of the 141 GB class provides 1,128 GB, which holds the weights with 375 GB left beside them against the 151 GB the planning factor reserves, so the KV cache ceiling is comfortable rather than marginal. The FP8 choice is the reason one node suffices: at BF16 the same model is roughly 1.5 TB of weights, which demands a second node and doubles the export-control exposure for an accuracy gain the ranking and drafting tasks have not been shown to need. Export control is itself a placement constraint, not just a procurement one: US ECCN 3A090 and 4A090 controls turn on total processing performance, so a license determination precedes any card commitment for Pakistan, and a non-US accelerator class stays open as the alternative. That determination may change which accelerator the node carries; it never changes which country the node sits in.

The second tier is deliberately small. The embedding model at FP16 occupies about 1.1 GB and the forecaster at FP32 about 0.48 GB, so both fit on the 48 GB card with two orders of magnitude of headroom, which is why the design gives them one server rather than two.

![Figure 6. Where each tier runs, what runs there, and the narrow set of outputs that cross the boundary.](https://codeatoms.ai/distribution-loss-theft-pakistan/figures/figure_06.png)

Figure 6. Where each tier runs, what runs there, and the narrow set of outputs that cross the boundary.

### 7.2  The Latency Budget

The design has no control loop, and nothing in it is allowed to touch one, so its latency budget buys interaction rather than reaction. The outer bound is set by the work itself: a transformer's monthly energy balance is computed on the billing cycle, and a feeder's loss percent moves monthly. Inside that outer bound the budget tightens in three steps. Tamper events must be joined to billing history and drafted as case files within a working day, so an inspection officer opens a queue that is already populated. The loss boards must refresh on the cadence of their feeds, not on the cadence of anyone remembering to run a report. And the command center's conversational interface must answer with citations at reading pace, which local serving on the operator's own hardware holds without any inference call leaving the network. Every hop, from Kafka through the object model to the surfaces, stays inside the operator's boundary, which is what makes the budget credible: there is no wide-area round trip in any path an officer waits on.

### 7.3  The Boundary and Its Failures

What crosses the network boundary is reads, and reads only. The meter data management system is read through a Kafka subscription; billing, energy audit, geographic information, outage and case records arrive as scheduled batch extracts. The single inbound crossing is the artifact path: model weights and container images enter through the Harbor registry as versioned artifacts, never as a call to a foreign service. This posture answers documented threats rather than hypothetical ones. State-sponsored actors have been indicted for targeting the energy sector specifically (CISA 2022), and a vendor data exposure at a utility drew a seven-figure reliability penalty (Natlawreview 2018), so a design that keeps consumer data off every external path is answering the sector's recorded history, not a general caution.

Each failure path has a stated behavior. If the link to a system of record fails, Kafka buffers the meter event stream and the batch extracts simply wait for their next schedule; per-feed freshness windows with stale and flatline detection flag any feed whose age exceeds its window, drafts built on stale feeds are held rather than sent, and staleness is visible on the command center so no one acts on a silent gap. If power fails, the data center's own resilience carries the platform and Kafka's replication preserves undelivered events for replay. If the update path fails, the artifact registry means the running versions continue to serve; a failed weight or image update leaves the previous version in place rather than leaving the platform down, and the retry is another artifact pull inside the same controlled path.

PART II · CHAPTER 8

## The License Decides What the Operator Can Own

Every model was chosen against its license before its accuracy.

Chapter 7 placed three serving classes inside one in-country data center and showed the arithmetic that fits them there. This chapter names the three models that occupy those classes, and shows why each one's license was weighed before its accuracy: a license decides whether the operator can hold the weights at all. The model stack is small by design, and Figure 7 shows it whole: one frontier model for the work surface, one embedding model for cited retrieval, one forecaster for the energy balances that trigger every ranking. Three models, three licenses, one country. GLM 5.3 is the frontier model. Its filed parameter count is 753 billion, served at FP8, which is about 756 GB of weights and roughly 1.5 TB if served at BF16; it runs on one node of eight GPUs of the 141 GB class, in the central tier. Its role is the agentic work surface and ontology maintenance: the command center's conversational interface, the drafting of ranked causes, case files and corrections, and the upkeep of the governed object model all run on it. Its license is the GLM-5.3 bespoke license, whose terms permit commercial use, fine-tuning and redistribution, and those three permissions are exactly what an operator-owned system needs: the operator can hold the weights, serve them for its own commercial purpose, and keep serving them regardless of any vendor's fortunes.

![Figure 7. The three models, their placement, and the work each one does.](https://codeatoms.ai/distribution-loss-theft-pakistan/figures/figure_07.png)

Figure 7. The three models, their placement, and the work each one does.

### 8.1  Three Models, Three Licenses

BGE-M3 is the embedding model. It occupies about 2.27 GB at float32 as published, about 1.1 GB at the FP16 serving precision chosen here, and about 0.6 GB at 8 bit, and it runs on the 48 GB PCIe inference GPU beside the forecaster. Its role is retrieval embedding for cited answers: the command center answers with citations, which means tariff codes, meter numbers, PPC sections and inspection findings must survive retrieval exactly, and BGE-M3 provides dense, sparse and multi-vector retrieval in a single pass over an 8,192-token window, long enough to embed a full inspection finding rather than a truncated one. It is MIT licensed. It was chosen over multilingual E5, whose 512-token window cannot hold a long finding, and over Nomic v2, whose Matryoshka truncation this design has no use for.

Chronos-2 is the forecaster. It occupies about 0.48 GB at 32 bit, about 0.24 GB at 16 bit, and runs at FP32 on the same 48 GB card. Its role is transformer and feeder energy balance forecasting: it forecasts multivariate series with covariates zero-shot, so the residual between each transformer's forecast and its measured balance is the anomaly signal, with no training run anywhere in the loop. That last clause is a requirement, not a convenience: the operator asked that the next ranking be better without training a model on the fly, so improvement runs on the kept record of confirmed causes and closed cases, never on the weights. Chronos-2 is Apache-2.0 licensed, and it was chosen over TimesFM 3.0 and Moirai 2.0, whose non-commercial terms cannot ship in an operator-owned system no matter how well they forecast.

The license test is the same for all three, and it is the chapter's argument. A non-commercial or service-only term would convert a sovereign system into a rented one, and a utility that leaked consumer information through a third party has already shown what such dependencies cost in regulatory response (Chuden 2023). Every model here is held as weights inside the country, on the operator's own hardware, under terms that let the operator keep them.

### 8.2  The Model and Equipment Register

Table 4 gathers the register: each model with its serving class, the hardware classes and sizing rules the placement stands on, the sensing the design reads, the patterns it stands on, and the ground everything runs on. Each row is a decision already argued in this part of the paper; the table exists so an engineer can check the whole stack against one view before quoting hardware or pulling weights.

Table 4 · Model and Equipment Register

| The choice | What was picked | Why here |
| --- | --- | --- |
| Frontier model | GLM 5.3 at FP8 on one node of the 141 GB HBM class | 753 GB of weights inside 1,128 GB with the KV cache ceiling covered; the bespoke license permits commercial use, fine-tuning and redistribution, so the operator holds the weights |
| Embedding model | BGE-M3 at FP16 on the 48 GB PCIe inference class | Dense, sparse and multi-vector retrieval over an 8,192-token window under MIT; tariff codes and case particulars stay retrievable and citable |
| Time series forecaster | Chronos-2 at FP32 beside the embedder | Zero-shot multivariate forecasting with covariates under Apache-2.0; the residual against each transformer's own baseline is the anomaly signal, with no training run |
| Hardware classes | a frontier inference cluster class (GPU nodes for 300B to 1T parameter open weight models); an on site inference server class | One frontier node and one dual-socket inference server carry all three models, subject to the export license determination that precedes any card commitment |
| Sizing rules | Frontier Model GPU Footprint Sizing Rule (vLLM, SGLang); GLM 5.3 Node Count by GPU Class | Weights times the 1.2 planning factor, checked per GPU class before any card is committed, with a non-US accelerator class held open |
| Sensing | Smart meter interval load and tamper events; the records of seven systems of record | No cameras and no field sensors; the meters and their head end already exist and the platform reads them |
| Patterns | Asset to alert to work order; improvement through the kept record of decisions, never weights; event streams for meters, batch extracts for records | An anomaly becomes an object linked to its asset and is resolved by approved work, and rankings improve from confirmed outcomes officers uphold |
| Ground | In-country sovereign data center or colocation on the operator's own hardware | Nothing about consumers leaves the country or reaches a foreign model service; weights and images enter only as artifacts through the registry |

PART III · CHAPTER 9

## Shadow Mode Comes Before Any Flag Is Trusted

The rollout earns each phase at a gate the operator can read.

Chapter 8 fixed the model stack and the licenses that let the operator hold every weight it runs. This chapter turns from what the system is to how it earns the right to run: one circle of feeders first, a measured baseline, unchanged control feeders, and gates written so the operator can read them without taking the platform's own account of itself on trust.

### 9.1  Phases, Workstreams and Gates

The rollout is two phases, and neither is a schedule: each phase is a set of items with an exit gate, and the gate, not a date, moves the work forward. Phase 1, one circle and one quarter, carries 15 items across six workstreams: the network and customer ontology, loss analytics, the loss and theft agents, approvals and audit, the sovereign platform, and measurement. Its items include the governed network and customer ontology, the meter and tamper event stream ingest, and the billing and network record batch extracts. Its exit gate is the billing agent drafting corrections: reading and multiplier corrections that a subdivision engineer approves and that land back in the customer information and billing system only through the recorded approval path. The phase runs on GLM 5.3 self hosted in an in-country data center, across one circle of feeders measured against a baseline, with control feeders left unchanged so the comparison stays honest. Phase 2, extending to the other circles, is a single item in the measurement workstream: the circle extension gate and the rollout plan. No other circle is touched until the four numbers that gate reads are met. Requirement coverage holds the design to the same discipline: 29 requirements trace through the two phases, so an item that serves no requirement does not enter the plan, and a requirement with no item is visible as a gap rather than silent. Figure 8 sets the phases, their item counts, their workstreams, their gates and the requirement coverage on one page.

![Figure 8. The two phases and their gates, and coverage of the 29 requirements across them.](https://codeatoms.ai/distribution-loss-theft-pakistan/figures/figure_08.png)

Figure 8. The two phases and their gates, and coverage of the 29 requirements across them.

### 9.2  What the Rollout Measures

Phase 1 measures against a baseline the operator already trusts, and the control feeders carry the counterfactual. The computed transformer balances, energy in against energy billed, are validated against the existing energy audit records per feeder and transformer before any agent ranking is read. Beyond the balances, the phase measures the confirmation rate of agent-ranked causes at inspection, the acceptance rate of case files at the Grade 17 gate, and the outcome of billing corrections in the system of record itself. It measures the meters actually delivering interval load and tamper events, reported separately from meters installed, because the two populations diverge exactly when the rollout outruns the interface. It measures approval quality through known-answer probes in the normal queue, and feed health through per-feed freshness windows. These measurements feed the four numbers the circle extension gate reads, and the gate is the single path from one circle to the next.

### 9.3  Failure Modes

Table 5 records what fails and what the design does about it, and every row is a mode the recorded reading or the operator's own situation already produced.

Table 5 · Failure Modes

| What fails | What the design does |
| --- | --- |
| Approvals degrade into rubber-stamping, and rubber-stamped approvals poison the record the next ranking learns from | Known-answer probes, fabricated positive drafts on historical cases with no violation, run in the normal approval queue; the upheld rate is measured, approvers are re-briefed that the draft is preliminary, and an agent class steps back to shadow mode when the rate falls |
| Export controls block or delay the GPU class GLM 5.3 needs | The license determination is a phase 1 checkpoint before any GPU class is quoted, and a non-US accelerator class is held open as the alternative |
| The smart meter rollout outruns the interface, as recorded in the Great Britain rollout where installations ran far ahead of the interface | Meters actually delivering interval and tamper events are reported separately from meters installed, and the connector is tested per meter generation before each circle extension |
| Case files are rejected for missing evidence, the exact failures the court recorded in acquittals | The completeness check maps every particular the complaint must carry and blocks the pack from the Grade 17 gate until each is present |
| Theft on conventional meters and unmetered direct taps gives no tamper event and no interval load | No cause attribution is claimed where no meter exists; the transformer balance still bounds the loss, and the blind spot closes as the national meter replacement program completes |
| Stale feeds silently drive rankings and dispatches | Per-feed freshness windows with stale and flatline detection hold drafts, and staleness is visible on the command center |

### 9.4  Lessons

**Shadow the agents before anyone approves them.** The trust that matters is the approvers', not the platform's, and trust built without measurement becomes rubber-stamping. The probe mechanism exists because an approval queue that is never tested cannot show that it has stopped judging, and a poisoned record of confirmed causes cannot be un-poisoned later. Report meters delivering data, not meters installed. An installed meter that has dropped out of smart mode is indistinguishable from a conventional one at the data center, and a loss ranking built on the installed count silently overstates its own coverage. The delivery count is the honest denominator for every coverage claim the command center makes. Treat the export license as a design input, not a procurement step. The controls turn on total processing performance, so the determination changes which accelerator class the sizing arithmetic runs on. Making it a checkpoint before any card is committed keeps the design portable between US and non-US classes instead of re-planned after a refusal.

### 9.5  What Is Still Open

Four questions stay open, and each has a named consequence. The measured interval rate is not yet stated, so the time series store is committed at design against that rate rather than now; settling it fixes the store and the retention arithmetic. The export license determination may move the node between accelerator classes without moving it out of the country; settling it fixes the hardware class and the node count. Interface charges levied by the operator's own vendors on the seven systems of record are payable by the operator; settling them fixes the connector cost line. The blind spot on conventional meters and unmetered taps closes only as the national program completes; until then the design bounds that loss without attributing it.

PART III · CHAPTER 10

## The Intelligence Should Stay with the Operation That Produced It

What the design builds belongs to the operator.

Chapter 9 ended at the circle extension gate, where the operator reads four numbers and decides whether the work widens. This chapter states what the operator holds by the time that gate is read, and what stays with the operation no matter how the platform grows.

### 10.1  What the Operator Holds

The object model is the operator's from the first item of phase 1: 15 objects, from the grid station to the approval, each anchored in one of the seven systems of record the operation already runs and joined by typed links that no document store reproduces. The weights are the operator's too. GLM 5.3 runs under a license whose terms permit commercial use, fine tuning and redistribution; BGE-M3 runs under MIT; Chronos-2 runs under Apache 2.0. All three run on hardware the operator owns, in an in-country data center, and no fine-tune exists anywhere in the design: the requirement asks that the next ranking improve without training a model on the fly, so confirmed causes and closed cases are kept as a record the next ranking reads and the weights stay as issued. The decision record is the operator's audit trail and its improvement engine at once. Every approval carries the approver role, the officer grade, the timestamp, the artifact hash and a written reason, and a recorded approval is the single write path into the systems of record. The boundary is the operator's to hold and to defend, and the recorded reading says why it must be defended: energy utilities are named targets of state-sponsored cyber actors (CISA 2022), a leak of customer data drawn from a utility's own systems drew business improvement recommendations from a sector regulator (Chuden 2023), and a vendor data exposure at a utility cost a seven-figure penalty (Natlawreview 2018). In-country serving on owned hardware, with nothing about customers leaving the country or reaching a foreign model service, is the single control that answers all three precedents.

### 10.2  The Offer Behind the Design

CodeNinja produced this design on Praxis, its platform for designing physical AI systems, and each element of it maps to CodeNinja's offer. The governed model of the network and its customers, 15 objects anchored in the operator's own systems of record, is Hyper Ontology. The ranked causes, case files and corrections that a named officer decides on, with every decision recorded against an artifact hash, are Decision Systems. The loss reduction command center, where the operator's engineers and officers approve agent drafts and build their own agents, is Hyper Pragma. The kept record of confirmed causes and closed cases that the next ranking reads before it acts is Hyper Engram, which does not update model weights. The operator-owned hardware, the open-weight licenses and the in-country, boundary-held operation are Sovereign Infrastructure. What the design builds therefore compounds inside the operation that produced it, which is the point.

PART IV · CONCLUSION

## The Pattern Repeats Wherever Systems of Record Do Not Meet

Seen whole, the design is one object model over the systems an electricity distribution company in Pakistan already runs, with inference placed where the data is and every decision left to a named person.

Running the same shape elsewhere takes the same four things: the named systems, an object model anchored in them, a first gate that can stop the work cheaply, and the license posture that lets the operator own what it learns.

PART IV · CHAPTER 11

## How Praxis Contextualized and Reasoned This Design

Every choice above traces back to something Praxis recorded reading.

Chapter 10 closed the ownership argument, and every element it named, from the object model to the boundary, was placed there by a recorded decision rather than a default. This chapter shows where those decisions came from: every design in this series is produced on Praxis, the design team platform for designing physical AI systems, and this chapter lets a reader trace any choice above back to the reading that justified it (Figure 9).

### 11.1  Contextualizing the Ask

The ask reached Praxis in the operator's own words: a sovereign AI architecture for loss and theft reduction at an electricity distribution company in Pakistan, with open-weight models on the operator's own hardware in the country, reading the operator's systems of record, and nothing about its customers leaving the country or reaching a foreign model service. Praxis assigned the design to the system of context family in the Energy and Utilities industry. What Praxis read: the operator's requirement document and the pinned energy and utilities brief, together with the stack shelf holding the tooling, model and hardware cards the design draws on. Nothing read was skimmed, and nothing outside it was assumed.

![Figure 9. From the ask to the design: the family and industry Praxis assigned, the eight lenses and what each cited, the patterns adopted and set aside, and the equipment the design lands on.](https://codeatoms.ai/distribution-loss-theft-pakistan/figures/figure_09.png)

Figure 9. From the ask to the design: the family and industry Praxis assigned, the eight lenses and what each cited, the patterns adopted and set aside, and the equipment the design lands on.

### 11.2  The Lenses

Praxis read through eight lenses, and Table 6 records what each could see, what it cited and what it contributed to the design. Two lenses returned nothing the design could use, and they are shown as gaps rather than folded into neighbouring rows.

Table 6 · The Lenses and What They Contributed

| Lens | Could see | Cited | What it contributed |
| --- | --- | --- | --- |
| First principles | no corpus shelf | 3 | The pinned energy and utilities brief supplied the asset to alert to work order pattern: an anomaly becomes a first class object linked to the exact asset, resolved by a work order, never by editing a status field. |
| Case studies | the case study shelf | 1 | The Great Britain smart meter rollout is the measured precedent for this operator's own situation: installations ran ahead of the interface, so meters delivering data are counted apart from meters installed. |
| Tooling and recency | the tooling and recency shelf | 6 | Three model roles verified live this run: GLM 5.3 (named in the requirement, 753B total, open weights published 28 August 2026 under a bespoke license, not MIT), BGE-M3 (MIT, multilingual dense, sparse and multi-vector retrieval in one pass) and Chronos-2 (Apache 2.0, zero shot forecasting with covariates). |
| Hardware and equipment | the hardware and equipment shelf | 4 | The GPU class entries gave the worked sizing: GLM 5.3 at FP8 needs 756 GB of weights, about 907 GB with KV overhead, so one node of eight 141 GB HBM class GPUs holds it, with the export control position checked before any card is committed. |
| Rules and regulations | the rules and regulations shelf | 6 | The national cloud first policy on power sector data, the Penal Code sections on electricity offences and penalties and on the theft complaint signed by a Grade 17 officer, the regulator's performance standards, and the data protection rules for customer data. |
| Approach | the approach shelf | 4 | Ontology first (phase one proves the joins on one real circle before any agent ships), a baseline and control zone (control feeders kept unchanged so seasonal demand movement is not reported as the pilot's effect), sovereign serving on the operator's own hardware, and phases earned at gates. |
| History | the history shelf | 0 | No history note was read that bears beyond the case study corpus; the smart meter rollout precedent that guided this design (installations outrunning the interface) is carried in case studies. |
| Domain fusion | no corpus shelf | 2 | The CodeNinja System of Context reference architecture and the energy and utilities domain. |

### 11.3  Patterns Adopted and Set Aside

Three patterns were adopted. The asset to alert to work order pattern shapes the whole object model: a crossing threshold or a tamper alarm becomes a tamper event or an agent draft linked to the exact meter or transformer, and it is resolved by an inspection or an approval, never by editing a status field. The energy-balance pattern drives the analytics: each transformer's energy in against energy billed, forecast by Chronos-2 so the residual against the transformer's own baseline is the anomaly signal with no training run. The recorded-approval pattern guards every write: the single path into a system of record is an approval carrying an artifact hash and a written reason. Three were set aside. Fine-tuning on historical case labels was rejected because the labels are biased by where inspections happened to be sent on hunches, and because the requirement forbids training on the fly. Streaming all seven systems of record was rejected in favour of event streams for meter data and batch extracts for billing, energy audit, GIS and outage records, since billing and network records change on their own cycles and streaming them adds connector risk without improving a monthly balance. BF16 serving on two nodes was rejected in favour of FP8 on one node of the 141 GB class, because the accuracy gain has not been shown to be needed and the doubling carries export-license exposure.

### 11.4  Where the Reasoning Lands

The reasoning lands on four equipment classes and their sizing rules: the frontier inference cluster class (GPU nodes for 300B to 1T parameter open weight models) for the frontier work surface model, sized from its filed parameter count at FP8 with the planning factor for KV cache and activations; the frontier model GPU footprint sizing rule under vLLM; the GLM 5.3 node count by GPU class, one node of eight GPUs holding the weights with room beside them; and the on site inference server class hosting the embedder and the forecaster in the same sovereign data center. Every choice traced in this chapter, and every figure in it, was recorded reading: what the lenses saw, what the shelf held and what the operator's own requirement stated. Nothing is inferred, and nothing enters the design that the reading did not contain.

Appendix A

## What the Operator's Own Inference Hardware Costs Over Three Years

The paper is written for an electricity distribution company in Pakistan, with every model running in an in-country sovereign data center or colocation on hardware the operator owns (chapter 1, section 1.3; chapter 3, section 3.1; chapter 7, section 7.1). This appendix therefore prices for Pakistan, with the regulator's uniform commercial electricity tariff for power and the AWS Asia Pacific (Mumbai) region, ap-south-1, as the rental reference. The design's compute is two servers inside one boundary: "a frontier node for the work surface model, and a dual-socket server with a 48 GB PCIe inference GPU that hosts the embedder and the forecaster together" (chapter 7, section 7.1). The frontier node is "one node of eight GPUs of the 141 GB class" serving GLM 5.3 at FP8 on vLLM (chapter 7, section 7.1; Table 4, "Frontier model" and "Hardware classes"); the second server carries BGE-M3 at about 1.1 GB and Chronos-2 at about 0.48 GB on one 48 GB card (chapter 7, section 7.1; chapter 8, section 8.1). Both are priced two ways: owned, from system builders' published configured prices with support and power added, and rented, from the AWS price files for the nearest region that offers the same cards, on demand and on the two three year all upfront plans. Every input is dated and cited, and the arithmetic is shown.

### A.1 The Answer

Owning the two servers for three years costs **about 641,000 US dollars**, inside a range of 615,000 to 667,000. Renting the same cards around the clock costs **about 773,000 dollars** on the deepest three year commitment (AWS EC2 Instance Savings Plans, all upfront, for p5en.48xlarge and g6e.xlarge in Asia Pacific (Mumbai)), **about 1.36 million dollars** on the three year Compute Savings Plan, all upfront, and **about 2.05 million dollars** on demand. Against the deepest commitment, ownership costs **about five sixths** (641,148 / 772,619 = 0.83, and 0.80 to 0.86 across the range); against on demand, a little under a third (641,148 / 2,054,838 = 0.31). No rented option can sit inside Pakistan: AWS lists no Pakistan region in its price files on the day read (AWS 2026a), and every rented option would carry interval load, tamper events, billing history, inspection findings and the decision record across the border, which the operator's own constraint rules out: "Customer and meter data never leave our network; models are open weights on hardware we own; no third party model service" (chapter 3, section 3.1; chapter 5, section 5.2; Table 4, "Ground"). Renting is therefore a price reference only. GLM 5.3 carries the GLM-5.3 bespoke license, whose terms "permit commercial use, fine-tuning and redistribution" (chapter 8); BGE-M3 is MIT and Chronos-2 is Apache 2.0 (Table 4), so no license line is priced here.

### A.2 What the Hardware Would Cost

| Option | Basis | Three year cost (USD) |
| --- | --- | --- |
| Owned, in the operator's own data center | One 8x H200 node and one single L40S server, with support and power, broken out below | 615,000 to 667,000, typical 641,000 |
| AWS, Asia Pacific (Mumbai), on demand | p5en.48xlarge, eight H200 cards, 1,128 GB of HBM3e (AWS 2026c), at 75.9552 dollars an hour, plus g6e.xlarge, one L40S card with 48 GB (AWS 2026d), at 2.235 dollars an hour (AWS 2026b), 26,280 hours each; outside Pakistan | 2,054,838 (1,996,103 + 58,736) |
| AWS, Asia Pacific (Mumbai), three year Compute Savings Plan, all upfront | p5en.48xlarge at 50.6602 dollars an hour plus g6e.xlarge at 1.05134 dollars an hour (AWS 2026a), 26,280 hours each; outside Pakistan | 1,358,979 (1,331,350 + 27,629) |
| AWS, Asia Pacific (Mumbai), three year EC2 Instance Savings Plan, all upfront | p5en.48xlarge at 28.55916 dollars an hour plus g6e.xlarge at 0.84036 dollars an hour, the deepest three year plans for these instances in the region (AWS 2026a), 26,280 hours each; outside Pakistan | 772,619 (750,535 + 22,085) |

The purchase option priced as the rental reference is the three year EC2 Instance Savings Plan, all upfront, the lowest three year rate the ap-south-1 file lists for each instance (the partial upfront and no upfront three year Instance plans list 30.38208 and 32.81265 dollars an hour for p5en.48xlarge and 0.894 and 0.96552 for g6e.xlarge). Egress, storage of the mirrored records and the network link to the region are excluded, and the all upfront plans are paid in full on day one, so every rented figure is a floor.

The owned line, item by item:

| Line | Basis | Three year cost (USD) |
| --- | --- | --- |
| Frontier node | Thinkmate GPX GXS5-2508-8HGX-H2, 5U, NVIDIA HGX H200 with eight H200 SXM5 cards (1.1 TB of HBM3), two Intel Xeon Platinum 8558 processors, 32 x 32 GB of DDR5 memory, 3000 W 4+2 redundant power and a three year depot warranty, the configurator's default build at a configured price of 407,660 dollars (Thinkmate 2026) | 407,660 |
| Inference server | Puget Systems E222-2U, a 2U server with two AMD EPYC 9005 processors, 1+1 redundant 2000 W power and a three year parts warranty, at its published starting price of 16,475.38 dollars, plus one NVIDIA L40S 48 GB card at the builder's option price of 9,882.00 dollars (Puget 2026a; Puget 2026b) | 26,357 |
| Support | 8 to 12 percent of hardware value a year (Introl 2026), 10 percent typical, on 434,017 dollars over three years | 104,164 to 156,246, typical 130,205 |
| Power | The paper states no power figure, so this line takes the 10.2 kW maximum NVIDIA gives for its own eight H200 system (NVIDIA 2026b) plus the 2 kW rating of one of the server's power supply modules (Puget 2026b) as a ceiling: 12.2 kW x 26,280 hours = 320,616 kWh, times a power usage effectiveness of 1.6 (above the 1.54 industry average, Uptime Institute 2025) = 512,986 kWh, at the uniform commercial tariff for a sanctioned load of 5 kW and above, 39.76 rupees per kWh, plus the fixed charge of 1,250 rupees per kW of sanctioned load a month on a 20 kW sanctioned load for 36 months (NEPRA 2026), at 276.84 rupees to the dollar (X-Rates 2026): 73,675 dollars of energy and 3,251 dollars of fixed charges | 76,926 |
| **Total** | Low: 8 percent support. High: 12 percent. Typical: 10 percent. Power at the ceiling in all three | **615,107 to 667,189, typical 641,148** |

The power line is a ceiling: it takes the node's system maximum and the server's full supply rating around the clock, against an H200 card's "up to 700W" (NVIDIA 2026a), and a work surface drafting case files for one circle will rarely hold eight cards at full draw. It prices every kilowatt hour at the base variable charge of the uniform schedule, excluding the monthly fuel and quarterly adjustments, sales tax and the other levies that a Pakistani commercial bill carries, so the energy line will read higher on a real bill; a time of use connection would bill 43.82 rupees at peak and 35.15 off peak instead (NEPRA 2026). The reseller prices are United States dollar prices from United States builders, before Pakistani customs duty, sales tax and freight, and a written quote delivered to Pakistan will differ.

Why this hardware: the paper's sizing line is explicit, "the 1.2 planning factor for KV cache and activations lifts what the GPUs must hold to 904 GB. One node of eight GPUs of the 141 GB class provides 1,128 GB" (chapter 7, section 7.1), and Table 4 fixes the class as "one node of the 141 GB HBM class", held at one node because "doubling the hardware doubles export-license exposure" (Table 2). Eight H200 cards at 141 GB are 1,128 GB, and that is the node priced, as Thinkmate's HGX H200 configuration and as p5en.48xlarge, whose eight H200 cards carry the same 1,128 GB (AWS 2026c; NVIDIA 2026b). The second server is "a dual-socket server with a 48 GB PCIe inference GPU" on which "both fit on the 48 GB card with two orders of magnitude of headroom" (chapter 7, section 7.1), and that is the single L40S server priced, as Puget's E222-2U with one card and as g6e.xlarge, whose one L40S carries 48 GB (AWS 2026d).

Two inconsistencies in the paper's own numbers, neither of which changes the node count or the price: the weights are 753 GB in chapter 7, section 7.1 and Table 4, but "about 756 GB of weights at FP8" in Table 2, chapter 8, Table 6 and Figure 7; and chapter 7 counts 1,128 GB on the node while Table 6 and Figure 9 give "about 1,038 GB usable". 756 GB times 1.2 is 907 GB, which either total holds.

### A.3 What the Price Does Not Include

- **An export licence determination, which is a checkpoint, not a price.** The paper makes "a license determination" precede "any card commitment for Pakistan" (chapter 3, section 3.1; chapter 7, section 7.1; Table 5). Pakistan sits in Country Groups D:2, D:3 and D:4 (eCFR 2026a), and 15 CFR 742.6(a)(6)(iii)(A), as it reads on the day, carries a worldwide licence requirement for 3A090.a and 4A090.a items, with D:4 destinations named again in (iii)(B) (eCFR 2026b). The order date for the node is therefore set by that determination, and the paper's "non-US accelerator class held open as the alternative" (Table 1) is not priced because the paper names no class for it.
- **Everything the paper's scope boundary keeps out**: SCADA integration, meter installation, model training, prosecution and recovery, transaction advisory, "hardware and infrastructure, third-party license fees, historic data migration, estate-wide training, round the clock support" (Table 2, "Out of scope"). The seven systems of record are the operator's own and carry no line here; interface charges levied by their vendors "are payable by the operator" (chapter 9, section 9.5).
- **The servers for the rest of the stack**: the ontology or graph store, the TimescaleDB time series store for several hundred thousand meters, the Kafka backbone, Keycloak, Chrony, Prometheus and the air gapped Harbor registry are chosen by class and not sized in the paper (chapter 4, Table 7; chapter 5, section 5.2).
- **Facilities work** for the node's load and cooling in the operator's data center or colocation, and any colocation fee if the operator rents the room rather than owning it, which the paper leaves open ("an in-country sovereign data center or colocation").
- **People**: the engineers who build and run the platform, and the subdivision engineers, inspection officers, revenue officers and the Grade 17 officer who approve every draft, whom every option carries.
- **Customs duty, sales tax, freight and installation** on the hardware, which a written quote delivered to Pakistan settles, and residual value at the end of three years.
- **Double counted cover.** Both configured prices already carry a three year warranty, so the support line may count some cover twice.
- **A closed model token comparison**, which is not printed because the paper states no token volume for the work surface.

### A.4 Sources for This Appendix

- AWS. 2026a. EC2 Instance and Compute Savings Plans price files, region index and ap-south-1, version 20261107012235, as read 8 November 2026. <https://pricing.us-east-1.amazonaws.com/savingsPlan/v1.0/aws/AWSComputeSavingsPlan/current/region_index.json> and <https://pricing.us-east-1.amazonaws.com/savingsPlan/v1.0/aws/AWSComputeSavingsPlan/20261107012235/ap-south-1/index.json>
- AWS. 2026b. EC2 on demand price data for the AWS pricing page, Linux, shared tenancy, Asia Pacific (Mumbai), as read 8 November 2026. <https://b0.p.awsstatic.com/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-ondemand-without-sec-sel/Asia%20Pacific%20(Mumbai>)/Linux/index.json
- AWS. 2026c. Amazon EC2 P5 instances, p5en.48xlarge, eight NVIDIA H200 GPUs, 1,128 GB HBM3e, as read 27 October 2026 for the ep28 appendix and not re-read. <https://aws.amazon.com/ec2/instance-types/p5/>
- AWS. 2026d. Amazon EC2 G6e instances, NVIDIA L40S, 48 GB per GPU; g6e.xlarge with one GPU, as read 2 November 2026 for the ep34 appendices and not re-read. <https://aws.amazon.com/ec2/instance-types/g6e/>
- eCFR. 2026a. 15 CFR Part 740, Supplement No. 1, Country Groups, Pakistan in D:2, D:3 and D:4, version of 29 October 2026, as read 8 November 2026. <https://www.ecfr.gov/current/title-15/part-740/appendix-Supplement%20No.%201%20to%20Part%20740> (read through <https://www.ecfr.gov/api/versioner/v1/full/2026-10-29/title-15.xml?part=740&appendix=Supplement%20No.%201%20to%20Part%20740>)
- eCFR. 2026b. 15 CFR 742.6(a)(6)(iii), worldwide license requirement for 3A090.a and 4A090.a items, version of 29 October 2026, as read 8 November 2026. <https://www.ecfr.gov/current/title-15/section-742.6> (read through <https://www.ecfr.gov/api/versioner/v1/full/2026-10-29/title-15.xml?part=742&section=742.6>)
- Introl. 2026. GPU infrastructure TCO model, "Vendor support agreements typically cost 8-12% of hardware value annually", as read 2 November 2026. <https://introl.com/blog/gpu-infrastructure-tco-model-5-year-enterprise-ai-deployment>
- NEPRA. 2026. National Electric Power Regulatory Authority, Decision of the Authority in the matter of Federal Government motion and policy guidelines for rationalization of tariff of XWDISCOs and K-Electric, No. NEPRA/R/DG(Trf)/TRF-100/2935-57, 11 February 2026, Annex-C, GoP applicable schedule of tariff, A-2 General Supply Tariff - Commercial: for sanctioned load 5 kW and above, fixed charge 1,250 rupees per kW per month and variable charge 39.76 rupees per kWh; time of use peak 43.82 and off peak 35.15, as read 8 November 2026. <https://www.nepra.org.pk/tariff/Tariff/Ex-WAPDA%20DISCOS/2026/TRF-100%20XWDISCOS%20AND%20KE%20RATIONALIZATION%20OF%20TARIFF%2011-02-2026%202935-57.pdf>
- NVIDIA. 2026a. H200 specifications, H200 SXM, up to 700W (configurable), 141GB, as read 2 November 2026. <https://www.nvidia.com/en-us/data-center/h200/>
- NVIDIA. 2026b. DGX H100/H200 User Guide, Introduction, Table 3 Power Specifications, "10.2 kW max", and 8 x H200 GPUs with 1,128 GB total GPU memory, as read 2 November 2026. <https://docs.nvidia.com/dgx/dgxh100-user-guide/introduction-to-dgxh100.html>
- Puget. 2026a. Puget Systems 2U rackmount servers, E222-2U, "Up to 2x NVIDIA RTX or L40S", starting at 16,475.38 dollars, as read 2 November 2026. <https://www.pugetsystems.com/products/rackmount-servers/2u/>
- Puget. 2026b. Puget Systems E222-2U configurator: two AMD EPYC 9005 processors, NVIDIA L40S 48GB at add 9,882.00 dollars, 1+1 redundant 2000W CRPS 80 PLUS Platinum power supply, three year parts warranty, as read 2 November 2026. <https://www.pugetsystems.com/products/rackmount-servers/2u/e222-2u/>
- Thinkmate. 2026. GPX GXS5-2508-8HGX-H2 5U H200 Xeon server, online configurator, default configuration, configured price 407,660 dollars, as read 2 November 2026. <https://www.thinkmate.com/system/gpx-gxs5-2508-8hgx-h2>
- Uptime Institute. 2025. Global Data Center Survey 2025, average annual PUE of 1.54, as read 2 November 2026. <https://intelligence.uptimeinstitute.com/resource/uptime-institute-global-data-center-survey-2025>
- X-Rates. 2026. US dollar to Pakistani rupee, 1.00 USD = 276.842488 PKR, 8 November 2026 02:50 UTC, as read 8 November 2026; the State Bank of Pakistan's own rate pages did not load for direct reading that day. <https://www.x-rates.com/calculator/?from=USD&to=PKR&amount=1>

SOURCES

## Source Register

Nserbt. 2025. Nova Scotia Energy Board. <https://nserbt.ca/sites/default/files/M12273%20-%20Incident%20Report%20%28redacted%29.pdf>

Chuden. 2023. Chubu Electric Power Co., Inc. Report on the business improvement recommendations from the Electricity and Gas Market Surveillance Commission and guidance from. <https://www.chuden.co.jp/english/corporate/releases/pressreleases/1210773_5163.html>

CISA. 2022. AA22-083A: TTPs of Indicted State-Sponsored Russian Cyber Actors Targeting the Energy Sector. <https://www.cisa.gov/sites/default/files/publications/AA22-083A_TTPs_of_Indicted_State-Sponsored_Russian_Cyber_Actors_Targeting_the_Energy_Sector.pdf>

Natlawreview. 2018. $2.7 Million NERC Penalty Due to Data Exposure. <https://natlawreview.com/article/data-exposure-vendor-leads-to-27-million-nerc-penalty-utility>

---

### About CodeNinja

CodeNinja is a Middle Eastern American artificial intelligence lab and system of context company. It builds sovereign self-improving systems that organizations own, run inside their own boundary and improve with every decision they make.

[codeatoms.ai](https://codeatoms.ai)
