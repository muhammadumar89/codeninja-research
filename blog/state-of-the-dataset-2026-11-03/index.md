# State of the Dataset: 3 November 2026

*Twenty eight published designs, 397 ontology objects and 290 register rows, covering eleven of thirteen sectors and eighteen of the thirty nine cells in the sector by country grid.*

Canonical: https://codeatoms.ai/blog/state-of-the-dataset-2026-11-03/
Author: CodeNinja Atoms, Research distribution
Published: 2026-11-03
License: CC BY 4.0
Publisher: CodeNinja Atoms (https://codeatoms.ai), a fully owned subsidiary of CodeNinja
This is the second weekly note on the open dataset behind CodeNinja Atoms. It goes out on Tuesdays. Every number below is computed from the published tables in the dataset folder of the repository (designs, objects, models and costs) and nothing else, so you can rerun the count yourself and get the same answer.

## What is in it

The dataset holds 28 designs, five more than last Tuesday. Each one is a complete reference architecture for putting intelligence into a physical operation on the operator's own hardware, reasoned on CodeNinja Praxis and published with a DOI. Together they carry 397 ontology objects joined by 360 typed links, 290 rows in the model and hardware register, and 245 cost lines.

Every design has register rows. Twenty four of the 28 carry cost lines; all five new designs do.

The objects break down by kind as follows.

| Kind | Objects | Last week |
|---|---|---|
| asset | 112 | 93 |
| record | 98 | 79 |
| event | 50 | 37 |
| site | 30 | 23 |
| actor | 24 | 13 |
| document | 22 | 20 |
| person | 20 | 20 |
| measure | 20 | 13 |
| system | 14 | 14 |
| material | 7 | 5 |

Assets and records are still more than half of all objects, 210 of 397. Actors nearly doubled this week, from 13 to 24: the new designs write down the desks, crews and roles that act on the operation, not only the things it owns. What an [industrial data ontology](https://codeatoms.ai/industrial-data-ontology/) holds, kind by kind, now has its own page, read from all 28 object models.

## Coverage against the grid

The goal is thirteen sectors in three countries, Pakistan, Saudi Arabia and the United States, which is 39 cells. Today the designs touch 11 of the 13 sectors and fill 18 of the 39 cells, up from 9 sectors and 15 cells.

By country, 14 designs are in the United States, 7 in Saudi Arabia and 6 in Pakistan. One more design is in Germany, a fourth country that sits outside the grid, so 27 designs count toward it.

Two sectors are covered in all three countries: agriculture and earth observation, and energy and utilities. Energy and utilities is now the deepest sector, with six designs.

| Sector | Pakistan | Saudi Arabia | United States |
|---|---|---|---|
| Agriculture and earth observation | 1 | 1 | 1 |
| Aviation and aerospace manufacturing | 0 | 0 | 1 |
| Defense and intelligence | 0 | 0 | 0 |
| Discrete manufacturing and automotive | 0 | 0 | 2 |
| Energy and utilities | 1 | 2 | 3 |
| Heavy industry and construction | 1 | 2 | 0 |
| Maritime and ports | 0 | 0 | 2 |
| Mining | 0 | 1 | 0 |
| Oil and gas | 3 | 0 | 1 |
| Rail and transportation | 0 | 0 | 2 |
| Semiconductors | 0 | 1 | 1 |
| Supply chain and logistics | 0 | 0 | 0 |
| Warehousing and intralogistics | 0 | 0 | 1 |

## What is still empty

Last week's note promised to show which of the 24 empty cells filled. Three did: semiconductors in Saudi Arabia, semiconductors in the United States and mining in Saudi Arabia. That leaves 21.

Two sectors have no design at all: defense and intelligence, and supply chain and logistics. That is 6 empty cells.

Another 15 cells are empty inside sectors that already have at least one design:

- Aviation and aerospace manufacturing in Pakistan and Saudi Arabia
- Discrete manufacturing and automotive in Pakistan and Saudi Arabia
- Heavy industry and construction in the United States
- Maritime and ports in Pakistan and Saudi Arabia
- Mining in Pakistan and the United States
- Oil and gas in Saudi Arabia
- Rail and transportation in Pakistan and Saudi Arabia
- Semiconductors in Pakistan
- Warehousing and intralogistics in Pakistan and Saudi Arabia

Pakistan is now the thinnest column with 9 of the 21 empty cells, Saudi Arabia has 8 and the United States 4. The same five sectors still have a United States design and no Pakistan or Saudi Arabia sibling, so carrying those five designs into the other two countries would fill ten of the 21 cells.

## New this week

Five designs joined the dataset in the last seven days: Silicon Ledger on 27 October and four on 2 November.

| Design | Sector | Country | Objects | Links | Models |
|---|---|---|---|---|---|
| [Silicon Ledger](https://codeatoms.ai/chip-design-ontology-saudi-arabia/) | semiconductors | Saudi Arabia | 16 | 13 | 3 |
| [Grid Control Room](https://codeatoms.ai/grid-control-room-saudi-arabia/) | energy and utilities | Saudi Arabia | 16 | 13 | 2 |
| [Wafer Defect Inspection](https://codeatoms.ai/wafer-defect-inspection-us/) | semiconductors | United States | 16 | 12 | 2 |
| [Water Utility Ontology](https://codeatoms.ai/water-utility-ontology-us/) | energy and utilities | United States | 16 | 14 | 2 |
| [Open Pit Mine Haul Fleet](https://codeatoms.ai/open-pit-mine-haul-fleet-saudi-arabia/) | mining | Saudi Arabia | 16 | 13 | 4 |

Silicon Ledger and the haul fleet design opened two new sectors for the grid, semiconductors and mining. Wafer Defect Inspection filled the second semiconductors cell. The grid control room and the water utility added depth to energy and utilities. Each of the five is a worked example of [physical AI system design](https://codeatoms.ai/physical-ai-system-design/), from what the system senses to the person who approves each action.

## The November release

The monthly snapshot for November is out: all five tables as one Zenodo record, DOI https://doi.org/10.5281/zenodo.23889945. It is the first release that carries all 28 designs.

To cite the dataset across all versions, use the Zenodo concept DOI https://doi.org/10.5281/zenodo.23160819. Monthly snapshots carry their own DOI; the Hugging Face tables update between releases.

## How to use it

The tables are on Hugging Face as the dataset CodeNinjatools/vertical-driven-architectures, with one config per table: designs, objects, models, costs and fulltext. Load the objects config and filter by kind or by design to get a ready object model for your own sector.

Every object model is also published as a package in the hyper-ontology/1 format, the input format for Hyper Ontology. Each object has an id, a label, a kind, the system of record it is anchored in, its properties, its status vocabulary and its typed, directed links. The hyper-ontology loader in the repository loads, validates and converts a package to Mermaid, Cypher or JSON-LD.

If you work through a coding agent, add the CodeNinja Atoms MCP server. It reads the published dataset at call time, so the five new designs are already in its answers. Install instructions are on the [developer page](https://codeatoms.ai/developer/).

Everything is CC BY 4.0. Next Tuesday's note will show which of the 21 empty cells filled.
