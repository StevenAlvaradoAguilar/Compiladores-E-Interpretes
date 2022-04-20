import sys

from antlr4.Recognizer import Recognizer
from antlr4.error.ErrorListener import ErrorListener
from generated.miniPythonParser import *


class MyErrorListener(ErrorListener):

    # Mostrar mensaje error proveniente del Lexer
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print("ERROR de sintaxis en Lexer: ", "En la linea ", line, "columna ", column,
              "se reporta el siguiente error: ", msg)
        sys.exit()

    # Mostrar Mensaje Error proveniente del Parser
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print("ERROR de sintaxis en Parser: ", "En la linea ", line, "columna ", column,
              "se reporta el siguiente error: ", msg)
        # raise Exception("Oh no!!")
        sys.exit()

    def hasErrors(self):
        return self.errorMsgs.size() > 0


