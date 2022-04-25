import sys

sys.path.append('./generated')

from AContextual import *
from MyErrorListener import *

# Main para errores.
if __name__ == "__main__":
    input = FileStream('test.txt')
    lexer = miniPythonLexer(input)

    try:
        tokens = CommonTokenStream(lexer)
        parser = miniPythonParser(tokens)

        parser._listeners = [MyErrorListener()]

        # manejo de errores
        errorListener = MyErrorListener()
        lexer.removeErrorListeners()
        lexer.addErrorListener(errorListener)
        parser.removeErrorListeners()
        parser.addErrorListener(errorListener)

        tree = parser.program()

        mv = AContextual()
        mv.visit(tree)

        if not (errorListener.hasError() and mv.hasErrors()):
            print("Compilación Exitosa!!!")
        else:
            print("Compilación Fallida!!!")
            if errorListener.hasError():
                errorListener.toString()
            if not mv.hasErrors():
                mv.printErrors()

    except RecognitionException:
        print("No hay archivo")
        # print(e.with_traceback())
        var = RecognitionException.__traceback__
