"""
Tests the instantiation of PyTorch dataloaders over the
cleaned images from the Laboratório Visão Robótica e Imagem 
charcoal dataset
"""

# Imports library

import torch
import os, sys 
# used to declare ../charcoal as a folder that can be imported
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from charcoal.generator_models import generate_model

# Main scripts

if __name__ == "__main__":
    print("Test declaration AlexNet + Adam")
    model, optimizer, criterion = generate_model()
    print("DONE")
    print("Test declaration AlexNet + SGD")
    model, optimizer, criterion = generate_model(optimizer="sgd")
    print("DONE")
    print("Test declaration VGG11")
    model, optimizer, criterion = generate_model(model="vgg")
    print("DONE")
    print("Test declaration ResNet18")
    model, optimizer, criterion = generate_model(model="resnet18")
    print("DONE")
    print("Test declaration ResNet50")
    model, optimizer, criterion = generate_model(model="restnet50")
    print("DONE")
    print("Test declaration convnext_tiny")
    model, optimizer, criterion = generate_model(model="convnext_tiny")
    print("DONE")
