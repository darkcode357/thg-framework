##
# This module requires lib: https://darkcode0x00.com/download
# Current source: https://github.com/darkcode357/thg-framework
##

"""
os.path.exists() – Returns True if path or directory does exists.
os.path.isfile() – Returns True if path is File.
os.path.isdir() - Returns True if path is Directory.
"""
###
#
# File system path option.
#
###
from os.path import exists
class OptPath:
    def __init__(self,path):
        self.path = path

    def check_is_path_file(self):
        """
        :param path -> str:
            path to check
        :return: self.path
        """
        if exists(self.path):
            return self.path
        else:
            return "is not validate path or file"
