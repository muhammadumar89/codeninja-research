# Appendix A · What the Central Card Costs Over Three Years

The design runs its work surface model, gpt-oss-120b, on vLLM on one card of the 141 GB HBM GPU class, one card in one node, in the railroad's own data center (chapter 7, section 7.1; Table 4, "Central hardware class"). Chronos-2 sits on the trending service beside the time series store at about 0.24 GB and needs no card of its own (chapter 7, section 7.1). D-FINE and PP-OCRv6 run on the octa-core NPU edge box at the four-camera yard-entry portal (chapter 7, section 7.1; Table 4, "Edge compute sizing"). This appendix prices the central card two ways, owned in the railroad's data center and rented from the AWS US East region, from public prices, dated and cited. The edge box, the portal cameras and the pilot locomotive sensing are specified as classes rather than part numbers and are sold by quotation, so they are named and left out of the total rather than guessed.

## A.1 The Answer

Owning the central card costs **about 54,000 US dollars over three years**, inside a range of 52,000 to 57,000, for the card, its support and its power; the host server is sold by quotation and is not in that figure. Renting the smallest AWS instance that holds one 141 GB card costs **about 625,000 dollars** on the deepest three-year commitment (an AWS EC2 Instance Savings Plan, all upfront, US East) and **about 1.66 million dollars** on demand, so the commitment costs **about three eighths** of the on demand price. All four models are open weights under Apache-2.0 and carry no licence line.

## A.2 What Owning Costs

| Line | Basis | Three-year cost (USD) |
|---|---|---|
| Card | One NVIDIA H200 NVL PCIe card of 141 GB at 39,774 dollars (CloudNinjas 2026) | 39,774 |
| Support | 8 to 12 percent of hardware value a year (Introl 2026), 24 to 36 percent over three years | 9,546 to 14,319 |
| Power | The card's 600 W maximum (NVIDIA 2026) for 26,280 hours at an assumed power usage effectiveness of 1.6, 25,229 kWh at the US industrial average of 9.77 cents per kWh in July 2026 (EIA 2026) | 2,465 |
| **Total** | | **51,785 to 56,558, typical 54,171** |

Why one card: the gpt-oss-120b checkpoint as shipped is 65.2 GB, its MoE weights in MXFP4 and the rest at 16 bit, and the paper's 1.2 planning factor brings the card to 78.2 GB, which one 141 GB card holds with about 63 GB spare (chapter 3, section 3.2; chapter 7, section 7.1; chapter 8, section 8.1).

The host server that carries the card is sold by quotation, because no public price was found for a server configured with one H200 NVL card, so it is left out of the total along with its share of support and power. The card's power is taken at its maximum draw, so that line is a ceiling for the card alone.

## A.3 What Renting Costs

AWS does not sell an H200 instance smaller than eight cards in US East: the region's price file lists p5en.48xlarge as the only p5en size. The smallest instance that holds one 141 GB card is therefore p5en.48xlarge, eight H200 cards of 141 GB, of which the design would use one. It is rented without a break for three years, 26,280 hours, because detector passes arrive at every hour and the trend must be ready before an axle reaches the next detector (chapter 7, section 7.2).

| Option | Basis | Three-year cost (USD) |
|---|---|---|
| AWS, US East, on demand | p5en.48xlarge at 63.296 dollars an hour (Vantage 2026), 26,280 hours | 1,663,000 |
| AWS, US East, three-year Compute Savings Plan, all upfront | p5en.48xlarge at 42.21683 dollars an hour (AWS 2026) | 1,109,000 |
| AWS, US East, three-year EC2 Instance Savings Plan, all upfront | p5en.48xlarge at 23.7993 dollars an hour, the deepest three-year plan in the region (AWS 2026) | 625,000 |

The arithmetic: 63.296 × 26,280 = 1,663,419; 23.7993 × 26,280 = 625,446; and 625,446 ÷ 1,663,419 = 0.376, about three eighths.

Against the owned option no ratio is printed, because the owned total leaves out the host server. What the arithmetic does support is a margin: 625,446 − 54,171 = 571,275, so the host server with its support and power would have to cost more than about 571,000 dollars over three years before owning cost as much as the deepest cloud commitment. Egress, storage and support plans are excluded from every rented figure, so each is a floor.

## A.4 What the Price Does Not Include

- **The host server for the central card**, sold by quotation, as above.
- **The octa-core NPU edge box at the portal**, specified by class and sized from its streams (Table 4, "Edge compute sizing"), sold by quotation.
- **The four portal cameras**, left side, right side, wheel line and yard throat overview, bought by class against pixel density and blur budget arithmetic (Table 4, "Portal sensing"), sold by quotation, with their enclosure, mounting, power and protection (chapter 11, section 11.4).
- **The pilot locomotive sensing**, vibration and temperature on traction motors and axle bearings (Table 4, "Wayside sensing"), sold by quotation; the paper does not state how many locomotives the pilot covers.
- **The 29 existing wayside detectors**, which the railroad already owns and runs, so they carry no new cost.
- **The data center servers for the event backbone, ontology store and time series store**, which the paper chooses by class against measured pass volume and does not size (chapter 4, Table 3).
- **Sales tax, freight, installation, people and implementation**, which a written quote and the build settle.

## A.5 Sources for This Appendix

- AWS. 2026. EC2 Instance and Compute Savings Plans price file, us-east-1, version 20261021225300, as read 22 October 2026. https://pricing.us-east-1.amazonaws.com/savingsPlan/v1.0/aws/AWSComputeSavingsPlan/current/region_index.json
- CloudNinjas. 2026. NVIDIA H200 NVL PCIe 141GB Data Center GPU, as read 22 October 2026. https://cloudninjas.com/collections/asrock-rack-4uxgm-turin2-gpu-upgrades/products/nvidia-h200-nvl-pcie-141gb-data-center-gpu
- EIA. 2026. Electric Power Monthly, Table 5.6.A, July 2026, as read 22 October 2026. https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_6_a
- Introl. 2026. GPU infrastructure TCO model, as read 22 October 2026. https://introl.com/blog/gpu-infrastructure-tco-model-5-year-enterprise-ai-deployment
- NVIDIA. 2026. H200 specifications, H200 NVL, as read 22 October 2026. https://www.nvidia.com/en-us/data-center/h200/
- Vantage. 2026. p5en.48xlarge pricing, US East (N. Virginia), Linux on demand, as read 22 October 2026. https://instances.vantage.sh/aws/ec2/p5en.48xlarge
