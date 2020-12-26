from packages.utils.Splitter import Splitter

class JLangGlobalLen:
    def __init__(self, asm_file):
        self.asm_file = asm_file

    def preprocess(self, input_str):
        splitter = Splitter()
        lines = splitter.split(input_str)

        processed = ''

        for line in lines:
            # Compute each possibility of a global len replacement
            global_names = self.asm_file.get_global_names()

            replaced = False

            for global_name in global_names:
                possible_global_len = f'jlang.global_len({global_name})'
                if possible_global_len in line:
                    processed += line.replace(possible_global_len, str(self.asm_file.get_global(global_name)['length']))
                    replaced = True

            # Add line back to processed even if we did not replace
            if not replaced:
                processed += line

        return processed
