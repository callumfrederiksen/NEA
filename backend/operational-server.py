import requests
import time

import pandas as pd
import numpy as np

from losses import *
from activations import *
from main import NeuralNetwork

import matplotlib.pyplot as plt

'''
submitted
modelSize
layerActivations
modelLoss
testTrainSplit - NEEDS NAME UPDATING :-)
dataSetShape
yColumnSize
'''

# Calling API to see if the file has been uploaded
while True: #basic while loop - NEEDS UPDATING!!!!!!
    res = requests.get("http://localhost:8443/return-hyperparameters").json()

    if res['submitted']:
        break

    time.sleep(1)

# Loading Variables and hyperparameters
model_size = res['modelSize']
layer_activations_str = res['layerActivations']
model_loss = res['modelLoss']
train_test_split = res['testTrainSplit']
dataset_shape = res['dataSetShape']
y_column_size = res['yColumnSize']

file_path = requests.get("http://localhost:8443/has-uploaded").json()['filePath']
y_column_name = requests.get("http://localhost:8443/return-select-y-column").json()['yColumnName']

# Reading CSV
df = pd.read_csv(file_path)

#  X - columns
x = df.drop(y_column_name, axis=1)
x = np.array(x)

#  Y - columns
y = df[y_column_name]
y = np.array(y)

# Train-test splits and shape normalisation
X_TRAIN_SPLIT = int(len(x) * train_test_split)

X_TRAIN, X_TEST = x[X_TRAIN_SPLIT:], x[:X_TRAIN_SPLIT]
Y_TRAIN, Y_TEST = y[X_TRAIN_SPLIT:].reshape(-1, 1), y[:X_TRAIN_SPLIT].reshape(-1, 1)

