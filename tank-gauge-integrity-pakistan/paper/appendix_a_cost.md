# Appendix A · What It Costs

The design buys no compute and serves no model. The integrity checks are deterministic rules that run on the operator's existing gauging host and server, and the model register is empty by design, so there is no owned-versus-rented comparison to print. The equipment the design does buy is field hardware inside the requirement's own supply scope: OEM-authorized Modbus boosters (repeaters), hazardous-area junction boxes, field power supplies and loop cabling. Those lines are priced by the OEM's quotation against the signal survey, not by any public list price, so this appendix prints none.

## A.1 What Would Change the Answer

| Line | When it appears | How to price it |
|---|---|---|
| Booster count | If the signal survey finds a loop needs a second booster, or one loop needs none | One OEM quotation per installation; the survey sets the count, not the paper |
| A learned anomaly model | If deterministic checks stop catching a new failure pattern | A small time series model on CPU at the operator's server; no GPU class is required at this scale |
| A generative work surface | If the operator later asks questions of the inventory model in natural language | A frontier open-weight model on one node of eight 141 GB HBM-class GPUs, 320,000 to 420,000 dollars (Mercatus 2026), which needs a US export licence for Pakistan |

## A.2 Sources for This Appendix

- Mercatus. 2026. H200 server price. https://mercatus-ai.com/blog/h200-server-price
