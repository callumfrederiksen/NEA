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
        self.__z_activations = []
        self.__activation_functions = [None] + activation_functions
        self.__model_loss = loss
        self.__initialise_parameters()

    def __initialise_parameters(self) -> None:
        model_size = self.__size
        for layer in range(1, len(model_size)):
            self.__weights.append(
                np.random.randn(model_size[layer], model_size[layer-1])
            )
            self.__biases.append(
                np.random.randn(1, model_size[layer])
            )


    def feed_forward(self, x) -> np.array:
        activations = [x]
        z_activations = [None]
        for layer in range(1, len(self.__size)):
            zi = np.dot(self.__weights[layer-1], activations[-1].reshape(-1, 1))

            activations.append(
                self.__activation_functions[layer].compute(zi)
            )

            z_activations.append(
                zi
            )

        self.__activations = activations
        self.__z_activations = z_activations
        return activations[-1] # Returns y_hat

    def backpropagation(self) -> tuple:
        # computing Delta L
        deltas = [None] * len(self.__size)
        deltas[-1] = self.__model_loss.derivative(np.array([1]), np.array([2]))
        deltas[-1] = deltas[-1] * self.__activation_functions[-1].derivative(self.__z_activations[-1]).reshape(-1, 1)

        for layer in range(1, len(self.__size) - 1 ):

            deltas[layer] = (self.__weights[layer].T @ deltas[layer+1])
            deltas[layer] = deltas[layer] * self.__activation_functions[layer].derivative(self.__z_activations[layer])

        weight_derivatives = []
        bias_derivatives = []

        for layer, delta in enumerate(deltas):
            if type(delta) == type(None): continue
            weight_derivatives.append(
                delta @ self.__activations[layer-1].reshape(-1, 1).T
            )
            bias_derivatives.append(deltas)

        return weight_derivatives, bias_derivatives

if __name__ == '__main__':
    s = Sigmoid
    sse = SSE
    nn = NeuralNetwork([2, 5, 1], [s, s], sse)
    nn.feed_forward(np.array([0, 2]))
    nn.backpropagation()