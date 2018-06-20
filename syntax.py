#!/usr/bin/env

from lexer import Lexer

class Syntax:

    def __init__(self,expression):
        self.lexer = Lexer(expression)
    
    
    def parse(self):
    
        self.token = self.lexer.nextToken()

        # try:
        self.ast = self.exp()
        
        # except ValueError:
        #     print("error!")
        
        if(self.ast):
    
            token = self.read("EOF")

            if(token):            
                return self.ast            
            else:            
                raise ValueError("Error Processing Request")

    def term(self):

        expression = self.factor()

        if(expression):
        
            while(self.token.getType() == "*" or self.token.getType() == "/"):            
                operator = self.read(self.token.getType())

                if(operator):                
                    exp = self.factor()

                    if(exp):                    
                        expression = [ "Times" if operator.getType() == "*" else "Division", expression, exp ]
                    
                    else:                    
                        raise ValueError("After a operator.getType() must have a expression")                    
                
                else:
                
                    raise ValueError("Could not read the operator self.token.getType() ")                            
            return expression
        else:        
            raise ValueError("A expression must be provided")
        
                    
            
    def exp(self):        

        expression = self.term()

        if(expression):
        
            while(self.token.getType() == "+" or self.token.getType() == "-"):
            
                operator = self.read(self.token.getType())

                if(operator):                
                    exp = self.term()

                    if(exp):                    
                        expression = [ "Plus" if operator.getType() == "+" else "Minus", expression, exp ]

                    else:                    
                        raise ValueError("After the operator operator.getType() must have a expression")                                
                else:                
                    raise ValueError("Could not read the operator self.token.getType() ")
                            
            return expression
        
        else:        
            raise ValueError("A expression must be provided")


    def factor(self):

        if(self.token.getType() == "-"):        
            operator = self.read("-")

            if(operator):
            
                return [ "Unary", self.factor()]            
            else:            
                raise ValueError("After unary operand, should have a expression")            
        
        else:

            return self.power()
        
    

    def power(self):

        expression = self.primary()

        if(expression):        
            while(self.token.getType() == "^"):
            
                operator = self.read("^")
                
                if(operator):                
                    exp = self.factor()

                    if(exp):                    
                        expression = ["Power",expression,exp]                    
                    else:                    
                        raise ValueError("After a ^ should have a expression")                    
                
                else:                
                    raise ValueError("Could not read operator ^")
                            
            return expression
        
        else:        
            raise ValueError("Expression must be provided")
        
    def primary(self):


        if(self.token.getType() == "Number"):

            numberToken = self.read("Number")
            if(numberToken):            
                return ["Number",numberToken.getLex()]            
            else:
                raise ValueError("Error processing a number on the tree")
            
        
        elif(self.token.getType() == "("):        
            
            bracketToken = self.read("(")
            
            if(bracketToken):            
                expression = self.exp()

                if(expression):                
                    bracketToken = self.read(")")

                    if(bracketToken):                    
                        return expression                    
                    else:                    
                        raise ValueError("Brackets should be balanced")
                    
                
                else:                
                    raise ValueError("After a ( should have another expression")                
            
            else:            
                raise ValueError("Error trying to read ( char")
            

    def read(self, typeValue):
    
        if(self.token.getType() == typeValue):
        
            oldToken = self.token
            self.token = self.lexer.nextToken()

            return oldToken
        
        else:
            raise ValueError("Cannot read operator type %s Current operator is %s" % typeValue, self.token.getType())