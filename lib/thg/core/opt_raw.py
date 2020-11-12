import pkg_resources
import os.path
###
#
# Raw, arbitrary data option.
#
###
class OptRaw:
    def __init__(self,raw):
        self.raw = raw

    def check_raw_file(self):
          if os.path.isfile(self.raw) == True:
              file = 'file://' + pkg_resources.resource_filename(__name__, '{}'.format(self.raw))
              return file
          else:
              return "is not validate Raw, arbitrary data"

#a = OptRaw("author.py").check_raw_file()
#print(a)