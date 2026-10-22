# At a glance · Wayside Trend Watch: Days of Warning Before Any Stop Alarm

**What this is.** An open reference architecture for system design in physical AI. A predictive maintenance system for a freight railroad in the United States: the 29 wayside detectors the railroad already runs are trended per axle, keyed to serialized bearings, wheelsets and traction motors, and joined to work orders, interchange records and digitized contractor track reports in one object model, so the mechanical and track teams act on one ranked queue days or weeks before a single-reading stop alarm. It is written for the chief mechanical officer and the track and maintenance-of-way leads, and the mechanical, reliability, data and platform engineers who would build and run it. The operator is described by class, never by name.

**The answer in numbers.**

| Part | The design |
|---|---|
| Sources | Five named systems, all read only: the wayside detector network (22 hot box and hot wheel detectors, 4 wheel impact load detectors, 2 acoustic bearing detectors, 1 automated wheel profile system), the maintenance system (CMMS/EAM), Railinc Umler and interchange services, the dispatcher advisory channel and the contractor geometry and rail flaw reports, entering through two adapter families |
| Object model | 14 typed objects with 13 typed links, from the freight car, locomotive, serialized axle bearing, wheelset and traction motor through the detector reading and the trend flag to the work order, track geometry exception, rail flaw indication and AAR interchange record, published as JSON for reuse |
| Models | gpt-oss-120b (Apache-2.0, self-hosted with vLLM) for the ranked queue and the ontology-maintaining agents; Chronos-2 (Apache-2.0) for zero-shot per-axle trend forecasting; D-FINE and PP-OCRv6 (Apache-2.0) for defect detection and reporting-mark OCR at the portal; no training run |
| Compute | At the new four-camera yard-entry portal, an octa-core NPU edge box sized from its streams, so only detections, OCR strings and short evidence frames cross a cellular link that drops for hours; centrally, one 141 GB HBM GPU class card in one node in the railroad's own data center, holding the 65.2 GB checkpoint with a 1.2 planning factor and about 63 GB to spare |
| Rollout | Three phases carrying 17 scope items (13, then 3, then 1) behind three gates: the cross-detector trending engine proven in shadow beside the existing alarm, the read-only dispatch advisory channel, then the runbook and IT handover |
| Three-year cost | About 54,000 US dollars to own the central card for three years (a range of 52,000 to 57,000, card, support and power, host server by quotation), against about 625,000 dollars to rent the smallest AWS instance that holds one such card on the deepest three-year commitment in US East and about 1.66 million on demand; the edge box, portal cameras and pilot locomotive sensing are priced by quotation (Appendix A) |
| Human control | The system advises and never acts: it touches no signal, train control or PTC system, the single-reading stop alarm to the dispatcher is unchanged, and a named person decides every set out and every slow order |

**Reuse it.** The object model, the model register and the figures are free to reuse under CC BY 4.0. Cite as https://codeatoms.ai/wayside-detector-trending-rail-us/ (DOI to be added at deposit).

**Made with.** Reasoned on [CodeNinja Praxis](https://codeatoms.ai/praxis/), the CodeNinja Atoms platform for designing physical AI systems. The object model imports into [Hyper Ontology](https://codeatoms.ai/hyper-ontology/), which turns it into a living system. Both are in beta; access by request.
