##
# This module requires THG: https://darkcode0x00.com/download
# Current source: https://github.com/darkcode357/thg-framework
##

class Url:
    def __init__(self,url):
        """
        :param url:str
        """
        self.url = url
    def check_url(self):
        try:
            from urllib.parse import urlparse
        except ImportError:
            print("install urllib")
        try:
            result = urlparse(self.url)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False





