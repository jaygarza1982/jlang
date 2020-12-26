from packages.parsing.JLangCompiler import JLangCompiler
from packages.commands.JLangMake import JLangMake
import os

class JLangMakeRun:
    def __init__(self):
        pass

    def make_run(self, project_name):
        # First make the project
        jlang_make = JLangMake()
        jlang_make.make(project_name)

        # Run our project
        os.system(f'./projects/{project_name}/{project_name}')