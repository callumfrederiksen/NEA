import numpy as np
import matplotlib.pyplot as plt
import sklearn
from tqdm import tqdm

class NeuralNetwork:
    def __init__(self, size):
        self.__size = size
        self.__weights = []
        self.__biases = []

    def __initialise_parameters(self):
        model_size = self.__size
        for layer in range(len(model_size) - 1):
            self.__weights.append(
                np.random.randn(model_size[layer + 1], model_size[layer])
            )
            self.__biases.append(
                np.random.randn(1, model_size[layer + 1])
            )

    def feed_forward(self, x):
        activations = []
        for layer in range(len(self.__size)):


if __name__ == '__main__':
    nn = NeuralNetwork([2, 10, 1])
    nn.__initialise_parameters()