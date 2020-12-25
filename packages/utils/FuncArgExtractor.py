import re

class FuncArgExtractor:
    def __init__(self):
        pass

    # Returns array of function arguments
    # str, 6 would return ["str", 6]
    def get_args(self, all_args_str):
        arg_list = re.split(',\s*', all_args_str)

        # Items are to be pushed in reverse order
        arg_list.reverse()

        return arg_list