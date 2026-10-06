# Physical AI for agriculture and earth observation: questions answered

Canonical: https://codeatoms.ai/sectors/agriculture-and-earth-observation/
License: CC BY 4.0
Publisher: CodeNinja Atoms (https://codeatoms.ai)

Farms, irrigation and land use are watched by sensors, satellites and aircraft, but the readings, the licences and the field records usually sit in separate systems.

## What does a physical AI system for agriculture and earth observation look like?

A complete physical AI design for agriculture and earth observation names what to sense, which existing systems to join, the object model that joins them, the models and hardware, the three-year cost and the person who approves every action. CodeNinja Atoms has published 3 such reference architectures for agriculture and earth observation, each free to reuse under CC BY 4.0. Field Ledger (Pakistan): one dashboard that joins a farm's live sensor feeds, its historical datasets and a big data and analytics repository into one object model, so any farm, crop cycle or season can be drilled into, exported and reported on under role-based access. Baseline (United States): one summer flight of 3-inch 4-band orthoimagery and USGS Quality Level 1 LiDAR, with every tile, point cloud and elevation model bound into a site ontology, so the next season starts from a comparison instead of rediscovery. Fodder Watch (Saudi Arabia): an 18-month earth observation service that screens every parcel for restricted green fodder and cultivation beyond the licensed area, checks each detection against the holding's licence, and turns the confirmed ones into case files an inspector can act on.

## Which AI models can an agriculture and earth observation operator run on its own hardware?

Each published agriculture and earth observation design names its models and why, and every model is open-weight or no model is used at all, so the operator can run it on hardware it owns. Field Ledger: None: the analytics are deterministic aggregations, drill-down and reporting. Baseline: None: vegetation analysis stays with the operator's own analysts. Fodder Watch: RF-DETR fine-tuned per region and Chronos-2 zero-shot, both Apache-2.0, about 0.55 GB of weights together.

## How much compute and hardware does AI in agriculture and earth observation need?

The compute follows from the models: the published agriculture and earth observation designs size it as follows, from no new hardware to a full GPU node. Field Ledger, stack: Open-source PostgreSQL with PostGIS on the operator's own servers; source code and full intellectual property handed over. Baseline, ground: The operator's ArcGIS Enterprise; nothing runs in a cloud the operator does not control. Baseline, acquisition: One manned flight within a week either side of 1 July; 3-inch 4-band (red, green, blue, near infrared) orthoimagery and Quality Level 1 LiDAR at a minimum of 8 pulses per square meter. Fodder Watch, compute: One 48 GB L40S-class inference node inside the Kingdom; the card class needs a US export licence.

## Is it cheaper to own AI hardware or rent cloud GPUs in agriculture and earth observation?

Each agriculture and earth observation design prices three years of ownership in its Appendix A, with every price cited, against renting the same capacity from a cloud region at its deepest three-year commitment where hardware is bought. Field Ledger: three-year cost, No hardware line to price: the cost is the integration and software work (Appendix A). Baseline: three-year cost, No compute to price; the acquisition is priced by the survey firm against the operator's own task table (Appendix A). Fodder Watch: three-year cost, About 15,200 dollars to own the node, about two thirds the deepest three-year AWS commitment, and renting would move the data outside the Kingdom (Appendix A).

## What ontology or object model does an agriculture and earth observation AI system need?

The object model is the part that makes the system an ontology rather than a pipeline: typed objects for the things in the agriculture and earth observation operation, with properties, status values and typed links. Every published design ships its object model as hyper-ontology/1 JSON that loads into Hyper Ontology. Field Ledger: The site, The field, Crop Cycle, Sensor Device, Sensor Reading, Historical Dataset, Publication, Dashboard User, Access Role, Alert, Report, Data Source Connection. Baseline: The site, The unit, Watercourse, Dam, Flight Mission, 4-Band Aerial Camera System, QL1 LiDAR Sensor System, GNSS/IMU Georeferencing Chain, Multispectral Orthoimagery Product, Classified LAS Point Cloud, Bare-Earth and Highest-Hit DEMs, QA/QC Accuracy Report, Professional Services Agreement, Monthly Itemized Invoice, Contractor Project Manager, Operator Project Manager. Fodder Watch: Farm holding, Centre pivot / cultivated field, Farm enterprise / large farmer, Crop licence (wheat / seasonal fodder), Water source (well) use licence, Green fodder ban control, Agricultural fuel / electricity service condition record, Imagery tasking order, Satellite image capture, Processed imagery product, Restricted-crop detection flag, Violation case file, Field inspector, Restricted-crop classifier.

## Who approves the decisions an AI system makes in agriculture and earth observation?

In every published agriculture and earth observation design a named person makes the decision that changes the physical world; the system prepares it. Field Ledger: Every alert is acknowledged by a named user under a role the operator assigns. Baseline: The operator's project manager accepts each deliverable against the QA/QC accuracy report. Fodder Watch: Every flag is verified on the ground by a named field inspector before a case file opens.

## Sources

- [Field Ledger: An Open Source Agriculture Data Dashboard the Operator Fully Owns](https://codeatoms.ai/farm-data-dashboard-pakistan/) (Pakistan), DOI https://doi.org/10.5281/zenodo.23186671
- [Baseline: One Flight of 4 Band Orthoimagery and LiDAR for Vegetation Mapping](https://codeatoms.ai/vegetation-mapping-lidar-us/) (United States), DOI https://doi.org/10.5281/zenodo.23186673
- [Fodder Watch: Earth Observation That Turns Restricted-Crop Detections Into Enforceable Case Files](https://codeatoms.ai/restricted-crop-monitoring-saudi-arabia/) (Saudi Arabia), DOI https://doi.org/10.5281/zenodo.23186675
