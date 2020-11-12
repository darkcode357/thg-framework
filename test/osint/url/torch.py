from lib.thg.core.osint.search_engines import Torch
from lib.thg.core.BaseXmodeClass import BaseMod
from colorama import Fore

class Exploit(BaseMod):
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
        })
        self.register_query_target()


    def check(self):
        query = self.options.get_option("query")
        pages = self.options.get_option("pages")
        engine = Torch()
        results = engine.search(query,int(pages))
        for resultado in results.results():
            for chave,valor in resultado.items():
                    print("{}[ok]{}{}".format(Fore.GREEN,Fore.GREEN,Fore.RESET),chave,valor,"\n",end=" ")
            print(" ")




