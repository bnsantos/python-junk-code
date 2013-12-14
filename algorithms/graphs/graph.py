__author__ = 'bruno'


def make_link(graph, node1, node2):
    if node1 not in graph:
        graph[node1] = {}
    (graph[node1])[node2] = 1
    if node2 not in graph:
        graph[node2] = {}
    (graph[node2])[node1] = 1
    return graph


def make_graph(connections):
    graph = {}
    for (x, y) in connections:
        make_link(graph, x, y)
    return graph