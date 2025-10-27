import socket
import threading

host = '192.168.100.2' # local host
port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

clients = []
nicks = []

def brodcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            brodcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicks[index]
            brodcast(f'{nickname} left the chat!'.encode('ascii'))
            nicks.remove(nickname)
            break

def recive():
    while True:
        client,address = server.accept()
        print(f'Connected with {str(address)}')

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicks.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {nickname}.')
        brodcast(f'{nickname} joined the chat'.encode('ascii'))
        client.send('Connected to the server'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print('Server is listening...')
recive()