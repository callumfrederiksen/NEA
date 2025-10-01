import requests
import time

import pandas as pd
import numpy as np

from losses import *
from activations import *
from main import NeuralNetwork

import matplotlib.pyplot as plt

from tqdm import tqdm

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

x_train, x_test = x[X_TRAIN_SPLIT:], x[:X_TRAIN_SPLIT]
y_train, y_test = y[X_TRAIN_SPLIT:].reshape(-1, 1), y[:X_TRAIN_SPLIT].reshape(-1, 1)

# One hot encoding
def one_hot_encode(y, possible_values=10): # possible values represents the range of possible values
    y = y.tolist()
    for index, data_point in tqdm(enumerate(y)):
        to_add = [0] * possible_values # Empty one hot encoding generator
        to_add[int(data_point[0])] = 1

        y[index] = to_add
    y = np.array(y)
    return y

y_train, y_test = one_hot_encode(y_train), one_hot_encode(y_test)

