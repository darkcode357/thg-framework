##
# This module requires THG: https://darkcode0x00.com/download
# Current source: https://github.com/darkcode357/thg-framework
##
from re import error
from re import compile
class OptRegex:
    def __init__(self,regex):
        self.regex = regex

    def check_regex(self):
        try:
            compile(self.regex)
            return self.regex
        except error:
            return "is not a regex expression"

#check_regex = OptRegex('[0-9]').check_regex()
#print(check_regex)