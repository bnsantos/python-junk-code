__author__ = 'bruno'


def clustering_coefficient(graph, node):
    if node in graph:
        kv = len(graph[node])
        neighbors = graph[node]
        nv = 0
        for neighbor1 in neighbors:
            for neighbor2 in neighbors:
                if neighbor2 in graph[neighbor1]:
                    nv += 0.5
        if kv != 1:
            return 2*nv / (kv*(kv-1))
        else:
            return 0


def graph_clustering_coefficient(graph):
    coefficient = 0
    for node in graph:
        coefficient += clustering_coefficient(graph, node)

    return coefficient / len(graph)