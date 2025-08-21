from main import NeuralNetwork
from activations import *
from losses import *

import pandas as pd
import numpy as np

FILE_PATH = './datasets/mnist_train.csv'
TRAIN_TEST_SPLIT = 0.8 # 80% train, 20% test
SIZE = [784, 256, 128, 10]
ACTIVATIONS = [ReLU, ReLU, Softmax]
LOSS = CategoricalCrossEntropyWithSoftmax
DATASET_SIZE = [785, 1]
Y_COLUMN = 'label'
Y_INDEX = 0 # ASSUMED

df = pd.read_csv(FILE_PATH)
df = np.array(df)

DF_RESHAPE = [-1] + DATASET_SIZE
df = df.reshape(DF_RESHAPE)

N_LENGTH = df.shape[0]

#Train-test-split

TRAIN_VAL = int((N_LENGTH * TRAIN_TEST_SPLIT)//1)
# TEST_VAL = N_LENGTH - TRAIN_VAL

TRAIN_DF, TEST_DF = df[:TRAIN_VAL], df[TRAIN_VAL:]

train_X, train_y = TRAIN_DF[:,Y_INDEX+1:], TRAIN_DF[:,Y_INDEX]
test_X, test_y = TEST_DF[:,Y_INDEX+1:], TRAIN_DF[:,Y_INDEX]
