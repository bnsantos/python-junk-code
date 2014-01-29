#
# Take a weighted graph representing a social network where the weight
# between two nodes is the "love" between them.  In this "feel the
# love of a path" problem, we want to find the best path from node `i`
# and node `j` where the score for a path is the maximum love of an
# edge on this path. If there is no path from `i` to `j` return
# `None`.  The returned path doesn't need to be simple, ie it can
# contain cycles or repeated vertices.
#
# Devise and implement an algorithm for this problem.
#

def feel_the_love(G, i, j):
    # return a path (a list of nodes) between `i` and `j`,
    # with `i` as the first node and `j` as the last node,
    # or None if no path exists
    result = create_love_paths(G, i)
    if j in result:
        return result[j][1]
    else:
        return None

def create_love_paths(G, v):
    """Given a graph G, and a node v, find the path from v to every other node
    in the graph that has the maximum score.  Where a score for a path is the
    maximum of the weights on any individual path.  Return as a dictionary."""
    love_so_far = {}
    love_so_far[v] = (0, [v])
    to_do_list = [v]
    while len(to_do_list) > 0:
        w = to_do_list.pop(0)
        love, path = love_so_far[w]
        for x in G[w]:
            new_path = path + [x]
            new_love = max([love, G[w][x]])
            if x in love_so_far:
                if new_love > love_so_far[x][0]:
                    love_so_far[x] = (new_love, new_path)
                    if x not in to_do_list: to_do_list.append(x)
            else:
                love_so_far[x] = (new_love, new_path)
                if x not in to_do_list: to_do_list.append(x)
    return love_so_far

#########
#
# Test

def score_of_path(G, path):
    max_love = -float('inf')
    for n1, n2 in zip(path[:-1], path[1:]):
        love = G[n1][n2]
        if love > max_love:
            max_love = love
    return max_love

def test():
    G = {'a':{'c':1},
         'b':{'c':1},
         'c':{'a':1, 'b':1, 'e':1, 'd':1},
         'e':{'c':1, 'd':2},
         'd':{'e':2, 'c':1},
         'f':{}}
    path = feel_the_love(G, 'a', 'b')
    assert score_of_path(G, path) == 2

    path = feel_the_love(G, 'a', 'f')
    assert path == None