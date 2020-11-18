##
# This module requires lib: https://darkcode0x00.com/download
# Current source: https://github.com/darkcode357/thg-framework
##
#
# todo v2
#     [ok]name = 'url',,description='target url',value=url),
#         name = 'EnableUl',required=False,description="Enable maximum number of request per URI"
#         name = 'MaxUriLimit', required=False, description="Number max. request per URI"
#         name = 'TakeTimeout', required=False, description="Timeout for loop ending"
#         name = 'SleepTime', required=False, description="Sleep time (secs) between requests"
#         name = 'ReadTimeout', description="Read timeout (-1 forever)"
#         name = 'ThreadNum',   description="Threads number"
#         name = 'DontCrawl',   description="Filestypes not to crawl"
#
##
#
# Web Crawler.
#
# Author:  Rebellion   et[at]  darkcode0x00@darkcode0x00.com 2020
#
#
# class base
from lib.thg.core.BaseXmodeClass.BaseMod import BaseMod

# class aux
from lib.thg.core.auxiliary.Web import Url

# imports extra
from time import sleep
import requests
from bs4 import BeautifulSoup


class Exploit(BaseMod):
    def __init__(self):
        super(Exploit, self).__init__()
        self.update_info(
            {
                "name": "thgcrawler",
                "description": "custon crawler for website",
                "author": ["Rebellion"],
                "references": [
                    "crawler web",
                ],
                "disclosure_date": "2020, 9, 6",
                "service_name": "thgcrawler",
                "service_version": "thgcrawler 0.1",
            }
        )
        ##
        #
        # atributos de class
        #
        ##
        self.register_crawler_target()
        self.options.set_option("SleepTime", 0.5)

    def check(self):
        url = self.options.get_option("url")
        if Url(url).check_url() == True:
            pass
        else:
            print("url invalida")
            print("url=> http://|https://|https://www|http://www")

    def exploit(self):

        results = []
        url = self.options.get_option("url")
        sleeptime = self.options.get_option("SleepTime")

        print(f"Target:{url}")
        sleep(sleeptime)
        try:
            request = requests.session()
            request.keep_alive = False
            response = request.get(url=url).text
            soup = BeautifulSoup(response, "html.parser")
            for link in soup.find_all("a"):
                if link.has_attr("href"):
                    if link["href"].startswith("http://") or link["href"].startswith(
                        "https://"
                    ):
                        pass
                    elif link["href"].startswith("/"):
                        link = url + str(link["href"])
                    else:
                        link = url + "/" + str(link["href"])
                    if link not in results:
                        print(f"[+] Found link: {link}")
                        results.append(link)
            for item in results:
                response = requests.get(item).text
                soup = BeautifulSoup(response, "html.parser")
                for link in soup.find_all("a"):
                    if link.has_attr("href"):
                        if link["href"].startswith("http://") or link[
                            "href"
                        ].startswith("https://"):
                            pass
                        elif link["href"].startswith("/"):
                            link = url + str(link["href"])
                        else:
                            link = url + "/" + str(link["href"])
                        if link not in results:
                            print(f"[+] Found link: {link}")
                            results.append(link)
        except requests.exceptions as e:
            self.results.failure(
                error_message="Host {host}:{port}: {error}".format(
                    host=host, port=port, error=e
                )
            )
        return self.results
