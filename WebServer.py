from socket import *
#initial a server socket
serverSocket = socket(AF_INET,SOCK_STREAM)
serverPort = 6789
serverSocket.bind(("",serverPort))
serverSocket.listen(1)

while True:
    print ('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)

        if not message:
                connectionSocket.close()
                continue
        filename = message.split()[1]

        requestFile = open(filename[1:])
        outputdata = requestFile.read()

        #Send header line
        header = 'HTTP/1.1 200 OK\r\n\
        Connection: close\r\n\
        Content-Length: %d\r\n %(len(outputdata))\
        Content-Type: text/html\r\n\r\n'
        connectionSocket.send(header.encode())

        #Send requested file
        for i in range(0,len(outputdata)) :
            connectionSocket.send(outputdata[i])
        connectionSocket.close()

    except IOError :
        header = 'HTTP/1.1 404 Not Found \r\n'
        connectionSocket.send(header.encode())
        connectionSocket.close()

serverSocket.close()
