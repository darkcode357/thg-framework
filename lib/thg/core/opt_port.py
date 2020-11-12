###
#
# Network port option.
#
###
class OptPort:
    def __init__(self,port):
        self.port = port

    def check_input_port(self):
        """
        :param port -> int:
            port to check
        :return: self.port
        """
        if self.port <= 65535 and self.port >= 0:
          return (self.port)
        else:
            return "is not validate port ranger"

#check = OptPort(65538).check_input_port()
#print(check)
