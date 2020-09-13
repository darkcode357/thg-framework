##
# This module requires THG: https://darkcode0x00.com/download
# Current source: https://github.com/darkcode357/thg-framework
##

class OptInt:
    def __init__(self, checkinit):
        self.checkinit = checkinit

    def check_init(self):
        if type(self.checkinit) == int:
            return self.checkinit
        else:
            return "is not int"


#check_init = OptInt(1).check_init()
#print(check_init)
