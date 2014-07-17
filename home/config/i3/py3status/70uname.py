# -*- coding: utf-8 -*-
from time import time
import platform
class Py3status:
	def uname(self, json, i3status_config):  
		data = platform.uname()  
		namestr = "  " + data[0] + " " + data[2]
		response = {'full_text': '', 'name': 'uname'}
		response['color'] = "#d33682"
		response['full_text'] = namestr
		response['cached_until'] = time() + 3600
		return (0, response)