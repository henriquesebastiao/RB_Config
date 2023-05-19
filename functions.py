import os
import re


def clear():
    """Clear the terminal screen"""
    os.system("cls" if os.name == "nt" else "clear")


def validate_ip(ip: str) -> bool:
    """
    Validate an IP address    :param ip:  to be validated
    :return: True if the IP address is valid, False otherwise
    """
    regex = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    if re.match(regex, ip):
        return True
    else:
        return False


def validate_netmask(netmask: str) -> bool:
    """
    Validate a netmask
    :param netmask: Netmask to be validated
    :return: True if the netmask is valid, False otherwise
    """
    list_netmask = [
        "255.0.0.0",
        "255.128.0.0",
        "255.192.0.0",
        "255.224.0.0",
        "255.240.0.0",
        "255.248.0.0",
        "255.252.0.0",
        "255.254.0.0",
        "255.255.0.0",
        "255.255.128.0",
        "255.255.192.0",
        "255.255.224.0",
        "255.255.240.0",
        "255.255.248.0",
        "255.255.252.0",
        "255.255.254.0",
        "255.255.255.0",
        "255.255.255.128",
        "255.255.255.192",
        "255.255.255.224",
        "255.255.255.240",
        "255.255.255.248",
        "255.255.255.252",
    ]

    if netmask in list_netmask:
        return True
    else:
        return False
