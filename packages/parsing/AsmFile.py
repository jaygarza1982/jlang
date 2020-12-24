
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

        global_length = data.replace('"', '')
        self._globals[name] = {'data': data, 'length': len(data)}

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
