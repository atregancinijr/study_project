import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
#host = '192.168.200.104'
port = 444

client_socket.connect(('192.168.200.104', port))

message = client_socket.recv(1024)

client_socket.close()

print(message.decode('ascii'))
