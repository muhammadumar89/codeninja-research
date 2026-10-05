# Appendix A · What Ownership Costs Over Three Years

The design runs its reasoning tier on one GPU node in the operator's own data center. This appendix prices that node against the two ways a utility in the United States could otherwise get the same capability: renting the same accelerators from a cloud region, or buying a closed frontier model by the token. Every input is a public price, dated and cited, and the arithmetic is shown so any reader can rerun it with a written quote. The user count below is an assumption, stated where it is used.

## A.1 The Answer

Owning the reasoning node costs about **510,000 US dollars over three years**, inside a range of 426,000 to 600,000. Renting the same capacity around the clock costs **0.63 million to 1.66 million dollars** over the same period. Against the deepest three-year commitment listed (AWS, three-year EC2 Instance Savings Plan, all upfront), ownership is **about four fifths** the cost. Every rented option can stay inside the United States, so for a US utility the case for ownership is cost, control and a reasoning tier that sits inside the operator's own boundary, not residency.

## A.2 What Owning Costs

| Line | Basis | Three-year cost (USD) |
|---|---|---|
| Frontier tier | One server of eight 141 GB HBM-class cards, 320,000 to 420,000 dollars, typical 370,000 (Mercatus 2026) | 320,000 to 420,000 |
| Support | 8 to 12 percent of hardware value a year (Introl 2026) | 77,000 to 151,000 |
| Power | 7 kW average draw of the server's 10.2 kW maximum (NVIDIA 2026) at a power usage effectiveness of 1.6 (Uptime Institute 2025), 294,336 kWh at the US industrial average of 9.77 cents per kWh in July 2026 (EIA 2026) | 29,000 |
| **Total** | | **426,000 to 600,000, typical 510,000** |

The node is one server because GLM 5.2 is 753 GB at FP8 and needs 904 GB with the 1.2 planning factor, against 1,128 GB on eight 141 GB cards (Table 4).

## A.3 What Renting Costs

The same server, rented without a break for three years, because alerts arrive at night and an audit does not wait for business hours.

| Option | Basis | Three-year cost (USD) |
|---|---|---|
| AWS, us-east-1, on demand | p5en.48xlarge at 63.296 dollars an hour (Vantage 2026) | 1.66 million |
| AWS, three-year EC2 Instance Savings Plan, all upfront | p5en.48xlarge at 23.80 dollars an hour, the deepest three-year plan in the region (AWS 2026) | 0.63 million |
| Azure, three-year reservation | ND96isr H200 v5 at 1,109,592 dollars for three years in East US 2 (Azure 2026) | 1.11 million |
| Specialist GPU cloud, on demand | 50.44 dollars an hour for eight H200 cards (CoreWeave 2026) | 1.33 million |
| Oracle, three-year commitment | 40 dollars an hour for eight H200 cards (Economize 2026) | 1.05 million |

Egress, storage and support plans are excluded, so every rented figure is a floor. Spot capacity is excluded because a triage service that can be evicted mid-incident is not a security control.

## A.4 What Closed Models Cost by the Token

A closed frontier model replaces the reasoning tier, and it is priced by use. At 25 users (an assumed count across the OT security analysts, compliance staff and incident responders the paper names), each running the equivalent of five agents at 2.4 billion tokens a year, with four input tokens to every output token and half the input served from cache, three years is 180 billion tokens.

| Model | List price per million tokens, input and output | Three-year cost (USD) |
|---|---|---|
| Claude Sonnet 5.5 | 2 and 10 (Anthropic 2026) | 0.52 million |
| Gemini 3.1 Pro | 2 and 12 (Google 2026) | 0.59 million |
| Claude Opus 5.5 | 4 and 20 (Anthropic 2026) | 1.04 million |
| GPT-5.5 | 5 and 30 (OpenAI 2026) | 1.48 million |

The cheapest closed model costs about 21,000 dollars per user over three years, so it matches the owned node at about **25 users**. Below that a closed model by the token is cheaper; above it ownership is, and the gap widens with every user while the owned cost stays flat. Every closed option also sends network telemetry, alert context and compliance evidence about the bulk electric system to a third-party AI service outside the operator's boundary, which the design's constraints rule out.

## A.5 What the Price Does Not Include

- **The procured monitoring platform**: its sensors, collectors, licences and support are bought under the operator's own procurement and are carried the same in every option.
- **Site hardware the design specifies**: fanless collector servers, NEMA cabinets with UPS, GNSS time cards, industrial switches and data diodes at the highest-impact perimeters. Their count follows the operator's substation topology, which a site survey settles; every option carries them.
- **Sales tax, freight and installation**, which a written quote settles.
- **An export licence** does not apply: the hardware stays inside the United States.
- **People, facilities and implementation**, which both sides carry.
- **Price movement.** Cloud prices rose as well as fell in 2026; AWS raised its H200 capacity block price about 15 percent in January (Gigazine 2026).

## A.6 Sources for This Appendix

- AWS. 2026. Compute and EC2 Instance Savings Plans price file, us-east-1, version 20261003071546. https://pricing.us-east-1.amazonaws.com/savingsPlan/v1.0/aws/AWSComputeSavingsPlan/current/region_index.json
- Anthropic. 2026. Pricing. https://claude.com/pricing
- Azure. 2026. Retail prices, Standard_ND96isr_H200_v5. https://prices.azure.com/api/retail/prices
- CoreWeave. 2026. Pricing. https://www.coreweave.com/pricing
- EIA. 2026. Electric Power Monthly, Table 5.6.A, July 2026. https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_6_a
- Economize. 2026. OCI BM.GPU.H200.8 pricing. https://www.economize.cloud
- Gigazine. 2026. AWS raises EC2 Capacity Blocks prices. https://gigazine.net
- Google. 2026. Gemini API pricing. https://ai.google.dev/gemini-api/docs/pricing
- Introl. 2026. GPU infrastructure TCO model. https://introl.com/blog/gpu-infrastructure-tco-model-5-year-enterprise-ai-deployment
- Mercatus. 2026. H200 server price. https://mercatus-ai.com/blog/h200-server-price
- NVIDIA. 2026. DGX H200. https://www.nvidia.com/en-us/data-center/dgx-h200/
- OpenAI. 2026. API pricing. https://developers.openai.com/api/docs/pricing
- Uptime Institute. 2025. Global Data Center Survey 2025. https://uptimeinstitute.com
- Vantage. 2026. EC2 instance prices. https://instances.vantage.sh
