# Appendix A · What the Monitoring Estate Costs Over Three Years

The design buys field equipment and no compute: gateways, transmitters, meters and contact nodes at each factory, read into an IoT platform the operator already runs inside Saudi Arabia. This appendix prices the estate for the hundred factories the paper classes high risk, from public list prices, dated and cited. There is no equivalent to rent: the devices sit at the factories in every option, so the only cloud line is what ingesting their messages would cost on a hyperscaler, printed for reference only, because the operator's platform is already hosted in the Kingdom and its cost is sunk. Every number can be rerun with a written quote.

## A.1 The Answer

Equipping a factory costs about **2,623 to 3,211 US dollars** in list prices, the range being the gateway class. Across 100 high-risk factories the estate costs **262,000 to 321,000 dollars**, and with support and power over three years **328,000 to 439,000 dollars**. The eight-factory pilot the paper starts with is about 21,000 to 26,000 dollars of equipment. Message ingestion on a hyperscaler outside the Kingdom would add at most about 1,188 dollars over three years, which says how little the platform cost matters next to the field estate.

## A.2 What Owning Costs

| Line | Basis | Three-year cost (USD) |
|---|---|---|
| Equipment, per factory | RAK7289V2 WisGate Edge Pro, 16 channels with LTE (RAK Wireless 2026); two Milesight EM500-SWL LoRaWAN submersible level transmitters at 420 dollars (MCCI 2026); two Eastron SDM630 three-phase CT meters at 137.63 pounds (Forestrock 2026), at an assumed 1.34 dollars to the pound; four Dragino LT-22222-L LoRaWAN digital input nodes at 71 dollars for the panel and pump contacts (Embedded Works 2026); one Moxa EDS-2008-EL fanless industrial switch at 107 euros (Elmark 2026), at an assumed 1.17 dollars to the euro; one Hoffman NEMA 4X fibreglass enclosure (DigiKey 2026); one APC BR1000MS UPS (Markertek 2026) | 2,623 |
| Gateway, upper bound | Kerlink Wirnet iStation outdoor gateway at 1,112 dollars (Novotech 2026) in place of the RAK gateway | 3,211 per factory |
| Equipment, 100 factories | The paper's count of factories classed high risk, one gateway, two tanks, two meters and four contact nodes each, as the design's monitored point families | 262,000 to 321,000 |
| Support | 8 to 12 percent of equipment value a year (Introl 2026) | 63,000 to 116,000 |
| Power | 20 W a factory for gateway, switch and nodes, 52,560 kWh at the industrial tariff of 0.20 riyals per kWh (ECRA 2025) at 3.75 riyals to the dollar | 2,803 |
| **Total** | | **328,000 to 439,000** |

The one model in the design, a 0.85 million parameter forecaster, runs on CPU inside the existing platform and adds no hardware line.

## A.3 What Ingesting the Messages Would Cost on a Hyperscaler

For reference only: the operator's platform is already hosted in Saudi Arabia. At 100 factories with 20 monitored points each sampled every 15 minutes, about 192,000 messages a day:

| Option | Basis | Three-year cost (USD) |
|---|---|---|
| AWS IoT Core, Bahrain region | 1.10 dollars per million messages, 0.165 per million rules triggered and per million actions (AWS 2026); outside the Kingdom | 301 |
| Azure IoT Hub, UAE North | S1 units at 33 dollars a month for 400,000 messages a day each, 1.0 units (Azure 2026); outside the Kingdom | 1,188 |

## A.4 What the Price Does Not Include

- **Installation, cabling, RF survey and commissioning** at each factory, which the design's phase 0 survey sizes.
- **Thermal and current transformer selection** per panel and pump controller, which the site survey fixes.
- **Customs duty and 15 percent VAT** on the equipment, which a written quote delivered to the Kingdom settles.
- **Exchange rates.** The meter and switch prices are listed in pounds and euros; this appendix converts them at assumed rates of 1.34 and 1.17 dollars, stated in the table.
- **The platform's own cost**, which the operator already pays.

## A.5 Sources for This Appendix

- AWS. 2026. AWS IoT Core price list, me-south-1. https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AWSIoT/current/me-south-1/index.json
- Azure. 2026. Retail prices, IoT Hub, UAE North. https://prices.azure.com/api/retail/prices
- DigiKey. 2026. Hoffman A16148CHSCFG. https://www.digikey.com/
- ECRA. 2025. Electricity tariff, effective 28 May 2025, as reported. https://clenergize.com/ksa-electricity-tariff-changes-in-2025-is-your-business-ready/
- Elmark. 2026. Moxa EDS-2008-EL. https://elmark-automation.com/shop/moxa/eds-2008-el
- Embedded Works. 2026. Dragino LT-22222-L. https://embeddedworks.net/product/sens648
- Forestrock. 2026. Eastron SDM630-MBUS-MID. https://forestrock.co.uk/product/eastron-sdm630-mbus-mid-meter
- Introl. 2026. GPU infrastructure TCO model (support rate). https://introl.com/blog/gpu-infrastructure-tco-model-5-year-enterprise-ai-deployment
- Markertek. 2026. APC BR1000MS. https://www.markertek.com/product/apc-br1000ms/
- MCCI. 2026. Milesight EM500-SWL. https://store.mcci.com/
- Novotech. 2026. Kerlink Wirnet iStation 915. https://novotech.com/products/outdoor-gateway-wirnet-istation-915-mhz
- RAK Wireless. 2026. WisGate Edge Pro RAK7289V2. https://store.rakwireless.com/products/wisgate-edge-pro-rak7289v2-rak7289cv2
