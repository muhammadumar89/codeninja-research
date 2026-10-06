# At a glance · Read-only fire protection monitoring for high-risk factories in Saudi Arabia

**What this is.** An open reference architecture for system design in physical AI: live, read-only visibility of fire alarm panels, fire pumps, fire water tanks and energy meters across an operator's highest-risk factories, read through contacts, PLC inputs and LoRaWAN into an IoT platform hosted in Saudi Arabia, with never a write path into certified life-safety equipment. It is written for the safety and operations executive accountable for fire risk and for the engineers who would build it. The operator is described by class, never by name.

**The answer in numbers.**

| Part | The design |
|---|---|
| Sources joined | Panel general alarm contacts, pump controller PLC inputs and relays, submersible tank level transmitters, CT energy meters and field rounds, through LoRaWAN gateways into the operator's existing IoT platform |
| Object model | 14 typed objects and 12 links, with the monitored point as the focal object, published as JSON for reuse |
| Models | One: IBM Granite Tiny Time Mixers (TTM-R2), about 0.85 million parameters, Apache-2.0, on CPU inside the platform; threshold evaluation on the safety path is rule logic |
| Compute | None bought: the requirement asks for no server or GPU, and the field gateways carry no model runtime |
| Equipment, per factory | About 2,600 to 3,200 US dollars in list prices: a LoRaWAN gateway, two tank transmitters, two CT meters, four contact nodes, a switch, an enclosure and a UPS |
| Three-year cost, 100 factories | About 328,000 to 439,000 US dollars with support and power; the eight-factory pilot is about 21,000 to 26,000 of equipment |
| Human control | A monitoring officer acknowledges or escalates every safety-critical alert; the design monitors and never controls a panel, pump or valve |

**Reuse it.** The object model, the model register and the figures are free to reuse under CC BY 4.0. Cite as DOI https://doi.org/10.5281/zenodo.23126565.

**Made with.** Reasoned on [Praxis](https://codeatoms.ai/praxis/), CodeNinja's platform for designing physical AI systems. The object model imports into [Hyper Ontology](https://codeatoms.ai/hyper-ontology/), which turns it into a living system. Both are in beta; access by request.
