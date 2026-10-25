# Port Drone Watch: From Oil Sheen to Dispatched Work on the Port's Own Hardware in Germany

*VERTICAL-DRIVEN ARCHITECTURES · MARITIME & PORTS · DESIGNED WITH CODENINJA PRAXIS · OCTOBER 2026*

An open reference architecture for physical AI in maritime and ports in Germany: a docked drone network at two port sites turned into detections, dispatched work items with a named responder and a living map, fifteen objects over five source systems, five open-weight models on three tiers of the authority's own hardware, and people deciding every response.

**Canonical page:** https://codeatoms.ai/drone-detection-dispatch-port-germany/
**DOI:** https://doi.org/10.5281/zenodo.23635729
**Paper:** [PDF](paper/drone-detection-dispatch-port-germany.pdf) · [HTML](paper/drone-detection-dispatch-port-germany.html) · [Word](paper/drone-detection-dispatch-port-germany.docx) · [Appendix A, what ownership costs over three years](paper/appendix_a_cost.md)
**Licence:** CC BY 4.0. Cite the DOI on the release, or the canonical page.

## At a glance

| Part | The design |
|---|---|
| Sources | Five systems, entering through one integration adapter family: the port GIS berth plan and asset register, the drone operator's mission and fleet system, the responders' existing work systems (read for status, work records pushed out), the vessel traffic feed (AIS/VTS) and the port's works register and weather feed, confirmed at the interface survey |
| Object model | 15 typed objects with 14 typed links, from the mission, drone, dock station and restricted zone through the detection, work item, flight authorisation and coverage statement to the berth, vessel, quay asset, construction work, responder role, drone operator and weather observation, published as JSON for reuse |
| Models | RF-DETR (Apache-2.0) for per-frame detection at the dock; OWLv2 (Apache-2.0) for zero-shot passes on oil sheen, debris, smoke and damage; Ministral 3 8B (Apache-2.0) for evidence triage and work item drafting; Roboflow trackers (Apache-2.0) for motion and association; GLM 5.3 (bespoke licence, 753B at FP8) for the agentic work surface; nothing trained into weights |
| Compute | Three tiers on the authority's own hardware: a GPU-class edge box at each dock, sized at the dock site survey; a site server at each port site with one to four 48 GB PCIe cards; and one node of eight 141 GB HBM cards (1,128 GB) in the port's own data centre, holding 753 GB of FP8 weights with a 1.2 planning factor, 904 GB. Detection events and evidence crops cross the boundary; pixels stay at the dock |
| Rollout | Four phases carrying 20 scope items (10, 4, 4, then 2) behind four gates: dock-side edge inference hardware in place, the first port site's mission set rolled out, port ownership secured through a supplier change, and the authority's own exit test; no detection class rolls out below its floor measured on the port's own two pilot missions |
| Three-year cost | About 735,000 US dollars to own the central node and the two site servers for three years (a range of 650,000 to 845,000: servers, support and power at the Eurostat non household tariff for Germany), against about 761,000 to rent the same card classes on the deepest three-year commitment in AWS Europe (Stockholm for the eight-card node, which Frankfurt does not sell, and Frankfurt for the site cards), so ownership costs about the same there, and about 2.02 million on demand, against which ownership costs about a third. Renting is a price reference only, because the imagery, the weights and the detection history stay on hardware the port owns; dock edge boxes are priced by quotation after the survey (Appendix A) |
| Human control | The system proposes and records and people decide every response: a detection stays proposed until a responder confirms, rejects or merges it, every work item is acknowledged with reason codes by its named responder role, flight approvers grant every mission, and automatic acts are limited to confirmation re-flights and notification escalation |

**Made with.** Reasoned on [CodeNinja Praxis](https://codeatoms.ai/praxis/), the CodeNinja Atoms platform for designing physical AI systems. The object model imports into [Hyper Ontology](https://codeatoms.ai/hyper-ontology/), which turns it into a living system. Load it with the [hyper-ontology loader](../hyper-ontology-py/): `hyper-ontology show drone-detection-dispatch-port-germany`. Both are in beta; access by request.

## Abstract

*A Detection Should Reach a Responder, Not a Video Archive*

For a maritime and ports authority in Germany, the question a physical AI system must answer is deceptively simple: what is happening right now on the water, the quays and the restricted zones of its two port sites, and which named person should respond. Drones already fly from docks at both sites and land hours of video and still imagery every day, but nobody can watch all of it, so oil sheen drifts, persons cross restricted zones, fenders and bollards fail and works packages slip while the footage sits unreviewed. The answer must also satisfy three regimes at once: the European specific category drone rules that govern every flight, the Seveso directives that fence the hazardous installations the drones overfly, and the GDPR rules that protect every person the cameras catch in frame.

The design turns those flights into detections and dispatched work entirely on the authority's own hardware: five source systems enter through one adapter family, fifteen objects form one typed object model, five services and eight surfaces carry the work, and five models are placed across three tiers. Per-frame closed-set detection runs on the dock's edge compute so that detection survives an uplink loss; zero-shot open-vocabulary passes and evidence-crop triage run on the port's site servers; and the frontier-class work surface model, 753 billion parameters at FP8 held by one node of eight GPUs of the 141 GB class, runs in the port's own data centre. Every detection becomes a work item with a named responder role, people decide every response, and the loop learns from what responders found through memory rather than weight training, so the imagery, the weights and the detection history survive a change of drone operator.

The paper covers the industry problem and the join failure in Part I; the constraints, the stack, the object model, ingestion, inference placement, and the models and their licences in Part II; the rollout with its phases and gates, and ownership, in Part III; and it closes with how Praxis contextualised and reasoned the design. Readers weighing industrial ontology examples will find every object and typed link in chapter 5.

## The object model

`ontology/objects.json` holds the 15 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology.

| Kind | Objects |
|---|---|
| site | Berth, Dock Station, Restricted Zone |
| asset | Vessel, Quay Asset, Drone |
| record | Detection, Work Item, Flight Authorisation, Coverage Statement |
| event | Mission, Construction Work |
| actor | Responder Role, Drone Operator |
| measure | Weather Observation |

## The model and equipment register

`register/models.csv`, read from the paper's model and hardware tables: every model, its licence and weight, every hardware class and sizing rule.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on Praxis, CodeNinja's platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
