import main
import losses
import activations

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tools import Tools


w = np.load("./backend/weights.npy", allow_pickle=True).tolist()
b = np.load("./backend/biases.npy", allow_pickle=True).tolist()

tools = Tools()

df = np.array(pd.read_csv("./src/uploads/mnist_train.csv"))
y = df[:,0].reshape(-1,1)
x = df[:,1:].reshape(-1, 784, 1)

x = tools._z_score(x)
y = tools._one_hot_encode(y)

model = main.NeuralNetwork([784, 128, 128, 10],
                           [activations.ReLU,activations.ReLU,activations.ReLU,activations.Softmax],
                           losses.CategoricalCrossEntropyWithSoftmax,
                           weights=w,
                           biases=b
                           )

print(model.forward(x[8]))
print(y[8])