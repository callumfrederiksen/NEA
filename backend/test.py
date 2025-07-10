import pandas as pd
import numpy as np

from losses import *
from activations import *
from main import NeuralNetwork

import matplotlib.pyplot as plt

df = pd.read_csv('./datasets/mnist_train.csv')

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

model = NeuralNetwork([784, 256, 128, 10], layer_activations=[ReLU, ReLU, Softmax], model_loss=CategoricalCrossEntropyWithSoftmax)
losses = model.fit(train_X, train_y, epochs=10, lr=0.001)

# plt.plot(losses)
# plt.show()
#

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

print(correct/total*100)
