---
title: "About"
nav_order: 1
---

<pre style="font-size: 0.7em; line-height: 1.2;">

 ________  ___  ___  ________  ________   _________  ________  ___  ___  ________   ________     
|\   __  \|\  \|\  \|\   __  \|\   ___  \|\___   ___\\   __  \|\  \|\  \|\   ___  \|\   ____\    
\ \  \|\  \ \  \\\  \ \  \|\  \ \  \\ \  \|___ \  \_\ \  \|\  \ \  \\\  \ \  \\ \  \ \  \___|    
 \ \  \\\  \ \  \\\  \ \   __  \ \  \\ \  \   \ \  \ \ \   ____\ \  \\\  \ \  \\ \  \ \  \       
  \ \  \\\  \ \  \\\  \ \  \ \  \ \  \\ \  \   \ \  \ \ \  \___|\ \  \\\  \ \  \\ \  \ \  \____  
   \ \_____  \ \_______\ \__\ \__\ \__\\ \__\   \ \__\ \ \__\    \ \_______\ \__\\ \__\ \_______\
    \|___| \__\|_______|\|__|\|__|\|__| \|__|    \|__|  \|__|     \|_______|\|__| \|__|\|_______|
          \|__|                                                                                  

</pre>

[QuantPunc] is a Napari plugin for puncta analysis and quantification in 2D microscopy images.

QuantPunc is currently in beta. Please report any problems to the [issues page].


## Features
1. Automated puncta labeling and counting
2. Watershed segmentation
3. Colocalization analysis 
4. Exportable counts and stats


## Installation
You can install `quantpunc` via Napari's plugin manager:

1. Click on "Plugins" in the toolbar.
2. Click on "Install/Uninstall Plugins..." in the context menu.
3. Type "quantpunc" in the searchbar.
4. Click install.

You can also install `quantpunc` via [pip]:

    pip install quantpunc


## Puncta Quantification and Workflow
Here’s an overview of the ideal workflow for puncta segmentation and quantification. This is the recommended way of using QuantPunc. However, QuantPunc’s widgets are modularly designed so that they can be used as standalone tools. In-depth instructions can be found by clicking on a step or using the navbar.

1. [Load a 2D image]
2. [Preprocessing] (optional but recommended)
3. [Automated labeling] via:
    * [Random forest classification] 
    * [skimage blob detection]
4. [Manual labeling]
5. [Watershed segmentation] (optional)
6. [Puncta counting]
7. [Colocalization analysis] (optional)
8. [Displaying stats and saving]


[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[pip]: https://pypi.org/project/pip/

[QuantPunc]: https://github.com/tehahn/quantpunc
[issues page]: https://github.com/tehahn/quantpunc/issues

[Load a 2D image]: /quantpunc/loading-an-image
[Preprocessing]: /quantpunc/preprocessing
[Automated labeling]: /quantpunc/puncta-labeling/general-usage
[Random forest classification]: /quantpunc/puncta-labeling/rfc
[skimage blob detection]: /quantpunc/puncta-labeling/skimage-blob-detection
[Manual labeling]: /quantpunc/puncta-labeling/manual-labeling
[Watershed segmentation]: /quantpunc/watershed-segmentation
[Puncta counting]: /quantpunc/puncta-counting
[Colocalization analysis]: /quantpunc/colocalization
[Displaying stats and saving]: /quantpunc/saving-your-data