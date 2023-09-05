#!/usr/bin/python3

import socket

clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#host = '192.168.56.1'
host = socket.gethostbyname()

port=444

clientsocket.connect(('192.168.56.1',port))

message=clientsocket.recv(1024)