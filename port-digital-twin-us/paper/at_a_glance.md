# At a glance · A governed digital twin for a landlord port authority in the United States

**What this is.** An open reference architecture for system design in physical AI: one authoritative digital twin that binds a port's operational systems, live sensor feeds and finance backbone into a thirteen-object ontology, self-hosted on the port's own virtual machines inside the continental United States. It is written for port information technology leaders and for the GIS, integration and data engineers who would build it. The operator is described by class, never by name.

**The answer in numbers.**

| Part | The design |
|---|---|
| Sources joined | 8 operational systems, 5 live sensor feeds and 1 finance backbone, including the port community system, the GIS estate, AIS vessel tracking, the gate system and environmental sensors |
| Object model | 13 typed objects and 13 links, with the berth as the focal object, published as JSON for reuse |
| Models | One self-hosted open model, BGE-M3, for document retrieval; no generative model and no token stream |
| Compute | No equipment bought: about 1.1 GB of fp16 weights on the port's existing enterprise virtual machines |
| Boundary | Everything runs inside the continental United States on infrastructure the port already operates; no hosted document AI service in the path |
| Three-year cost | No hardware line to price: the design adds software and integration work to servers the port already runs |
| Human control | The twin shows; pilots, berth planners, engineers and finance staff decide in their own systems, and nothing writes back into a system of record |

**Reuse it.** The object model, the model register and the figures are free to reuse under CC BY 4.0.
