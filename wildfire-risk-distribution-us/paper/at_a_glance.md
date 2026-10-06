# At a glance · Live wildfire ignition risk for an electric distribution cooperative in the United States

**What this is.** An open reference architecture for system design in physical AI: a live ignition and outage risk score for every distribution feeder segment, built on the cooperative's own hardware, with every de-energisation and fast-trip change approved by a named operator. It is written for operations and engineering leaders at distribution utilities and for the engineers who would build it. The operator is an illustrative scenario, not a CodeNinja customer.

**The answer in numbers.**

| Part | The design |
|---|---|
| Sources joined | 12 systems, including SCADA, GIS, the AMI head end, the outage management system, work management, wildfire camera and weather feeds |
| Object model | 14 typed objects and 12 links, published as JSON for reuse |
| Models | Self-hosted open-weight models: GLM 5.2 under MIT (reasoning) on site, RF-DETR (vision) at the edge |
| Frontier compute | One node of eight 141 GB HBM-class GPUs holds GLM 5.2 at FP8 (753 GB of weights, 904 GB with headroom) |
| Edge | Sealed industrial boxes at substations and on patrol trucks detect smoke and damaged equipment when cellular coverage drops |
| Three-year cost, owned | About 841,000 US dollars with support and power at the Texas industrial power price |
| Three-year cost, rented | 0.88 million to 1.92 million US dollars for the same GPUs around the clock; ownership costs about the same as the deepest three-year commitment (version 2) |
| Closed model break-even | The cheapest closed model matches the owned stack at about 41 users; above that, ownership is cheaper and the gap grows with every user |
| Human control | Every public safety power shutoff (PSPS) recommendation becomes a decision record a named operator approves or declines; the design never opens or closes a recloser |

**Reuse it.** The object model, the model register and the figures are free to reuse under CC BY 4.0.

**Made with.** Reasoned on [Praxis](https://codeatoms.ai/praxis/), CodeNinja's platform for designing physical AI systems. The object model imports into [Hyper Ontology](https://codeatoms.ai/hyper-ontology/), which turns it into a living system. Both are in beta; access by request.
