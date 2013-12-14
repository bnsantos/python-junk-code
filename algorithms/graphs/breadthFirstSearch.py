__author__ = 'bruno'


def search(graph, node1, node2):
    distance_from_start = {}
    open_list = [node1]
    distance_from_start[node1] = [node1]
    while len(open_list) > 0:
        current = open_list[0]
        del open_list[0]
        for neighbor in graph[current].keys():
            if neighbor not in distance_from_start:
                distance_from_start[neighbor] = distance_from_start[current]+[neighbor]
                if neighbor == node2:
                    return distance_from_start[node2]
                open_list.append(neighbor)
    return []