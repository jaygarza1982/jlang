from packages.parsing.AsmFile import AsmFile

class JLangLineEvaluator:
    def __init__(self, asm_file):
        self.asm_file = asm_file

    def evaluate(self, line):
        possible_func = line.split('(')[0]
        # Check for raw assembly
        if line.strip().startswith('ASM '):
            self.asm_file.code += line.strip()[4:] + '\n'
        # Check for predefined function calls
        elif self.asm_file.has_function(possible_func):
            # Get args from func and push onto stack
            func_len = len(f'{possible_func}(')
            func_arg = line[func_len:len(line)-1]
            self.asm_file.code += f'push {func_arg}\n'
            self.asm_file.code += f'call {possible_func}\n'