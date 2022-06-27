"""
Tests the instantiation of PyTorch dataloaders over the
cleaned images from the Laboratório Visão Robótica e Imagem 
charcoal dataset
"""

# Imports library

import copy
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

from sklearn.svm import SVC

import os, sys 
# used to declare ../charcoal as a folder that can be imported
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from charcoal.generator_dataloaders import generate_dataloaders
from charcoal.generator_models import generate_model

# Main scripts

if __name__ == "__main__":
	
	print("STEP 1: Parameter Declaration\n")
	
	# Declares parameters
	optimizer		  = "sgd"
	model			  = "convnext_tiny"
	ufpr_dataset_path = "dataset_ufpr/cleaned/"
	device			  = torch.device("cpu")
	batch_size		  = 128
	train_size		  = 2/3
	n_epochs          = 2
	
	print("STEP 2: Generating Dataloaders\n")
	
	# Imports training, validation, and test dataloaders
	classes, datasets, dataloaders = generate_dataloaders(ufpr_dataset_path,
														  batch_size = batch_size,
														  train_size = train_size)
	# Placeholder tensor to retrieve the training set
	
	X_train, Y_train = torch.tensor([]), torch.tensor([])
	X_test, Y_test = torch.tensor([]), torch.tensor([])
	while X_train.shape[0]<10000:
		for x, y in dataloaders["train"]:
			X_train = torch.cat([X_train, x])
			Y_train = torch.cat([Y_train, y])

	for x, y in dataloaders["test"]:
		X_test = torch.cat([X_test, x])
		Y_test = torch.cat([Y_test, y])

	print(X_train.shape, X_train.reshape(X_train.shape[0], -1).shape)

	print("STEP 3: Generating Models: SVM, ResNet18\n")
	
	print("STEP 3.1: Generating SVM\n")
	
	
	
	print("STEP 3.2: Generating ResNet18\n")
	
	# Generates model and modifies the input layer
	resnet, optimizer, criterion = generate_model(model = "resnet18",
			 									  optimizer = optimizer)
	resnet.conv1 = nn.Conv2d(3, 64, kernel_size=(3,3),stride=(1,1), padding=(1,1), bias=False)
	resnet.fc	= nn.Linear(in_features=512, out_features=len(classes), bias=True)
	
	# Modify the input and output layers of the model
	resnet.to(device)
	best_model = copy.deepcopy(resnet.state_dict())
	best_acc = 0
	
	for epoch in range(n_epochs):
		print(f"Epoch {epoch}/{n_epochs}")
		for phase in ["train", "val"]:
			if phase == "train":
				resnet.train()
			else:
				resnet.eval()
			running_loss = 0.
			running_corrects = 0
			for X_phase, y_phase in dataloaders[phase]:
				optimizer.zero_grad()
				outputs = resnet(X_phase.float().to(device)).to("cpu")
				_, preds = torch.max(outputs, 1)
				loss = criterion(outputs, y_phase)
				if phase == "train":
					loss.backward()
					optimizer.step()
				running_loss += loss.item() * X_phase.size(0)
				running_corrects += torch.sum(preds == y_phase.data)
			
			epoch_loss = running_loss / len(datasets[phase])
			epoch_acc = running_corrects.double() / len(datasets[phase])
			print(f'{phase} Loss: {epoch_loss:.4f} Acc: {epoch_acc:.4f}')
			
			# deep copy the model
			if phase == 'val' and epoch_acc > best_acc:
				best_acc = epoch_acc
				best_model_wts = copy.deepcopy(resnet.state_dict())

	
	
	
	
