import socket
import threading


HOST = 'localhost'
PORT = 8888
clients =[]

def chating(client_socket, client_address):
    print(f"접속: {client_address}")

    while True:
        chat = client_socket.recv(1024)

        if not chat:
            print("연결종료")
            break

        print(f"받은 메세지: {chat.decode("utf-8")}")

        client_socket.send(chat)

    client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_socket.bind((HOST, PORT))


server_socket.listen()
print("서버 대기 중...")


while (1):
    client_socket, client_address = server_socket.accept()

    clients.append(client_socket)
    t = threading.Thread(target=chating, args=(client_socket,client_address))
    t.start()



server_socket.close()
