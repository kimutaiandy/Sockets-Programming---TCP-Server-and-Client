import socket #here we import the socket module from the python library

#creating a server socket object - specifying the socket type and family
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = '192.168.56.1'
host = socket.gethostbyname()
port = 444

#we bind address to port/socket
serversocket.bind(('192.168.56.1', port)) #host will be replaced/substituted with IP, if changed and not running on host

#starting tcp listener
serversocket.listen(3)

while True:
    #starting the connection
    clientsocket, address = serversocket.accept()

    print("received connection from" % str(address))

    message = "hello! Thank you for connecting to the server"  "\r\n"
    clientsocket.send(message.encode('ascii'))

    clientsocket.close()
    