from socket import *


serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)

# Create connection and send message to server
clientSocket.connect((serverName, serverPort))
messageToServer = 'Connected by (' + serverName + ', ' + str(serverPort) + ')'
clientSocket.send(messageToServer.encode())

# Receive response from server
messageFromServer = clientSocket.recv(1024)
print(messageFromServer.decode())

# Send initial message
messageToServer = input('Client: ')

if messageToServer == '/q':  # client prompts to quit
    clientSocket.send(messageToServer.encode())
    clientSocket.close()

else:
    messageToServer += '\nType /q to quit\nEnter message to send...'
    clientSocket.send(messageToServer.encode())

    # Receive initial message from server
    messageFromServer = clientSocket.recv(1024).decode()

    if messageFromServer == '/q':  # Send /q to server and close connection
        clientSocket.close()

    else:
        print('Server: ' + messageFromServer)

        while True:  # Continue sending and receiving messages until client or server types /q
            messageToServer = input('Client: ')

            if messageToServer == '/q':  # client quits
                clientSocket.send(messageToServer.encode())
                clientSocket.close()
                break

            clientSocket.send(messageToServer.encode())  # send message to server
            messageFromServer = clientSocket.recv(1024).decode()

            if messageFromServer == '/q':  # Send /q to server and close connection
                clientSocket.close()
                break

            # Respond to server
            print('Server: ' + messageFromServer)



