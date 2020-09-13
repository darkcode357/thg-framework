##
# This module requires THG: https://darkcode0x00.com/download
# Current source: https://github.com/darkcode357/thg-framework
##
from THG.Model.Xcore import is_ipv4, is_ipv6


class CheckOptAddress:
    """
    class check opt is valid address!
    """
    def __init__(self, address):
        """
        :param address -> str :
            recv string to contain ipaddress
        """
        self.address = address

    def validate_ipv4address(self):
        """
        :return obj -> bool:
            False or True
        """
        return is_ipv4(self.address)

    def validate_ipv6address(self):
        """
        :return obj -> bool:
            False or True
        """
        return is_ipv6(self.address)

