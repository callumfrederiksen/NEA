import pandas
import numpy as np
from sklearn.datasets import make_moons

def z_score(x):
    mean = np.mean(x)
    std = np.std(x)

    return (x - mean) / std

x, y = make_moons(100000, noise=0.1)

#RESHAPE Y - A
y = y.reshape(-1, 1)

data = []
for i in range(len(x)):
    data.append(x[i].tolist() + y[i].tolist())

data = np.array(data)
columns = ['x', 'y', 'label']

df = pandas.DataFrame(data = data, columns=columns)
df.to_csv("./moons.csv")