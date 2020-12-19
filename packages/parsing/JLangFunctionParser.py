from packages.utils.Splitter import Splitter
from packages.parsing.JLangLineEvaluator import JLangLineEvaluator

class JLangFunctionParser:
    def __init__(self, asm_file):
        self.asm_file = asm_file

    def parse(self, input_str):
        splitter = Splitter()
        lines = splitter.split(input_str)

        for i in range(len(lines)):
            line = lines[i]

            if line.strip() != '':
                # print(line)
                current_line = line.strip()
                func_name = ''
                if current_line.startswith('func'):
                    # Get our function name
                    func_name = current_line.strip()
                    func_name = func_name[len('func'):].strip()
                    func_name = func_name.split('(')[0].strip()

                    # Add a function name to the set of functions
                    self.asm_file.add_function(func_name)

                    # Compile start of function in assembly
                    self.asm_file.code += f'{func_name}:\n'
                    self.asm_file.code += '\npush ebp\nmov ebp, esp\n\n'

                    # print('func name', func_name)

                    # Bracket loop
                    # Loop until we find balanced brackets
                    j = i
                    brackets = 0
                    while True:
                        current_line = lines[j].strip()

                        # print(current_line)

                        # Balance brackets
                        if current_line.endswith('{'):
                            brackets += 1
                        elif current_line.endswith('}'):
                            brackets -= 1
                        # If we are balanced, quit
                        if brackets == 0:
                            break

                        # Evaluate each line
                        evaluator = JLangLineEvaluator(self.asm_file)
                        evaluator.evaluate(current_line)

                        j += 1

                    self.asm_file.code += '\nmov esp, ebp\npop ebp\nret\n\n'
                    self.asm_file.code += f'{func_name}_end:\n'
