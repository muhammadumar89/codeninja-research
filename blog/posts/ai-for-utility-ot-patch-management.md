---
{
 "title": "AI for Utility OT Patch Management: Remember Every Grid Security Decision",
 "subtitle": "Every security advisory for grid software starts from zero at a utility. An AI the utility owns, on its own servers, can join the records, recall the last decision and keep every lesson.",
 "author": "Muhammad Umar",
 "author_role": "Cofounder, CodeNinja Atoms",
 "author_url": "https://codeatoms.ai/about/#muhammad-umar-bilal",
 "date": "2026-11-25",
 "cover_photo": "substation.jpg",
 "cover_position": "center",
 "cover_line": "Industrial AI that remembers every grid security decision.",
 "cover_credit": "Photo by Mr Dr3igeteilt on Pexels (https://www.pexels.com/photo/36137497/), Pexels License",
 "tags": [
  "Industrial AI",
  "OT Security",
  "Sovereign AI"
 ],
 "audience": "For utility leaders accountable for the patch cycle, their compliance engineers and asset owners, and the data and platform engineers who would build an owned AI that works each security advisory against the utility's own records.",
 "description": "CISA flagged critical flaws in Siemens grid control room software. How an owned AI at a utility joins the records, recalls the last decision, files the audit.",
 "youtube_id": "QD4ffH3Ssls",
 "video_url": "https://www.youtube.com/watch?v=QD4ffH3Ssls",
 "source_url": "https://www.cisa.gov/news-events/ics-advisories/icsa-26-316-01",
 "design_url": "https://codeatoms.ai/ot-vulnerability-utility-us/",
 "cluster": "OT security + NERC CIP",
 "owned_keyword": "industrial AI"
}
---

Watch the 90 second video: [AI for Utility OT Patch Management](https://www.youtube.com/watch?v=QD4ffH3Ssls)

When the grid fails in a cold snap, families lose heat at home.

On Nov 18, grid watchdog NERC warned winter is the hardest season to keep power on.

## The problem

On Nov 12, CISA flagged critical flaws in Siemens grid control room software.

The advisory names four Spectrum Power products, software that grid control rooms use to run the network.
Across the whole advisory, the worst flaw scores 9.8 out of 10, and Siemens says some fixes are not yet available.

So every utility running that software has a question to answer, in the hardest season of the year.
Which of our machines does this touch, and what do we do about it?

## How it is done today

Today, an engineer at each utility works each advisory by hand.

They find the machines it touches.
The owner decides to patch now or protect until a safe outage.

Patching a control room server is not like updating a phone.
It needs a window when the grid can spare it, a change ticket, and proof for the auditor afterwards.

## Why it is hard

That is hard.

The device list, the vendor notice and the change tickets sit in different systems.
And why the last fix for that vendor was chosen is rarely recorded.

So every advisory starts from zero.

Imagine a doctor who treats the same patient every month, but the chart is wiped after each visit.
The symptoms come back, and the reasoning behind the last prescription is gone.

## This is work AI can do.

It joins those records, shows which machines are touched, and recalls the last decision.

It reads the advisory against the device list and the verified baseline, and shows why each machine is in or out.
And it brings back what was decided the last time this vendor's advisory touched these devices, and why.

![A high voltage transmission tower: the grid that every patch decision protects.](figures/transmission-tower.jpg)

## What the utility needs

The utility runs its own AI on its own servers.

It drafts the change, the owner approves, and the audit record files itself.

The compliance engineer confirms which machines the advisory touches.
The asset owner approves each decision to patch now or protect until an outage, with its window and change request.
The compliance manager confirms each evidence package.

No agent applies a patch, changes a baseline or closes a change.
The AI does the drafting. A named person signs for it.

## Why own it, not rent it

Owning it matters for two reasons.

A map of a utility's weak points should never leave its network.

And an AI you rent learns for its vendor.
An AI you own remembers every decision, and gets sharper each cycle without more data.

Every decision the asset owner confirms becomes a precedent the next cycle retrieves.
When a better model ships, the utility swaps it in and keeps every lesson.

So it runs inside the utility, air gapped where needed, on open weight models and software it owns.

## The reference architecture

We published the design for an electric utility in the United States whose substations, control centers and plants fall under the grid's critical infrastructure protection standards.
It is an open [reference architecture for OT vulnerability management at a utility](https://codeatoms.ai/ot-vulnerability-utility-us/).

In short:

- **Sources.** Seven systems of record, read through their own interfaces: the asset inventory and baseline system, the vendors' advisory feeds, the national vulnerability advisories, change management, work orders, the audit evidence repository and the network monitoring tool's device list. The only writes back are draft change requests and confirmed evidence items.
- **One record per device.** Sixteen kinds of object with thirteen links, from the substation, protective relay and engineering workstation to the advisory, applicability decision, change request, outage window and evidence item.
- **Models.** Two open weight models of United States origin on the utility's own hardware: one of about 120 billion parameters reasons, drafts and answers in plain words, and one finds the advisories, baselines and past decisions behind every answer.
- **Compute.** One server of eight 80 GB cards in the utility's own data center, at about ten kilowatts. Nothing about its assets leaves its network.
- **Cost.** About 477,000 US dollars to own the server for three years, against about 544,000 to rent the same eight cards on the deepest three year cloud commitment. Owning costs about seven eighths of renting, and the vulnerability record never leaves the network.
- **Who approves.** The compliance engineer confirms each applicability call, the asset owner approves each disposition and its change request, and the compliance manager confirms each evidence package.
- **Rollout.** Two phases, each closed by a gate, never a date: first the protective relays and engineering workstations at one group of substations for two patch cycles, then the other asset classes and the generating plants. It is measured in engineer hours per cycle, windows kept and auditor questions answered from the record.

The design, its object model and its model register are free to reuse under CC BY 4.0.

## The close

A critical advisory lands in the hardest season to keep power on.
The reasoning behind the last decision should not have to be rebuilt from zero.

A utility that owns its AI keeps every decision inside its own network, hands it to the next engineer, and gets sharper each cycle.

That is what [industrial AI](https://codeatoms.ai/industrial-ai/) is for.

Source: [Siemens Building Automation and Energy Products, CISA](https://www.cisa.gov/news-events/ics-advisories/icsa-26-316-01)

Reference architecture: [https://codeatoms.ai/ot-vulnerability-utility-us/](https://codeatoms.ai/ot-vulnerability-utility-us/)

Learn more at [https://codeatoms.ai](https://codeatoms.ai)
