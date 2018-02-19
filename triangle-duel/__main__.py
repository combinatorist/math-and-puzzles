from fractions import Fraction as F
from numpy import array as a
import numpy as np

players = {
    'a': F(1),
    'b': F(4, 5),
    'c': F(1, 2),
}

def infinite_duels(a_accuracy, b_accuracy):
    """defines probability of survival for 'a' given their's and b's accuracy
    If neither person has perfect accuracy the duel can go forever, but by
    summing the geometric series, there is an exact solution.
    """
    # https://en.wikipedia.org/wiki/Geometric_series
    # The "common ratio" is the probability of everyone missing
    common_ratio = (F(1) - a_accuracy) * (F(1) - b_accuracy)
    return F(a_accuracy, (1 - common_ratio))

c_vs_a = infinite_duels(players['c'], players['a'])
b_vs_c = infinite_duels(players['b'], players['c'])
c_vs_b = infinite_duels(players['c'], players['b'])

p = {
    "ca": a([F(1) - c_vs_a, 0, c_vs_a]),
    "bc": a([0, b_vs_c, F(1) - b_vs_c]),
    "cb": a([0, F(1) - c_vs_b, c_vs_b]),
    # a always hits target: b, regardless of order
    "a": ((F(1), "ca"),),
    # b always shoots at a
    "bac": ((F(4, 5), "cb"), (F(1, 5), "a")),
    "bca": ((F(4, 5), "cb"), (F(1, 5), "cab")),
    # c always shoots into air, hitting no-one
    "cab": ((F(1), "a"),),
    "cba": ((F(1), "bac"),),
    "start": (
        (F(1, 3), "a"),
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
compute("a")
compute("bac")
print compute("start")
print [float(x) for x in compute("start")]
assert compute("start").sum() == 1
