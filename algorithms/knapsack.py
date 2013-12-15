__author__ = 'bruno'
from collections import namedtuple


Bounty = namedtuple('Bounty', 'name value weight volume')


def get_items(n):
    items = [Bounty('bread',        2600,   2,  4),
             Bounty('money',        1500,   5,  1),
             Bounty('gold',         2000,  20,  9),
             Bounty('water',        2900,   5,  5),
             Bounty('banana',       2800,   4,  4),
             Bounty('compass',      2000,   3,  3),
             Bounty('whisky',       1000,   7,  7),
             Bounty('meal',         2500,   8, 10),
             Bounty('tent',         3000,  30, 30),
             Bounty('jacket',       3000,  10, 10),
             Bounty('speedo',       1800,   2,  2),
             Bounty('sunglasses',   1900,   2,  5),
             Bounty('socks',        2000,   2,  1),
             Bounty('short',        2500,   5,  3),
             Bounty('boots',        2500,  10, 10)]

    return items[0:n]


def knapsack_dp(items, sack):
    """
    Solves the Knapsack problem, with two sets of weights,
    using a dynamic programming approach
    """
    # (weight+1) x (volume+1) table
    # table[w][v] is the maximum value that can be achieved
    # with a sack of weight w and volume v.
    # They all start out as 0 (empty sack)
    table = [[0] * (sack.volume + 1) for i in xrange(sack.weight + 1)]

    for w in xrange(sack.weight + 1):
        for v in xrange(sack.volume + 1):
            # Consider the optimal solution, and consider the "last item" added
            # to the sack. Removing this item must produce an optimal solution
            # to the subproblem with the sack's weight and volume reduced by that
            # of the item. So we search through all possible "last items":
            for item in items:
                # Only consider items that would fit:
                if w >= item.weight and v >= item.volume:
                    table[w][v] = max(table[w][v],
                                      # Optimal solution to subproblem + value of item:
                                      table[w - item.weight][v - item.volume] + item.value)

    # Backtrack through matrix to re-construct optimum:
    result = [0] * len(items)
    w = sack.weight
    v = sack.volume
    while table[w][v]:
        # Find the last item that was added:
        aux = [table[w-item.weight][v-item.volume] + item.value for item in items]
        i = aux.index(table[w][v])

        # Record it in the result, and remove it:
        result[i] += 1
        w -= items[i].weight
        v -= items[i].volume

    return result
