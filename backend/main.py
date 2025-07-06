import numpy as np
import matplotlib.pyplot as plt
import sklearn
from tqdm import tqdm

from activations import Sigmoid, ReLU
from losses import SSE


class NeuralNetwork:
    def __init__(self, size, activation_functions, loss) -> None:
        self.__size = size
        self.__weights = []
        self.__biases = []
        self.__activations = []
        self.activation_functions = activation_functions
        self.__initialise_parameters()

    def __initialise_parameters(self) -> None:
        model_size = self.__size
        for layer in range(len(model_size) - 1):
            self.__weights.append(
            np.random.randn(model_size[layer + 1], model_size[layer])
            )
            self.__biases.append(
            np.random.randn(1, model_size[layer + 1])
            )

    def feed_forward(self, x) -> np.array:
        activations = [x]
        for layer in range(len(self.__size) - 1):
            zi = np.dot(self.__weights[layer], activations[-1])
            activations.append(
                self.activation_functions[layer]().compute(zi)
            )

        self.__activations = activations
        return activations[-1] # Returns y_hat

    def __backpropagation(self ) -> list:
        # computing Delta L
        delta_layers = [None] * ( len(self.__size) - 1 )
        delta_layers[-1] = None

if __name__ == '__main__':
    s = Sigmoid
    sse = SSE
    nn = NeuralNetwork([2, 5, 1], [s, s], sse)
    print(nn.feed_forward(np.array([0, 2])))
    print(nn.activation_functions)