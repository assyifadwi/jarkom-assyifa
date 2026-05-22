from socket import *

serverPort = 6789

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))

serverSocket.listen(1)

print("Server siap di http://localhost:6789")

while True:

    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024).decode()

        print(message)

        filename = message.split()[1]

        if filename == '/':
            filename = '/index.html'

        f = open(filename[1:], 'r', encoding='utf-8')

        outputdata = f.read()

        connectionSocket.send("HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n".encode())

        connectionSocket.send(outputdata.encode())

        connectionSocket.close()

    except IOError:

        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())

        connectionSocket.send(
            "<html><body><h1>404 Not Found</h1></body></html>".encode()
        )

        connectionSocket.close()
        