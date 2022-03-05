"""
Instantiates the cleaned images from the Laboratório Visão 
Robótica e Imagem charcoal dataset as PyTorch dataloaders
"""

# Imports library

import os
import torch

from torch.utils.data import random_split, DataLoader
from torchvision.datasets import ImageFolder
from torchvision import transforms as tf

# global variable declarations

TRANSFORM = tf.Compose([
    tf.RandomResizedCrop(64),
    tf.RandomRotation(180),
    tf.PILToTensor(),
    tf.ConvertImageDtype(torch.float64),
    tf.Normalize(mean=[0.5],std=[0.5]),
])

# Function declarations

def generate_dataloaders(
        path: str, 
        batch_size: int = 128, 
        train_size: float = 2/3,
        transform: tf.transforms = None
    ) -> tuple:
    """
    Given a folder path to the cleaned (i.e. without banner)
    Charcoal images, return the training, validation and test
    dataloaders.
    
    Parameters
    ----------
    path : str
        path to the cleaned data folder to retrieve
        images from to build dataloaders
    batch_size : float, optional
        Batch size for the dataloaders
    train_size : float, optional
        % split of images to allocated to the training
        dataset (validation and test sets are split 50/50
        with the remainder)
    transform : tf.transforms
        Torchvision Transform object to apply pre-processing
        to the datasets
    
    Returns
    -------
        Tuple of:
            - list of classes
            - PyTorch datasets (training, validation,test)
            - PyTorch dataloaders (training, validation, test)
    """
    # Instantiates the image data into a PyTorch
    # ImageFolder object
    if transform is None:
        transform = TRANSFORM
    dataset = ImageFolder(path, transform = transform)
    classes = dataset.classes
    # Computes the number of images to allocate to
    # each subset: training, validation, test
    nb_images = sum([len(folder[2]) 
                     for folder in list(os.walk(path))])
    train_count = int(nb_images*train_size)
    valid_count = int(nb_images*(1-train_size)/2)
    test_count = nb_images - train_count - valid_count
    # Random splits the images between training, validation
    # and test datasets
    train_dataset, valid_dataset, test_dataset = random_split(
        dataset,
        (train_count, valid_count, test_count)
    )
    # Computes the dataloaders
    train_dataset_loader = DataLoader(
        train_dataset, 
        batch_size=batch_size, 
        shuffle=True, 
        num_workers=4
    )
    valid_dataset_loader = DataLoader(
        valid_dataset, 
        batch_size=batch_size, 
        shuffle=True, 
        num_workers=4
    )
    test_dataset_loader = DataLoader(
        test_dataset, 
        batch_size=batch_size, 
        shuffle=True, 
        num_workers=4
    )
    # Computes the return objects
    datasets = {
        "train": train_dataset,
        "val": valid_dataset,
        "test": test_dataset
    }
    dataloaders = {
        "train": train_dataset_loader,
        "val": valid_dataset_loader,
        "test": test_dataset_loader
    }
    return classes, datasets, dataloaders