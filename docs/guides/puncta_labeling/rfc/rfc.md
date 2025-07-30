---
title: "Random forest classifier"
permalink: puncta-labeling/rfc
parent: "Puncta labeling"
nav_order: 1
has_toc: false
---

# Random forest classifier
---

This guide will show you how to use QuantPunc's random forest classifier (RFC). The RFC is more generalizable than skimage's blob counting algorithms which can lead to more accurate puncta labels. 

## Instructions
1. Select “Random Forest Classifier” from the *Method* dropdown menu.
2. The RFC requires annotations for both puncta and background. You can either:

    * [Create them through Napari]
    * [Provide your own annotations]

3. Select your annotated layer using the *Select annotated layer* dropdown menu.
4. Enter the integer value associated with your puncta labels in *puncta_label*.
5. Enter the integer value associated with your background labels in *background_label*.
6. Click on *Train*.
7. A message saying “Training complete.” should pop up indicating that your RFC has been trained.
8. Enter a value into *label_color* for your puncta labels and click on *Label puncta* to segment your puncta. 

[Create them through Napari]: /quantpunc/puncta-labeling/annotating-with-napari
[Provide your own annotations]: /quantpunc/puncta-labeling/provide-own-annotations