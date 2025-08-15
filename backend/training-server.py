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

# CHANGE - COPIED FROM backend/test.py - SUITED FOR MNIST ONLY!
train_df = np.array(df)
train_X, train_y = train_df[:48000,1:], train_df[:,0]
test_X = np.array(train_df[48000:,1:]) / 255
train_y = train_y.tolist()
for i in range(len(train_y)):
    toadd = [0]*10
    toadd[train_y[i]] = 1
    train_y[i] = toadd

train_X = np.array(train_X / 255).reshape(-1, 784, 1)
train_y = np.array(train_y).reshape(-1, 10, 1)
train_y, test_y = train_y[:48000], train_y[48000:]

model = NeuralNetwork(model_size, layer_activations=layer_activations, model_loss=model_loss)
losses = model.fit(train_X, train_y, epochs=2, lr=0.001)


plt.plot(losses)
plt.show()


test_X = test_X.reshape(-1, 784, 1)
test_y = test_y.reshape(-1, 10, 1)
correct = 0
total = 0
for i, sample in enumerate(test_X):
    prediction = model.forward(sample)
    one_hot = np.zeros_like(prediction)
    one_hot[np.argmax(prediction)] = 1


    if np.array_equal(one_hot.reshape(10), test_y[i].reshape(10)): correct += 1
    total += 1

print(f'{correct/total*100:.2f}% accuracy')
