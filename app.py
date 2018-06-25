#!/usr/bin/env
import sys

from eval import Eval
from insideVariables import Var

var = Var()
evaluator = Eval()

print('\n========== MATH EXPRESSION ==========\n')
while True:
    print('To exit the program write \'exit\'\n')
    exp = input('Enter your math expression: ')
    if exp == 'exit':
        sys.exit()
    try:
        result = evaluator.parse(exp)
        print(result)
    except ValueError as err:
        print('Error: '+str(err))
        sys.exit()
