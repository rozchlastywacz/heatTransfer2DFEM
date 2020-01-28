from functools import partial

import numpy as np
import matplotlib.pyplot as plt

size = 100


# wizualizacja wykresu, w duzje mierze prawie gotowiec z neta
def visualize(elements_number: int, W_matrix: [int], elements: [partial]) -> None:
    # obliczanie wartosci funkcji wyliczonej za pomoca MES
    def final_function(x: float, y: float) -> float:
        result: float = 0
        for j in range(elements_number):
            result += W_matrix[j] * elements[j](x, y)
        return result

    xi = yi = np.linspace(-1, 1, size)
    zi = np.array([final_function(i, j) for j in yi for i in xi])

    # Change color palette
    plt.pcolormesh(xi, yi, zi.reshape(size, size), cmap=plt.cm.seismic)
    plt.colorbar()
    plt.show()
