import socket
import threading


HOST = 'localhost'
PORT = 8888
clients = []

def broadcast(chat, sender_socket):
    for i in clients:
        if i != sender_socket:
            i.sendall(chat)

def handle_client(client_socket, client_address):
    print(f"접속: {client_address}")

    while True:
        chat = client_socket.recv(1024)

        if not chat:
            print(f"종료: {client_address}")
            break

        print(f"받은 메세지: {chat.decode('utf-8')}")

        broadcast(chat, client_socket)

    client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()
print("서버 대기 중...")

while True:
    client_socket, client_address = server_socket.accept()

    clients.append(client_socket)
    t = threading.Thread(target=handle_client, args=(client_socket,client_address))
    t.start()



server_socket.close()
