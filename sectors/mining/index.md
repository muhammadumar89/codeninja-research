# Physical AI for mining: questions answered

Canonical: https://codeatoms.ai/sectors/mining/
License: CC BY 4.0
Publisher: CodeNinja Atoms (https://codeatoms.ai)



## What does a physical AI system for mining look like?

A complete physical AI design for mining names what to sense, which existing systems to join, the object model that joins them, the models and hardware, the three-year cost and the person who approves every action. CodeNinja Atoms has published 1 such reference architecture for mining, each free to reuse under CC BY 4.0. Industrial AI for an Open Pit Mine Haul Fleet in Saudi Arabia (Saudi Arabia): An open reference architecture for system design in physical AI, built for an open pit mine operator in Saudi Arabia whose pit is worked by a contractor with a haul fleet of about 35 trucks of the 100 tonne class and one shovel of the 600 tonne class, where owning the reasoning node that runs it costs about 556,000 US dollars over three years. Every alarm, oil result, tyre reading, payload record and rebuild is joined on one governed fleet ontology, so the maintenance planner can ask which component on which truck fails next and catch a final drive in the workshop rather than on the ramp. The models run entirely on the operator's own hardware on site, under the Mining Investment Law and its safety regulations, the national cybersecurity controls for operational technology, the Personal Data Protection Law and export control on the GPU node.

## Which AI models can a mining operator run on its own hardware?

Each published mining design names its models and why, and every model is open-weight or no model is used at all, so the operator can run it on hardware it owns. Industrial AI for an Open Pit Mine Haul Fleet in Saudi Arabia: GLM 5.3 (bespoke licence, 753B at FP8) for reasoning, the conversational interface and the agents' drafts; Grounding DINO Swin-T (Apache-2.0, about 345 MB at 16 bit) for shovel bucket tooth detection at the edge; Chronos-2 (Apache-2.0) for zero shot telemetry and oil trend forecasting with covariates; BGE-M3 (MIT) for evidence retrieval so every answer cites its record; nothing trained into weights.

## How much compute and hardware does AI in mining need?

The compute follows from the models: the published mining designs size it as follows, from no new hardware to a full GPU node. Industrial AI for an Open Pit Mine Haul Fleet in Saudi Arabia, compute: One node of eight 141 GB cards (1,128 GB) in the site server room, holding 753 GB of FP8 weights with a 1.2 planning factor, 904 GB, at roughly ten kilowatts; rack servers beside it for forecasting and embedding; heat rated automotive grade SoC edge units, fanless, on the trucks and at the shovel bucket camera. The node is a 4A090.a class item for a D:3 and D:4 destination, so a BIS licence determination belongs in phase one (Appendix A.3). Nothing leaves; updates arrive one way through a hardware enforced data diode.

## Is it cheaper to own AI hardware or rent cloud GPUs in mining?

Each mining design prices three years of ownership in its Appendix A, with every price cited, against renting the same capacity from a cloud region at its deepest three-year commitment where hardware is bought. Industrial AI for an Open Pit Mine Haul Fleet in Saudi Arabia: three-year cost, About 556,000 US dollars to own the reasoning node for three years (a range of 528,000 to 580,000: server, support and power at the Saudi industrial electricity tariff), against about 751,000 to rent the same eight cards on the cheapest three year commitment in AWS Middle East (UAE), an EC2 Instance Savings Plan, all upfront, so ownership costs about three quarters of it. Renting is a price reference only, because AWS lists no Saudi region on the day read and every rented option would carry fleet records across the border (Appendix A).

## What ontology or object model does a mining AI system need?

The object model is the part that makes the system an ontology rather than a pipeline: typed objects for the things in the mining operation, with properties, status values and typed links. Every published design ships its object model as hyper-ontology/1 JSON that loads into Hyper Ontology. Industrial AI for an Open Pit Mine Haul Fleet in Saudi Arabia: Haul truck, Shovel, Component, Haul road segment, Haul cycle, Payload record, Telematics alarm, Oil sample, Tyre reading, Work order, Rebuild, Ground engaging tool, Shift, Maintenance planner, Dispatcher, Mine superintendent.

## Who approves the decisions an AI system makes in mining?

In every published mining design a named person makes the decision that changes the physical world; the system prepares it. Industrial AI for an Open Pit Mine Haul Fleet in Saudi Arabia: Agents draft and named people decide: the maintenance planner approves each health ranking, the dispatcher approves each haul redraft, the shovel operator confirms each tooth loss, and the mine superintendent owns the command center and holds escalation authority; no agent stops a machine or changes a work order without a named approval, except the tooth loss stop, which follows the site safety procedure.

## Sources

- [Industrial AI for an Open Pit Mine Haul Fleet in Saudi Arabia](https://codeatoms.ai/open-pit-mine-haul-fleet-saudi-arabia/) (Saudi Arabia), DOI https://doi.org/10.5281/zenodo.23889774
