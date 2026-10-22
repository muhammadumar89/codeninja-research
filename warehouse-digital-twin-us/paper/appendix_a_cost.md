# Appendix A · What the Twin's Compute Costs Over Three Years

The requirement keeps data and models in the company's own environment, on open weights, with video processed at each of the four sites (chapter 3). The design places inference at three tiers (chapter 7). At each site, one industrial edge server carries one 48 GB PCIe inference card, which runs the RF-DETR and OC-SORT vision stack in Triton and the site model, Qwen3.8-27B at FP8, under vLLM on the same card (chapters 4 and 7). At the center, Mistral Large 3 675B runs on one node of the 141 GB HBM class with eight cards (chapter 7; Table 4 in chapter 8). That is five inference servers and twelve cards in all. This appendix prices them two ways: owned, as the design specifies, and rented from the AWS price files for the US East region as a reference. Every price is dated and cited. The roughly 220 existing cameras are reused and are not priced. The rugged edge server chassis is specified as a class (a rugged rack server with PCIe inference accelerators, Table 4) and is sold by quotation, so it is named and left out of the total rather than guessed.

## A.1 The Answer

Owning the compute the design names costs **about 597,000 US dollars over three years**, inside a range of 510,000 to 689,000, before the four edge chassis. Renting the same cards around the clock costs **about 1.86 million dollars** on demand and **about 699,000 dollars** on the deepest three-year commitment, an AWS EC2 Instance Savings Plan, all upfront, US East. The commitment costs **about three eighths** of the on-demand price, and ownership costs **about one third** of it. Against the commitment, ownership lands between about three quarters of its price and roughly the same price, so the arithmetic does not support a larger saving there. All five models are open weights (Mistral Large 3 675B and Qwen3.8-27B under Apache-2.0, RF-DETR N to L under Apache-2.0, OC-SORT and BGE-M3 under MIT) and carry no licence line.

The arithmetic: 699,000 divided by 1,859,000 is 0.376, about three eighths. 597,000 divided by 1,859,000 is 0.32, about one third, with the range at 0.27 to 0.37. 510,000 to 689,000 divided by 699,000 is 0.73 to 0.99.

## A.2 What Owning Costs

| Line | Basis | Three-year cost (USD) |
|---|---|---|
| Central tier | One server of eight 141 GB HBM class cards, 320,000 to 420,000 dollars, typical 370,000 (Mercatus 2026) | 320,000 to 420,000 |
| Site tier | Four 48 GB PCIe inference cards, one per site, at 8,595 dollars each for the NVIDIA L40S (Newegg 2026) | 34,380 |
| Support | 8 to 12 percent of hardware value a year for three years (Introl 2026), typical 10 percent | 85,051 to 163,577 |
| Power | 11.6 kW of IT load at maximum draw, times a power usage effectiveness of 1.6, is 18.56 kW; over 26,280 hours that is 487,757 kWh at the US commercial average of 14.53 cents per kWh (EIA 2026) | 70,871 |
| **Total** | | **510,302 to 688,828, typical 596,565** |

The 11.6 kW is the central server at its stated maximum of about 10.2 kW (NVIDIA 2026) plus four cards at 350 W each (Newegg 2026), so the power line is a ceiling for the cards it covers. A power usage effectiveness of 1.6 sits slightly above the 1.54 global average the Uptime Institute reports (Uptime Institute 2025).

Why eight cards at the center: the published FP8 checkpoint of Mistral Large 3 675B is about 682 GB; eight 141 GB cards give 1,128 GB, about 1,038 GB usable at 0.92 utilisation, which leaves about 350 GB of KV ceiling for concurrent assistant sessions (chapter 7). Why one card per site: Qwen3.8-27B is about 31 GB at FP8 and BGE-M3 about 1.1 GB at FP16, which fit one 48 GB card with headroom for the KV cache beside the vision checkpoints of 61 to 68 MB each (chapters 7 and 8).

Not in the table: the four rugged edge server chassis, their PoE switches and UPS units (chapter 7), and the optional hardware one-way egress path (chapter 7), all sold by quotation; the purpose-placed fixed cameras the six-gate survey may add, whose count is still open (chapter 9); people, facilities, networking and implementation; and residual value at the end of three years.

## A.3 What Renting Would Cost

The same twelve cards rented without a break for three years, because the safety path runs every shift. Renting the site tier in a cloud region would break the rule that video is processed in each building (chapter 3), so these figures are a price reference, not an option the design can take.

| Option | Basis | Three-year cost (USD) |
|---|---|---|
| AWS, US East, on demand | p5en.48xlarge, eight H200 cards of 141 GB, at 63.296 dollars an hour, plus four g6e.xlarge, one L40S card of 48 GB each, at 1.861 dollars an hour (Vantage 2026), 26,280 hours | 1,859,000 |
| AWS, US East, three-year Compute Savings Plan, all upfront | p5en.48xlarge at 42.21683 and g6e.xlarge at 0.87541 dollars an hour (AWS 2026) | 1,201,000 |
| AWS, US East, three-year EC2 Instance Savings Plan, all upfront | p5en.48xlarge at 23.7993 and g6e.xlarge at 0.69974 dollars an hour, the deepest three-year plan in the region (AWS 2026) | 699,000 |

The central node is 1,663,000 dollars of the on-demand total, 1,109,000 of the Compute Savings Plan total and 625,000 of the EC2 Instance Savings Plan total; the four site instances are 196,000, 92,000 and 74,000. The g6e.xlarge is the smallest AWS instance carrying one 48 GB card, with 4 vCPUs and 32 GiB of memory, so the site figures are a floor: decoding about 55 camera substreams per site would likely need a larger host. Egress and storage are excluded.

## A.4 Sources for This Appendix

- AWS. 2026. EC2 Instance and Compute Savings Plans price file, us-east-1, version 20261021225300, as read 22 October 2026. https://pricing.us-east-1.amazonaws.com/savingsPlan/v1.0/aws/AWSComputeSavingsPlan/current/region_index.json and https://pricing.us-east-1.amazonaws.com/savingsPlan/v1.0/aws/AWSComputeSavingsPlan/20261021225300/us-east-1/index.json
- EIA. 2026. Electric Power Monthly, Table 5.6.A, average price of electricity to ultimate customers, commercial sector, US total, July 2026, as read 22 October 2026. https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_6_a
- Introl. 2026. GPU infrastructure TCO model, as read 22 October 2026. https://introl.com/blog/gpu-infrastructure-tco-model-5-year-enterprise-ai-deployment
- Mercatus. 2026. H200 server price, as read 22 October 2026. https://mercatus-ai.com/blog/h200-server-price
- Newegg. 2026. NVIDIA L40S, 48 GB GDDR6, PCIe 4.0 x16, part 900-2G133-0080-000, sold by Newegg, as read 22 October 2026. https://www.newegg.com/p/N82E16888892001
- NVIDIA. 2026. DGX H200 specifications, as read 22 October 2026. https://www.nvidia.com/en-us/data-center/dgx-h200/
- Uptime Institute. 2025. Global Data Center Survey 2025. https://intelligence.uptimeinstitute.com/resource/uptime-institute-global-data-center-survey-2025
- Vantage. 2026. p5en.48xlarge and g6e.xlarge pricing, US East (N. Virginia), Linux on demand, as read 22 October 2026. https://instances.vantage.sh/aws/ec2/p5en.48xlarge and https://instances.vantage.sh/aws/ec2/g6e.xlarge
