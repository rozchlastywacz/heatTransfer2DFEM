from solver.hillfunctions import *


# to jest funkcja na brzegu po przejsciu z biegunowych na ludzkie
def g(x: float) -> float:
    return (x ** 2) ** (1. / 3)


# to jest glownie dla wygody, zeby kod był czytelniejszy,
# czyli iloczyn g i v dla calkowania po x i po y
def gv_x(x: float, y: float, index: int) -> float:
    return g(x) * elements[index](x, y)


def gv_y(y: float, x: float, index: int) -> float:
    return g(x) * elements[index](x, y)
