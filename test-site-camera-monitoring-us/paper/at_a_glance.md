# At a glance · Camera monitoring for a vehicle proving ground in the United States

**What this is.** An open reference architecture for system design in physical AI: a fully on-premises camera monitoring system that puts every turn, crossing, pit entry and access point of a vehicle proving ground on footage the operator owns, with exportable clips and camera uptime it can prove. It is written for the proving ground operations and safety lead and for the surveillance, fiber plant and platform engineers who would build it. The operator is described by class, never by name.

**The answer in numbers.**

| Part | The design |
|---|---|
| Field estate | 40 to 60 poles of fixed thermal and visible camera heads on new underground single-mode fiber, two strands per pole, 80 to 120 streams |
| Recording | An N+1 recorder pair, open-source Frigate NVR, each holding 30 days of footage on local disk inside an isolated network |
| Object model | 15 typed objects, from camera pole and fiber run to incident record and vehicle under test, published as JSON for reuse |
| Models | D-FINE, Apache-2.0, for retrospective search over the archive (test vehicle, support vehicle, pedestrian); about 8 to 124 MB of weights |
| Compute | One 48 GB L40S-class card per recorder host, in the conditioned server room; nothing at the poles |
| Three-year cost | About 474,000 to 871,000 US dollars to own over three years, mostly camera heads; the two recorder hosts alone cost about four fifths of the deepest three-year AWS commitment, and there is no per camera license at any pole count (Appendix A) |
| Human control | Booth operators watch and decide; nothing raises an automated alarm; only the safety office can export a clip |

**Reuse it.** The object model, the model register and the figures are free to reuse under CC BY 4.0. Cite as DOI https://doi.org/10.5281/zenodo.23296077.

**Made with.** Reasoned on [CodeNinja Praxis](https://codeatoms.ai/praxis/), the CodeNinja Atoms platform for designing physical AI systems. The object model imports into [Hyper Ontology](https://codeatoms.ai/hyper-ontology/), which turns it into a living system. Both are in beta; access by request.
