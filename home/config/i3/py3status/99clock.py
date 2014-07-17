# -*- coding: utf-8 -*-
import locale
from time import time, strftime
import subprocess
class Py3status:
	def clock(self, json, i3status_config):  
		locale.setlocale(locale.LC_TIME, "de_DE")      
		clockstr = "  " + strftime("%A %-d. %B %X KW%V")
		response = {'full_text': '', 'name': 'clock'}
		response['color'] = "#eee8d5"
		response['full_text'] = clockstr
		response['cached_until'] = time() + 1
		return (0, response)
	def on_click(self, json, i3status_config, event):
		if event['button'] == 1:
			#subprocess.Popen(["chromium"])
			subprocess.Popen(["killall", "-USR1", "py3status"])