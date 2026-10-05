# Grid Context Watch: One system of context for OT Security and NERC CIP Evidence

*VERTICAL-DRIVEN ARCHITECTURES · ENERGY & UTILITIES · DESIGNED WITH PRAXIS · OCTOBER 2026*

An open reference architecture for operational technology security monitoring and NERC CIP evidence at an energy and utilities operator in the United States: ten source systems read one way out of the control networks into a fourteen-object ontology, with a frontier model and an embedding model on the operator's own hardware.

For the operational technology security lead, the compliance and CIP lead, and the platform, network, data and integration engineers who would build and run it.

**Made with:** [Praxis](https://muhammadumar89.github.io/codeninja-research/praxis/) (design) and [Hyper Ontology](https://muhammadumar89.github.io/codeninja-research/hyper-ontology/) (living system). Load the object model with the [hyper-ontology loader](../hyper-ontology-py/): `hyper-ontology show ot-security-cip-evidence-us`.

**Canonical page:** https://muhammadumar89.github.io/codeninja-research/ot-security-cip-evidence-us/
**Paper:** [PDF](paper/grid-context-watch-ot-security-nerc-cip-evidence-utility-us.pdf) · [HTML](paper/grid-context-watch-ot-security-nerc-cip-evidence-utility-us.html) · [Word](paper/grid-context-watch-ot-security-nerc-cip-evidence-utility-us.docx) · [Appendix A, what ownership costs over three years](paper/appendix_a_cost.md)
**DOI:** [10.5281/zenodo.23157957](https://doi.org/10.5281/zenodo.23157957)
**Licence:** CC BY 4.0. Cite the DOI on the release, or the canonical page.

## Abstract

*An OT Estate Should Be Watched From One system of context, Not Five Fragmented Tools*

An energy and utilities operator in the United States needs one answer about its operational technology estate: what is connected to the control networks behind its more than 80 substations, whether anything on those networks is behaving abnormally, and whether that can be proven with evidence when the regional reliability regulator arrives for its next audit. Today the answer cannot be produced, because asset discovery, network monitoring, log retention, threat intelligence and compliance reporting live in separate systems that each hold one slice of the picture. The stakes are set by regulation and by events: mandatory critical infrastructure protection standards for the bulk system (FERC 2008), a federal rule requiring internal network security monitoring for high and medium impact bulk system cyber systems (Federal Register 2023), and advisories showing state-affiliated actors actively exploiting programmable logic controllers across US critical infrastructure (CISA 2026).

The design is a system of context: one living model of the operational technology estate, holding 14 object types spanning substations, assets, sensors, alerts, cases, vulnerabilities, detection rules, threat intelligence, pcap evidence and CIP evidence artefacts. It is fed by 10 source systems entering through 2 adapter families, always read-only and one-way out of the control networks, so nothing in the design ever writes into an electronic security perimeter. Seven services and 4 surfaces carry asset visibility, detection, forensics, integration and compliance work; 2 models, a frontier-class reasoning model under an MIT license and an Apache-2.0 embedding model for retrieval, run on the operator's own hardware at its data center, sized to one node of eight GPUs of the 141 GB HBM class, with no weights rented and no data leaving the boundary.

The paper proceeds in four parts. Part I states the industry problem and the join failure across the operator's existing systems. Part II gives the constraints, the stack from systems of record to surfaces, the 14-object model, ingestion through adapters, inference placement and the memory arithmetic, and the models and licenses that decide ownership. Part III lays out the four-phase rollout with item counts and measured gates, and who owns what the design builds. Part IV closes with the conclusion and Chapter 11, how Praxis contextualized and reasoned this design.

## The object model

`ontology/objects.json` holds the 14 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology.

| Kind | Objects |
|---|---|
| site | Substation |
| asset | OT Asset, Network Sensor |
| event | Anomaly Alert |
| record | Investigation Case, Vulnerability Finding, Detection Rule, Pcap Evidence Record |
| document | Threat Intelligence Item, CIP Evidence Artefact |
| person | OT Security Analyst |
| system | SIEM, Energy management system, Substation data platform |

## The model and equipment register

`register/models.csv`, read from the paper's Table 4: every model, its licence and weight, every hardware class and sizing rule.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on Praxis, CodeNinja's platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
