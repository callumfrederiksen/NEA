import numpy as np

class Sigmoid:
    def compute(self, x) -> np.array:
        return 1 / ( 1 + np.exp(-x) )

    def derivative(self, x) -> np.array:
        return self.compute(x) * ( 1 - self.compute(x) )


class ReLU:
    def compute(self, x):
        return np.maximum(0, x)

    def derivative(self, x):
        return np.float32(x > 0)