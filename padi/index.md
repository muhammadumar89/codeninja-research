# Physical AI Design Index (PADI)

Canonical: https://codeatoms.ai/padi/
Publisher: CodeNinja Atoms (https://codeatoms.ai)

When a customer sends a short requirement for physical AI in a real operation, does the design name the rules that bind in that country, flag what the requirement leaves out, and stay clear of invented specifics? PADI scores the same model twice, bare and inside Praxis, on tasks neither has seen, across 13 industries in three countries.

PADI is the benchmark CodeNinja uses to improve Praxis release by release. Scores are far from saturated: the goal is every check on every task in all 13 industries, and the best cycle so far passes under half. We publish the trajectory as it is, including the cycles where the bare model scored higher.

Latest cycle 16 (2026-10-07): Praxis platform 36.5%, bare model 26.0% of checks passed.
All 5 cycles: Praxis platform 37.7%, bare model 34.6% over 546 checks per arm.
Industries measured: 10 of 13.

## Industries

| Industry | Praxis platform | Bare model | Cycles |
|---|---|---|---|
| Agriculture and Earth Observation | 35.0% | 40.0% | 14 |
| Aviation Manufacturing | not yet measured | not yet measured | |
| Defense and Intelligence | 48.6% | 35.1% | 13, 15 |
| Discrete Manufacturing and Automotive | 32.4% | 32.4% | 13, 15 |
| Energy and Utilities | 27.6% | 34.2% | 13 |
| Heavy Industry and Construction | 44.6% | 46.4% | 12 |
| Maritime and Ports | 33.3% | 26.7% | 12, 16 |
| Mining | 46.2% | 40.7% | 14, 15, 16 |
| Oil and Gas | 28.2% | 25.6% | 14 |
| Rail Transport | 41.6% | 35.1% | 14, 15, 16 |
| Semiconductors | not yet measured | not yet measured | |
| Supply Chain and Logistics | 34.2% | 26.3% | 15, 16 |
| Warehousing and Intralogistics | not yet measured | not yet measured | |

## Results by cycle

| Cycle | Date | Tasks | Praxis platform | Bare model | Rubric |
|---|---|---|---|---|---|
| 12 | 2026-10-03 | 6 | 37.5% | 38.4% | 0.1 |
| 13 | 2026-10-04 | 6 | 29.5% | 32.1% | 0.2 |
| 14 | 2026-10-05 | 6 | 43.2% | 39.6% | 0.2 |
| 15 | 2026-10-05 | 6 | 41.7% | 35.7% | 0.2 |
| 16 | 2026-10-07 | 5 | 36.5% | 26.0% | 0.2 |

Different tasks each cycle, so cycles are not like for like.

## Methodology

- Arms: the bare model and the same model inside Praxis, both glm-5.3-flash, on the same pack and instruction.
- Judge: glm-4.6 through three lenses (strict reviewer, plant engineer, regulator's technical assessor); a check passes on a majority yes.
- Families: must name, must flag, must never.
- Fresh tasks: 17 of 60 tasks held out for a final blind evaluation; no task is run twice.
- Score: checks passed divided by checks total, per arm, no partial credit.

## Limitations

- **Design judgement, not deployment.** PADI scores designs on paper. No plant, sensor or model was run.
- **One judge model.** A single model reads every design through three lenses. Judging the same text again can move a few checks. No human has scored the outputs yet.
- **Small samples.** Each cycle is five or six tasks and roughly a hundred checks per arm. A swing of a few points is within noise, so no single cycle is a trend.
- **Different tasks every cycle.** Fresh tasks keep the measure honest, and they also mean cycles are not like for like.
- **Written by CodeNinja.** Tasks and checks were written by CodeNinja with model assistance and reviewed adversarially. Independent expert grading is planned and not yet done.
- **Two arms.** Only the bare model and the same model inside Praxis are scored. No other system or model is in the index yet.
- **Partial coverage.** Ten of thirteen industries are measured. Aviation manufacturing, semiconductors and warehousing have not been run.
- **One rubric change.** Cycle 12 used rubric 0.1. Every later cycle uses 0.2.

## Questions

### What is the Physical AI Design Index?

PADI is CodeNinja's benchmark for design judgement in physical AI. Each task is a short anonymised requirement for an AI system in a real kind of operation, such as a mine, a port, a rail line or a substation, plus yes or no checks. A judge model scores the design from the bare model and from the same model inside the Praxis platform.

### What does PADI measure?

Three families of checks: what a design must name (the regulation that binds in that country, the systems it reads, where things run, which decisions a person confirms, what phase one must prove), what it must flag (a missing fact asked as a question, a foreign rule that does not apply), and what it must never do (a part number, an invented regulation or saving, a customer name, data leaving the site when residency forbids it).

### How is PADI scored?

Checks passed divided by checks total, for each arm, with no partial credit and no weighting. The judge is glm-4.6 through three lenses (a strict reviewer, a plant engineer and a regulator's technical assessor); a check passes when the majority say yes. Both arms use glm-5.3-flash.

### How often is PADI updated?

Once per Praxis release cycle, on tasks never run before. A third of the task bank is held out for a final blind evaluation and never run in a cycle.

Updated each Praxis release cycle. Last published: cycle 16, 2026-10-07. Cycle 17 is under way.
