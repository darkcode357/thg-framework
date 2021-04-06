
from colorama import Fore
from lib.thg.base.Database.Database import Database

###
#
# This file contains constants that are referenced by the core
# framework and by framework modules.
#
###
__version__ = 1.2


#
# Global constants
#
#
# menu


class Menu(Database):
    def __init__(self):
        Database.__init__(self)

    def menu(self):
        return """
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
            """.format(
            count=self.get_module_count(),
            red=Fore.RED,
            CYAN=Fore.CYAN,
            GREEN=Fore.GREEN,
            RED=Fore.RED,
            YELLOW=Fore.YELLOW,
            MAGENTA=Fore.MAGENTA,
            os=platform.uname()[0],
            machine=platform.uname()[4],
            version=__version__,
        )


#
# Interpreter thg categoria
#
CMD_CORE = "Core Command"
CMD_MODULE = "Module Command"
Data_format = "Data-format"
Encryption_encoding = "Encryption_encoding"
Public_key = "Public_key"
Arithmetic_Logic = "Arithmetic_Logic"
Networking = "Networking"
Language = "Language"
utils = "utils"
data_time = "data_time"
extractors = "extractors"
compression = "compression"
hashing = "hashing"
codetidy = "codetidy"
forensics = "forensics"
multmidia = "multmidia"

