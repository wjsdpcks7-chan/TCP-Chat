import socket
import threading

HOST = 'localhost'
PORT = 5555

def receive_chat(client_socket):
    while True:
        receive = client_socket.recv(1024)

        if not receive:
            print("끊김")
            break
        print(f"\n{receive.decode('utf-8')}")

def start_chat(client_socket):
    print("서버에 접속했습니다.")
    nickname = input("사용할 닉네임: ")
    print("채팅방에 입장했습니다.")
    print("종료를 원할시 out을 입력해주세요.")

    client_socket.sendall(nickname.encode('utf-8'))
    
    


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))

start_chat(client_socket)

t = threading.Thread(target= receive_chat, args=(client_socket,), daemon=True)
t.start()



while True:
    chat = input("나:")
    if chat == "out":
        break
    
    client_socket.sendall(chat.encode('utf-8'))
    

client_socket.close()