def x_xy_derivative(xy_function, x, y):  # po x
    h = 0.001
    result = (xy_function(x + h, y) - xy_function(x, y)) / h
    return result


def y_xy_derivative(xy_function, x, y):  # po y
    h = 0.001
    result = (xy_function(x, y + h) - xy_function(x, y)) / h
    return result
