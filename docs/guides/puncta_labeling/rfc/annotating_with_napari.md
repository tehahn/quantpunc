---
title: "Annotating with Napari"
permalink: puncta-labeling/annotating-with-napari
parent: "Random forest classifier"
nav_order: 1
---

# Annotating using Napari
---

You want to “teach” the RFC to recognize edges so that it can be more robust against clumping. So, I suggest you label the edges of your puncta first and then use the fill bucket to label your puncta.

## Instructions
1. Create a labels layer by clicking on this icon: 
<br>
<img 
src="{{ '/assets/images/napari_labels.svg' | relative_url }}" 
alt="napari_labels" 
width="50" 
style="vertical-align: middle;">

2. You can rename it by selecting the labels layer in the layer list and double clicking it.
3. Click on the paint brush icon:
<br>
<img 
src="{{ '/assets/images/napari_paintbrush.svg' | relative_url }}" 
alt="napari_paintbrush" 
width="50" 
style="vertical-align: middle;">

4. Select the color you want to annotate your background with by using the + and - next to the *label* setting in the top left widget named layer controls. 
5. Adjust the brush size with the brush size slider so that you can draw accurate borders. I usually choose 1.
6. Label the edges of your puncta like this:
<br>
<img 
src="{{ '/assets/images/puncta_annotation_example.gif' | relative_url }}" 
alt="" 
width="500"
style="border-radius: 8px; max-width: 100%;">


7. Make the brush size larger (10 <) and create larger background annotations like this:
<br>
<img src="{{ '/assets/images/background_annotation_example.gif' | relative_url }}" 
alt="" 
width="500" 
style="border-radius: 8px; max-width: 100%;">

8. Click on the fill bucket in the layer controls widget.
9. Select the color you want to annotate your puncta.
10. Fill in your puncta.
<br>
<img 
src="{{ '/assets/images/fill_example.gif' | relative_url }}" 
alt="" 
width="500" 
style="border-radius: 8px; max-width: 100%;">

11. Try and label puncta of different sizes and brightness and segment out the ones in clusters. You only need to provide several training examples before you saturate the RFC, i.e., you don’t need to annotate the entire image.