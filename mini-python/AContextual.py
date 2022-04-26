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
        # self.laTabla.closeScope()
        # self.laTabla.imprimir()
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
        m = self.laTabla.buscar(ctx.IDENTIFIER().getText())
        # saca todos los parametros
        if ctx.argList().IDENTIFIER() is not None:
            contador = 1 + len(ctx.argList().moreArgs().IDENTIFIER())
        # print(contador)

        if m is not None:
            if m.isMethod:
                print("La función ya ha sido declarada " + ctx.IDENTIFIER().getText(), file=sys.stderr)
            else:
                print("El identificador no es un método")
        else:
            self.laTabla.insertar(ctx.IDENTIFIER().getText(), contador, True, "Declaración de Función")
        self.visit(ctx.argList())
        self.laTabla.openScope()
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
        self.laTabla.openScope()
        self.visit(ctx.sequence())
        self.laTabla.closeScope()
        return

    # Visit a parse tree produced by miniPythonParser#forStatementMP.
    def visitForStatementMP(self, ctx: miniPythonParser.ForStatementMPContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#returnStatementMP.
    def visitReturnStatementMP(self, ctx: miniPythonParser.ReturnStatementMPContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#printStatementMP.
    def visitPrintStatementMP(self, ctx: miniPythonParser.PrintStatementMPContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#assignStatementMP.
    def visitAssignStatementMP(self, ctx: miniPythonParser.AssignStatementMPContext):
        self.laTabla.insertar(ctx.IDENTIFIER(), 0, False, ctx.expression())
        self.visit(ctx.expression())
        return

    # Visit a parse tree produced by miniPythonParser#functionCallStatementMP.
    def visitFunctionCallStatementMP(self, ctx: miniPythonParser.FunctionCallStatementMPContext):
        # sacar primer parámetro
        nombreFuncionLlamada = None
        if ctx.primitiveExpression().IDENTIFIER() is not None:
            nombreFuncionLlamada = ctx.primitiveExpression().IDENTIFIER().getText()
        if not self.laTabla.buscar(nombreFuncionLlamada):
            print("La función no ha sido declarada")
        if ctx.expressionList().expression() is not None:
            print(ctx.expressionList().moreExpressions().expression()[0].getText())
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
        """
        Este método que da de está forma ya que el visitChildren visita
        a todos.
        """
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#expression.
    def visitExpression(self, ctx: miniPythonParser.ExpressionContext):
        """
        Este método que da de está forma ya que el visitChildren visita
        a todos.
        """
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#comparisonMP.
    def visitComparisonMP(self, ctx: miniPythonParser.ComparisonMPContext):
        """
        Este método que da de está forma ya que el visitChildren visita
        a todos.
        """
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#additionExpressionMP.
    def visitAdditionExpressionMP(self, ctx: miniPythonParser.AdditionExpressionMPContext):
        """
        Este método que da de está forma ya que el visitChildren visita
        a todos.
        """
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#additionFactorMP.
    def visitAdditionFactorMP(self, ctx: miniPythonParser.AdditionFactorMPContext):
        """
        Este método que da de está forma ya que el visitChildren visita
        a todos.
        """
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#multiplicationExpressionMP.
    def visitMultiplicationExpressionMP(self, ctx: miniPythonParser.MultiplicationExpressionMPContext):
        """
        Este método que da de está forma ya que el visitChildren visita
        a todos.
        """
        return self.visitChildren(ctx)

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
        Este método que da de está forma ya que el visitChildren visita
        a todos.
        """
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#elementAccessMP.
    def visitElementAccessMP(self, ctx: miniPythonParser.ElementAccessMPContext):
        """
        Este método que da de está forma ya que el visitChildren visita
        a todos.
        """
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
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#primitiveExpressionMP.
    def visitPrimitiveExpressionMP(self, ctx: miniPythonParser.PrimitiveExpressionMPContext):
        self.laTabla.insertar(ctx.IDENTIFIER(), 0, False, ctx.expressionList())
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#listExpressionMP.
    def visitListExpressionMP(self, ctx: miniPythonParser.ListExpressionMPContext):
        """
        Este método que da de está forma ya que el visitChildren visita
        a todos.
        """
        return self.visitChildren(ctx)
