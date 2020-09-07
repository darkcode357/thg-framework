##
# This module requires THG: https://darkcode0x00.com/download
# Current source: https://github.com/darkcode357/thg-framework
##

###
#
# This sample auxiliary module simply displays the selected action and
# registers a custom command that will show up when the module is used.
#
###

from THG.Model.BaseXmodeClass.BaseMod import BaseMod ##class base to create all modules
from colorama import Fore

class Exploit(BaseMod):
  '''
herança da class pai
  '''
  def __init__(self):
    super(Exploit, self).__init__()
    self.update_info({
      "name": "torch",
      "description": "buscador de url no torch",
      "author": ["darkcode0x00"],
      "references": [
        "torch",
        ],
      "disclosure_date": "2020, 9, 5",
      "service_name": "torch",
      "service_version": "torch_search 0.1",
      "rank":12
      })
    self.register_http_target()
  def check(self):
    query = self.options.get_option("URL")
    pages = self.options.get_option("pages")
    engine = Torch()
    results = engine.search(query,int(pages))
    for resultado in results.results():
      for chave,valor in resultado.items():
        print("{}[ok]{}{}".format(Fore.GREEN,Fore.GREEN,Fore.RESET),chave,valor,"\n",end=" ")
      print(" ")




