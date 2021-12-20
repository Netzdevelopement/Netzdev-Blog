from xmlrpc.server import SimpleXMLRPCServer as Server

def sum(x1, x2): # Calc the sum of the two numbers
    erg = int(x1) + int(x2)
    return erg

server = Server(("127.0.0.1", 1337)) # (IP,Port)
server.register_function(sum) 
server.serve_forever()