---
title: "Watershed segmentation"
permalink: /watershed-segmentation
nav_order: 5
has_toc: false
---

# Watershed segmentation
---

**This step is optional but highly recommended, especially if your puncta exhibits lots of clumping.**

The watershed algorithm is used for instance segmentation and resolving clumped puncta labels as shown below:

<img 
src="{{ '/assets/images/clumped_puncta.png' | relative_url }}" 
alt="" 
width="500"
style="border-radius: 8px; max-width: 100%;"> 

The general idea of how water segmentation works is that you treat an image like a topographical map and “flood” different parts of it at local minima to create borders. Imagine that the pixel intensities represent elevation where higher intensities correspond to elevated regions like mountains and lower intensities correspond to regions at sea level. Let’s pretend that we have two basins from your image adjacent to each other.

Now imagine flooding both of these basins starting at their lowest points. Eventually, their water levels are going to rise up to the highest points of the mountain separating them.

To prevent the water from spilling over, we choose to build a dam directly on the highest points of the mountain which forms a border between the two basins. Now imagine applying this to all basins. This is essentially what the watershed algorithm does to create borders between clustered puncta labels and perform instance segmentation.

## Instructions
1. Click on the *Watershed* tab.
2. Select the puncta labels layer you want to watershed from the *Select layer to watershed* dropdown menu. This should be the output from one of the automated labeling algorithms or your own annotations.
3. Select the labels layer you want as seed points from the *Select seed point layer* drop down menu. If you specify “None,” local minima are computed using this [function]. More on seed point layer generation can be found in the [Seed points] section. 
4. Select the elevation transform you want to use in the *Elevation map* dropdown menu.

    * The ***distance transformation*** creates basins with gradually increasing elevation. You can think of the basin shape as a valley. 

      Each label pixel is assigned a value equal to its Euclidean distance from its nearest background pixel, i.e., the further a puncta label pixel is from the background, the higher its pixel value will be. Since the center of each puncta label will have the highest elevation, the image will be negated to create basins. 

    * The ***Sobel filter*** is more edge aware and creates basins that are flat in the middle with large walls at its boundaries. You can think of the basin shape as a room in a      house.

      The gradient magnitude of each pixel is approximated. Since you have a binary mask, the gradient magnitude will be the largest and constant at the edges of your labels and 0 elsewhere. 

5. Click on the *Watershed* button to perform instance segmentation.

[function]: https://scikit-image.org/docs/0.25.x/api/skimage.morphology.html#skimage.morphology.local_minima
[Seed points]: /quantpunc/watershed-segmentation/seed-points