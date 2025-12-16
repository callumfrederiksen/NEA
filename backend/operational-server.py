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
X_TRAIN_SPLIT = int(len(x) - (len(x) * train_test_split))

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

# Z-score normalisation

# Flat normalisation
x_train = x_train / 255
x_test = x_test / 255

# TODO

# Reshaping data
x_train, x_test = x_train.reshape(-1, 784, 1), x_test.reshape(-1, 784, 1)
y_train, y_test = y_train.reshape(-1, 10, 1), y_test.reshape(-1, 10, 1)

model = NeuralNetwork(
    [784, 256, 10],
    layer_activations=[ReLU, ReLU, Softmax],
    model_loss=CategoricalCrossEntropyWithSoftmax
)

losses = model.fit(x_train, y_train, 2, lr=0.001)

plt.plot(losses)
#plt.show()

# Verifying test accuracy

correct_counter = 0
total_counter = 0

for index, element in tqdm(enumerate(x_test)):
    element = np.array(element).reshape(1, 784, 1)
    prediction = model.forward(element)

    if int(np.argmax(prediction)) == int(np.argmax(y_test[index])):
        correct_counter += 1

    total_counter += 1

result = f'{(correct_counter / total_counter * 100):.2f}% accuracy'
json_post = {
    "accuracyMetric": result
}
requests.post("http://localhost:8443/returned-metrics", json_post)

plt.plot(losses)
plt.savefig("./src/uploads/losses.png", dpi=1000)
print(losses)
# requests.post("http://localhost:8443/post-loss-png-url", json={"urlSubmitted": True, 'pngUrl': './src/uploads/losses.png'})