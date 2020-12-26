from packages.utils.GlobalLengthExtractor import GlobalLengthExtractor

class AsmFile:
    def __init__(self):
        self.data = ''
        self.bss = ''
        self.code = ''

        # Store the function names defined within our assembly
        self._function_names = set()
        # Store globals that are in the assembly file
        self._globals = dict()

    def add_global(self, name, data):
        if name in self._globals:
            print(f'Variable redefined error! Variable "{name}" already defined! Aborting.')
            exit(-3)
        
        global_length_ext = GlobalLengthExtractor()
        global_length = global_length_ext.get_length(data)

        self._globals[name] = {'data': data, 'length': global_length}

    def get_global(self, name):
        if name not in self._globals:
            print(f'Global {name} does not exist! Aborting!.')
            exit(-4)
        
        return self._globals[name]

    def get_global_names(self):
        return self._globals.keys()

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
