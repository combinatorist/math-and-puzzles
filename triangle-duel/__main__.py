from fractions import Fraction as F
from numpy import array as a
import numpy as np

p = {
    "ca": a([F(1, 2), 0, F(1, 2)]),
    "bc": a([0, F(8, 9), F(1, 9)]),
    "cb": a([0, F(4, 9), F(5, 9)]),
    "a": ((F(1), "ca"),),
    "bac": ((F(4, 5), "cb"), (F(1, 5), "a")),
    "cab": ((F(1, 2), "bc"), (F(1, 2), "a")),
    "bca": ((F(4, 5), "cb"), (F(1, 5), "cab")),
    "cba": ((F(1, 2), "bc"), (F(1, 2), "bac")),
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
