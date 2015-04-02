import socket
import sys

HOST = 'localhost'
PORT = 8001             
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

#debes escribir el dato cuando ejecutas el programa(sys.argv[1])
#Ej. escribir en terminal: python client2.py 20.5
s.sendall(sys.argv[1])
data = s.recv(1024)
s.close()
print('Received', repr(data))

