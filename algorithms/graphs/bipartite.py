__author__ = 'bruno'


#
# Write a function, `bipartite` that
# takes as input a graph, `G` and tries
# to divide G into two sets where
# there are no edges between elements of the
# the same set - only between elements in
# different sets.
# If two sets exists, return one of them
# or `None` otherwise
# Assume G is connected
#
def node_fit(graph, node, target_set, other_set):
    if node in other_set:
        return False
    neighbors = graph[node].keys()
    for neighbor in neighbors:
        if neighbor in target_set:
            return False
    return True


def add_node_neighbors_set(graph, node, target_set, other_set):
    if node not in target_set:
        target_set.append(node)
    neighbors = graph[node].keys()
    for neighbor in neighbors:
        if neighbor not in other_set:
            other_set.append(neighbor)


def bipartite(graph):
    nodes = graph.keys()
    set1 = []
    set2 = []

    for node in nodes:
        if node_fit(graph, node, set1, set2):
            #add node to set1 and all his neighbors to set2
            add_node_neighbors_set(graph, node, set1, set2)
        elif node_fit(graph, node, set2, set1):
            #add node to set2 and all his neighbors to set2
            add_node_neighbors_set(graph, node, set2, set1)
        else:
            return None
    return set1

########
#
# Test

def make_link(G, node1, node2, weight=1):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = weight
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = weight
    return G


def test():
    edges = [(1, 2), (2, 3), (1, 4), (2, 5),
             (3, 8), (5, 6)]
    G = {}
    for n1, n2 in edges:
        make_link(G, n1, n2)
    g1 = bipartite(G)
    assert (g1 == set([1, 3, 5]) or
            g1 == set([2, 4, 6, 8]))
    edges = [(1, 2), (1, 3), (2, 3)]
    G = {}
    for n1, n2 in edges:
        make_link(G, n1, n2)
    g1 = bipartite(G)
    assert g1 == None

