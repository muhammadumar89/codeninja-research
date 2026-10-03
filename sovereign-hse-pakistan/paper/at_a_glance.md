# At a glance · A sovereign health, safety and environment (HSE) platform for oil and gas in Pakistan

**What this is.** An open reference architecture for predicting HSE incidents at an oil and gas operator in Pakistan, on the operator's own hardware, with no data leaving the country and no third-party AI service in the serving path. It is written for HSE heads and for the engineers who would build it.

**The answer in numbers.**

| Part | The design |
|---|---|
| Sources joined | 8 systems: SAP EHS, PM and QM; SCADA; fire and gas; Vision AI cameras; SQL databases; scanned files; the identity provider |
| Object model | 12 typed objects and their links, published as JSON for reuse |
| Models | 6 self-hosted open-weight models, including GLM 5.3 (reasoning), Chronos-2 (forecasting), RF-DETR (vision), BGE-M3 (retrieval in English and Urdu) and PaddleOCR-VL 1.6 (scans) |
| Frontier compute | One node of eight 141 GB HBM-class GPUs holds GLM 5.3 at FP8 (753 GB of weights, 904 GB with headroom) |
| Three-year cost, owned | About 670,000 US dollars with support and power at Pakistan's industrial tariff |
| Three-year cost, rented | 1.4 to 2.8 million US dollars for the same GPUs in the nearest cloud region; no hyperscaler runs a region in Pakistan |
| Human control | Every recommendation is approved or rejected by a named person; nothing executes on equipment |
| The hard dependency | 141 GB-class accelerators need a US export licence for Pakistan (Country Group D:4); the rollout's first gate confirms installed hardware first |

**Reuse it.** The object model, the model register and the figures are free to reuse under CC BY 4.0.
