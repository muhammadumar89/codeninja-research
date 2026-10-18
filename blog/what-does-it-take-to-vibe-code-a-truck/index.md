# What Does It Take to Vibe Code a Truck?

*Software can now be described into existence. Physical systems cannot, because the knowledge needed to design them lives in the heads of senior engineers. This is how CodeNinja Atoms is building the missing piece: deep domain expertise for physical AI system design, carried as context instead of trained into weights.*

Canonical: https://codeatoms.ai/blog/what-does-it-take-to-vibe-code-a-truck/
Author: Muhammad Umar, Cofounder, CodeNinja
Published: 2026-10-18
License: CC BY 4.0
Publisher: CodeNinja Atoms (https://codeatoms.ai), a fully owned subsidiary of CodeNinja
A year ago, vibe coding meant something new. You describe the app you want, a model writes it, you run it, you describe what is wrong, and it fixes it. A person with no training in software can now ship working software.

So here is the question I keep coming back to. What would it take to vibe code a truck?

Not the cab or the paint. The whole system. An autonomous haul truck working in a copper mine, the fleet it belongs to, the network it talks over, the people who work around it, and the regulator who has to sign it off.

Today no model can do that. This post is about why, and about what we are building at CodeNinja Atoms to change it.

## The Truck

Start with what an engineer actually has to decide before an autonomous haul truck moves a single tonne.

**Sensing.** Which lidar, radar and cameras, where they sit, and what they can see in dust, rain and at night. A sensor that works on a highway can fail on a haul road.

**Compute.** What runs on the truck, what runs at the edge of the pit, and what runs in a data center. How much power, cooling and memory each one needs, and what happens when the link drops.

**Models.** Which perception, prediction and planning models, at what size, trained or adapted on what data, and how each one is monitored once it is running.

**The site.** Haul roads, loading points, crushers, fuel bays, light vehicles driven by people, and the private network that ties them together. The truck is only safe if the site is designed around it.

**Safety and approvals.** Autonomous mining machines have their own safety standards, and each country adds its own rules on top. Someone has to write the safety case, and someone has to approve it.

**Cost and time.** What the system costs over three years, what it saves, and how long it takes before the first truck runs on its own.

**Maintenance.** How the fleet knows a part is about to fail, and who acts on it.

Every one of these decisions depends on the others. Change the sensor and the compute changes. Change the country and the approval path changes. That web of decisions is system design, and for physical AI it is one of the hardest problems there is.

## The Bottleneck

A model can write software because it has read more software than any person ever will. Billions of lines of code are public, along with the questions people asked about them and the answers that worked.

Physical system design is not like that. The knowledge sits in tender documents, internal standards, site reports and, above all, in the heads of engineers who spent twenty years in mining, oil and gas, ports or power. Very little of it is written down, and almost none of it is public.

So the bottleneck in physical AI is not the model. It is deep domain expertise. A young engineer can learn to code in a year. Learning to design a mine takes a career.

That is the problem we set out to solve. Our mission is to let a young engineer design the physical AI systems that whole industries run on, without first spending twenty years in those industries.

## CodeNinja Atoms

CodeNinja Atoms is how we work on that mission in the open. It has four parts.

**Praxis** is the platform. An engineer brings a requirement, often a real tender, and Praxis reasons out the full system design: sensing, compute, models, the object model of the operation, cost, timeline and the approvals it will need. It explains every choice, so the engineer learns the design instead of just receiving it. Praxis is free for engineers.

**Hyper Ontology** is the shared language of those designs. Every design carries an object model of the operation, the assets, people, events and rules, and how they connect, in an open JSON format called hyper-ontology/1.

**The reference architectures** are the designs we publish. There are eighteen so far, across energy, oil and gas, ports, manufacturing, agriculture, rail and more, in the United States, Saudi Arabia and Pakistan. Together their object models hold 246 typed objects and 228 links. They are on [codeatoms.ai](https://codeatoms.ai/sovereign-ai-reference-architectures/) and as a dataset on [Hugging Face](https://huggingface.co/datasets/CodeNinjatools/vertical-driven-architectures).

**PADI**, the Physical AI Design Index, is the benchmark. It asks a simple question: does the Praxis platform design better systems than frontier AI on its own? It scores both on fresh tasks across 13 industries in three countries. In our latest round, a blind evaluation on seven tasks the platform had never seen, the Praxis platform passed 48.5% of the checks against 28.4% for frontier AI, and came out ahead on all seven tasks. The results are on the [PADI page](https://codeatoms.ai/padi/).

## Compression and Reinflation

The obvious way to give a model domain expertise is to fine tune it. Collect the data, train the weights, ship the model.

We chose not to, and I wrote about why in a memo, [Compression and Reinflation](https://codeatoms.ai/memos/compression-and-reinflation/). Here is the short version.

Fine tuning freezes what you know into weights. The day training ends, the world has already moved: a new regulation, a new site, a new country. And when a better model arrives, the money spent on the old weights is gone.

So we keep expertise as context instead. It works in two steps.

**Compression.** Every day, routines run over what the platform has learned: from real deals, from benchmark rounds, and from engineers correcting a design. Many observations become one sharp principle. Contradictions are resolved. What proved itself rises and what never mattered fades. What is left is small. It is not a record of everything that happened. It is the meaning of what happened.

**Reinflation.** When a new requirement arrives, say a copper mine in a country we have never worked in, no stored principle fits it exactly. It was never meant to. The model reads the compressed expertise and expands it into this site, this country's rules, this fleet and these people. The same lesson becomes a different design every time, because the world it lands in is different every time.

The idea comes from biology. The biologist Michael Levin describes memory as a bowtie: a lot of experience squeezed through a narrow middle and then expanded again for a new body and a new world. A caterpillar's lessons survive inside the butterfly, remapped for wings instead of legs.

There is one rule that makes this work. Everything is context for the model to reason over. Never a keyword match, never a lookup.

## Why It Beats Fine Tuning

Keeping expertise as context instead of weights changes four things.

**It stays current.** A new regulation is one new entry, not a new training run.

**It stays readable.** An engineer can see what the system knows, where it came from, and correct it. Nobody can read a weight.

**It survives the model.** When a stronger open weights model arrives, the expertise carries straight over and the designs improve on day one.

**It stays with the owner.** The expertise lives inside the customer's own perimeter, on their own infrastructure. For a sovereign deployment, that is the whole point.

## Back to the Truck

So what would it take to vibe code a truck?

An engineer would describe the operation: an autonomous haul fleet for a copper mine, in a named country, with a target output and a budget. The system would come back with the sensing, the compute, the models, the site network, the object model of the mine, the safety case outline, the approvals, the three year cost and the plan. Then the engineer would push back, as engineers do, and the system would explain itself and change.

That is not science fiction, and it is not finished either. It needs a model that is good at reasoning, which we now have. It needs deep domain expertise, carried in a form the model can read and an engineer can check, which is what we are building. And it needs a way to measure whether the designs are any good, which is why PADI exists.

When those three come together, the most complex physical systems in the world stop being the work of a handful of people with twenty years behind them. A young engineer anywhere can design them, and understand every choice they made.

Explore the designs, the benchmark and the platform at [codeatoms.ai](https://codeatoms.ai).
