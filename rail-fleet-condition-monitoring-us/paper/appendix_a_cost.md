# Appendix A · What the Fleet Compute Costs Over Three Years

The requirement puts compute in a contractor-hosted cloud in the United States, with no server room on the property (chapter 1). The design serves its reasoning model, Mistral Large 3 675B, self-hosted on one node of the 141 GB HBM GPU class with vLLM, beside a small time series model (chapter 7). This appendix prices that node from the AWS price files for the US East region, dated and cited. The 225 monitoring modules are specified as a class (EN 50155 and IEC 60571 electronics, IP62, CFR 238 materials) rather than a part number and are sold by quotation, so they are named and left out of the total rather than guessed.

## A.1 The Answer

Running the node around the clock for three years costs **about 625,000 US dollars** on the deepest three-year commitment (an AWS EC2 Instance Savings Plan, all upfront, US East) and **about 1.66 million dollars** on demand, so the commitment costs **about three eighths** of the on-demand price. Both models are open weights under Apache-2.0 and carry no licence line.

## A.2 What the Node Would Cost

| Option | Basis | Three-year cost (USD) |
|---|---|---|
| AWS, US East, on demand | p5en.48xlarge, eight H200 cards of 141 GB, at 63.296 dollars an hour (Vantage 2026), 26,280 hours | 1,663,000 |
| AWS, US East, three-year Compute Savings Plan, all upfront | p5en.48xlarge at 42.21683 dollars an hour (AWS 2026) | 1,109,000 |
| AWS, US East, three-year EC2 Instance Savings Plan, all upfront | p5en.48xlarge at 23.7993 dollars an hour, the deepest three-year plan in the region (AWS 2026) | 625,000 |

Why eight cards: the 675 billion parameter model needs about 675 GB for its weights at eight bits, which fits on eight 141 GB cards with room for the KV cache and does not fit on fewer.

Not in the table: the 225 onboard monitoring modules and their installation across the fleet, sold by quotation; the 13 months of telemetry history over 64 signals per car, which the design prices into the service contract against the 5 percent annual escalation cap; and egress, which depends on the cellular plan already on each car.

## A.3 Sources for This Appendix

- AWS. 2026. EC2 Instance and Compute Savings Plans price file, us-east-1, version 20261013035015, as read 14 October 2026. https://pricing.us-east-1.amazonaws.com/savingsPlan/v1.0/aws/AWSComputeSavingsPlan/current/region_index.json
- Vantage. 2026. p5en.48xlarge pricing, US East (N. Virginia), Linux on demand, as read 14 October 2026. https://instances.vantage.sh/aws/ec2/p5en.48xlarge
