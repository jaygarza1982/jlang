from packages.parsing.JLangGlobalParser import JLangGlobalParser
from packages.parsing.JLangFunctionParser import JLangFunctionParser
from packages.parsing.JLangAsmModifier import JLangAsmModifier
from packages.parsing.JLangIncludeModifier import JLangIncludeModifier
from packages.parsing.JLangPreprocessors import JLangGlobalLen
from packages.parsing.AsmFile import AsmFile

class JLangCompiler:
    def __init__(self):
        pass
    
    def compile_jlang(self, project_dir, source_file):
        print(f'Compiling from source file {source_file}')

        source_file_open = open(source_file, 'r')
        input_str = source_file_open.read()
        source_file_open.close()

        # Include files within our initial file string
        include_modifier = JLangIncludeModifier()
        input_str = include_modifier.modify(project_dir, input_str)

        # Add pure assembly code to our compiled asm file
        # print(input_str)
        asm_parser = JLangAsmModifier()
        input_str = asm_parser.modify(input_str)
        print(input_str)

        asm_file = AsmFile()

        # Parse global variables
        global_parser = JLangGlobalParser(asm_file)
        global_parser.parse(input_str)

        # Preprocess global lengths after adding them to the asm file
        global_length_processor = JLangGlobalLen(asm_file)
        input_str = global_length_processor.preprocess(input_str)

        # Parse functions
        function_parser = JLangFunctionParser(asm_file)
        function_parser.parse(input_str)

        # At top of code, jump to the main function
        asm_file.code = 'jmp main\n\n' + asm_file.code

        return asm_file.compile()