import zerorpc

server_count = 4

for i in range(4200, 4200 + server_count):
    c = zerorpc.Client()
    c.connect("tcp://127.0.0.1:{}".format(i))
    print(c.edges())
