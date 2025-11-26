import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from main import NeuralNetwork
from losses import *
from activations import *

# DATA PREPROP
df = pd.read_csv('other/moons.csv')
df = df.drop(df.columns[0], axis=1)

print(df.head())

def z_score(x):
    mean = np.mean(x)
    std = np.std(x)

    return (x - mean) / std

df = np.array(df).T
x, x_test = df[:2].T.reshape(-1, 2, 1)[:80000], df[:2].T.reshape(-1, 2, 1)[80000:]
y, y_test = df[-1].T.reshape(-1, 1, 1)[:80000], df[-1].T.reshape(-1, 1, 1)[80000:]
print(x.shape)
print(y.shape)

# Model construction

model = NeuralNetwork(
    [2, 128, 64, 1],
    layer_activations=[ReLU, ReLU, Sigmoid],
    model_loss=SSE
)

losses = model.fit(x, y, epochs=10, lr=0.001)
plt.plot(losses)
plt.show()

#prediction



correct = 0
total  = 0

for i in range(20000):
    pred = model.forward(x_test[i].reshape(1, 2, 1))[0][0][0]
    if pred > 0.5: pred = 1
    else: pred = 0
    
    act = int(y_test[i][0][0])
    if pred == act: correct += 1
    total += 1


print(f'{correct/total*100:.2f}%')

