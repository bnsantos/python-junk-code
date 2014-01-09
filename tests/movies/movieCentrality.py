__author__ = 'bruno'
import random
import csv


#Function to create a bidirectional edge between nodes supplied as arguments in graph
def make_link(graph, node1, node2):
    #Check to see if we have the node already in the graph
    if node1 not in graph:
        graph[node1] = {}

    #Now add the edge from the first node to the second to the graph
    (graph[node1])[node2] = 1

    #Check to see if we have the node already in the graph
    if node2 not in graph:
        graph[node2] = {}

    #Now add the edge from the second node to the second to the graph
    (graph[node2])[node1] = 1

    return graph


def read_graph(filename):
#Read a graph from a filename in TSV format, with each line being an edg
    tsv = csv.reader(open(filename), delimiter='\t')

    #Set up empty dictionaries to store the data read. Graph contains the bipartite graph
    #that is read from the file while actors and movies contain a complete list of the actors
    #and movies read in. actors and movies are dictionaries instead of lists so that we
    #didn't have to check if a movie or actor is already in the list before we add it
    graph = {}
    read_actors = {}
    read_movies = {}

    #Now we loop ver the lines in the input adding edges to our graph
    for (actor, movie_name, year) in tsv:
        #Create a unique string for each movie that is also human readable
        movie = str(movie_name) + ", " + str(year)

        #Store new movies/actors read
        read_actors[actor] = 1
        read_movies[movie] = 1

        #Finally add the edge to our graph
        make_link(graph, actor, movie)

    return graph, read_actors, read_movies


#Calculate the average centrality of a node, v in the graph graph
#We are using the average shortest path distance to all other nodes in the graph
def centrality(graph, v):
    #Keep a dictionary of the shortest path to a node from the starting node v
    #the distance from v to itself will be always 0 so we initialize that here
    distance_from_start = {}
    distance_from_start[v] = 0

    #Store the nodes to search in a queue for a BFS
    open_list = [v]

    #While we still have nodes to proccess
    while len(open_list) > 0:
        #Get the first node from the queue and remove it
        current = open_list.pop(0)

        #For all the nodes with an edge to the current node, add them to the queue if needed
        for neighbour in graph[current].keys():
            if neighbour not in distance_from_start:
                #If not, add its distance to our distance dictionary
                distance_from_start[neighbour] = distance_from_start[current] + 1

                #Add the neighbour to the queue also so it's children are processed
                open_list.append(neighbour)

    return (float(sum(distance_from_start.values())))/len(distance_from_start)


#Find the rank of v in the list L. Takes O(n) time
def rank(unsorted_list, value):
    pos = 0
    for val in unsorted_list:
        if val <= value:
            pos += 1
    return pos


def find_rank(unsorted_list, i):
    lt = {}
    eq = {}
    gt = {}

    v = random.choice(unsorted_list.keys())

    for l in unsorted_list.keys():
        if unsorted_list[l] < unsorted_list[v] : lt[l] = unsorted_list[l]
        elif unsorted_list[l] == unsorted_list[v] : eq[l] = unsorted_list[l]
        elif unsorted_list[l] > unsorted_list[v] : gt[l] = unsorted_list[l]

    if len(lt) >= i:
        return find_rank(lt, i)
    elif len(lt) + len(eq) >= i:
        return v
    else:
        return find_rank(gt, i-len(lt)-len(eq))


(G, actors, movies) = read_graph("imdb1.tst")

centralities = {}

for actor in actors.keys():
    centralities[actor] = centrality(G, actor)

actor_index = find_rank(centralities, 20)
print actor_index
print centralities[actor_index]