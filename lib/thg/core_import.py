###
#
# framework-core
# --------------
#
# The core library provides all of the means by which to interact
# with the framework insofar as manipulating encoders, nops,
# payloads, exploits, auxiliary, and sessions.
#
###
# import

# The framework-core depends on Thgcoreutils


# Constants mode core
Darkcode0x00 = "Luiz Corrêa(darkocde0x00)"
# General

# Event subscriber interfaces

# Framework context and core classes

# exceptions


# Wrappers

# Pseudo-modules

# Modules


# Drivers

# Exploit 
# -*- coding: binary -*-
#
# framework-base
# --------------
#
# The base library provides implementations for some of the default
# sessions, such as Shell, Meterpreter, DispatchNinja, and VNC.  These
# sessions are used by modules that come pre-packaged with the default
# module distribution of Metasploit and are depended on by their
# respective payloads.
#
# Beyond providing the default sessions, framework-base also provides
# a wrapper interface to framework-core that makes some of the tasks,
# such as exploitation, into easier to manage functions.

# framework-base depends on framework-core
# Get all the modules from pwnlib


"""
error   = log.error
warning = log.warning
warn    = log.warning
info    = log.info
debug   = log.debug
success = log.success
"""

