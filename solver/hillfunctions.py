from functools import partial


def inside_domain(x: float, y: float, xp: int, yp: int) -> bool:
    return abs(x - xp) < 1 and abs(y - yp) < 1


def pyramid(x: float, y: float, xp:int , yp: int ) ->float:
    if inside_domain(x, y, xp, yp):
        return (1 - abs(x - xp)) * (1 - abs(y - yp))
    else:
        return 0


partial_pyramid = partial(pyramid, xp=0, yp=0)

top_points = [(-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
limits = [((-1, 0), (0, 1)), ((-1, -1), (0, 1)), ((-1, -1), (0, 0)), ((-1, -1), (1, 0)), ((0, -1), (1, 0))]
k = 1

partial_pyramids = []
for i in top_points:
    x0, y0 = i
    partial_pyramids.append(partial(pyramid, xp=x0, yp=y0))
