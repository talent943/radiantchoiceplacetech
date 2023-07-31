import socket

s = socket.socket()
host = socket.gethostbyname('localhost')
print("HOST NAME IS:{}".format(host))
# host = '127.0.0.1'
port = 1234

s.connect((host, port))
print(s.recv(1024))
s.close
