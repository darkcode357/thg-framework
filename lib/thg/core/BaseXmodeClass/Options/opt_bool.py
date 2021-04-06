##
# This module requires lib: https://darkcode0x00.com/download
# Current source: https://github.com/darkcode357/thg-framework
##


class OptBool:
    def __init__(self, value):
        """

        :param value:
        """
        self.value = value

    def check(self):
        try:
            assert type(self.value) == bool
            return self.value
        except:
            return "is not validate path or file"
