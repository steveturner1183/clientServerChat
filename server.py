#  Author: Steven Turner
#  Date: 8/1/2021
#  Description: Server side of a simple client-server chat program

# ######################################## #
# Sources:                                 #
# Computer Networking by Kurose and Ross   #
#                                          #
# ######################################## #

# Sources for following code:
# Computer Networking by Kurose and Ross - Chapter 2.7.2 pg 163

from socket import *

# Set up initial connection and wait for client to connect
serverName = 'localhost'
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen(1)
print('Server listening on: ' + serverName + ' on port: ' + str(serverPort))

# Create connection and send message
connectionSocket, addr = serverSocket.accept()
connectionMessage = 'Connected to: ' + serverName + ' on port: ' + str(serverPort) + '\nType /q to quit' + \
                    '\nEnter message to send...'
connectionSocket.send(connectionMessage.encode())

# Receive message after connection
messageFromClient = connectionSocket.recv(1024).decode()
print(messageFromClient)
print('Waiting for message...')

while True:
    messageFromClient = connectionSocket.recv(1024).decode()

    if messageFromClient == '/q':  # close connection when client sends /q
        connectionSocket.close()
        break

    print('Client: ' + messageFromClient)
    messageToClient = input('Server: ')

    if messageToClient == '/q':  # server quits
        connectionSocket.send(messageToClient.encode())
        connectionSocket.close()
        break

    connectionSocket.send(messageToClient.encode())  # send message to client
