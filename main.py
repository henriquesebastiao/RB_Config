from router import Router
from functions import *
from ready_scripts import *

print('''Bem-vindo ao RB_Config!
v0.0.1
Autor: Henrique Sebastião\n''')

print("Para começar, informe os dados do roteador")
ip = input("IP: ")
port = int(input("Porta SSH: "))
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
    print("3 - Setar Servidores NTP da RB")
    print("4 - Adicionar IP")
    print("5 - Configurar Access Point")
    print("Ctrl + C - Sair\n")
    option = int(input("Opção: "))

    match option:
        case 1:  # Send a command to the router
            clear()
            command = input("Comando: ")
            router_board.send_command(connection, command)
        case 2:  # Set DNS Servers on the router
            clear()
            number_servers = int(input("Quantos servidores DNS deseja adicionar? "))

            servers = []

            for i in range(number_servers):
                servers.append(input(f"Servidor DNS {i + 1}: "))

            for dns in servers:
                if not validate_ip(dns):
                    print("IP inválido")
                    exit()

            router_board.set_dns(connection, *servers)

        case 3:  # Configure NTP Servers on the router
            clear()
            print("Escolha um modo:")
            print("1 - broadcast")
            print("2 - manycast")
            print("3 - multicast")
            print("4 - unicast")
            option = int(input("Opção: "))

            if option not in range(1, 5):
                print("Opção inválida")
                exit()

            modes = ["broadcast", "manycast", "multicast", "unicast"]
            mode = modes[option - 1]

            primary_server = input("Servidor primário: ")
            if not validate_ip(primary_server):
                print("IP inválido")
                exit()

            secondary_server = input("Servidor secundário: ")
            if not validate_ip(secondary_server):
                print("IP inválido")
                exit()

            router_board.set_ntp(connection, mode, primary_server, secondary_server)
        case 4:  # Add an IP address to the router
            clear()
            ip = input("IP: ")

            if not validate_ip(ip):
                print("IP inválido")
                exit()

            interface = input("Interface: ")
            netmask = input("Netmask: ")

            if not validate_netmask(netmask):
                print("Netmask inválida")
                exit()

            router_board.add_ip(connection, ip, interface, netmask)
        case 5:  # Configure Access Point
            clear()
            print("Escolha um modelo:")
            print("1 - Groove A-52HPn r2 (Modelo de 5.8GHz e 2.4GHz)")
            try:
                model = int(input("Opção: "))
            except ValueError:
                print("Opção inválida")
                exit()

            clear()
            print("Informe os dados para o Access Point")
            ssid = input("SSID: ")
            password = input("Senha da rede: ")

            if model == 1:
                clear()
                print("Escolha uma banda:")
                print("1 - 2.4GHz")
                print("2 - 5.8GHz")
                band = int(input("Opção: "))

                if band not in range(1, 3):
                    print("Opção inválida")
                    exit()
                else:
                    band = "2ghz-b/g/n" if band == 1 else "5ghz-a/n"

            router_board.configure_access_point_basic(connection, model, ssid, password, band)
        case _:
            print("Opção inválida")

    router_board.disconnect(connection)  # Disconnect from the router
except ValueError:
    print("Opção inválida")
except KeyboardInterrupt:
    print("Saindo...")
    exit()
