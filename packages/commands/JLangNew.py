import os

class JLangNew:
    def __init__(self):
        pass

    def make_new(self, project_name):
        os.mkdir(f'projects/{project_name}')
        main_file = open(f'projects/{project_name}/main.jlang', 'w')
        main_file.write('\nfunc main() {\n\tlet hello_str = "Hello, World!";\n\tprint(hello_str)\n}\n')
        main_file.close()
