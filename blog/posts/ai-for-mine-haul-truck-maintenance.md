---
{
 "title": "AI for Mine Haul Truck Maintenance: Keep a Retiring Planner's Judgement",
 "subtitle": "The people who know which truck will fail next are leaving the mines. An AI the mine owns, on a server on site, can keep that judgement and hand it to the next planner.",
 "author": "Muhammad Umar",
 "author_role": "Cofounder, CodeNinja Atoms",
 "author_url": "https://codeatoms.ai/about/#muhammad-umar-bilal",
 "date": "2026-11-24",
 "cover_photo": "haul-fleet.jpg",
 "cover_position": "center",
 "cover_line": "Physical AI that keeps a veteran planner's judgement on site.",
 "cover_credit": "Photo by Deyler Rivera Segura on Pexels (https://www.pexels.com/photo/29506757/), Pexels License",
 "tags": [
  "Physical AI",
  "Mining",
  "Sovereign AI"
 ],
 "audience": "For mine superintendents, maintenance planners and the reliability and data engineers who would build an owned AI that tells a mine which part on which truck fails next.",
 "description": "Mines are losing the planners who know which truck fails next. How an owned AI on site joins every alarm, oil sample and repair to keep that judgement.",
 "youtube_id": "1yTh2BpGBlU",
 "video_url": "https://www.youtube.com/watch?v=1yTh2BpGBlU",
 "source_url": "https://www.kentuckytoday.com/news/harlan-county-mine-closed-after-fatal-coal-truck-accident/article_3f2d6f0d-d979-4af5-b548-0e374453f39c.html",
 "design_url": "https://codeatoms.ai/open-pit-mine-haul-fleet-saudi-arabia/",
 "cluster": "mining fleet maintenance",
 "owned_keyword": "physical AI"
}
---

Watch the 90 second video: [AI for Mine Haul Truck Maintenance](https://www.youtube.com/watch?v=1yTh2BpGBlU)

A 25 year old truck driver died at a Kentucky surface mine on Nov 9.

Police said his truck failed on the haul road.

## The problem

He was leaving the mine in Harlan County just after seven in the morning.
No other vehicle was involved. A state trooper said something on the truck malfunctioned and it lost control.

The site was closed while state mine safety inspectors, the state police and federal mine safety officials investigate.
It was Kentucky's second coal mining death this year.

A truck does not fail out of nowhere.
It leaves signs first, and someone has to read them.

The people who know which truck will fail next are leaving.
A federal energy official expects US mining to lose half its workers to retirement in ten years.

## How it is done today

Today, a veteran maintenance planner keeps the trucks safe.

They read oil results, alarms and repairs, and know which truck needs the shop.

A rising metal count in an oil sample.
An alarm that came back twice this week.
A part rebuilt sooner than it should have been.

None of it means much alone. Together, it tells a planner which truck to pull.

## Why it is hard

That judgement is hard to pass on.

The records sit in five systems, and the pattern lives in one head.

Imagine five people each holding one page of the same letter.
None of them can read it. Only the planner has seen every page, so only the planner knows what it says.

When the planner retires, the pattern walks out the gate.

## This is work AI can do.

It can join every alarm, oil sample and repair and flag which part on which truck fails next.

It reads the whole letter at once, every page, for every truck, every shift.
And it shows the records behind each call, so a person can check it.

![A planner at a diagnostic screen beside a truck in the shop: the person who asks the AI and approves the work order.](figures/planner-screen.jpg)

## What the mine needs

For that, the mine needs its own AI on a server on site.

A young planner asks in plain words, sees what a veteran would, and approves each work order.

The AI drafts the ranking and the reasons.
The maintenance planner approves each health ranking and each work order. The dispatcher approves any change to the haul plan.
No agent stops a machine or changes a work order without a named approval.

The AI does the reading. A person signs for it.

## Why own it, not rent it

Owning it matters for two reasons.

A mine's fleet records are its business and should not leave the site.

And an AI you rent learns for its vendor.
An AI you own learns for you, and every repair makes the next call sharper.

Every work order that closes teaches it what that alarm really meant on that truck.
When a better model ships, the mine swaps it in and keeps every lesson.

So it runs inside the mine, air gapped where needed, on open weight models and software it owns.

![Haul trucks on the winding roads of an open pit mine.](figures/haul-road.jpg)

## The reference architecture

We published the design for an open pit mine in Saudi Arabia; the same pattern fits a US mine.
It is an open [reference architecture for an open pit mine haul fleet](https://codeatoms.ai/open-pit-mine-haul-fleet-saudi-arabia/), written for a pit with about 35 trucks and one 600 tonne class shovel.

In short:

- **Sources.** Five systems, all read only: the fleet management and dispatch system, the equipment makers' telematics, the maintenance management system, the oil laboratory and the mine plan. The only writes back are approved work orders and approved haul changes, each with an audit trail.
- **One record per truck.** Sixteen kinds of object with thirteen links, from the haul truck, component and haul road segment to the alarm, oil sample, tyre reading, work order and rebuild, joined on one fleet model.
- **Models.** Four open models on the mine's own hardware: one reasons and answers the planner in plain words, one forecasts telemetry and oil trends, one finds the records behind every answer so each call cites its evidence, and one watches the shovel bucket for lost teeth.
- **Compute.** One server of eight GPU cards in the site server room, at roughly ten kilowatts, with small heat rated computers on the trucks and at the shovel. Nothing leaves the site; updates arrive one way through a hardware data diode.
- **Cost.** About 556,000 US dollars to own the reasoning server for three years, against about 751,000 to rent the same eight cards on the cheapest three year cloud commitment. Owning costs about three quarters of renting, and the records never cross a border.
- **Who approves.** The maintenance planner approves each health ranking, the dispatcher each haul change, the shovel operator each lost tooth, and the mine superintendent holds escalation.
- **Rollout.** Four phases, ending in a six month measured run on one pit's fleet against the mine's own numbers for unplanned downtime, time between failures and cost per tonne.

The design, its object model and its model register are free to reuse under CC BY 4.0.

## The close

A truck that fails on the haul road gave warnings first.
The planner who could read them is about to retire.

A mine that owns its AI keeps that judgement on site, hands it to the next planner, and gets better with every repair.

That is what [physical AI](https://codeatoms.ai/physical-ai/) is for.

Source: [Harlan County mine closed after fatal coal truck accident, Kentucky Today](https://www.kentuckytoday.com/news/harlan-county-mine-closed-after-fatal-coal-truck-accident/article_3f2d6f0d-d979-4af5-b548-0e374453f39c.html)

Reference architecture: [https://codeatoms.ai/open-pit-mine-haul-fleet-saudi-arabia/](https://codeatoms.ai/open-pit-mine-haul-fleet-saudi-arabia/)

Learn more at [https://codeatoms.ai](https://codeatoms.ai)
