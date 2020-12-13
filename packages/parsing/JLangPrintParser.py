from packages.utils.Splitter import Splitter

class JLangPrintParser:
    def __init__(self, asm_file):
        self.asm_file = asm_file

    def parse(self, input_str):
        # Get what is inside the ()
        to_print = input_str.strip()
        to_print = to_print[len('print('):]
        to_print = to_print[:len(to_print) - 1]

        # print('print var', to_print)
        self.asm_file.code += '\tmov eax, 4\n'
        self.asm_file.code += '\tmov ebx, 1\n'
        self.asm_file.code += f'\tmov ecx, {to_print}\n'
        self.asm_file.code += f'\tmov edx, 32\n'
        self.asm_file.code += '\tint 0x80\n'