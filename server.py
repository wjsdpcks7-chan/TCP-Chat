import socket


HOST = 'localhost'
PORT = 8888


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_socket.bind((HOST, PORT))


server_socket.listen()
print("서버 대기 중...")


client_socket, client_address = server_socket.accept()
print(f"접속: {client_address}")


server_socket.close()
client_socket.close()
