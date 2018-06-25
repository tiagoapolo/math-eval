# class Var:
#
#     def __init__(self):
#         self.variables = []
#
#     def appendVar(self, value):
#         self.variables.append(value)
#
#     def getVar(self, name):
#         for item in self.variables:
#             if item:
#                 return item
#             else:
#                 return None

class Var:
    # Here will be the instance stored.
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Var.__instance == None:
            Var()
        return Var.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Var.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Var.__instance = self
            self.variables = []

    def appendVar(self, value):
        if self.getVar(value[0]):
            raise ValueError('Variable already declared')
        else:
            self.variables.append(value)

    def getVar(self, name):
        var = None

        for item in self.variables:
            if item[0] == name:
                var = item

        return var