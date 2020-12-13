from packages.parsing.JLangCompiler import JLangCompiler

class JLangMake:
    def __init__(self):
        pass

    def make(self, project_name):
        print(f'Parsing {project_name}')

        compiler = JLangCompiler()
        compiled = compiler.compile_jlang(f'projects/{project_name}/main.jlang')

        print(compiled)