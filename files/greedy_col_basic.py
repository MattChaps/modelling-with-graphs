import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5


def find_smallest_color(G,i):
    global kmax
    n = len(G.nodes())

    colours_lst = []
    for j in range(0,n+1):
        colours_lst.append(j)
    if i == 1:
        k = 1
    else:
        neighbours_colours_lst = []
        for j in G.neighbors(i):
            neighbours_colours_lst.append(G.node[j]['color'])
        while 'never coloured' in neighbours_colours_lst:
            neighbours_colours_lst.remove('never coloured') 
        k = 1
        while colours_lst[k] in neighbours_colours_lst:
            k += 1
    if k > kmax:
        kmax = k
    return k


def greedy(G):
    global kmax
    kmax = 1

    for i in range(1,len(G.nodes())+1):
        c = find_smallest_color(G,i)
        G.node[i]['color'] = c
        
    print()
    for i in G.nodes():
        print('vertex', i, ': color', G.node[i]['color'])
    print()
    print('The number of colors that Greedy computed is:', kmax)

print('Graph G1:')
G=graph1.Graph()
greedy(G)


print('Graph G2:')
G=graph2.Graph()
greedy(G)


print('Graph G3:')
G=graph3.Graph()
greedy(G)


print('Graph G4:')
G=graph4.Graph()
greedy(G)


print('Graph G5:')
G=graph5.Graph()
greedy(G)