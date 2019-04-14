from socket import *
serverName = x.x.x.x
serverPort = xxxxx
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence= input("Input lowercase sentence:")
clientSocket.send(str.encode(sentence))
modifiedSentence = clientSocket.recv(1024)
print ('From Server:', modifiedSentence.decode())
clientSocket.close()
