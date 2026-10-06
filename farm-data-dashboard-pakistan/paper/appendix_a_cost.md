# Appendix A · What It Costs

The design buys no hardware and serves no model. The dashboard, its PostgreSQL and PostGIS database and the adapters run on servers, storage and connectivity the operator provides, the sensors already in the field generate the data, and the analytics are deterministic aggregations, drill-down and reporting, so there is no owned-versus-rented comparison to print. The cost of this design is the integration and software work itself, delivered against the requirement's milestones and handed over with its source code and intellectual property.

## A.1 What Would Change the Answer

| Line | When it appears | How to price it |
|---|---|---|
| Database and buffer capacity | If measured sensor volumes in the phase one prototype outgrow the operator's servers | The server specification recorded at the Milestone 1 kick-off, re-estimated on measured volumes; the operator's own hardware cost per core and per terabyte |
| A forecaster over sensor time series | If the operator later commits a forecasting workload | A small open-weight time series model on CPU or one 48 GB card; one L40S-class card lists at 7,709 dollars (esaitech 2026), and Pakistan needs a US export licence for that class |
| A generative work surface | If staff later ask questions of the farm model in natural language | A frontier open-weight model on one node of eight 141 GB HBM-class GPUs, 320,000 to 420,000 dollars (Mercatus 2026), priced in the series' other papers |

## A.2 Sources for This Appendix

- esaitech. 2026. PNY NVIDIA L40S 48 GB GDDR6 PCIe. https://esaitech.com/products/pny-technologies-nvl40stcgpu-kit-nvidia-l40s-4-port-48gb-gddr6-graphic-card
- Mercatus. 2026. H200 server price. https://mercatus-ai.com/blog/h200-server-price
