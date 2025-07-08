import numpy as np
import matplotlib.pyplot as plt
import sklearn
from tqdm import tqdm

from activations import Sigmoid, ReLU
from losses import SSE


class NeuralNetwork:
    def __init__(self, size):
        self.__size = size
        self.__weights = [None]
        self.__biases = [None]
        self.__activations = []
        self.__z_activations = [None]
        self.__layer_activations = [None, ReLU, Sigmoid]
        self.__model_loss = SSE
        self.__initialise_parameters()

    def __initialise_parameters(self):
        for layer in range(1, len(self.__size)):
            self.__weights.append(
                np.random.randn(self.__size[layer], self.__size[layer-1])
            )
            self.__biases.append(
                np.random.randn(self.__size[layer], 1)
            )

    def forward(self, xi):
        activations = [xi]
        z_activations = [None]

        for layer in range(1, len(self.__size)):
            zi = (self.__weights[layer] @ activations[-1]) + self.__biases[layer]
            ai = self.__layer_activations[layer].compute(zi)
            z_activations.append(zi)
            activations.append(ai)

        self.__activations = activations
        self.__z_activations = z_activations

        return activations[-1] # y_hat

    def backprop(self, xi, yi):
        deltas = [None] * len(self.__size)
        weight_derivatives = [None]
        bias_derivatives = [None]

        deltas[-1] = self.__model_loss.derivative(self.__activations[-1], yi)
        deltas[-1] *= self.__layer_activations[-1].derivative(self.__z_activations[-1])

        for layer in reversed(range(1, len(self.__size) - 1)):
            deltas[layer] = self.__weights[layer+1].T @ deltas[layer+1]
            deltas[layer] *= self.__layer_activations[layer].derivative(self.__z_activations[layer])

        for layer in reversed(range(1, len(self.__size))):
            weight_derivatives.append(
                deltas[layer] @ self.__activations[layer - 1].T
            )

            bias_derivatives.append(
                deltas[layer]
            )

        weight_derivatives = [None] + list(reversed(weight_derivatives[1:]))
        bias_derivatives = [None] + list(reversed(bias_derivatives[1:]))
        return weight_derivatives, bias_derivatives


    def fit(self, x, y, epochs=100, lr=0.1):
        losses = []
        for i in tqdm(range(epochs)):
            loss = 0
            for j in range(len(x)):
                y_hat = self.forward(x[j])


                loss += self.__model_loss.compute(y_hat, y[j])
                weight_derivatives, bias_derivatives = self.backprop(x[j], y[j])

                for layer in range(len(weight_derivatives)):
                    if type(self.__weights[layer]) == type(None): continue
                    self.__weights[layer] -= lr * weight_derivatives[layer]
                    self.__biases[layer] -= lr * bias_derivatives[layer]

            losses.append(loss / len(x))

        return np.array(losses).reshape(epochs)
if __name__ == '__main__':
    model = NeuralNetwork([2, 16, 1])

    x, y = sklearn.datasets.make_moons(n_samples=10000, noise=0.1)
    x, y = sklearn.utils.shuffle(x, y, random_state=72)

    x = x.reshape(-1, 2, 1)
    y = y.reshape(-1, 1, 1)

    model.forward(x[0])
    # model.backprop(x[0], y[0])
    #losses = model.fit(x, y)
    losses = model.fit(x, y)
    # plt.plot(np.array(losses).reshape(200000))
    # plt.show()

    plt.plot(losses)
    plt.show()

    print(model.forward(x[3])[-1])
    print(y[3])
