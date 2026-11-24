---
{
 "title": "AI for Aircraft Parts Shortages: Form Sheet Metal Parts In House Without a Die",
 "subtitle": "A medevac or firefighting aircraft can sit in a hangar, waiting on one bent metal part nobody makes anymore. A robot cell by the hangar, run by AI the shop owns, can form that part from the drawing.",
 "author": "Muhammad Umar",
 "author_role": "Cofounder, CodeNinja Atoms",
 "author_url": "https://codeatoms.ai/about/#muhammad-umar-bilal",
 "date": "2026-11-23",
 "cover_photo": "hangar.jpg",
 "cover_position": "center",
 "cover_line": "Physical AI for the parts nobody makes anymore.",
 "cover_credit": "Photo by Daniel Torobekov on Pexels (https://www.pexels.com/photo/5262808/), Pexels License",
 "tags": [
  "Physical AI",
  "Aviation",
  "Sovereign AI"
 ],
 "audience": "For aircraft maintenance leaders, repair shop owners and the engineers who would build an owned AI robot cell to make out of production sheet metal parts in house.",
 "description": "Aircraft wait weeks for sheet metal parts no one makes. How an owned AI robot cell forms them in house from the drawing, without a die.",
 "youtube_id": "_aSfdvGHGUQ",
 "video_url": "https://www.youtube.com/watch?v=_aSfdvGHGUQ",
 "source_url": "https://www.aviationpros.com/aircraft-maintenance-technology/engines-parts/article/55417444/why-the-parts-supply-chain-puts-pressure-on-maintainers-plus-how-to-help",
 "design_url": "https://codeatoms.ai/dieless-sheet-metal-cell-aerospace-mro-us/",
 "cluster": "aviation MRO",
 "owned_keyword": "physical AI"
}
---

Watch the 90 second video: [AI for Aircraft Parts Shortages](https://www.youtube.com/watch?v=_aSfdvGHGUQ)

A medevac or firefighting aircraft can sit in a hangar, waiting on one metal part.

Not an engine. Not a computer.
A bent piece of aluminium the size of a book.

## The problem

This month, a survey of aircraft repair shops found that over a third of the large shops hit parts delays every day.

Not once a week. Every single day.

The survey came from TBX, an aviation maintenance software company. Its parts survey drew more than 350 responses.
The answer that came back, over and over, was time.

A shop bills by the hour.
When an aircraft waits, the hangar slot waits, the mechanic waits, and every aircraft booked behind it waits too.

The big shops feel it most.
They see the most aircraft, order the most parts, and their customers fly for a living: medevac, aerial firefighting, charter.

Two thirds of the shops said it will get worse.

## How it is done today

Today, a shop orders the part from the maker and waits.

Some parts are no longer made.
The maker has moved on, or has no stock for months, sometimes years.

So the shop calls around, searches salvage, and pays what it has to.
The same survey heard of markups of 1,000 percent and more.

## Why it is hard

Making the part in house is hard.

Aircraft sheet metal is bent over a custom die, and every sheet springs back differently.

Imagine bending a sheet of paper over the edge of a table.
Let go, and it lifts back a little. Metal does the same, and how far depends on the sheet, the alloy and the day.

A die is built to cancel that out for one part.
It is expensive, and it only pays off when you make thousands of that part.

For a fleet under a hundred aircraft, no supplier builds a die for one part.
Even the companies that make approved replacement parts will not tool up when the whole market is a few dozen aircraft.

So the aircraft waits.

## This is work AI can do.

It can turn a drawing into a robot forming path.
It can correct springback as it bends, and scan each part against the drawing.

Instead of a die, two robot arms hold a smooth tool on each side of the sheet, press a little at a time, and walk the shape in.

The AI watches the force on the tool and the shape of the sheet as it forms.
When the metal springs back more than expected, it corrects the next pass.

![A robot cell at work on metal: the kind of cell that forms an aircraft part from a drawing instead of a die.](figures/robot-cell.jpg)

## What the shop needs

For that, the shop needs its own AI in a robot cell by the hangar.

Every part gets a record under its serial number.
The drawing, the forming path, the scans, the force traces and any defect are joined in one place.

And an inspector approves it.

A named operator releases every forming program.
An authorized person decides on every part that does not match the drawing.
The machine's safety system never takes an instruction from the AI.

The AI does the work. A person signs for it.

## Why own it, not rent it

Owning it matters for two reasons.

A shop's drawings and repair records are controlled data that should never leave the shop.
They belong inside the shop's own walls, air gapped where needed.

And an AI you rent learns for its vendor.
An AI you own learns for you.

Every part the cell forms teaches it something about that sheet, that alloy and that shape.
When a better model ships, the shop swaps it in and keeps every lesson.

So the cell runs inside the shop, on open weight models and software it owns.

## The reference architecture

We published the full design as an open [reference architecture for a dieless robotic sheet metal cell](https://codeatoms.ai/dieless-sheet-metal-cell-aerospace-mro-us/) in an aircraft repair facility in the United States.

In short:

- **Sources.** Six, read only: the part drawing, the cell's own sensors, the forming software, the production systems, the quality records and the cell's machine telemetry.
- **One record per part.** Fourteen kinds of object, from the sheet blank and the robot arm to the forming program, the scan and the defect, joined under each serial number.
- **Models.** Two open models on a small computer in the cell panel: one spots surface and shape defects on each formed panel, one learns what a normal force trace looks like so a bad pass stands out.
- **Compute.** That edge computer, plus one eight card inference server in the facility, joined one way through a hardware data diode so nothing flows back out.
- **Cost.** About 202,000 to 220,000 US dollars to own over three years, most of it the scanner and the server. The compute alone costs about two fifths of the deepest three year cloud commitment for the same cards, and the cell has to run offline anyway.
- **Rollout.** Three phases: a prototype on scrap sheets with a written rule for when to stop, then the production cell, then a study of steel and titanium before any claim is made for them.

The design, its object model and its parts list are free to reuse under CC BY 4.0.

## The close

The aircraft is not waiting on a miracle.
It is waiting on a bent piece of metal.

A shop that owns its AI can make that part next to the hangar, prove it against the drawing, and put the aircraft back in the air.

That is what [physical AI](https://codeatoms.ai/physical-ai/) is for.

Source: [Why the parts supply chain puts pressure on maintainers, Aviation Pros](https://www.aviationpros.com/aircraft-maintenance-technology/engines-parts/article/55417444/why-the-parts-supply-chain-puts-pressure-on-maintainers-plus-how-to-help)

Reference architecture: [https://codeatoms.ai/dieless-sheet-metal-cell-aerospace-mro-us/](https://codeatoms.ai/dieless-sheet-metal-cell-aerospace-mro-us/)

Learn more at [https://codeatoms.ai](https://codeatoms.ai)
