from packages.utils.IntegerParser import IntegerParser

class AsmFile:
    def __init__(self):
        self.data = ''
        self.bss = ''
        self.code = ''

        # Store the function names defined within our assembly
        self._function_names = set()
        # Store globals that are in the assembly file
        self._globals = dict()

    # TODO: Parse global, then add to the .data segment of the assembly
    # Store the global length in a map in this asm file to query later when accessing the variable
    def add_global(self, name, data):
        if name in self._globals:
            print(f'Variable redefined error! Variable "{name}" already defined! Quitting.')
            exit(-3)

        # global_length = data.replace('"', '')
        global_length = 0
        # Split data by commas
        data_comma_split = data.split(',')
        int_parser = IntegerParser()
        # Loop through each comma separated item
        for data_item in data_comma_split:
            if int_parser.is_int(data_item):
                global_length += 1
            else:
                # Item is not an int, strip quotes and get length of string
                string = data_item.replace('"', '')
                global_length += len(string)

        self._globals[name] = {'data': data, 'length': global_length}

    def add_function(self, name):
        # Stop compiling if a function name is already in the function names
        if name in self._function_names:
            print(f'!!!Function name "{name}" is already declared. Exiting with error code -2.')
            exit(-2)
        self._function_names.add(name)
        print('added func', name)

    def has_function(self, name):
        return name in self._function_names

    def compile(self):
        return f'segment .data\n{self.data}\n\nsegment .bss\n{self.bss}\n\nsegment .text\n\tglobal main\n\n{self.code}\n'
