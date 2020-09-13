##
# This module requires THG: https://darkcode0x00.com/download
# Current source: https://github.com/darkcode357/thg-framework
##
# autor:nat

class OptFloat:
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
            return "Erro no valor"  # todo mudar para o processo de class do not set
