# Appendix A · What Ownership Costs Over Three Years

The design runs both of its models, the RF-DETR detector and the Chronos-2 forecaster, on one 48 GB L40S-class inference node in the operator's own facility inside the Kingdom. This appendix prices that node against renting the same card from a cloud region. Every input is a public price, dated and cited, and the arithmetic is shown so any reader can rerun it with a written quote. A closed model priced by the token is not compared, because neither model is a language model and no hosted service offers this detector and forecaster pair.

## A.1 The Answer

Owning the inference node costs about **15,200 US dollars over three years**, inside a range of 14,600 to 15,800. Renting one L40S card around the clock costs **22,600 to 60,000 dollars** over the same period. Against the deepest three-year commitment listed (AWS, three-year EC2 Instance Savings Plan, all upfront, in the UAE region), ownership is **about two thirds** the cost. No rented option can sit inside the Kingdom today: AWS's Saudi region opens in December 2026 (Channel Insider 2026), and every option below would move imagery, register data and detections across the border, which the design's sovereignty constraint rules out.

## A.2 What Owning Costs

| Line | Basis | Three-year cost (USD) |
|---|---|---|
| Inference node | One L40S-class card with its share of host, memory and power supply, priced as one eighth of an eight-card L40S server at 85,271 dollars (Newegg 2026); the card alone lists at 7,709 dollars (esaitech 2026) | 10,700 |
| Support | 8 to 12 percent of hardware value a year (Introl 2026) | 2,600 to 3,800 |
| Power | 0.6 kW average draw for the card and its host share (an assumption: the L40S is rated at 350 W) at a power usage effectiveness of 1.6 (Uptime Institute 2025), 25,229 kWh at the industrial tariff of 0.20 riyals per kWh (ECRA 2025) at 3.75 riyals to the dollar | 1,300 |
| **Total** | | **14,600 to 15,800, typical 15,200** |

One card is enough because the two models together hold about 0.55 GB of weights (Table 4); the 48 GB class leaves room for batching every parcel in a screening round.

## A.3 What Renting Costs

The same card, rented without a break for three years, because screening rounds follow the imagery and the season, not office hours.

| Option | Basis | Three-year cost (USD) |
|---|---|---|
| AWS, UAE region, on demand | g6e.xlarge, one L40S, at 2.283 dollars an hour in me-central-1 (AWS 2026a); outside the Kingdom | 60,000 |
| AWS, UAE region, three-year EC2 Instance Savings Plan, all upfront | g6e.xlarge at 0.858 dollars an hour, the deepest three-year plan in the region (AWS 2026b); outside the Kingdom | 22,600 |
| Specialist GPU cloud, on demand | 18.00 dollars an hour for eight L40S cards, 2.25 per card (CoreWeave 2026); outside the Kingdom | 59,100 |

Egress, storage of the mirrored archive and the network link to the region are excluded, so every rented figure is a floor.

## A.4 What the Price Does Not Include

- **An export licence.** The L40S is an advanced computing item under ECCN 3A090, and its export to Saudi Arabia needs a licence from the Bureau of Industry and Security (NVIDIA 2023; eCFR 2026), granted case by case. The order date for the node is therefore a phase one checkpoint on the licence timeline.
- **The imagery itself**: Sentinel-2, Sentinel-1 and Landsat are free; commercial confirmation tasking is bought per need and priced by the supplier.
- **Field tablets and GNSS equipment** for inspectors, which the operator already issues.
- **Customs duty and 15 percent VAT** on the hardware, which a written quote delivered to the Kingdom settles.
- **People, facilities and implementation**, which both sides carry.

## A.5 Sources for This Appendix

- AWS. 2026a. Amazon EC2 on-demand prices, Middle East (UAE), Linux, g6e.xlarge. https://aws.amazon.com/ec2/pricing/on-demand/
- AWS. 2026b. EC2 Instance Savings Plans price file, me-central-1, version 20261005200132. https://pricing.us-east-1.amazonaws.com/savingsPlan/v1.0/aws/AWSComputeSavingsPlan/current/region_index.json
- Channel Insider. 2026. AWS cloud region launch, Saudi Arabia. https://www.channelinsider.com/infrastructure/news-aws-cloud-region-launch-emea-saudi-arabia/
- CoreWeave. 2026. Pricing. https://www.coreweave.com/pricing
- eCFR. 2026. 15 CFR Part 740, Supplement No. 1, Country Groups. https://www.ecfr.gov/current/title-15/part-740/appendix-Supplement%20No.%201%20to%20Part%20740
- ECRA. 2025. Electricity tariff, effective 28 May 2025, as reported. https://clenergize.com/ksa-electricity-tariff-changes-in-2025-is-your-business-ready/
- esaitech. 2026. PNY NVIDIA L40S 48 GB GDDR6 PCIe. https://esaitech.com/products/pny-technologies-nvl40stcgpu-kit-nvidia-l40s-4-port-48gb-gddr6-graphic-card
- Introl. 2026. GPU infrastructure TCO model. https://introl.com/blog/gpu-infrastructure-tco-model-5-year-enterprise-ai-deployment
- Newegg. 2026. Supermicro SYS-421GE-TNRT-02-G1. https://www.newegg.com/p/N82E16859152404
- NVIDIA. 2023. Form 8-K, 17 October 2023. https://www.sec.gov/Archives/edgar/data/1045810/000104581023000217/nvda-20231017.htm
- Uptime Institute. 2025. Global Data Center Survey 2025. https://uptimeinstitute.com
