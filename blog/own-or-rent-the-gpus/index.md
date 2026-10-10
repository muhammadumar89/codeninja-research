# Own or Rent the GPUs

*Seven published reference architectures, priced the same way, say owning the reasoning node costs between about half and nearly all of the deepest three year cloud commitment. Not a tenth.*

Canonical: https://codeatoms.ai/blog/own-or-rent-the-gpus/
Author: CodeNinja Atoms, Research distribution
Published: 2026-10-10
License: CC BY 4.0
Publisher: CodeNinja Atoms (https://codeatoms.ai), a fully owned subsidiary of CodeNinja
Every vendor page on this question answers it in the abstract. Utilization curves, break even hours, a worked example with four A100s. The honest version needs real systems with real sizing, priced the same way, and published so the arithmetic can be checked.

We have seven. Each is an open reference architecture for a physical operation, each carries a cost appendix computed from its own sizing with public prices cited by URL and date, and each is free to reuse under CC BY 4.0. This is what they say when you line them up.

## The number

| Design | Operation | Owned, 3 years | Cheapest 3 year rental | Owned as a share |
|---|---|---|---|---|
| [Structure Phase Watch](https://codeatoms.ai/structure-phase-construction-saudi-arabia/) | Construction site, Saudi Arabia | 642,000 | 1.41m (Oracle) | 46% |
| [Sovereign HSE Watch](https://codeatoms.ai/sovereign-hse-pakistan/) | Oil and gas, Pakistan | 670,000 | 1.14m (AWS) | 59% |
| [Fodder Watch](https://codeatoms.ai/restricted-crop-monitoring-saudi-arabia/) | Earth observation, Saudi Arabia | 15,200 | 22,600 (AWS) | 67% |
| [Terminal Pulse](https://codeatoms.ai/truck-turn-container-terminal-us/) | Container terminal, United States | 722,000 | 990,000 (AWS) | 73% |
| [Grid Context Watch](https://codeatoms.ai/ot-security-cip-evidence-us/) | Electric utility, United States | 510,000 | 630,000 (AWS) | 81% |
| [Feeder Firewatch](https://codeatoms.ai/wildfire-risk-distribution-us/) | Distribution feeders, United States | 841,000 | 880,000 (AWS) | 96% |

Owning wins in all six. It wins by between a factor of two and almost nothing.

Two caveats belong in the table rather than under it. The AWS figures are the deepest three year EC2 Instance Savings Plan, all upfront, taken from the region's price file on the day the appendix was written, which is the hardest number for ownership to beat. Structure Phase Watch has no AWS three year row in its appendix, so its 46% is measured against Oracle's three year commitment and is not strictly comparable with the rest.

## Where owning stops being obvious

Feeder Firewatch is the interesting row. Owning costs 841,000 dollars against 880,000 to rent: a 4% margin, which is inside the error bars of any hardware quote. The owned total there carries 252,000 dollars of edge devices spread across distribution feeders, and the support line runs 137,000 to 242,000 over three years. Move either and the answer flips.

The general shape: the more of the system that lives outside the data center, the weaker the ownership case gets, because edge hardware depreciates on someone else's schedule and carries its own support contract. The ownership argument is strongest for a single reasoning node that runs hot and is cheap to keep.

What none of these rows measure is the reason most of these operators chose to own anyway. Four of the seven move data that cannot leave a jurisdiction or a security perimeter. For those, the rental column is not a price, it is a non option, and the comparison is a sanity check rather than a decision.

## The design where the question is wrong

The seventh design does not fit the table, and that is the useful part.

[Steel Count Ledger](https://codeatoms.ai/steel-production-count-pakistan/) costs 4,445,000 dollars to own over three years against 750,000 to rent the frontier node. Six times more expensive. Except that is not a like for like comparison, and printing it as a ratio would be dishonest: 2,832,000 of the owned total is 300 counting kits at 9,441 dollars each, installed at the mills. The rental figure covers the reasoning node alone.

Strip the sensing estate and the node is 320,000 to 420,000 dollars, and Steel Count Ledger lands with the others. The real finding is that for this design the own or rent question is a rounding error. The money is in cameras on gantries, and no cloud commitment changes that.

This is the trap in every generic own versus rent guide. They price a GPU decision for systems whose cost is not a GPU decision. Before reaching for the utilization curve, check what fraction of the three year total is actually compute. In Steel Count Ledger it is 36%. In Feeder Firewatch, the row where ownership barely wins, hardware outside the data center is 30% of the total. In the other five it runs from zero to 21%, and those are the five where the own or rent arithmetic decides anything.

## How to check this

Everything above comes from `costs.jsonl` in the published dataset, which has 102 cost lines across the designs, each with its basis and its three year figure:

```bash
curl -s https://huggingface.co/datasets/CodeNinjatools/vertical-driven-architectures/resolve/main/costs.jsonl \
  | jq -r 'select(.line=="Total") | [.design_id, .three_year_usd] | @tsv'
```

The per design appendices carry the sourced prices with their URLs and dates. If a number looks wrong, the appendix shows where it came from and the design it was computed for.

## What we are not claiming

We are not claiming owning is cheaper in general. These seven systems are frontier model reasoning nodes sized from open weights, running continuously for an operation that cannot pause, in three countries, priced in 2026. Change the model, the duty cycle or the year and the table changes. A system that runs a model for two hours a day should rent.

We are also not claiming the spread is precise. The owned totals are typical values inside ranges that run 20 to 30% wide, because server pricing is negotiated and support is quoted per customer. The ranges are in each appendix.

The claim is narrower and, we think, more useful than the usual one: for a continuously running frontier reasoning node in a physical operation, owning lands somewhere between half and nearly all of the deepest cloud commitment, and the decision is usually settled by what else is in the system rather than by the GPUs.

---

Each design links to its paper, its object model as JSON, its model register and a Zenodo DOI. The full set is at [codeatoms.ai](https://codeatoms.ai/), and the dataset behind this post is on [Hugging Face](https://huggingface.co/datasets/CodeNinjatools/vertical-driven-architectures). If you run a physical operation and want one of these built for it, the [co-build pages](https://codeatoms.ai/co-build/) say what we bring and what you bring.

## About CodeNinja

CodeNinja is a Middle Eastern-American artificial intelligence lab focused on building self-improving systems. We are reinventing knowledge work to close the loop between vertical AI use cases and the generalized intelligence that fuels it, accelerating the path toward organizational superintelligence.
