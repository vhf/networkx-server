import networkx as nx
import random


def build_graph():
    G = nx.Graph()
    G.add_node(1)
    G.add_nodes_from([2, 3])
    G.add_edge(1, 2)
    for i in range(0, 10):
        rand = random.randint(100, 200)
        G.add_node(rand)
        G.add_edge(1, rand)
    return G
