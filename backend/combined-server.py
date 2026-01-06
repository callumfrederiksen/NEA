import numpy as np
import matplotlib.pyplot as plt
import main
import activations
import losses
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm
import requests

#1 Get Hyperparamters
upload_path = requests.get("http://localhost:8443/has-uploaded").json()['filePath']
hyperparameters = requests.get("http://localhost:8443/return-hyperparameters").json()

#2 Read CSV
df = pd.read_csv(upload_path)

#3 Drop Columns

#3.1 Isolating the y column
y_column_name = requests.get("http://localhost:8443/return-select-y-column").json()['yColumnName']
y_column = df[y_column_name]
x_columns = df.drop(y_column_name, axis=1)

#3.2 Custom Drop Columns
columns_to_drop = [] # TODO: Add columns manually using trainable.studio
for column in columns_to_drop:
    x_columns.drop(column, axis=1)

#4 Cast to a numpy array
#4.1 Casting
x_columns = np.array(x_columns)
y_column = np.array(y_column)

#4.2 Reshaping X for model
raw_x_shape = hyperparameters['dataSetShape']
raw_y_shape = hyperparameters['yColumnSize']

def dataSetShapeToArray(raw_shape):
    shape = [-1]
    current_string = ""
    for l in raw_shape:
        if l != ",":
            current_string += l
        else:
            shape.append(int(current_string))
            current_string = ""
    shape.append(int(current_string))
    return shape

x_shape = dataSetShapeToArray(raw_x_shape)
y_shape = dataSetShapeToArray(raw_y_shape)

x_columns = x_columns.reshape(x_shape)
y_column = y_column.reshape(y_shape)
print(y_column.shape)
#5 Data Normalisation

def z_score(x):
    mean = np.mean(x)
    std = np.std(x)
    return (x - mean) / std

def min_max(x, scale_factor):
    return x / scale_factor

zScore = hyperparameters['zScoreVal']
minMax = hyperparameters['minMaxVal']

if zScore:
    x_columns = z_score(x_columns)
elif minMax:
    x_columns = min_max(x_columns, 255) # TODO: ENSURE /255 IS NOT HARDCODED

#6 One-hot encoding
oneHot = hyperparameters['oneHotVal']

def getUniqueValues(y):
    unique_values = []
    for data_point in y:
        if data_point not in unique_values:
            unique_values.append(int(data_point)) # TODO: TEST FOR A POINT OF ERROR
# TODO: MERGE SORT !!!!!!!!!!!!!!!!!!
    return unique_values

def one_hot_encode(y):
    return_y = []
    unique_values = getUniqueValues(y)
    for data_point in y:
        to_return = [0] * len(unique_values)
        index = unique_values.index(data_point)
        to_return[index] = 1
        return_y.append(to_return)

    return_y = np.array(return_y)
    return_y = return_y.reshape(-1, len(unique_values), 1)
    return return_y


if oneHot:
    y_column = one_hot_encode(y_column)
#7 Splits
total_size = x_columns.shape[0]
split = int(total_size * hyperparameters['testTrainSplit']) # // 1 # To round down if needed?

# The split works where a specific index, for example MNIST with a size of 60000 has a 0.8 test-train split
# This means that the FIRST 48000 data items will be designated for the test split
# The data items after item 48000 will be designated for the testing split (12000 items)

train_x = x_columns[:split]
test_x = x_columns[split:]
train_y = y_column[:split]
test_y = y_column[split:]

print(f'y: {train_y[9]}')
# Model definition

model_size = hyperparameters['modelSize']
for i in range(len(model_size)):
    model_size[i] = int(model_size[i])

layer_activations = hyperparameters['layerActivations']
model_loss = hyperparameters["modelLoss"]
activation_constructor = []
for layer in layer_activations:
    if layer == "ReLU":
        activation_constructor.append(activations.ReLU)
    elif layer == 'Sigmoid':
        activation_constructor.append(activations.Sigmoid)
    elif layer == 'SoftMax':
        activation_constructor.append(activations.Softmax)

loss_constructor = None
if model_loss == "CategoricalCrossEntropyWithSoftmax":
    loss_constructor = losses.CategoricalCrossEntropyWithSoftmax
elif model_loss == "SSE":
    loss_constructor = losses.SSE

model = main.NeuralNetwork(
    size=model_size,
    layer_activations=activation_constructor,
    model_loss=loss_constructor
)

epochs = int(hyperparameters['epochs'])
lr = float(hyperparameters['lr'])
print(f'Epochs: {epochs}, alpha: {lr}')

print(model_size)
print(train_x.shape)
print(train_y.shape)

losses = model.fit(
    train_x,
    train_y,
    epochs=epochs,
    lr=lr
)

plt.plot(losses)
plt.savefig("./src/uploads/losses.png", dpi=1000)

correct_counter = 0
total_counter = 0

for index, element in tqdm(enumerate(test_x)):
    element = np.array(element).reshape(1, 2, 1)
    prediction = model.forward(element)

    if int(np.argmax(prediction)) == int(np.argmax(test_y[index])):
        correct_counter += 1

    total_counter += 1

print(correct_counter/total_counter)
result = f'{(correct_counter / total_counter * 100):.2f}% accuracy'
