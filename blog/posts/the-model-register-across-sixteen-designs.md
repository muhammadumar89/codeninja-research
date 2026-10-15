---
{
 "title": "The Model Register Across Sixteen Designs",
 "subtitle": "Sixteen open reference architectures for physical operations, each with a model register the operator owns outright. Twelve models, four empty registers by decision, and one licence pattern that repeats in every design.",
 "author": "CodeNinja Atoms",
 "author_role": "Research distribution",
 "author_url": "https://codeatoms.ai/about/",
 "date": "2026-10-13",
 "tags": [
  "Engineering",
  "Models",
  "Sovereign AI"
 ],
 "audience": "For engineers and their coding agents choosing models for a physical AI system, who want to see what sixteen published designs chose, under which licence, and why.",
 "description": "Every model the sixteen published reference architectures chose, by name and licence: GLM 5.3 and GLM 5.2 as reasoning models, RF-DETR and D-FINE as detectors, Chronos-2, Chronos-Bolt and Granite TTM-R2 as forecasters, BGE-M3 and Qwen3-Embedding-0.6B for retrieval, PaddleOCR-VL for document parsing, Anomalib for anomaly detection, plus the four designs whose register is empty by decision.",
 "cluster": "model names"
}
---

A model register is the part of a system design that names every learned component the operation will run, with its licence, its size and the reason it was chosen over the alternatives. Sixteen open reference architectures on this site carry one, and every row of every register is in the public dataset as `models.jsonl`. This note lines them up.

Two things stand out before the table. Four of the sixteen designs have an empty register, and in each case the emptiness is a decision the paper defends rather than a gap. And no design holds a model under a licence with a field of use restriction, a revenue trigger or a copyleft clause that would reach the operator's own code. Weight ownership is the rule the whole corpus runs on.

## The reasoning models

Five designs put a frontier class open weight model behind a work surface for the operation's own people and agents. All five chose a GLM model from the same family, self hosted at FP8 on one node of eight 141 GB HBM class GPUs, and the register says why in licence terms.

| Model | Licence | Designs that chose it | The reason the register gives |
|---|---|---|---|
| GLM 5.3, 753B mixture of experts, FP8 | Bespoke licence permitting internal commercial use with attribution and no revenue trigger | [Sovereign HSE Watch](https://codeatoms.ai/sovereign-hse-pakistan/), [Steel Count Ledger](https://codeatoms.ai/steel-production-count-pakistan/), [Terminal Pulse](https://codeatoms.ai/truck-turn-container-terminal-us/) | Strongest open agentic model; purely internal use is exempt from the model as a service security review trigger; 904 GB of weights against one node of 1,128 GB leaves KV headroom |
| GLM 5.2, 753B, FP8, 1M context | MIT | [Grid Context Watch](https://codeatoms.ai/ot-security-cip-evidence-us/), [Feeder Firewatch](https://codeatoms.ai/wildfire-risk-distribution-us/) | A plain MIT licence with no revenue trigger or security review clause; one node holds it |

The split is not an accident. Where the operator wanted the strongest agentic behaviour, the design accepted a bespoke licence whose internal use carve out it had read. Where the operator was a utility or a cooperative with an auditor behind it, the design took the one generation older model under MIT and gave up nothing it needed.

## The detectors and trackers

Among the designs that watch with cameras, five chose the same detector.

| Model | Licence | Designs that chose it | The reason the register gives |
|---|---|---|---|
| RF-DETR, Nano to Large checkpoints, BF16, about 61 to 68 MB at 16 bit | Apache 2.0 | [Sovereign HSE Watch](https://codeatoms.ai/sovereign-hse-pakistan/), [Steel Count Ledger](https://codeatoms.ai/steel-production-count-pakistan/), [Feeder Firewatch](https://codeatoms.ai/wildfire-risk-distribution-us/), [Terminal Pulse](https://codeatoms.ai/truck-turn-container-terminal-us/), [Fodder Watch](https://codeatoms.ai/restricted-crop-monitoring-saudi-arabia/) | The practical sovereign answer to the AGPL gate; fine tuned on the operator's own footage; the operator owns and hardens the weights. Two designs exclude the XL and 2XL checkpoints because they sit under a platform licence whose field of use terms would compromise weight ownership |
| D-FINE, N to X tiers, BF16 | Apache 2.0 | [Pit Camera Watch](https://codeatoms.ai/test-site-camera-monitoring-us/) | An unconditional licence; the N through L tiers fit one 48 GB card; ahead of DEIM on matched compute |
| Roboflow trackers, ByteTrack and OC-SORT class | Apache 2.0 | [Sovereign HSE Watch](https://codeatoms.ai/sovereign-hse-pakistan/), [Structure Phase Watch](https://codeatoms.ai/structure-phase-construction-saudi-arabia/), [Steel Count Ledger](https://codeatoms.ai/steel-production-count-pakistan/) | Stable identity across frames without reintroducing copyleft after an Apache detector; one billet crossing two camera fields counts once |
| Anomalib 2.7.0, FP32, exported to ONNX Runtime | Apache 2.0 | [Hangar Form Cell](https://codeatoms.ai/dieless-sheet-metal-cell-aerospace-mro-us/) | Unsupervised fit on the facility's own good panels needs no labelled defect set |

The pattern a developer should copy is the pairing: an Apache detector followed by an Apache tracker. The register in three designs says in so many words that the tracker was chosen so that the AGPL exposure of the better known tracking collections never enters the serving path.

## The forecasters

| Model | Licence | Designs that chose it | The reason the register gives |
|---|---|---|---|
| Chronos-2, about 120M parameters, about 0.48 GB at FP32 | Apache 2.0 | [Sovereign HSE Watch](https://codeatoms.ai/sovereign-hse-pakistan/), [Terminal Pulse](https://codeatoms.ai/truck-turn-container-terminal-us/), [Fodder Watch](https://codeatoms.ai/restricted-crop-monitoring-saudi-arabia/) | Zero shot multivariate forecasting with covariates and no field of use restriction; thousands of independent per parcel series with no fine tuning dependency |
| Chronos-Bolt | Apache 2.0 | [Hangar Form Cell](https://codeatoms.ai/dieless-sheet-metal-cell-aerospace-mro-us/) | Learns per arm, per stylus load baselines on the edge box and flags drifting pass signatures |
| IBM Granite Tiny Time Mixers TTM-R2, about 0.85M parameters, FP32, about 0.003 GB | Apache 2.0 | [Factory Fire Watch](https://codeatoms.ai/factory-fire-monitoring-saudi-arabia/) | A CPU only forecaster inside the operator's existing platform; the requirement asked for no server or GPU, so none was deployed |

The Granite row is the one to notice. The design covers a hundred factories and runs its forecaster on the CPU the operator already has, because a model of under a million parameters was enough and the requirement forbade buying compute.

## Retrieval and document parsing

| Model | Licence | Designs that chose it | The reason the register gives |
|---|---|---|---|
| BGE-M3, 568M parameters, FP16 | MIT | [Sovereign HSE Watch](https://codeatoms.ai/sovereign-hse-pakistan/), [Port Twin](https://codeatoms.ai/port-digital-twin-us/), [Structure Phase Watch](https://codeatoms.ai/structure-phase-construction-saudi-arabia/) | Dense plus sparse plus multi vector retrieval in one pass with an 8,192 token window; multilingual retrieval across a workforce tagged by language; in the port design it is the only model in the register |
| Qwen3-Embedding-0.6B, 32K window, about 1.2 GB at BF16 | Apache 2.0 | [Grid Context Watch](https://codeatoms.ai/ot-security-cip-evidence-us/), [Terminal Pulse](https://codeatoms.ai/truck-turn-container-terminal-us/) | Whole playbooks, CIP procedures or a whole shift's gate record retrieve as single passages; runs beside the frontier model |
| PaddleOCR-VL 1.6, about 0.9B parameters, BF16 | Apache 2.0 | [Sovereign HSE Watch](https://codeatoms.ai/sovereign-hse-pakistan/), [Corridor Guard](https://codeatoms.ai/dc-interference-gas-pipelines-pakistan/) | Strong on degraded multilingual scans; no user or revenue threshold; digitises a scanned package with human reconciliation before any value enters the record |

The choice between the two embedders is a window question. BGE-M3 wins where the corpus is drawings, inspections and messages in several languages. Qwen3-Embedding-0.6B wins where a single document, a procedure or a shift log, must retrieve whole, and its 32K window makes that possible.

## The four empty registers

| Design | What the register says | Why |
|---|---|---|
| [Reliability Atlas](https://codeatoms.ai/plant-reliability-assessment-saudi-arabia/) | None: the register is empty by design | No inference workload is contracted; the deliverable is the study, and an empty register recorded plainly outranks a speculative entry |
| [Loop Integrity Watch](https://codeatoms.ai/tank-gauge-integrity-pakistan/) | Zero entries; all integrity logic is deterministic thresholds and rules | The failure modes are physical and protocol level, so no learned model is needed, no weights are held and no licence question arises |
| [Field Ledger](https://codeatoms.ai/farm-data-dashboard-pakistan/) | Zero models committed; a forecaster over sensor time series stays open work gated on the first milestone's evidence | The requirement commits aggregations, drill down and reporting, and no model was verified for this run |
| [Baseline](https://codeatoms.ai/vegetation-mapping-lidar-us/) | None; the register is empty by decision | No agent or model layer was wanted; analysis stays with the operator's own staff in their own tools |

A quarter of the designs needed no learned model at all. Each of those papers still carries the register, with its emptiness and the reason written down, because a reader deciding whether to copy the design needs to know that the absence was chosen.

## The licence pattern

Across the twelve named models the licences are Apache 2.0 (nine models), MIT (two) and one bespoke licence read for its internal use carve out. Three things never appear: a field of use restriction on a model the operator fine tunes, a revenue or user threshold, and a copyleft licence in the serving path. Where a stronger checkpoint existed under a platform licence, the register excludes it by name and says why.

That is the whole method. Choose the model for the job, read the licence as carefully as the benchmark, and write the reason down where the next engineer will find it.

## Use the register

The rows behind this note are the `models.jsonl` file of the [Vertical-Driven Architectures dataset](https://huggingface.co/datasets/CodeNinjatools/vertical-driven-architectures), one row per choice with the design, the choice, what was picked and why. The same file is served live by the [codeninja-research MCP server](https://github.com/muhammadumar89/codeninja-research/tree/main/mcp-server), so a coding agent can ask which designs chose a given model and read the reason. Every design named above was reasoned on [CodeNinja Praxis](https://codeatoms.ai/praxis/) and its object model imports into [Hyper Ontology](https://codeatoms.ai/hyper-ontology/).

## About CodeNinja

CodeNinja is a Middle Eastern-American artificial intelligence lab focused on building self-improving systems. We are reinventing knowledge work to close the loop between vertical AI use cases and the generalized intelligence that fuels it, accelerating the path toward organizational superintelligence.
