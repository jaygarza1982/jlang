from packages.utils.Splitter import Splitter

class JLangIncludeModifier:
    def __init__(self):
        pass

    def modify(self, project_dir, input_str):
        splitter = Splitter()
        lines = splitter.split(input_str)

        output_file_str = ''
        for i in range(len(lines)):
            line = lines[i]
            current_line = line.strip()
            print(line)

            # If our line includes the include keyword, include it in our output string
            if current_line.startswith('include:'):
                file_to_include = f'{project_dir}/{current_line.split(":")[1]}'
                print('file to include', file_to_include)
                output_file_str += open(file_to_include, 'r').read()
            # If our line does not contain include, append the current line to output
            else:
                output_file_str += current_line
            output_file_str += '\n'

        return output_file_str