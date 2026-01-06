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

class CombinedServer:
    def __init__(self):
        self.__url = "http://localhost:8443"

    def __get_hyperparameters(self):
        self.__upload_path = requests.get("http://localhost:8443/has-uploaded").json()['filePath']
        self.__hyperparameters = requests.get("http://localhost:8443/return-hyperparameters").json()

    def __read_and_drop_csv(self):
        #2 Read CSV
        self.__df = pd.read_csv(self.__upload_path)

        #3 Drop Columns
        #3.1 Isolating the y column
        self.__y_column_name = requests.get("http://localhost:8443/return-select-y-column").json()['yColumnName']
        self.__y_column = self.__df[self.__y_column_name]
        self.__x_columns = self.__df.drop(self.__y_column_name, axis=1)

        # #3.2 Custom Drop Columns'
        # columns_to_drop = [] # TODO: Add columns manually using trainable.studio
        # for column in columns_to_drop:
        #     x_columns.drop(column, axis=1)'

    def __dataSetShapeToArray(self, raw_shape):
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

    def __np_casting(self):
        #4 Cast to a numpy array
        #4.1 Casting
        self.__x_columns = np.array(self.__x_columns)
        self.__y_column = np.array(self.__y_column)

        #4.2 Reshaping X for model
        raw_x_shape = self.__hyperparameters['dataSetShape']
        raw_y_shape = self.__hyperparameters['yColumnSize']



        x_shape = self.__dataSetShapeToArray(raw_x_shape)
        y_shape = self.__dataSetShapeToArray(raw_y_shape)

        self.__x_columns = self.__x_columns.reshape(x_shape)
        self.__y_column = self.__y_column.reshape(y_shape)

    def __z_score(self, x):
        mean = np.mean(x)
        std = np.std(x)
        return (x - mean) / std

    def __min_max(self, x, scale_factor):
        return x / scale_factor

    def __getUniqueValues(self, y):
        unique_values = []
        for data_point in y:
            if data_point not in unique_values:
                unique_values.append(int(data_point)) # TODO: TEST FOR A POINT OF ERROR
        # TODO: MERGE SORT !!!!!!!!!!!!!!!!!!
        return unique_values

    def __one_hot_encode(self, y):
        return_y = []
        unique_values = self.__getUniqueValues(y)
        for data_point in y:
            to_return = [0] * len(unique_values)
            index = unique_values.index(data_point)
            to_return[index] = 1
            return_y.append(to_return)

        return_y = np.array(return_y)
        return_y = return_y.reshape(-1, len(unique_values), 1)
        return return_y

    def __data_normalisation_and_one_hot(self):
        zScore = self.__hyperparameters['zScoreVal']
        minMax = self.__hyperparameters['minMaxVal']

        if zScore:
            self.__x_columns = self.__z_score(self.__x_columns)
        elif minMax:
            self.__x_columns = self.__min_max(self.__x_columns, 255) # TODO: ENSURE /255 IS NOT HARDCODED

        #6 One-hot encoding
        oneHot = self.__hyperparameters['oneHotVal']
        print("y before one-hot:", type(self.__y_column), np.asarray(self.__y_column).shape)
        print("first item type/shape:", type(self.__y_column[0]), np.asarray(self.__y_column[0]).shape)
        print("yColumnSize raw:", self.__hyperparameters["yColumnSize"])

        if oneHot:
            self.__y_column = self.__one_hot_encode(self.__y_column)

    def __generate_splits(self):
        # The split works where a specific index, for example MNIST with a size of 60000 has a 0.8 test-train split
        # This means that the FIRST 48000 data items will be designated for the test split
        # The data items after item 48000 will be designated for the testing split (12000 items)
        total_size = self.__x_columns.shape[0]
        split = int(total_size * self.__hyperparameters['testTrainSplit'])

        self.__train_x = self.__x_columns[:split]
        self.__test_x = self.__x_columns[split:]
        self.__train_y = self.__y_column[:split]
        self.__test_y = self.__y_column[split:]

    def __model_definition(self):
        model_size = self.__hyperparameters['modelSize']
        for i in range(len(model_size)):
            model_size[i] = int(model_size[i])

        layer_activations = self.__hyperparameters['layerActivations']
        model_loss = self.__hyperparameters["modelLoss"]
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

        self.__model = main.NeuralNetwork(
            size=model_size,
            layer_activations=activation_constructor,
            model_loss=loss_constructor
        )

    def __fit(self):
        epochs = int(self.__hyperparameters['epochs'])
        lr = float(self.__hyperparameters['lr'])
        print(f'Epochs: {epochs}, alpha: {lr}')


        losses = self.__model.fit(
            self.__train_x,
            self.__train_y,
            epochs=epochs,
            lr=lr
        )

        plt.plot(losses)
        plt.savefig("./src/uploads/losses.png", dpi=1000)

    def __test_accuracy(self):
        correct_counter = 0
        total_counter = 0

        for index, element in tqdm(enumerate(self.__test_x)):
            element = np.array(element).reshape(1, 784, 1)
            prediction = self.__model.forward(element)

            if int(np.argmax(prediction)) == int(np.argmax(self.__test_y[index])):
                correct_counter += 1

            total_counter += 1

        print(correct_counter/total_counter)
        result = f'{(correct_counter / total_counter * 100):.2f}% accuracy'



    def run(self):
        self.__get_hyperparameters()
        self.__read_and_drop_csv()
        self.__np_casting()
        self.__data_normalisation_and_one_hot()
        self.__generate_splits()
        self.__model_definition()
        self.__fit()
        self.__test_accuracy()

        self.__model.save()

if __name__ == '__main__':
    CombinedServer().run()