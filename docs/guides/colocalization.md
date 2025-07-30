---
title: "Colocalization"
permalink: /colocalization
nav_order: 7
---

# Colocalization
---

QuantPunc uses intersection over union (IoU), aka the Jaccard index, to quantify colocalization between two sets of puncta. You can read more about this [here].

## Instructions
1. Select a puncta labels layer in the *Select first annotated layer* dropdown menu.
2. Select a different puncta labels layer in the *Select second annotated layer* dropdown menu.
3. Specify whether a mask labels layer is present in the *Select mask* dropdown menu. If a mask labels layer is present, the IoU will only be computed within each ROI.
4. Click on *Compute IoU*.
5. Select one of the layers you selected in steps 1 or 2 from the *Select layer to display table* dropdown menu.
6. Click on the *Colocalization* tab beneath the *Select layer to display table* dropdown menu.
7. Like the puncta counts table, the first column specifies the mask ID and the second specifies the IoU for each mask.

[here]: https://en.wikipedia.org/wiki/Jaccard_index