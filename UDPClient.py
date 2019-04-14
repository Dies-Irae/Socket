from socket import *
serverName = x.x.x.x
serverPort = xxxxx
clientSocket = socket(AF_INET,SOCK_DGRAM)
message= input('Input lowercase sentence:')
clientSocket.sendto(str.encode(message),(serverName,serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage)
clientSocket.close()