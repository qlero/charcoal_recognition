"""
Downloads, unzips/extracts, and reformats the Charcoal images
provided by Laboratório Visão Robótica e Imagem in the following
link:
> https://web.inf.ufpr.br/vri/databases/charcoal/
"""

# Imports library

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import requests
import shutil

from charcoal.functions import check_create_folder
from charcoal.functions import crop_PIL_image
from charcoal.functions import check_create_folder
from zipfile import ZipFile

# Function declarations

rename_tif = lambda x: x + "f"
retrieve_tif = lambda x: x[-4:] == ".tif"
retrieve_tiff = lambda x: x[-5:] == ".tiff"
image_name_splitter = lambda x: (x, "_".join(x.split(" ")[:2]))

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
