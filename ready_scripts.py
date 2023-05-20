from router import Router


def configure_access_point() -> str:
    """
    Return a string with the configuration for an access point
    :return: configuration
    """
    return r'''# may/19/2023 16:02:54 by RouterOS 6.49.7
# software id = MRD2-3KJJ
#
# model = Groove A-52HPn r2
# serial number = BDFC0BC847A7
/interface list
add name=WAN
add name=LAN
/interface wireless security-profiles
set [ find default=yes ] supplicant-identity=MikroTik
add authentication-types=wpa2-psk mode=dynamic-keys name=profile1 \
    supplicant-identity="" wpa-pre-shared-key=12345678 wpa2-pre-shared-key=\
    12345678
/interface wireless
set [ find default-name=wlan1 ] antenna-gain=6 band=2ghz-b/g/n country=\
    brazil-anatel disabled=no frequency=2412 installation=outdoor mode=\
    ap-bridge radio-name=Groove security-profile=profile1 ssid=MikroTik \
    wireless-protocol=802.11 wps-mode=disabled
/ip pool
add name=dhcp ranges=192.168.0.2-192.168.0.254
/ip dhcp-server
add address-pool=dhcp disabled=no interface=wlan1 name=dhcp1
/ip neighbor discovery-settings
set discover-interface-list=!dynamic
/interface list member
add list=LAN
add interface=ether1 list=WAN
/ip address
add address=192.168.0.1/24 interface=wlan1 network=192.168.0.0
/ip dhcp-client
add disabled=no interface=wlan1
add disabled=no interface=ether1
/ip dhcp-server network
add address=192.168.0.0/24 dns-server=8.8.8.8,1.1.1.1 gateway=192.168.0.1 \
    netmask=24
/ip dns
set servers=8.8.8.8,1.1.1.1
/ip firewall nat
add action=masquerade chain=srcnat out-interface-list=WAN
add action=masquerade chain=srcnat out-interface-list=WAN
/ip service
set telnet disabled=yes
set api disabled=yes
set api-ssl disabled=yes
/system note
set note="--- ATEN\C7\C3O --\r\
    \n\C9 essencial para a seguran\E7a dos usu\E1rios da rede que a senha da r\
    ede wifi e usu\E1rio e login do roteador seja alterado ap\F3s a configura\
    \E7\E3o."
/system ntp client
set enabled=yes primary-ntp=200.160.7.186 secondary-ntp=201.49.148.135
/tool romon
set enabled=yes id=00:00:00:00:00:01
'''