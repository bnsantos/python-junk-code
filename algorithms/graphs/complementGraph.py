__author__ = 'bruno'


def make_link(graph, node1, node2):
    if node1 not in graph:
        graph[node1] = {}
    (graph[node1])[node2] = 1
    if node2 not in graph:
        graph[node2] = {}
    (graph[node2])[node1] = 1
    return graph


def make_complement_graph(graph):
    complement_graph = {}
    keys = graph.keys()
    for key in keys:
        missing_connections = list(keys)
        missing_connections.remove(key)
        connections = graph[key]
        for adjacent_node in connections:
            missing_connections.remove(adjacent_node)
        for new_adjacent_node in missing_connections:
            make_link(complement_graph, key, new_adjacent_node)

    return complement_graph