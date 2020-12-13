from packages.parsing.AsmFile import AsmFile
from packages.parsing.JLangPrintParser import JLangPrintParser

class JLangLineEvaluator:
    def __init__(self, asm_file):
        self.asm_file = asm_file

    def evaluate(self, line):
        if line.startswith('print'):
            print_parser = JLangPrintParser(self.asm_file)
            print_parser.parse(line)
