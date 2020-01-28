import matplotlib.pyplot as plt
import numpy as np

from solver.boundaries import gv_x, gv_y
from solver.gauss import solve
from solver.integrals import *
from solver.visualizer import visualize

# liczba piramidek
elements_number: int = len(summits)
# deklaracja macierzy B z pomocą numpy - macierz n x n
B_matrix = np.arange(25, dtype=np.float).reshape(elements_number, elements_number)
# obliczanie elementow macierzy B
for i in range(elements_number):
    # magiczne pythonowe wyciaganie elementow z krotek(tuple)
    # wyciagam krotke (start, end), ktore tez sa krotkami
    start, end = limits[i]
    # dlatego teraz wyciagam ze start i z end wartosci do granic calkowania
    x_lower_bound, y_lower_bound = start
    x_upper_bound, y_upper_bound = end
    for j in range(elements_number):
        B_matrix[i, j] = (double_integral(partial(first_integrand, k=k, i=i, j=j), x_lower_bound, y_lower_bound,
                                          x_upper_bound, y_upper_bound)
                          +
                          double_integral(partial(second_integrand, k=k, i=i, j=j), x_lower_bound, y_lower_bound,
                                          x_upper_bound, y_upper_bound))
# deklaracja macierzy L
L_matrix = np.arange(elements_number, dtype=np.float).reshape(elements_number, 1)
print(B_matrix)
# obliczanie elementow macierzy L
for i in range(elements_number):
    x, y = summits[i]
    start, end = limits[i]
    x_lower_bound, y_lower_bound = start
    x_upper_bound, y_upper_bound = end
    L_matrix[i, 0] = integral(partial(gv_x, index=i, y=y), x_lower_bound, x_upper_bound) + integral(
        partial(gv_y, index=i, x=x), y_lower_bound, y_upper_bound)

# rozwiązanie układu rownan Gaussem
W_matrix = solve(np.hstack((B_matrix, L_matrix)))
# narysowanie wykresu
visualize(elements_number, W_matrix, elements)
