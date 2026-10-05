# Appendix A · What Ownership Costs Over Three Years

*Version 2, 5 October 2026. Version 1 compared ownership with AWS's three-year EC2 Instance Savings Plan at the no upfront rates (27.34 and 13.02 dollars an hour) and printed "about two thirds"; the deepest three-year plan in the region, all upfront at 23.80 and 11.33, makes it about four fifths. Every other number is unchanged.*

The design runs on the operator's own hardware. This appendix prices that choice against the two ways an operator in the United States could otherwise get the same capability: renting the same accelerators from a cloud region, or buying a closed frontier model by the token. Every input is a public price, dated and cited. The arithmetic is shown so any reader can rerun it with a written quote. The operator in this design is an illustrative scenario, so the user count and the edge allowance below are assumptions, stated where they are used.

## A.1 The Answer

Owning the stack this design specifies costs about **722,000 US dollars over three years**, inside a range of 629,000 to 821,000. Renting the same capacity around the clock costs **0.99 million to 2.52 million dollars** over the same period. Against the cheapest three-year commitment listed (AWS, three-year EC2 Instance Savings Plan, all upfront), ownership is **about four fifths** the cost. Every rented option here can stay inside the United States, so for a US operator the case for ownership is cost, control and a site that keeps working when the link drops, not residency.

## A.2 What Owning Costs

| Line | Basis | Three-year cost (USD) |
|---|---|---|
| Frontier tier | One server of eight 141 GB HBM-class cards, 320,000 to 420,000 dollars, typical 370,000 (Mercatus 2026) | 320,000 to 420,000 |
| Site tier | One GPU server, priced at the upper bound of eight 48 GB L40S-class cards although the paper's forecaster and embedder fit on one card, 85,271 dollars (Newegg 2026) | 85,000 |
| Edge | An allowance of 16 fanless IP-rated edge nodes, one at each of the 14 yard blocks, one at the gate and one at the quay at 4,000 dollars each (Eurotech 2026) | 64,000 |
| Support | 8 to 12 percent of hardware value a year (Introl 2026) | 113,000 to 205,000 |
| Power | 11.5 kW average IT load at a power usage effectiveness of 1.6 (Uptime Institute 2025), 481,870 kWh at the US industrial average of 9.77 cents per kWh in July 2026 (EIA 2026) | 47,000 |
| **Total** | | **629,000 to 821,000, typical 722,000** |

The average load assumes the frontier server draws 7 kW of its 10.2 kW maximum (NVIDIA 2026), the site server 3.5 kW and each edge node 60 W. The frontier tier fits one node because GLM 5.3 is 753 GB at FP8 and needs 904 GB with headroom, against 1,128 GB on eight 141 GB cards.

## A.3 What Renting Costs

The same frontier server and site server, rented without a break for three years, because a terminal works three shifts and turn time is predicted around the clock. The edge nodes stay on site in every option and are included in each total.

| Option | Basis | Three-year cost (USD) |
|---|---|---|
| AWS, us-east-1, on demand | p5en.48xlarge at 63.296 dollars an hour, g6e.48xlarge at 30.13 (Vantage 2026) | 2.52 million |
| AWS, three-year EC2 Instance Savings Plan, all upfront | the deepest three-year plan in us-east-1: 23.80 dollars an hour for p5en.48xlarge, 11.33 for g6e.48xlarge (AWS 2026) | 0.99 million |
| Azure, three-year reservation | ND96isr H200 v5 at 1,109,592 dollars for three years in East US 2, about 42.22 an hour (Azure 2026); site tier as AWS | 1.52 million |
| Specialist GPU cloud, on demand | 50.44 dollars an hour for eight H200 cards, 18.00 for eight L40S (CoreWeave 2026) | 1.86 million |
| Oracle, three-year commitment | 40 dollars an hour for eight H200 cards (Economize 2026); site tier as AWS | 1.46 million |

Egress, storage and support plans are excluded, so every rented figure is a floor. Spot capacity is excluded because a service that must run through a storm or a shift cannot be evicted.

## A.4 What Closed Models Cost by the Token

A closed frontier model replaces the frontier tier rather than the whole stack, and it is priced by use. At 40 users (an assumed count across the eight roles the paper names, over three shifts), each running the equivalent of five agents at 2.4 billion tokens a year, with four input tokens to every output token and half the input served from cache, three years is 288 billion tokens.

| Model | List price per million tokens, input and output | Three-year cost (USD) |
|---|---|---|
| Claude Sonnet 5.5 | 2 and 10 (Anthropic 2026) | 0.83 million |
| Gemini 3.1 Pro | 2 and 12 (Google 2026) | 0.94 million |
| Claude Opus 5.5 | 4 and 20 (Anthropic 2026) | 1.66 million |
| GPT-5.5 | 5 and 30 (OpenAI 2026) | 2.36 million |

The cheapest closed model costs about 21,000 dollars per user over three years, so it matches the whole owned stack at about **35 users**. Below that, renting a closed model by the token is cheaper; above it, ownership is, and the gap widens linearly with users while the owned cost stays flat. Every closed option also sends terminal transactions and camera footage of longshore labour to a third-party AI service outside the boundary, which the design's constraints rule out.

## A.5 What the Price Does Not Include

- **Cameras and installation**; the design reuses the existing camera estate.
- **The site tier is priced high on purpose.** The paper allows one H100-class or L40S-class node, and its two site models fit on one card, so a written quote will come in lower.
- **Sales tax, freight and installation** on the hardware, which a written quote settles.
- **An export licence** does not apply: the hardware stays inside the United States.
- **People, facilities and implementation**, which both sides carry.
- **Price movement.** Cloud prices rose as well as fell in 2026; AWS raised its H200 capacity block price about 15 percent in January (Gigazine 2026).

## A.6 Sources for This Appendix

- AWS. 2026. Compute and EC2 Instance Savings Plans price file, us-east-1, 3 October 2026. https://pricing.us-east-1.amazonaws.com/savingsPlan/v1.0/aws/AWSComputeSavingsPlan/current/region_index.json
- Anthropic. 2026. Pricing. https://claude.com/pricing
- Azure. 2026. Retail prices, Standard_ND96isr_H200_v5. https://prices.azure.com/api/retail/prices
- CoreWeave. 2026. Pricing. https://www.coreweave.com/pricing
- EIA. 2026. Electric Power Monthly, Table 5.6.A, July 2026. https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_6_a
- Economize. 2026. OCI BM.GPU.H200.8 pricing. https://www.economize.cloud
- Eurotech. 2026. ReliaCOR 33-11. https://buy.eurotech.com/products/reliacor-33-11
- Gigazine. 2026. AWS raises EC2 Capacity Blocks prices. https://gigazine.net
- Google. 2026. Gemini API pricing. https://ai.google.dev/gemini-api/docs/pricing
- Introl. 2026. GPU infrastructure TCO model. https://introl.com/blog/gpu-infrastructure-tco-model-5-year-enterprise-ai-deployment
- Mercatus. 2026. H200 server price. https://mercatus-ai.com/blog/h200-server-price
- NVIDIA. 2026. DGX H200. https://www.nvidia.com/en-us/data-center/dgx-h200/
- Newegg. 2026. Supermicro SYS-421GE-TNRT-02-G1. https://www.newegg.com/p/N82E16859152404
- OpenAI. 2026. API pricing. https://developers.openai.com/api/docs/pricing
- Uptime Institute. 2025. Global Data Center Survey 2025. https://uptimeinstitute.com
- Vantage. 2026. EC2 instance prices. https://instances.vantage.sh
