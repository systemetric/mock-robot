from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler


class RemoteRobot():
    def __init__(self):
        print("Remote init called")
        self.foo = "foo"

    def see(self):
        return "I CAN SEE"

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8001),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

server.register_instance(RemoteRobot())

# Run the server's main loop
server.serve_forever()
