# Implementation of minimum cut graph algorithm
# written by Lydia Ding
# 02/23/18

import networkx as nx
import random

# calculates the minimum cut of a connected graph G.
# input: a networkx multiGraph.
# output: graph of 2 nodes that represents the 2 clusters of the minimum cut.
def minCut(g):

    # contract two nodes joined by an edge picked @ random until 2 nodes left.
    while g.number_of_nodes() > 2:
        # select an edge at random
        # random.seed(seed)
        contractEdge = random.choice(list(g.edges))
        node1, node2 = contractEdge[0], contractEdge[1]
        # print(node1, node2)
        # delete all edges btw node1 and node2.
        while g.has_edge(node1, node2): g.remove_edge(node1, node2)
        # print(node1, node2, list(g.neighbors(node2)))
        # transfer edges that node2 is a part of to node1.
        for neighbor in list(g.neighbors(node2)):
            for i in range(g.number_of_edges(node2, neighbor)):
                g.add_edge(node1, neighbor)
        # finally, remove node 2.
        g.remove_node(node2)
    return g

if __name__ == "__main__":
    # graph = nx.Graph()
    # graph.add_edge(2, 4)
    # graph.add_edge(4, 2)
    # mGraph = nx.MultiGraph()
    # for n in list(graph.nodes):
    #     mGraph.add_node(n)
    # for e in list(graph.edges):
    #     mGraph.add_edge(*e)
    # nodes = list(mGraph.nodes)
    # edges = list(mGraph.edges)
    # print("BEFORE ADD:", nodes, edges)
    # mGraph.add_edge(4, 2)
    # print("AFTER ADD: ", list(mGraph.edges))
    # while mGraph.has_edge(2, 4):
    #     mGraph.remove_edge(2, 4)
    # print("AFTER REMOVE: ", list(mGraph.edges))

    g = nx.Graph()
    with open("mincut_test.txt", "r") as f:
        for line in f:
            pairs = line.split()
            node, neighbors = pairs[0], pairs[1:]
            for neighbor in neighbors:
                g.add_edge(node, neighbor)

    # shift over to multiGraph, which allows parallel edges.
    mG = nx.MultiGraph()
    for edge in list(g.edges):
        mG.add_edge(*edge)

    # cuts = []
    # for i in range(200):
    #     minimumCut = minCut(mG, i)
    #     print(minimumCut.number_of_edges())
    #     cuts.append(minimumCut.number_of_edges())
    #     # print(list(minimumCut.nodes))
    #
    # print (min(cuts))

    minimumCut = minCut(mG)
    print(minimumCut.number_of_edges())
