import argparse
import time
import platform
import threading
from queue import Queue
from THG.View.Interpreter.cmd2.cmd2 import Cmd, with_category, with_argparser
import base64
import binascii
import numpy
import idna
import quopri
from utils import module
from pathlib import Path
from colorama import Fore, Style
from tabulate import tabulate
from importlib import import_module, reload
from THG.Controller.Database.Database import Database
from THG.Model.BaseXmodeClass.BaseOption import BaseOption
from THG.Model.BaseXmodeClass.ModuleNotUseException import ModuleNotUseException
from utils.utils import *
import unicodedata
from urllib.parse import quote
from utils.base62 import encode as encode62
from utils.base62 import decode as decode62


class ThgInterpreter(Cmd, Database):
    colors = "Always"

    console_prompt = "{COLOR_START}THG{COLOR_END}".format(COLOR_START=Fore.BLUE,
                                                          COLOR_END=Fore.YELLOW
                                                          )
    console_prompt_end = " > "
    module_name = None
    module_class = None
    module_instance = None
    __version__ = 1.0
    # command categories
    CMD_CORE = "Core Command"
    CMD_MODULE = "Module Command"
    Data_format   = "Data-format"
    Encryption_encoding="Encryption_encoding"
    Public_key="Public_key"
    Arithmetic_Logic="Arithmetic_Logic"
    Networking="Networking"
    Language="Language"
    utils="utils"
    data_time="data_time"
    extractors="extractors"
    compression="compression"
    hashing="hashing"
    codetidy="codetidy"
    forensics="forensics"
    multmidia="multmidia"
    othres="othres"
    flow="flow"
    control="control"
########################
    def __init__(self):
        super(ThgInterpreter, self).__init__()
        Database.__init__(self)
        self.prompt = self.console_prompt + self.console_prompt_end

        self.thg_banner(None)

    @with_category(CMD_CORE)
    def thg_banner(self, args):
        """Print THG banner"""
        self.poutput("\n\n")
        self.poutput("""
{CYAN}==================={GREEN}[ thgconsole {version}-dev ]{GREEN}{CYAN}======================

        {YELLOW}+ -- --=[{RED}THGEF   :{MAGENTA} The Hacker Group Exploitation Framework{RED}{YELLOW} ]=-- -- +
        {YELLOW}+ -- --=[{RED}Code by :{MAGENTA} Darkcode                               {RED}{YELLOW} ]=-- -- +
        {YELLOW}+ -- --=[{RED}Codename:{MAGENTA} FlagXpwn                               {RED}{YELLOW} ]=-- -- +
        {YELLOW}+ -- --=[{RED}Homepage:{MAGENTA} https://darkcode0x00.com.br/category/thg/ {RED}{YELLOW} ]=-- -- +
        {YELLOW}+ -- --=[{RED}youtube :{MAGENTA} https://www.youtube.com/channel/UC4d_mJv4uhppA-hCdFODWJw{RED}{YELLOW}]=-- -- + 

{CYAN}==================={GREEN}[ thgconsole-info ]{GREEN}{CYAN}=============================

        {YELLOW}+ -- --=[{RED} - exploits        - payloads    {RED}{YELLOW}]=-- -- +
        {YELLOW}+ -- --=[{RED} - auxiliary       - post        {RED}{YELLOW}]=-- -- +
        {YELLOW}+ -- --=[{RED} - encoders        - nops        {RED}{YELLOW}]=-- -- +
        {YELLOW}+ -- --=[{RED} - evasion         - extra       {RED}{YELLOW}]=-- -- +
        {YELLOW}+ -- --=[{RED}          - total {count}              {RED}{YELLOW}]=-- -- +

{CYAN}==================={GREEN}[ thgconsole-pc ]{GREEN}{CYAN}===============================

        {YELLOW}+ -- --=[{RED}system  =>{MAGENTA} {os}             {RED}{YELLOW}]=-- -- +
        {YELLOW}+ -- --=[{RED}machine =>{MAGENTA} {machine}            {RED}{YELLOW}]=-- -- +



{CYAN}==================={GREEN}[ thgconsole-config ]{GREEN}{CYAN}===========================
        {YELLOW}+ -- --=[{RED}DB_STATUS =>{MAGENTA} on              {RED}{YELLOW}]=-- -- +



        """.format(count=self.get_module_count(), red=Fore.RED,
                   CYAN=Fore.CYAN,
                   GREEN=Fore.GREEN,
                   RED=Fore.RED,
                   YELLOW=Fore.YELLOW,
                   MAGENTA=Fore.MAGENTA,
                   os=platform.uname()[0],
                   machine=platform.uname()[4],
                   version=self.__version__))

    @with_category(CMD_MODULE)
    def thg_list(self, args):
        """List all modules"""
        local_modules = module.get_local_modules()
        self._print_modules(local_modules, "Module List:")

    @with_category(CMD_MODULE)
    def thg_search(self, args):
        """
        Search modules

        Support fields:
            name, module_name, description, author, disclosure_date, service_name, service_version, check
        Eg:
            search redis
            search service_name=phpcms  service_version=9.6.0
        """
        search_conditions = args.split(" ")
        db_conditions = {}
        for condition in search_conditions:
            cd = condition.split("=")
            if len(cd) == 1:
                [module_name] = cd
                db_conditions['module_name'] = module_name
            else:
                [field, value] = cd
                if field in self.searchable_fields:
                    db_conditions[field] = value

        modules = self.search_modules(db_conditions)

        self._print_modules(modules, 'Search results:')
        self._print_item("The search is only retrieved from the database")
        self._print_item(
            "If you add/delete some new modules, please execute `db_rebuild` first\n\n")

    def complete_set(self, text, line, begidx, endidx):
        if len(line.split(" ")) > 2:
            completion_items = []
        else:
            completion_items = ['debug']
            if self.module_instance:
                completion_items += [
                    option.name for option in self.module_instance.options.get_options()]
        return self.basic_complete(text, line, begidx, endidx, completion_items)

    set_parser = argparse.ArgumentParser()
    set_parser.add_argument(
        "name", help="The name of the field you want to set")
    set_parser.add_argument(
        "-f", "--file", action="store_true", help="Specify multiple targets")
    set_parser.add_argument(
        "value", help="The value of the field you want to set")
#############
    @with_category(Data_format)
    def thg_dump(self,args):
        arg = args.split(" ")
        if arg[0] == "":
            print("dump mod[hex,hex_file] tab[int]\ndump hex string\ndump hex_file file")
        elif arg[0] == "hex":
            if arg[1] == "help":
                print("""{YELLOW}hex{YELLOW}{BLUE} =>{BLUE}{RED} text for hex.""".format(
                    YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED))
            else:
                print(hexdump(src=arg[1],length=int(arg[2])))
        elif arg[0] == "hex_file":
            if arg[1] == "help":
                print("""{YELLOW}hex_file{YELLOW}{BLUE} =>{BLUE}{RED} file for hex.""".format(
                    YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED))
            else:
                try:
                    with (open(arg[1], 'br')) as file:
                        data = file.read()
                        hexdump_file(data)
                except FileNotFoundError:
                    print("esse comando requer um arquivo e não uma string")



#############

################################### thg_encode thg_decode
    @with_category(Data_format)
    def thg_encode(self, args):
        """modulo referente a encode de estrings"""
        arg_mensage = args.split(" ")
        if arg_mensage[0] == "":
            print("""suporte encode:

Este módulo fornece funções para codificar dados binários em caracteres ASCII 
imprimíveis e decodificar essas codificações de volta para dados binários.
Ele fornece funções de codificação e decodificação para as codificações 
especificadas em RFC 3548 ,que define os algoritmos Base16, Base32 e Base64,
e para as codificações Ascii85 e Base85 padrão de fato.

a2b_uu
b2a_uu
a2b_base64
b2a_base64
a2b_qp
b2a_qp
a2b_hqx
rledecode_hqx
rlecode_hqx
b2a_hqx
crc_hqx
crc32
b2a_hex
a2b_hex
hexlify
unhexlify
Charcode
binary
base62
basen
bcd
ur
unicode_normalize
qp_encoding
        encode type[2,16,32,64]  str
        
        """.format(YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED))

        elif arg_mensage[0] == "64":
            arg_mensage[1] = arg_mensage[1].encode('ascii')
            base64_bytes = base64.b64encode(arg_mensage[1])
            by_to_st(base64_bytes)
        elif arg_mensage[0] == "32":
            arg_mensage[1] = arg_mensage[1].encode('ascii')
            b32encode_bytes = base64.b32encode(arg_mensage[1])
            by_to_st(b32encode_bytes)
        elif arg_mensage[0] == "16":
            arg_mensage[1] = arg_mensage[1].encode('ascii')
            b16encode_bytes = base64.b16encode(arg_mensage[1])
            by_to_st(b16encode_bytes)
        elif arg_mensage[0] == "a85encode":
            arg_mensage[1] = arg_mensage[1].encode('ascii')
            a85encode_bytes = base64.a85encode(arg_mensage[1])
            by_to_st(a85encode_bytes)
        elif arg_mensage[0] == "b85encode":
            arg_mensage[1] = arg_mensage[1].encode('ascii')
            b85encode_bytes = base64.b85encode(arg_mensage[1])
            by_to_st(b85encode_bytes)
        elif arg_mensage[0] == "a2b_uu":
            if arg_mensage[1] == "help":
                print("""{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED} Converta uma única linha de dados uuencodificados de volta em binários e retorne os dados binários. As linhas normalmente contêm 45 bytes (binários), exceto a última linha. Os dados da linha podem ser seguidos de espaços em branco.""".format(
                    YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED))
            else:
                by_to_st((binascii.a2b_uu(arg_mensage[1])))
        elif arg_mensage[0] == "a2b_base64":
            if arg_mensage[1] == "help":
                print("""{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED}Converta dados binários em uma linha de caracteres ASCII na codificação base64. O valor de retorno é a linha convertida, incluindo um caractere de nova linha. O comprimento dos dados deve ser de no máximo 57 para aderir ao padrão base64.""".format(
                    YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED))
            else:
                by_to_st(binascii.a2b_base64(arg_mensage[1]))
        elif arg_mensage[0] == "b2a_base64":
            if arg_mensage[1] == "help":
                print("""{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED} Converta dados binários em uma linha de caracteres ASCII na codificação base64. O valor de retorno é a linha convertida, incluindo um caractere de nova linha. O comprimento dos dados deve ser de no máximo 57 para aderir ao padrão base64.""".format(
                    YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED))
            else:
                by_to_st(binascii.b2a_base64(b'arg_mensage[1]'))
        elif arg_mensage[0] == "a2b_qp":
            if arg_mensage[1] == "help":
                print("""{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED}Converta um bloco de dados imprimíveis entre aspas de volta em binários e retorne os dados binários. Mais de uma linha pode ser passada por vez. Se o cabeçalho do argumento opcional estiver presente e verdadeiro, os sublinhados serão decodificados como espaços.""".format(
                    YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED))
            else:
                by_to_st(binascii.a2b_qp(arg_mensage[1]))
        elif arg_mensage[0] == "b2a_qp":
            if arg_mensage[1] == "help":
                print("""{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED}Converta dados binários em uma (s) linha (s) de caracteres ASCII em codificação imprimível entre aspas. O valor de retorno é a (s) linha (s) convertida (s). Se o argumento opcional quotetabs estiver presente e verdadeiro, todas as tabulações e espaços serão codificados. Se o argumento opcional istext estiver presente e verdadeiro, as novas linhas não serão codificadas, mas os espaços em branco finais serão codificados. Se o cabeçalho do argumento opcional estiver presente e verdadeiro, os espaços serão codificados como sublinhados de acordo com RFC1522. Se o cabeçalho do argumento opcional estiver presente e for falso, os caracteres de nova linha também serão codificados; caso contrário, a conversão de alimentação de linha pode corromper o fluxo de dados binários.""".format(YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED))
            else:
                by_to_st(binascii.a2b_qp(arg_mensage[1].encode()))
        elif arg_mensage[0] == "a2b_hqx":
            if arg_mensage[1] == "help":
                print("""{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED}Converta dados ASCII formatados de binhex4 em binários, sem fazer a descompressão RLE. A string deve conter um número completo de bytes binários ou (no caso da última parte dos dados binhex4) ter os bits restantes zero.
""".format(YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED))
            else:
                by_to_st(binascii.a2b_hqx(arg_mensage[1]))
        elif arg_mensage[0] == "rledecode_hqx":
            if arg_mensage[1] == "help":
                print("""{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED} Execute a descompressão RLE nos dados, de acordo com o padrão binhex4. O algoritmo usa 0x90 após um byte como um indicador de repetição, seguido por uma contagem. Uma contagem de 0 especifica um valor de byte de 0x90 . A rotina retorna os dados descompactados, a menos que os dados de entrada de dados terminem em um indicador de repetição órfão, caso em que a exceção Incompleta é levantada.""".format(YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED))
            else:
                by_to_st((binascii.rledecode_hqx(arg_mensage[1].encode())))
        elif arg_mensage[0] == "rlecode_hqx":
            if arg_mensage[1] == "help":
                print("""{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED} Execute a compactação RLE no estilo binhex4 nos dados e retorne o resultado.""".format(
                    YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED))
            else:
                by_to_st((binascii.rlecode_hqx(arg_mensage[1].encode())))
        elif arg_mensage[0] == "b2a_hqx":
            if arg_mensage[1] == "help":
                print("""{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED} Execute a conversão hexbin4 binário para ASCII e retorne a string resultante. O argumento já deve ser codificado por RLE e ter um comprimento divisível por 3 (exceto possivelmente o último fragmento).
""".format(YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED))
            else:
                by_to_st((binascii.b2a_hqx(arg_mensage[1].encode())))
        elif arg_mensage[0] == "crc_hqx":
            if arg_mensage[1] == "help":
                print("""{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED} Calcule o valor binhex4 crc dos dados , começando com um crc inicial e retornando o resultado.
""".format(YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED))
            else:
                by_to_st(
                    (binascii.crc_hqx(arg_mensage[1].encode(), int(arg_mensage[2]))))
        elif arg_mensage[0] == "crc32":
            if arg_mensage[1] == "help":
                print("""{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED} Calcule CRC-32, a soma de verificação de dados de 32 bits, começando com um crc inicial. Isso é consistente com a soma de verificação do arquivo ZIP. Uma vez que o algoritmo é projetado para uso como um algoritmo de soma de verificação, não é adequado para uso como um algoritmo de hash geral.

{YELLOW}Nota{YELLOW}{RED} Para gerar o mesmo valor numérico em todas as versões e plataformas Python, {RED}{BLUE}use crc32 (dados) & 0xffffffff{BLUE}{RED}. Se você estiver usando apenas a soma de verificação no formato binário compactado, isso não é necessário, pois o valor de retorno é a representação binária correta de 32 bits, independentemente do sinal.
        """.format(YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED))
            else:
                by_to_st((binascii.crc32(arg_mensage[1].encode())))
        elif arg_mensage[0] == "hexlify":
            if arg_mensage[1] == "help":
                print("""{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED} Retorna a representação hexadecimal dos dados binários . Cada byte de dados é convertido na representação hexadecimal de 2 dígitos correspondente. A string resultante é, portanto, o dobro do comprimento dos dados .

        """.format(YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED))
            else:
                by_to_st(
                    (binascii.hexlify(arg_mensage[1].encode(), arg_mensage[2].encode())))
        elif arg_mensage[0] == "b2a_hex":
            if arg_mensage[1] == "help":
                print("""{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED} hex
        """.format(YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED))
            else:
                by_to_st(
                    (binascii.b2a_hex(arg_mensage[1].encode(), int(arg_mensage[2]))))
        elif arg_mensage[0] == "unhexlify":
            if arg_mensage[1] == "help":
                print("""{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED} Retorna os dados binários representados pela string hexadecimal hexstr . Esta função é o inverso de b2a_hex () . hexstr deve conter um número par de dígitos hexadecimais (que podem ser maiúsculas ou minúsculas), caso contrário, um TypeError é gerado.

        """.format(YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED))
            else:
                by_to_st((binascii.unhexlify(arg_mensage[1].encode())))
        elif arg_mensage[0] == "b2a_uu":
            if arg_mensage[1] == "help":
                print("""{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED} Converta dados binários em uma linha de caracteres ASCII, o valor de retorno é a linha convertida, incluindo um caractere de nova linha. O comprimento dos dados deve ser de no máximo 45.

        """.format(YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED))
            else:
                by_to_st(
                    (binascii.b2a_uu(arg_mensage[1].encode(), int(arg_mensage[2]))))
        elif arg_mensage[0] == "charcode":
            if arg_mensage[1] == "help":
                print("""{YELLOW}charcode{YELLOW}{BLUE} =>{BLUE}{RED}converte string em charcode
        """.format(YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED))
            else:
                print(ord(arg_mensage[1].encode()))
        elif arg_mensage[0] == "binary":
            if arg_mensage[1] == "help":
                print("""{YELLOW}binary{YELLOW}{BLUE} =>{BLUE}{RED}converte string em binary
        """.format(YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED))
            else:
                print(' '.join(format(ord(x), 'b') for x in arg_mensage[1]))
        elif arg_mensage[0] == "base62":
            if arg_mensage[1] == "help":
                print("""{YELLOW}base62{YELLOW}{BLUE} =>{BLUE}{RED}converte string em base62
        """.format(YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED))
            else:
                 print(decode62(arg_mensage[1]))
        elif arg_mensage[0] == "basen":
            if arg_mensage[1] == "help":
                print("""{YELLOW}basen{YELLOW}{BLUE} =>{BLUE}{RED}converte decimal em basen
        """.format(YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED))
            else:
                 print(numpy.base_repr(int(arg_mensage[1]), base=int(arg_mensage[2])))
        elif arg_mensage[0] == "url":
            try:
                if arg_mensage[1] =="help":
                    print("""{YELLOW}url_encode{YELLOW}{BLUE} =>{BLUE}{RED}encode personalidado para url\nencode url_encode safa[] encoding""".format(YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED))
                else:
                     print(quote(arg_mensage[1],safe=arg_mensage[2],encoding=arg_mensage[3]))
            except IndexError:
                print("digite a sintaxe correta\nncode url_encode safa[] encoding\n ou use o comando help")
        elif arg_mensage[0] == "unicode_normalize":
            try:
                if arg_mensage[1] =="help":
                    print("""{YELLOW}unicode_normalize{YELLOW}{BLUE} =>{BLUE}{RED}Transforme caracteres Unicode em uma das formas de normalização['NFC', 'NFKC', 'NFD','NFKD']\n                   
{YELLOW}NFD{YELLOW}{BLUE} =>{BLUE}{RED}Normalisation Form Canonical Decomposition
{YELLOW}NFC{YELLOW}{BLUE} =>{BLUE}{RED}Normalisation Form Canonical Composition
{YELLOW}NFKD{YELLOW}{BLUE} =>{BLUE}{RED}Normalisation Form Compatibility Decomposition
{YELLOW}NFKC{YELLOW}{BLUE} =>{BLUE}{RED}Normalisation Form Compatibility Composition    
encode unicode_normalize str encoding['NFC', 'NFKC', 'NFD','NFKD']\n""".format(YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED))
                else:
                     print(unicodedata.normalize(arg_mensage[1],arg_mensage[2]))
            except IndexError:
                print("digite a sintaxe correta\nncode url_encode safa[] encoding\n ou use o comando help")
        elif arg_mensage[0] == "qp_encoding":
            try:
                if arg_mensage[1] =="help":
                    print("""{YELLOW}qp_encoding{YELLOW}{BLUE} =>{BLUE}{RED}
                    Quoted-Printable, ou QP encoding, 
                    é uma codificação que usa caracteres ASCII imprimíveis (alfanuméricos e o sinal de igual '=') 
                    para transmitir dados de 8 bits em um caminho de dados de 7 bits ou, geralmente, em um meio que não é 8- um pouco limpo. 
                    É definido como uma codificação de transferência de conteúdo MIME para uso em e-mail.
                    QP funciona usando o sinal de igual '=' como um caractere de escape. Ele também limita o comprimento da linha a 76, pois alguns softwares têm limites no comprimento da linha\nencode qp_encoding TXT encode""".format(YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED))
                else:
                    encoded = quopri.encodestring(arg_mensage[1].encode(arg_mensage[2]))
                    print(encoded.decode())
            except IndexError:
                print("digite a sintaxe correta\nencode qp_encoding é utf-16\n ou use o comando help")
        elif arg_mensage[0] == "idna":
            try:
                if arg_mensage[1] =="help":
                    print("""{YELLOW}idna{YELLOW}{BLUE} =>{BLUE}{RED}encode personalidado para url\nencode url_encode safa[] encoding""".format(YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED))
                else:
                     print (idna.encode(arg_mensage[1]).decode(arg_mensage[2]))
            except IndexError:
                print("digite a sintaxe correta\nncode idna string encoding\n ou use o comando help")

        else:
            pass
        try:
            pass

        except IndexError:
            print("verificar a saida")

#####################################
    @with_argparser(set_parser)
    @with_category(CMD_MODULE)
    def thg_set(self, args):
        """Set module option value/ set program config"""
        if args.name == 'debug':
            self.debug = args.value
            return None

        if not self.module_instance:
            raise ModuleNotUseException()

        if args.file and args.name in ["HOST", "URL"]:
            try:
                open(args.value, 'r')
                self.module_instance.multi_target = True
            except IOError as e:
                self._print_item(e, color=Fore.RED)
                return False
        elif not args.file and args.name in ["HOST", "URL"]:
            self.module_instance.multi_target = False
            self.module_instance.targets = None

        self.module_instance.options.set_option(args.name, args.value)

    def complete_use(self, text, line, begidx, endidx):
        if len(line.split(" ")) > 2:
            modules = []
        else:
            modules = [local_module[0]
                       for local_module in module.get_local_modules()]
        return self.basic_complete(text, line, begidx, endidx, modules)

    @with_category(CMD_MODULE)
    def thg_use(self, module_name, module_reload=False):
        """Chose a module"""
        module_file = module.name_convert(module_name)
        module_type = module_name.split("/")[0]

        if Path(module_file).is_file():
            self.module_name = module_name
            if module_reload:
                self.module_class = reload(self.module_class)
            else:
                self.module_class = import_module("modules.{module_name}".format(
                    module_name=module_name.replace("/", ".")))
            self.module_instance = self.module_class.Exploit()
            self.set_prompt(module_type=module_type, module_name=module_name)
        else:
            self.poutput("Module/Exploit not found.")

    @with_category(CMD_MODULE)
    def thg_back(self, args):
        """Clear module that chose"""
        self.module_name = None
        self.module_instance = None
        self.prompt = self.console_prompt + self.console_prompt_end

    def complete_show(self, text, line, begidx, endidx):
        if len(line.split(" ")) > 2:
            completion_items = []
        else:
            completion_items = ['info', 'options', 'missing']
        return self.basic_complete(text, line, begidx, endidx, completion_items)

    @with_category(CMD_MODULE)
    def thg_show(self, content):
        """
        Display module information

        Eg:
            show info
            show options
            show missing
        """
        if not self.module_instance:
            raise ModuleNotUseException()

        if content == "info":
            info = self.module_instance.get_info()
            info_table = []
            self.poutput("Module info:")
            for item in info.keys():
                info_table.append([item + ":", info.get(item)])
            self.poutput(
                tabulate(info_table, colalign=("right",), tablefmt="plain"))

        if content == "options" or content == "info":
            options = self.module_instance.options.get_options()
            default_options_instance = BaseOption()
            options_table = []
            for option in options:
                options_table_row = []
                for field in default_options_instance.__dict__.keys():
                    options_table_row.append(getattr(option, field))
                options_table.append(options_table_row)

            self.poutput("Module options:")
            self.poutput(
                tabulate(
                    options_table,
                    headers=default_options_instance.__dict__.keys(),
                )
            )

        if content == "missing":
            missing_options = self.module_instance.get_missing_options()
            if len(missing_options) == 0:
                self.poutput("No option missing!")
                return None

            default_options_instance = BaseOption()
            missing_options_table = []
            for option in missing_options:
                options_table_row = []
                for field in default_options_instance.__dict__.keys():
                    options_table_row.append(getattr(option, field))
                missing_options_table.append(options_table_row)
            self.poutput("Missing Module options:")
            self.poutput(
                tabulate(
                    missing_options_table,
                    headers=default_options_instance.__dict__.keys(),
                )
            )

    @with_category(CMD_MODULE)
    def thg_run(self, args):
        """alias to exploit"""
        self.thg_exploit(args=args)

    def exploit_thread(self, target, target_type, thread_queue):
        target_field = None
        port = None

        if target_type == "tcp":
            [target, port] = module.parse_ip_port(target)
            target_field = "HOST"
        elif target_type == "http":
            target_field = "URL"
        exp = self.module_class.Exploit()
        exp.options.set_option(target_field, target)
        exp.options.set_option(
            "TIMEOUT", self.module_instance.options.get_option("TIMEOUT"))
        if port:
            exp.options.set_option("PORT", port)
        else:
            exp.options.set_option(
                "PORT", self.module_instance.options.get_option("PORT"))

        exploit_result = exp.exploit()

        if exploit_result.status:
            self._print_item(exploit_result.success_message)
        else:
            self._print_item(exploit_result.error_message, color=Fore.RED)
        thread_queue.get(1)

    @with_category(CMD_MODULE)
    def thg_exploit(self, args):
        """Execute module exploit"""
        if not self.module_instance:
            raise ModuleNotUseException()

        [validate_result, validate_message] = self.module_instance.options.validate()
        if not validate_result:
            for error in validate_message:
                self._print_item(error, color=Fore.RED)
            return False

        if self.module_instance.multi_target:
            target_type = self.module_instance.target_type
            target_field = None

            if target_type == "tcp":
                target_field = "HOST"
            elif target_type == "http":
                target_field = "URL"

            target_filename = self.module_instance.options.get_option(
                target_field)

            try:
                target_file = open(target_filename, 'r')
                self.module_instance.targets = []
                for line in target_file.readlines():
                    self.module_instance.targets.append(line.strip())
                self.module_instance.multi_target = True
            except IOError as e:
                self._print_item(e, color=Fore.RED)
                return False

            targets = self.module_instance.targets
            targets_queue = Queue()
            for target in targets:
                targets_queue.put(target)

            if not targets_queue.empty():
                thread_count = int(
                    self.module_instance.options.get_option("THREADS"))
                thread_queue = Queue(maxsize=thread_count)

                try:
                    while not targets_queue.empty():
                        while thread_queue.full():
                            time.sleep(0.1)

                        target = targets_queue.get()
                        thread_queue.put(1)
                        _thread = threading.Thread(target=self.exploit_thread, args=(
                            target, target_type, thread_queue))
                        _thread.start()

                    while not thread_queue.empty():
                        time.sleep(0.1)
                except KeyboardInterrupt:
                    self._print_item(
                        "Wait for existing process to exit...", color=Fore.RED)
                    while threading.activeCount() > 1:
                        time.sleep(0.5)
                    return None

            self.poutput("{style}[*]{style_end} module execution completed".format(
                style=Fore.BLUE + Style.BRIGHT,
                style_end=Style.RESET_ALL
            ))
            return False

        exploit_result = self.module_instance.exploit()
        if exploit_result.status:
            self._print_item("Exploit success!")
            self._print_item(exploit_result.success_message)
        else:
            self._print_item("Exploit failure!", color=Fore.RED)
            self._print_item(exploit_result.error_message, color=Fore.RED)
        self.poutput("{style}[*]{style_end} module execution completed".format(
            style=Fore.BLUE + Style.BRIGHT,
            style_end=Style.RESET_ALL
        ))

    def check_thread(self, target, target_type, thread_queue):
        target_field = None
        port = None

        if target_type == "tcp":
            [target, port] = module.parse_ip_port(target)
            target_field = "HOST"
        elif target_type == "http":
            target_field = "URL"
        exp = self.module_class.Exploit()
        exp.options.set_option(target_field, target)
        exp.options.set_option(
            "TIMEOUT", self.module_instance.options.get_option("TIMEOUT"))
        if port:
            exp.options.set_option("PORT", port)
        else:
            exp.options.set_option(
                "PORT", self.module_instance.options.get_option("PORT"))

        exploit_result = exp.check()

        if exploit_result.status:
            self._print_item(exploit_result.success_message)
        else:
            self._print_item(exploit_result.error_message, color=Fore.RED)
        thread_queue.get(1)

    @with_category(CMD_MODULE)
    def thg_check(self, args):
        """Execute module check"""
        if not self.module_instance:
            raise ModuleNotUseException()

        [validate_result, validate_message] = self.module_instance.options.validate()
        if not validate_result:
            for error in validate_message:
                self._print_item(error, Fore.RED)
            return False

        if self.module_instance.multi_target:

            target_type = self.module_instance.target_type
            target_field = None

            if target_type == "tcp":
                target_field = "HOST"
            elif target_type == "http":
                target_field = "URL"

            target_filename = self.module_instance.options.get_option(
                target_field)

            try:
                target_file = open(target_filename, 'r')
                self.module_instance.targets = []
                for line in target_file.readlines():
                    self.module_instance.targets.append(line.strip())
                self.module_instance.multi_target = True
            except IOError as e:
                self._print_item(e, color=Fore.RED)
                return False

            targets = self.module_instance.targets
            targets_queue = Queue()
            for target in targets:
                targets_queue.put(target)

            if not targets_queue.empty():
                thread_count = int(
                    self.module_instance.options.get_option("THREADS"))
                thread_queue = Queue(maxsize=thread_count)

                try:
                    while not targets_queue.empty():
                        while thread_queue.full():
                            time.sleep(0.1)

                        target = targets_queue.get()
                        thread_queue.put(1)
                        _thread = threading.Thread(target=self.check_thread,
                                                   args=(target, target_type, thread_queue))
                        _thread.start()

                    while not thread_queue.empty():
                        time.sleep(0.1)
                except KeyboardInterrupt:
                    self._print_item(
                        "Wait for existing process to exit...", color=Fore.RED)
                    while threading.activeCount() > 1:
                        time.sleep(0.5)
                    return None

            self.poutput("{style}[*]{style_end} module execution completed".format(
                style=Fore.BLUE + Style.BRIGHT,
                style_end=Style.RESET_ALL
            ))
            return None

        exploit_result = self.module_instance.check()

        if exploit_result is None:
            self._print_item("Check Error: check function no results returned")
            return None

        if exploit_result.status:
            self._print_item("Check success!")
            self._print_item(exploit_result.success_message)
        else:
            self._print_item("Exploit failure!", color=Fore.RED)
            self._print_item(exploit_result.error_message, color=Fore.RED)
        self.poutput("{style}[*]{style_end} module execution completed".format(
            style=Fore.BLUE + Style.BRIGHT,
            style_end=Style.RESET_ALL
        ))

    @with_category(CMD_CORE)
    def thg_db_rebuild(self, args):
        """Rebuild database for search"""
        self.db_rebuild()
        self.poutput("Database rebuild done.")

    @with_category(CMD_MODULE)
    def thg_reload(self, args):
        """reload the chose module"""
        self.thg_use(self.module_name, module_reload=True)

    def set_prompt(self, module_type, module_name):
        module_prompt = " {module_type}({color}{module_name}{color_end})".format(
            module_type=module_type,
            module_name=module_name.replace(module_type + "/", ""),
            color=Fore.RED,
            color_end=Fore.RESET
        )
        self.prompt = self.console_prompt + module_prompt + self.console_prompt_end

    def _print_modules(self, modules, title):
        self.poutput(title)
        self.poutput(tabulate(modules, headers=(
            'module_name', 'check', 'disclosure_date', 'description')))

    def _print_item(self, message, color=Fore.YELLOW):
        self.poutput("{style}[+]{style_end} {message}".format(
            style=color + Style.BRIGHT,
            style_end=Style.RESET_ALL,
            message=message,
        ))
