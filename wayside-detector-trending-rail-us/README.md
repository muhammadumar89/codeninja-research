# Wayside Trend Watch: Predictive Maintenance From Wayside Detectors for a Freight Railroad in the United States

*VERTICAL-DRIVEN ARCHITECTURES · RAIL & TRANSPORTATION · DESIGNED WITH CODENINJA PRAXIS · OCTOBER 2026*

An open reference architecture for wayside detector predictive maintenance in the United States, in rail and transportation: cross-detector trending of 29 existing detectors keyed to serialized bearings and wheelsets, a fourteen-object ontology, edge vision at a four-camera yard portal, and one ranked queue on self-hosted open weights where a person decides every set out.

**Canonical page:** https://codeatoms.ai/wayside-detector-trending-rail-us/
**DOI:** https://doi.org/10.5281/zenodo.23556421
**Paper:** [PDF](paper/wayside-trend-watch-wayside-detector-trending-rail-us.pdf) · [HTML](paper/wayside-trend-watch-wayside-detector-trending-rail-us.html) · [Word](paper/wayside-trend-watch-wayside-detector-trending-rail-us.docx) · [Appendix A, what ownership costs over three years](paper/appendix_a_cost.md)
**Licence:** CC BY 4.0. Cite the DOI on the release, or the canonical page.

## At a glance

| Part | The design |
|---|---|
| Sources | Five named systems, all read only: the wayside detector network (22 hot box and hot wheel detectors, 4 wheel impact load detectors, 2 acoustic bearing detectors, 1 automated wheel profile system), the maintenance system (CMMS/EAM), Railinc Umler and interchange services, the dispatcher advisory channel and the contractor geometry and rail flaw reports, entering through two adapter families |
| Object model | 14 typed objects with 13 typed links, from the freight car, locomotive, serialized axle bearing, wheelset and traction motor through the detector reading and the trend flag to the work order, track geometry exception, rail flaw indication and AAR interchange record, published as JSON for reuse |
| Models | gpt-oss-120b (Apache-2.0, self-hosted with vLLM) for the ranked queue and the ontology-maintaining agents; Chronos-2 (Apache-2.0) for zero-shot per-axle trend forecasting; D-FINE and PP-OCRv6 (Apache-2.0) for defect detection and reporting-mark OCR at the portal; no training run |
| Compute | At the new four-camera yard-entry portal, an octa-core NPU edge box sized from its streams, so only detections, OCR strings and short evidence frames cross a cellular link that drops for hours; centrally, one 141 GB HBM GPU class card in one node in the railroad's own data center, holding the 65.2 GB checkpoint with a 1.2 planning factor and about 63 GB to spare |
| Rollout | Three phases carrying 17 scope items (13, then 3, then 1) behind three gates: the cross-detector trending engine proven in shadow beside the existing alarm, the read-only dispatch advisory channel, then the runbook and IT handover |
| Three-year cost | About 54,000 US dollars to own the central card for three years (a range of 52,000 to 57,000, card, support and power, host server by quotation), against about 625,000 dollars to rent the smallest AWS instance that holds one such card on the deepest three-year commitment in US East and about 1.66 million on demand; the edge box, portal cameras and pilot locomotive sensing are priced by quotation (Appendix A) |
| Human control | The system advises and never acts: it touches no signal, train control or PTC system, the single-reading stop alarm to the dispatcher is unchanged, and a named person decides every set out and every slow order |

**Made with.** Reasoned on CodeNinja Praxis; the object model imports into Hyper Ontology.

## The object model

`ontology/objects.json` holds the 14 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology. It joins the [industrial ontology examples](https://codeatoms.ai/industrial-ontology-examples/).

| Kind | Objects |
|---|---|
| asset | Freight Car, Locomotive, Axle Bearing (Roller Bearing), Wheelset, Traction Motor, Wayside Detector, Track Segment |
| measure | Detector Reading |
| record | Trend Flag, Work Order, Track Geometry Exception, Rail Flaw Indication, AAR Interchange Record |
| event | Train |

## The model and equipment register

`register/models.csv`, read from the paper's Table 4: every model, its licence and weight, every hardware class and sizing rule.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on CodeNinja Praxis, the CodeNinja Atoms platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
