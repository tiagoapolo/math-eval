#!/usr/bin/env

class Tokenizer:
    def __init__(self, typeValue, lex=''):
        self.type = typeValue
        self.lex = lex
    
    def getType(self):
        return self.type

    def getLex(self):
        return self.lex