---
{
 "title": "State of the Dataset: 24 November 2026",
 "subtitle": "Forty four published designs, 643 ontology objects and 565 register rows, unchanged for seventeen days, while every one of the 45 DOIs is now indexed in OpenAlex and two designs were corrected in every copy.",
 "author": "CodeNinja Atoms",
 "author_role": "Research distribution",
 "author_url": "https://codeatoms.ai/about/",
 "date": "2026-11-24",
 "tags": [
  "Engineering",
  "Ontologies",
  "Dataset"
 ],
 "audience": "For engineers and their coding agents who build on the open dataset of physical AI system designs and want to know what is in it this week, what changed and where the gaps are.",
 "description": "Weekly dataset note: 44 designs, 643 ontology objects, 565 register rows, 27 of 39 grid cells, 45 of 45 DOIs in OpenAlex, two corrections.",
 "cover_photo": "plant.jpg",
 "cover_position": "center",
 "cover_credit": "Photo by Johannes Plenio on Pexels (https://www.pexels.com/photo/3105242/), Pexels License",
 "cover_line": "Weekly note on the open dataset",
 "cluster": "dataset",
 "owned_keyword": "ontologies"
}
---

This is the fourth note on the open dataset behind CodeNinja Atoms. It goes out on Tuesdays. The design, object, register and cost numbers below are computed from the published tables in the dataset folder of the repository and nothing else, so you can rerun the count yourself and get the same answer. The reach numbers come from the public Zenodo and OpenAlex APIs, read this morning.

## What is in it

The dataset holds 44 designs, the same 44 as on 10 November. The last design was dated 7 November, so the tables have not grown for seventeen days. Each design is a complete reference architecture for putting intelligence into a physical operation on the operator's own hardware, reasoned on CodeNinja Praxis and published with a DOI.

Together they carry 643 ontology objects joined by 560 typed links, 565 rows in the model and hardware register, and 384 cost lines. Every design has register rows, and 40 of the 44 carry cost lines.

| Kind | Objects |
|---|---|
| record | 180 |
| asset | 155 |
| event | 90 |
| actor | 47 |
| site | 46 |
| measure | 38 |
| document | 35 |
| person | 20 |
| system | 16 |
| material | 15 |
| vocabulary | 1 |

Records still lead assets, 180 to 155. Every object model in the table can be browsed object by object on the [industrial ontology examples](https://codeatoms.ai/industrial-ontology-examples/) page, and what [ontologies](https://codeatoms.ai/ontologies/) for physical operations are, and how these ones are built, is answered on its own page.

## What changed

Nothing was added, but two designs were corrected. In each, the description of the operator was narrowed back to its class, because the original wording combined enough detail to point at one company. The remote open pit mine in Pakistan now reads as a mining operator at a remote open pit mine in Pakistan, and the weld and assembly quality design now reads as a vehicle assembly plant in Pakistan. Each correction reached every copy the same day: the web edition, the Word and PDF files, the object model JSON, the fulltext and designs tables, the Hugging Face Space and datasets, and the sector and collection pages that quote the design. The architecture, the object model and the numbers did not change.

If you pulled fulltext.jsonl or a design's objects.json before 21 November, pull again.

## Who is reading it

All 45 DOIs behind the dataset, the 44 designs and the monthly release, are now indexed in OpenAlex, so the designs can be found and cited from the same graph as the papers they cite. Across the 45 Zenodo records there have been 1,023 views and 824 downloads since the first record went up on 3 October, 71 of those views in the last day.

## Coverage against the grid

The goal is thirteen sectors in three countries, Pakistan, Saudi Arabia and the United States, which is 39 cells. The designs touch 12 of the 13 sectors and fill 27 of the 39 cells, the same as two weeks ago. By country, 19 designs are in the United States, 13 in Saudi Arabia and 11 in Pakistan, with one more in Germany outside the grid.

The 12 empty cells are unchanged. Defense and intelligence has no design, which is 3 cells. The other 9 sit inside sectors that already have a design elsewhere:

- Aviation and aerospace manufacturing in Pakistan
- Discrete manufacturing and automotive in Saudi Arabia
- Heavy industry and construction in the United States
- Maritime and ports in Pakistan
- Oil and gas in Saudi Arabia
- Rail and transportation in Pakistan
- Semiconductors in Pakistan
- Supply chain and logistics in Pakistan
- Warehousing and intralogistics in Pakistan

Pakistan holds 7 of the 12. The next builds we would pick are maritime and ports in Pakistan or warehousing and intralogistics in Pakistan, then oil and gas in Saudi Arabia: each has a neighbour design in another country to carry across, and each fills a cell that no design touches today.

## Using it

The tables are newline delimited JSON, one row per design, object, register row, cost line or full text, and every row carries its design_id and DOI. The object models import into Hyper Ontology as hyper-ontology/1 JSON. Everything is CC BY 4.0. The full set is on Hugging Face as CodeNinjatools/vertical-driven-architectures and in the dataset folder of the repository, and each design's canonical page is on [codeatoms.ai](https://codeatoms.ai/).
