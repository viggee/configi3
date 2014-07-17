# -*- coding: utf-8 -*-
from time import time
import subprocess
import re
class Py3status:
	def volume(self, json, i3status_config):  
		data = subprocess.check_output(['amixer', '-M', '-c', '0', 'sget', 'Master']).decode('utf-8')
		volumeobj = re.search(r"\[.*%\]", data, re.M)
		volume = int(volumeobj.group()[1:-2])

		status = re.search(r"\[on\]", data, re.M)
		if status == None:
			volumeicon = " "
		else:
			volumeicon = " "
		volumestr = volumeicon + "{:3.0f}".format(volume) + "%"

		response = {'full_text': '', 'name': 'volume'}
		response['color'] = "#268bd2"
		response['full_text'] = volumestr
		response['cached_until'] = time() + 60
		return (0, response)
	def on_click(self, json, i3status_config, event):
		if event['button'] == 1:
			subprocess.Popen(["volume_ctl", "mute"])
		if event['button'] == 4:
			subprocess.Popen(["volume_ctl", "up"])
		if event['button'] == 5:
			subprocess.Popen(["volume_ctl", "down"])			
		subprocess.Popen(["killall", "-USR1", "py3status"])                    		