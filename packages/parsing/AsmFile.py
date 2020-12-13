
class AsmFile:
    def __init__(self):
        self.data = ''
        self.bss = ''
        self.code = ''

    # TODO: Parse global, then add to the .data segment of the assembly
    # Store the global length in a map in this asm file to query later when accessing the variable
    def add_global(self, type, name, data):
        pass

    def compile(self):
        return f'segment .data\n{self.data}\n\nsegment .bss\n{self.bss}\n\nsegment .text\n\tglobal main\n\n{self.code}\n'
