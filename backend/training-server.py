import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from main import *
from losses import *
from activations import *

file_path = requests.get("http://localhost:8443/has-uploaded").json()['filePath']
df = pd.read_csv(file_path)

hyperparameters = requests.get("http://localhost:8443/return-hyperparameters").json()
print(hyperparameters)

model_size = hyperparameters['modelSize']

layer_activations = []
for activation in hyperparameters['layerActivations']:
    if activation == 'Sigmoid':
        layer_activations.append(Sigmoid)
    elif activation == 'ReLU':
        layer_activations.append(ReLU)
    elif activation == 'Softmax':
        layer_activations.append(Softmax)

model_loss = None
if hyperparameters['modelLoss'] == 'SSE':
    model_loss = SSE
elif hyperparameters['modelLoss'] == 'CategoricalCrossEntropyWithSoftmax':
    model_loss = CategoricalCrossEntropyWithSoftmax

