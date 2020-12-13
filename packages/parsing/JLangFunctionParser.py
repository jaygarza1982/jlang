from packages.utils.Splitter import Splitter

class JLangFunctionParser:
    def __init__(self, asm_file):
        self.asm_file = asm_file

    def parse(self, input_str):
        splitter = Splitter()
        lines = splitter.split(input_str)

        for line in lines:
            if line.strip() != '':
                # print(line)
                current_line = line.strip()
                if current_line.startswith('func'):
                    print(current_line)