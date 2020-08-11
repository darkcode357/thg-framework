 thg-framework - exploit dev/toolkit

![thg logo](https://github.com/darkcode357/thg-framework/raw/master/logo.png?raw=true)
[![PyPI](https://img.shields.io/pypi/v/thg-framework?color=thg-framework&label=thg-framework&logo=thg-framework&logoColor=thg-framework)](https://pypi.python.org/pypi/pwntools/)
[![Docs](https://readthedocs.org/projects/pwntools/badge/?version=stable)](criar_site_documentação)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](http://choosealicense.com/licenses/mit/)
[![Twitter](https://img.shields.io/twitter/follow/DarkcodeHacking)](http://twitter.com/DarkcodeHacking)

O THG é um framework voltado para teste de segurança e jogos de  ctf, porém pode ser usado como uma biblioteca para desenvolvimento de exploits.
Escrito em Python, é projetado para prototipagem e desenvolvimento rápido e tem como objetivo tornar a escrita de exploit a mais simples possível,
dando a possibilidade para o explorador/dev ter total controle da ferramenta em tempo de execução, podendo trabalhar tanto como console de exploração tanto como o console
interativo do python em seu modo dinâmico, dando total flexibilidade na hora da exploração

```python
from pwn import *
context(arch = 'i386', os = 'linux')

r = remote('exploitme.example.com', 31337)
# EXPLOIT CODE GOES HERE
r.send(asm(shellcraft.sh()))
r.interactive()
```

# Documentation

Our documentation is available at [docs.pwntools.com](https://docs.pwntools.com/)

A series of tutorials is also [available online](https://github.com/Gallopsled/pwntools-tutorial#readme)

To get you started, we've provided some example solutions for past CTF challenges in our [write-ups repository](https://github.com/Gallopsled/pwntools-write-ups).

# Installation

Pwntools is best supported on 64-bit Ubuntu LTE releases (14.04, 16.04, 18.04, and 20.04).  Most functionality should work on any Posix-like distribution (Debian, Arch, FreeBSD, OSX, etc.).  Python >= 2.7 is required (Python 3 suggested as best).

Most of the functionality of pwntools is self-contained and Python-only.  You should be able to get running quickly with

```sh
apt-get update
apt-get install python3 python3-pip python3-dev git libssl-dev libffi-dev build-essential
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade pwntools
```

However, some of the features (assembling/disassembling foreign architectures) require non-Python dependencies.  For more information, see the [complete installation instructions here](https://docs.pwntools.com/en/stable/install.html).


# Contribution

See [CONTRIBUTING.md](CONTRIBUTING.md)

# Contact
If you have any questions not worthy of a [bug report](https://github.com/Gallopsled/pwntools/issues), feel free to ping us
at [`#pwntools` on Freenode](irc://irc.freenode.net/pwntools) and ask away.
Click [here](https://kiwiirc.com/client/irc.freenode.net/pwntools) to connect.
There is also a [mailing list](https://groups.google.com/forum/#!forum/pwntools-users) for higher latency discussion.