import paramiko
import sys


class Router:
    def __init__(self, ip: str, port: int, username: str, password: str):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password

    def get_ip(self) -> str:
        """
        Get the IP address for the router
        :return: IP address
        """
        return self.ip

    def get_port(self) -> int:
        """
        Get the port for the router
        :return: port
        """
        return self.port

    def get_username(self) -> str:
        """
        Get the username for the router
        :return: username
        """
        return self.username

    def get_password(self) -> str:
        """
        Get the password for the router
        :return: password
        """
        return self.password

    def connect(self) -> paramiko.SSHClient:
        """
        Connect to the router via SSH
        :return: SSHClient object
        """
        connection = paramiko.SSHClient()
        connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        connection.connect(self.ip, self.port, self.username, self.password)
        return connection

    def disconnect(self, connection):
        """
        Disconnect from the router
        :param connection: SSHClient object
        :return: None
        """
        connection.close()

    def send_command(self, connection, command: str):
        """
        Send a command to the router
        :param connection: SSHClient object
        :param command: command to be sent
        :return: None
        """
        stdin, stdout, stderr = connection.exec_command(command)

    def add_ip(self, connection, ip: str, interface: str, netmask: str):
        """
        Add an IP address to the router
        :param connection: SSHClient object
        :param ip: IP address
        :param interface: interface
        :param netmask: netmask
        :return: None
        """
        command = f"/ip address add address={ip} interface={interface} netmask={netmask}"
        self.send_command(connection, command)

    def set_dns(self, connection, *ip: str):
        """
        Set the DNS server
        :param connection: SSHClient object
        :param ip: IP address
        :return: None
        """
        command = f"/ip dns set servers={ip}"  # Example: "8.8.8.8,8.8.4.4"
        self.send_command(connection, command)

    def set_ntp(self, connection, mode: str, primary_server: str, secondary_server: str):
        """
        Set the NTP server
        :param connection: SSHClient object
        :param mode: mode
        :param primary_server: primary server
        :param secondary_server: secondary server
        :return: None
        """
        command = f"/system ntp client set enabled=yes mode={mode} primary-ntp={primary_server} secondary-ntp={secondary_server}"
        self.send_command(connection, command)

    def add_dhcp_server(self):  # TODO: Implementar servidor DHCP
        pass

    def add_dhcp_client(self):  # TODO: Implementar cliente DHCP
        pass
