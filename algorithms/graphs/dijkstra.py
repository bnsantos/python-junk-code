__author__ = 'bruno'
from algorithms.priorityDictionary import PriorityDictionary


def dijkstra(graph, start, end=None):
    """
    Find shortest paths from the start vertex to all
    vertices nearer than or equal to the end.

    The input graph G is assumed to have the following
    representation: A vertex can be any object that can
    be used as an index into a dictionary.  G is a
    dictionary, indexed by vertices.  For any vertex v,
    G[v] is itself a dictionary, indexed by the neighbors
    of v.  For any edge v->w, G[v][w] is the length of
    the edge.  This is related to the representation in
    <http://www.python.org/doc/essays/graphs.html>
    where Guido van Rossum suggests representing graphs
    as dictionaries mapping vertices to lists of neighbors,
    however dictionaries of edges have many advantages
    over lists: they can store extra information (here,
    the lengths), they support fast existence tests,
    and they allow easy modification of the graph by edge
    insertion and removal.  Such modifications are not
    needed here but are important in other graph algorithms.
    Since dictionaries obey iterator protocol, a graph
    represented as described here could be handed without
    modification to an algorithm using Guido's representation.

    Of course, G and G[v] need not be Python dict objects;
    they can be any other object that obeys dict protocol,
    for instance a wrapper in which vertices are URLs
    and a call to G[v] loads the web page and finds its links.

    The output is a pair (D,P) where D[v] is the distance
    from start to v and P[v] is the predecessor of v along
    the shortest path from s to v.

    Dijkstra's algorithm is only guaranteed to work correctly
    when all edge lengths are positive. This code does not
    verify this property for all edges (only the edges seen
    before the end vertex is reached), but will correctly
    compute shortest paths even for some graphs with negative
    edges, and will raise an exception if it discovers that
    a negative edge has caused it to make a mistake.
    """

    final_dist = {}
    predecessors = {}
    dist_so_far = PriorityDictionary()
    dist_so_far[start] = 0

    for v in dist_so_far:
        final_dist[v] = dist_so_far[v]
        if v == end:
            break

        for w in graph[v]:
            vwLength = final_dist[v] + graph[v][w]
            if w in final_dist:
                if vwLength < final_dist[w]:
                    raise ValueError + "Dijkstra: found better path to already-final vertex"
            elif w not in dist_so_far or vwLength < dist_so_far[w]:
                dist_so_far[w] = vwLength
                predecessors[w] = v

    return final_dist, predecessors


def shortest_path(graph, start, end):
    """
    Find a single shortest path from the given start vertex
    to the given end vertex.
    The input has the same conventions as Dijkstra().
    The output is a list of the vertices in order along
    the shortest path.
    """

    dijkstra_distance, predecessors = dijkstra(graph, start, end)
    path = []
    while 1:
        path.append(end)
        if end == start:
            break
        end = predecessors[end]
    path.reverse()
    return path