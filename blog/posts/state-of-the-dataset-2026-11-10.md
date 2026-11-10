---
{
 "title": "State of the Dataset: 10 November 2026",
 "subtitle": "Forty four published designs, 643 ontology objects and 565 register rows, covering twelve of thirteen sectors and twenty seven of the thirty nine cells in the sector by country grid.",
 "author": "CodeNinja Atoms",
 "author_role": "Research distribution",
 "author_url": "https://codeatoms.ai/about/",
 "date": "2026-11-10",
 "tags": [
  "Engineering",
  "Ontologies",
  "Dataset"
 ],
 "audience": "For engineers and their coding agents who build on the open dataset of physical AI system designs and want to know what is in it this week, what is new and where the gaps are.",
 "description": "Weekly dataset note: 44 designs, 643 ontology objects, 565 register rows, 12 of 13 sectors, 16 new designs and the 12 cells still empty.",
 "cover_line": "Weekly note on the open dataset",
 "cluster": "dataset",
 "owned_keyword": "ontologies"
}
---

This is the third weekly note on the open dataset behind CodeNinja Atoms. It goes out on Tuesdays. Every number below is computed from the published tables in the dataset folder of the repository (designs, objects, models and costs) and nothing else, so you can rerun the count yourself and get the same answer.

## What is in it

The dataset holds 44 designs, sixteen more than last Tuesday. It is the biggest week so far. Each design is a complete reference architecture for putting intelligence into a physical operation on the operator's own hardware, reasoned on CodeNinja Praxis and published with a DOI. Together they carry 643 ontology objects joined by 560 typed links, 565 rows in the model and hardware register, and 384 cost lines.

Every design has register rows. Forty of the 44 carry cost lines; all sixteen new designs do.

The objects break down by kind as follows.

| Kind | Objects | Last week |
|---|---|---|
| record | 180 | 98 |
| asset | 155 | 112 |
| event | 90 | 50 |
| actor | 47 | 24 |
| site | 46 | 30 |
| measure | 38 | 20 |
| document | 35 | 22 |
| person | 20 | 20 |
| system | 16 | 14 |
| material | 15 | 7 |
| vocabulary | 1 | 0 |

Records overtook assets this week, 180 to 155. The new designs are mostly about what happens to things (a declaration that stalls, a weld that fails, a carrier exception, a water allocation) rather than the things themselves, and each of those leaves a record. Actors roughly doubled again, from 24 to 47, because every new design names the desk or role that approves each action. What an [industrial data ontology](https://codeatoms.ai/industrial-data-ontology/) holds, kind by kind, is read from all 44 object models on its own page.

## Coverage against the grid

The goal is thirteen sectors in three countries, Pakistan, Saudi Arabia and the United States, which is 39 cells. Today the designs touch 12 of the 13 sectors and fill 27 of the 39 cells, up from 11 sectors and 18 cells.

By country, 19 designs are in the United States, 13 in Saudi Arabia and 11 in Pakistan. One more design is in Germany, a fourth country outside the grid, so 43 designs count toward it.

Three sectors are now covered in all three countries: agriculture and earth observation, energy and utilities, and mining. Energy and utilities is still the deepest sector, with eight designs.

| Sector | Pakistan | Saudi Arabia | United States |
|---|---|---|---|
| Agriculture and earth observation | 2 | 1 | 1 |
| Aviation and aerospace manufacturing | 0 | 1 | 2 |
| Defense and intelligence | 0 | 0 | 0 |
| Discrete manufacturing and automotive | 1 | 0 | 2 |
| Energy and utilities | 2 | 2 | 4 |
| Heavy industry and construction | 2 | 3 | 0 |
| Maritime and ports | 0 | 1 | 2 |
| Mining | 1 | 1 | 1 |
| Oil and gas | 3 | 0 | 1 |
| Rail and transportation | 0 | 1 | 2 |
| Semiconductors | 0 | 1 | 1 |
| Supply chain and logistics | 0 | 1 | 2 |
| Warehousing and intralogistics | 0 | 1 | 1 |

## What is still empty

Last week's note promised to show which of the 21 empty cells filled. Nine did: aviation in Saudi Arabia, discrete manufacturing in Pakistan, maritime and ports in Saudi Arabia, mining in Pakistan and the United States, rail in Saudi Arabia, warehousing in Saudi Arabia, and supply chain and logistics in Saudi Arabia and the United States. Supply chain and logistics went from no design at all to two countries in one week. That leaves 12.

One sector has no design at all: defense and intelligence, which is 3 empty cells.

The other 9 empty cells sit inside sectors that already have at least one design:

- Aviation and aerospace manufacturing in Pakistan
- Discrete manufacturing and automotive in Saudi Arabia
- Heavy industry and construction in the United States
- Maritime and ports in Pakistan
- Oil and gas in Saudi Arabia
- Rail and transportation in Pakistan
- Semiconductors in Pakistan
- Supply chain and logistics in Pakistan
- Warehousing and intralogistics in Pakistan

Pakistan is still the thinnest column, with 7 of the 12 empty cells; Saudi Arabia has 3 and the United States 2. Six of Pakistan's seven gaps are sectors where a Saudi or United States design already exists, so the shortest path to a full grid is carrying those designs into Pakistan.

## New this week

Sixteen designs joined the dataset in the last seven days, all dated 7 November.

| Design | Sector | Country | Objects | Links | Models |
|---|---|---|---|---|---|
| [Port Equipment and Berth Object Model](https://codeatoms.ai/port-equipment-berth-ontology-saudi-arabia/) | maritime and ports | Saudi Arabia | 16 | 13 | 17 |
| [Cold Chain From Plant to Store](https://codeatoms.ai/cold-chain-ontology-us/) | supply chain and logistics | United States | 16 | 13 | 20 |
| [Cement Kiln Control](https://codeatoms.ai/cement-kiln-control-saudi-arabia/) | heavy industry and construction | Saudi Arabia | 16 | 10 | 15 |
| [Passenger Rail Fleet Maintenance](https://codeatoms.ai/passenger-rail-fleet-saudi-arabia/) | rail and transportation | Saudi Arabia | 14 | 12 | 18 |
| [Freight Corridor and Customs Clearance](https://codeatoms.ai/freight-corridor-customs-saudi-arabia/) | supply chain and logistics | Saudi Arabia | 15 | 11 | 18 |
| [Distribution Loss and Theft Reduction](https://codeatoms.ai/distribution-loss-theft-pakistan/) | energy and utilities | Pakistan | 15 | 14 | 17 |
| [Composite Part Inspection in an Aviation MRO](https://codeatoms.ai/composite-part-inspection-mro-saudi-arabia/) | aviation and aerospace manufacturing | Saudi Arabia | 16 | 12 | 17 |
| [OT Vulnerability Management at a Utility](https://codeatoms.ai/ot-vulnerability-utility-us/) | energy and utilities | United States | 16 | 13 | 15 |
| [Tailings Storage Facility Monitoring](https://codeatoms.ai/tailings-monitoring-us/) | mining | United States | 15 | 12 | 17 |
| [Engine MRO Shop Floor](https://codeatoms.ai/engine-mro-shop-us/) | aviation and aerospace manufacturing | United States | 15 | 16 | 15 |
| [Fertilizer Plant Reliability](https://codeatoms.ai/fertilizer-plant-reliability-pakistan/) | heavy industry and construction | Pakistan | 14 | 10 | 19 |
| [Mobile Robot Fulfilment Centre](https://codeatoms.ai/mobile-robot-fulfilment-centre-saudi-arabia/) | warehousing and intralogistics | Saudi Arabia | 15 | 13 | 18 |
| [Remote Mine on a Satellite Link](https://codeatoms.ai/remote-mine-satellite-pakistan/) | mining | Pakistan | 15 | 13 | 16 |
| [Carrier Exception Handling](https://codeatoms.ai/carrier-exceptions-us/) | supply chain and logistics | United States | 16 | 13 | 19 |
| [Canal Irrigation Water Allocation](https://codeatoms.ai/canal-irrigation-pakistan/) | agriculture and earth observation | Pakistan | 16 | 13 | 15 |
| [Weld and Assembly Quality in a Vehicle Plant](https://codeatoms.ai/weld-assembly-quality-vehicle-plant-pakistan/) | discrete manufacturing and automotive | Pakistan | 16 | 12 | 19 |

The register grew faster than the object models this week: the sixteen new designs average about 17 register rows each, against about 10 for the first 28, because each one now lists every component it chose and the one it rejected beside it. Each new design is filed under the search term it answers, so the series also reads as worked examples of [sovereign AI reference architectures](https://codeatoms.ai/sovereign-ai-reference-architectures/), [industrial AI reference architecture](https://codeatoms.ai/industrial-ai-reference-architecture/), [physical AI system design](https://codeatoms.ai/physical-ai-system-design/) and the [self-improving AI system](https://codeatoms.ai/self-improving-ai-system/).

## Releases

The November snapshot on Zenodo, DOI https://doi.org/10.5281/zenodo.23889945, was cut on 1 November and carries the first 28 designs. The sixteen new designs are in the Hugging Face tables now and will be in the December snapshot. To cite the dataset across all versions, use the Zenodo concept DOI https://doi.org/10.5281/zenodo.23160819.

## How to use it

The tables are on Hugging Face as the dataset CodeNinjatools/vertical-driven-architectures, with one config per table: designs, objects, models, costs and fulltext. Load the objects config and filter by kind or by design to get a ready object model for your own sector.

Every object model is also published as a package in the hyper-ontology/1 format, the input format for Hyper Ontology. Each object has an id, a label, a kind, the system of record it is anchored in, its properties, its status vocabulary and its typed, directed links. The hyper-ontology loader in the repository loads, validates and converts a package to Mermaid, Cypher or JSON-LD.

If you work through a coding agent, add the CodeNinja Atoms MCP server. It reads the published dataset at call time, so the sixteen new designs are already in its answers. Install instructions are on the [developer page](https://codeatoms.ai/developer/).

Everything is CC BY 4.0. Next Tuesday's note will show which of the 12 empty cells filled.
