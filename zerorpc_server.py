import multiprocessing
import zerorpc
from pprint import pprint

class Server(object):
    def __init__(self, port, graph):
        self.port = port
        self.graph = graph
    def edges(self):
        return self.graph.edges()


def serve(port, manager):
    print("Starting RCP server on port {}".format(port))
    server = Server(port, manager.get_graph())
    s = zerorpc.Server(server)
    s.bind("tcp://0.0.0.0:{}".format(port))
    s.run()
