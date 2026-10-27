# Physical AI for semiconductors: questions answered

Canonical: https://codeatoms.ai/sectors/semiconductors/
License: CC BY 4.0
Publisher: CodeNinja Atoms (https://codeatoms.ai)

A chip is specified, implemented, verified and handed to a foundry across separate tools, so the trace from a requirement to the check that proves it is usually rebuilt by hand.

## What does a physical AI system for semiconductors look like?

A complete physical AI design for semiconductors names what to sense, which existing systems to join, the object model that joins them, the models and hardware, the three-year cost and the person who approves every action. CodeNinja Atoms has published 1 such reference architecture for semiconductors, each free to reuse under CC BY 4.0. Silicon Ledger (Saudi Arabia): An open reference architecture for system design in physical AI, built for a fabless chip design company in Saudi Arabia that designs silicon in vendor design tool suites and hands tapeouts to an outside foundry, where owning the inference node that runs it costs about 569,000 US dollars over three years. Every requirement is traced to the block, interface and signal that implement it and to the check, test and coverage result that prove it, so the verification lead can ask which requirements have no proof and what one interface change on one block actually touches. The model runs entirely on the company's own hardware under the kingdom's data protection law, export control on the GPU node and trade secret law.

## Which AI models can a semiconductor company run on its own hardware?

Each published semiconductors design names its models and why, and every model is open-weight or no model is used at all, so the operator can run it on hardware it owns. Silicon Ledger: GLM 5.3 (bespoke licence, 753B at FP8) for the agentic work surface: the spec agent, the check agent and cited answers; BGE-M3 (MIT) for embedding and retrieval so every answer cites its record; PaddleOCR-VL 1.6 (Apache-2.0) for specification parsing at ingestion; no third party model service, nothing trained into weights.

## How much compute and hardware does AI in semiconductors need?

The compute follows from the models: the published semiconductors designs size it as follows, from no new hardware to a full GPU node. Silicon Ledger, compute: One node of eight 141 GB HBM cards (1,128 GB) in the company's own server room, holding 753 GB of FP8 weights with a 1.2 planning factor, 904 GB, at roughly ten kilowatts; no edge estate. The node is a 4A090 item for a D:4 destination, so a BIS licence determination is a phase one checkpoint, and the platform runs on the company's existing hardware until it lands. Nothing crosses outward.

## Is it cheaper to own AI hardware or rent cloud GPUs in semiconductors?

Each semiconductors design prices three years of ownership in its Appendix A, with every price cited, against renting the same capacity from a cloud region at its deepest three-year commitment where hardware is bought. Silicon Ledger: three-year cost, About 569,000 US dollars to own the node for three years (a range of 541,000 to 594,000: server, support and power at the Saudi commercial electricity tariff), against about 751,000 to rent the same eight cards on the deepest three-year commitment in AWS Middle East (UAE), so ownership costs about three quarters of it, and about 2.00 million on demand, against which ownership costs a little over a quarter. Renting is a price reference only, because AWS lists no Saudi region on the day read and every rented option would carry design records across the border (Appendix A).

## What ontology or object model does a semiconductors AI system need?

The object model is the part that makes the system an ontology rather than a pipeline: typed objects for the things in the semiconductors operation, with properties, status values and typed links. Every published design ships its object model as hyper-ontology/1 JSON that loads into Hyper Ontology. Silicon Ledger: Specification section, Requirement, Design block, Interface, Signal, Design assumption, Verification check, Test, Coverage result, Bug, Waiver, Design revision, Engineer, Verification lead, Expert lesson, Foundry handoff.

## Who approves the decisions an AI system makes in semiconductors?

In every published semiconductors design a named person makes the decision that changes the physical world; the system prepares it. Silicon Ledger: Agents draft and engineers decide: an engineer confirms each extracted requirement before it is used, with the rejection rate as a phase one gate; the verification lead approves every drafted check before it enters the regression, escalating to the senior verification expert after five working days; a reconciliation job after every sync cycle flags stale impact lists and keeps them out of citations.

## Sources

- [Silicon Ledger: Ontologies for Semiconductor Design From Specification to Tapeout in Saudi Arabia](https://codeatoms.ai/chip-design-ontology-saudi-arabia/) (Saudi Arabia), DOI https://doi.org/10.5281/zenodo.23693146
