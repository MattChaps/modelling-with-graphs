import networkx as nx
import random as rd
import graph6
import graph7
import graph8
import graph9
import graph10


def max_distance(G):
    nodes = G.nodes()
    kmax = 0
    for i in range(1 , len(nodes)):
        k = 0
        G.node[i]['label'] = 0
        for key in G.nodes():
            val = G.nodes[key]
            if val['label'] == -1:  
                for u in G.nodes():
                    if G.nodes[u]['label'] == k:
                        for v in G.neighbors(u):
                            if G.nodes[v]['label'] == -1:
                                G.nodes[v]['label'] = k+1
                k = k + 1
        if k > kmax:
            kmax = k
        G.add_nodes_from(G.nodes(), label = -1)
    return kmax


print()
G6=graph6.Graph()
print('The diameter of G6 (i.e. the maximum distance between two vertices) is:', max_distance(G6))
print()


G7=graph7.Graph()
print('The diameter of G7 (i.e. the maximum distance between two vertices) is:', max_distance(G7))
print()


G8=graph8.Graph()
print('The diameter of G8 (i.e. the maximum distance between two vertices) is:', max_distance(G8))
print()


G9=graph9.Graph()
print('The diameter of G9 (i.e. the maximum distance between two vertices) is:', max_distance(G9))
print()


G10=graph10.Graph()
print('The diameter of G10 (i.e. the maximum distance between two vertices) is:', max_distance(G10))
print()
