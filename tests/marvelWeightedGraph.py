__author__ = 'bruno'
import csv
from collections import defaultdict
import time


def highest_strength(graph):
    return max((s, x, y) for x, links in graph.items() for y, s in links.items())


#Function to create a bidirectional edge between nodes supplied as arguments in graph
def make_link(graph, node1, node2):
    if node1 not in graph:
        graph[node1] = defaultdict(int)

    (graph[node1])[node2] += 1

    #Check to see if we have the node already in the graph
    if node2 not in graph:
        graph[node2] = defaultdict(int)

    #Now add the edge from the second node to the second to the graph
    (graph[node2])[node1] += 1

    return graph


def read_file(filename):
    tsv = csv.reader(open(filename), delimiter='\t')

    comics = {}
    for (character, comic) in tsv:
        #print character
        if comic not in comics:
            comics[comic] = []
        comics[comic].append(character)

    graph = {}

    for comic_book in comics:
        for i in range(len(comics[comic_book])):
            for j in range(i+1, len(comics[comic_book])):
                make_link(graph, comics[comic_book][i], comics[comic_book][j])
                #print comic_book, comics[comic_book][i], comics[comic_book][j]

    return graph


start_time = time.time()
marvel_graph = read_file('../input/marvel.tsv')
print highest_strength(marvel_graph)
print "running time:", time.time() - start_time