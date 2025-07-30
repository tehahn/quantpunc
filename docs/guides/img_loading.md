---
title: "Loading an image"
permalink: /loading-an-image
nav_order: 2
---

# Loading an image
---

First load an image in Napari. **The primary image formats supported are TIFs, PNGs, JPEGs/JPGs, BMPs, and GIFs.**

### There are two ways you can do this:

* You can drag and drop an image into Napari from file explorer or your desktop. 

* You can use Napari’s toolbar to load an image:

  1. Click on “File.”
  2. Click on “Open File(s)...” from the context menu.
  3. Select an image from file explorer.
  4. Alternatively you can use ctrl + o to instantly bring up file explorer.

## **Ensure that the image you loaded is a 2D image. QuantPunc only supports 2D images.** 

<br>

You can check this by looking to see if there’s a scroll bar at the bottom of the GUI as displayed here:

<img 
src="{{ '/assets/images/scrollbar.png' | relative_url }}" 
alt="scrollbar"
height="100"
width="1000" 
style="border-radius: 8px; max-width: 100%;">

### If you see a scroll bar, that means you’ve uploaded a multi-layer image. 

To split image stacks:

1. Load your image stack as detailed above
2. Right click on the layer you want to split.
3. Click on "Split Stack" from the context menu.
4. Repeat this process if you have an image stack that exceeds 3 dimensions.
