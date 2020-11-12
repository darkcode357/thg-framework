from lib.thg.core.osint.search_engines.engines import Startpage
from lib.thg.core.BaseXmodeClass import BaseMod
from colorama import Fore

class Exploit(BaseMod):
    def __init__(self):
        super(Exploit, self).__init__()
        self.update_info({
            "name": "startpage",
            "description": "buscador de url no startpage",
            "author": ["darkcode0x00"],
            "references": [
                "startpage",
            ],
            "disclosure_date": "2020, 9, 5",
            "service_name": "startpage",
            "service_version": "startpage_search 0.1",
        })
        self.register_query_target()


    def check(self):
        query = self.options.get_option("query")
        pages = self.options.get_option("pages")
        engine = Startpage()
        results = engine.search(query,int(pages))
        for resultado in results.results():
            for chave,valor in resultado.items():
                    print("{}[ok]{}{}".format(Fore.GREEN,Fore.GREEN,Fore.RESET),chave,valor,"\n",end=" ")
            print(" ")




