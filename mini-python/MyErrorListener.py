from antlr4.error.ErrorListener import ErrorListener
from generated.miniPythonParser import *


class MyErrorListener(ErrorListener):

    errorMsgs = [""]

    def MyErrorListener(self):
        self.errorMsgs = [""]

    # Mostrar mensaje error proveniente del Lexer
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if recognizer in miniPythonParser:
            self.errorMsgs.insert("ERROR de sintaxis en Lexer: ", "En la linea ", line, "columna ", column,
                                  "se reporta el siguiente error: ", msg)
        elif recognizer in miniPythonParser:
            self.errorMsgs.insert("ERROR de sintaxis en Parser: ", "En la linea ", line, "columna ", column,
                                  "se reporta el siguiente error: ", msg)
        else:
            self.errorMsgs.insert("Other error")

    def hasErrors(self):
        return self.errorMsgs.__len__() > 0

    def toString(self):
        if not self.hasErrors():
            return "0 errores"
        builder = StringIO
        for s in self.errorMsgs:
            builder.writable("%s\n", s)  # verificar
        return builder.__str__(self)



