# pwntools - kit de ferramentas CTF
! [logotipo do pwntools] (https://github.com/Gallopsled/pwntools/blob/stable/docs/source/logo.png?raw=true)

[! [PyPI] (https://img.shields.io/pypi/v/pwntools?style=flat)] (https://pypi.python.org/pypi/pwntools/)
[! [Docs] (https://readthedocs.org/projects/pwntools/badge/?version=stable)] (https://docs.pwntools.com/)
[! [Travis] (https://img.shields.io/travis/Gallopsled/pwntools/dev?logo=Travis)] (https://travis-ci.org/Gallopsled/pwntools)
! [Status do fluxo de trabalho do GitHub (branch)] (https://img.shields.io/github/workflow/status/Gallopsled/pwntools/Continuous%20Integration/dev?logo=GitHub)
[! [Coveralls] (https://img.shields.io/coveralls/github/Gallopsled/pwntools/dev?logo=coveralls)] (https://coveralls.io/github/Gallopsled/pwntools?branch=dev)
[! [Licença MIT] (https://img.shields.io/badge/license-MIT-blue.svg?style=flat)] (http://choosealicense.com/licenses/mit/)
[! [Twitter] (https://img.shields.io/twitter/follow/Pwntools)] (https://twitter.com/pwntools)

Pwntools é um framework CTF e uma biblioteca de desenvolvimento de exploits. Escrito em Python, é projetado para prototipagem e desenvolvimento rápidos e tem como objetivo tornar a escrita de exploits o mais simples possível.

`` `python
da importação pwn *
contexto (arch = 'i386', os = 'linux')

r = remoto ('exploitme.example.com', 31337)
# EXPLORAR O CÓDIGO VAI AQUI
r.send (asm (shellcraft.sh ()))
r.interactive ()
`` `

# Documentação

Nossa documentação está disponível em [docs.pwntools.com] (https://docs.pwntools.com/)

Uma série de tutoriais também está disponível online (https://github.com/Gallopsled/pwntools-tutorial#readme)

Para começar, fornecemos algumas soluções de exemplo para desafios anteriores de CTF em nosso [repositório de write-ups] (https://github.com/Gallopsled/pwntools-write-ups).

# Instalação

O Pwntools tem melhor suporte nas versões LTE do Ubuntu de 64 bits (14.04, 16.04, 18.04 e 20.04). A maioria das funcionalidades deve funcionar em qualquer distribuição do tipo Posix (Debian, Arch, FreeBSD, OSX, etc.). Python> = 2.7 é necessário (Python 3 sugerido como melhor).

A maior parte da funcionalidade do pwntools é independente e somente Python. Você deve ser capaz de começar a trabalhar rapidamente com

`` `sh
apt-get update
apt-get install python3 python3-pip python3-dev git libssl-dev libffi-dev build-essential
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade pwntools
`` `

No entanto, alguns dos recursos (montagem / desmontagem de arquiteturas estrangeiras) requerem dependências não-Python. Para obter mais informações, consulte as [instruções completas de instalação aqui] (https://docs.pwntools.com/en/stable/install.html).


# Contribuição

Veja [CONTRIBUTING.md] (CONTRIBUTING.md)

# Contato
Se você tiver alguma pergunta que não mereça um [relatório de bug] (https://github.com/Gallopsled/pwntools/issues), sinta-se à vontade para nos enviar um ping
em [`# pwntools` em Freenode] (irc: //irc.freenode.net/pwntools) e pergunte.
Clique [aqui] (https://kiwiirc.com/client/irc.freenode.net/pwntools) para se conectar.
Também existe uma [lista de discussão] (https://groups.google.com/forum/#!forum/pwntools-users) para discussão de latência mais alta.