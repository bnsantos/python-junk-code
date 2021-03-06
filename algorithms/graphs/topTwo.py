__author__ = 'bruno'
#
# write a function, `top_two` that takes in a graph and a starting
# node and returns two paths, the first and second shortest paths,
# for all the other nodes in the graph.  You can assume that the
# graph is connected.
#

import heapq
from collections import defaultdict
def top_two(graph, start):
    ncount = len(graph)  # total node count
    ccount = 1           # current node processed count (set to 1 because of start node)
    explored = defaultdict(list)
    frontier = []
    heapq.heappush(frontier,(0,[start]))
    while frontier and (ccount < ncount):
        (pcost,path) = heapq.heappop(frontier)
        cstate = path[-1]
        if len(explored[cstate]) < 2:
            explored[cstate] += [(pcost,path)]  # keep the two least cost paths
            if len(explored[cstate]) == 2:
                ccount += 1  # got two paths for this node
        for neighbor in graph[cstate]:
            if neighbor not in path:   # Do not allow loops
                newpath = path + [neighbor]
                heapq.heappush(frontier,(pcost+graph[cstate][neighbor],newpath))
    return explored

def test():
    graph = {'a':{'b':3, 'c':4, 'd':8},
             'b':{'a':3, 'c':1, 'd':2},
             'c':{'a':4, 'b':1, 'd':2},
             'd':{'a':8, 'b':2, 'c':2}}
    result = top_two(graph, 'a') # this is a dictionary
    b = result['b'] # this is a list
    b_first = b[0] # this is a list
    assert b_first[0] == 3 # the cost to get to 'b'
    assert b_first[1] == ['a', 'b'] # the path to 'b'
    b_second = b[1] # this is a list
    assert b_second[0] == 5 # the cost to get to 'b'
    assert b_second[1] == ['a', 'c', 'b']



