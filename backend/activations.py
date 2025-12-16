import numpy as np

# The purpose of this code is to ensure that the activations of the model are interchangeable.
#
# The regular format of a static object with the forward compute() function as well as the "backward" derivative()
# function results in ease of introduction of new functions; for example, if one wanted to add a new activation function,
# such as the LeakyReLU function, they would need to copy the regular structure, but implement its own logic within the
# compute() function and derivative() function, as long as the type hinting has been abided by, then there should be a
# seamless introduction into the model
#
# The type hinting should allow potential new developers to easily integrate new functions, as well as being explicit to
# the current developers and examiners to understand the ideal inputs and outputs of the model
#
# Static methods have been used for the main reason of integration into the NeuralNetwork model without instantiation,
# therefore the code can use the class as a datatype without instantiating to an object as there is no need for there are
# no attributes in the class.

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

    # As the Softmax function has many variables, the derivative of this function would be a Jacobian, which although  has
    # many uses within the world of multivariate calculus, linear algebra, and machine learning, the model will use this
    # in conjunction with the CategoricalCrossEntropyWithSoftmax static loss class to resolve the derivative of the
    # combination of the two to be y_hat - y, this is why the Softmax static class only has the compute() function for
    # the forward pass, but no derivative() function, as there will be no requirement to call it within the context of the code
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