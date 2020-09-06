from THG.Model.Xmode.osint.search_engines import Mojeek
from THG.Model.Xmode.exploit.BaseExploit import BaseExploit
from colorama import Fore

class Exploit(BaseExploit):
    def __init__(self):
        super(Exploit, self).__init__()
        self.update_info({
            "name": "mojeek",
            "description": "buscador de url no mojeek",
            "author": ["darkcode0x00"],
            "references": [
                "mojeek",
            ],
            "disclosure_date": "2020, 9, 5",
            "service_name": "mojeek",
            "service_version": "mojeek_search 0.1",
        })
        self.register_query_target()


    def check(self):
        query = self.options.get_option("query")
        pages = self.options.get_option("pages")
        engine = Mojeek()
        results = engine.search(query,int(pages))
        for resultado in results.results():
            for chave,valor in resultado.items():
                    print("{}[ok]{}{}".format(Fore.GREEN,Fore.GREEN,Fore.RESET),chave,valor,"\n",end=" ")
            print(" ")




