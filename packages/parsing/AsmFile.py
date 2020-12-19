
class AsmFile:
    def __init__(self):
        self.data = ''
        self.bss = ''
        self.code = ''

        # Store the function names defined within our assembly
        self._function_names = set()

    # TODO: Parse global, then add to the .data segment of the assembly
    # Store the global length in a map in this asm file to query later when accessing the variable
    def add_global(self, type, name, data):
        pass

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
