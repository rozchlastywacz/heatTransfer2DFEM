from functools import partial
# dokładnosc pochodnej
h = 0.0001


# pochodna centralna liczona z definicji po x i nizej po y
def df_dx(f: partial, x: float, y: float) -> float:
    result = (f(x + h, y) - f(x - h, y)) / (2 * h)
    return result


def df_dy(f: partial, x: float, y: float) -> float:
    result = (f(x, y + h) - f(x, y - h)) / (2 * h)
    return result
