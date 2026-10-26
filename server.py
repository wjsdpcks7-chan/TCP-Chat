import socket
import threading


HOST = 'localhost'
PORT = 5555
clients = []

def broadcast(chat, sender_socket):
    for s in clients:
        if s != sender_socket:
            s.sendall(chat)

def handle_client(client_socket, client_address):
    print(f"접속: {client_address}")

    nickname = client_socket.recv(1024).decode('utf-8')
    broadcast(f"[{nickname}]님이 입장하였습니다.".encode('utf-8'), client_socket)
    clients.append(client_socket)

    while True:
        chat = client_socket.recv(1024)

        if not chat:
            print(f"종료: {client_address}")
            break

        message = f"[{nickname}]: {chat.decode('utf-8')}"

        broadcast(message.encode('utf-8'), client_socket)

    client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()
print("서버 대기 중...")

while True:
    client_socket, client_address = server_socket.accept()

    t = threading.Thread(target=handle_client, args=(client_socket,client_address), daemon=True)
    t.start()




server_socket.close()
