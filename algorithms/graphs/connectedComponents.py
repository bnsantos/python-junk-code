__author__ = 'bruno'


def mark_component(graph, node, marked):
    marked[node] = True
    total_marked = 1
    for neighbor in graph[node]:
        if neighbor not in marked:
            total_marked += mark_component(graph, neighbor, marked)
    return total_marked


def list_component_number_of_vertices(graph):
    marked = {}
    components = {}
    for node in graph.keys():
        if node not in marked:
            components[node] = mark_component(graph, node, marked)
    return components