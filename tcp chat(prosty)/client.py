import socket
import threading

nickname = input("chose a nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.100.2',9999))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print('Error')
            client.close()
            break

def writte():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

writte_thread = threading.Thread(target=writte)
writte_thread.start()