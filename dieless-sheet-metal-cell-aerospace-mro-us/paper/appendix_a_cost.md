# Appendix A · What the Cell's Compute and Sensing Cost Over Three Years

The design buys compute at two tiers and a sensing set around one dieless cell: a fanless inference computer in the cell panel, an eight-card 48 GB PCIe inference server in the facility, a PTP grandmaster time card, a hardware data diode, four fixed cameras, a structured-light scanner, a laser tracker reference channel, force load cells and temperature transmitters, in a rugged enclosure with clean shutdown. This appendix prices the classes that Table 4 names from public list prices, dated and cited, and compares the facility server with renting the same eight cards from the nearest hyperscaler region. The robot arms, the styli and the sheet metal are the forming cell itself and are outside Table 4; the laser tracker, the data diode and the safety controller are sold by quotation and are named but left out of the total. Every number can be rerun with a written quote.

## A.1 The Answer

Equipping the classes priced below costs about **151,000 US dollars** in list prices, and with support and power over three years **202,000 to 220,000 dollars**. The structured-light scanner and the eight-card server are most of it. Owning the two compute tiers costs about **132,000 dollars** over three years against **298,000 to 792,000 dollars** to rent eight L40S cards around the clock, so ownership is **about two fifths** the deepest three-year AWS commitment (EC2 Instance Savings Plan, all upfront, US East). The rental is printed for reference only: the request requires the cell to run wholly offline on the local network with no vendor cloud, so no rented option satisfies it. Every model in the register is Apache-2.0 and adds no license line.

## A.2 What Owning Costs

| Line | Basis | Three-year cost (USD) |
|---|---|---|
| Edge inference computer | One fanless industrial inference computer with an embedded GPU, Advantech MIC-733-AO5A1 (Jetson AGX Orin 32G class) at 4,646.41 dollars (Advantech 2026) | 4,600 |
| Facility inference server | One eight-card L40S server, Supermicro SYS-421GE-TNRT-02-G1, at 85,271.00 dollars (Newegg 2026) | 85,300 |
| Time synchronization | One OCP-TAP Time Card grandmaster at 1,500.00 dollars (Makerfabs 2026); antenna not separately priced | 1,500 |
| Structured-light scanner | One ZEISS ATOS Q 8M basic system package at 50,890.00 dollars (MatterHackers 2026) | 50,900 |
| Cameras | Four fixed PoE dome cameras with RTSP, Axis M3086-V at 523.00 dollars each (SHI 2026) | 2,100 |
| Force sensing | Two S-beam load cells, Omega LC103B-2K at 367.41 dollars each (Zot Supply 2026); amplifiers not included | 700 |
| Temperature sensing | Four DIN rail RTD transmitters, Phoenix Contact MINI MCR-2-RTD-UI-PT at 250.68 dollars each (Digi-Key 2026) | 1,000 |
| Enclosure | One nVent Hoffman A603616LP NEMA 12 enclosure, 60 by 36 by 16 inches, at 2,082.59 dollars (Zoro 2026) | 2,100 |
| Clean shutdown | One APC Smart-UPS 3 kVA at 2,425.00 dollars (Markertek 2026), driven by Network UPS Tools | 2,400 |
| **Equipment** | | **151,000** |
| Support | 8 to 12 percent of equipment value a year (Introl 2026) | 36,200 to 54,200 |
| Power | 3.7 kW average draw for the eight cards, their host and the edge box (an assumption: the L40S is rated at 350 W) at a power usage effectiveness of 1.6 (Uptime Institute 2025), 155,578 kWh at the US average industrial price of 9.77 cents per kWh for July 2026 (EIA 2026) | 15,200 |
| **Total** | | **202,000 to 220,000** |

Not in the table, because no public list price was found on 12 October 2026: the laser tracker (a used demonstration Leica AT500 set was listed at 18,500 dollars by a surveying reseller, which is a floor, not a list price), the hardware data diode (Fend Inc lists the SE and XE families without prices), and the safety PLC. Each is bought by quotation and each would add to the total.

## A.3 What Renting the Eight Cards Would Cost

| Option | Basis | Three-year cost (USD) |
|---|---|---|
| AWS, US East, on demand | g6e.48xlarge, eight L40S, at 30.13 dollars an hour in us-east-1 (AWS 2026a) | 792,000 |
| AWS, US East, three-year EC2 Instance Savings Plan, all upfront | g6e.48xlarge at 11.329 dollars an hour, the deepest three-year plan in the region (AWS 2026b) | 298,000 |

Storage, egress and the link from the facility to the region are excluded, so every rented figure is a floor. The owned figure it is compared with is the server and the edge box with support at 10 percent a year and their power: 132,000 dollars.

## A.4 Sources for This Appendix

- Advantech. 2026. MIC-733-AO5A1 fanless edge AI system, AGX Orin 32G, read 12 October 2026. https://buy.advantech.com/Compact-Computers/Edge-AI-Systems-Orin-NX/model-MIC-733-AO5A1.htm
- AWS. 2026a. Amazon EC2 on-demand prices, US East (N. Virginia), Linux, g6e.48xlarge, read 12 October 2026. https://instances.vantage.sh/aws/ec2/g6e.48xlarge
- AWS. 2026b. EC2 Instance Savings Plans price file, us-east-1, read 12 October 2026. https://pricing.us-east-1.amazonaws.com/savingsPlan/v1.0/aws/AWSComputeSavingsPlan/current/region_index.json
- Digi-Key. 2026. Phoenix Contact 2902052 MINI MCR-2-RTD-UI-PT, read 12 October 2026. https://www.digikey.com/en/products/detail/phoenix-contact/2902052/5198268
- EIA. 2026. Electric Power Monthly, Table 5.6.A, July 2026. https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_6_a
- Introl. 2026. GPU infrastructure TCO model. https://introl.com/blog/gpu-infrastructure-tco-model-5-year-enterprise-ai-deployment
- Makerfabs. 2026. OCP-TAP Time Card, read 12 October 2026. https://www.makerfabs.com/catalogsearch/result/?q=time+card
- Markertek. 2026. APC SMT3000RM2UC Smart-UPS 3000VA RM 2U LCD 120V with SmartConnect, read 12 October 2026. https://www.markertek.com/product/apc-smt3000rm2uc/apc-smt3000rm2u-smart-ups-3000va-rm-2u-lcd-120v-with-smartconnec
- MatterHackers. 2026. ZEISS ATOS Q 3D Scanner, ATOS Q 8M basic system package, read 12 October 2026. https://www.matterhackers.com/store/l/zeiss-atos-q-3d-scanner
- Newegg. 2026. Supermicro SYS-421GE-TNRT-02-G1, eight L40S cards, 85,271 dollars, read 12 October 2026. https://www.newegg.com/p/N82E16859152404
- SHI. 2026. Axis M3086-V network camera, 523.00 dollars as listed in search results on 12 October 2026; the product page itself refused the routine's fetch. https://www.shi.com/product/44881768/M3086-V
- Uptime Institute. 2025. Global Data Center Survey 2025. https://uptimeinstitute.com
- Zoro. 2026. nVent Hoffman A603616LP enclosure, read 12 October 2026. https://www.zoro.com/nvent-hoffman-screw-down-clamps-with-padlocking
- Zot Supply. 2026. Omega LC103B-2K S-beam load cell, 2,000 lbf, read 12 October 2026. https://zotsupply.com/Omega-LC103B-2K
