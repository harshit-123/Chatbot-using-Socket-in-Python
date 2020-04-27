import socket
import sys

s = socket.socket()
print("Socket created successfully")
port = 8955
s.bind(('127.0.0.1',port))
print("socket binded to port %s" %(port))
s.listen(1)
while True:
    c ,addr = s.accept()
    print("Got Connection from", addr)
    c.send("thanks for connecting")
    c.close()
