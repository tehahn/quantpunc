---
title: "Preprocessing"
permalink: /preprocessing
nav_order: 3
---
# Preprocessing

---

**Preprocessing is optional, but highly recommended. If your image has good contrast and contains minimal noise, you can skip this step.**

Your image is first denoised with wavelet thresholding and then its contrast is increased through adaptive histogram equalization. This will enhance edge information between the puncta and background which improves the performance of QuantPunc’s automated segmentation methods. To learn more about the preprocessing methods used you can review these resources linked below: 

1. [Wavelet denoising]
2. [Histogram equalization]

## Instructions
1. Select your image from the *Select layer dropdown* menu.
2. Select the mode from the *Denoising mode* dropdown menu.

    * ***Soft thresholding*** will create a smoother looking image but can lead to some loss of edge information. This occurs by setting the wavelet coefficients of your image below a threshold to 0 while shrinking the other coefficients towards 0. 

    * ***Hard thresholding*** will create an image with sharp edges but can introduce artifacts. This occurs by setting the wavelet coefficients of your image below a threshold to 0 while leaving the other coefficients untouched. 

3. Select the method you want to use in the *Thresholding method* dropdown menu.

    * ***VisuShrink*** will remove most of the fine textures in your image but is more effective at reducing noise. This does so by applying a global threshold across all wavelet coefficients.

    * ***BayesShrink*** will create an image that preserves fine textures in your image but may be less effective at reducing noise. This does so by applying a local threshold for each set of wavelet coefficients.

4. Click on the *Process button* to preprocess your image. A new layer named after your image with "_processed" as its suffix (e.g., your_image_processed) will now be in the layers list.

[Wavelet denoising]: https://scikit-image.org/docs/stable/auto_examples/filters/plot_denoise_wavelet.html
[Histogram equalization]: https://scikit-image.org/docs/0.25.x/auto_examples/color_exposure/plot_equalize.html