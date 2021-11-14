import socket
#Creating socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #preciso estudar mais sobre os tipos e familias

#host = '192.x.x.x'
host = socket.gethostname()       
port = 444

#Biding to socket
server_socket.bind(('192.168.200.104', port))

#Starting TCP listener
server_socket.listen(3) 

while True:
    # Starting the connection
    client_socket, address = server_socket.accept()

    print(f"receive connection from: {address}")

    message = f"Hello! Thank you for connection to the server.\r\nThis is an example how socket can work"
    client_socket.send(message.encode('ascii'))

    client_socket.close()
