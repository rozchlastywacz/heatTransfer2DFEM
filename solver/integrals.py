from data.derivatives import *
from data.hillfunctions import *


def integral(function, x_start, x_end):
    sum = 0
    step = 0.1
    x = x_start
    while x < x_end:
        x2 = x + step / 2
        sum += step * function(x2)
        x += step

    return sum


def double_integral(xy_function, x_start, y_start, x_end, y_end):
    sum = 0
    step = 0.1
    base_area = step * step

    x = x_start
    while x < x_end:
        y = y_start
        while y < y_end:
            x2 = x + step / 2
            y2 = y + step / 2
            sum += base_area * xy_function(x2, y2)
            y += step
        x += step

    return sum


def first(x, y, k, i, j):
    return k * x_xy_derivative(partial_pyramids[i], x, y) * x_xy_derivative(partial_pyramids[j], x, y)


def second(x, y, k, i, j):
    return k * y_xy_derivative(partial_pyramids[i], x, y) * y_xy_derivative(partial_pyramids[j], x, y)
