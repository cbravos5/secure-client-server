#!/usr/bin/env python3

import json


class Serializer:
    def serialize(self, data):
        return json.dumps(data)

    def deserialize(self, json_string):
        return json.loads(json_string)
