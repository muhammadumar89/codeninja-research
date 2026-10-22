# Pipeline Integrity Watch: Leak Detection, Fleet Health and Security Directive Evidence for Natural Gas Transmission in the United States

*VERTICAL-DRIVEN ARCHITECTURES · OIL & GAS · DESIGNED WITH CODENINJA PRAXIS · OCTOBER 2026*

An open reference architecture for pipeline integrity at a natural gas transmission operator in the United States, in oil and gas: passive OT network monitoring with self-generating TSA security directive evidence, compressor fleet health, leak and abnormal operation detection, a fourteen-object pipeline ontology, and four open-weight models on the operator's own hardware.

**Canonical page:** https://codeatoms.ai/pipeline-integrity-gas-transmission-us/
**DOI:** https://doi.org/10.5281/zenodo.23556374
**Paper:** [PDF](paper/pipeline-integrity-watch-pipeline-integrity-gas-transmission-us.pdf) · [HTML](paper/pipeline-integrity-watch-pipeline-integrity-gas-transmission-us.html) · [Word](paper/pipeline-integrity-watch-pipeline-integrity-gas-transmission-us.docx) · [Appendix A, what ownership costs over three years](paper/appendix_a_cost.md)
**Licence:** CC BY 4.0. Cite the DOI on the release, or the canonical page.

## At a glance

| Part | The design |
|---|---|
| Sources | Four named systems, all read only: the historian on AVEVA PI System open APIs, the alarm and event stream, the CMMS and the corporate identity directory, entering through three adapter families (Telemetry, Ops systems, Integration); nothing ever addresses a field device |
| Object model | 14 typed objects and 13 typed links, from the compressor station, the meter station, the pipeline segment and the compressor unit through the alarm, the leak or abnormal operation event and the work order to the pipeline controller and the security directive control, published as JSON for reuse |
| Models | Mistral Large 3 675B (Apache-2.0) for the control room assistant, the compliance agent and the work surface; Chronos-2 (Apache-2.0) for telemetry forecasting with residual anomaly detection; RF-DETR Apache sizes for station camera scene detection; BGE-M3 (MIT) for retrieval |
| Compute | At each station, volume production edge modules in 7W to 60W envelopes inside hazardous area enclosures, detecting through backhaul loss; centrally, one node of eight 141 GB HBM-class GPUs in the gas control center |
| Rollout | Two phases carrying 17 scope items: 16 items across six workstreams at the pilot stations, gated by an API RP 1130 computational pipeline monitoring test per segment, then the fourteen station fleet rollout; 3 of 3 requirements covered |
| Three-year cost | About 465,000 US dollars to own the control center node for three years (432,000 to 485,000), about three quarters of the 625,000 the deepest AWS commitment in US East costs and well under the 1.66 million on demand; the station modules, enclosures, cameras, diodes and sensors are priced by quotation (Appendix A) |
| Human control | The system never writes to a field device and shutdown stays with the certified control paths; a hardware one-way diode is the only way out of each station OT zone; every decision-influencing model runs in shadow mode before any controller-facing alert, and a named controller confirms or clears every leak event |

**Made with.** Reasoned on CodeNinja Praxis; the object model imports into Hyper Ontology.

## The object model

`ontology/objects.json` holds the 14 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology. It joins the [industrial ontology examples](https://codeatoms.ai/industrial-ontology-examples/).

| Kind | Objects |
|---|---|
| site | Compressor Station, Meter Station |
| asset | Pipeline Segment, Compressor Unit, OT Device |
| actor | Pipeline Controller |
| event | Alarm, Leak or Abnormal Operation Event, Remote Access Session |
| record | Work Order, Security Directive Control |
| system | Historian, CMMS |
| document | Hazardous Area Classification |

## The model and equipment register

`register/models.csv`, read from the paper's Table 4: every model, its licence and weight, every hardware class and sizing rule.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on CodeNinja Praxis, the CodeNinja Atoms platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
