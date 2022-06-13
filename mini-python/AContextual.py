# Importing the StringIO module.
# from io import StringIO

from TablaSimbolos import *

from generated.miniPythonVisitor import *
from generated.miniPythonParser import *


class AContextual(miniPythonVisitor):
    TablaSimbolos = None
    laTabla = TablaSimbolos

    errorMsgs = []

    def __init__(self):
        self.errorMsgs = []
        self.laTabla = TablaSimbolos()
        self.laTabla.openScope()

    def hasErrors(self):
        return len(self.errorMsgs) > 0

    def printErrors(self):
        if not self.hasErrors():
            return "0 errors"
        for s in self.errorMsgs:
            print("%s\n", s)  # verificar

    # Visit a parse tree produced by miniPythonParser#programMP.
    def visitProgramMP(self, ctx: miniPythonParser.ProgramMPContext):
        self.visit(ctx.statement(0))
        for i in ctx.statement():
            if ctx.statement() is not None:
                self.visit(i)
        return
        # return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#statementMP.
    def visitStatementMP(self, ctx: miniPythonParser.StatementMPContext):
        return self.visitChildren(ctx)
        # return super().visitStatementMP(ctx)

    # Visit a parse tree produced by miniPythonParser#defStatementMP.
    def visitDefStatementMP(self, ctx: miniPythonParser.DefStatementMPContext):
        # print(ctx.IDENTIFIER().getText())

        contador = 0
        self.laTabla.openScope()
        m = self.laTabla.buscar(ctx.IDENTIFIER().getText())
        # saca todos los parámetros
        if ctx.argList().IDENTIFIER() is not None:
            contador = 1 + len(ctx.argList().moreArgs().IDENTIFIER())
        # print(contador)

        #  identifier, level, isMethod, decl
        self.laTabla.insertar(ctx.IDENTIFIER().getText(), self.laTabla.getLevel(), True, "Declaración de Función")
        self.visit(ctx.argList())
        self.visit(ctx.sequence())
        self.laTabla.closeScope()

    # Visit a parse tree produced by miniPythonParser#argListMP.
    def visitArgListMP(self, ctx: miniPythonParser.ArgListMPContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#moreArgsMP.
    def visitMoreArgsMP(self, ctx: miniPythonParser.MoreArgsMPContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#ifStatementMP.
    def visitIfStatementMP(self, ctx: miniPythonParser.IfStatementMPContext):
        self.visit(ctx.expression())
        if ctx.expression().getText is not None:
            # Validaciones de errores del if
            validationsF = ctx.expression().getText()
            if '"' in validationsF:
                print("Error no se puede poner parentesis dobles ", validationsF, file=sys.stderr)
            if "'" in validationsF:
                print("Error no se puede poner parentesis simples ", validationsF, file=sys.stderr)
        self.laTabla.openScope()
        self.visit(ctx.sequence()[0])
        self.laTabla.closeScope()
        if len(ctx.sequence()) > 1:
            self.laTabla.openScope()
            self.visit(ctx.sequence()[1])
            self.laTabla.closeScope()
        return

    # Visit a parse tree produced by miniPythonParser#whileStatementMP.
    def visitWhileStatementMP(self, ctx: miniPythonParser.WhileStatementMPContext):
        self.visit(ctx.expression())
        # Validaciones de errores del while
        validationsW = ctx.expression().getText()
        if '"' in validationsW:
            print("Error no se puede poner parentesis dobles ", validationsW, file=sys.stderr)
        if "'" in validationsW:
            print("Error no se puede puede poner parentesis simples ", validationsW, file=sys.stderr)
        self.laTabla.openScope()
        self.visit(ctx.sequence())
        self.laTabla.closeScope()
        return

    # Visit a parse tree produced by miniPythonParser#forStatementMP.
    def visitForStatementMP(self, ctx: miniPythonParser.ForStatementMPContext):
        if ctx.expression() is not None:
            self.visit(ctx.expression())
            # Validaciones de errores
            validationFor = ctx.expression().getText()
            if '"' in validationFor:
                print("Error no se puede llamar a funciones con parentesis dobles ", validationFor, file=sys.stderr)
            if "'" in validationFor:
                print("Error no se puede llamar a funciones con parentesis simples ", validationFor, file=sys.stderr)
            listNumber = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            for m in listNumber:
                if m in validationFor:
                    print("Error no se puede llamar a funciones con un numero", validationFor, file=sys.stderr)

            self.visit(ctx.expressionList())
            self.laTabla.openScope()
            self.visit(ctx.sequence())
            self.laTabla.closeScope()
            return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#returnStatementMP.
    def visitReturnStatementMP(self, ctx: miniPythonParser.ReturnStatementMPContext):
        if ctx.expression() is not None:
            return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#printStatementMP.
    def visitPrintStatementMP(self, ctx: miniPythonParser.PrintStatementMPContext):
        if ctx.expression() is not None:
            return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#assignStatementMP.
    def visitAssignStatementMP(self, ctx: miniPythonParser.AssignStatementMPContext):
        if ctx.expression() is not None:
            #  identifier, level, isMethod, decl
            self.laTabla.insertar(ctx.IDENTIFIER(), self.laTabla.getLevel(), False, ctx.expression())
            self.visit(ctx.expression())
        return

    # Visit a parse tree produced by miniPythonParser#functionCallStatementMP.
    def visitFunctionCallStatementMP(self, ctx: miniPythonParser.FunctionCallStatementMPContext):
        # sacar primer parámetro
        nombreFuncionLlamada = None
        if ctx.primitiveExpression().IDENTIFIER() is not None:
            nombreFuncionLlamada = ctx.primitiveExpression().IDENTIFIER().getText()
        # Validaciones de errores
        validationFunctionCall = ctx.primitiveExpression().getText()
        if '"' in validationFunctionCall:
            print("Error no se puede llamar a funciones con parentesis dobles ", validationFunctionCall, file=sys.stderr)
        if "'" in validationFunctionCall:
            print("Error no se puede llamar a funciones con parentesis simples ", validationFunctionCall, file=sys.stderr)
        listNumber = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for m in listNumber:
            if m in validationFunctionCall:
                print("Error no se puede llamar a funciones con un numero adelante del nombre, sino omita el mensaje", validationFunctionCall, file=sys.stderr)

        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#expressionStatementMP.
    def visitExpressionStatementMP(self, ctx: miniPythonParser.ExpressionStatementMPContext):
        """
        Este método que da de está forma ya que el visitChildren visita
        a todos.
        """
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#sequenceMP.
    def visitSequenceMP(self, ctx: miniPythonParser.SequenceMPContext):
        """
        Este método que da de está forma ya que el visitChildren visita
        a todos.
        """
        return self.visit(ctx.moreStatements())

    # Visit a parse tree produced by miniPythonParser#moreStatementsMP.
    def visitMoreStatementsMP(self, ctx: miniPythonParser.MoreStatementsMPContext):
        for i in range(len(ctx.statement())):
            self.visit(ctx.statement(i))
        return None

    # Visit a parse tree produced by miniPythonParser#expression.
    def visitExpression(self, ctx: miniPythonParser.ExpressionContext):
        self.visit(ctx.additionExpression())
        self.visit(ctx.comparison())
        return None

    # Visit a parse tree produced by miniPythonParser#comparisonMP.
    def visitComparisonMP(self, ctx: miniPythonParser.ComparisonMPContext):
        """
        Este método que da de está forma ya que el visitChildren visita
        a todos.
        """
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#additionExpressionMP.
    def visitAdditionExpressionMP(self, ctx: miniPythonParser.AdditionExpressionMPContext):
        self.visit(ctx.multiplicationExpression())
        self.visit(ctx.additionFactor())
        return None

    # Visit a parse tree produced by miniPythonParser#additionFactorMP.
    def visitAdditionFactorMP(self, ctx: miniPythonParser.AdditionFactorMPContext):
        """
        Este método que da de está forma ya que el visitChildren visita
        a todos.
        """
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#multiplicationExpressionMP.
    def visitMultiplicationExpressionMP(self, ctx: miniPythonParser.MultiplicationExpressionMPContext):
        self.visit(ctx.elementExpression())
        self.visit(ctx.multiplicationFactor())
        return None

    # Visit a parse tree produced by miniPythonParser#multiplicationFactorMP.
    def visitMultiplicationFactorMP(self, ctx: miniPythonParser.MultiplicationFactorMPContext):
        """
        Este método que da de está forma ya que el visitChildren visita
        a todos.
        """
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#elementExpressionMP.
    def visitElementExpressionMP(self, ctx: miniPythonParser.ElementExpressionMPContext):
        """
        Validaciones de errores de 3[2], “hola”[x], ‘a’(3,5),
        """
        if ctx.elementAccess() is not None:
            validarElem = ctx.primitiveExpression().getText()
            if '"' in validarElem:
                print("Error no se puede llamar a funciones con parentesis dobles ", file=sys.stderr)
            if "'" in validarElem:
                print("Error no se puede llamar a funciones con parentesis simples ", file=sys.stderr)
            listNumber = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            for i in listNumber:
                if i in validarElem:
                    print("Error no se puede llamar a funciones con un numero", file=sys.stderr)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#elementAccessMP.
    def visitElementAccessMP(self, ctx: miniPythonParser.ElementAccessMPContext):
        temporal = ""
        if ctx.expression() is not None:
            for x in ctx.expression():
                temporal = x.getText()
                # hacer un buscar
                #  identifier, level, isMethod, decl
                self.laTabla.insertar(temporal, self.laTabla.getLevel(), False, ctx.expression())  # verificar
                if self.laTabla.buscar(temporal) is None:
                    print("Error la variable no hay sido declarada " + temporal, file=sys.stderr)
            return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#expressionListMP.
    def visitExpressionListMP(self, ctx: miniPythonParser.ExpressionListMPContext):
        if ctx.expression() is not None:
            self.visit(ctx.expression())
            self.visit(ctx.moreExpressions())
        return

    # Visit a parse tree produced by miniPythonParser#moreExpressionsMP.
    def visitMoreExpressionsMP(self, ctx: miniPythonParser.MoreExpressionsMPContext):
        """
        Este método que da de está forma ya que el visitChildren visita
        a todos.
        """
        if ctx.expression() is not None:
            return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#primitiveExpressionMP.
    def visitPrimitiveExpressionMP(self, ctx: miniPythonParser.PrimitiveExpressionMPContext):
        #  identifier, level, isMethod, decl
        self.laTabla.insertar(ctx.IDENTIFIER(), self.laTabla.getLevel(), False, ctx.expressionList())
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#listExpressionMP.
    def visitListExpressionMP(self, ctx: miniPythonParser.ListExpressionMPContext):
        """
        Este método que da de está forma ya que el visitChildren visita
        a todos.
        """
        return self.visitChildren(ctx)
