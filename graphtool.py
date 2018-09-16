import networkx as nx
import matplotlib.pyplot as plt
from keywords import *
from colour import Color
import time

def normalizeWeights(dict):
    maximum = 0
    for firstTerm, value in dict.items():
        for secondTerm, weight in value.items():
            maximum = max(maximum, weight['weight'])
    for firstTerm in dict:
        for secondTerm, weight in dict[firstTerm].items():
            dict[firstTerm][secondTerm]['weight'] /= (maximum / 5.0)

def drawNetworkGraph(edgedict, sentiments):

    print(sentiments)
    print(edgedict)
    normalizeWeights(edgedict)
    nodelist = []
    colorlist = []
    for key in sentiments:
        nodelist.append(key)
        c = 150.0 # increase to push colors further to red/green extremes
        red = int(255.0/(1+c**(2*sentiments[key]-1)))
        colorlist.append('#' + str(hex(red))[2:] + str(hex(255-red))[2:] + '00')
    edge_list = []

    for firstKey in edgedict:
        for secondKey in edgedict[firstKey]:
            edge_list.append((firstKey, secondKey, {'weight': edgedict[firstKey][secondKey]['weight']}))

    g = nx.from_dict_of_dicts(edgedict)
    pos = nx.spring_layout(g)
    edges = g.edges()
    G = nx.Graph()
    weights = [g[u][v]['weight'] for u, v in edges]
    G.add_edges_from(g.edges())
    nx.draw(G, pos, nodelist=nodelist, node_color=colorlist, with_labels=True, alpha=0.8, width=weights)
    # plt.show()
    plt.savefig("static/Graph.png", format="PNG", transparent=True)
    plt.clf()
