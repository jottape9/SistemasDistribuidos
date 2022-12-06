import threading
import socket


def clientstart():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect(('192.168.0.20', 2222))
    except:
        return print('\n Não conectou\n')

    print('\nConectou')
    print("Bem vindo ao Banco Juliet")
    user = input("Digite o Usuario: ")


    thread = threading.Thread(target=enviarmensagem, args=[client, user])
    thread.start()


def enviarmensagem(client, user):
    while True:
        try:

            nomecliente = input('Digite o Nome do cliente: \n')
            cpf = input('Digite o CPF: \n')
            datanasc = input('Digite sua data de nascimento: \n')
            cadastro = ["usuario: " + user, "Nome cliente: " + nomecliente, "cpf: " + cpf, "data de nascimento: " + datanasc]
            client.send(f'{cadastro}'.encode('utf-8'))
        except:
            return

clientstart()

