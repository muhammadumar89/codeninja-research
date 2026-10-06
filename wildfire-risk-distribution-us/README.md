# Feeder Firewatch: Live Ignition and Outage Risk for Every Distribution Feeder

*VERTICAL-DRIVEN ARCHITECTURES · ENERGY & UTILITIES · DESIGNED WITH PRAXIS · OCTOBER 2026*

One live distribution risk model joins reclosers, meters, poles, vegetation, weather, cameras and crews into a 48-hour ignition and outage picture for a member-owned distribution cooperative in the United States, with every de-energisation and fast-trip decision left to a named person.

For the operations and wildfire mitigation lead, the dispatch supervisor and vegetation management coordinator, and the grid, vision, data and platform engineers who would build and run it.

*The operator in this design is an illustrative scenario written for it, not a CodeNinja customer.*


**Made with:** [Praxis](https://codeatoms.ai/praxis/) (design) and [Hyper Ontology](https://codeatoms.ai/hyper-ontology/) (living system). Load the object model with the [hyper-ontology loader](../hyper-ontology-py/): `hyper-ontology show wildfire-risk-distribution-us`.

**Canonical page:** https://codeatoms.ai/wildfire-risk-distribution-us/
**Paper:** [PDF](paper/feeder-firewatch-wildfire-risk-distribution-cooperative-us.pdf) · [HTML](paper/feeder-firewatch-wildfire-risk-distribution-cooperative-us.html) · [Word](paper/feeder-firewatch-wildfire-risk-distribution-cooperative-us.docx) · [Appendix A, what ownership costs over three years](paper/appendix_a_cost.md)
**DOI:** [10.5281/zenodo.23159328](https://doi.org/10.5281/zenodo.23159328) (version 2, corrected Appendix A; all versions: [10.5281/zenodo.23119324](https://doi.org/10.5281/zenodo.23119324))
**Licence:** CC BY 4.0. Cite the DOI on the release, or the canonical page.

## Abstract

*An Ignition Risk Should Be Scored Days Ahead, Not Discovered in Smoke*

The operator needs to know which feeder segments will fail or ignite next, and what to de-energise before a red flag wind arrives. It cannot answer that today because the signals that would answer it sit apart: recloser fault counts live in SCADA, last gasp messages live in the AMI head end, pole crossarm conditions live in inspection photos in folders, vegetation records sit with the trimming contractor, and public safety power shutoff decisions are made from two websites and a phone call. The systems that know a line is dead and the systems that know the wind is coming never meet before an event. The design is one live distribution risk model built as a system of context: twelve named source systems enter through two adapter families into an ontology of fourteen objects that binds feeders, segments, poles, reclosers, meters, inspections, outages, weather, cameras, crews, work orders and PSPS decision records into a single feeder-and-pole picture. Seven services run on it, served through eight surfaces: edge vision boxes at substations and on patrol trucks detect smoke and damaged equipment where the cameras are, ruggedised servers at the operations center hold the risk store and the storm picture, and an agentic work surface on one FP8 node of the 141 GB HBM class lets four distribution engineers, six system operators and the dispatch supervisor ask what changed on a feeder and build their own agents. Two models carry the load, RF-DETR at the edge under Apache-2.0 and GLM 5.2 at the center under MIT, both held on the cooperative's own hardware, with read-only paths from every system of record and no SCADA control writes. The paper opens with the problem and the join failure across the operator's existing systems, then the design: constraints and scoping, the stack from sources to surfaces, the object model and its hosting posture, ingestion through the adapter tier and event backbone, inference placement and the latency budget, and the models and licenses that decide what the cooperative owns. Part III covers the two-phase rollout with its item counts and exit gates, requirement coverage, failure modes and ownership. Part IV closes with the Praxis chapter, tracing every choice back to what justified it.

## The object model

`ontology/objects.json` holds the 14 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology.

| Kind | Objects |
|---|---|
| site | Substation |
| asset | Feeder, Feeder segment, Pole, Recloser, Meter, Wildfire camera station |
| record | Pole inspection record, Work order, PSPS decision record |
| event | Outage event, Red flag warning |
| measure | Feeder segment ignition risk score |
| actor | Field crew |

## The model and equipment register

`register/models.csv`, read from the paper's Table 4: every model, its licence and weight, every hardware class and sizing rule.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on Praxis, CodeNinja's platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
