import socket


HOST = 'localhost'
PORT = 8888


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_socket.bind((HOST, PORT))


server_socket.listen()
print("서버 대기 중...")


client_socket, client_address = server_socket.accept()
print(f"접속: {client_address}")

while True:
    chat = client_socket.recv(1024)

    if not chat:
        print("연결종료")
        break

    print(f"받은 메세지: {chat.decode("utf-8")}")

    client_socket.send(chat)



server_socket.close()
client_socket.close()
