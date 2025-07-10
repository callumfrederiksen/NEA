import numpy as np
import activations

class SSE:
    combination = None
    @staticmethod
    def compute(y_hat, y) -> np.array:
        return 0.5 * (y_hat - y) ** 2

    @staticmethod
    def derivative(y_hat, y) -> np.array:
        return np.array(y_hat - y).astype('float32')

class CategoricalCrossEntropyWithSoftmax:
    combination = True
    @staticmethod
    def compute(y_hat, y):
        return -np.sum( y * np.log(y_hat) )

    @staticmethod
    def derivative(y_hat, y):
        return y_hat - y