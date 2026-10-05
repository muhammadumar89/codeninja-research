# At a glance · Predicted truck turn time for a container terminal in the United States

**What this is.** An open reference architecture for system design in physical AI: truck turn time predicted two hours out and yard congestion seen live, at a container terminal, on the operator's own hardware with no outbound connection. It is written for terminal operations leaders and for the engineers who would build it. The operator is an illustrative scenario, not a CodeNinja customer.

**The answer in numbers.**

| Part | The design |
|---|---|
| Sources joined | 11 systems, including the terminal operating system, the gate system, two crane management systems, reefer monitoring, railroad switch lists, cameras and weather and tide feeds |
| Object model | 12 typed objects and 11 links, published as JSON for reuse |
| Models | 5 self-hosted open models: GLM 5.3 (reasoning), Chronos-2 (forecasting), Qwen3-Embedding-0.6B (retrieval), RF-DETR (vision), Roboflow trackers |
| Frontier compute | One node of eight 141 GB HBM-class GPUs holds GLM 5.3 at FP8 (753 GB of weights, 904 GB with headroom), at about 10 kW |
| Edge | Fanless IP-rated enclosures at the yard blocks, gate and quay; no safety reflex crosses a network hop |
| Three-year cost, owned | About 722,000 US dollars with support and power at the US industrial power price |
| Three-year cost, rented | 0.99 million to 2.52 million US dollars for the same GPUs around the clock; ownership is about four fifths the deepest three-year commitment (version 2) |
| Closed model break-even | The cheapest closed model matches the owned stack at about 35 users; above that, ownership is cheaper and the gap grows with every user |
| Human control | Surfaces warn and propose; the named planner acts in the terminal operating system and the named safety supervisor acknowledges every safety event |

**Reuse it.** The object model, the model register and the figures are free to reuse under CC BY 4.0.

**Made with.** Reasoned on [Praxis](https://muhammadumar89.github.io/codeninja-research/praxis/), CodeNinja's platform for designing physical AI systems. The object model imports into [Hyper Ontology](https://muhammadumar89.github.io/codeninja-research/hyper-ontology/), which turns it into a living system. Both are in beta; access by request.
