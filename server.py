import socket

def ServerProgram():
    host = socket.gethostbyname('localhost')
    print("HOST NAME IS:{}".format(host))
    # host = '127.0.0.1'
    port = 1234
    ServerSocket = socket.socket()
    ServerSocket.bind((host, port))
    ServerSocket.listen(2)
    conn, ClientAddress = ServerSocket.accept()
    print("Connection from: " + str(ClientAddress))
    while True:
        ClientMsg = conn.recv(1024).decode()
        if not ClientMsg:
            break
        print("from connected user: " + str(ClientMsg))
        ClientMsg = input(' -> ')
        conn.send(ClientMsg.encode())
    conn.close()
if __name__ == '__main__':
    ServerProgram()