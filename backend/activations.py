import numpy as np

class Sigmoid: # Check the research part of the documentation for an explanation of the mathematics behind this
    @staticmethod
    def compute(x: np.array) -> np.array:  # For forward pass
        return 1 / (1 + np.exp(-x))

    @staticmethod
    def derivative(x: np.array) -> np.array:  # For backward pass
        return np.array(Sigmoid.compute(x) * (1 - Sigmoid.compute(x))).astype('float32')


class ReLU: # Check the research part of the documentation for an explanation of the mathematics behind this
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

# Custom Losses: SiLU and GELU

class SiLU:
    @staticmethod
    def compute(x: np.array, beta=1) -> np.array:
        return x * Sigmoid.compute(x, beta=beta)

    @staticmethod
    def derivative(x: np.array, beta=1) -> np.array:
        return x * Sigmoid.derivative(x, beta=beta) + Sigmoid.compute(x, beta=beta) # Uses Product Rule

class GELU:
    @staticmethod
    def compute(x: np.array, beta=1.702) -> np.array:
        return SiLU.compute(x, beta=beta)

    @staticmethod
    def derivative(x: np.array, beta=1.702) -> np.array:
        return SiLU.derivative(x, beta=beta)