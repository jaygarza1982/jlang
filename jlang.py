import sys
import os
from packages.commands.JLangMake import JLangMake
from packages.commands.JLangNew import JLangNew

if sys.argv[1] == 'jlang-new':
    print('Making new project', sys.argv[2])
    jlang_new = JLangNew()
    jlang_new.make_new(sys.argv[2])
elif sys.argv[1] == 'make':
    print('Compiling project', sys.argv[2])
    make = JLangMake()
    make.make(sys.argv[2])
else:
    print(f'Invalid command "{sys.argv[1]}" Please enter a valid command e.g jlang-new, make')