__author__ = 'bruno'
import rank as Rank
import random


def top_k(values, k):
    v = values[random.randrange(len(values))]
    (left, middle, right) = Rank.partition_tuple(values, v)
    if len(left) == k:
        return left
    if len(left)+1 == k:
        return left + [v]
    if len(left) > k:
        return top_k(left, k)
    if len(left) < k:
        return left+[v]+top_k(right, k-len(left)-1)