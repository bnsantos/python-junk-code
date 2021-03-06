__author__ = 'bruno'
answer = {(u'Boone Junior, Mark', u'Del Toro, Benicio'): None,
          (u'Braine, Richard', u'Coogan, Will'): None,
          (u'Byrne, Michael (I)', u'Quinn, Al (I)'): None,
          (u'Cartwright, Veronica', u'Edelstein, Lisa'): None,
          (u'Curry, Jon (II)', u'Wise, Ray (I)'): None,
          (u'Di Benedetto, John', u'Hallgrey, Johnathan'): None,
          (u'Hochendoner, Jeff', u'Cross, Kendall'): None,
          (u'Izquierdo, Ty', u'Kimball, Donna'): None,
          (u'Jace, Michael', u'Snell, Don'): None,
          (u'James, Charity', u'Tuerpe, Paul'): None,
          (u'Kay, Dominic Scott', u'Cathey, Reg E.'): None,
          (u'McCabe, Richard', u'Washington, Denzel'): None,
          (u'Reid, Kevin (I)', u'Affleck, Rab'): None,
          (u'Reid, R.D.', u'Boston, David (IV)'): None,
          (u'Restivo, Steve', u'Preston, Carrie (I)'): None,
          (u'Rodriguez, Ramon (II)', u'Mulrooney, Kelsey'): None,
          (u'Rooker, Michael (I)', u'Grady, Kevin (I)'): None,
          (u'Ruscoe, Alan', u'Thornton, Cooper'): None,
          (u'Sloan, Tina', u'Dever, James D.'): None,
          (u'Wasserman, Jerry', u'Sizemore, Tom'): None}

test = {(u'Ali, Tony', u'Allen, Woody'): 0.5657,
        (u'Auberjonois, Rene', u'MacInnes, Angus'): 0.0814,
        (u'Avery, Shondrella', u'Dorsey, Kimberly (I)'): 0.7837,
        (u'Bollo, Lou', u'Jeremy, Ron'): 0.4763,
        (u'Byrne, P.J.', u'Clarke, Larry'): 0.109,
        (u'Couturier, Sandra-Jessica', u'Jean-Louis, Jimmy'): 0.3649,
        (u'Crawford, Eve (I)', u'Cutler, Tom'): 0.2052,
        (u'Flemyng, Jason', u'Newman, Laraine'): 0.139,
        (u'French, Dawn', u'Smallwood, Tucker'): 0.2979,
        (u'Gunton, Bob', u'Nagra, Joti'): 0.2136,
        (u'Hoffman, Jake (I)', u'Shook, Carol'): 0.6073,
        #(u'Kamiki, Ry\xfbnosuke', u'Thor, Cameron'): 0.3644,
        (u'Roache, Linus', u'Dreyfuss, Richard'): 0.6731,
        (u'Sanchez, Phillip (I)', u'Wiest, Dianne'): 0.5083,
        (u'Sheppard, William Morgan', u'Crook, Mackenzie'): 0.0849,
        (u'Stan, Sebastian', u'Malahide, Patrick'): 0.2857,
        (u'Tessiero, Michael A.', u'Molen, Gerald R.'): 0.2056,
        (u'Thomas, Ken (I)', u'Bell, Jamie (I)'): 0.3941,
        (u'Thompson, Sophie (I)', u'Foley, Dave (I)'): 0.1095,
        (u'Tzur, Mira', u'Heston, Charlton'): 0.3642}

import csv
import copy
import heapq

def add_item(H,control,item,priority):

    if item in control:
        del_item(H,control,item)

    entry = [priority,item]
    control[item] = entry
    heapq.heappush(H,entry)

def del_item(H,control,item):
    entry = control.pop(item)
    entry[-1] = 'deleted'

def shortest_dist_node(H,control):
    while H:
        priority,item = heapq.heappop(H)
        if item is not 'deleted':
            del control[item]
            return item

def dijkstra(G,v):
    H = [] #heap
    control = {}
    dist_so_far = {}
    dist_so_far[v] = 0
    add_item(H,control,v,dist_so_far[v])
    final_dist = {}
    while len(final_dist) < len(G):
        w = shortest_dist_node(H,control)
        final_dist[w] = dist_so_far[w]
        del dist_so_far[w]
        for x in G[w]:
            if x not in final_dist:
                if x not in dist_so_far:
                    dist_so_far[x] = max(final_dist[w],G[w][x])
                    add_item(H,control,x,dist_so_far[x])
                elif final_dist[w] + G[w][x] < dist_so_far[x]:
                    dist_so_far[x] = max(final_dist[w],G[w][x])
                    add_item(H,control,x,dist_so_far[x])
    return final_dist

def make_link(G,node1, node2,weight):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = weight
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = weight
    return G

def read_graph(filename,weighted_movies):
    # Read an undirected graph in CSV format. Each line is an edge
    tsv = csv.reader(open(filename), delimiter='\t')
    G = {}
    actors = {}
    movies = {}
    index = 0
    for x in tsv:
        actors[x[0]] = index
        index += 1

        aux = x[1]+','+x[2]

        movies[aux] = 1
        make_link(G,x[0],aux,weighted_movies[aux])
    return G,actors,movies

def read_weighted_movies(filename):
    # Read an undirected graph in CSV format. Each line is an edge
    tsv = csv.reader(open(filename), delimiter='\t')
    weighted_movies = {}
    for x in tsv:
        weighted_movies[x[0]+','+x[1]] = float(x[2])
    return weighted_movies

weighted_movies = read_weighted_movies('../input/imdb-weights.tsv')
G,actors,movies = read_graph('../input/imdb-1.tsv',weighted_movies)

arq = open('answer.txt','w')
arq.write('answer = {\n')
for x in sorted(answer.keys()):
    print x,':',dijkstra(G,x[0])[x[1]],','
    arq.write(str(x)+':'+str(dijkstra(G,x[0])[x[1]])+',\n')
arq.writelines('}')
arq.close()