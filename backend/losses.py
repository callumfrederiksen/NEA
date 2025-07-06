import numpy as np

class SSE:
    @staticmethod
    def compute(y_hat, y) -> np.array:
        return 0.5 * (y_hat - y) ** 2

    @staticmethod
    def derivative(y_hat, y) -> np.array:
        return np.array(y_hat - y).astype('float32')

