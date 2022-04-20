import sys

sys.path.append('./generated')

from generated.miniPythonLexer import *
from generated.miniPythonParser import *
from antlr4 import *
from antlr4.error.ErrorListener import *
from MyErrorListener import *
from AContextual import *


# Mostrar mensaje error proveniente del Lexer
class errorLexer(ErrorListener):

    def __init__(self):
        super(errorLexer, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print("ERROR de sintaxis en Lexer: ", "En la linea ", line, "columna ", column,
              "se reporta el siguiente error: ", msg)
        sys.exit()


# Mostrar Mensaje Error proveniente del Parser
class errorParser(ErrorListener):

    def __init__(self):
        super(errorParser, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print("ERROR de sintaxis en Parser: ", "En la linea ", line, "columna ", column,
              "se reporta el siguiente error: ", msg)
        # raise Exception("Oh no!!")
        sys.exit()


# Main para errores.
if __name__ == "__main__":
    input = FileStream('test.txt')
    lexer = miniPythonLexer(input)
    lexer._listeners = [errorLexer()]
    stream = CommonTokenStream(lexer)
    parser = miniPythonParser(stream)
    parser._listeners = [errorParser()]

    try:
        tokens = CommonTokenStream(lexer)
        parser = miniPythonParser(tokens)

        # manejo de errores
        errorListener = MyErrorListener()
        lexer.removeErrorListeners()
        lexer.addErrorListener(errorListener)
        parser.removeErrorListeners()
        parser.addErrorListener(errorListener)

        tree = parser.program()

        mv = AContextual
        mv.visit(tree)

        if errorListener.hasErrors() & mv.hasErrors():
            print("Compilación Exitosa!!!")
        else:
            print("Compilación Fallida!!!")
            if errorListener.hasErrors():
                print(errorListener.toString())
            if mv.hasErrors():
                print(mv.printErrors())
    except:
        e = RecognitionException
        print("No hay archivo")
        e.with_traceback()
