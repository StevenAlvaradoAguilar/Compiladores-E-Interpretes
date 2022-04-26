from io import StringIO

from antlr4.error.ErrorListener import *

from generated.miniPythonParser import miniPythonParser
from generated.miniPythonLexer import miniPythonLexer


class MyErrorListener(ErrorListener):

    def __init__(self):

        self.errorMsgs = []

    def syntaxError(self, recognizer,
                    offendingSymbol,
                    line,
                    column,
                    msg,
                    e):
        if isinstance(recognizer, miniPythonParser):
            self.errorMsgs.append("PARSER ERROR - line " + str(line))
            print("Error del parser en linea " + str(line))
        elif isinstance(recognizer, miniPythonLexer):
            self.errorMsgs.append("LEXER ERROR - line " + str(line))
            print("Error del lexer en linea " + str(line) + " columna " + str(column + 1))
        else:
            self.errorMsgs.append("OTHER ERROR!!!")
            # print ("Otro error")

    def hasError(self):
        return len(self.errorMsgs) > 0

    def toString(self):
        if not self.hasError:
            return "0 errors"
        print(len(self.errorMsgs))
        for i in self.errorMsgs:
            print(i)

