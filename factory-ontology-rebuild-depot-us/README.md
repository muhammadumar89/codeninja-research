# Depot Operating Object Model: Ontologies for Unifying Factory Systems at a United States Vehicle Rebuild Depot

*VERTICAL-DRIVEN ARCHITECTURES · DISCRETE MANUFACTURING & AUTOMOTIVE · DESIGNED WITH CODENINJA PRAXIS · OCTOBER 2026*

An open reference architecture for ontologies in discrete manufacturing in the United States: one fourteen-object operating model over the production control, inventory, maintenance and test cell systems of a government vehicle rebuild depot, read-only machine interfaces, three open-weight models on the depot's own two-card server, and a named person's sign-off on every release.

**Canonical page:** https://codeatoms.ai/factory-ontology-rebuild-depot-us/
**DOI:** https://doi.org/10.5281/zenodo.23570177
**Paper:** [PDF](paper/depot-operating-object-model-factory-ontology-rebuild-depot-us.pdf) · [HTML](paper/depot-operating-object-model-factory-ontology-rebuild-depot-us.html) · [Word](paper/depot-operating-object-model-factory-ontology-rebuild-depot-us.docx) · [Appendix A, what ownership costs over three years](paper/appendix_a_cost.md)
**Licence:** CC BY 4.0. Cite the DOI on the release, or the canonical page.

## At a glance

| Part | The design |
|---|---|
| Sources | Five named systems, all read only: the production control system, the inventory system, the maintenance system, the test cell software and the OPC UA site standard, entering through one integration adapter family on the Open62541 OPC UA stack, with MTConnect and stack light and serial taps bringing legacy machine tools on beside equipment that stays |
| Object model | 14 typed objects with 13 typed links, from the power pack, vehicle hull, machine tool and power pack test cell through the machine sensor, edge gateway and condition indicator to the production and maintenance work orders, schedule proposal, part lot, test run, run report and operator role, published as JSON for reuse |
| Models | gpt-oss-120b (Apache-2.0, US origin, self-hosted with vLLM) for the agentic work surface and ontology maintenance; Chronos-2 (Apache-2.0) for zero-shot machine condition forecasting and residual anomaly detection; nomic-embed-text-v2-moe (Apache-2.0) for retrieval over work orders, maintenance and test reports; no training run |
| Compute | Fanless DIN-rail edge boxes beside each machine group and at the test cell, their class fixed by a phase one measurement of the vibration load; centrally, two cards of the 48 GB PCIe class air cooled in the depot's own server room on its existing power, holding the 65.2 GB checkpoint with a 1.2 planning factor, about 78.2 GB against roughly 88 GB usable |
| Rollout | Two phases carrying 17 scope items (16, then 1) behind one gate: entity resolution proven on a week of live production records, with power pack serial, machine asset tag, part lot and test run joined at a stated match rate, before the estate instrumentation rollout |
| Three-year cost | About 67,000 US dollars to own the two-card server for three years (a range of 62,000 to 70,000: server, support and power), against about 104,000 dollars to rent the same card class on the deepest three-year commitment in US East and about 276,000 on demand; the cheapest rental that holds the model, one 96 GB card, is about 33,000 on that commitment, so ownership is chosen for the boundary, not the price, and renting is a price reference only because data and weights stay in the government's environment; edge boxes, sensors, cameras, time card and switches are priced by quotation (Appendix A) |
| Human control | The system proposes and a person commits: the test cell operator signs every release or return, a planner approves every maintenance work order and accepts, modifies or declines every schedule proposal, and no machine, test cell or site control is ever written to |

**Made with.** Reasoned on [CodeNinja Praxis](https://codeatoms.ai/praxis/), the CodeNinja Atoms platform for designing physical AI systems. The object model imports into [Hyper Ontology](https://codeatoms.ai/hyper-ontology/), which turns it into a living system. Both are in beta; access by request.

## Abstract

*A Failed Test Run Should Explain Itself the Same Day*

When a power pack fails its scripted test run, a United States government vehicle rebuild depot needs to know which machine cut the parts, from which lot, on which shift, and whether that machine's condition was already drifting; that is exactly the question ontologies for unifying factory systems exist to answer, and today the depot cannot ask it. The answer is scattered across four systems of record that never shared a key, built from technologies that were never designed to interoperate with each other (NIST 2012). The cost of that gap is not hypothetical: a single update to a parts-ordering system halted a major automaker's production at an estimated 350 million US dollars in lost output (ABI Research 2023), and the depot's own version of the same failure is the failed power pack that returns for rework with no trace of why.

The design builds one living operating object model of fourteen typed objects as a projection over five source systems, all of which enter through a single integration adapter family over the site's OPC UA standard, with legacy machine tools and test equipment brought on read only. Eight services run on the model and reach people through three surfaces: two planner surfaces for schedules and condition-based maintenance work, and one test cell surface holding each scripted run. Three Apache-2.0 models carry the work, with condition forecasting on fanless edge boxes beside each machine group and the 117- billion-parameter work surface model on a two-card 48 GB inference server in the depot's own server room, so that every byte of data and every weight stays on government hardware inside the government facility's security rules.

The paper covers the problem and the join failure, the four constraints, the layered stack, the fourteen objects with their typed links, the ingestion path, the inference placement with its memory arithmetic, and the three models with their licenses; readers weighing industrial ontology examples will find the object model chapter shows every object in its recorded form. It then sets out the two-phase rollout with its item counts and the entity resolution gate, the ownership of what the design builds, and closes with the chapter on how Praxis contextualized and reasoned this design.

## The object model

`ontology/objects.json` holds the 14 objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology.

| Kind | Objects |
|---|---|
| asset | Power Pack, Vehicle Hull, Machine Tool, Power Pack Test Cell, Machine Sensor |
| system | Edge Gateway |
| record | Production Work Order, Maintenance Work Order, Schedule Proposal |
| material | Part Lot |
| event | Test Run |
| document | Run Report |
| actor | Operator Role |
| measure | Condition Indicator |

## The model and equipment register

`register/models.csv`, read from the paper's Table 4: every model, its licence and weight, every hardware class and sizing rule.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on Praxis, CodeNinja's platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
