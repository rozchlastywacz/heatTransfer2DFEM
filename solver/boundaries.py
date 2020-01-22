from data.hillfunctions import *


def g(x):
    return (x ** 2) ** (1. / 3)


def gv_x(x, y, i):
    return g(x) * partial_pyramids[i](x, y)


def gv_y(y, x, i):
    return g(x) * partial_pyramids[i](x, y)
