import json

class Params:

    def __init__(self, json_path):
        self.update(json_path)

    def update(self, json_path):
        """Load parameters from json file"""
        with open(json_path) as f:
            params = json.load(f)
            self.__dict__.update(params)