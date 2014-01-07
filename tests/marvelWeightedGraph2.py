__author__ = 'bruno'
import heapq
#import dr
import copy

ans_provided_by_lucas = '''SPIDER-MAN/PETER PAR : 4165  differences
GREEN GOBLIN/NORMAN  : 5775  differences
WOLVERINE/LOGAN  : 4408  differences
PROFESSOR X/CHARLES  : 5399  differences
CAPTAIN AMERICA : 3542  differences
Total number of differences: 23289
'''
myans = '''"SPIDER-MAN/PETER PAR" calculated and added to total. (4166 added)
"GREEN GOBLIN/NORMAN " calculated and added to total. (5776 added)
"WOLVERINE/LOGAN " calculated and added to total. (4408 added)
"PROFESSOR X/CHARLES " calculated and added to total. (5399 added)
"CAPTAIN AMERICA" calculated and added to total. (3543 added)
For a grand total of 23292'''

def dsp(G,v):

    final_dist = {}
    dist_so_far = [(0,v,[str(v)])]
    while dist_so_far:

        w = heapq.heappop(dist_so_far)

        # lock it down!
        if w[1] not in final_dist:
            final_dist[w[1]] = (w[0],w[2])
            for x in G[w[1]]:
                if x not in final_dist:
                    heapq.heappush(dist_so_far,(final_dist[w[1]][0] + G[w[1]][x],x,w[2]+[str(x)]))
    return final_dist

def read_file(b):
    file_object = open(b)
    f = file_object.read()
    file_object.close()
    return f

def graphify_weighted_and_unweighted(L):

    graph = {}
    b = L.splitlines()

    for item in b:
    # reverse the graph
        index = item.index("\t")

        try:
            graph[item[index + 1:]][item[:index]] = 1
        except:
            graph[item[index + 1:]] = {item[:index] : 1}

    weighted = {}
    unweighted = {}

    for movie in graph: # create two actor only graphs
        for actor in graph[movie]:
            for fellow_actor in graph[movie]:
                #if actor != fellow_actor:
                    if actor not in weighted:
                        weighted[actor] = {fellow_actor:1}
                        unweighted[actor] = {fellow_actor:1}
                    else:
                        try:
                            weighted[actor][fellow_actor] += 1
                            unweighted[actor][fellow_actor] = 1
                        except:
                            weighted[actor][fellow_actor] = 1
                            unweighted[actor][fellow_actor] = 1

    for actor in weighted: # weigh one graph
        for fellow in weighted[actor]:
            weighted[actor][fellow] = 1.0/(weighted[actor][fellow])

    return weighted, unweighted # return both graphs

b = read_file("../input/marvel.tsv")
G, g = graphify_weighted_and_unweighted(b)

def calculate_differences(graph1, graph2):
    result = 0
    for i in graph1:
        if len(graph1[i][1]) != len(graph2[i][1]):
            result += 1
    return result

def differences(character, graph1, graph2):
    one = dsp(graph1, character)
    two = dsp(graph2, character)
    return calculate_differences(one,two)

heroes = ['"SPIDER-MAN/PETER PAR"',
          '"GREEN GOBLIN/NORMAN "',
          '"WOLVERINE/LOGAN "',
          '"PROFESSOR X/CHARLES "',
          '"CAPTAIN AMERICA"']
total = 0
for i in heroes:
    added = differences(i,g,G)
    total += added
    print i + " calculated and added to total. (%s added)" %added
print "For a grand total of " + str(total)
#Wrong value, missing by 3 (+3)