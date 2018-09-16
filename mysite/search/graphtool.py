import networkx as nx
import matplotlib.pyplot as plt
from keywords import *
from colour import Color
import time


def normalizeWeights(dict):
    normstart = time.time()
    maximum = 0
    for firstTerm, value in dict.items():
        for secondTerm, weight in value.items():
            maximum = max(maximum, weight['weight'])
    for firstTerm in dict:
        for secondTerm, weight in dict[firstTerm].items():
            dict[firstTerm][secondTerm]['weight'] /= (maximum / 5.0)
    print('normalizetime: %f' % (float(time.time()) - float(normstart)))


def drawNetworkGraph(edgedict, sentiments):
    normalizeWeights(edgedict)
    nodelist = []
    colorlist = []
    for key in sentiments:
        nodelist.append(key)
        c = 150.0 # increase to push colors further to red/green extremes
        red = (int)(255.0/(1+c**(2*sentiments[key]['color']-1)))
        print(red)
        colorlist.append('#' + str(hex(red))[2:] + str(hex(255-red))[2:] + '00')
    print(colorlist)
    edge_list = []

    for firstKey in edgedict:
        for secondKey in edgedict[firstKey]:
            edge_list.append((firstKey, secondKey, {'weight': edgedict[firstKey][secondKey]['weight']}))


    g = nx.from_dict_of_dicts(edgedict)
    pos = nx.spring_layout(g)
    edges = g.edges()
    G = nx.Graph()
    weights = [g[u][v]['weight'] for u, v in edges]
    # G.add_nodes_from(nodelist)
    # G.add_nodes_from([(1, dict(size=11)), (2, {'color': 'blue'})])

    # G.add_edges_from(edge_list)
    # nx.draw(G, with_labels=True, width=weights)
    # nx.draw(g, pos, edges=edges, with_labels=True, node_color='#00aced', width=weights)
    G.add_edges_from(g.edges())
    nx.draw(G, pos, nodelist=nodelist, node_color=colorlist, with_labels=True, alpha=1, width=weights)
    plt.show()


d, sentiments = ({'computer science': {'students': {'weight': 57.34121863799287},
                                       'googleforedu': {'weight': 43.776749446893206},
                                       'teachers': {'weight': 19.974516129032263},
                                       'intimidating': {'weight': 14.41436172812139},
                                       'math': {'weight': 4.6117383512544805}, 'history': {'weight': 3.381807108084572},
                                       'passions': {'weight': 16.631955840140066},
                                       'skills': {'weight': 16.631955840140066},
                                       'hobby_touya': {'weight': 3.8626543629611594},
                                       'lid': {'weight': 3.6351882240373516},
                                       'lightwave3d': {'weight': 4.335188224037354},
                                       '3dcg': {'weight': 5.11109625813707}},
                  'students': {'computer science': {'weight': 57.34121863799287},
                               'students': {'weight': 80.27102426247589},
                               'googleforedu': {'weight': 9.229677419354838}}, 'googleforedu': {'computer science': {'weight': 43.776749446893206}, 'students': {'weight': 9.229677419354838}, 'googleforedu': {'weight': 78.43000417070324}, 'teachers': {'weight': 16.429354838709685}}, 'teachers': {'computer science': {'weight': 19.974516129032263},
                                                          'googleforedu': {'weight': 16.429354838709685},
                  'teachers': {'weight': 51.96007765830343}}, 'intimidating': {'computer science': {
    'weight': 14.41436172812139}, 'intimidating': {'weight': 77.37188465444267}}, 'math': {
    'computer science': {'weight': 4.6117383512544805}, 'math': {'weight': 78.49886704096394}}, 'history': {
    'computer science': {'weight': 3.381807108084572}, 'history': {'weight': 23.416395429284158}}, 'passions': {
    'computer science': {'weight': 16.631955840140066}, 'passions': {'weight': 37.248391306813176}}, 'skills': {
    'computer science': {'weight': 16.631955840140066}, 'skills': {'weight': 54.028462235956134}}, 'hobby_touya': {
    'computer science': {'weight': 3.8626543629611594}, 'lightwave3d': {'weight':
                                                                            15.210010918832165},
    '3dcg': {'weight': 11.690900420715861}}, 'lid': {'computer science': {'weight': 3.6351882240373516},
                                                     'lid': {'weight': 53.348649856476214}}, 'lightwave3d': {
    'computer science': {'weight': 4.335188224037354}, 'hobby_touya': {'weight': 15.210010918832165},
    'lightwave3d': {'weight': 26.494926400233453}, '3dcg': {'weight': 13.52710773395026}},
'3dcg': {'computer science': {'weight': 5.11109625813707}, 'hobby_touya': {'weight': 11.690900420715861}, 'lightwave3d':
    {'weight': 13.52710773395026}}}, {'computer science': {'color': 0.5491607279678484}, 'students': {'color': 0.48402029937170526},
                                      'googleforedu': {'color': 0.7073953376641555}, 'teachers': {'color': 0.5599710810039497},
                                      'intimidating': {'color': 0.6408747145018667}, 'math': {'color': 0.44731760775914725},
                                      'history': {'color': 0.6185327157544797}, 'passions': {'color': 0.5814836978733093},
                                      'skills': {'color': 0.6308493535838404}, 'hobby_touya': {'color': 0.5959127433140696},
                                      'lid': {'color': 0.3889967700511042}, 'lightwave3d': {'color': 0.5795693029344643},
                                      '3dcg': {'color': 0.5669733824400874}})
# drawNetworkGraph(get_graph("Waterloo"))
drawNetworkGraph(d, sentiments)
