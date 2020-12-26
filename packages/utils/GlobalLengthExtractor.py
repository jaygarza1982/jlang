import re

from packages.utils.IntegerParser import IntegerParser


class GlobalLengthExtractor:
    def __init__(self):
        pass

    def get_length(self, variable_data):
        # global_length = data.replace('"', '')
        global_length = 0
        # Split data by commas that are before quotes "Hello, World!(", )10
        data_comma_split = re.split('"\s*,\s*', variable_data)
        int_parser = IntegerParser()
        # Loop through each comma separated item
        for data_item in data_comma_split:
            if int_parser.is_int(data_item):
                global_length += 1
            else:
                # Item is not an int, strip quotes and get length of string
                string = data_item.replace('"', '')
                global_length += len(string)

        return global_length