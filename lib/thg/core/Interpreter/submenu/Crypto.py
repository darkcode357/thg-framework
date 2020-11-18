import base64
import binascii
import quopri
import sys
import unicodedata

import idna
import numpy
from IPython import embed
from lib.thg.core.Interpreter.thgcmd import Cmd
from colorama import Fore
from lib.thg.core.Interpreter.thgcmd.thgcmd import Cmd, with_category, with_argparser
from lib.thg.core.constants import *
from utils.utils import by_to_st, hexdump, hexdump_file
from urllib.parse import quote
from utils.base62 import decode as decode62


class CryptoLevel(Cmd):
    colors = "Always"
    console_prompt = "{COLOR_START}Crypto{COLOR_END}".format(
        COLOR_START=Fore.BLUE, COLOR_END=Fore.RED
    )
    doc_header = " Crypto COMMAND HELP"
    doc_leader = ""
    intro = None
    lastcmd = ""
    misc_header = "Miscellaneous help topics:"
    nohelp = "*** No help on %s"
    ruler = "="
    undoc_header = "Undocumented commands:"
    console_prompt_end = ">"
    module_name = None
    module_class = None
    module_instance = None
    __Menu__version__ = 1.0
    """To be used as a Crypto level command class. """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.top_level_attr = None
        self.second_level_attr = 987654321
        self.prompt = self.console_prompt + self.console_prompt_end

        @with_category(Data_format)
        def thg_encode(self, args):
            """modulo referente a encode de estrings"""
            arg_mensage = args.split(" ")
            if arg_mensage[0] == "":
                print(
                    """suporte encode:

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

            """.format(
                        YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                    )
                )

            elif arg_mensage[0] == "64":
                arg_mensage[1] = arg_mensage[1].encode("ascii")
                base64_bytes = base64.b64encode(arg_mensage[1])
                by_to_st(base64_bytes)
            elif arg_mensage[0] == "32":
                arg_mensage[1] = arg_mensage[1].encode("ascii")
                b32encode_bytes = base64.b32encode(arg_mensage[1])
                by_to_st(b32encode_bytes)
            elif arg_mensage[0] == "16":
                arg_mensage[1] = arg_mensage[1].encode("ascii")
                b16encode_bytes = base64.b16encode(arg_mensage[1])
                by_to_st(b16encode_bytes)
            elif arg_mensage[0] == "a85encode":
                arg_mensage[1] = arg_mensage[1].encode("ascii")
                a85encode_bytes = base64.a85encode(arg_mensage[1])
                by_to_st(a85encode_bytes)
            elif arg_mensage[0] == "b85encode":
                arg_mensage[1] = arg_mensage[1].encode("ascii")
                b85encode_bytes = base64.b85encode(arg_mensage[1])
                by_to_st(b85encode_bytes)
            elif arg_mensage[0] == "a2b_uu":
                if arg_mensage[1] == "help":
                    print(
                        """{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED} Converta uma única linha de dados uuencodificados de volta em binários e retorne os dados binários. As linhas normalmente contêm 45 bytes (binários), exceto a última linha. Os dados da linha podem ser seguidos de espaços em branco.""".format(
                            YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                        )
                    )
                else:
                    by_to_st((binascii.a2b_uu(arg_mensage[1])))
            elif arg_mensage[0] == "a2b_base64":
                if arg_mensage[1] == "help":
                    print(
                        """{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED}Converta dados binários em uma linha de caracteres ASCII na codificação base64. O valor de retorno é a linha convertida, incluindo um caractere de nova linha. O comprimento dos dados deve ser de no máximo 57 para aderir ao padrão base64.""".format(
                            YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                        )
                    )
                else:
                    by_to_st(binascii.a2b_base64(arg_mensage[1]))
            elif arg_mensage[0] == "b2a_base64":
                if arg_mensage[1] == "help":
                    print(
                        """{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED} Converta dados binários em uma linha de caracteres ASCII na codificação base64. O valor de retorno é a linha convertida, incluindo um caractere de nova linha. O comprimento dos dados deve ser de no máximo 57 para aderir ao padrão base64.""".format(
                            YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                        )
                    )
                else:
                    by_to_st(binascii.b2a_base64(b"arg_mensage[1]"))
            elif arg_mensage[0] == "a2b_qp":
                if arg_mensage[1] == "help":
                    print(
                        """{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED}Converta um bloco de dados imprimíveis entre aspas de volta em binários e retorne os dados binários. Mais de uma linha pode ser passada por vez. Se o cabeçalho do argumento opcional estiver presente e verdadeiro, os sublinhados serão decodificados como espaços.""".format(
                            YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                        )
                    )
                else:
                    by_to_st(binascii.a2b_qp(arg_mensage[1]))
            elif arg_mensage[0] == "b2a_qp":
                if arg_mensage[1] == "help":
                    print(
                        """{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED}Converta dados binários em uma (s) linha (s) de caracteres ASCII em codificação imprimível entre aspas. O valor de retorno é a (s) linha (s) convertida (s). Se o argumento opcional quotetabs estiver presente e verdadeiro, todas as tabulações e espaços serão codificados. Se o argumento opcional istext estiver presente e verdadeiro, as novas linhas não serão codificadas, mas os espaços em branco finais serão codificados. Se o cabeçalho do argumento opcional estiver presente e verdadeiro, os espaços serão codificados como sublinhados de acordo com RFC1522. Se o cabeçalho do argumento opcional estiver presente e for falso, os caracteres de nova linha também serão codificados; caso contrário, a conversão de alimentação de linha pode corromper o fluxo de dados binários.""".format(
                            YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                        )
                    )
                else:
                    by_to_st(binascii.a2b_qp(arg_mensage[1].encode()))
            elif arg_mensage[0] == "a2b_hqx":
                if arg_mensage[1] == "help":
                    print(
                        """{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED}Converta dados ASCII formatados de binhex4 em binários, sem fazer a descompressão RLE. A string deve conter um número completo de bytes binários ou (no caso da última parte dos dados binhex4) ter os bits restantes zero.
    """.format(
                            YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                        )
                    )
                else:
                    by_to_st(binascii.a2b_hqx(arg_mensage[1]))
            elif arg_mensage[0] == "rledecode_hqx":
                if arg_mensage[1] == "help":
                    print(
                        """{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED} Execute a descompressão RLE nos dados, de acordo com o padrão binhex4. O algoritmo usa 0x90 após um byte como um indicador de repetição, seguido por uma contagem. Uma contagem de 0 especifica um valor de byte de 0x90 . A rotina retorna os dados descompactados, a menos que os dados de entrada de dados terminem em um indicador de repetição órfão, caso em que a exceção Incompleta é levantada.""".format(
                            YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                        )
                    )
                else:
                    by_to_st((binascii.rledecode_hqx(arg_mensage[1].encode())))
            elif arg_mensage[0] == "rlecode_hqx":
                if arg_mensage[1] == "help":
                    print(
                        """{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED} Execute a compactação RLE no estilo binhex4 nos dados e retorne o resultado.""".format(
                            YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                        )
                    )
                else:
                    by_to_st((binascii.rlecode_hqx(arg_mensage[1].encode())))
            elif arg_mensage[0] == "b2a_hqx":
                if arg_mensage[1] == "help":
                    print(
                        """{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED} Execute a conversão hexbin4 binário para ASCII e retorne a string resultante. O argumento já deve ser codificado por RLE e ter um comprimento divisível por 3 (exceto possivelmente o último fragmento).
    """.format(
                            YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                        )
                    )
                else:
                    by_to_st((binascii.b2a_hqx(arg_mensage[1].encode())))
            elif arg_mensage[0] == "crc_hqx":
                if arg_mensage[1] == "help":
                    print(
                        """{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED} Calcule o valor binhex4 crc dos dados , começando com um crc inicial e retornando o resultado.
    """.format(
                            YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                        )
                    )
                else:
                    by_to_st(
                        (binascii.crc_hqx(arg_mensage[1].encode(), int(arg_mensage[2])))
                    )
            elif arg_mensage[0] == "crc32":
                if arg_mensage[1] == "help":
                    print(
                        """{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED} Calcule CRC-32, a soma de verificação de dados de 
                    32 bits, começando com um crc inicial. Isso é consistente com a soma de verificação do arquivo ZIP. 
                    Uma vez que o algoritmo é projetado para uso como um algoritmo de soma de verificação, não é adequado 
                    para uso como um algoritmo de hash geral. 

    {YELLOW}Nota{YELLOW}{RED} Para gerar o mesmo valor numérico em todas as versões e plataformas Python, {RED}{BLUE}use crc32 (dados) & 0xffffffff{BLUE}{RED}. Se você estiver usando apenas a soma de verificação no formato binário compactado, isso não é necessário, pois o valor de retorno é a representação binária correta de 32 bits, independentemente do sinal.
            """.format(
                            YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                        )
                    )
                else:
                    by_to_st((binascii.crc32(arg_mensage[1].encode())))
            elif arg_mensage[0] == "hexlify":
                if arg_mensage[1] == "help":
                    print(
                        """{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED} Retorna a representação hexadecimal dos dados 
                    binários . Cada byte de dados é convertido na representação hexadecimal de 2 dígitos correspondente. 
                    A string resultante é, portanto, o dobro do comprimento dos dados . 

            """.format(
                            YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                        )
                    )
                else:
                    by_to_st(
                        (binascii.hexlify(arg_mensage[1].encode(), arg_mensage[2].encode()))
                    )
            elif arg_mensage[0] == "b2a_hex":
                if arg_mensage[1] == "help":
                    print(
                        """{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED} hex
            """.format(
                            YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                        )
                    )
                else:
                    by_to_st(
                        (binascii.b2a_hex(arg_mensage[1].encode(), int(arg_mensage[2])))
                    )
            elif arg_mensage[0] == "unhexlify":
                if arg_mensage[1] == "help":
                    print(
                        """{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED} Retorna os dados binários representados pela string hexadecimal hexstr . Esta função é o inverso de b2a_hex () . hexstr deve conter um número par de dígitos hexadecimais (que podem ser maiúsculas ou minúsculas), caso contrário, um TypeError é gerado.

            """.format(
                            YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                        )
                    )
                else:
                    by_to_st((binascii.unhexlify(arg_mensage[1].encode())))
            elif arg_mensage[0] == "b2a_uu":
                if arg_mensage[1] == "help":
                    print(
                        """{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED} Converta dados binários em uma linha de caracteres ASCII, o valor de retorno é a linha convertida, incluindo um caractere de nova linha. O comprimento dos dados deve ser de no máximo 45.

            """.format(
                            YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                        )
                    )
                else:
                    by_to_st(
                        (binascii.b2a_uu(arg_mensage[1].encode(), int(arg_mensage[2])))
                    )
            elif arg_mensage[0] == "charcode":
                if arg_mensage[1] == "help":
                    print(
                        """{YELLOW}charcode{YELLOW}{BLUE} =>{BLUE}{RED}converte string em charcode
            """.format(
                            YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                        )
                    )
                else:
                    print(ord(arg_mensage[1].encode()))
            elif arg_mensage[0] == "binary":
                if arg_mensage[1] == "help":
                    print(
                        """{YELLOW}binary{YELLOW}{BLUE} =>{BLUE}{RED}converte string em binary
            """.format(
                            YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                        )
                    )
                else:
                    print(" ".join(format(ord(x), "b") for x in arg_mensage[1]))
            elif arg_mensage[0] == "base62":
                if arg_mensage[1] == "help":
                    print(
                        """{YELLOW}base62{YELLOW}{BLUE} =>{BLUE}{RED}converte string em base62
            """.format(
                            YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                        )
                    )
                else:
                    print(decode62(arg_mensage[1]))
            elif arg_mensage[0] == "basen":
                if arg_mensage[1] == "help":
                    print(
                        """{YELLOW}basen{YELLOW}{BLUE} =>{BLUE}{RED}converte decimal em basen
            """.format(
                            YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                        )
                    )
                else:
                    print(numpy.base_repr(int(arg_mensage[1]), base=int(arg_mensage[2])))
            elif arg_mensage[0] == "url":
                try:
                    if arg_mensage[1] == "help":
                        print(
                            """{YELLOW}url_encode{YELLOW}{BLUE} =>{BLUE}{RED}encode personalidado para url\nencode url_encode safa[] encoding""".format(
                                YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                            )
                        )
                    else:
                        print(
                            quote(
                                arg_mensage[1], safe=arg_mensage[2], encoding=arg_mensage[3]
                            )
                        )
                except IndexError:
                    print(
                        "digite a sintaxe correta\nncode url_encode safa[] encoding\n ou use o comando help"
                    )
            elif arg_mensage[0] == "unicode_normalize":
                try:
                    if arg_mensage[1] == "help":
                        print(
                            """{YELLOW}unicode_normalize{YELLOW}{BLUE} =>{BLUE}{RED}Transforme caracteres Unicode em uma das formas de normalização['NFC', 'NFKC', 'NFD','NFKD']\n                   
    {YELLOW}NFD{YELLOW}{BLUE} =>{BLUE}{RED}Normalisation Form Canonical Decomposition
    {YELLOW}NFC{YELLOW}{BLUE} =>{BLUE}{RED}Normalisation Form Canonical Composition
    {YELLOW}NFKD{YELLOW}{BLUE} =>{BLUE}{RED}Normalisation Form Compatibility Decomposition
    {YELLOW}NFKC{YELLOW}{BLUE} =>{BLUE}{RED}Normalisation Form Compatibility Composition    
    encode unicode_normalize str encoding['NFC', 'NFKC', 'NFD','NFKD']\n""".format(
                                YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                            )
                        )
                    else:
                        print(unicodedata.normalize(arg_mensage[1], arg_mensage[2]))
                except IndexError:
                    print(
                        "digite a sintaxe correta\nncode url_encode safa[] encoding\n ou use o comando help"
                    )
            elif arg_mensage[0] == "qp_encoding":
                try:
                    if arg_mensage[1] == "help":
                        print(
                            """{YELLOW}qp_encoding{YELLOW}{BLUE} =>{BLUE}{RED}
                        Quoted-Printable, ou QP encoding, 
                        é uma codificação que usa caracteres ASCII imprimíveis (alfanuméricos e o sinal de igual '=') 
                        para transmitir dados de 8 bits em um caminho de dados de 7 bits ou, geralmente, em um meio que não é 8- um pouco limpo. 
                        É definido como uma codificação de transferência de conteúdo MIME para uso em e-mail.
                        QP funciona usando o sinal de igual '=' como um caractere de escape. Ele também limita o comprimento da linha a 76, pois alguns softwares têm limites no comprimento da linha\nencode qp_encoding TXT encode""".format(
                                YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                            )
                        )
                    else:
                        encoded = quopri.encodestring(arg_mensage[1].encode(arg_mensage[2]))
                        print(encoded.decode())
                except IndexError:
                    print(
                        "digite a sintaxe correta\nencode qp_encoding é utf-16\n ou use o comando help"
                    )
            elif arg_mensage[0] == "idna":
                try:
                    if arg_mensage[1] == "help":
                        print(
                            """{YELLOW}idna{YELLOW}{BLUE} =>{BLUE}{RED}encode personalidado para url\nencode url_encode safa[] encoding""".format(
                                YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                            )
                        )
                    else:
                        print(idna.encode(arg_mensage[1]).decode(arg_mensage[2]))
                except IndexError:
                    print(
                        "digite a sintaxe correta\nncode idna string encoding\n ou use o comando help"
                    )

            else:
                pass
            try:
                pass

            except IndexError:
                print("verificar a saida")

    def thg_say(self, line):
        print(
            "You called a command in SecondLevel with '%s'. "
            "It has access to top_level_attr: %s" % (line, self.top_level_attr)
        )

    def help_say(self):
        print("This is a SecondLevel menu. Options are qwe, asd, zxc")

    def complete_say(self, text, line, begidx, endidx):
        return [s for s in ["qwe", "asd", "zxc"] if s.startswith(text)]

    @with_category(Data_format)
    def thg_encode(self, args):
        """modulo referente a encode de estrings"""
        arg_mensage = args.split(" ")
        if arg_mensage[0] == "":
            print(
                """suporte encode:
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

        """.format(
                    YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                )
            )

        elif arg_mensage[0] == "64":
            arg_mensage[1] = arg_mensage[1].encode("ascii")
            base64_bytes = base64.b64encode(arg_mensage[1])
            by_to_st(base64_bytes)
        elif arg_mensage[0] == "32":
            arg_mensage[1] = arg_mensage[1].encode("ascii")
            b32encode_bytes = base64.b32encode(arg_mensage[1])
            by_to_st(b32encode_bytes)
        elif arg_mensage[0] == "16":
            arg_mensage[1] = arg_mensage[1].encode("ascii")
            b16encode_bytes = base64.b16encode(arg_mensage[1])
            by_to_st(b16encode_bytes)
        elif arg_mensage[0] == "a85encode":
            arg_mensage[1] = arg_mensage[1].encode("ascii")
            a85encode_bytes = base64.a85encode(arg_mensage[1])
            by_to_st(a85encode_bytes)
        elif arg_mensage[0] == "b85encode":
            arg_mensage[1] = arg_mensage[1].encode("ascii")
            b85encode_bytes = base64.b85encode(arg_mensage[1])
            by_to_st(b85encode_bytes)
        elif arg_mensage[0] == "a2b_uu":
            if arg_mensage[1] == "help":
                print(
                    """{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED} Converta uma única linha de dados uuencodificados de volta em binários e retorne os dados binários. As linhas normalmente contêm 45 bytes (binários), exceto a última linha. Os dados da linha podem ser seguidos de espaços em branco.""".format(
                        YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                    )
                )
            else:
                by_to_st((binascii.a2b_uu(arg_mensage[1])))
        elif arg_mensage[0] == "a2b_base64":
            if arg_mensage[1] == "help":
                print(
                    """{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED}Converta dados binários em uma linha de caracteres ASCII na codificação base64. O valor de retorno é a linha convertida, incluindo um caractere de nova linha. O comprimento dos dados deve ser de no máximo 57 para aderir ao padrão base64.""".format(
                        YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                    )
                )
            else:
                by_to_st(binascii.a2b_base64(arg_mensage[1]))
        elif arg_mensage[0] == "b2a_base64":
            if arg_mensage[1] == "help":
                print(
                    """{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED} Converta dados binários em uma linha de caracteres ASCII na codificação base64. O valor de retorno é a linha convertida, incluindo um caractere de nova linha. O comprimento dos dados deve ser de no máximo 57 para aderir ao padrão base64.""".format(
                        YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                    )
                )
            else:
                by_to_st(binascii.b2a_base64(b"arg_mensage[1]"))
        elif arg_mensage[0] == "a2b_qp":
            if arg_mensage[1] == "help":
                print(
                    """{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED}Converta um bloco de dados imprimíveis entre aspas de volta em binários e retorne os dados binários. Mais de uma linha pode ser passada por vez. Se o cabeçalho do argumento opcional estiver presente e verdadeiro, os sublinhados serão decodificados como espaços.""".format(
                        YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                    )
                )
            else:
                by_to_st(binascii.a2b_qp(arg_mensage[1]))
        elif arg_mensage[0] == "b2a_qp":
            if arg_mensage[1] == "help":
                print(
                    """{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED}Converta dados binários em uma (s) linha (s) de caracteres ASCII em codificação imprimível entre aspas. O valor de retorno é a (s) linha (s) convertida (s). Se o argumento opcional quotetabs estiver presente e verdadeiro, todas as tabulações e espaços serão codificados. Se o argumento opcional istext estiver presente e verdadeiro, as novas linhas não serão codificadas, mas os espaços em branco finais serão codificados. Se o cabeçalho do argumento opcional estiver presente e verdadeiro, os espaços serão codificados como sublinhados de acordo com RFC1522. Se o cabeçalho do argumento opcional estiver presente e for falso, os caracteres de nova linha também serão codificados; caso contrário, a conversão de alimentação de linha pode corromper o fluxo de dados binários.""".format(
                        YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                    )
                )
            else:
                by_to_st(binascii.a2b_qp(arg_mensage[1].encode()))
        elif arg_mensage[0] == "a2b_hqx":
            if arg_mensage[1] == "help":
                print(
                    """{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED}Converta dados ASCII formatados de binhex4 em binários, sem fazer a descompressão RLE. A string deve conter um número completo de bytes binários ou (no caso da última parte dos dados binhex4) ter os bits restantes zero.
""".format(
                        YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                    )
                )
            else:
                by_to_st(binascii.a2b_hqx(arg_mensage[1]))
        elif arg_mensage[0] == "rledecode_hqx":
            if arg_mensage[1] == "help":
                print(
                    """{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED} Execute a descompressão RLE nos dados, de acordo com o padrão binhex4. O algoritmo usa 0x90 após um byte como um indicador de repetição, seguido por uma contagem. Uma contagem de 0 especifica um valor de byte de 0x90 . A rotina retorna os dados descompactados, a menos que os dados de entrada de dados terminem em um indicador de repetição órfão, caso em que a exceção Incompleta é levantada.""".format(
                        YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                    )
                )
            else:
                by_to_st((binascii.rledecode_hqx(arg_mensage[1].encode())))
        elif arg_mensage[0] == "rlecode_hqx":
            if arg_mensage[1] == "help":
                print(
                    """{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED} Execute a compactação RLE no estilo binhex4 nos dados e retorne o resultado.""".format(
                        YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                    )
                )
            else:
                by_to_st((binascii.rlecode_hqx(arg_mensage[1].encode())))
        elif arg_mensage[0] == "b2a_hqx":
            if arg_mensage[1] == "help":
                print(
                    """{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED} Execute a conversão hexbin4 binário para ASCII e retorne a string resultante. O argumento já deve ser codificado por RLE e ter um comprimento divisível por 3 (exceto possivelmente o último fragmento).
""".format(
                        YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                    )
                )
            else:
                by_to_st((binascii.b2a_hqx(arg_mensage[1].encode())))
        elif arg_mensage[0] == "crc_hqx":
            if arg_mensage[1] == "help":
                print(
                    """{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED} Calcule o valor binhex4 crc dos dados , começando com um crc inicial e retornando o resultado.
""".format(
                        YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                    )
                )
            else:
                by_to_st(
                    (binascii.crc_hqx(arg_mensage[1].encode(), int(arg_mensage[2])))
                )
        elif arg_mensage[0] == "crc32":
            if arg_mensage[1] == "help":
                print(
                    """{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED} Calcule CRC-32, a soma de verificação de dados de 
                32 bits, começando com um crc inicial. Isso é consistente com a soma de verificação do arquivo ZIP. 
                Uma vez que o algoritmo é projetado para uso como um algoritmo de soma de verificação, não é adequado 
                para uso como um algoritmo de hash geral. 
{YELLOW}Nota{YELLOW}{RED} Para gerar o mesmo valor numérico em todas as versões e plataformas Python, {RED}{BLUE}use crc32 (dados) & 0xffffffff{BLUE}{RED}. Se você estiver usando apenas a soma de verificação no formato binário compactado, isso não é necessário, pois o valor de retorno é a representação binária correta de 32 bits, independentemente do sinal.
        """.format(
                        YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                    )
                )
            else:
                by_to_st((binascii.crc32(arg_mensage[1].encode())))
        elif arg_mensage[0] == "hexlify":
            if arg_mensage[1] == "help":
                print(
                    """{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED} Retorna a representação hexadecimal dos dados 
                binários . Cada byte de dados é convertido na representação hexadecimal de 2 dígitos correspondente. 
                A string resultante é, portanto, o dobro do comprimento dos dados . 
        """.format(
                        YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                    )
                )
            else:
                by_to_st(
                    (binascii.hexlify(arg_mensage[1].encode(), arg_mensage[2].encode()))
                )
        elif arg_mensage[0] == "b2a_hex":
            if arg_mensage[1] == "help":
                print(
                    """{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED} hex
        """.format(
                        YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                    )
                )
            else:
                by_to_st(
                    (binascii.b2a_hex(arg_mensage[1].encode(), int(arg_mensage[2])))
                )
        elif arg_mensage[0] == "unhexlify":
            if arg_mensage[1] == "help":
                print(
                    """{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED} Retorna os dados binários representados pela string hexadecimal hexstr . Esta função é o inverso de b2a_hex () . hexstr deve conter um número par de dígitos hexadecimais (que podem ser maiúsculas ou minúsculas), caso contrário, um TypeError é gerado.
        """.format(
                        YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                    )
                )
            else:
                by_to_st((binascii.unhexlify(arg_mensage[1].encode())))
        elif arg_mensage[0] == "b2a_uu":
            if arg_mensage[1] == "help":
                print(
                    """{YELLOW}a2b_uu{YELLOW}{BLUE} =>{BLUE}{RED} Converta dados binários em uma linha de caracteres ASCII, o valor de retorno é a linha convertida, incluindo um caractere de nova linha. O comprimento dos dados deve ser de no máximo 45.
        """.format(
                        YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                    )
                )
            else:
                by_to_st(
                    (binascii.b2a_uu(arg_mensage[1].encode(), int(arg_mensage[2])))
                )
        elif arg_mensage[0] == "charcode":
            if arg_mensage[1] == "help":
                print(
                    """{YELLOW}charcode{YELLOW}{BLUE} =>{BLUE}{RED}converte string em charcode
        """.format(
                        YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                    )
                )
            else:
                print(ord(arg_mensage[1].encode()))
        elif arg_mensage[0] == "binary":
            if arg_mensage[1] == "help":
                print(
                    """{YELLOW}binary{YELLOW}{BLUE} =>{BLUE}{RED}converte string em binary
        """.format(
                        YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                    )
                )
            else:
                print(" ".join(format(ord(x), "b") for x in arg_mensage[1]))
        elif arg_mensage[0] == "base62":
            if arg_mensage[1] == "help":
                print(
                    """{YELLOW}base62{YELLOW}{BLUE} =>{BLUE}{RED}converte string em base62
        """.format(
                        YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                    )
                )
            else:
                print(decode62(arg_mensage[1]))
        elif arg_mensage[0] == "basen":
            if arg_mensage[1] == "help":
                print(
                    """{YELLOW}basen{YELLOW}{BLUE} =>{BLUE}{RED}converte decimal em basen
        """.format(
                        YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                    )
                )
            else:
                print(numpy.base_repr(int(arg_mensage[1]), base=int(arg_mensage[2])))
        elif arg_mensage[0] == "url":
            try:
                if arg_mensage[1] == "help":
                    print(
                        """{YELLOW}url_encode{YELLOW}{BLUE} =>{BLUE}{RED}encode personalidado para url\nencode url_encode safa[] encoding""".format(
                            YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                        )
                    )
                else:
                    print(
                        quote(
                            arg_mensage[1], safe=arg_mensage[2], encoding=arg_mensage[3]
                        )
                    )
            except IndexError:
                print(
                    "digite a sintaxe correta\nncode url_encode safa[] encoding\n ou use o comando help"
                )
        elif arg_mensage[0] == "unicode_normalize":
            try:
                if arg_mensage[1] == "help":
                    print(
                        """{YELLOW}unicode_normalize{YELLOW}{BLUE} =>{BLUE}{RED}Transforme caracteres Unicode em uma das formas de normalização['NFC', 'NFKC', 'NFD','NFKD']\n                   
{YELLOW}NFD{YELLOW}{BLUE} =>{BLUE}{RED}Normalisation Form Canonical Decomposition
{YELLOW}NFC{YELLOW}{BLUE} =>{BLUE}{RED}Normalisation Form Canonical Composition
{YELLOW}NFKD{YELLOW}{BLUE} =>{BLUE}{RED}Normalisation Form Compatibility Decomposition
{YELLOW}NFKC{YELLOW}{BLUE} =>{BLUE}{RED}Normalisation Form Compatibility Composition    
encode unicode_normalize str encoding['NFC', 'NFKC', 'NFD','NFKD']\n""".format(
                            YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                        )
                    )
                else:
                    print(unicodedata.normalize(arg_mensage[1], arg_mensage[2]))
            except IndexError:
                print(
                    "digite a sintaxe correta\nncode url_encode safa[] encoding\n ou use o comando help"
                )
        elif arg_mensage[0] == "qp_encoding":
            try:
                if arg_mensage[1] == "help":
                    print(
                        """{YELLOW}qp_encoding{YELLOW}{BLUE} =>{BLUE}{RED}
                    Quoted-Printable, ou QP encoding, 
                    é uma codificação que usa caracteres ASCII imprimíveis (alfanuméricos e o sinal de igual '=') 
                    para transmitir dados de 8 bits em um caminho de dados de 7 bits ou, geralmente, em um meio que não é 8- um pouco limpo. 
                    É definido como uma codificação de transferência de conteúdo MIME para uso em e-mail.
                    QP funciona usando o sinal de igual '=' como um caractere de escape. Ele também limita o comprimento da linha a 76, pois alguns softwares têm limites no comprimento da linha\nencode qp_encoding TXT encode""".format(
                            YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                        )
                    )
                else:
                    encoded = quopri.encodestring(arg_mensage[1].encode(arg_mensage[2]))
                    print(encoded.decode())
            except IndexError:
                print(
                    "digite a sintaxe correta\nencode qp_encoding é utf-16\n ou use o comando help"
                )
        elif arg_mensage[0] == "idna":
            try:
                if arg_mensage[1] == "help":
                    print(
                        """{YELLOW}idna{YELLOW}{BLUE} =>{BLUE}{RED}encode personalidado para url\nencode url_encode safa[] encoding""".format(
                            YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                        )
                    )
                else:
                    print(idna.encode(arg_mensage[1]).decode(arg_mensage[2]))
            except IndexError:
                print(
                    "digite a sintaxe correta\nncode idna string encoding\n ou use o comando help"
                )

        else:
            pass
        try:
            pass

        except IndexError:
            print("verificar a saida")

    @with_category(Data_format)
    def thg_dump(self, args):
        arg = args.split(" ")
        if arg[0] == "":
            print(
                "dump mod[hex,hex_file] tab[int]\ndump hex string\ndump hex_file file"
            )
        elif arg[0] == "hex":
            if arg[1] == "help":
                print(
                    """{YELLOW}hex{YELLOW}{BLUE} =>{BLUE}{RED} text for hex.""".format(
                        YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                    )
                )
            else:
                print(hexdump(src=arg[1], length=int(arg[2])))
        elif arg[0] == "hex_file":
            if arg[1] == "help":
                print(
                    """{YELLOW}hex_file{YELLOW}{BLUE} =>{BLUE}{RED} file for hex.""".format(
                        YELLOW=Fore.YELLOW, BLUE=Fore.BLUE, RED=Fore.RED
                    )
                )
            else:
                try:
                    with (open(arg[1], "br")) as file:
                        data = file.read()
                        hexdump_file(data)
                except FileNotFoundError:
                    print("esse comando requer um arquivo e não uma string")
