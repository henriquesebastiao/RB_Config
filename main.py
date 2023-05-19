from router import Router
from functions import *

print('''Bem-vindo ao RB_Config!
v0.0.1
Autor: Henrique Sebastião\n''')

print("Para começar, informe os dados do roteador")
ip = input("IP: ")
port = input("Porta SSH: ")
username = input("Usuário: ")
password = input("Senha: ")

clear()

router_board = Router(ip, port, username, password)  # Create a Router object
try:
    connection = router_board.connect()  # Connect to the router
except:
    print("Erro ao conectar ao roteador")
    exit()

try:
    print("Escolha uma opção:")
    print("1 - Enviar comando")
    print("2 - Setar DNS da RB")
    print("Ctrl + C - Sair")
    option = int(input("Opção: "))

    match option:
        case 1:
            command = input("Comando: ")
            router_board.send_command(connection, command)
        case 2:
            number_servers = int(input("Quantos servidores DNS deseja adicionar? "))
            servers = []
            for i in range(number_servers):
                servers.append(input(f"Servidor DNS {i + 1}: "))
            router_board.set_dns(*servers)
        case _:
            print("Opção inválida")

    router_board.disconnect(connection)  # Disconnect from the router
except ValueError:
    print("Opção inválida")
except KeyboardInterrupt:
    print("Saindo...")
    exit()
