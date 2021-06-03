import socket
import os
from _thread import *


serverSocket = socket.socket()

host = ""
port = 8888
ThreadCount = 0

try:

    serverSocket.bind((host, port))

except socket.error as e:

    print(str(e))


print('Waiting for a Connection... ')

serverSocket.listen(5)


def threaded_client(connection):

    connection.send(str.encode(" Welcome to the Server \n"))  


    terima = connection.recv(2048)
    if not terima:
                print ("No message")  #print
    else:
                msg = terima.decode()
                print ("Client message: ", msg)
                chat = input("Mesej Server: " ) #send chat to client 
                reply = 'Server Says: ' + chat 
                connection.sendall(str.encode(reply))

    connection.close()


while True:

    Client, address = serverSocket.accept()

    print('Connected to: ' + address[0] + ':' + str(address[1])) #keluar bila dah connect dgn client 

    start_new_thread(threaded_client, (Client, ))

    ThreadCount += 1

    print('Thread Number: ' + str(ThreadCount)) #tunjuk thread number

serverSocket.close()
