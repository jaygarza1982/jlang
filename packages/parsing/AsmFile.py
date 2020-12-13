
class AsmFile:
    def __init__(self):
        self.data = ''
        self.bss = ''
        self.code = ''

    def compile(self):
        return f'segment .data\n{self.data}\n\nsegment .bss\n{self.bss}\n\n{self.code}\n'
