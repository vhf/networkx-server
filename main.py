import multiprocessing as m
import multiprocessing.managers as managers
import logging
import networkx as nx
from graph_builder import build_graph
from zerorpc_server import serve


server_count = 4
graph = build_graph()

class GraphClass:
    def get_graph(self):
        return graph

class GraphManager(managers.BaseManager):
    pass

def main():
    logger = m.log_to_stderr()
    logger.setLevel(m.SUBDEBUG)
    GraphManager.register("GraphClass", GraphClass)
    with GraphManager() as manager:
        for (i) in range(4200, 4200 + server_count):
            p = m.Process(target=serve, args=(i, manager.GraphClass(),))
            p.start()

if __name__ == "__main__":
    main()
