# At a glance · Leak Detection, Fleet Health and Security Directive Evidence for Every Station

**What this is.** An open reference architecture for system design in physical AI. A single on-premises model of a natural gas transmission estate in the United States: passive taps watch the OT network at every station and in the gas control centers, open-weight models watch compressor health and leak indicators at the station, and a control room assistant explains each alert and drafts a response for a pipeline controller who decides every action. The security directive evidence generates itself from the monitoring. It is written for the vice president of operations and pipeline integrity, gas control and compliance managers, and the OT security, reliability, data and platform engineers who would build and run it. The operator is described by class, never by name.

**The answer in numbers.**

| Part | The design |
|---|---|
| Sources | Four named systems, all read only: the historian on AVEVA PI System open APIs, the alarm and event stream, the CMMS and the corporate identity directory, entering through three adapter families (Telemetry, Ops systems, Integration); nothing ever addresses a field device |
| Object model | 14 typed objects and 13 typed links, from the compressor station, the meter station, the pipeline segment and the compressor unit through the alarm, the leak or abnormal operation event and the work order to the pipeline controller and the security directive control, published as JSON for reuse |
| Models | Mistral Large 3 675B (Apache-2.0) for the control room assistant, the compliance agent and the work surface; Chronos-2 (Apache-2.0) for telemetry forecasting with residual anomaly detection; RF-DETR Apache sizes for station camera scene detection; BGE-M3 (MIT) for retrieval |
| Compute | At each station, volume production edge modules in 7W to 60W envelopes inside hazardous area enclosures, detecting through backhaul loss; centrally, one node of eight 141 GB HBM-class GPUs in the gas control center |
| Rollout | Two phases carrying 17 scope items: 16 items across six workstreams at the pilot stations, gated by an API RP 1130 computational pipeline monitoring test per segment, then the fourteen station fleet rollout; 3 of 3 requirements covered |
| Three-year cost | About 465,000 US dollars to own the control center node for three years (432,000 to 485,000), about three quarters of the 625,000 the deepest AWS commitment in US East costs and well under the 1.66 million on demand; the station modules, enclosures, cameras, diodes and sensors are priced by quotation (Appendix A) |
| Human control | The system never writes to a field device and shutdown stays with the certified control paths; a hardware one-way diode is the only way out of each station OT zone; every decision-influencing model runs in shadow mode before any controller-facing alert, and a named controller confirms or clears every leak event |

**Reuse it.** The object model, the model register and the figures are free to reuse under CC BY 4.0. Cite the canonical page, https://codeatoms.ai/pipeline-integrity-gas-transmission-us/, until the DOI is minted on release.

**Made with.** Reasoned on [CodeNinja Praxis](https://codeatoms.ai/praxis/), the CodeNinja Atoms platform for designing physical AI systems. The object model imports into [Hyper Ontology](https://codeatoms.ai/hyper-ontology/), which turns it into a living system. Both are in beta; access by request.
