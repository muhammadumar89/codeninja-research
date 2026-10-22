# Appendix A · What the Control Center Node Costs Over Three Years

The design runs on the operator's own hardware, in the gas control centers and the station cabinets, with nothing in a third party cloud (chapter 3 and Table 4). Its reasoning model, Mistral Large 3 675B (Instruct), runs at FP8 on a single node of eight 141 GB HBM-class GPUs with vLLM, and BGE-M3 runs beside it on the same node (chapter 7, section 7.1; Table 4, "one control-center node"). This appendix prices that node two ways: owned, from a published server list price with support and power added, and rented, from the AWS price files for the US East region, as the cloud equivalent. Every input is dated and cited, and the arithmetic is shown. The station edge modules are specified as a class (volume production modules in 7W to 60W envelopes, Table 4) rather than a part number and are sold by quotation, so they are named and left out of the total rather than guessed.

## A.1 The Answer

Owning the node for three years costs **about 465,000 US dollars**, inside a range of 432,000 to 485,000. Renting the same eight cards around the clock costs **about 625,000 dollars** on the deepest three-year commitment (an AWS EC2 Instance Savings Plan, all upfront, US East) and **about 1.66 million dollars** on demand. Ownership costs **about three quarters** of the deepest commitment (465,000 / 625,000 = 0.74, and 0.69 to 0.78 across the range), and the commitment costs **about three eighths** of on demand (625,000 / 1,663,000 = 0.38). All four models are open weights, Mistral Large 3 675B, Chronos-2 and the RF-DETR sizes the design uses under Apache-2.0 and BGE-M3 under MIT (chapter 8), and carry no licence line.

## A.2 What the Node Would Cost

| Option | Basis | Three-year cost (USD) |
|---|---|---|
| Owned, in the control center | One server of eight H200 cards of 141 GB, with support and power, broken out below | 432,000 to 485,000, typical 465,000 |
| AWS, US East, on demand | p5en.48xlarge, eight H200 cards of 141 GB, at 63.296 dollars an hour (Vantage 2026), 26,280 hours | 1,663,000 |
| AWS, US East, three-year Compute Savings Plan, all upfront | p5en.48xlarge at 42.21683 dollars an hour (AWS 2026), 26,280 hours | 1,109,000 |
| AWS, US East, three-year EC2 Instance Savings Plan, all upfront | p5en.48xlarge at 23.7993 dollars an hour, the deepest three-year plan in the region (AWS 2026), 26,280 hours | 625,000 |

The owned line, item by item:

| Line | Basis | Three-year cost (USD) |
|---|---|---|
| Server | Exxact TensorEX 5U HGX H200 server, eight H200 SXM5 cards of 141 GB, published starting price of 325,039 dollars (Exxact 2026) | 325,000 |
| Support | 8 to 12 percent of hardware value a year (Introl 2026), 10 percent typical, over three years | 78,000 to 117,000, typical 98,000 |
| Power | 7 kW assumed average draw against the 10.2 kW maximum of an eight card H200 system (NVIDIA 2026), 7 x 26,280 = 183,960 kWh, times a power usage effectiveness of 1.6 (above the 1.54 industry average, Uptime Institute 2025) = 294,336 kWh, at the US average of 9.77 cents per kWh industrial or 14.53 cents commercial, July 2026 (EIA 2026) | 29,000 to 43,000 |
| **Total** | Low: 8 percent support, industrial tariff. High: 12 percent, commercial. Typical: 10 percent, commercial | **432,000 to 485,000, typical 465,000** |

Why eight cards of 141 GB: the paper sizes the model at about 682 GB of weights at FP8 (chapter 7, section 7.1; chapter 8, section 8.1), which fits on eight 141 GB cards (1,128 GB) with about 446 GB left for the KV cache and serving overhead, and does not fit on fewer. AWS p5en.48xlarge is the US East instance with exactly that card class; p5.48xlarge carries eight 80 GB cards and fits only the NVFP4 build the paper mentions as an alternative, not the FP8 build it chooses, so it is not priced.

Not in the table: the station edge modules (more than a dozen compressor stations, chapter 1, one module class per cabinet, Table 4), the hazardous area enclosures, the station cameras, the data diodes, the passive OT network taps at every station and both control centers, the methane point sensors, vibration sensors, discharge temperature probes and PTP grandmaster clocks (Table 4, Sensing), and site networking; the paper names all of these as classes, not part numbers, and records the station inference server, camera, enclosure and frontier cluster classes as open decisions (chapter 9, section 9.5), so each is sold by quotation. Also out: the control center cluster for Kafka, Harbor and observability, which the paper does not size; sales tax, freight, installation and any configuration above the server's starting price, which a written quote settles; and people and facilities, which every option carries. Every rented figure is a floor, because egress, storage and support plans are excluded, and the all upfront plan is paid in full on day one.

## A.3 Sources for This Appendix

- AWS. 2026. EC2 Instance and Compute Savings Plans price file, us-east-1, version 20261021225300, as read 22 October 2026. https://pricing.us-east-1.amazonaws.com/savingsPlan/v1.0/aws/AWSComputeSavingsPlan/current/region_index.json
- EIA. 2026. Electric Power Monthly, Table 5.6.A, Average Price of Electricity to Ultimate Customers by End-Use Sector, July 2026, as read 22 October 2026. https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_6_a
- Exxact. 2026. TensorEX 5U HGX H200 Server, TS4-181733724, as read 22 October 2026. https://www.exxactcorp.com/Exxact-TS4-181733724-E181733724
- Introl. 2026. GPU infrastructure TCO model, as read 22 October 2026. https://introl.com/blog/gpu-infrastructure-tco-model-5-year-enterprise-ai-deployment
- NVIDIA. 2026. NVIDIA DGX H100/H200 User Guide, Power Specifications, as read 22 October 2026. https://docs.nvidia.com/dgx/dgxh100-user-guide/introduction-to-dgxh100.html
- Uptime Institute. 2025. Global Data Center Survey 2025, as read 22 October 2026. https://intelligence.uptimeinstitute.com/resource/uptime-institute-global-data-center-survey-2025
- Vantage. 2026. p5en.48xlarge pricing, US East (N. Virginia), Linux on demand, as read 22 October 2026. https://instances.vantage.sh/aws/ec2/p5en.48xlarge
