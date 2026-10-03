# Appendix A · What Ownership Costs Over Three Years

The design runs on hardware the authority owns: a counting kit at every installation point, and one frontier node in a dedicated data center where an export licence holds. This appendix prices that choice against renting the frontier node from a cloud region and against buying a closed frontier model by the token. Every input is a public price, dated and cited. The arithmetic is shown so any reader can rerun it with a written quote. The paper names the scale only in bands, hundreds of mills covered line by line, so the installation point count below is an assumption, stated where it is used.

## A.1 The Answer

Owning the stack this design specifies costs about **4,445,000 US dollars over three years** for 300 installation points, inside a range of 4,191,000 to 4,705,000. The counting kits are 2,832,000 of that and cannot be rented: cameras and industrial PCs sit at the mill in every option. The one line a cloud can replace is the frontier node, and owning it costs about **686,000 dollars** over three years against **0.75 million** on AWS's deepest three-year commitment, so ownership of the node is about the same as the cheapest rental. Renting that node also moves the counted record of every mill in the country outside Pakistan, which the design's first constraint rules out; no hyperscaler runs a region inside the country.

## A.2 What Owning Costs

| Line | Basis | Three-year cost (USD) |
|---|---|---|
| Counting kit, per installation point | Advantech MIC-733-AO5A1, a fanless Jetson AGX Orin 32 GB industrial PC (Advantech 2026), 4,646; two Basler ace 2 IP67 5 MP GigE cameras at 699 dollars (Basler 2026); two Basler IP67 housings at 216.49 dollars (Basler 2026); one Advantech EKI-7708G-4FPI managed PoE industrial switch at list (Avendor 2026); one APC Smart-UPS SRT1500XLA double-conversion UPS (APC Guard 2026) | 9,441 each |
| Counting kits, 300 points | 300 installation points, one per casting strand or cooling bed: the paper's "hundreds of mills" covered line by line, taken here as an assumption | 2,832,000 |
| Frontier node | One server of eight 141 GB HBM-class cards, 320,000 to 420,000 dollars, typical 370,000 (Mercatus 2026) | 320,000 to 420,000 |
| Dedicated data center | One rack at a Gulf colocation guide rate of 18,000 dirhams a month, about 4,901 dollars (UAE Free Zone Finder 2026); Pakistani operators publish no rate, a quote settles it | 176,000 |
| Support | 8 to 12 percent of hardware value a year (Introl 2026) | 757,000 to 1,171,000 |
| Power | 30 kW across the kits at the mills plus 7 kW at the node at a power usage effectiveness of 1.6 (Uptime Institute 2025), 1,082,736 kWh at the industrial B3 average of 27 rupees per kWh (Dawn 2026), at 277.38 rupees to the dollar (SBP 2026) | 105,000 |
| **Total** | | **4,191,000 to 4,705,000, typical 4,445,000** |

The frontier tier fits one node because GLM 5.3 is 753 GB at FP8 and needs 904 GB with headroom, against 1,128 GB on eight 141 GB cards. Each kit is sized at 100 W: an Orin class industrial PC at 60 W, two cameras and a switch.

## A.3 What Renting the Frontier Node Costs

The node, rented without a break for three years, because counts reconcile every filing period and the work surface answers through the day. The counting kits stay at the mills in every option and are included in each total at 3,759,000 with their support and power.

| Option | Basis | Node alone | Three-year cost with the kits (USD) |
|---|---|---|---|
| AWS, UAE region, on demand | p5en.48xlarge at 75.96 dollars an hour in me-central-1 (Vantage 2026) | 2.00 million | 5.76 million |
| AWS, UAE region, three-year EC2 Instance Savings Plan | all upfront, 28.56 dollars an hour (AWS 2026) | 0.75 million | 4.51 million |
| Specialist GPU cloud, on demand | 50.44 dollars an hour for eight H200 cards (CoreWeave 2026) | 1.33 million | 5.08 million |
| Oracle, three-year commitment | 40 dollars an hour for eight H200 cards (Economize 2026) | 1.05 million | 4.81 million |

Egress, storage and the network link from Pakistan to the region are excluded, so every rented figure is a floor.

## A.4 What Closed Models Cost by the Token

A closed frontier model replaces the frontier node rather than the kits, and it is priced by use. At 60 users (an assumed count across the revenue field officers and audit staff the paper names; it scales with the mills each officer owns), each running the equivalent of five agents at 2.4 billion tokens a year, with four input tokens to every output token and half the input served from cache, three years is 432 billion tokens.

| Model | List price per million tokens, input and output | Three-year cost (USD) |
|---|---|---|
| Claude Sonnet 5.5 | 2 and 10 (Anthropic 2026) | 1.24 million |
| Gemini 3.1 Pro | 2 and 12 (Google 2026) | 1.42 million |
| Claude Opus 5.5 | 4 and 20 (Anthropic 2026) | 2.49 million |
| GPT-5.5 | 5 and 30 (OpenAI 2026) | 3.54 million |

The cheapest closed model costs about 21,000 dollars per user over three years, so it matches the owned node at about **33 users**; above that, ownership is cheaper and the gap grows with every user. Every closed option also sends the counted and declared production of every mill to a third-party AI service outside the boundary, which the design rules out.

## A.5 What the Price Does Not Include

- **Enclosure cooling, mounts, cabling and installation** at each point. No vendor publishes a list price for an actively cooled IP67 camera enclosure, so the kit prices the passive housings only; a written quote settles the rest.
- **An export licence.** Pakistan sits in US Country Group D:4, so the 141 GB HBM-class accelerators need a licence from the Bureau of Industry and Security (eCFR 2026); the design's licensing checkpoint confirms it before the node is ordered.
- **Import duty, sales tax, freight and insurance** on the hardware.
- **People, facilities and implementation**, which both sides carry.

## A.6 Sources for This Appendix

- Advantech. 2026. MIC-733-AO5A1. https://buy.advantech.com/
- Anthropic. 2026. Pricing. https://claude.com/pricing
- APC Guard. 2026. APC Smart-UPS SRT1500XLA. https://apcguard.com/srt1500xla.asp
- Avendor. 2026. Advantech EKI-7708G-4FPI-AE. https://avendor.com/products/4g-4sfp-with-poe-wide-temp
- AWS. 2026. EC2 Instance Savings Plans price file, me-central-1, 3 October 2026. https://pricing.us-east-1.amazonaws.com/savingsPlan/v1.0/aws/AWSComputeSavingsPlan/current/region_index.json
- Basler. 2026. ace 2 a2A2448-23gcIP67 and the ace 2 GigE camera housing. https://www.baslerweb.com/
- CoreWeave. 2026. Pricing. https://www.coreweave.com/pricing
- Dawn. 2026. NEPRA notifies new industrial tariffs. https://www.dawn.com/news/1973828
- eCFR. 2026. 15 CFR Part 740, Supplement No. 1, Country Groups. https://www.ecfr.gov/current/title-15/part-740/appendix-Supplement%20No.%201%20to%20Part%20740
- Economize. 2026. OCI BM.GPU.H200.8 pricing. https://www.economize.cloud
- Google. 2026. Gemini API pricing. https://ai.google.dev/gemini-api/docs/pricing
- Introl. 2026. GPU infrastructure TCO model. https://introl.com/blog/gpu-infrastructure-tco-model-5-year-enterprise-ai-deployment
- Mercatus. 2026. H200 server price. https://mercatus-ai.com/blog/h200-server-price
- OpenAI. 2026. API pricing. https://developers.openai.com/api/docs/pricing
- SBP. 2026. Conversion rates, 4 September 2026. https://www.sbp.org.pk
- UAE Free Zone Finder. 2026. UAE cloud computing and data center guide. https://uaefreezonefinder.com/uae-cloud-computing-data-center-guide-2026
- Uptime Institute. 2025. Global Data Center Survey 2025. https://uptimeinstitute.com
- Vantage. 2026. EC2 instance prices. https://instances.vantage.sh
