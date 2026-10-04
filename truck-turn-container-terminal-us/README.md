# Terminal Pulse: Predicted Truck Turn Time and Live Yard Sight for a Container Terminal

*VERTICAL-DRIVEN ARCHITECTURES · MARITIME & PORTS · DESIGNED WITH PRAXIS · OCTOBER 2026*

A live object model of vessel, yard, gate, crane, reefer and rail data that predicts truck turn time two hours out, names the cause and watches for conflicts as they happen, for a container terminal operator in the United States.

For the terminal operations director, the yard, vessel and rail planners, and the platform, data and vision engineers who would build and run it.

*The operator in this design is an illustrative scenario written for it, not a CodeNinja customer.*


**Made with:** [Praxis](https://muhammadumar89.github.io/codeninja-research/praxis/) (design) and [Hyper Ontology](https://muhammadumar89.github.io/codeninja-research/hyper-ontology/) (living system). Load the object model with the [hyper-ontology loader](../hyper-ontology-py/): `hyper-ontology show truck-turn-container-terminal-us`.

**Canonical page:** https://muhammadumar89.github.io/codeninja-research/truck-turn-container-terminal-us/
**Paper:** [PDF](paper/terminal-pulse-truck-turn-time-container-terminal-us.pdf) · [HTML](paper/terminal-pulse-truck-turn-time-container-terminal-us.html) · [Word](paper/terminal-pulse-truck-turn-time-container-terminal-us.docx) · [Appendix A, what ownership costs over three years](paper/appendix_a_cost.md)
**DOI:** [10.5281/zenodo.23119348](https://doi.org/10.5281/zenodo.23119348) (all versions: [10.5281/zenodo.23119347](https://doi.org/10.5281/zenodo.23119347))
**Licence:** CC BY 4.0. Cite the DOI on the release, or the canonical page.

## Abstract

*A Congestion Spike Should Be Named While It Is Still Forming*

Truck turn time is the number the trucking community feels and the number a container terminal cannot currently explain while it is happening. Turn time at this operator averages 54 minutes and spikes above 90 minutes on resin export peaks, and the interacting causes live in separate systems: the terminal operating system knows the moves, the gate system knows the trucks, the crane controllers know the cycles, the cameras see the queues, and rail dwell arrives weekly after the fact. Planners stitch these slices together in their heads at the 06:00 and 14:00 operations meetings, so a spike is explained hours after the trucks have felt it, and safety conflicts in the transfer zones are found in incident reports rather than seen. The design builds one live model of the terminal. Eleven source systems, from the terminal operating system and gate OCR to two crane makers' controllers, the reefer monitors, railroad feeds and the existing 220-camera estate, enter through three adapter families into a model of twelve objects with typed links, served by seven services and four decision surfaces. Five models carry the intelligence: detectors and trackers on edge compute at the yard blocks and gate, time series forecasting and retrieval embeddings on a site inference node, and frontier open weights on an eight-GPU node inside the operator's own data center within its facility security boundary, so no data leaves the site and every reassignment remains a planner's decision made inside the terminal operating system. The paper opens with the problem and the join failure across the terminal's systems, then sets the constraints, the layered stack, the twelve-object model, ingestion through the adapter tier, and the placement of inference from the yard edge to the operator's own hardware, before registering the five models and their licenses. Part III covers the phased rollout, whose first gate proves or redirects the yard-side hypothesis using gate OCR data the operator already holds, and the ownership of everything built. It closes with the Praxis chapter, which traces every design choice back to what was recorded.

## The object model

`ontology/objects.json` holds the 12 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology.

| Kind | Objects |
|---|---|
| event | Vessel Call, Truck Visit |
| material | Container |
| site | Yard Block, Transfer Zone |
| asset | RTG, Ship to Shore Crane, Gate Lane, Reefer Plug |
| record | Rail Cut, Safety Event |
| person | Yard Person |

## The model and equipment register

`register/models.csv`, read from the paper's Table 4: every model, its licence and weight, every hardware class and sizing rule.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on Praxis, CodeNinja's platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
