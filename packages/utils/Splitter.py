import re

class Splitter:
    def __init__(self):
        pass

    def split(self, input_str):
        return re.split('(\n+|\r+)', input_str)