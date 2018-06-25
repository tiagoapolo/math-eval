#!/usr/bin/env

from syntax import Syntax
from insideVariables import Var

class Eval:

    def __init__(self):
        # self.variables = []
        pass
    
    def parse(self, expression):
    
        self.expression = expression
        syntactic = Syntax(self.expression)

        # try:
        self.ast = syntactic.parse()
        
        # except ValueError:
            # print("erro!")
        
        # try:        
        return self.evaluate(self.ast)
        
        # except ValueError:        
        # print("erro!2")
        
    
    def evaluate(self, ast):
    
        if(ast[0] == 'Number'):
            return ast[1]
        elif(ast[0] == 'Plus'):
            return self.evaluate(ast[1]) + self.evaluate(ast[2])
        
        elif(ast[0] == 'Minus'):
            return self.evaluate(ast[1]) -self.evaluate(ast[2])
        
        elif(ast[0] == 'Times'):
            return self.evaluate(ast[1]) * self.evaluate(ast[2])
        
        elif(ast[0] == 'Division'):
            if(ast[2][1] == 0):
                raise ValueError("Division by 0")

            return self.evaluate(ast[1]) / self.evaluate(ast[2])
        
        elif(ast[0] == 'Power'):
            return pow(self.evaluate(ast[1]),self.evaluate(ast[2]))
        
        elif(ast[0] == 'Unary'):
            return (0 - self.evaluate(ast[1]))

        elif ast[0] == 'Variable':
            return ast[1]

        elif(ast[0] == 'Attribute'):
            var = Var.getInstance()
            var.appendVar([self.evaluate(ast[1]), self.evaluate(ast[2])])
            # self.variables.append([self.evaluate(ast[1]), self.evaluate(ast[2])])
            return str(ast[1][1])+"="+str(ast[2][1])
