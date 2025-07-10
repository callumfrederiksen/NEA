import numpy as np

class Sigmoid:
    @staticmethod
    def compute(x) -> np.array:
        return 1 / ( 1 + np.exp(-x) )

    @staticmethod
    def derivative(x) -> np.array:
        return np.array(Sigmoid.compute(x) * ( 1 - Sigmoid.compute(x) )).astype('float32')


class ReLU:
    @staticmethod
    def compute(x):
        return np.maximum(0, x)

    @staticmethod
    def derivative(x):
        return np.array(x > 0).astype('float32')


class Softmax:
    @staticmethod
    def compute(z):
        return np.exp(z) / np.sum(np.exp(z))

    @staticmethod
    def derivative(x):
        pass # Used in combination with losses.CategoricalCrossEntropyWithSoftmax