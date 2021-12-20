from xmlrpc.client import ServerProxy

client = ServerProxy("http://127.0.0.1:1337")
x1 = input("x1: ")
x2 = input("x2: ")

print(client.sum(x1, x2) )