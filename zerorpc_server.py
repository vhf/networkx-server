import multiprocessing
import zerorpc

class HelloRPC(object):
    def hello(self, name):
        return "Hello, {}".format(name)

def serve(port):
    print(port)
    print(multiprocessing.current_process())
    print("Starting RCP server on port {}".format(port))
    s = zerorpc.Server(HelloRPC())
    s.bind("tcp://0.0.0.0:{}".format(port))
    s.run()
