# At a glance · Three-day schedule slip forecasts for a construction site in Saudi Arabia

**What this is.** An open reference architecture for system design in physical AI: one live model of a construction site's structure phase that forecasts schedule slips three days out and shows safety breaches as they happen, on the contractor's own hardware inside the Kingdom. It is written for construction directors and for the engineers who would build it. The operator is an illustrative scenario, not a CodeNinja customer.

**The answer in numbers.**

| Part | The design |
|---|---|
| Sources joined | 12 systems, including Primavera P6, batch plant SCADA, the casting bed register, the lift schedule, crane anti-collision logs, haulage GPS, gate logs and biometric turnstiles |
| Object model | 15 typed objects and 12 links, published as JSON for reuse |
| Models | 5 self-hosted open models: GLM 5.3 (reasoning), Chronos-2 (forecasting), BGE-M3 (multilingual retrieval), RF-DETR (vision), Roboflow trackers |
| Frontier compute | One node of eight 141 GB HBM-class GPUs holds GLM 5.3 at FP8 (753 GB of weights, 904 GB with headroom) |
| Edge | Five Jetson Orin class nodes in solar powered enclosures at the gate, laydown, crane slew zone, batch plant and haul road |
| Three-year cost, owned | About 642,000 US dollars with support and power at the Saudi industrial tariff |
| Three-year cost, rented | 1.41 million to 2.81 million US dollars for the same GPUs around the clock; ownership is about one half the cheapest three-year commitment |
| Closed model break-even | The cheapest closed model matches the owned stack at about 31 users; above that, ownership is cheaper and the gap grows with every user |
| Human control | Every re-sequencing is a recommendation a named planner approves; every breach alert is confirmed, dismissed or escalated by the HSE officer |

**Reuse it.** The object model, the model register and the figures are free to reuse under CC BY 4.0.
