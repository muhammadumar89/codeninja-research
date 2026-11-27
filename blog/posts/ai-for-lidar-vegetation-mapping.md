---
{
 "title": "AI for LiDAR Vegetation Mapping: See What Grew Back Near Homes Each Season",
 "subtitle": "Every new laser survey lands as a fresh pile of files, so each season starts from scratch. An AI the land manager owns, over its own maps, can show where brush grew back near homes.",
 "author": "Muhammad Umar",
 "author_role": "Cofounder, CodeNinja Atoms",
 "author_url": "https://codeatoms.ai/about/#muhammad-umar-bilal",
 "date": "2026-11-26",
 "cover_photo": "dry-hillside.jpg",
 "cover_position": "center",
 "cover_line": "Physical AI that shows where brush grew back near homes.",
 "cover_credit": "Photo by Robert So on Pexels (https://www.pexels.com/photo/12446043/), Pexels License",
 "tags": [
  "Physical AI",
  "Earth Observation",
  "Sovereign AI"
 ],
 "audience": "For land managers and foresters who decide where brush is cleared near homes, their GIS and stewardship leads, and the geospatial and data engineers who would build an owned AI that compares every flight against the last.",
 "description": "NASA mapped all of California tree by tree. How an owned AI lines up every flight and shows a forester where brush grew back near homes.",
 "youtube_id": "FST9lhMwY2s",
 "video_url": "https://www.youtube.com/watch?v=FST9lhMwY2s",
 "source_url": "https://science.nasa.gov/blogs/science-news/2026/11/18/california-wildfire-risk-3d-maps/",
 "design_url": "https://codeatoms.ai/vegetation-mapping-lidar-us/",
 "cluster": "earth observation",
 "owned_keyword": "physical AI"
}
---

Watch the 90 second video: [AI for LiDAR Vegetation Mapping](https://www.youtube.com/watch?v=FST9lhMwY2s)

Where forests meet neighborhoods, the risk to a home can come down to a single tree.

On Nov 18, NASA released laser maps of all of California, sharp enough to show each tree.

## The problem

NASA researchers built one consistent map of the whole state, with each pixel one square meter, to help judge wildfire risk.

A map like that is a picture of one moment.
The brush near a home does not stop growing because the survey is done.

So the question that matters to a family on the edge of the forest is simple.
What grew back near my house since the last time anyone looked?

## How it is done today

Maps like these come from aircraft that pulse lasers at the ground.

Land managers use them to decide where to thin brush near homes.

The laser returns build a cloud of points, from the treetops down to the bare earth.
An analyst reads that cloud next to the aerial photos, tile by tile, and marks what needs clearing.

## Why it is hard

Keeping them current is hard.

California's map joins 118 surveys flown from 2013 to 2023, and plants keep growing after each one.

Every new flight lands as a fresh pile of files.
Analysts compare seasons by hand, so each season starts from scratch.

The files rarely say which unit they cover, which aircraft flew them, or how accurate they are.
So nobody can line this summer up against last summer without rebuilding the link first.

For example, imagine two class photos taken a year apart, with no names written on the back.
You can see every face changed. You just cannot say whose.

![Homes on open ground where the forest begins: the edge a land manager has to keep clear.](figures/homes-forest-edge.jpg)

## This is work AI can do.

It lines up every flight and field note, and shows where brush grew back near homes since the last pass.

It compares canopy height and cover tile by tile, season against season.
And it shows the flight, the date and the accuracy behind each flag, so a person can check it.

## What the land manager needs

For that, each land manager needs its own AI over its own maps.

It flags the change, and a forester approves what gets cleared.

The AI drafts the list of places where growth came back close to homes, roads and water.
The forester confirms or rejects each flag and signs the clearing plan. No agent sends a crew on its own.

The AI does the comparing. A named person signs for it.

## Why own it, not rent it

Owning it matters for two reasons.

Those maps show every home, road and water source, and should stay inside the owner's walls.

And an AI you rent learns for its vendor.
An AI you own learns for you, and every flight makes the next one sharper.

Every flag the forester confirms or rejects teaches it what real regrowth looks like on that ground.
When a better model ships, the land manager swaps it in and keeps every lesson.

So it runs inside the organisation, air gapped where needed, on open weight models and software it owns.

![Forest canopy seen from above: the surface every laser survey measures, season after season.](figures/forest-canopy.jpg)

## The reference architecture

We published the design for an agriculture and earth observation operator in the United States.
It is an open [reference architecture for LiDAR vegetation mapping](https://codeatoms.ai/vegetation-mapping-lidar-us/): one summer flight of imagery and laser data, with every deliverable bound into a site ontology the operator owns.

That ontology is the ground an owned AI stands on.
The published design deliberately serves no model; the change flagging is what an owned AI adds on top.

In short:

- **Sources.** Four named sources through two adapter families: the operator's boundary file and GIS server, read in place, and the survey firm's flight records and delivered files.
- **One record per flight.** Sixteen kinds of object, with the flight mission at the center, from the site, land unit, watercourse and dam to the camera, laser sensor, point cloud, elevation models and the accuracy report.
- **Acquisition.** One manned flight within a week either side of 1 July: 3 inch, four band imagery in red, green, blue and near infrared, and laser data at the national Quality Level 1 standard, at a minimum of 8 pulses per square meter.
- **Models.** None in the published design: vegetation analysis stays with the operator's own analysts. Its cost appendix names the first step up, one open weight vegetation model on a single 48 GB card, listed at 7,709 dollars.
- **Compute.** Nothing runs in a cloud the operator does not control; the ontology lives in its own GIS server.
- **Cost.** No compute to price over three years. The acquisition is priced by the survey firm against the operator's own task table.
- **Who approves.** The operator's project manager accepts each deliverable against the accuracy report.
- **Rollout.** Four phases, each closed by a gate: model the objects before any aircraft moves, fly inside the window, prove accuracy, then hand over and rehearse the export.

The design, its object model and its model register are free to reuse under CC BY 4.0.

## The close

The risk to a home can come down to a single tree that grew back since the last pass.
The map that could show it should not start from scratch every season.

A land manager that owns its AI keeps every flight inside its own walls, shows the forester what changed, and gets sharper with every season.

That is what [physical AI](https://codeatoms.ai/physical-ai/) is for.

Source: [NASA Researchers Create 3D Maps of California to Assess Wildfire Risk, NASA Science](https://science.nasa.gov/blogs/science-news/2026/11/18/california-wildfire-risk-3d-maps/)

Reference architecture: [https://codeatoms.ai/vegetation-mapping-lidar-us/](https://codeatoms.ai/vegetation-mapping-lidar-us/)

Learn more at [https://codeatoms.ai](https://codeatoms.ai)
