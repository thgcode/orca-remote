import sys
import os

# Orca Remote Settings
YOUR_ORCA_SCRIPTS_FOLDER = os.path.expanduser("~/.local/share/orca/orca-scripts")
YOUR_NVDAREMOTE_SERVER_ADDRESS = "host"
YOUR_NVDAREMOTE_SERVER_PORT = 6837
YOUR_NVDAREMOTE_KEY = "key"

# Make the NVDA Remote modules importable
sys.path.insert(0, YOUR_ORCA_SCRIPTS_FOLDER)

from orca.speechdispatcherfactory import SpeechServer
from serializer import JSONSerializer
from transport import RelayTransport
import traceback
import threading

mySerializer = JSONSerializer()

transport = RelayTransport(mySerializer, (YOUR_NVDAREMOTE_SERVER_ADDRESS, YOUR_NVDAREMOTE_SERVER_PORT), channel=YOUR_NVDAREMOTE_KEY, connection_type="slave")

def try_run_thread():
    try:
        transport.run()
    except exception:
        print("Error in thread")
        traceback.print_exc()

# Starts the thread that connects to the NVDA Remote server
t = threading.Thread(target=try_run_thread)
t.daemon = True
t.start()

# Patch Orca functions
old_speak = SpeechServer.speak
old_stop = SpeechServer.stop

def my_speak(self, text=None, acss=None, interrupt=True):
    if text:
        transport.send(type="speak", sequence=text)
    return old_speak(self, text, acss, interrupt)

def my_stop(self):
    transport.send(type="cancel")
    return old_stop(self)

SpeechServer.speak = my_speak
SpeechServer.stop = my_stop

print("Orca patched")
