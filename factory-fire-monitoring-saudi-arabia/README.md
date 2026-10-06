# OCTOBER 2026 Factory Fire Watch: Read-Only Smart Fire Protection Monitoring for Every

*V E R T I C A L - D R I V E N A R C H I T E C T U R E S · H E AV Y I N D U S T R Y & C O N S T R U C T I O N · D E S I G N E D W I T H P R A X I S ·*

High-Risk Factory A smart fire protection monitoring design that gives a heavy industry and construction operator live, read-only visibility of fire alarm panels, fire pumps, fire water reserves and energy consumption across its highest-risk factories, published into its own IoT platform hosted in Saudi Arabia.

For the safety and operations executive accountable for fire risk at a heavy industry and construction operator, factory and reliability leads, and the instrumentation, radio, integration and platform engineers who would build and run it.


**Made with:** [Praxis](https://codeatoms.ai/praxis/) (design) and [Hyper Ontology](https://codeatoms.ai/hyper-ontology/) (living system). Load the object model with the [hyper-ontology loader](../hyper-ontology-py/): `hyper-ontology show factory-fire-monitoring-saudi-arabia`.

**Canonical page:** https://codeatoms.ai/factory-fire-monitoring-saudi-arabia/
**Paper:** [PDF](paper/factory-fire-watch-fire-protection-monitoring-industrial-cities-saudi-arabia.pdf) · [HTML](paper/factory-fire-watch-fire-protection-monitoring-industrial-cities-saudi-arabia.html) · [Word](paper/factory-fire-watch-fire-protection-monitoring-industrial-cities-saudi-arabia.docx) · [Appendix A, what ownership costs over three years](paper/appendix_a_cost.md)
**DOI:** [10.5281/zenodo.23126565](https://doi.org/10.5281/zenodo.23126565) (all versions: [10.5281/zenodo.23126564](https://doi.org/10.5281/zenodo.23126564))
**Licence:** CC BY 4.0. Cite the DOI on the release, or the canonical page.

## Abstract

*A Fire Estate Should Report Its Own Silence*

The operation needs one answer at all hours: are the fire alarm panels, fire pumps, fire water reserves and energy feeds in its highest-risk factories alive, within limits, and provably monitored. It cannot answer that today because panel status, pump health, tank levels and meter readings sit behind separate or unmonitored equipment, and a sensor that has stopped reporting still reads as normal, so the worst failure mode is silence that looks like safety.

The design adds a read-only smart fire protection monitoring layer across the eight pilot high-risk factories: fire alarm control panel status, fire pump controllers, fire water tank level transmitters and current transformer energy meters enter through LoRaWAN field connectivity and per-site backhaul, cross two adapter families into fourteen objects and seven services surfaced on two screens, all published as

one owned object model over secure MQTT into the operator's existing Saudi-hosted IoT platform, hardened to national cybersecurity controls for operational technology, with one small forecasting model running centrally on CPU inside that platform. No write path into certified fire equipment exists anywhere in the design.

The paper states the problem and its documented cost, shows why each existing system sees only one slice of fire risk, fixes the constraints, walks the stack from field sensor to dashboard, defines the object model and its typed links, specifies ingestion and state discipline, places inference, registers the model and its license, plans a four-phase rollout with exit gates and requirement coverage, assigns ownership, and closes with the Praxis chapter that records how every choice was reasoned.

## The object model

`ontology/objects.json` holds the 14 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology.

| Kind | Objects |
|---|---|
| site | High-risk factory |
| asset | Fire alarm control panel, Fire pump, Fire water tank, Tank level transmitter, Energy meter (CT set), LoRaWAN gateway |
| measure | Monitored point |
| event | Safety-critical alert |
| record | Audit log record, Periodic monitoring round, Preventive maintenance visit |
| person | Technical personnel |
| actor | Monitoring officer |

## The model and equipment register

`register/models.csv`, read from the paper's Table 4: every model, its licence and weight, every hardware class and sizing rule.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on Praxis, CodeNinja's platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
