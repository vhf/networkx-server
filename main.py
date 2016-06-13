import multiprocessing as m
import multiprocessing.managers as managers
import logging
import networkx as nx
from graph_builder import build_graph
from zerorpc_server import serve

server_count = 4

G = build_graph()
print(G.edges())

def main():
    logger = m.log_to_stderr()
    logger.setLevel(m.SUBDEBUG)
    manager = m.Manager()
    results = manager.list()
    for (i) in range(4200, 4200 + server_count):
        p = m.Process(target=serve, args=(i,))
        p.start()

if __name__ == "__main__":
    main()
