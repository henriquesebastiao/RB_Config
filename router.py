import paramiko


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

    def configure_access_point_basic(self, connection, model: int, ssid: str, password: str, band: str) -> None:
        """
        Configure the access point with basic settings
        :param connection: SSHClient object
        :param model: model
        :param ssid: SSID
        :param password: password
        :param band: band
        :return: None
        """
        if model == 1:
            comands = [
                r'/interface wireless security-profiles set [ find default=yes ] supplicant-identity=MikroTik',
                f'/interface wireless security-profiles add authentication-types=wpa2-psk mode=dynamic-keys name=profile1 supplicant-identity="" wpa-pre-shared-key={password} wpa2-pre-shared-key={password}',
                f'/interface wireless set [ find default-name=wlan1 ] antenna-gain=6 band={band} country=brazil-anatel disabled=no frequency=auto installation=outdoor mode=ap-bridge radio-name=Groove security-profile=profile1 ssid={ssid} wireless-protocol=802.11 wps-mode=disabled',
                r'/ip pool add name=dhcp ranges=192.168.0.2-192.168.0.254',
                r'/ip dhcp-server add address-pool=dhcp disabled=no interface=wlan1 name=dhcp1',
                r'/ip neighbor discovery-settings set discover-interface-list=!dynamic',
                r'/interface list member add interface=wlan1 list=LAN',
                r'/interface list member add interface=ether1 list=WAN',
                r'/ip address add address=192.168.0.1/24 interface=wlan1 network=192.168.0.0',
                r'/ip dhcp-client add disabled=no interface=wlan1',
                r'/ip dhcp-client add disabled=no interface=ether1',
                r'/ip dhcp-server network add address=192.168.0.0/24 dns-server=8.8.8.8,1.1.1.1 gateway=192.168.0.1 netmask=24',
                r'/ip dns set servers=8.8.8.8,1.1.1.1',
                r'/ip firewall nat add action=masquerade chain=srcnat out-interface-list=WAN',
                r'/ip service set telnet disabled=yes',
                r'/ip service set api disabled=yes',
                r'/ip service set api-ssl disabled=yes',
                r'/system ntp client set enabled=yes primary-ntp=200.160.7.186 secondary-ntp=201.49.148.135',
                r'/tool romon set enabled=yes id=00:00:00:00:00:01',
            ]

            for comand in comands:
                self.send_command(connection, comand)
    def add_dhcp_server(self):  # TODO: Implementar servidor DHCP
        pass

    def add_dhcp_client(self):  # TODO: Implementar cliente DHCP
        pass
