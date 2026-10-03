# Appendix A · What It Costs

The design buys no hardware. The requirement asks for no cameras, sensors or servers, and the only model in the register, the BGE-M3 embedding model, occupies about 1.1 GB of weights at fp16, which fits a standard enterprise virtual machine the port already operates. There is therefore no owned-versus-rented comparison to print: the cost of this design is integration and software work on infrastructure the port already pays for, and a closed document AI service was set aside on boundary grounds, not price.

## A.1 What Would Change the Answer

| Line | When it appears | How to price it |
|---|---|---|
| Virtual machine capacity | If the twin's event backbone and GIS services outgrow the existing cluster | The port's own virtualisation cost per core and per gigabyte, which no public list price captures |
| Document retrieval at scale | If the drawing and inspection corpus grows into the millions of pages | Embedding throughput on CPU is the limit; one mid-range GPU card (48 GB class, about 85,000 dollars for a server of eight, Newegg 2026) removes it |
| A generative work surface | If the port later asks questions in natural language over the twin | A frontier open-weight model on one node of eight 141 GB HBM-class GPUs, 320,000 to 420,000 dollars (Mercatus 2026), priced in the series' other papers |

## A.2 Sources for This Appendix

- Mercatus. 2026. H200 server price. https://mercatus-ai.com/blog/h200-server-price
- Newegg. 2026. Supermicro SYS-421GE-TNRT-02-G1. https://www.newegg.com/p/N82E16859152404
