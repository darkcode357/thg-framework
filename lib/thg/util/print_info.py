from colorama import Fore


def _print_info(msg):
    return Fore.YELLOW + f'[{Fore.GREEN}!{Fore.GREEN + Fore.YELLOW}] {msg}'


def _print_error(msg):
    return Fore.YELLOW + f'[{Fore.RED}X{Fore.RED + Fore.YELLOW}] {msg}'

def _print_warning(msg):
    return Fore.YELLOW + f'[{Fore.YELLOW}?{Fore.YELLOW + Fore.YELLOW}] {msg}'



