# Appendix A · What It Costs

The design buys no hardware and serves no model. The assessment runs on the operator's own in-country servers and storage, the model register is empty by design, and the world is read through records rather than sensors, so there is no owned-versus-rented comparison to print. The cost of this design is the assessment work itself: data collection, reconciliation, availability modelling and the root cause reviews, carried on infrastructure the operator already pays for.

## A.1 What Would Change the Answer

| Line | When it appears | How to price it |
|---|---|---|
| Document retrieval over the plant record | If the design document packs and work order history grow beyond what keyword lookup on the object model serves | One self-hosted embedding model on CPU or a single mid-range GPU card; a server of eight 48 GB class cards is about 85,000 dollars (Newegg 2026) |
| A generative work surface | If the operator later asks to query the reliability model in natural language | A frontier open-weight model on one node of eight 141 GB HBM-class GPUs, 320,000 to 420,000 dollars (Mercatus 2026), which ships to Saudi Arabia only under a US export licence |
| Live plant data | If a later phase replaces exports with live historian feeds | The operator's own OT integration and security programme, which this scope deliberately does not import |

## A.2 Sources for This Appendix

- Mercatus. 2026. H200 server price. https://mercatus-ai.com/blog/h200-server-price
- Newegg. 2026. Supermicro SYS-421GE-TNRT-02-G1. https://www.newegg.com/p/N82E16859152404
