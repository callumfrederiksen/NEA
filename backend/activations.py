import numpy as np

class Sigmoid:
    @staticmethod
    def compute(x: np.array) -> np.array:  # For forward pass
        return 1 / (1 + np.exp(-x))

    @staticmethod
    def derivative(x: np.array) -> np.array:  # For backward pass
        return np.array(Sigmoid.compute(x) * (1 - Sigmoid.compute(x))).astype('float32')


class ReLU:
    @staticmethod
    def compute(x: np.array) -> np.array: # For forward pass
        return np.maximum(0, x)

    @staticmethod
    def derivative(x: np.array) -> np.array: # For backward pass
        return np.array(x > 0).astype('float32')


class Softmax:
    @staticmethod
    def compute(z: np.array) -> np.array: # For forward pass
        return np.exp(z) / np.sum(np.exp(z))


    @staticmethod
    def derivative(x: np.array) -> None: # For backward pass
        pass # Used in combination with losses.CategoricalCrossEntropyWithSoftmax
