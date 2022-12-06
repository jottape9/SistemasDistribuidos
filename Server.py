import threading
import socket

contrato = []


def serverstart():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind(("0.0.0.0", 2222))
        server.listen()
    except:
        return print('\n Não iniciou o servidor!\n')

    while True:
        client, addr = server.accept()

        thread = threading.Thread(target=tratamentomensagem, args=[client])
        thread.start()


def tratamentomensagem(client):
    while True:
        try:
            msg = client.recv(2048)
            print(msg.decode('utf-8'))
        except:
            break

serverstart()
