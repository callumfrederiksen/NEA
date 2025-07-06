import numpy as np

class SSE:
    def __init__(self) -> None: pass

    def compute(self, y_hat, y) -> np.array:
        return 0.5 * (y_hat - y) ** 2

    def derivative(self, y_hat, y) -> np.array:
        return y_hat - y

