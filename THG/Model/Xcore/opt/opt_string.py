class OptString:
    def __init__(self,string):
        self.string = string
    def check_string(self):
        if type(self.string) == str:
            return self.string
        else:
            return 'is not string'