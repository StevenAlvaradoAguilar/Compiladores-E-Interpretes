from generated.miniPythonParser import *
from generated.miniPythonVisitor import *


class codeGen(miniPythonVisitor):
    class Instr:
        def __init__(self, i, a):
            self.instr = i
            self.arg = a

    def __init__(self):
        self.codigo = []
        self.instActual = 0
        self.variablesLocalesDefinidas = []

    def generate(self, instr, arg):
        self.codigo.append(codeGen.Instr(instr, arg))
        self.instActual += 1

    def printCode(self):
        print("----- CODIGO GENERA ------\n")
        for x in self.codigo:
            print(x.instr, end='')
            if (x.arg):
                print(" " + x.arg)
            else:
                print(" ")

    def agregarVariableDefinida(self, nombre, lista):
        if (self.buscarVariableDefinida(nombre,lista) == False):
            lista.append(nombre)

    def buscarVariableDefinida(self, nombre, lista):
        for v in lista:
            if v == nombre:
                return True
        return False

    # Visit a parse tree produced by miniPythonParser#programMP.
    def visitProgramMP(self, ctx: miniPythonParser.ProgramMPContext):
        self.visitChildren(ctx)
        self.printCode()
        return self.codigo

    # Visit a parse tree produced by miniPythonParser#statementMP.
    def visitStatementMP(self, ctx: miniPythonParser.StatementMPContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#defStatementMP.
    def visitDefStatementMP(self, ctx: miniPythonParser.DefStatementMPContext):
        self.generate("DEF", ctx.IDENTIFIER().getText())
        if(ctx.argList()):
            self.visit(ctx.argList())

        # Acá hay algo malo se debe de verificar el return value y return
        self.visit(ctx.sequence())
        if(ctx.IDENTIFIER().getText() == "Main"):
            self.generate("END", None)
        else:
            self.generate("RETURN", None)
        self.variablesLocalesDefinidas = []
        return None

    # Visit a parse tree produced by miniPythonParser#argListMP.
    def visitArgListMP(self, ctx: miniPythonParser.ArgListMPContext):
        self.visitChildren(ctx)
        if(ctx.IDENTIFIER() != None):
            self.generate("PUSH_LOCAL", ctx.IDENTIFIER().getText())
            self.generate("LOAD_GLOBAL", ctx.IDENTIFIER())
            self.generate("CALL_FUNCTION", ctx.IDENTIFIER())
            self.agregarVariableDefinida(ctx.IDENTIFIER().getText(), self.variablesLocalesDefinidas)
        return None

    # Visit a parse tree produced by miniPythonParser#moreArgsMP.
    def visitMoreArgsMP(self, ctx: miniPythonParser.MoreArgsMPContext):
        for i in ctx.IDENTIFIER():
            self.generate("PUSH_LOCAL", i.getText())
            self.agregarVariableDefinida(i.getText(), self.variablesLocalesDefinidas)
        return None

    # Visit a parse tree produced by miniPythonParser#ifStatementMP.
    def visitIfStatementMP(self, ctx: miniPythonParser.IfStatementMPContext):
        self.visitChildren(ctx)
        return

    # Visit a parse tree produced by miniPythonParser#whileStatementMP.
    def visitWhileStatementMP(self, ctx: miniPythonParser.WhileStatementMPContext):
        self.visitChildren(ctx)
        return

    # Visit a parse tree produced by miniPythonParser#forStatementMP.
    def visitForStatementMP(self, ctx: miniPythonParser.ForStatementMPContext):
        self.visitChildren(ctx)
        return

    # Visit a parse tree produced by miniPythonParser#returnStatementMP.
    def visitReturnStatementMP(self, ctx: miniPythonParser.ReturnStatementMPContext):
        self.visit(ctx.expression())
        self.generate("RETURN_VALUE", None)
        return None

    # Visit a parse tree produced by miniPythonParser#printStatementMP.
    def visitPrintStatementMP(self, ctx: miniPythonParser.PrintStatementMPContext):
        self.visit(ctx.expression())
        self.generate("LOAD_GLOBAL", "print")
        self.generate("CALL_FUNCTION", "1")
        return None

    # Visit a parse tree produced by miniPythonParser#assignStatementMP.
    def visitAssignStatementMP(self, ctx: miniPythonParser.AssignStatementMPContext):
        if (self.buscarVariableDefinida(ctx.IDENTIFIER().getText(), self.variablesLocalesDefinidas) == False):
            self.generate("PUSH_LOCAL", ctx.IDENTIFIER().getText())  # NO DEBERÍA HACERSE SIEMPRE EL PUSH
            self.agregarVariableDefinida(ctx.IDENTIFIER().getText(), self.variablesLocalesDefinidas)
        self.visit(ctx.expression())
        self.generate("STORE_FAST", ctx.IDENTIFIER().getText())
        return None

    # Visit a parse tree produced by miniPythonParser#functionCallStatementMP.
    def visitFunctionCallStatementMP(self, ctx: miniPythonParser.FunctionCallStatementMPContext):
        cant_params = 0
        if (ctx.expressionList()):
            cant_params = self.visit(ctx.expressionList())
        self.generate("LOAD_GLOBAL", str(cant_params))
        self.generate("CALL_FUNCTION", str(cant_params))
        self.visit(ctx.primitiveExpression())
        return None

    # Visit a parse tree produced by miniPythonParser#expressionStatementMP.
    def visitExpressionStatementMP(self, ctx: miniPythonParser.ExpressionStatementMPContext):
        self.visit(ctx.expressionList())
        return None

    # Visit a parse tree produced by miniPythonParser#sequenceMP.
    def visitSequenceMP(self, ctx: miniPythonParser.SequenceMPContext):
        self.visitChildren(ctx)
        return

    # Visit a parse tree produced by miniPythonParser#moreStatementsMP.
    def visitMoreStatementsMP(self, ctx: miniPythonParser.MoreStatementsMPContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#expression.
    def visitExpression(self, ctx: miniPythonParser.ExpressionContext):
        self.visit(ctx.additionExpression())
        self.visit(ctx.comparison())
        return None

    # Visit a parse tree produced by miniPythonParser#comparisonMP.
    def visitComparisonMP(self, ctx: miniPythonParser.ComparisonMPContext):
        self.visitChildren(ctx)
        return None

    # Visit a parse tree produced by miniPythonParser#additionExpressionMP.
    def visitAdditionExpressionMP(self, ctx: miniPythonParser.AdditionExpressionMPContext):
        self.visit(ctx.multiplicationExpression())
        self.visit(ctx.additionFactor())
        return None

    # Visit a parse tree produced by miniPythonParser#additionFactorMP.
    def visitAdditionFactorMP(self, ctx: miniPythonParser.AdditionFactorMPContext):
        '''self.visit(ctx.getChild(0))
        i = 1
        while i < len(ctx.children):
            oper = ctx.children[i]
            i += 1
            self.visit(ctx.getChild(i))
            if (oper.getText() == "+"):
                self.generate("BINARY_ADD", None)
            elif (oper.getText() == "-"):
                self.generate("BINARY_SUBSTRACT", None)
            i += 1

        return None
        '''
        listaSimbolos = []
        listaExpresiones = []
        for simboloIngresado in ctx.getChildren():
            if (simboloIngresado.getText() == "+"):
                listaSimbolos.append(simboloIngresado.getText())
            elif (simboloIngresado == "-"):
                listaSimbolos.append(simboloIngresado.getText())
            else:
                listaExpresiones.append(simboloIngresado.getText())

        contador = 0
        for expresiones in listaExpresiones:
            self.visit(ctx.multiplicationExpression()[contador])
            if (listaSimbolos[contador] == "+"):
               self.generate("BINARY_ADD", None)
            elif (listaSimbolos[contador] == "-"):
                self.generate("BINARY_SUBSTRACT", None)
            contador += 1
        return None

    # Visit a parse tree produced by miniPythonParser#multiplicationExpressionMP.
    def visitMultiplicationExpressionMP(self, ctx: miniPythonParser.MultiplicationExpressionMPContext):
        self.visit(ctx.elementExpression())
        self.visit(ctx.multiplicationFactor())
        return None

    # Visit a parse tree produced by miniPythonParser#multiplicationFactorMP.
    def visitMultiplicationFactorMP(self, ctx: miniPythonParser.MultiplicationFactorMPContext):
        """self.visit(ctx.getChild(0))
        i = 1
        while i < len(ctx.children):
            oper = ctx.children[i]
            i += 1
            self.visit(ctx.getChild(i))
            # generar operación
            if (oper.getText() == "*"):
                self.generate("BINARY_MULTIPLY", None)
            elif (oper.getText() == "/"):
                self.generate("BINARY_DIVIDE", None)
            i += 1

        return None
        """

        listaSimbolos = []
        listaExpresiones = []
        for simboloIngresado in ctx.getChildren():
            if (simboloIngresado.getText() == "*"):
                listaSimbolos.append(simboloIngresado.getText())
            elif (simboloIngresado == "/"):
                listaSimbolos.append(simboloIngresado.getText())
            else:
                listaExpresiones.append(simboloIngresado.getText())

        contador = 0
        for expresiones in listaExpresiones:
            self.visit(ctx.elementExpression()[contador])
            if (listaSimbolos[contador] == "*"):
                self.generate("BINARY_MULTIPLY", None)
            elif (listaSimbolos[contador] == "/"):
                self.generate("BINARY_DIVIDE", None)
            contador += 1
        return None

    # Visit a parse tree produced by miniPythonParser#elementExpressionMP.
    def visitElementExpressionMP(self, ctx: miniPythonParser.ElementExpressionMPContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#elementAccessMP.
    def visitElementAccessMP(self, ctx: miniPythonParser.ElementAccessMPContext):
        self.visitChildren(ctx)
        return

    # Visit a parse tree produced by miniPythonParser#expressionListMP.
    def visitExpressionListMP(self, ctx: miniPythonParser.ExpressionListMPContext):
        self.visitChildren(ctx)
        return

    # Visit a parse tree produced by miniPythonParser#moreExpressionsMP.
    def visitMoreExpressionsMP(self, ctx: miniPythonParser.MoreExpressionsMPContext):
        for e in ctx.expression():
            self.visit(e)
        return len(ctx.expression())

    # Visit a parse tree produced by miniPythonParser#primitiveExpressionMP.
    def visitPrimitiveExpressionMP(self, ctx: miniPythonParser.PrimitiveExpressionMPContext):
        if(ctx.expressionList() == ctx.IDENTIFIER()):
            self.generate("LOAD_CONST", ctx.IDENTIFIER())
        elif(ctx.expressionList() == None):
            # Deberíamos saber si es FAST o GLOBAL
            self.generate("LOAD_FAST", ctx.IDENTIFIER().getText())
            # self.generate("CALL_FUNCTION", ctx.IDENTIFIER().getText())
        else:
            cant_params = self.visit(ctx.expressionList())
            self.generate("LOAD_GLOBAL", ctx.IDENTIFIER().getText())
            self.generate("CALL_FUNCTION", "0")
        return

    # Visit a parse tree produced by miniPythonParser#listExpressionMP.
    def visitListExpressionMP(self, ctx: miniPythonParser.ListExpressionMPContext):
        return self.visitChildren(ctx)

