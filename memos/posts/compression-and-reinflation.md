---
{
 "title": "Compression and Reinflation",
 "subtitle": "Why we do not fine tune, and how we build physical AI systems that get better when the next model arrives",
 "author": "Umar Bilal",
 "author_role": "Cofounder, CodeNinja",
 "date": "2026-10-10",
 "description": "A memo from CodeNinja cofounder Umar Bilal on compression and reinflation, the alternative to fine tuning: compress what the system learns into something small and meaningful, keep it where you can read it, and let a strong model reinflate it at the moment of use.",
 "cover_line": "An alternative to fine tuning, taken from biology",
 "banner": "Read cofounder Umar Bilal's memo, Compression and Reinflation"
}
---

Every enterprise that wants its own AI eventually asks the same question. Do we fine tune a model on our data?

For a long time I thought the answer was yes. I no longer think so. We have built this company on the opposite bet, and this memo is the argument for it.

## The cost of weights

Fine tuning freezes what you know into weights. The day you finish, the world has already moved. New regulations, new equipment, a new country, a new customer. The weights do not know.

And then a better model comes out, and the money you spent is gone.

So we went looking for another path. We found it in biology.

## Biology

The work that changed how I think about this is Michael Levin's. He is a biologist at Tufts, and he studies how cells, tissues and whole organisms remember, solve problems and rebuild themselves.

In a 2024 paper in Entropy, "Self Improvising Memory", he argues that memory in living systems is about **preserving salience, not fidelity**.

A living system does not store the past like a hard drive. It keeps the meaning, and it reinterprets that meaning every time it is needed, in a body and a world that have both changed.

He starts from an old paradox. If a species does not change, it dies out. If it does change, is it still the same thing?

Biology's answer is to stop defending a fixed self. It commits to change, and it gets very good at making sense of its own past in new conditions.

## The caterpillar

His favourite example is metamorphosis.

A caterpillar learns things. Then it dissolves most of its brain and rebuilds itself as a butterfly. And some of what it learned survives.

But the butterfly has no use for the caterpillar's memories as they were. It does not crawl. It does not eat leaves. It flies and it wants nectar.

What survives is not the detail. It is the lesson, generalised from leaves to food, and then remapped for a completely different body.

That is the whole idea in one picture.

## The bowtie

Levin describes this as a bowtie.

On one side, a huge amount of experience. In the middle, a tight bottleneck where it is compressed into something small. On the other side, it is expanded again, creatively, into whatever the new situation needs.

Biology does this everywhere. An organism does not copy itself. It compresses itself into an egg, and the egg reinflates into a new body in a new world, often with different parts. Language does it. A musical score does it, played years later on a different instrument. Science does it, when years of work become a paper that another scientist reinterprets for their own problem.

The important part is what happens at the bottleneck. Compression strips away the context, so what comes out the other side cannot simply be read back. The side that expands it has to be intelligent. It has to reason about what the memory means here, now.

Levin goes further. He suggests that a stored memory behaves less like a record and more like a prompt. A small signal that a capable receiver turns into the right behaviour for its situation.

When I read that, I thought of every large language model we work with.

## Forgetting

There is one more idea in the paper that matters a lot for anyone building AI.

Levin points out that biological systems add new functions by adding new interpretations of the mechanisms they already have, not by rewriting those mechanisms. That way nothing that depends on the old mechanism breaks. He notes this is exactly the problem that plagues machine learning: catastrophic forgetting.

Fine tuning is a rewrite of the mechanism. You change the weights, and you hope nothing you depended on moved.

Reinterpretation is the other path. The mechanism stays. What changes is how the past is read.

He also has a wonderful observation about planarian flatworms. They have one of the noisiest genomes in nature, and they are among the best at regenerating. Because the hardware is unreliable, the animal stopped trusting the details and got very good at rebuilding the pattern.

The lesson for us is simple. The world our systems run in is noisy and unreliable. Build for reinterpretation, not for memorisation.

## Stilts

The other piece that shaped my thinking came from a very different place.

Ian Fischer, cofounder of Poetic and a decade at Google DeepMind, explained on Y Combinator's Light Cone podcast why his company does not fine tune at all. They build recursively self improving harnesses: code, prompts, data and reasoning strategies that sit on top of frontier models.

His argument is the one I had arrived at from biology. Training or fine tuning your own model costs a fortune and takes months, and the next frontier release overtakes it. A harness that sits on top of the model does not lose that race. When a better model arrives, the same harness gets better with it.

He calls the frontier models stilts. **You do not compete with them. You stand on them.**

He says their system reached 54 percent on ARC AGI 2 at roughly half the cost of the model it beat, and 55 percent on Humanity's Last Exam, with an optimisation run under 100,000 dollars and a team of seven. Those are his numbers, but the shape of the argument is what stayed with me.

Self improvement does not have to mean retraining. It can mean a system that keeps getting better at using the model in front of it.

## What we build

At CodeNinja we build Praxis, a platform that designs physical AI and knowledge work systems for real industries and real countries. A young forward deployed engineer uploads a tender, and Praxis reasons out the system design, the architecture, the simulation and the proposal.

Underneath it is what we call a System of Context. Hyper Ontology holds a living model of the customer's world. Hyper Engram is agentic memory, where every run, every outcome and every correction is written back. Hyper Pragma is the work surface where people act.

The models never retrain on any of it. Everything becomes context.

## Compression

Every day, routines run on their own over what the platform has learned.

They take raw learnings from real deals, from benchmark runs, from engineers correcting a design, and they compress them. Many observations become one sharp principle. Contradictions are resolved. Things that proved themselves rise. Things that never mattered fade.

What is left is small. It is not a record of everything that happened. It is the salience of what happened.

That is the left side of the bowtie.

## Reinflation

Then a new requirement arrives. A mine in Chile. A contact center in Pakistan. A hospital in Ontario.

The compressed memory does not fit any of them exactly. It was never meant to.

So at inference, the model reinterprets it. It takes the compact principle and expands it into this customer, this country's laws, this estate, these people. The same lesson becomes a different design every time, because the world it lands in is different every time.

I call this compression and reinflation. Levin would call it remapping. It is the right side of the bowtie.

## Four consequences

When you fine tune, you bet that the future looks like your training data. When you compress and reinflate, you bet on the opposite. You assume everything will change, and you build a system that is good at making sense of its own past in a new situation.

That has four consequences we care about.

**The memory stays current.** A new regulation is one new entry, not a new training run.

**The memory stays inspectable.** You can read what the system knows, see where it came from, and correct it. You cannot read a weight.

**The memory survives the model.** When a stronger open weights model arrives, the memory carries straight over, and the design gets better on day one. That is Fischer's stilts, applied to memory.

**The memory stays the customer's.** It lives in their perimeter, on their infrastructure, under their control. For a sovereign deployment, that is not a feature. It is the point.

## The discipline

None of this works if the reinflation is lazy.

The bottleneck cuts both ways. Because the compressed memory has lost its context, the system that expands it must reason, not look things up. So we hold one rule above all others.

**Everything is context for the model to reason over. Never a keyword match. Never a count.**

When we have broken that rule, the platform has made confident mistakes. When we have kept it, the designs have gotten better every cycle.

## The loop

Levin ends somewhere I did not expect. He suggests the line between a memory and the mind that holds it may not be sharp at all. That memories, as patterns, may actively help the system that interprets them.

I am not making that claim about software. But I notice something when I watch our platform work. The memory and the reasoning are not two separate things anymore. Each run reads what came before and writes back what it learned, and the next run is a little better because of it.

That is what a self improving system looks like. Not a model that was trained once. A loop that keeps making sense of its own past.

## For engineers

If you are building enterprise AI and your first instinct is to fine tune, try the other path first.

Compress what you learn into something small and meaningful. Keep it where you can read it. Let a strong model reinflate it at the moment of use, for the situation in front of it. Stand on the frontier models instead of racing them.

Biology has been doing this for a very long time. I think it is the more honest way to build systems that live in a changing world.

## Reading

Michael Levin, "Self Improvising Memory: A Perspective on Memories as Agential, Dynamically Reinterpreting Cognitive Glue", Entropy 2024, 26(6), 481. https://doi.org/10.3390/e26060481

Ian Fischer on Y Combinator's Light Cone, "The Powerful Alternative To Fine Tuning". https://www.youtube.com/watch?v=UPGB-hsAoVY
