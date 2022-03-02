"""
Downloads, unzips/extracts, and reformats the Charcoal images
provided by Laboratório Visão Robótica e Imagem in the following
link:
> https://web.inf.ufpr.br/vri/databases/charcoal/
"""

# Imports library

import numpy as np
import os
import requests
import shutil

from PIL import Image
from zipfile import ZipFile

# Function declarations

rename_tif = lambda x: x + "f"
retrieve_tif = lambda x: x[-4:] == ".tif"
retrieve_tiff = lambda x: x[-5:] == ".tiff"
image_name_splitter = lambda x: (x, "_".join(x.split(" ")[:2]))

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

# Main scripts

if __name__ == "__main__":
    # Declares the target paths for downloading the
    # Charcoal dataset as a .zip file
    ufpr_dataset_url = "http://www.inf.ufpr.br/vri/databases/" + \
                       "florestais/charcoal.zip"
    ufpr_dataset_path = "dataset_ufpr/"
    ufpr_raw_dataset_path = f"{ufpr_dataset_path}charcoal/"
    ufpr_cleaned_dataset_path = f"{ufpr_dataset_path}cleaned/"
    ufpr_dataset_zip_path = f"{ufpr_dataset_path}charcoal.zip"
    # Checks whether to create the dataset folder
    check_create_folder(ufpr_dataset_path)
    check_create_folder(ufpr_cleaned_dataset_path)
    # Retrieves the raw data as a .zip file
    print("Downloading the Charcoal dataset")
    #charcoal_file = requests.get(ufpr_dataset_url)
    #with open(ufpr_dataset_zip_path, "wb") as f:
    #    f.write(charcoal_file.content)
    #print("Done")
    # Extract the content of the zip
    with ZipFile(ufpr_dataset_zip_path) as z:
        print(f"Extracting all files")
        z.extractall(ufpr_dataset_path)
        print("Done")
    # Finds all .tif images that were extracted
    images = sorted(os.listdir(ufpr_raw_dataset_path))
    images = list(filter(retrieve_tif, images))
    # Renames .tif images to .tiff
    print("Changing extensions from .tif to .tiff")
    for img in images:
        old = f"{ufpr_raw_dataset_path}{img}"
        new = f"{old}f"
        os.rename(old, new)
    print("Done")
    # Updates the list of .tif images to tiff
    images = list(map(rename_tif, images))
    images = list(map(image_name_splitter, images))
    # Crops and exports in the cleaned folder all the
    # tiff images
    print("Cropping the metadata banner from the .tiff files")
    for img in images:
        crop_PIL_image(
            f"{ufpr_raw_dataset_path}{img[0]}", 
            (0, 0, 1280, 960), 
            f"{ufpr_cleaned_dataset_path}{img[1]}/"
        )
    print("Done")
    # Removes the possibly created __MACOSX folder
    print("Cleanup")
    if os.path.exists(f"{ufpr_dataset_path}__MACOSX/"):
        shutil.rmtree(f"{ufpr_dataset_path}__MACOSX/")
    print("Done")
