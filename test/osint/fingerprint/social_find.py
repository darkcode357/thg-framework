from lib.thg.core.osint import Startpage
from lib.thg.core.BaseXmodeClass import BaseMod
from colorama import Fore


class Exploit(BaseMod):
    def __init__(self):
        super(Exploit, self).__init__()
        self.update_info(
            {
                "name": "social_find",
                "description": "buscador de redes sociais em uma url",
                "author": ["darkcode0x00"],
                "references": [
                    "social_find",
                ],
                "disclosure_date": "2020, 9, 6",
                "service_name": "social_find",
                "service_version": "social_find_search 0.1",
            }
        )
        self.register_social_target()

    def check(self):
        query = self.options.get_option("url")
        engine = Startpage()
        results = engine.search(query, int(pages))
        for resultado in results.results():
            for chave, valor in resultado.items():
                print(
                    "{}[ok]{}{}".format(Fore.GREEN, Fore.GREEN, Fore.RESET),
                    chave,
                    valor,
                    "\n",
                    end=" ",
                )
            print(" ")
