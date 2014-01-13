__author__ = 'bruno'


# Find me that path!
def long_and_simple_path(graph, node1, node2, link):
    """
    G: Graph
    u: starting node
    v: ending node
    l: minimum length of path
    """
    if not long_and_simple_decision(graph, node1, node2, link):
        return False
    else:
        return None


def make_link(graph, node1, node2):
    if node1 not in graph:
        graph[node1] = {}
    (graph[node1])[node2] = 1
    if node2 not in graph:
        graph[node2] = {}
    (graph[node2])[node1] = 1
    return graph


def break_link(graph, node1, node2):
    if node1 not in graph:
        print "error: breaking link in a non-existent node"
        return
    if node2 not in graph:
        print "error: breaking link in a non-existent node"
        return
    if node2 not in graph[node1]:
        print "error: breaking non-existent link"
        return
    if node1 not in graph[node2]:
        print "error: breaking non-existent link"
        return
    del graph[node1][node2]
    del graph[node2][node1]
    return graph


def all_perms(seq):
    if len(seq) == 0:
        return [[]]
    if len(seq) == 1:
        return [seq, []]
    most = all_perms(seq[1:])
    first = seq[0]
    rest = []
    for perm in most:
        for i in range(len(perm)+1):
            rest.append(perm[0:i] + [first] + perm[i:])
    return most + rest


def check_path(graph, path):
    for i in range(len(path)-1):
        if path[i+1] not in graph[path[i]]:
            return False
    return True


def long_and_simple_decision(graph, node1, node2, link):
    if link == 0:
        return False
    n = len(graph)
    perms = all_perms(graph.keys())
    for perm in perms:
        # check path
        if len(perm) >= link and check_path(graph, perm) and perm[0] == node1 and perm[len(perm)-1] == node2:
            return True
    return False

