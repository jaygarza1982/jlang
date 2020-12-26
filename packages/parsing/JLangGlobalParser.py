from packages.utils.Splitter import Splitter
from packages.parsing.AsmFile import AsmFile

import re

class JLangGlobalParser:
    def __init__(self, asm_file):
        self.asm_file = asm_file

    def parse(self, input_str):
        splitter = Splitter()
        lines = splitter.split(input_str)

        for line in lines:
            if line.strip() != '':
                # print(line)
                current_line = line.strip()
                if current_line.startswith('global'):
                    # Remove the global symbol
                    current_line = current_line[len('global'):].strip()
                    
                    # Check for type
                    data_type = ''
                    data_code_type = ''
                    if current_line.startswith('byte'):
                        data_type = 'db'
                        data_code_type = 'byte'
                    elif current_line.startswith('int'):
                        data_type = 'dd'
                        data_code_type = 'int'
                    else:
                        print(f'Compiling failed near "{current_line}". Exiting with error code -1 Global Parser error.')
                        exit(-1)

                    # Remove the type
                    current_line = current_line[len(data_code_type):].strip()

                    # Get variable and assignment
                    current_split = re.split('\s?=\s?', current_line)

                    # Add global to assembly file globals
                    self.asm_file.add_global(current_split[0], current_split[1])

                    # Append to the assembly
                    self.asm_file.data += f'\t{current_split[0]} {data_type} {current_split[1]}\n'
