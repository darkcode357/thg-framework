from THG.Model.Xmode.osint.search_engines import Yahoo
from THG.Model.Xmode.exploit.BaseExploit import BaseExploit
from THG.Model.BaseXmodeClass.BaseOption import BaseOption
from colorama import Fore

class Exploit(BaseExploit):
    def __init__(self):
        super(Exploit, self).__init__()
        self.update_info({
            "name": "yahoo",
            "description": "buscador de url no yahoo",
            "author": ["darkcode0x00"],
            "references": [
                "yahoo",
            ],
            "disclosure_date": "2020, 9, 5",
            "service_name": "yahoo",
            "service_version": "yahoo_search 0.1",
        })
        self.register_query_target()


    def check(self):
        query = self.options.get_option("query")
        pages = self.options.get_option("pages")
        engine = Yahoo()
        results = engine.search(query,int(pages))
        for resultado in results.results():
            for chave,valor in resultado.items():
                    print("{}[ok]{}{}".format(Fore.GREEN,Fore.GREEN,Fore.RESET),chave,valor,"\n",end=" ")
            print(" ")




