# Content

This repository covers the exploration of various supervised recognition techniques applied to the 44-species wood charcoal databased introduced by Maruyama, T., Oliveira, L. S., Britto Jr, Nisgoski, S., Automatic Classification of Native Wood Charcoal, Ecological Informatics, 48:1-7, 2018.

### Folder content

`charcoal` contains a set of files (e.g. .py, .ipynb) used to explore the dataset, train models, etc.

`dataset_ufpr` is dedicated to holding the dataset itself (as raw and cleaned .tif/.tiff images).

`scripts` contains .py scripts that can be ran from the root to perform given tasks.

### Working scripts

#### `dataset.py`

This scripts downloads the raw dataset from its internet archive (.zip file), extracts the content, incl. the .tif images, and performs a cleanup step that removes the metadata banner from each images. The cleaned images are stored as .tiff files in the subfolder `dataset_ufpr/cleaned`. Raw dataset remains available in the subfolder `dataset_ufpr/charcoal`.
