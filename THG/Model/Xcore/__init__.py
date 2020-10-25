"""
The thg Xcode library is provided under the 3-clause BSD license.
Copyright (c) 2020-2030, THG/Darkcode0x00, Inc.
All rights reserved.
Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:
 * Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

 * Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

 * Neither the name of THG/Darkcode0x00, Inc. nor the names of its contributors may be
   used to endorse or promote products derived from this software without
   specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

#
# Xcore libs for thg
#
# Library for manager user_agent
from THG.Model.Xcore.useragents import getall
from THG.Model.Xcore.useragents import random
from THG.Model.Xcore.useragents import randommod
#ipaddress
from THG.Model.Xcore.ipaddress import random_text
from THG.Model.Xcore.ipaddress import is_ipv4
from THG.Model.Xcore.ipaddress import is_ipv6
from THG.Model.Xcore.ipaddress import convert_ip
from THG.Model.Xcore.ipaddress import convert_port

# Text manipulation library for things like generating random string
# todo import  'Xcore/text'

# Library for Generating Randomized strings valid as Identifiers such as variable names
# todo import 'Xcore/random_identifier'

# library for creating Powershell scripts for exploitation purposes
# todo import 'Xcore/powershell'

# Library for processing and creating Zip compatible archives
# todo import'Xcore/zip'

# Library for processing and creating tar compatible archives (not really a gem)
# todo import 'Xcore/tar'

# Library for parsing offline Windows Registry files
# todo import 'Xcore/registry'

# Library for parsing Java serialized streams
# todo import 'Xcore/java'

# Library for creating C-style Structs

# todo import 'Xcore/struct2'
# Library for working with OLE

# todo import 'Xcore/ole'
# Library for creating and/or parsing MIME messages

# todo import 'Xcore/mime'
# Library for polymorphic encoders

# todo import 'Xcore/encoder'
# Architecture subsystem

# todo import 'Xcore/arch'
# Exploit Helper Library

# todo import 'Xcore/exploitation'
# Generic classes

# todo import 'Xcore/exceptions'

# todo import 'Xcore/transformer'

# todo import 'Xcore/random_identifier'

# todo import 'Xcore/time'

# todo import 'Xcore/job_container'

# todo import 'Xcore/file'

# Thread safety and synchronization
# todo import 'Xcore/sync'

# Thread factory
# todo import 'Xcore/thread_factory'

# Assembly
# todo import 'Xcore/assembly/nasm'

# Logging
# todo import 'Xcore/logging/log_dispatcher'

# IO
# todo import 'Xcore/io/stream'
# todo import 'Xcore/io/stream_abstraction'
# todo import 'Xcore/io/stream_server'

# Sockets
# todo import 'Xcore/socket'

# Protocols
# todo import 'Xcore/proto'
# todo import 'Xcore/mac_oui'

# Parsers
# todo import 'Xcore/parser/arguments'
# todo import 'Xcore/parser/ini'

# Compatibility
# todo import 'Xcore/compat'

# SSLScan
# todo import 'Xcore/sslscan/scanner'
# todo import 'Xcore/sslscan/result'

# Cryptography
# todo import 'Xcore/crypto/aes256'
# todo import 'Xcore/crypto/rc4'
# todo import 'Xcore/crypto/chacha20'

#Exceptions
from THG.Model.Xcore.exception.exception import AddressValueError
from THG.Model.Xcore.exception.exception import NetmaskValueError