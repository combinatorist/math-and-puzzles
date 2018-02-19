from fractions import Fraction as F
from numpy import array as a
import numpy as np
from functools import reduce
from operator import mul

def miss(accuracy):
    return F(1) - accuracy

class Player:

    def __init__(self, accuracy):
        self.hit = accuracy
        self.miss = miss(self.hit)

players = {
    'a': Player(F(1)),
    'b': Player(F(4, 5)),
    'c': Player(F(1, 2)),
}

def duel(order):
    """Probability of success for each player given everyone's accuracy.
    If no person has perfect accuracy, attempts may go on forever, but by
    summing the geometric series, there is an exact probability.
    """
    # https://en.wikipedia.org/wiki/Geometric_series
    # The "common ratio" is the probability of everyone missing
    common_ratio = reduce(mul, [a.miss for a in order])
    success_probabilities = []
    cumulative_miss = F(1)
    for player in order:
        numerator = player.hit * cumulative_miss
        success_probabilities.append(F(numerator / (1 - common_ratio)))
        cumulative_miss = cumulative_miss * player.miss
    return success_probabilities

c_vs_a = duel((players['c'], players['a']))
b_vs_c = duel((players['b'], players['c']))
c_vs_b = duel((players['c'], players['b']))

p = {
    "ca": a([F(1) - c_vs_a[0], 0, c_vs_a[0]]),
    "bc": a([0, b_vs_c[0], F(1) - b_vs_c[0]]),
    "cb": a([0, F(1) - c_vs_b[0], c_vs_b[0]]),
    # a always hits target: b, regardless of order
    "abc": ((F(1), "ca"),),
    "acb": ((F(1), "ca"),),
    # b always shoots at a
    "bac": ((F(4, 5), "cb"), (F(1, 5), "acb")),
    "bca": ((F(4, 5), "cb"), (F(1, 5), "cab")),
    # c always shoots into air, hitting no-one
    "cab": ((F(1), "abc"),),
    "cba": ((F(1), "bac"),),
    "start": (
        (F(1, 6), "abc"),
        (F(1, 6), "acb"),
        (F(1, 6), "bac"),
        (F(1, 6), "cab"),
        (F(1, 6), "bca"),
        (F(1, 6), "cba"),
    )
}

def compute(entry_point_ref):
    """computes probability for each (A, B, C) to be last survivor
    """
    entry_point = p[entry_point_ref]
    if isinstance(entry_point, np.ndarray):
        return entry_point
    else:
        results = [compute(pair[1]) * pair[0] for pair in entry_point]

    return np.asarray(results).sum(axis=0)

# import pdb; pdb.set_trace()
compute("ca")
compute("bc")
compute("cb")
compute("abc")
compute("bac")
print compute("start")
print [float(x) for x in compute("start")]
assert compute("start").sum() == 1
