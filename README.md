# networkx-server

The goal of this project is to load a graph in memory using networkx and then spawn a few zerorpc servers which get a proxy to the graph. The zerorpc servers are supposed to expose the networkx API.

## Use case

We have a very large (900GB) graph we want to keep in memory. We would like to run queries on this graph without having to reload it into memory.

The approach here is to load the graph, spawn servers, and query the graph or run networkx algorithms through zerorpc. Obviously, we shouldn't ever modify the graph while running parallel queries on the graph.
