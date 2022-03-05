"""
Instantiates the cleaned images from the Laboratório Visão 
Robótica e Imagem charcoal dataset as PyTorch dataloaders
"""

# Imports library

import torch.nn as nn
import torch.optim as optim

from torchvision import models

# Function declarations

def generate_model(
        model: str = "alexnet",
        optimizer: str = "Adam",
        optimizer_parameters: dict = {},
        pretrained: bool = False
    ):
    """
    Outputs a PyTorch model with criterion and optimizer
    for use during a machine learning process.
    
    Parameters
    ----------
    model : string, optional
        String name of the model to generate.
        covered models: AlexNet, VGG11, ResNet18, ResNet50
    optimizer : string, optional
        String name of the optimizer to use.
        covered optimizers: Adam, SGD
    optimizer_parameters : dict, optional
        Dictionary of parameters for the optimizer
        input by the user as declaration
    pretrained : boolean, optional
        Indicates whether the model to generate fetches
        pretrained weights
        
    Returns 
    -------
        
    """
    # Retrieves existing parameters from the input
    # optimizer_parameters
    # > default SGD parameters
    lr_sgd = 0.1
    momentum = 0
    dampening = 0
    weight_decay_sgd = 0
    nesterov = False
    # > default Adam parameters
    lr_adam = 0.001
    betas = (0.9, 0.999)
    eps = 1e-08
    weight_decay_adam = 0
    amsgrad = False
    # Updates base parameters
    if len(optimizer_parameters) != 0:
        if "lr" in optimizer_parameters.keys():
            lr = optimizer_parameters["lr"]
            lr_sgd = lr
            lr_adam = lr
            print(f"Optim. lr updated to {lr}")
        if "momentum" in optimizer_parameters.keys():
            momentum = optimizer_parameters["momentum"]
            print(f"Optim. momentum updated to {momentum}")
        if "dampening" in optimizer_parameters.keys():
            dampening = optimizer_parameters["dampening"]
            print(f"Optim. dampening updated to {dampening}")
        if "weight_decay" in optimizer_parameters.keys():
            weight_decay = optimizer_parameters["weight_decay"]
            weight_decay_sgd = weight_decay
            weight_decay_adam = weight_decay
            print(f"Optim. weight_decay update to {weight_decay}")
        if "nesterov" in optimizer_parameters.keys():
            nesterov = optimizer_parameters["nesterov"]
            print(f"Optim. nesterov update to {nesterov}")
        if "betas" in optimizer_parameters.keys():
            betas = optimizer_parameters["betas"]
            print(f"Optim. betas update to {betas}")
        if "eps" in optimizer_parameters.keys():
            eps = optimizer_parameters["eps"]
            print(f"Optim. eps update to {eps}")
        if "amsgrad" in optimizer_parameters.keys():
            amsgrad = optimizer_parameters["amsgrad"]
            print(f"Optim. amsgrad update to {amsgrad}")
    # Generates the baseline model
    if model == "alexnet":
        model = models.AlexNet() # AN does not have the arg "pretrained"
        print("AlexNet model loaded")
    elif model in ["vgg", "vgg11"]:
        model = models.vgg11(pretrained=pretrained)
        print("VGG11 model loaded")
    elif model in ["resnet18", "resnet"]:
        model = models.resnet18(pretrained=pretrained)
        print("ResNet18 model loaded")
    elif model == "resnet50":
        model = models.resnet50(pretrained=pretrained)
        print("ResNet50 model loaded")
    else:
        model = models.AlexNet()
        print("AlexNet model loaded")
    # Generates the optimizer
    if optimizer == "adam":
        opt = optim.Adam(
            lr = lr_adam,
            betas = betas,
            eps = eps,
            weight_decay = weight_decay_adam
        )
    elif optimizer == "sgd":
        opt = optim.SGD(
            model.parameters(),
            lr = lr_adam,
            momentum = momentum,
            dampening = dampening,
            weight_decay = weight_decay_sgd,
            nesterov = nesterov
        )
    else: 
        opt = optim.Adam(
            model.parameters(),
            lr = lr_adam,
            betas = betas,
            eps = eps,
            weight_decay = weight_decay_adam
        )
    # returns the model, the optimizer, and the criterion
    return model, opt, nn.CrossEntropyLoss()