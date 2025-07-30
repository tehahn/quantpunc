---
title: "Seed points"
permalink: /watershed-segmentation/seed-points
parent: Watershed segmentation
nav_order: 1
---

# Seed points
---

Seed points designate where you want to start flooding your basins from. You ideally want your seed points to be in the middle of your puncta labels like this:

<img 
src="{{ '/assets/images/seed_points_example.png' | relative_url }}" 
alt="" 
width="500"
style="border-radius: 8px; max-width: 100%;">

Seed point size also affects the number of instance segmentations. The larger your seed points are, the less segmentations you’ll have. The smaller your seed points are, the more segmentations you’ll have. 

You can either create your own seed points following the steps in the [Manual labeling] section or use one of the [skimage blob detection] methods with low *min_sigma* and *max_sigma* values, e.g.,
<br>
*min_sigma* = 1, *max_sigma* = 2.

[Manual labeling]: ../puncta-labeling/manual-labeling
[skimage blob detection]: ../puncta-labeling/skimage-blob-detection