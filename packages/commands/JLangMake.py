from packages.parsing.JLangCompiler import JLangCompiler

import os

class JLangMake:
    def __init__(self):
        pass

    def make(self, project_name):
        print(f'Parsing {project_name}')

        compiler = JLangCompiler()
        compiled = compiler.compile_jlang(f'projects/{project_name}/main.jlang')

        print(compiled)

        asm_file_path = f'projects/{project_name}/{project_name}.asm'
        folder_path = f'projects/{project_name}'

        # Write the assembly to a file
        jlang_asm_file = open(f'{asm_file_path}', 'w')
        jlang_asm_file.write(compiled)
        jlang_asm_file.close()

        # Assemble the project
        os.system(f'nasm -f elf {asm_file_path}')
        os.system(f'gcc -m32 {folder_path}/{project_name}.o -o {folder_path}/{project_name}')
