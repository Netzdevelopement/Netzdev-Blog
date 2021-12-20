from xmlrpc.client import ServerProxy, MultiCall

client = ServerProxy("http://127.0.0.1:1337")
x1 = input("x1: ")
x2 = input("x2: ")

multicl = MultiCall(client)
multicl.sum(x1,x2) 
multicl.div(x1,x2)

