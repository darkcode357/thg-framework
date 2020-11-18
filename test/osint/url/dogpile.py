from lib.thg.core.osint.search_engines import Dogpile
from lib.thg.core.BaseXmodeClass import BaseMod
from colorama import Fore


class Exploit(BaseMod):
    def __init__(self):
        super(Exploit, self).__init__()
        self.update_info(
            {
                "name": "dogpile",
                "description": "buscador de url no dogpile",
                "author": ["darkcode0x00"],
                "references": [
                    "dogpile",
                ],
                "disclosure_date": "2020, 9, 5",
                "service_name": "dogpile",
                "service_version": "dogpile_search 0.1",
            }
        )
        self.register_query_target()

    def check(self):
        query = self.options.get_option("query")
        pages = self.options.get_option("pages")
        engine = Dogpile()
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
