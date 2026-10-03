# Appendix A · What Ownership Costs Over Three Years

*Version 2, 3 October 2026. Version 1 compared ownership with AWS's Compute Savings Plan (26 percent off) and printed "about one third"; AWS's deepest three-year plan makes it about three fifths. Every other number is unchanged.*

The design runs on the operator's own hardware. This appendix prices that choice against the two ways an operator in Pakistan could otherwise get the same capability: renting the same accelerators from the nearest hyperscaler region, or buying a closed frontier model by the token. Every input is a public price, dated and cited. The arithmetic is shown so any reader can rerun it with a written quote.

## A.1 The Answer

Owning the stack this design specifies costs about **670,000 US dollars over three years**, inside a range of 580,000 to 770,000. Renting the same capacity around the clock from the nearest hyperscaler region costs **1.1 to 2.8 million dollars** over the same period. Ownership is therefore between about one quarter and three fifths of the cost of renting, and **about three fifths** against the deepest three-year commitment, an AWS EC2 Instance Savings Plan paid up front. None of the rented options keeps the data in Pakistan, because no hyperscaler operates a region inside the country (Alskyline 2026).

## A.2 What Owning Costs

Table A1 prices the hardware the design names and three years of running it.

| Line | Basis | Three-year cost (USD) |
|---|---|---|
| Frontier tier | One server of eight 141 GB HBM-class cards, 320,000 to 420,000 dollars, typical 370,000 (Mercatus 2026) | 320,000 to 420,000 |
| Site tier | One PCIe inference server, priced at the upper bound of eight 48 GB cards, 85,271 dollars (Newegg 2026); its three models weigh under 4 GB | 85,271 |
| Edge | An allowance of six fanless industrial nodes at 4,000 dollars each (Eurotech 2026); the design reuses the operator's NPU compute where it exists | 24,000 |
| Support | 8 to 12 percent of hardware value a year (Introl 2026) | 103,000 to 191,000 |
| Power | 10.9 kW average IT load at a power usage effectiveness of 1.6 (Uptime Institute 2025), 456,641 kWh at the industrial B3 average of 27 rupees per kWh plus the fixed kW charge (Dawn 2026), at 277.38 rupees to the dollar (SBP 2026) | 47,269 |
| **Total** | | **580,000 to 767,000, typical 670,000** |

The average load assumes the frontier server draws 7 kW of its 10.2 kW maximum (NVIDIA 2026), the site server 3.5 kW and each edge node 60 W. The frontier tier fits one node because the design's reasoning model, GLM 5.3, is 753 GB at FP8 and needs 904 GB with headroom, against 1,128 GB on eight 141 GB cards.

## A.3 What Renting Costs

The same frontier server and site server, rented without a break for three years, because HSE monitoring does not stop at night. The edge nodes stay on site in every option.

| Option | Basis | Three-year cost (USD) |
|---|---|---|
| AWS, UAE region, on demand | p5en.48xlarge at 75.96 dollars an hour in me-central-1, g6e.48xlarge at 30.13 (Vantage 2026) | 2.82 million |
| AWS, three-year EC2 Instance Savings Plan | all upfront in me-central-1: 28.56 dollars an hour for p5en.48xlarge, 13.90 for g6e.48xlarge (AWS 2026) | 1.14 million |
| Specialist GPU cloud, on demand | 50.44 dollars an hour for eight H200 cards, 18.00 for eight L40S (CoreWeave 2026) | 1.83 million |
| Oracle, three-year commitment | 40 dollars an hour for eight H200 cards (Economize 2026), site tier as AWS reserved | 1.42 million |

Egress, storage, and the network link from Pakistan to the region are excluded, so every rented figure is a floor.

## A.4 What Closed Models Cost by the Token

A closed frontier model replaces the frontier tier rather than the whole stack, and it is priced by use. At 50 HSE users, each running the equivalent of five agents at 2.4 billion tokens a year, with four input tokens to every output token and half the input served from cache, three years is 360 billion tokens.

| Model | List price per million tokens, input and output | Three-year cost (USD) |
|---|---|---|
| Claude Sonnet 5.5 | 2 and 10 (Anthropic 2026) | 1.04 million |
| Gemini 3.1 Pro | 2 and 12 (Google 2026) | 1.18 million |
| Claude Opus 5.5 | 4 and 20 (Anthropic 2026) | 2.07 million |
| GPT-5.5 | 5 and 30 (OpenAI 2026) | 2.95 million |

At this volume even the cheapest closed model costs about one and a half times the whole owned stack, and the largest cost three to four and a half times as much. Token volume is the assumption that moves this comparison most: it scales linearly with users, and ownership does not. Every one of these options also sends HSE records, which carry personal data and investigation findings, to a third-party AI service outside the boundary, which the design's first constraint rules out.

## A.5 What the Price Does Not Include

- **Import duty, sales tax, freight and insurance** on the hardware, which a written quote delivered to Pakistan settles.
- **An export license.** Pakistan sits in US Country Group D:4, so 141 GB HBM-class accelerators need a license from the Bureau of Industry and Security (eCFR 2026). Approved channels have delivered more than 3,000 accelerators to a Pakistani operator (The News 2026). The design's Phase 0 checkpoint confirms the operator's actual inventory before anything is bought, and holds a downgrade path to a mid-size model on accelerators already installed.
- **People, facilities and implementation**, which both sides carry.
- **Price movement.** Cloud prices rose as well as fell in 2026; AWS raised its H200 capacity block price about 15 percent in January (Gigazine 2026).

## A.6 Sources for This Appendix

- Alskyline. 2026. Cloud regions in Saudi Arabia, 2026 guide. https://alskyline.com/kb/cloud-regions-saudi-arabia-2026-guide
- Anthropic. 2026. Pricing. https://claude.com/pricing
- AWS. 2026. Compute and EC2 Instance Savings Plans price file, me-central-1, 3 October 2026. https://pricing.us-east-1.amazonaws.com/savingsPlan/v1.0/aws/AWSComputeSavingsPlan/current/region_index.json
- CoreWeave. 2026. Pricing. https://www.coreweave.com/pricing
- Dawn. 2026. NEPRA notifies new industrial tariffs. https://www.dawn.com/news/1973828
- eCFR. 2026. 15 CFR Part 740, Supplement No. 1, Country Groups. https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-740
- Economize. 2026. OCI BM.GPU.H200.8 pricing. https://www.economize.cloud
- Eurotech. 2026. ReliaCOR 33-11. https://buy.eurotech.com/products/reliacor-33-11
- Gigazine. 2026. AWS raises EC2 Capacity Blocks prices. https://gigazine.net
- Google. 2026. Gemini API pricing. https://ai.google.dev/gemini-api/docs/pricing
- Introl. 2026. GPU infrastructure TCO model. https://introl.com/blog/gpu-infrastructure-tco-model-5-year-enterprise-ai-deployment
- Mercatus. 2026. H200 server price. https://mercatus-ai.com/blog/h200-server-price
- Newegg. 2026. Supermicro SYS-421GE-TNRT-02-G1. https://www.newegg.com/p/N82E16859152404
- NVIDIA. 2026. DGX H200. https://www.nvidia.com/en-us/data-center/dgx-h200/
- OpenAI. 2026. API pricing. https://developers.openai.com/api/docs/pricing
- SBP. 2026. Conversion rates, 4 September 2026. https://www.sbp.org.pk
- The News. 2026. Data Vault Pakistan GPUs. https://www.thenews.com.pk
- Uptime Institute. 2025. Global Data Center Survey 2025. https://uptimeinstitute.com
- Vantage. 2026. EC2 instance prices. https://instances.vantage.sh
