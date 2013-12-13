__author__ = 'bruno'
import bisect, heapq


def sort(unordered):
    piles = []
    for item in unordered:
        new_pile = [item]
        i = bisect.bisect_left(piles, new_pile)
        if i != len(piles):
            piles[i].insert(0, item)
        else:
            piles.append(new_pile)

    for i in xrange(len(unordered)):
        small_pile = piles[0]
        unordered[i] = small_pile.pop(0)
        if small_pile:
            heapq.heapreplace(piles, small_pile)
        else:
            heapq.heappop(piles)
    assert not piles

    return unordered
