# Promote useful stuff to toplevel
from __future__ import absolute_import

from lib.toplevel import *
#pwnlib.args.initialize()
pwnlib.log.install_default_handler()
pwnlib.config.initialize()

log = pwnlib.log.getLogger('thg.exploit')
args = pwnlib.args.args

if not platform.architecture()[0].startswith('64'):
    log.warn_once('Mod Pwntools does not support 32-bit Python.  Use a 64-bit release.')

