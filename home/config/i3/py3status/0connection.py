import socket
from time import time
REMOTE_SERVER = "www.google.de"
def is_connected():
    try:
        host = socket.gethostbyname(REMOTE_SERVER)
        s = socket.create_connection((host, 80), 2)
        return True
    except:
        pass
    return False

class Py3status:
    def connection(self, i3status_output_json, i3status_config):
        if is_connected():
            text = ""
        else:
            text = ""

        response = {'full_text': '', 'name': 'connection'}
        response['color'] = "#b58900"
        response['full_text'] = text;
        response['cached_until'] = time() + 60
        return (0, response)
