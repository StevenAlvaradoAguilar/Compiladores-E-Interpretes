# Importing the StringIO module.
# from io import StringIO

from TablaSimbolos import *
from generated.miniPythonParser import *
from generated.miniPythonVisitor import *


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
        return self.visitChildren(ctx)
        # return super().visitProgramMP(ctx)

    # Visit a parse tree produced by miniPythonParser#statementMP.
    def visitStatementMP(self, ctx: miniPythonParser.StatementMPContext):
        return self.visitChildren(ctx)
        # return super().visitStatementMP(ctx)

    # Visit a parse tree produced by miniPythonParser#defStatementMP.
    def visitDefStatementMP(self, ctx: miniPythonParser.DefStatementMPContext):
        #print(ctx.IDENTIFIER().getText())
        m = TablaSimbolos.Ident
        m = self.laTabla.buscar(ctx.IDENTIFIER().getText())
        if m is not None:
            if m.isMethod:
                argList = []
                argList = self.visit(ctx.argList())
                if len(m.Ident.params) is not len(argList):
                    print("Cantidad de parámetros no coincide con la declaración")
            else:
                print("El identificador no es un método")
        else:
            print("El método no ha sido declarado")

        #self.visit(ctx.argList())
        #self.visit(ctx.sequence())
        return
        # return super().visitDefStatementMP(ctx)

    # Visit a parse tree produced by miniPythonParser#argListMP.
    def visitArgListMP(self, ctx: miniPythonParser.ArgListMPContext):
        print(ctx.moreArgs())
        n = TablaSimbolos.Ident
        n = self.laTabla.buscar(ctx.IDENTIFIER().getText())
        if n is not None:
            if n.isMethod:
                moreArgs = []
                moreArgs = self.visit(ctx.moreArgs())
                if len(n.Ident.params) is not len(moreArgs):
                    print("Cantidad de parámetros no coincide con la declaración")
            else:
                print("El identificador no es un método")
        else:
            print("El método no ha sido declarado")

        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#moreArgsMP.
    def visitMoreArgsMP(self, ctx: miniPythonParser.MoreArgsMPContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#ifStatementMP.
    def visitIfStatementMP(self, ctx: miniPythonParser.IfStatementMPContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#whileStatementMP.
    def visitWhileStatementMP(self, ctx: miniPythonParser.WhileStatementMPContext):
        return self.visitChildren(ctx)

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
        '''print(ctx.expression())
        self.laTabla.insertar(ctx.IDENTIFIER().getSymbol(), None, False, ctx);
        '''
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#functionCallStatementMP.
    def visitFunctionCallStatementMP(self, ctx: miniPythonParser.FunctionCallStatementMPContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#expressionStatementMP.
    def visitExpressionStatementMP(self, ctx: miniPythonParser.ExpressionStatementMPContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#sequenceMP.
    def visitSequenceMP(self, ctx: miniPythonParser.SequenceMPContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#moreStatementsMP.
    def visitMoreStatementsMP(self, ctx: miniPythonParser.MoreStatementsMPContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#expression.
    def visitExpression(self, ctx: miniPythonParser.ExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#comparisonMP.
    def visitComparisonMP(self, ctx: miniPythonParser.ComparisonMPContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#additionExpressionMP.
    def visitAdditionExpressionMP(self, ctx: miniPythonParser.AdditionExpressionMPContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#additionFactorMP.
    def visitAdditionFactorMP(self, ctx: miniPythonParser.AdditionFactorMPContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#multiplicationExpressionMP.
    def visitMultiplicationExpressionMP(self, ctx: miniPythonParser.MultiplicationExpressionMPContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#multiplicationFactorMP.
    def visitMultiplicationFactorMP(self, ctx: miniPythonParser.MultiplicationFactorMPContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#elementExpressionMP.
    def visitElementExpressionMP(self, ctx: miniPythonParser.ElementExpressionMPContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#elementAccessMP.
    def visitElementAccessMP(self, ctx: miniPythonParser.ElementAccessMPContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#expressionListMP.
    def visitExpressionListMP(self, ctx: miniPythonParser.ExpressionListMPContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#moreExpressionsMP.
    def visitMoreExpressionsMP(self, ctx: miniPythonParser.MoreExpressionsMPContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#primitiveExpressionMP.
    def visitPrimitiveExpressionMP(self, ctx: miniPythonParser.PrimitiveExpressionMPContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#listExpressionMP.
    def visitListExpressionMP(self, ctx: miniPythonParser.ListExpressionMPContext):
        return self.visitChildren(ctx)
