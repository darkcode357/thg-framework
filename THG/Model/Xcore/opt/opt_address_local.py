##
# This module requires THG: https://darkcode0x00.com/download
# Current source: https://github.com/darkcode357/thg-framework
##
from THG.Model.Xcore import is_ipv4, is_ipv6
import netifaces

class OptAddressLocal:
    def __init__(self,interface):
        self.interface = interface
    def return_ip_for_interface(self):
        if netifaces.AF_INET in netifaces.ifaddresses(self.interface):
            ip = netifaces.ifaddresses(self.interface)[netifaces.AF_INET][0]['addr']
            if is_ipv4(ip):
                return ip
            elif is_ipv6(ip):
                return ip
        else:
            print("unrecognized interface")

#a = OptAddressLocal("wlp5s0").return_ip_for_interface()
#print(a)