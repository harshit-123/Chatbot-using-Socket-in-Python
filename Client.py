import socket
import sys
import time

s = socket.socket()
host = input(str("Please Enter the Host Name of the Server :"))
port = 8955
s.connect((host,port))
print("Connected to the Chat Server...")
while True:
    incomming_message = s.recv(1024)
    incomming_message = incomming_message.decode()
    print("Server :",incomming_message)
    #print("")
    message = input(str(">>"))
    message = message.encode()
    s.send(message)
    print("Message has been sent....")
    #print("")