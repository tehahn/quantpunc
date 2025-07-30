---
title: "Puncta counting"
permalink: /puncta-counting
nav_order: 6
---

# Puncta counting
---

### Once you have a set of puncta labels you’re happy with, follow these steps to count them:

1. Click on the *Puncta labeling* tab
2. Select the image layer you want to count puncta for using the *Select layer* dropdown menu.
3. Specify whether there’s a corresponding mask layer in the *Select mask* dropdown menu. If “None” is specified, all the puncta in your image will be counted.
4. QuantPunc expects a puncta labels layer in the layer list named after the image you’ve selected in the first step with "_puncta" as its suffix, e.g., "your_image_puncta". 

    * If the base names don’t match, e.g. "your_image_processed" (name of selected layer) and "your_image_puncta" (name of puncta labels layer), nothing will get quantified.

5. Click the *Count puncta* button.

### To view your puncta counts and stats follow these steps:

1. At the bottommost widget, choose the image layer you want to view your puncta stats for in the *Select layer to display* table dropdown menu.
2. Click on the *Counts* tab if it hasn’t already been selected to view puncta counts.

    * The first column specifies the ROI ID and the second column specifies the puncta counts for each ROI.
    * If no masks were specified, the ROI ID for all counts is -1.

3. Click on the *Puncta stats* tab to view the area, intensity, and associated mask for each puncta.

    * The area corresponds to the number of pixels a puncta label covers.
    * The intensity is the aggregate pixel intensity in a puncta label.
    * The associated mask is the mask a punctum is in.
