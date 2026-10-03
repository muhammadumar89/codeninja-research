# Appendix A · What Ownership Costs Over Three Years

The design runs on the operator's own hardware. This appendix prices that choice against the two ways an operator in Saudi Arabia could otherwise get the same capability: renting the same accelerators from a cloud region, or buying a closed frontier model by the token. Every input is a public price, dated and cited. The arithmetic is shown so any reader can rerun it with a written quote. The operator in this design is an illustrative scenario, so the user count and the edge allowance below are assumptions, stated where they are used.

## A.1 The Answer

Owning the stack this design specifies costs about **642,000 US dollars over three years**, inside a range of 552,000 to 739,000. Renting the same capacity around the clock costs **1.41 million to 2.81 million dollars** over the same period. Against the cheapest three-year commitment listed (Oracle, three-year commitment), ownership is **about one half** the cost. Only one of the rented options can sit inside the Kingdom today: no hyperscaler GPU region with H200-class machines is live there, and AWS's Saudi region opens in December 2026 (Channel Insider 2026).

## A.2 What Owning Costs

| Line | Basis | Three-year cost (USD) |
|---|---|---|
| Frontier tier | One server of eight 141 GB HBM-class cards, 320,000 to 420,000 dollars, typical 370,000 (Mercatus 2026) | 320,000 to 420,000 |
| Site tier | One PCIe inference server of eight 48 GB L40S-class cards, as the paper specifies, 85,271 dollars (Newegg 2026) | 85,000 |
| Edge | Five Jetson Orin industrial edge nodes in solar powered enclosures, one at each camera location the paper names at 4,000 dollars each (Eurotech 2026) | 20,000 |
| Support | 8 to 12 percent of hardware value a year (Introl 2026) | 102,000 to 189,000 |
| Power | 10.8 kW average IT load at a power usage effectiveness of 1.6 (Uptime Institute 2025), 454,118 kWh at the industrial tariff of 0.20 riyals per kWh (ECRA 2025) at 3.75 riyals to the dollar | 24,000 |
| **Total** | | **552,000 to 739,000, typical 642,000** |

The average load assumes the frontier server draws 7 kW of its 10.2 kW maximum (NVIDIA 2026), the site server 3.5 kW and each edge node 60 W. The frontier tier fits one node because GLM 5.3 is 753 GB at FP8 and needs 904 GB with headroom, against 1,128 GB on eight 141 GB cards.

## A.3 What Renting Costs

The same frontier server and site server, rented without a break for three years, because breach detection runs while crews work and forecasts refresh through the night. The edge nodes stay on site in every option and are included in each total.

| Option | Basis | Three-year cost (USD) |
|---|---|---|
| AWS, UAE region, on demand | p5en.48xlarge at 75.96 dollars an hour in me-central-1, g6e.48xlarge at 30.13 (Vantage 2026); outside the Kingdom | 2.81 million |
| Specialist GPU cloud, on demand | 50.44 dollars an hour for eight H200 cards, 18.00 for eight L40S (CoreWeave 2026); outside the Kingdom | 1.82 million |
| Oracle, three-year commitment | 40 dollars an hour for eight H200 cards at Oracle's single global price (Oracle 2026), listed for Riyadh and Jeddah by a third party (Northflank 2026); site tier at AWS reserved 13.02 | 1.41 million |

Egress, storage and the network link to the region are excluded, so every rented figure is a floor.

## A.4 What Closed Models Cost by the Token

A closed frontier model replaces the frontier tier rather than the whole stack, and it is priced by use. At 30 users (an assumed count across the planning, crane coordination and HSE leads the paper writes for), each running the equivalent of five agents at 2.4 billion tokens a year, with four input tokens to every output token and half the input served from cache, three years is 216 billion tokens.

| Model | List price per million tokens, input and output | Three-year cost (USD) |
|---|---|---|
| Claude Sonnet 5.5 | 2 and 10 (Anthropic 2026) | 0.62 million |
| Gemini 3.1 Pro | 2 and 12 (Google 2026) | 0.71 million |
| Claude Opus 5.5 | 4 and 20 (Anthropic 2026) | 1.24 million |
| GPT-5.5 | 5 and 30 (OpenAI 2026) | 1.77 million |

The cheapest closed model costs about 21,000 dollars per user over three years, so it matches the whole owned stack at about **31 users**. Below that, renting a closed model by the token is cheaper; above it, ownership is, and the gap widens linearly with users while the owned cost stays flat. Every closed option also sends worker biometric data, site footage and the owner's schedule to a third-party AI service outside the boundary, which the design's constraints rule out.

## A.5 What the Price Does Not Include

- **Solar enclosures, batteries, sunshields and private LTE**; the edge line prices the compute only.
- **The project's own data room and its fit-out**, which the joint venture already runs.
- **An export licence.** Saudi Arabia sits in US Country Groups D:3 and D:4 (eCFR 2026), so 141 GB HBM-class accelerators need a licence from the Bureau of Industry and Security, granted case by case; BIS guidance of May 2026 confirms no blanket exemption (Holland & Knight 2026).
- **Customs duty and 15 percent VAT** on the hardware, which a written quote delivered to the Kingdom settles.
- **People, facilities and implementation**, which both sides carry.

## A.6 Sources for This Appendix

- Anthropic. 2026. Pricing. https://claude.com/pricing
- Channel Insider. 2026. AWS cloud region launch, Saudi Arabia. https://www.channelinsider.com/infrastructure/news-aws-cloud-region-launch-emea-saudi-arabia/
- CoreWeave. 2026. Pricing. https://www.coreweave.com/pricing
- ECRA. 2025. Electricity tariff, effective 28 May 2025, as reported. https://clenergize.com/ksa-electricity-tariff-changes-in-2025-is-your-business-ready/
- Eurotech. 2026. ReliaCOR 33-11. https://buy.eurotech.com/products/reliacor-33-11
- Google. 2026. Gemini API pricing. https://ai.google.dev/gemini-api/docs/pricing
- Holland & Knight. 2026. BIS guidance on licence requirements for advanced computing items. https://www.hklaw.com/en/insights/publications/2026/06/bis-publishes-guidance-license-requirements-advanced-computing-items
- Introl. 2026. GPU infrastructure TCO model. https://introl.com/blog/gpu-infrastructure-tco-model-5-year-enterprise-ai-deployment
- Mercatus. 2026. H200 server price. https://mercatus-ai.com/blog/h200-server-price
- NVIDIA. 2026. DGX H200. https://www.nvidia.com/en-us/data-center/dgx-h200/
- Newegg. 2026. Supermicro SYS-421GE-TNRT-02-G1. https://www.newegg.com/p/N82E16859152404
- Northflank. 2026. OCI BM.GPU.H200.8 regions. https://northflank.com/cloud/oci/instances/BM.GPU.H200.8
- OpenAI. 2026. API pricing. https://developers.openai.com/api/docs/pricing
- Oracle. 2026. Cloud pricing. https://www.oracle.com/cloud/pricing/
- Uptime Institute. 2025. Global Data Center Survey 2025. https://uptimeinstitute.com
- Vantage. 2026. EC2 instance prices. https://instances.vantage.sh
- eCFR. 2026. 15 CFR Part 740, Supplement No. 1, Country Groups. https://www.ecfr.gov/current/title-15/part-740/appendix-Supplement%20No.%201%20to%20Part%20740
