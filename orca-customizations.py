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
    except Exception:
        print("Error in thread")
        traceback.print_exc()

# Starts the thread that connects to the NVDA Remote server
t = threading.Thread(target=try_run_thread)
t.daemon = True
t.start()

# Patch Orca functions
old_speak = SpeechServer._speak
old_speakCharacter = SpeechServer.speakCharacter
old_stop = SpeechServer.stop

def my_speak(self, text, acss, **kw):
    if text:
        transport.send(type="speak", sequence=text)
    return old_speak(self, text, acss, **kw)

def my_speakCharacter(self, character, acss=None):
    transport.send(type="speak", sequence=[character])
    return old_speakCharacter(self, character, acss)

def my_stop(self):
    transport.send(type="cancel")
    return old_stop(self)

SpeechServer._speak = my_speak
SpeechServer.speakCharacter = my_speakCharacter
SpeechServer.stop = my_stop

print("Orca patched")
