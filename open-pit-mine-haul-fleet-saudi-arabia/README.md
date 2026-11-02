# Industrial AI for an Open Pit Mine Haul Fleet in Saudi Arabia

*VERTICAL-DRIVEN ARCHITECTURES · MINING · DESIGNED WITH CODENINJA PRAXIS · NOVEMBER 2026*

A sovereign reference architecture for industrial AI in mining in Saudi Arabia: one governed fleet ontology of sixteen objects over five systems of record, four open-weight models across the truck, the shovel and the site server room on the operator's own hardware, and named people approving every draft.

**Canonical page:** https://codeatoms.ai/open-pit-mine-haul-fleet-saudi-arabia/
**DOI:** https://doi.org/10.5281/zenodo.23889774
**Paper:** [PDF](paper/open-pit-mine-haul-fleet-saudi-arabia.pdf) · [HTML](paper/open-pit-mine-haul-fleet-saudi-arabia.html) · [Word](paper/open-pit-mine-haul-fleet-saudi-arabia.docx) · [Appendix A, what ownership costs over three years](paper/appendix_a_cost.md)
**Licence:** CC BY 4.0. Cite the canonical page.

## At a glance

| Part | The design |
|---|---|
| Sources | Five systems, entering through two adapter families (the integration adapter for vendor APIs, database reads and file exports, the telemetry adapter for high rate signals) that stamp every fact with its source system, provenance class and a synchronized timestamp: the fleet management and dispatch system, the original equipment makers' telematics, the maintenance management system, the oil laboratory and the mine plan, all read only; the two writes are approved haul redrafts back into the fleet system and approved work orders back into the maintenance system, each with an audit trail |
| Object model | 16 typed objects with 13 labelled typed links, from the haul truck, shovel, component and haul road segment through the haul cycle, payload record, telematics alarm, oil sample and tyre reading to the work order, rebuild, ground engaging tool and shift, with the maintenance planner, dispatcher and mine superintendent, published as JSON for reuse |
| Models | GLM 5.3 (bespoke licence, 753B at FP8) for reasoning, the conversational interface and the agents' drafts; Grounding DINO Swin-T (Apache-2.0, about 345 MB at 16 bit) for shovel bucket tooth detection at the edge; Chronos-2 (Apache-2.0) for zero shot telemetry and oil trend forecasting with covariates; BGE-M3 (MIT) for evidence retrieval so every answer cites its record; nothing trained into weights |
| Compute | One node of eight 141 GB cards (1,128 GB) in the site server room, holding 753 GB of FP8 weights with a 1.2 planning factor, 904 GB, at roughly ten kilowatts; rack servers beside it for forecasting and embedding; heat rated automotive grade SoC edge units, fanless, on the trucks and at the shovel bucket camera. The node is a 4A090.a class item for a D:3 and D:4 destination, so a BIS licence determination belongs in phase one (Appendix A.3). Nothing leaves; updates arrive one way through a hardware enforced data diode |
| Rollout | Four phases carrying 18 scope items (5, 6, 6, then 1) behind four gates: the fleet ontology standing on the systems of record, the private LTE network across the pit, the tooth loss stop agent, and a six month measured run of one pit's haul fleet of about 35 trucks and one 600 tonne class shovel against the operator's own baselines of unplanned downtime, mean time between failures, tooth loss reaching the crusher and cost per tonne |
| Three-year cost | About 556,000 US dollars to own the reasoning node for three years (a range of 528,000 to 580,000: server, support and power at the Saudi industrial electricity tariff), against about 751,000 to rent the same eight cards on the cheapest three year commitment in AWS Middle East (UAE), an EC2 Instance Savings Plan, all upfront, so ownership costs about three quarters of it. Renting is a price reference only, because AWS lists no Saudi region on the day read and every rented option would carry fleet records across the border (Appendix A) |
| Human control | Agents draft and named people decide: the maintenance planner approves each health ranking, the dispatcher approves each haul redraft, the shovel operator confirms each tooth loss, and the mine superintendent owns the command center and holds escalation authority; no agent stops a machine or changes a work order without a named approval, except the tooth loss stop, which follows the site safety procedure |

**Made with.** Reasoned on [CodeNinja Praxis](https://codeatoms.ai/praxis/), the CodeNinja Atoms platform for designing physical AI systems. The object model imports into [Hyper Ontology](https://codeatoms.ai/hyper-ontology/), which turns it into a living system. Load it with the [hyper-ontology loader](../hyper-ontology-py/): `hyper-ontology show open-pit-mine-haul-fleet-saudi-arabia`. Both are in beta; access by request.

## Abstract

*A Failing Final Drive Leaves Evidence Long Before It Fails*

When a haul truck's final drive fails on the ramp, the question an open pit mine operator in Saudi Arabia needs industrial AI to answer is which machine fails next and what the planner should do about it today, and that question cannot be answered with the data as it stands: the alarm lives in the operator's own telematics, the wear metals in the laboratory's oil findings, the payload history in the fleet management and dispatch system, the rebuild hours in the maintenance management system and the ramp itself in the mine plan, and no one of those systems can see the other four. Reference architectures for industrial AI exist for exactly this condition, because the join has to happen somewhere, the data may not leave the site, and the pit must keep working when the link to the city fails.

The design is a sovereign, offline-capable system for one pit: five sources of record joined through two adapter families into a governed fleet ontology of sixteen objects, with seven services and five surfaces serving a control room command center, and four models placed across three tiers: GLM 5.3, at 753 billion parameters served at FP8 on one node of eight 141 GB GPUs, runs reasoning and the conversational interface on the site's own servers; Chronos-2 forecasts telemetry and oil trends and BGE-M3 embeds evidence for cited answers on the same site tier; Grounding DINO open weights run on heat-rated automotive-grade edge units on the trucks and at the shovel bucket camera, where vibration, motor current and camera evidence is gathered even when coverage drops. Three named agents draft for named people: a health agent on a new alarm, oil result or tyre reading for the maintenance planner, a tooth loss agent on a shovel camera detection for the shovel operator, and a dispatch agent on a truck pulled from service for the dispatcher, with every work order outcome feeding memory, never weights. Phase one runs one pit's haul truck fleet, about 35 trucks and one 600 tonne class shovel, for six months against the operation's own baselines of unplanned downtime, mean time between failures, tooth loss events reaching the crusher and cost per tonne.

The paper covers the industry problem and the join failure across the five systems, the constraints and the stack, the sixteen-object fleet ontology and how every source enters it through an adapter, the placement of inference across edge and site tiers, the four models and the licenses that let the operator hold their weights, the four phases with their eighteen items, gates and measured run, what the operator owns at the end, and finally how Praxis contextualized and reasoned the design.

## The object model

`ontology/objects.json` holds the 16 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology.

| Kind | Objects |
|---|---|
| asset | Haul Truck, Shovel, Component, Haul Road Segment, Ground Engaging Tool |
| event | Haul Cycle, Telematics Alarm, Rebuild, Shift |
| measure | Payload Record, Oil Sample, Tyre Reading |
| record | Work Order |
| actor | Maintenance Planner, Dispatcher, Mine Superintendent |

## The model and equipment register

`register/models.csv`, read from the paper's model and equipment register (Table 4) and chapters 7 and 8: every model, its licence and weight, every hardware class and sizing rule.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on Praxis, CodeNinja's platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
