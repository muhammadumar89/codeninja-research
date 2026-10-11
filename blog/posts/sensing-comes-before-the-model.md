---
{
 "title": "Sensing Comes Before the Model",
 "subtitle": "Three published earth observation architectures decide what to watch from law, revisit and ownership, never from model accuracy. Two of the three ship with an empty model register.",
 "author": "CodeNinja Atoms",
 "author_role": "Research distribution",
 "author_url": "https://codeatoms.ai/about/",
 "date": "2026-10-11",
 "tags": [
  "Engineering",
  "Earth observation",
  "Sovereign AI"
 ],
 "audience": "For engineers designing an earth observation or remote sensing system who are about to start with the model.",
 "description": "A cross design read of the three open earth observation reference architectures in the Vertical-Driven Architectures corpus: how each one chose its sensing, why two of the three carry no model at all, and the one case where the cheapest rental is still the wrong answer."
}
---

The usual way to start an earth observation project is to pick the model. Someone has a segmentation network that works on satellite imagery, and the architecture grows around it.

Three designs in this corpus say the order is wrong. All three are agriculture and earth observation systems, in Pakistan, Saudi Arabia and the United States. In all three the sensing decision is made first and made from constraints that have nothing to do with accuracy: what the law allows, how often the sensor comes back, and who ends up owning the output. In two of the three, no model is committed at all.

## Two of three registers are empty, by decision

[Field Ledger](https://codeatoms.ai/farm-data-dashboard-pakistan/) is an agriculture data dashboard in Pakistan on twelve objects. Its register records zero models, and the reason is written down: the requirement commits aggregations, drill down and reporting, and no model was verified for this run. A forecaster over the sensor time series is named as open work, gated on Milestone 1 evidence rather than assumed into the design.

[Baseline](https://codeatoms.ai/vegetation-mapping-lidar-us/) is a one flight acquisition of 4 band orthoimagery and LiDAR in the United States on sixteen objects. Its register is empty too, for a blunter reason: no model layer was wanted. Vegetation analysis stays with the operator's own staff in the operator's own tools. The entry that follows it is the one most model centric designs never write, that with zero weights there is no model license to hold or to trigger, so ownership runs through the services agreement instead.

[Fodder Watch](https://codeatoms.ai/restricted-crop-monitoring-saudi-arabia/) is the only one of the three that commits models: two, on fourteen objects. A detector, RF-DETR under Apache 2.0, fine tuned per region. A forecaster, Chronos-2 under Apache 2.0, zero shot, about 120M parameters. Both licenses were part of the choice, not a footnote after it.

An empty register is a result, not a gap. It says the cross system join was the hard part and the design did not need a learned component to do it.

## What actually decided the sensing

In each design the sensing entry carries its own reason, and none of the reasons is a benchmark score.

Fodder Watch screens parcels for restricted cultivation. Its optical channel is Sentinel-2 at 10 m with a 5 day revisit, picked because it resolves center pivots for crop class without a foreign processing dependency. Its radar channel is Sentinel-1 C band SAR, and the stated reason is worth reading twice: the cloud proof complement matters because dust and haze, not cloud, are the optical channel's real attacker in that geography. Landsat 8/9 at an 8 day combined revisit is there for the archive reaching back decades, which is what gives each parcel a baseline series. The cloud layer from Sentinel-2 is recorded as evidence in the screening rule rather than as truth.

Baseline flies a manned aircraft with a 4 band red, green, blue and near infrared large format camera, because the requirement excludes unmanned data outright. Its LiDAR is a Quality Level 1 sensor at a minimum 8 pulses per square meter, with the 16 pulse option priced separately and left exercisable. The positioning entry is the one that decides whether the deliverable is QL1 at all: GNSS guidance with network RTK or an owned base station, specified by baselines, correction source and test evidence, because that chain is what the accuracy claim rests on.

Field Ledger installs no sensing whatsoever. It reads the operator's existing sensor devices, read only, no cameras, no new field hardware. The world is sensed by farm rather than watched.

Three systems in one sector, and the sensing ranges from four satellite and aerial sources to none at all. That range is the argument. Sensing is a requirements decision.

## The license is a design constraint, not paperwork

Fodder Watch has an entry that explains itself in one line: RF-DETR XL and 2XL, under Roboflow's Platform Model License, excluded. The reason is that field of use terms would compromise in Kingdom weight ownership.

That is a checkpoint rejected for its license while the smaller checkpoint under Apache 2.0 was kept. If the model had been chosen first and the sovereignty requirement read later, the design would have had to be rebuilt around a constraint it could have honored on day one.

## Where renting is not an option at any price

Fodder Watch needs one 48 GB PCIe card, L40S class, chosen by a footprint rule: the combined weights come to under 0.55 GB, which leaves batch and cache headroom. Owning that node costs about 15,200 dollars over three years, in a range of 14,600 to 15,800 once support at 8 to 12 percent a year and power at a PUE of 1.6 on the Saudi industrial tariff are counted. Renting the same card on demand in the nearest AWS region is about 60,000 dollars over the same three years, and 22,600 dollars on the deepest three year EC2 Instance Savings Plan, all upfront.

Owning wins on money here. But the line that matters in the appendix is the qualifier attached to every rental row: outside the Kingdom. For a service whose whole purpose is that detections stay sovereign, the cheapest cloud number is not a competing option. It is a measurement of what the requirement already ruled out.

## The order the designs actually follow

Read across the three and one order falls out. What the law and the operator permit you to sense. What revisit and resolution that sensing gives you. What objects those readings have to become for the question to be answerable. Only then, whether a learned model is needed at all, and only then, under what license and on whose hardware it runs.

The model is the fourth decision, and twice out of three it turns out not to be a decision at all.

---

*The three designs, their object models as JSON, their model registers and their sourced cost appendices are free to reuse under CC BY 4.0: [Field Ledger](https://codeatoms.ai/farm-data-dashboard-pakistan/), [Baseline](https://codeatoms.ai/vegetation-mapping-lidar-us/), [Fodder Watch](https://codeatoms.ai/restricted-crop-monitoring-saudi-arabia/). All three were designed on [CodeNinja Praxis](https://codeatoms.ai/praxis/) and their object models import into [Hyper Ontology](https://codeatoms.ai/hyper-ontology/). Operations are described by class, never by name.*
