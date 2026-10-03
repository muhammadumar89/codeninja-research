# Appendix A · What Ownership Costs Over Three Years

The design runs on the operator's own hardware. This appendix prices that choice against the two ways an operator in the United States could otherwise get the same capability: renting the same accelerators from a cloud region, or buying a closed frontier model by the token. Every input is a public price, dated and cited. The arithmetic is shown so any reader can rerun it with a written quote. The operator in this design is an illustrative scenario, so the user count and the edge allowance below are assumptions, stated where they are used.

## A.1 The Answer

Owning the stack this design specifies costs about **841,000 US dollars over three years**, inside a range of 741,000 to 946,000. Renting the same capacity around the clock costs **0.97 million to 1.92 million dollars** over the same period. Against the cheapest three-year commitment listed (AWS, three-year EC2 Instance Savings Plan), ownership is **about four fifths** the cost. Every rented option here can stay inside the United States, so for a US operator the case for ownership is cost, control and a site that keeps working when the link drops, not residency.

## A.2 What Owning Costs

| Line | Basis | Three-year cost (USD) |
|---|---|---|
| Frontier tier | One server of eight 141 GB HBM-class cards, 320,000 to 420,000 dollars, typical 370,000 (Mercatus 2026) | 320,000 to 420,000 |
| Edge | An allowance of 63 fanless industrial edge nodes, one at each of the paper's more than 40 substations, one on each of its about 20 patrol trucks and one at the yard at 4,000 dollars each (Eurotech 2026) | 252,000 |
| Support | 8 to 12 percent of hardware value a year (Introl 2026) | 137,000 to 242,000 |
| Power | 10.8 kW average IT load at a power usage effectiveness of 1.6 (Uptime Institute 2025), 453,277 kWh at the Texas industrial average of 7.07 cents per kWh in July 2026 (EIA 2026) | 32,000 |
| **Total** | | **741,000 to 946,000, typical 841,000** |

The average load assumes the frontier server draws 7 kW of its 10.2 kW maximum (NVIDIA 2026) and each edge node 60 W. The frontier tier fits one node because GLM 5.2 is 753 GB at FP8 and needs 904 GB with headroom, against 1,128 GB on eight 141 GB cards.

## A.3 What Renting Costs

The same frontier server, rented without a break for three years, because wildfire risk does not stop at night and a storm is when the picture matters most. The edge nodes stay on site in every option and are included in each total.

| Option | Basis | Three-year cost (USD) |
|---|---|---|
| AWS, us-east-1, on demand | p5en.48xlarge at 63.296 dollars an hour (Vantage 2026) | 1.92 million |
| AWS, three-year EC2 Instance Savings Plan | p5en.48xlarge at 27.34 dollars an hour, no upfront (AWS 2026) | 0.97 million |
| Azure, three-year reservation | ND96isr H200 v5 at 1,109,592 dollars for three years in East US 2, about 42.22 an hour (Azure 2026) | 1.36 million |
| Specialist GPU cloud, on demand | 50.44 dollars an hour for eight H200 cards (CoreWeave 2026) | 1.58 million |
| Oracle, three-year commitment | 40 dollars an hour for eight H200 cards (Economize 2026) | 1.30 million |

Egress, storage and support plans are excluded, so every rented figure is a floor. Spot capacity is excluded because a service that must run through a storm or a shift cannot be evicted.

## A.4 What Closed Models Cost by the Token

A closed frontier model replaces the frontier tier rather than the whole stack, and it is priced by use. At 30 users (an assumed count across the dispatchers, distribution engineers and vegetation coordinators the paper names), each running the equivalent of five agents at 2.4 billion tokens a year, with four input tokens to every output token and half the input served from cache, three years is 216 billion tokens.

| Model | List price per million tokens, input and output | Three-year cost (USD) |
|---|---|---|
| Claude Sonnet 5.5 | 2 and 10 (Anthropic 2026) | 0.62 million |
| Gemini 3.1 Pro | 2 and 12 (Google 2026) | 0.71 million |
| Claude Opus 5.5 | 4 and 20 (Anthropic 2026) | 1.24 million |
| GPT-5.5 | 5 and 30 (OpenAI 2026) | 1.77 million |

The cheapest closed model costs about 21,000 dollars per user over three years, so it matches the whole owned stack at about **41 users**. Below that, renting a closed model by the token is cheaper; above it, ownership is, and the gap widens linearly with users while the owned cost stays flat. Every closed option also sends grid telemetry, member meter data and de-energisation decisions to a third-party AI service outside the boundary, which the design's constraints rule out.

## A.5 What the Price Does Not Include

- **Cameras, enclosures and installation** at substations and on trucks; the edge line prices the compute only.
- **The edge count.** It is the largest cost line this design controls: 63 nodes is one per place the paper puts a box, and a bench measurement on the real camera streams may let several sites share one node.
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
- OpenAI. 2026. API pricing. https://developers.openai.com/api/docs/pricing
- Uptime Institute. 2025. Global Data Center Survey 2025. https://uptimeinstitute.com
- Vantage. 2026. EC2 instance prices. https://instances.vantage.sh
