# Agentic Memory Architecture

How Praxis keeps what it learns outside the model, so the reasoning can be replaced and the memory stands.

By Muhammad Umar, Cofounder, CodeNinja, October 23, 2026.
Canonical: https://codeatoms.ai/agentic-memory-architecture/
License: CC BY 4.0
Publisher: CodeNinja Atoms (https://codeatoms.ai)

## The model

Most memory systems for software agents treat memory as storage: write a sentence, fetch the same sentence later. Fidelity in, fidelity out. Praxis is built on a different model of memory, taken from the biologist Michael Levin's 2024 paper Self-Improvising Memory in Entropy.
Levin's claim is that living systems keep memory the way a bow tie is shaped.
Left wing. The high dimensional past: everything that happened, in full detail, in the body and the environment that existed then.
The waist. A narrow bottleneck the past must pass through to persist at all. The compression strips correlations and contingent detail. What survives the waist is not a record of the past but its salient pattern. Once the correlations are gone the stored pattern no longer resembles the experience that produced it, and it cannot be played back.
Right wing. A future self decodes the compressed pattern into whatever its present context needs. That self is never the one that wrote the memory. It has a different body, a different environment and different goals, so decoding is not retrieval. It is interpretation, and Levin is explicit that creative, adaptive confabulation is the feature that makes memory useful rather than the bug that makes it unreliable.

Three consequences follow, and all three matter for an engineering platform.
- Salience over fidelity. Evolution does not optimise memory for accurate replay. It optimises for what is still actionable later. A caterpillar's memory of where food was does not survive metamorphosis as a map; it survives as a relationship that a butterfly with a rebuilt brain can act on.- Memories are messages between agents separated across time. The writer cannot know the reader's situation, so the reader must do work. Reading memory is an act of sense making by the present, not a lookup into the past.- The persistence paradox. A system that never changes becomes obsolete; a system that changes is no longer the one that remembered. Planaria regrow a head and keep learned behaviour. Centenarians keep childhood memories through decades of molecular turnover. Identity persists as a process that trades fidelity to the past for patterns that still generalise. Memory therefore cannot live in the part of the system that is replaced.
Levin extends the bow tie to every scale, from the egg that compresses an adult body into a cell to the genome that compresses a lineage, and he calls the arrangement polycomputing: the same stored pattern computes different things for different readers, and that freedom is where new capability comes from without catastrophic forgetting.

## Why it fits

Praxis is a platform on which an engineer designs a physical AI system for an estate they have never seen, in a sector they may not know, and comes out with a design a ten year engineer would recognise. The model that reasons is a frontier class open weights model, self hosted. Its weights never change.
So the platform's memory has to carry everything the model does not know and everything the platform learns, and it has to survive the model being swapped. That is the persistence paradox stated as a procurement requirement. The bow tie answers it: compress experience into patterns that do not depend on the reasoner, and let each new design read those patterns in its own context.

## Left wing

Everything the platform experiences enters as entries in Engram, CodeNinja's system of record for agent memory. Each entry has a source, a date and an honesty line that says what it cannot vouch for. Entries arrive through one validating door that refuses by name anything without a source, a jurisdiction where a law needs one, or a verified date. No customer of the platform is ever named in an entry.
Four kinds of experience land there.
ExperienceWhat an entry is- Reference: A sourced fact a builder can act on: a regulation clause, a model or hardware class, a precedent, a method, a past failure. Six lenses: rules, tooling, hardware, case studies, approach, history.- Learning: A raw sentence of domain knowledge from a talk, a paper, a build or a founder's note, with tags.- Episode: A design the platform produced, with its measured quality, and every line of feedback a person filed on it.- Ask: A question a design needed answered and the memory could not supply.
The reference corpus holds thousands of entries across the six lenses. The learnings number in the tens of thousands. Every design episode since the platform went live is kept. The counts move every night and are not the point; the shape is.

## The waist

Two routines run every night and do the compression. Neither touches the model. Both write only through the door.
Distillation. The raw learnings are folded into design briefs, one per domain tag, each a short ranked list of principles. Four operations and nothing else: merge near duplicates into one rule, resolve contradictions with the newest and most used reading winning, promote rules that good outcomes relied on and demote rules implicated in corrected ones, and mark as stale what was never used and never repeated. Every principle keeps the identifiers of the learnings it came from, so any rule on any design can be walked back to its sources. Every new brief is a new version; nothing is deleted.
This is salience over fidelity made literal. Tens of thousands of learnings stand behind a few hundred briefs. The sentences are gone. The relationships that still bind are kept, with their provenance.
Commissioning. The reference corpus is measured each morning against what practitioners in each sector expect it to answer, in two of the countries the platform serves. Where it falls short, writer agents stage new sourced entries and adversarial verifier agents remove what they cannot ground against the source. The door lands what survives. Superseded entries are never deleted; the new entry names what it replaces, and the planner's supersession index drops the old one from view.
The compression ratio is the point. Thousands of rules become the handful that bind in this country and this sector. Tens of thousands of learnings become a few hundred briefs, which become twenty lines on the table when a design begins.

## Right wing

A design in Praxis is called a birth. Before the model is asked anything, the platform assembles a room: the context the model will reason over for this requirement and no other. Assembly is deterministic code, not a search by similarity.
- Reference is filtered by the requirement's domain and by the country whose law binds, aged by verification date, de duplicated through supersession, and laid out under a fixed budget. Entries that fit ride in full. The rest ride as one title line each, and the model may call for any of them by name during reasoning. That call is the inflation step: a line becomes the full text only when the present design needs it.- Doctrine is read by a fit judge that marks which principles of the sector's brief and the cross sector briefs bear on this requirement. The planner receives them ranked and must cite them by number in the scope items they shaped.- The fleet record is read lesson by lesson, house scope first, then the sector's, up to a budget, together with the sector's rated past designs.- Standing memory, the project's own notes and the engineer's working preferences, rides last.
The model then reasons once over that room, in a single conversation, carrying its own thinking from part to part, and writes the design in three parts: the architecture, the scope ledger, the contract.
This is Levin's right wing. The same compressed principle, read by two births in different countries and sectors, produces two different scope items, because the requirement in front of the planner decides what the memory means today. The platform does not retrieve a past decision. It re decides, with the past as a message it has to interpret.
What a reader can verify on any Praxis design: every cited principle resolves to a brief version, every brief version resolves to its source learnings, and every reference line resolves to a dated source. The design is a document whose every claim can be walked back to an entry the customer owns.

## Reinforcement

Levin's bow tie is a funnel. Praxis closes it into a loop, so the right wing's output becomes the next left wing's input. This is recursive self improvement on Engram, and it changes memory, never weights.
At the design. Every birth is judged after reasoning against a rubric and filed as an episode with its score. Below a floor it is reasoned again with the verdict as a directive. A person's feedback on the design becomes lessons the next birth reads. The principles the design cited ride back to the distillation routine as outcomes, so a principle that good designs relied on rises and one that corrected designs leaned on falls. The asks a design could not answer become commissions for the corpus routine.
At the platform. A master agent runs improvement cycles on the platform itself: it reads what the routines did and owe, reads the misses from an independent benchmark of physical AI design, changes the platform, births real public requirements on production, and files what it learned as gap records on the routines' own episodes. The routines read those at the start of their next run. The agents never talk to each other directly. They talk through Engram.
At the substrate. Because every one of these signals is an entry in memory and not a weight, the reasoning model can be replaced and the memory stands. The platform has moved its reasoning between model providers with no change to what it remembers. New head, same memory.
What is published about the benchmark is its results. How it scores is not published.

## In pseudo code

The functions named here exist. Their internals, the prompts, the judges and the thresholds are not described on this page.

## Glossary

TermMeaning on this page- Engram: CodeNinja's system of record for agent memory. Every entry has a source, a date and an honesty line.- The door: The single validating entry point to the memory. Refuses by name.- Brief: A versioned, ranked list of design principles for one domain tag, each principle traceable to its sources.- Room: The context assembled for one design before the model is called.- Birth: One design produced by the platform from one requirement.- Episode: The record of one design or one routine run, with its measure, feedback and gap records.- Inflation: A reference that rode into the room as a title line being expanded to full text on the model's call.
Reference: Michael Levin, Self-Improvising Memory: A Perspective on Memories as Agential, Dynamically Reinterpreting Cognitive Glue, Entropy 26(6), 481, 2024. Read the paper.
Read next: Compression and Reinflation, the memo this architecture grew out of, and Praxis, the platform that runs it.
