from functools import partial


# funkcja określajaca dziedzinę funkcji bazowej, w taki sposób, by była ograniczona na kwadratach 1x1
def inside_domain(x: float, y: float, xp: int, yp: int) -> bool:
    return abs(x - xp) < 1 and abs(y - yp) < 1


# definicja samej funkcji bazowej f(x,y) = (1-|x|)(1-|y|)
def hills(x: float, y: float, xp: int, yp: int) -> float:
    if inside_domain(x, y, xp, yp):
        return (1 - abs(x - xp)) * (1 - abs(y - yp))
    else:
        return 0


# Okrelenie gdzie są szczyty tych pagórków/piramid
summits: [(int, int)] = [(-1, 1),
                         (-1, 0),
                         (-1, -1),
                         (0, -1),
                         (1, -1)]

# okreslenie lewego dolnego i prawego górnego punktu obszaru, po którym będę całkować dla każdego ze szczytów
# w sensie każdy szczyt ma swoje ograniczenie przez te dwa punkty
limits: [((int, int), (int, int))] = [((-1, 0), (0, 1)),
                                      ((-1, -1), (0, 1)),
                                      ((-1, -1), (0, 0)),
                                      ((-1, -1), (1, 0)),
                                      ((0, -1), (1, 0))]

# zeby nie komplikowac, to k jest 1 zawsze
k: int = 1

# dodaje funkcje hills po czesci zaaplikowane, teraz sa zalezne tylko od x i y
# a nie tez od xp i yp
elements: [partial] = []
for i in summits:
    x0, y0 = i
    elements.append(partial(hills, xp=x0, yp=y0))
