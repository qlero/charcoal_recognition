"""
Downloads, unzips/extracts, and reformats the Charcoal images
provided by Laboratório Visão Robótica e Imagem in the following
link:
> https://web.inf.ufpr.br/vri/databases/charcoal/
"""

# Imports library

import numpy as np
import os

from PIL import Image

# Function declarations

def check_create_folder(
        path: str
    ) -> None:
    """
    Checks if a folder path exists and creates
    it if it does not.
    
    Parameters
    ----------
    path : String
        Path of the folder to check

    Returns
    -------
        None
    """
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"{path} created")

def crop_PIL_image(
        img: str, 
        crop_dims: tuple, 
        save_folder: str
    ) -> None:
    """
    Crops a PIL image and saves the cropped version in a
    specific folder.

    Parameters
    ----------
    img : string
        path to the .tiff PIL Image object (tested on .tiff)
        to crop
    crop_dims : Tuple
        Tuple of the form (l, t, b, r) where l, t are 0 and
        b corresponds to the width of the target crop and r
        corresponds to the height of the target crop
    save_filder : string
        Folder path where to save the cropped version
        of img

    Returns
    -------
        None
    """
    name = img.split("/")[-1]
    with Image.open(img) as i:
        i = i.crop(crop_dims)
        if not os.path.exists(save_folder):
            os.mkdir(save_folder)
        i.save(fp = f"{save_folder}{name}")


def plot_PIL_image(
        img: Image
    ) -> None:
    """
    Plots a .tiff PIL image.
    
    Parameters
    ----------
    img : PIL.TiffImagePlugin.TiffImageFile
        An .tiff PIL Image object (tested on .tiff)
    
    Returns
    -------
        None
    """
    plt.figure(figsize=(8,6))
    plt.imshow(np.asarray(img, dtype = np.uint8), cmap="gray")
    plt.title(image_files[0])
    plt.show()
