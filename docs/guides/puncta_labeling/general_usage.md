---
title: "Puncta labeling"
permalink: puncta-labeling/general-usage
nav_order: 4
has_toc: false
---

# General usage
---

1. Select the *Puncta Labeling* tab in the middle widget if it hasn’t already been selected.
2. Select the layer you want to label puncta from the *Select layer* dropdown menu.
3. You can select an image with ROIs from the *Select mask* dropdown menu if you have one. Otherwise, you can keep the default selection at “None” which will label all the puncta in your image. Providing a mask layer will only label puncta in those ROIs.
4. Select the method you want to use to label your puncta from the *Method* dropdown menu. 
5. Provide the required inputs for the method you selected. More details can be found here:

    * [Random forest classifier]
    * [Skimage blob detection]
    * [Manual labeling]

6. Specify the color of your puncta labels by entering an integer value in *label_color*.
7. Click on the *Label puncta* button.

The name of your puncta labels layer will always have the suffix "_puncta". If you want to keep the outputs of different puncta labelers, simply rename your puncta labels layer to something else. 

QuantPunc has two automated puncta labeling methods. One of them uses parameterized algorithms from skimage’s blob detection methods and the other uses a random forest classifier that uses features inspired by [ilastik].

[Random forest classifier]: /quantpunc/puncta-labeling/rfc
[Skimage blob detection]: /quantpunc/puncta-labeling/skimage-blob-detection
[Manual labeling]: /quantpunc/puncta-labeling/manual-labeling
[ilastik]: https://www.ilastik.org/