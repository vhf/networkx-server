import multiprocessing
import zerorpc
import random
from pprint import pprint

class Server(object):
    def __init__(self, port, graph):
        self.port = port
        self.graph = graph
    def id(self):
        return hex(id(self.graph))
    def edges(self):
        return self.graph.edges()
    def add(self):
        self.graph.add_nodes_from([11, 12])
        self.graph.add_edge(11, 12)
        for i in range(0, 10):
            rand = random.randint(200, 300)
            self.graph.add_node(rand)
            self.graph.add_edge(11, rand)


def serve(port, manager):
    print("Starting RCP server on port {}".format(port))
    graph = manager
    server = Server(port, graph)
    s = zerorpc.Server(server)
    s.bind("tcp://0.0.0.0:{}".format(port))
    s.run()
