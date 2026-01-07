import numpy as np

class Tools:
    def __init__(self):
        pass

    def _z_score(self, x):
        mean = np.mean(x)
        std = np.std(x)
        return (x - mean) / std

    def _min_max(self, x, scale_factor):
        return x / scale_factor

    def _getUniqueValues(self, y):
        unique_values = []
        for data_point in y:
            if data_point not in unique_values:
                unique_values.append(int(data_point)) # TODO: TEST FOR A POINT OF ERROR
        # TODO: MERGE SORT !!!!!!!!!!!!!!!!!!
        return unique_values

    def _one_hot_encode(self, y):
        return_y = []
        unique_values = self._getUniqueValues(y)
        for data_point in y:
            to_return = [0] * len(unique_values)
            index = unique_values.index(data_point)
            to_return[index] = 1
            return_y.append(to_return)

        return_y = np.array(return_y)
        return_y = return_y.reshape(-1, len(unique_values), 1)
        return return_y
