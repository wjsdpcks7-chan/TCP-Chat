import socket
import threading

HOST = 'localhost'
PORT = 8888

def receive_chat(client_socket):
    while True:
        receive = client_socket.recv(1024)

        if not receive:
            print("끊김")
            break
        print(f"\n[다른 참가자]: {receive.decode('utf-8')}")
    
    


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))
print("서버에 접속했습니다.")
print("(종료: out)")

t = threading.Thread(target= receive_chat, args=(client_socket,), daemon=True)
t.start()


while True:
    chat = input("나:")
    if chat == "out":
        break
    
    client_socket.sendall(chat.encode('utf-8'))
    

client_socket.close()