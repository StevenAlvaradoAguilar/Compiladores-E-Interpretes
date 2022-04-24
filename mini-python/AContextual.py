# Importing the StringIO module.
# from io import StringIO

from TablaSimbolos import *
from generated.miniPythonParser import *
from generated.miniPythonVisitor import *


class AContextual(miniPythonVisitor):
    TablaSimbolos = None
    laTabla = TablaSimbolos

    errorMsgs = [""]

    def __init__(self):
        self.errorMsgs = [""]
        self.laTabla = TablaSimbolos()
        self.laTabla.openScope()

    def hasErrors(self):
        return self.errorMsgs.__len__() > 0

    '''def printErrors(self):
        if not self.hasErrors():
            return "0 errors"
        builder = StringIO
        for s in self.errorMsgs:
            builder.writable("%s\n", s)  # verificar
        return builder.__str__(self)'''

    # Visit a parse tree produced by miniPythonParser#programMP.
    def visitProgramMP(self, ctx: miniPythonParser.ProgramMPContext):
        self.visit(ctx.statement())
        '''for x in ctx.statement():
            self.visit(ctx.statement(x))'''

        return self.visitChildren(ctx)
        # return super().visitProgramMP(ctx)

    # Visit a parse tree produced by miniPythonParser#statementMP.
    def visitStatementMP(self, ctx: miniPythonParser.StatementMPContext):
        self.visit(ctx.defStatement())
        self.visit(ctx.ifStatement())
        self.visit(ctx.returnStatement())
        self.visit(ctx.printStatement())
        self.visit(ctx.whileStatement())
        self.visit(ctx.forStatement())
        self.visit(ctx.assignStatement())
        self.visit(ctx.functionCallStatement())
        self.visit(ctx.expressionStatement())
        # return super().visitStatementMP(ctx)

    # Visit a parse tree produced by miniPythonParser#defStatementMP.
    def visitDefStatementMP(self, ctx: miniPythonParser.DefStatementMPContext):
        self.visit(ctx.argList())
        self.visit(ctx.sequence())
        return self.visitChildren(ctx)
        # return super().visitDefStatementMP(ctx)

    # Visit a parse tree produced by miniPythonParser#argListMP.
    def visitArgListMP(self, ctx: miniPythonParser.ArgListMPContext):
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
