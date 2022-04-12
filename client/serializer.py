#!/usr/bin/env python3

import json


class Serializer:
    def serialize(self, action, data):
        formatted_data = {
            'action': action,
            'data': data
        }
        return json.dumps(formatted_data)

    def deserialize(self, json_string):
        return json.loads(json_string)
