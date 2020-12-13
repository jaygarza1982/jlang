from packages.parsing.JLangGlobalParser import JLangGlobalParser
from packages.parsing.JLangFunctionParser import JLangFunctionParser
from packages.parsing.AsmFile import AsmFile

class JLangCompiler:
    def __init__(self):
        pass
    
    def compile_jlang(self, source_file):
        print(f'Compiling from source file {source_file}')

        source_file_open = open(source_file, 'r')
        input_str = source_file_open.read()
        source_file_open.close()

        asm_file = AsmFile()

        # Parse global variables
        global_parser = JLangGlobalParser(asm_file)
        global_parser.parse(input_str)

        # Parse functions
        function_parser = JLangFunctionParser(asm_file)
        function_parser.parse(input_str)

        # At top of code, jump to the main function
        asm_file.code = 'jmp func_main_start\n\n' + asm_file.code

        return asm_file.compile()