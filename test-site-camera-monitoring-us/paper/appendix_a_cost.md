# Appendix A · What the Camera Estate Costs Over Three Years

The design buys a field estate and a small amount of compute: fixed thermal and visible camera heads on 40 to 60 poles, the switches, enclosures and power at each pole, two fiber aggregation switches, a four-display booth, and an N+1 recorder pair in the conditioned server room, each host carrying one 48 GB L40S-class card and 30 days of footage on local disk. This appendix prices that estate from public list prices, dated and cited, at both ends of the pole count. The field estate has no rental equivalent, so the only rent comparison is the compute, and it is printed for reference only, because the operator requires the audio visual core to run on-premises. Every number can be rerun with a written quote.

## A.1 The Answer

Equipping the estate costs about **375,000 to 632,000 US dollars** in list prices, and with support and power over three years **474,000 to 871,000 dollars**. The camera heads are most of it: 287,000 to 501,000 dollars, because a thermal and visible head costs about seven to eight thousand dollars and a proving ground needs one on every pole. The compute is small by comparison: owning the two recorder hosts costs about **32,600 dollars** over three years, against **36,800 to 118,000 dollars** to rent two L40S cards around the clock, so ownership is **about four fifths** the deepest three-year AWS commitment (EC2 Instance Savings Plan, all upfront, US East) before the 30 days of footage are stored anywhere. There is **no per camera license** at any pole count: the recorder is open source and the detector is Apache-2.0.

## A.2 What Owning Costs

| Line | Basis | Three-year cost (USD) |
|---|---|---|
| Camera heads | One bi-spectrum thermal and visible head per pole, 40 to 60 poles: Hanwha Vision TNM-C4950TD at 7,165.99 dollars (IP Security Depot 2026) at the low end, TNM-C4940TD at 8,351.00 (OWL360IT 2026) at the high end; two streams per head gives the paper's 80 to 120 | 287,000 to 501,000 |
| Pole kit | Per pole: Planet IGS-5225-4P2S managed PoE switch with two SFP uplinks at 393.25 (Nassau National Cable 2026), nVent Hoffman NEMA 4X enclosure at 344.99 (Zoro 2026), Hammond 1 kVA 277 V to 120 V transformer at 345.79 (Standard Electric Supply 2026), Mean Well 24 V DIN supply at 26.78 (TRC Electronics 2026); 1,110.81 a pole | 44,400 to 66,600 |
| Fiber aggregation | Two FS S5850-48S6Q switches with 48 SFP+ ports each at 3,798.48 (SabrePC 2026), enough for 60 poles with a spare path | 7,600 |
| Operator booth | Four Samsung QM55C 55 inch displays rated for continuous use at 1,260.00 (AVendor 2026) | 5,000 |
| Recorder hosts | Two hosts, primary and standby, each one L40S-class card with its share of host, memory and power supply, priced as one eighth of an eight-card L40S server at 85,271 dollars (Newegg 2026); the card alone lists at 10,710.15 (SabrePC 2026) | 21,300 |
| Footage disks | 30 days of 80 to 120 streams on each host at 1.21 to 5 Mbps a stream (Bosch 2020; Hanwha Vision 2026), 31 to 194 TB a host plus a quarter for parity, on 2 to 11 WD Purple Pro 24 TB drives a host at 1,133.99 (CDW 2026) | 4,500 to 24,900 |
| Clean shutdown | Two APC Smart-UPS 3 kVA at 2,039.99 (CDW 2026), one per host, driven by Network UPS Tools | 4,100 |
| Time | One OCP Time Card grandmaster with holdover oscillator at 1,500.00 (Makerfabs 2026) | 1,500 |
| **Equipment** | | **375,000 to 632,000** |
| Support | 8 to 12 percent of equipment value a year (Introl 2026) | 90,000 to 228,000 |
| Power, server room | 0.6 kW a host for the card and its host share (an assumption: the L40S is rated at 350 W) plus about 7 W a drive, at a power usage effectiveness of 1.6 (Uptime Institute 2025), at the US average industrial price of 9.77 cents per kWh for July 2026 (EIA 2026) | 5,000 to 5,600 |
| Power, poles | 35 W a pole for the head inside its PoE+ budget and the switch (an assumption), around the clock, at the same price | 3,600 to 5,400 |
| **Total** | | **474,000 to 871,000** |

The low end is 40 poles, the lower priced head and the low bitrate; the high end is 60 poles, the higher priced head and 5 Mbps on every stream. The one model, D-FINE, holds about 8 to 124 MB of weights and adds no hardware line.

## A.3 What Renting the Compute Would Cost

For reference only: the operator requires the audio visual core on-premises, and the field estate cannot be rented at all. The same two cards, rented without a break for three years, because recording never stops:

| Option | Basis | Three-year cost (USD) |
|---|---|---|
| AWS, US East, on demand | two g6e.xlarge, one L40S each, at 1.861 dollars an hour in us-east-1 (AWS 2026a) | 97,800 |
| AWS, US East, three-year EC2 Instance Savings Plan, all upfront | two g6e.xlarge at 0.69974 dollars an hour, the deepest three-year plan in the region (AWS 2026b) | 36,800 |
| Specialist GPU cloud, on demand | 18.00 dollars an hour for eight L40S cards, 2.25 per card, two cards (CoreWeave 2026) | 118,000 |

Each g6e.xlarge carries 250 GB of local disk, so storing 30 days of footage, egress and the network link back to the site are all excluded, and every rented figure is a floor.

## A.4 What the Price Does Not Include

- **Poles, trenching, conduit and the fiber itself.** No fiber route diagrams exist, so the run lengths are unknown until the phase one survey; civil works are priced on the survey, not here.
- **Installation, the coverage survey, commissioning and acceptance testing**, which the phased rollout sizes.
- **A drive chassis.** The recorder host share carries the card; the 2 to 11 drives each host needs sit in its own bays or in a small external enclosure, priced on the written quote.
- **Section 889 sourcing.** The time card listed here ships from outside the United States, and the booth display has built-in wireless radios that the design does not allow; both are placeholders for screened, radio-free equivalents, which the component-level bill of materials settles.
- **Lightning and surge protection** at each pole and on the grandmaster antenna run, which the vendor's alternate and the operator's assessment fix.
- **Sales tax and freight**, which a written quote settles.

## A.5 Sources for This Appendix

- AWS. 2026a. Amazon EC2 on-demand prices, US East (N. Virginia), Linux, g6e.xlarge, price file of 9 October 2026. https://aws.amazon.com/ec2/pricing/on-demand/
- AWS. 2026b. EC2 Instance Savings Plans price file, us-east-1, version 20261010020024. https://pricing.us-east-1.amazonaws.com/savingsPlan/v1.0/aws/AWSComputeSavingsPlan/current/region_index.json
- AVendor. 2026. Samsung QM55C 55 inch commercial display. https://avendor.com/products/samsung-qm55c-55-commercial-4k-uhd-display
- Bosch. 2020. DINION IP 5000i data sheet, H.265 typical bitrate. https://cdn.commerce.boschsecurity.com/public/documents/DINION_IP_5000i_Data_sheet_enUS_33412453003.pdf
- CDW. 2026. APC Smart-UPS SMT3000RM2UC 3 kVA. https://www.cdw.com/product/apc-smart-ups-line-interactive-3kva-rackmount-2u-120v-6x-nema-5-15r-2x/4894882
- CDW. 2026. WD Purple Pro WD240PURP 24 TB. https://www.cdw.com/product/wd-purple-pro-wd240purp-hard-drive-24-tb-surveillance-smart-video/8237466
- CoreWeave. 2026. Pricing, L40S on demand. https://www.coreweave.com/pricing
- EIA. 2026. Electric Power Monthly, Table 5.6.A, July 2026. https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_6_a
- Hanwha Vision. 2026. DesignPro, understanding bitrates. https://support.hanwhavision.com/hc/en-001/articles/54540420837779-DesignPro-Understanding-Bitrates
- IP Security Depot. 2026. Hanwha Vision TNM-C4950TD bi-spectrum thermal and visible camera. https://www.ipsecuritydepot.com/hanwha-tnm-c4950td-vga-4k-dual-sensor-ai-bi-spectrum-thermal-outdoor-varifocal-dome-ip-camera/tnm-c4950td/
- Introl. 2026. GPU infrastructure TCO model (support rate). https://introl.com/blog/gpu-infrastructure-tco-model-5-year-enterprise-ai-deployment
- Makerfabs. 2026. OCP-TAP Time Card. https://www.makerfabs.com/ocp-tap-time-card.html
- Nassau National Cable. 2026. Planet IGS-5225-4P2S industrial managed PoE switch. https://nassaunationalcable.com/products/planet-igs-5225-4p2s-industrial-full-managed-port-poe-switch
- Newegg. 2026. Supermicro SYS-421GE-TNRT-02-G1, eight L40S cards. https://www.newegg.com/p/N82E16859152404
- OWL360IT. 2026. Hanwha Vision TNM-C4940TD bi-spectrum thermal and visible camera. https://storeusa.owl360it.com/products/hanwha-bi-spectrum-ai-thermal-camera-1431429
- SabrePC. 2026. FS S5850-48S6Q, 48 SFP+ ports. https://www.sabrepc.com/29123-FS-S112555877
- SabrePC. 2026. L40S 48 GB PCIe card, part 900-2G133-0080-000. https://www.sabrepc.com/900-2G133-0080-000-NVIDIA-S7323682
- Standard Electric Supply. 2026. Hammond C1F1C0CES 1 kVA, 277 V to 120/240 V. https://www.standardelectricsupply.com/Hammond-Power-Solutions-C1F1C0CES-HPS-Fortress-Distribution-Transformer
- TRC Electronics. 2026. Mean Well HDR-60-24. https://trcelectronics.com/products/mean-well-hdr-60-24
- Uptime Institute. 2025. Global Data Center Survey 2025. https://uptimeinstitute.com
- Zoro. 2026. nVent Hoffman A16148CHQRFG NEMA 4X enclosure. https://www.zoro.com/nvent-hoffman-quick-release-latch-electrical-enclosures-16-in-h-8-in-d-14-in-w-12-13-4-4x-fiberglass-a16148chqrfg/i/G8750594/

All prices were read on 11 October 2026.
