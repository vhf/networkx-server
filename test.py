import zerorpc
from pprint import pprint

server_count = 10
result = dict(
    edges1 = set(),
    ids1 = set(),
    edges2 = set(),
    ids2 = set(),
)

for i in range(4200, 4200 + server_count):
    c = zerorpc.Client()
    c.connect("tcp://127.0.0.1:{}".format(i))
    result['edges1'].add(c.edges()[-1][1])
    result['ids1'].add(c.id())

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:4201".format(i))
c.add()

for i in range(4200, 4200 + server_count):
    c = zerorpc.Client()
    c.connect("tcp://127.0.0.1:{}".format(i))
    result['edges2'].add(c.edges()[-1][1])
    result['ids2'].add(c.id())

pprint(result)

if len(result['ids1']) > 1:
    print("Object has been copied {} times :(".format(len(result['ids1'])))

if len(result['ids2']) > 1:
    print("Object has been copied {} times since being modified :(".format(len(result['ids2'])))
