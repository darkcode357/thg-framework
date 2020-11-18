import platform

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
        menu = """
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
        return menu


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

#
# Global constants
#

# Licenses
THG_LICENSE = "Thg Framework License (BSD)"
GPL_LICENSE = "GNU Public License v2.0"
BSD_LICENSE = "BSD License"
CORE_LICENSE = "CORE Security License (Apache 1.1)"
ARTISTIC_LICENSE = "Perl Artistic License"
UNKNOWN_LICENSE = "Unknown License"
LICENSES = [
    THG_LICENSE,
    GPL_LICENSE,
    BSD_LICENSE,
    CORE_LICENSE,
    ARTISTIC_LICENSE,
    UNKNOWN_LICENSE,
]
#
# Module types
#
MODULE_ANY = "_any_"
MODULE_ENCODER = "encoder"
MODULE_EXPLOIT = "exploit"
MODULE_NOP = "nop"
MODULE_AUX = "auxiliary"
MODULE_PAYLOAD = "payload"
MODULE_POST = "post"
MODULE_EVASION = "evasion"
MODULE_TYPES = [
    MODULE_ENCODER,
    MODULE_PAYLOAD,
    MODULE_EXPLOIT,
    MODULE_NOP,
    MODULE_POST,
    MODULE_AUX,
    MODULE_EVASION,
]
#
# Module rankings
#
ManualRanking = 0
LowRanking = 100
AverageRanking = 200
NormalRanking = 300
GoodRanking = 400
GreatRanking = 500
ExcellentRanking = 600
RankingName = {
    "ManualRanking   ": "manual",
    "LowRanking      ": "low",
    "AverageRanking  ": "average",
    "NormalRanking   ": "normal",
    "GoodRanking     ": "good",
    "GreatRanking    ": "great",
    "ExcellentRanking": "excellent",
}

#
# Stability traits
#

# Module should not crash the service.
CRASH_SAFE = "crash-safe"
# Module may crash the service, but the service restarts.
CRASH_SERVICE_RESTARTS = "crash-service-restarts"
# Module may crash the service, and the service remains down.
CRASH_SERVICE_DOWN = "crash-service-down"
# Module may crash the OS, but the OS restarts.
CRASH_OS_RESTARTS = "crash-os-restarts"
# Module may crash the OS, and the OS remains down.
CRASH_OS_DOWN = "crash-os-down"
# Module may cause a resource (such as a file or data in a database) to be unavailable for the service.
SERVICE_RESOURCE_LOSS = "service-resource-loss"
# Modules may cause a resource (such as a file) to be unavailable for the OS.
OS_RESOURCE_LOSS = "os-resource-loss"

#
# Side-effect traits
#

# Modules leaves a payload or a dropper on the target machine.
ARTIFACTS_ON_DISK = "artifacts-on-disk"
# Module modifies some configuration setting on the target machine.
CONFIG_CHANGES = "config-changes"
# Module leaves signs of a compromise in a log file (Example: SQL injection data found in HTTP log).
IOC_IN_LOGS = "ioc-in-logs"
# Module may cause account lockouts (likely due to brute-forcing).
ACCOUNT_LOCKOUTS = "account-lockouts"
# Module may show something on the screen (Example: a window pops up).
SCREEN_EFFECTS = "screen-effects"
# Module may cause a noise (Examples: audio output from the speakers or hardware beeps).
AUDIO_EFFECTS = "audio-effects"
# Module may produce physical effects (Examples: the device makes movement or flashes LEDs).
PHYSICAL_EFFECTS = "physical-effects"

#
# Reliability
#

# The module tends to fail to get a session on the first attempt.
FIRST_ATTEMPT_FAIL = "first-attempt-fail"
# The module is expected to get a shell every time it runs.
REPEATABLE_SESSION = "repeatable-session"
# The module isn't expected to get a shell reliably (such as only once).
UNRELIABLE_SESSION = "unreliable-session"


class HttpClients:
    IE = "MSIE"
    FF = "Firefox"
    SAFARI = "Safari"
    OPERA = "Opera"
    CHROME = "Chrome"
    EDGE = "Edge"

    UNKNOWN = "Unknown"


class OperatingSystems:
    LINUX = "Linux"
    MAC_OSX = "Mac OS X"
    WINDOWS = "Windows"
    FREEBSD = "FreeBSD"
    NETBSD = "NetBSD"
    OPENBSD = "OpenBSD"
    VMWARE = "VMware"
    ANDROID = "Android"
    APPLE_IOS = "iOS"


class VmwareVersions:
    ESX = "ESX"
    ESXI = "ESXi"


class WindowsVersions:
    NINE5 = "95"
    NINE8 = "98"
    NT = "NT"
    XP = "XP"
    TWOK = "2000"
    TWOK3 = "2003"
    VISTA = "Vista"
    TWOK8 = "2008"
    TWOK12 = "2012"
    SEVEN = "7"
    EIGHT = "8"
    EIGHTONE = "8.1"
    TEN = "10.0"
    UNKNOWN = "Unknown"


class SystemMatch:
    systemmatch = {
        ################windows##########
        "WINDOWS": """ /^(?:Microsoft )?Windows/""",
        "WINDOWS_95": """ /^(?:Microsoft )?Windows 95/""",
        "WINDOWS_98": """ /^(?:Microsoft )?Windows 98/""",
        "WINDOWS_ME": """ /^(?:Microsoft )?Windows ME/""",
        "WINDOWS_NT3": """ /^(?:Microsoft )?Windows NT 3/""",
        "WINDOWS_NT4": """ /^(?:Microsoft )?Windows NT 4/""",
        "WINDOWS_2000": """ /^(?:Microsoft )?Windows 2000/""",
        "WINDOWS_XP": """ /^(?:Microsoft )?Windows XP/""",
        "WINDOWS_2003": """ /^(?:Microsoft )?Windows 2003/""",
        "WINDOWS_VISTA": """ /^(?:Microsoft )?Windows Vista/""",
        "WINDOWS_2008": """ /^(?:Microsoft )?Windows 2008/""",
        "WINDOWS_7": """ /^(?:Microsoft )?Windows 7/""",
        "WINDOWS_2012": """ /^(?:Microsoft )?Windows 2012/""",
        "WINDOWS_8": """ /^(?:Microsoft )?Windows 8/""",
        "WINDOWS_81": """ /^(?:Microsoft )?Windows 8\.1/""",
        "WINDOWS_10": """ /^(?:Microsoft )?Windows 10/""",
        ################linux/unix##########
        "LINUX": """ /^Linux/i""",
        "MAC_OSX": """ /^(?:Apple )?Mac OS X/""",
        "FREEBSD": """' /^FreeBSD/""",
        "NETBSD": """ /^NetBSD/""",
        "OPENBSD": """' /^OpenBSD/""",
        "VMWARE": """ /^VMware/""",
        "ANDROID": """ /^(?:Google )?Android/""",
        "APPLE_IOS": """ /^(?:Apple )?iOS/""",
    }
