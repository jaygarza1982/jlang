from packages.parsing.AsmFile import AsmFile
from packages.utils.FuncArgExtractor import FuncArgExtractor

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
            func_args = line[func_len:len(line)-1]
            arg_extractor = FuncArgExtractor()
            func_args_list = arg_extractor.get_args(func_args)
            for func_arg in func_args_list:
                self.asm_file.code += f'push {func_arg}\n'
            # Call our function
            self.asm_file.code += f'call {possible_func}\n'
            # Clean the stack
            self.asm_file.code += f'add esp, {len(func_args_list) * 4}\n'