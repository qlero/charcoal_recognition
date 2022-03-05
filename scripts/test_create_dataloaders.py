"""
Tests the instantiation of PyTorch dataloaders over the
cleaned images from the Laboratório Visão Robótica e Imagem 
charcoal dataset
"""

# Imports library

import os, sys 
# used to declare ../charcoal as a folder that can be imported
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from charcoal.generator_dataloaders import generate_dataloaders

# Main scripts

if __name__ == "__main__":
    # Declares the target path for the dataset
    ufpr_dataset_path = "dataset_ufpr/cleaned/"
    print("Imports training, validation, and test dataloaders")
    classes, datasets, dataloaders = generate_dataloaders(ufpr_dataset_path)
    print("DONE")
    print("\nImported Classes")
    print(", ".join(classes))
    print("\nImported datasets")
    print(datasets)
    print("\nImported dataloaders")
    print(dataloaders)