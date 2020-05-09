import sys
import os
import json

class JSONSerializer:
        SEP = B'\n'

        def serialize(self, type=None, **obj) -> bytes:
                obj['type'] = type
                data = json.dumps(obj).encode('UTF-8') + self.SEP
                return data

        def deserialize(self, data: bytes):
                obj = json.loads(data)
                return obj
