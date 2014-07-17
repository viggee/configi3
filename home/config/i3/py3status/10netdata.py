# -*- coding: utf-8 -*-

"""
Copyright (c) 2013 Ultrabug, http://www.ultrabug.fr
All rights reserved.

 Redistribution and use in source and binary forms, with or without
 modification, are permitted provided that the following conditions are met:

 * Redistributions of source code must retain the above copyright notice,
  this list of conditions and the following disclaimer.

 * Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

 THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
 LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 POSSIBILITY OF SUCH DAMAGE.

Modified by viggee
"""

import subprocess
from time import time

old_transmitted, old_received = 0, 0
refresh = 2

class GetData:
    """Get system status

    """
    def __init__(self):
        # You can change it to another interface.
        # It'll be used for grabbing net interface data.
        self.net_interface = 'enp4s0'

    def execCMD(self, cmd, arg):
        """Take a system command and its argument, then return the result.

        Arguments:
        - `cmd`: system command.
        - `arg`: argument.
        """
        result = subprocess.check_output([cmd, arg])
        return result

    def netBytes(self):
        """Execute 'cat /proc/net/dev', find the interface line (Default
        'eth0') and grab received/transmitted bytes.

        """
        net_data = self.execCMD('cat', '/proc/net/dev').decode('utf-8').split()
        interface_index = net_data.index(self.net_interface + ':')
        received_bytes = int(net_data[interface_index + 1])
        transmitted_bytes = int(net_data[interface_index + 9])
        return received_bytes, transmitted_bytes

class Py3status:
    def download(self, json, i3status_config):
        data = GetData()
        response = {'full_text': '', 'name': 'netdata'}

        global old_received 

        (received_bytes, transmitted_bytes) = data.netBytes()
    
        dl_speed = (received_bytes - old_received) / 1024 / refresh
        download = received_bytes / 1024 / 1024.  

        response['color'] = "#859900"
        response['full_text'] = "  {:5.1f} KiB/s ({:.0f} MiB)".format(dl_speed, download)
        response['cached_until'] = time() + refresh

        old_received = received_bytes
        return (0, response)
    def upload(self, json, i3status_config):
        data = GetData()
        response = {'full_text': '', 'name': 'netdata'}

        global old_transmitted

        (received_bytes, transmitted_bytes) = data.netBytes()
    
        up_speed = (transmitted_bytes - old_transmitted) / 1024 / refresh
        upload = transmitted_bytes / 1024 / 1024.     

        response['color'] = "#cb4b16"
        response['full_text'] = "  {:5.1f} KiB/s ({:.0f} MiB)".format(up_speed, upload)
        response['cached_until'] = time() + refresh

        old_transmitted = transmitted_bytes
        return (0, response)    
