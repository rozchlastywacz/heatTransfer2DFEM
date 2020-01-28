from solver.derivatives import *
from solver.hillfunctions import *

# dokładnosc calkowania
step = 0.1


# całka pojedyncza wg Riemanna
def integral(f: partial, lower_bound: float, upper_bound: float) -> float:
    result = 0
    x = lower_bound
    while x < upper_bound:
        x2 = x + step / 2
        result += step * f(x2)
        x += step

    return result


# cąłka podwojna wg Riemanna
def double_integral(f: partial, x_lower_bound: float, y_lower_bound: float, x_upper_bound: float,
                    y_upper_bound: float) -> float:
    result = 0
    base_area = step * step

    x = x_lower_bound
    while x < x_upper_bound:
        y = y_lower_bound
        while y < y_upper_bound:
            x2 = x + step / 2
            y2 = y + step / 2
            result += base_area * f(x2, y2)
            y += step
        x += step

    return result


# pierwsza funckja podcalkowa - pomoc do liczenia B(i,j)
def first_integrand(x: float, y: float, k: float, i: int, j: int) -> float:
    return k * df_dx(elements[i], x, y) * df_dx(elements[j], x, y)


#  druga podcałkowa - pomoc do liczenia B(i,j)
def second_integrand(x: float, y: float, k: float, i: int, j: int) -> float:
    return k * df_dy(elements[i], x, y) * df_dy(elements[j], x, y)
