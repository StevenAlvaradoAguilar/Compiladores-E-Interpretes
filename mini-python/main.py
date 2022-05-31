import sys
import os

from antlr4 import FileStream, CommonTokenStream

sys.path.append('./generated')

from AContextual import *
from MyErrorListener import *
from codeGen import codeGen

# Main para errores.
if __name__ == "__main__":
    # input = FileStream('test.txt')
    # input = FileStream('pruebaContextual.txt')
    # input = FileStream('test2.txt')
    input = FileStream('Tarea5.txt')
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
        v = codeGen()
        mv.visit(tree)
        v.visit(tree)

        os.system("MiniPY Tarea5.txt")

        if (not errorListener.hasError()) and (not mv.hasErrors()):
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
        var = RecognitionException.__traceback__()
