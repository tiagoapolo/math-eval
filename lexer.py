#!/usr/bin/env
from tokenizer import Tokenizer
from insideVariables import Var

class Lexer:
    def __init__(self, expression):

        self.tokensPos = 0
        self.expression = expression
        self.tokens = []

        # try:
        self.tokenizer()
        # except ValueError:
        #     raise ValueError


    def tokenizer(self):
        if not self.expression:
            raise ValueError("Empty expression! Cannot process!")

        expressionLen =  len(self.expression)
        i = 0
        number = ''
        current = ''

        while (i < expressionLen):
            
            current = self.expression[i]

            if (current == ' ' or current == '\n' or current == '\t'):
                i = i + 1
                continue
                
            elif current.isnumeric():

                while (current.isnumeric()):
                    number = number + current
                    i = i + 1
                    if (i >= expressionLen):
                        break
                    current = self.expression[i]

                if (current == '.'):

                    number = number + current
                    i = i + 1
                    current = self.expression[i]
                    
                    if current.isnumeric():
                        while (current.isnumeric()):
                            number = number + current
                            i = i + 1
                            if (i >= expressionLen):
                                break
                            current = self.expression[i]
                    else:
                        raise ValueError("FLOAT USAGE: [0-9].[0-9][0-9]* ")

                token = Tokenizer('Number', float(number))

                i = i - 1
                number = ''
            
            elif current == '+':
                token = Tokenizer('+')

            elif current == '-':
                token = Tokenizer('-')

            elif current == '*':
                token = Tokenizer('*')
            
            elif current == '/':
                token = Tokenizer('/')
                
            elif current == '^':
                token = Tokenizer('^')

            elif current == '(':
                token = Tokenizer('(')
            
            elif current == ')':
                token = Tokenizer(')')

            elif current == '@':

                variable = ''
                i = i + 1
                current = self.expression[i]

                while (current.isalpha()):
                    variable = variable + current
                    i = i + 1
                    if (i >= expressionLen):
                        break
                    current = self.expression[i]

                # if :
                var = Var.getInstance()
                val = var.getVar(variable)
                if val == None:
                    raise ValueError('Variable => ' + variable + ' not declared')

                token = Tokenizer('Number', val[1])
                i = i - 1

            elif current.isalpha():
                variable = ''
                while (current.isalpha()):
                    variable = variable + current
                    i = i + 1
                    current = self.expression[i]

                token = Tokenizer('Variable', variable)
                i = i - 1

            elif current == '=':
                token = Tokenizer('=')

            else:
                raise ValueError("INVALID TOKEN => %s" % current)

            i = i + 1
            if token:
                self.tokens.append(token)

    def nextToken(self):

        pos = self.tokensPos

        if pos == len(self.tokens):
            return Tokenizer('EOF')
        
        self.tokensPos = self.tokensPos + 1
        return self.tokens[pos]
