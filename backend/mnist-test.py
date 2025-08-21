from main import NeuralNetwork
from activations import *
from losses import *

import pandas as pd
import numpy as np

class DataImplementation:
    def __init__(self):
        self.__FILE_PATH = './datasets/mnist_train.csv'
        self.__TRAIN_TEST_SPLIT = 0.8  # 80% train, 20% test
        self.__SIZE = [784, 256, 128, 10]
        self.__ACTIVATIONS = [ReLU, ReLU, Softmax]
        self.__LOSS = CategoricalCrossEntropyWithSoftmax
        self.__DATASET_SIZE = [785, 1]
        self.__Y_COLUMN_SIZE = [10, 1]
        self.__Y_COLUMN = 'label'
        self.__Y_INDEX = 0  # ASSUMED

    def __read_csv(self):
        df = pd.read_csv(self.__FILE_PATH)
        df = np.array(df)
        DF_RESHAPE = [-1] + self.__DATASET_SIZE
        self.__df = df.reshape(DF_RESHAPE)

    def __get_dataset_size(self):
        self.__N_LENGTH = self.__df.shape[0]
        return self.__N_LENGTH

    def __train_test_split(self):
        TRAIN_VAL = int((self.__N_LENGTH * self.__TRAIN_TEST_SPLIT) // 1)
        TRAIN_DF, TEST_DF = self.__df[:TRAIN_VAL], self.__df[TRAIN_VAL:]

        self.__train_X, self.__train_y = TRAIN_DF[:, self.__Y_INDEX + 1:], TRAIN_DF[:, self.__Y_INDEX]
        self.__test_X, self.__test_y = TEST_DF[:, self.__Y_INDEX + 1:], TRAIN_DF[:, self.__Y_INDEX]

        return (self.__train_X, self.__train_y), (self.__test_X, self.__test_y)

    def __one_hot_encode(self, array, output_size):
        min_value, max_value = min(array), max(array)
        range = (max_value - min_value + 1)[0]

        output_array = []

        for element in array:
            out = [0] * range

            out[element[0]] = 1
            output_array.append(out)

        output_array = np.array(output_array)

        to_reshape = [-1] + output_size
        output_array = output_array.reshape(to_reshape)

        return output_array

    def compute(self):
        self.__read_csv()
        self.__get_dataset_size()
        self.__train_test_split()

        self.__train_y = self.__one_hot_encode(self.__train_y, [10, 1])
        self.__test_y = self.__one_hot_encode(self.__test_y, [10, 1])

if __name__ == '__main__':
    di = DataImplementation()
    di.compute()

