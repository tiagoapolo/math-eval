#!/usr/bin/env

from syntax import Syntax

class Eval:

    def __init__(self):
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
        
    