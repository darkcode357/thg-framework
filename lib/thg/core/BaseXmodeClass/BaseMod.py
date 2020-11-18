##
# This module requires lib: https://darkcode0x00.com/download
# Current source: https://github.com/darkcode357/thg-framework
##

from lib.thg.core.BaseXmodeClass.BaseOption import BaseOption
from lib.thg.core.BaseXmodeClass.BaseOptions import BaseOptions
from lib.thg.core.BaseXmodeClass.BaseResult import BaseResult
from lib.thg.core_import import constants


class BaseMod:
    """class attributes aimed at creating modules
    name = None
    description = None
    author = []
    references = []
    disclosure_date = None
    service_name = None
    service_version = None
    multi_target = False
    targets = []
    target_type = None
    options = None
    results = None

    :todo add
    Arch =  None,  # No architectures by default.
    Platform =  [],  # No platforms by default.
    Privileged =  None,
    License =  constants.THG_LICENSE,
    Notes =  {}


    """

    name = None
    description = None
    author = []
    references = []
    disclosure_date = None
    service_name = None
    service_version = None
    info_fields = [
        "name",
        "description",
        "author",
        "references",
        "disclosure_date",
        "service_name",
        "service_version",
    ]

    multi_target = False
    targets = []
    target_type = None

    options = None
    results = None

    def __init__(self):
        """
        constructor method accessing class attributes
        """
        self.multi_target = False
        self.target_type = None
        self.targets = []
        self.options = BaseOptions()
        self.results = BaseResult()

    @property
    def get_info(self):
        """função recebe informações dos modulos"""
        info = {}
        for field_name in self.info_fields:
            info[field_name] = getattr(self, field_name)
        return info

    from lib.thg.core.BaseXmodeClass.BaseOption import BaseOption

    def register_query_target(self, query="darkcode", pages=20):
        """adicionar metodo query, para busca de informações"""
        self.target_type = "query"
        self.register_options(
            [
                BaseOption(
                    name="query",
                    required=True,
                    description="query para busca de dados ",
                    value=query,
                ),
                BaseOption(
                    name="pages",
                    required=True,
                    description="numero maximo de páginas a se buscar",
                    value=pages,
                ),
            ]
        )

    def register_crawler_target(
            self,
            enableUl=None,
            storeDB=None,
            maxUriLimit=None,
            sleepTime=None,
            takeTimeout=None,
            readTimeout=None,
            threadNum=None,
            dontCrawl=None,
            url=None,
    ):
        self.target_type = "crawler"
        self.register_options(
            [
                BaseOption(
                    name="url", required=True, description="target url", value=url
                ),
                BaseOption(
                    name="EnableUl",
                    required=False,
                    description="Enable maximum number of request per URI",
                    value=enableUl,
                ),
                BaseOption(
                    name="StoreDB",
                    required=False,
                    description="Store requests in database",
                    value=storeDB,
                ),
                BaseOption(
                    name="MaxUriLimit",
                    required=False,
                    description="Number max. request per URI",
                    value=maxUriLimit,
                ),
                BaseOption(
                    name="SleepTime",
                    required=False,
                    description="Sleep time (secs) between requests",
                    value=sleepTime,
                ),
                BaseOption(
                    name="TakeTimeout",
                    required=False,
                    description="Timeout for loop ending",
                    value=takeTimeout,
                ),
                BaseOption(
                    name="ReadTimeout",
                    required=False,
                    description="Read timeout (-1 forever)",
                    value=readTimeout,
                ),
                BaseOption(
                    name="ThreadNum",
                    required=False,
                    description="Threads number",
                    value=threadNum,
                ),
                BaseOption(
                    name="DontCrawl",
                    required=False,
                    description="Filestypes not to crawl",
                    value=dontCrawl,
                ),
            ]
        )

    def register_social_target(self, url="https://www.darkcode0x00.com.br"):
        self.target_type = "social"
        """adicionar metodo url  para busca de redes sociais """
        self.target_type = "url"
        self.register_options(
            [
                BaseOption(
                    name="url",
                    required=True,
                    description="url para busca de dados  ",
                    value=url,
                ),
            ]
        )

    def register_tcp_target(self, port_value=None, timeout_value=5, threads_value=1):
        """adiciona o os principais metodos
            do modulo nesse caso metodos classico de uma conexão tcp"""
        self.target_type = "tcp"
        self.register_options(
            [
                BaseOption(
                    name="HOST",
                    required=True,
                    description="The IP address to be tested",
                ),
                BaseOption(
                    name="PORT",
                    required=True,
                    description="The port to be tested",
                    value=port_value,
                ),
                BaseOption(
                    name="TIMEOUT",
                    required=True,
                    description="Connection timeout",
                    value=timeout_value,
                ),
                BaseOption(
                    name="THREADS",
                    required=True,
                    description="The number of threads",
                    value=threads_value,
                ),
            ]
        )

    def register_http_target(self, timeout_value=5, threads_value=1):
        """adiciona o os principais metodos do
            modulo nesse caso metodos classico de uma conexão http"""
        self.target_type = "http"
        self.register_options(
            [
                BaseOption(
                    name="URL", required=True, description="The url to be tested"
                ),
                BaseOption(
                    name="TIMEOUT",
                    required=True,
                    description="Connection timeout",
                    value=timeout_value,
                ),
                BaseOption(name="THREADS", required=True, description="The number of threads", value=threads_value),
            ]
        )

    def stager_retry_options(self, threads_value):
        self.target_type = "http"
        self.register_options(
            [
                BaseOption(
                    name="StagerRetryCount", required=True,
                    description="The number of times the stager should retry if the first connect fails", value=10
                ),
                BaseOption(
                    name="StagerRetryWait",
                    required=True,
                    description="Number of seconds to wait for the stager between reconnect attempts",
                    value=5,
                ),
                BaseOption(name="THREADS", required=True, description="The number of threads", value=threads_value),
            ]
        )

    def http_proxy_options(self, threads_value):
        self.target_type = "http"
        self.register_options(
            [
                BaseOption(
                    name="HttpProxyHost", required=True,
                    description="An optional proxy server IP address or hostname", value=''
                ),
                BaseOption(
                    name="HttpProxyPort",
                    required=True,
                    description="An optional proxy server port",
                    value=5,
                ),
                BaseOption(name="HttpProxyUser", required=True, description="An optional proxy server username",
                           value=''),
                BaseOption(name="HttpProxyPass", required=True, description="An optional proxy server password",
                           value=threads_value),
                BaseOption(name="HttpProxyType", required=True, description="The type of HTTP proxy['HTTP', 'SOCKS']",
                           value=threads_value),
            ]
        )

    def http_header_options(self, threads_value):
        self.target_type = "http"
        self.register_options(
            [
                BaseOption(
                    name="HttpHostHeader", required=True,
                    description="An optional value to use for the Host HTTP header", value=0
                ),
                BaseOption(
                    name="HttpCookie",
                    required=True,
                    description="An optional value to use for the Cookie HTTP header",
                    value=5,
                ),
                BaseOption(name="HttpReferer", required=True,
                           description="An optional value to use for the Referer HTTP header", value=threads_value),
            ]
        )

    def update_info(self, info):
        """atualiza as informações dentro de um determinado modulo"""
        for name in info:
            if name in self.info_fields:
                setattr(self, name, info[name])

    def register_options(self, option_array):
        """adiciona infomraçõers dentro de um modulo thg_use"""
        for option in option_array:
            self.options.add_option(option)

    def get_missing_options(self):
        """verifica as opções necessarias em falta dentro de um determinado modulo"""

        def is_missing(option):
            return option.required and option.value in [None, ""]

        missing_options = filter(is_missing, self.options.get_options())
        return list(missing_options)
