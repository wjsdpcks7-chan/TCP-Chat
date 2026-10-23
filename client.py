import socket

HOST = 'localhost'
PORT = 8888

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))

while True:
    chat = input("나:")
    if chat == "out":
        break
    
    client_socket.send(chat.encode("utf-8"))
    reply = client_socket.recv(1024)
    print(f"서버: {reply.decode("utf-8")}")

client_socket.close()