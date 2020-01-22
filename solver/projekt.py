import matplotlib.pyplot as plt
import numpy as np

from data.boundaries import gv_x, gv_y
from data.gauss import solve
from data.integrals import *

elements_number: int = len(top_points)

B_matrix = np.arange(25, dtype=np.float).reshape(5, 5)

for i in range(elements_number):
    start, end = limits[i]
    xi_start, yi_start = start
    xi_end, yi_end = end
    for j in range(elements_number):
        B_matrix[i, j] = (double_integral(partial(first, k=k, i=i, j=j), xi_start, yi_start, xi_end, yi_end)
                          + double_integral(partial(second, k=k, i=i, j=j), xi_start, yi_start, xi_end, yi_end))

L_matrix = np.arange(5, dtype=np.float).reshape(5, 1)

L_matrix[0, 0] = integral(partial(gv_x, i=0, y=1), -1, 0) + integral(partial(gv_y, i=0, x=-1), 0, 1)
L_matrix[1, 0] = integral(partial(gv_y, i=1, x=-1), -1, 1)
L_matrix[2, 0] = integral(partial(gv_y, i=2, x=-1), -1, 0) + integral(partial(gv_x, i=2, y=-1), -1, 0)
L_matrix[3, 0] = integral(partial(gv_x, i=3, y=-1), -1, 1)
L_matrix[4, 0] = integral(partial(gv_x, i=4, y=-1), -1, 1) + integral(partial(gv_y, i=4, x=1), -1, 0)


W_matrix = solve(np.hstack((B_matrix, L_matrix)))


def final_function(x, y):
    result: float = 0
    for j in range(elements_number):
        result += W_matrix[j] * partial_pyramids[j](x, y)
    return result


# create data

size = 100
xi = yi = np.linspace(-1, 1, size)
zi = np.array([final_function(i, j) for j in yi for i in xi])

# Change color palette
plt.pcolormesh(xi, yi, zi.reshape(size, size), cmap=plt.cm.YlOrRd)
plt.colorbar()
plt.show()
