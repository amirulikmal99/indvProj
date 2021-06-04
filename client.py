import socket


ClientSocket = socket.socket()

host = '192.168.56.104'
port = 8888

print("Waiting for connection")

try:

        ClientSocket.connect((host, port))

except socket.error as e:

        print(str(e))


response = ClientSocket.recv(1024)

print(response)

while True:

        Input = input("Message to Server: ")  #send chat to server

        ClientSocket.send(str.encode(Input))

        response = ClientSocket.recv(1024)

        print(response.decode('utf-8'))
        print("Disconnected")
        break
ClientSocket.close()
