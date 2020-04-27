import socket
import sys
import time
s = socket.socket()
host = socket.gethostname()
print("Server will Start on Host:",host)
port = 8955
s.bind((host,port))
#print("")
print("Server done Binding to the Host and Port Successfully")
#print("")
print("Server is Waiting for Incomming Connections")
#print("")
s.listen(1)
conn,addr = s.accept()
print(addr,"Has connected to the Server and is Online...")
#print("")
while True:
    message = input(str(">>"))
    message = message.encode()
    conn.send(message)
    print("Message has been sent....")
    #print("")

    incomming_message = conn.recv(1024)
    incomming_message = incomming_message.decode()
    print("Client :", incomming_message)
   # print("")