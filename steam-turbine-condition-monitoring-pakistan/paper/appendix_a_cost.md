# Appendix A · What the Site Inference Host Costs Over Three Years

The design runs every tier on the operator's own hardware inside the plant perimeter: one host of the 48 GB PCIe inference GPU class on a ruggedised edge server, hardened industrial switches, a PTP grandmaster time card and a one-way egress path for the DCS read (chapter 7). This appendix prices that envelope from public list prices, dated and cited, against renting the same card from the nearest hyperscaler region. Two lines are sold only by written quotation and are named and left out of the total rather than guessed. Every number can be rerun with a written quote.

## A.1 The Answer

Owning the site envelope costs about **22,500 US dollars over three years**, inside a range of 21,600 to 23,400. Renting one L40S card around the clock from the nearest region costs **22,600 to 60,000 dollars** over the same period, so ownership costs **about the same** as the deepest three-year commitment (an AWS EC2 Instance Savings Plan, all upfront, in the UAE region) and buys the switches, the time card and the power protection with it. The comparison is printed for reference only: no hyperscaler operates a region inside Pakistan, and the NEPRA Security of IT and OT Regulations 2022 bind the design to domain separation, so a rented card outside the plant would break the one-way read before it saved a dollar. Both models are open weights (MIT and Apache-2.0) and carry no licence line.

## A.2 What Owning Costs

| Line | Basis | Three-year cost (USD) |
|---|---|---|
| Inference host | One 48 GB L40S-class card with its share of host, memory and power supply, priced as one eighth of an eight-card L40S server at 85,271 dollars (Newegg 2026) | 10,700 |
| Time reference | One OCP-TAP Time Card as the PTP grandmaster at 1,500 dollars (Makerfabs 2026) | 1,500 |
| Network | Two industrial managed switches at 393.25 dollars each (Nassau National Cable 2026) | 800 |
| Clean shutdown | One APC Smart-UPS 3 kVA at 2,425.00 dollars (Markertek 2026) | 2,400 |
| **Equipment** | | **15,400** |
| Support | 8 to 12 percent of equipment value a year (Introl 2026) | 3,700 to 5,500 |
| Power | 0.6 kW average draw for the card and its host share (an assumption: the L40S is rated at 350 W) at a power usage effectiveness of 1.6 (Uptime Institute 2025), 25,229 kWh at the industrial B3 average of 27 rupees per kWh (Dawn 2026) at 277.38 rupees to the dollar (SBP 2026) | 2,500 |
| **Total** | | **21,600 to 23,400** |

Not in the table: the hardware data diode on the one-way egress path and the ruggedised enclosure beyond the host share, both sold by quotation; the five camera views, whose count and whether they reuse existing plant cameras are fixed at the site survey; and the DCS vendor's OPC UA server licence, which belongs to the upgraded DCS rather than to this design.

## A.3 What Renting the Card Would Cost

| Option | Basis | Three-year cost (USD) |
|---|---|---|
| AWS, UAE region, on demand | g6e.xlarge, one L40S, at 2.283 dollars an hour in me-central-1 (AWS 2026a); outside Pakistan | 60,000 |
| AWS, UAE region, three-year EC2 Instance Savings Plan, all upfront | g6e.xlarge at 0.85841 dollars an hour, the deepest three-year plan in the region (AWS 2026b); outside Pakistan | 22,600 |

Egress, storage and the network link from the plant to the region are excluded, so every rented figure is a floor. Neither option satisfies the boundary the design is built on.

## A.4 Sources for This Appendix

- AWS. 2026a. Amazon EC2 on-demand prices, Middle East (UAE), Linux, g6e.xlarge, as read 6 October 2026. https://aws.amazon.com/ec2/pricing/on-demand/
- AWS. 2026b. EC2 Instance Savings Plans price file, me-central-1, version 20261013035015, as read 14 October 2026. https://pricing.us-east-1.amazonaws.com/savingsPlan/v1.0/aws/AWSComputeSavingsPlan/current/region_index.json
- Dawn. 2026. NEPRA notifies new industrial tariffs. https://www.dawn.com/news/1973828
- Introl. 2026. GPU infrastructure TCO model. https://introl.com/blog/gpu-infrastructure-tco-model-5-year-enterprise-ai-deployment
- Makerfabs. 2026. OCP-TAP Time Card, read 12 October 2026. https://www.makerfabs.com/ocp-tap-time-card.html
- Markertek. 2026. APC SMT3000RM2UC Smart-UPS 3000VA, read 12 October 2026. https://www.markertek.com/product/apc-smt3000rm2uc/apc-smt3000rm2u-smart-ups-3000va-rm-2u-lcd-120v-with-smartconnec
- Nassau National Cable. 2026. Planet IGS-5225-4P2S industrial managed switch, read 12 October 2026. https://nassaunationalcable.com/products/planet-igs-5225-4p2s-industrial-full-managed-port-poe-switch
- Newegg. 2026. Supermicro SYS-421GE-TNRT-02-G1, eight L40S cards, 85,271 dollars, read 12 October 2026. https://www.newegg.com/p/N82E16859152404
- SBP. 2026. Conversion rates, 4 September 2026. https://www.sbp.org.pk
- Uptime Institute. 2025. Global Data Center Survey 2025. https://uptimeinstitute.com
