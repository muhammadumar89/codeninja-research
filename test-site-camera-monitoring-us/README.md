# 

*V E R T I C A L - D R I V E N A R C H I T E C T U R E S · D I S C R E T E M A N U FA C T U R I N G & A U TO M O T I V E · D E S I G N E D W I T H P R A X I S*

· OCTOBER 2026 Pit Camera Watch: An On-Premises Camera Monitoring System for Every Turn, Crossing and Pit Entry on the Test Site A fully on-premises camera monitoring system design for a United States vehicle proving ground, putting every turn, crossing, pit entry and access point behind owned fiber, owned recorders and per-use-case acceptance evidence.

For the proving ground operations and safety lead, the site and network supervisors, and the surveillance, fiber plant and platform engineers who would build and run it.

**Canonical page:** https://codeatoms.ai/test-site-camera-monitoring-us/
**Paper:** [PDF](paper/pit-camera-watch-on-premises-camera-monitoring-test-site-us.pdf) · [HTML](paper/pit-camera-watch-on-premises-camera-monitoring-test-site-us.html) · [Word](paper/pit-camera-watch-on-premises-camera-monitoring-test-site-us.docx) · [Appendix A, what ownership costs over three years](paper/appendix_a_cost.md)
**Licence:** CC BY 4.0. Cite the DOI on the release, or the canonical page.

## Abstract

*A Camera System Should Be Judged by Uptime, Not by Camera Count*

Can the operator see every turn, crossing, pit entry and access point of its vehicle proving ground at all times, on footage it owns, with recorded clips it can export as evidence and camera uptime it can prove? Today it cannot: the existing camera monitoring system was purchased in 2013 and is at end-of-life status, with the decay that age brings, outages, dead heads and no redundancy, and no diagram of the cabling routes it depends on. A camera count on a purchase order does not answer the question; only a surveyed, tested, owned estate does.

The design replaces the 2013 estate with a fully on-premises system on site hardware: 40 to 60 poles of fixed Power over Ethernet (PoE) camera heads on new underground single-mode fiber, two strands per pole, terminated at the operator's own termination point. The design holds three source systems, one integration adapter family, fifteen objects, four services, two surfaces and one detection model. An N+1 recorder pair with 30-day local retention serves a four-display operator booth with freely manipulable layouts, and a 48 GB class GPU in the conditioned server room runs retrospective D-FINE forensic search over the 30-day archive. Everything runs behind an isolated network gated by Section 889 supply- chain screens, with camera uptime as a first-class acceptance metric.

The paper covers the problem and its cost in Part I, the constraints, stack, object model, ingestion and inference placement in Part II, the phased rollout with gates, failure modes and ownership in Part III, and closes with the chapter on how Praxis contextualized and reasoned the design.

## The object model

`ontology/objects.json` holds the 15 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology.

| Kind | Objects |
|---|---|
| site | The site |
| asset | Camera Pole, Camera Head, Underground Fiber Run, Safety Gate, Operator Booth Display, Vehicle Under Test |
| system | Server (the operator's own system) |
| record | 30-Day Footage Archive, Incident/Accident Record |
| person | The site Operator, Gate Officer, Safety Office Reviewer |
| event | Test Cycle |
| document | The operator's own system Power/Fiber assessment package |

## The model and equipment register

`register/models.csv`, read from the paper's Table 4: every model, its licence and weight, every hardware class and sizing rule.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on Praxis, CodeNinja's platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
