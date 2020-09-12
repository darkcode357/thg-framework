##
# This module requires THG: https://darkcode0x00.com/download
# Current source: https://github.com/darkcode357/thg-framework
##
import json, requests, pprint
class GeoLocate:
    def __init__(self,address,sensor=False):
        """

        :param address: str address research
        """
        self.sensor = sensor
        self.address = address

    def geolocate(self):
        """
        :return: address
        """
        parameters = {'address':self.address,'sensor':self.sensor}
        base = 'http://maps.googleapis.com/maps/api/geocode/json'
        data = requests.get(url=base, params=parameters)
        binary = data.content
        output = json.loads(binary)
        return output #todo:key google maps
#a = GeoLocate('207 N. Defiance St, Archbold, OH').geolocate()
