from packages.utils.Splitter import Splitter

class JLangAsmModifier:
    def __init__(self):
        pass

    def modify(self, input_str):
        splitter = Splitter()
        lines = splitter.split(input_str)

        output_str = ''
        for i in range(len(lines)):
            line = lines[i]
            current_line = line.strip()
            
            if current_line.startswith('ASM'):

                # print('func name', func_name)

                # Bracket loop
                # Loop until we find balanced brackets
                j = i
                brackets = 0
                while True:
                    current_line = lines[j].strip()
                    # Programmers can put ASM { or ASM\n{
                    # if not current_line.endswith('{'):
                            # print(current_line)

                        # Balance brackets
                    if current_line.endswith('{'):
                        brackets += 1
                    elif current_line.endswith('}'):
                        brackets -= 1
                    # If we are balanced, quit
                    if brackets == 0:
                        break

                    # Put each line into code
                    # if not current_line.endswith('{') and current_line.strip() != '':
                    #     self.asm_file.code += f'{current_line}\n'
                    #     # print('would put', current_line)

                    # Mark each line for assembly
                    if not current_line.strip().endswith('{') and current_line.strip() != '':
                        output_str += f'ASM {current_line}'
                    elif current_line.strip() != 'ASM {':
                        output_str += current_line

                    output_str += '\n'
                        # self.asm_file.code += f'{current_line}\n'
                        # # print('would put', current_line)

                    j += 1

            else:
                output_str += current_line
                output_str += '\n'

        return output_str