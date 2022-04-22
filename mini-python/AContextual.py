from generated.miniPythonVisitor import *
from TablaSimbolos import *
# Importing the StringIO module.
from io import StringIO


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

    def printErrors(self):
        if not self.hasErrors():
            return "0 errors"
        builder = StringIO
        for s in self.errorMsgs:
            builder.writable("%s\n", s)  # verificar
        return builder.__str__(self)

    # Visit a parse tree produced by miniPythonParser#programMP.
    def visitProgramMP(self, ctx: miniPythonParser.ProgramMPContext):
        return super().visitProgramMP(ctx)

    # Visit a parse tree produced by miniPythonParser#statementMP.
    def visitStatementMP(self, ctx: miniPythonParser.StatementMPContext):
        return super().visitStatementMP(ctx)

    # Visit a parse tree produced by miniPythonParser#defStatementMP.
    def visitDefStatementMP(self, ctx: miniPythonParser.DefStatementMPContext):
        return super().visitDefStatementMP(ctx)

    # Visit a parse tree produced by miniPythonParser#argListMP.
    def visitArgListMP(self, ctx: miniPythonParser.ArgListMPContext):
        return super().visitArgListMP(ctx)

    # Visit a parse tree produced by miniPythonParser#moreArgsMP.
    def visitMoreArgsMP(self, ctx: miniPythonParser.MoreArgsMPContext):
        return super().visitMoreArgsMP(ctx)

    # Visit a parse tree produced by miniPythonParser#ifStatementMP.
    def visitIfStatementMP(self, ctx: miniPythonParser.IfStatementMPContext):
        return super().visitIfStatementMP(ctx)

    # Visit a parse tree produced by miniPythonParser#whileStatementMP.
    def visitWhileStatementMP(self, ctx: miniPythonParser.WhileStatementMPContext):
        return super().visitWhileStatementMP(ctx)

    # Visit a parse tree produced by miniPythonParser#forStatementMP.
    def visitForStatementMP(self, ctx: miniPythonParser.ForStatementMPContext):
        return super().visitForStatementMP(ctx)

    # Visit a parse tree produced by miniPythonParser#returnStatementMP.
    def visitReturnStatementMP(self, ctx: miniPythonParser.ReturnStatementMPContext):
        return super().visitReturnStatementMP(ctx)

    # Visit a parse tree produced by miniPythonParser#printStatementMP.
    def visitPrintStatementMP(self, ctx: miniPythonParser.PrintStatementMPContext):
        return super().visitPrintStatementMP(ctx)

    # Visit a parse tree produced by miniPythonParser#assignStatementMP.
    def visitAssignStatementMP(self, ctx: miniPythonParser.AssignStatementMPContext):
        return super().visitAssignStatementMP(ctx)

    # Visit a parse tree produced by miniPythonParser#functionCallStatementMP.
    def visitFunctionCallStatementMP(self, ctx: miniPythonParser.FunctionCallStatementMPContext):
        return super().visitFunctionCallStatementMP(ctx)

    # Visit a parse tree produced by miniPythonParser#expressionStatementMP.
    def visitExpressionStatementMP(self, ctx: miniPythonParser.ExpressionStatementMPContext):
        return super().visitExpressionStatementMP(ctx)

    # Visit a parse tree produced by miniPythonParser#sequenceMP.
    def visitSequenceMP(self, ctx: miniPythonParser.SequenceMPContext):
        return super().visitSequenceMP(ctx)

    # Visit a parse tree produced by miniPythonParser#moreStatementsMP.
    def visitMoreStatementsMP(self, ctx: miniPythonParser.MoreStatementsMPContext):
        return super().visitMoreStatementsMP(ctx)

    # Visit a parse tree produced by miniPythonParser#expression.
    def visitExpression(self, ctx: miniPythonParser.ExpressionContext):
        return super().visitExpression(ctx)

    # Visit a parse tree produced by miniPythonParser#comparisonMP.
    def visitComparisonMP(self, ctx: miniPythonParser.ComparisonMPContext):
        return super().visitComparisonMP(ctx)

    # Visit a parse tree produced by miniPythonParser#additionExpressionMP.
    def visitAdditionExpressionMP(self, ctx: miniPythonParser.AdditionExpressionMPContext):
        return super().visitAdditionExpressionMP(ctx)

    # Visit a parse tree produced by miniPythonParser#additionFactorMP.
    def visitAdditionFactorMP(self, ctx: miniPythonParser.AdditionFactorMPContext):
        return super().visitAdditionFactorMP(ctx)

    # Visit a parse tree produced by miniPythonParser#multiplicationExpressionMP.
    def visitMultiplicationExpressionMP(self, ctx: miniPythonParser.MultiplicationExpressionMPContext):
        return super().visitMultiplicationExpressionMP(ctx)

    # Visit a parse tree produced by miniPythonParser#multiplicationFactorMP.
    def visitMultiplicationFactorMP(self, ctx: miniPythonParser.MultiplicationFactorMPContext):
        return super().visitMultiplicationFactorMP(ctx)

    # Visit a parse tree produced by miniPythonParser#elementExpressionMP.
    def visitElementExpressionMP(self, ctx: miniPythonParser.ElementExpressionMPContext):
        return super().visitElementExpressionMP(ctx)

    # Visit a parse tree produced by miniPythonParser#elementAccessMP.
    def visitElementAccessMP(self, ctx: miniPythonParser.ElementAccessMPContext):
        return super().visitElementAccessMP(ctx)

    # Visit a parse tree produced by miniPythonParser#expressionListMP.
    def visitExpressionListMP(self, ctx: miniPythonParser.ExpressionListMPContext):
        return super().visitExpressionListMP(ctx)

    # Visit a parse tree produced by miniPythonParser#moreExpressionsMP.
    def visitMoreExpressionsMP(self, ctx: miniPythonParser.MoreExpressionsMPContext):
        return super().visitMoreExpressionsMP(ctx)

    # Visit a parse tree produced by miniPythonParser#primitiveExpressionMP.
    def visitPrimitiveExpressionMP(self, ctx: miniPythonParser.PrimitiveExpressionMPContext):
        return super().visitPrimitiveExpressionMP(ctx)

    # Visit a parse tree produced by miniPythonParser#listExpressionMP.
    def visitListExpressionMP(self, ctx: miniPythonParser.ListExpressionMPContext):
        return super().visitListExpressionMP(ctx)
