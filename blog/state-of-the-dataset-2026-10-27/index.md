# State of the Dataset: 27 October 2026

*Twenty three published designs, 317 ontology objects and 238 register rows, covering nine of thirteen sectors and fifteen of the thirty nine cells in the sector by country grid.*

Canonical: https://codeatoms.ai/blog/state-of-the-dataset-2026-10-27/
Author: CodeNinja Atoms, Research distribution
Published: 2026-10-27
License: CC BY 4.0
Publisher: CodeNinja Atoms (https://codeatoms.ai), a fully owned subsidiary of CodeNinja
This is the first weekly note on the open dataset behind CodeNinja Atoms. It goes out on Tuesdays. Every number below is computed from the published tables in the dataset folder of the repository (designs, objects, models and costs) and nothing else, so you can rerun the count yourself and get the same answer.

## What is in it

The dataset holds 23 designs. Each one is a complete reference architecture for putting intelligence into a physical operation on the operator's own hardware, reasoned on CodeNinja Praxis and published with a DOI. Together they carry 317 ontology objects joined by 295 typed links, 238 rows in the model and hardware register, and 203 cost lines.

Every design has register rows. Nineteen of the 23 carry cost lines.

The objects break down by kind as follows.

| Kind | Objects |
|---|---|
| asset | 93 |
| record | 79 |
| event | 37 |
| site | 23 |
| document | 20 |
| person | 20 |
| system | 14 |
| actor | 13 |
| measure | 13 |
| material | 5 |

Assets and records make up more than half of all objects. That is what a working operation looks like when you write it down: the things it owns and the paper trail they leave. You can browse every object model on the [industrial ontology examples](https://codeatoms.ai/industrial-ontology-examples/) page, and every design as one row on [sovereign AI reference architectures](https://codeatoms.ai/sovereign-ai-reference-architectures/).

## Coverage against the grid

The goal is thirteen sectors in three countries, Pakistan, Saudi Arabia and the United States, which is 39 cells. Today the designs touch 9 of the 13 sectors and fill 15 of the 39 cells.

By country, 12 designs are in the United States, 6 in Pakistan and 4 in Saudi Arabia. One more design is in Germany, a fourth country that sits outside the grid, so 22 designs count toward it.

Two sectors are covered in all three countries: agriculture and earth observation, and energy and utilities.

| Sector | Pakistan | Saudi Arabia | United States |
|---|---|---|---|
| Agriculture and earth observation | 1 | 1 | 1 |
| Aviation and aerospace manufacturing | 0 | 0 | 1 |
| Defense and intelligence | 0 | 0 | 0 |
| Discrete manufacturing and automotive | 0 | 0 | 2 |
| Energy and utilities | 1 | 1 | 2 |
| Heavy industry and construction | 1 | 2 | 0 |
| Maritime and ports | 0 | 0 | 2 |
| Mining | 0 | 0 | 0 |
| Oil and gas | 3 | 0 | 1 |
| Rail and transportation | 0 | 0 | 2 |
| Semiconductors | 0 | 0 | 0 |
| Supply chain and logistics | 0 | 0 | 0 |
| Warehousing and intralogistics | 0 | 0 | 1 |

## What is still empty

Four sectors have no design at all: defense and intelligence, mining, semiconductors, and supply chain and logistics. That is 12 empty cells.

Another 12 cells are empty inside sectors that already have at least one design:

- Aviation and aerospace manufacturing in Pakistan and Saudi Arabia
- Discrete manufacturing and automotive in Pakistan and Saudi Arabia
- Heavy industry and construction in the United States
- Maritime and ports in Pakistan and Saudi Arabia
- Oil and gas in Saudi Arabia
- Rail and transportation in Pakistan and Saudi Arabia
- Warehousing and intralogistics in Pakistan and Saudi Arabia

Saudi Arabia is the thinnest column with 10 of the 24 empty cells, Pakistan has 9 and the United States 5. In five sectors a United States design exists and its Pakistan and Saudi Arabia siblings do not yet, so the fastest way to fill the grid is to carry those five designs into the other two countries.

## New this week

Five designs joined the dataset in the last seven days.

| Design | Sector | Country | Objects | Links | Models |
|---|---|---|---|---|---|
| [Warehouse Twin Command](https://codeatoms.ai/warehouse-digital-twin-us/) | warehousing and intralogistics | United States | 14 | 14 | 5 |
| [Pipeline Integrity Watch](https://codeatoms.ai/pipeline-integrity-gas-transmission-us/) | oil and gas | United States | 14 | 13 | 4 |
| [Wayside Trend Watch](https://codeatoms.ai/wayside-detector-trending-rail-us/) | rail and transportation | United States | 14 | 13 | 4 |
| [Depot Operating Object Model](https://codeatoms.ai/factory-ontology-rebuild-depot-us/) | discrete manufacturing and automotive | United States | 14 | 13 | 3 |
| [Port Drone Watch](https://codeatoms.ai/drone-detection-dispatch-port-germany/) | maritime and ports | Germany | 15 | 14 | 5 |

Warehouse Twin Command opened a new sector for the grid. The other four added depth to sectors that already had a design.

## How to use it

The tables are on Hugging Face as the dataset CodeNinjatools/vertical-driven-architectures, with one config per table: designs, objects, models, costs and fulltext. Load the objects config and filter by kind or by design to get a ready object model for your own sector.

To cite the dataset across all versions, use the Zenodo concept DOI https://doi.org/10.5281/zenodo.23160819. Monthly snapshots carry their own DOI; the Hugging Face tables update between releases.

Every object model is also published as a package in the hyper-ontology/1 format, the input format for Hyper Ontology. Each object has an id, a label, a kind, the system of record it is anchored in, its properties, its status vocabulary and its typed, directed links. The hyper-ontology loader in the repository loads, validates and converts a package to Mermaid, Cypher or JSON-LD.

If you work through a coding agent, add the CodeNinja Atoms MCP server. It reads the published dataset at call time and gives the agent five tools: list designs by sector and country, get one design with its object model, register and cost lines, read the full paper, find where a model or regulation appears across designs, and learn where the designs come from. Install instructions are on the [developer page](https://codeatoms.ai/developer/).

Everything is CC BY 4.0. Next Tuesday's note will show which of the 24 empty cells filled.
