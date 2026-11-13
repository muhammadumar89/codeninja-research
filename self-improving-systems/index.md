# Self-improving systems

Canonical: https://codeatoms.ai/self-improving-systems/
License: CC BY 4.0
Publisher: CodeNinja Atoms (https://codeatoms.ai)

A self-improving system is a system that measures its own output, finds where it fell short, and changes itself so the next round does better, without a person rewriting it each time. In AI the safest form improves the system's context (its documents, models of the domain, rules and records of past gaps) rather than its weights, so every change can be read and reverted. CodeNinja runs Praxis this way and publishes each loop's results in the open: 10 RSI loops so far, the latest at 54.4% of checks passed against frontier AI on its own at 37.7%.

## How self-improving systems work

1. **Measure on fresh tasks.** Every loop starts with tasks the system has not seen, scored the same way for the system and for a baseline, so a gain is a gain and not memory.
2. **Find the gaps.** Each failed check becomes a written gap: what was missing, where, and what would have fixed it.
3. **Improve the context, not the weights.** The fixes land in what the system reasons with (documents, object models, registers, rules), so every change is readable and can be reverted.
4. **Measure again, blind.** The next loop is scored on new tasks, and a held out blind set checks that the improvement carries to work the system never saw.

- [Self-improving AI system](https://codeatoms.ai/self-improving-ai-system/): Praxis loop by loop
- [PADI](https://codeatoms.ai/padi/): the benchmark
