import networkx as nx


def build_graph():
    G = nx.Graph()
    G.add_node(1)
    G.add_nodes_from([2,3])
    G.add_edge(1,2)
    return G
