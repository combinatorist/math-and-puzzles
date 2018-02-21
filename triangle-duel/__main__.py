from fractions import Fraction as F
from numpy import array as a
import numpy as np
from functools import reduce
from operator import mul
from itertools import permutations, product

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

strategies = {
}

def eliminate(order, shooter, target):
    """shows next states after a player's been eliminated
    """
    if target == '_':
        return order
    else:
        next_shooter_index = order.index(shooter) + 1
        reorder = (2 * order)[next_shooter_index:][:len(order)]
        return ''.join(reorder.replace(target,'')) # expects and returns a string

def strategize(name_order):
    """Determines and saves optimal strategy in dictionary
    """
    if name_order in strategies:
        return strategies[name_order][0]
    else:
        strats = [
            ''.join(a)
            for a in product(name_order + "_", repeat=len(name_order))
        ]

    # compute best strategy from all possibilities
    pass

def compute(name_order):
    """computes probability for each (A, B, C) to be last survivor
    """
    if len(name_order) == 1:
        player_index = sorted(players.keys()).index(name_order[0])
        array = np.zeros(len(players), dtype = F)
        array[player_index] = F(1)
        return array

    order = [players[name] for name in name_order]
    targets = strategize(name_order)

    # '_' is interpretted as player passing (no target)
    for i in range(len(name_order)):
        if targets[i] == "_":
            # so, they are masked with a 0 accuracy player
            order[i] = Player(0)

    success_probabilities = duel(order)
    triples = zip(success_probabilities, name_order, targets)
    results = [
            t[0] * compute(eliminate(name_order, t[1], t[2]))
            for t in triples
            if t[2] != '_' # drop players who pass
        ]

    return np.asarray(results).sum(axis=0)

# import pdb; pdb.set_trace()
compute("ca")
compute("bc")
compute("cb")
compute("abc")
compute("bac")

starts = [''.join(a) for a in permutations(''.join(players.keys()))]
result = F(1, len(starts)) * np.asarray([compute(start) for start in starts]).sum(axis=0)
print result
print [float(x) for x in result]
assert result.sum() == 1
assert eliminate("ca", "c", "a") == "c"
