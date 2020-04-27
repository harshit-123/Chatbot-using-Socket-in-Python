import socket
import sys
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket is successfully created")
except socket.error as err:
    print("Socket creation failed with error",err)

# default port for socket
port =8955
try:
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:
    # this means could not resolve the host
    print("there was an error resolving the host")
    sys.exit()
s.connect((host_ip,port))
print("the socket has successfully connected to google on port %s" %(host_ip))