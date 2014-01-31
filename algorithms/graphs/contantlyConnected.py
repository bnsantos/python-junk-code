__author__ = 'bruno'
#
# Design and implement an algorithm that can preprocess a
# graph and then answer the question "is x connected to y in the
# graph" for any x and y in constant time Theta(1).
#

#
# `process_graph` will be called only once on each graph.  If you want,
# you can store whatever information you need for `is_connected` in
# global variables
#


def add_neighbors(graph, visited, current, connect):
    for neighbor in graph[current].keys():
        if neighbor not in connect and neighbor not in visited:
            connect.append(neighbor)
            visited.append(neighbor)
            add_neighbors(graph, visited, neighbor, connect)


def process_graph(graph):
    connected = {}
    for key in graph.keys():
        visited = []
        connect = []
        visited.append(key)
        for neighbor in graph[key].keys():
            if neighbor not in connect and neighbor != key:
                connect.append(neighbor)
                add_neighbors(graph, visited, neighbor, connect)
        connected[key] = connect
    return connected


#
# When being graded, `is_connected` will be called
# many times so this routine needs to be quick
#
def is_connected(preprocessed, i, j):
    return j in preprocessed[i]


