import paramiko
import sys


class Router:
    def __init__(self, ip, port, username, password):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password

    def get_ip(self):
        return self.ip

    def get_port(self):
        return self.port

    def get_username(self):
        return self.username

    def get_password(self):
        """
        Get the password for the router
        :return: password
        """
        return self.password

    def connect(self):
        """
        Connect to the router via SSH

        :return: SSHClient object
        """
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, self.port, self.username, self.password)
        return ssh

    def disconnect(self, connection):
        """
        Disconnect from the router
        :param connection: SSHClient object
        :return: None
        """
        connection.close()

    def send_command(self, connection, command):
        """
        Send a command to the router
        :param connection: SSHClient object
        :param command: command to be sent
        :return: None
        """
        stdin, stdout, stderr = connection.exec_command(command)

    def add_ip(self, connection, ip, interface, netmask):
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

    def set_dns(self, connection, *ip):
        """
        Set the DNS server
        :param connection: SSHClient object
        :param ip: IP address
        :return: None
        """
        command = f"/ip dns set servers={ip}"  # Example: "8.8.8.8,8.8.4.4"
        self.send_command(connection, command)

