import os

class JLangNew:
    def __init__(self):
        pass

    def make_new(self, project_name):
        # Make a new folder for the new project
        os.mkdir(f'projects/{project_name}')

        template_file = open('jlang/hello-world.jlang', 'r')
        main_file = open(f'projects/{project_name}/main.jlang', 'w')

        # Copy contents of the template into the new project folder
        main_file.write(template_file.read())
        
        template_file.close()
        main_file.close()
