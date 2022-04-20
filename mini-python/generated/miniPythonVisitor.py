# Generated from D:/Universidad/Compiladores_e_Interpretes/Compiladores-E-Interpretes/mini-python\miniPython.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .miniPythonParser import miniPythonParser
else:
    from miniPythonParser import miniPythonParser

# This class defines a complete generic visitor for a parse tree produced by miniPythonParser.

class miniPythonVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by miniPythonParser#programMP.
    def visitProgramMP(self, ctx:miniPythonParser.ProgramMPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPythonParser#statementMP.
    def visitStatementMP(self, ctx:miniPythonParser.StatementMPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPythonParser#defStatementMP.
    def visitDefStatementMP(self, ctx:miniPythonParser.DefStatementMPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPythonParser#argListMP.
    def visitArgListMP(self, ctx:miniPythonParser.ArgListMPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPythonParser#moreArgsMP.
    def visitMoreArgsMP(self, ctx:miniPythonParser.MoreArgsMPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPythonParser#ifStatementMP.
    def visitIfStatementMP(self, ctx:miniPythonParser.IfStatementMPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPythonParser#whileStatementMP.
    def visitWhileStatementMP(self, ctx:miniPythonParser.WhileStatementMPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPythonParser#forStatementMP.
    def visitForStatementMP(self, ctx:miniPythonParser.ForStatementMPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPythonParser#returnStatementMP.
    def visitReturnStatementMP(self, ctx:miniPythonParser.ReturnStatementMPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPythonParser#printStatementMP.
    def visitPrintStatementMP(self, ctx:miniPythonParser.PrintStatementMPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPythonParser#assignStatementMP.
    def visitAssignStatementMP(self, ctx:miniPythonParser.AssignStatementMPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPythonParser#functionCallStatementMP.
    def visitFunctionCallStatementMP(self, ctx:miniPythonParser.FunctionCallStatementMPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPythonParser#expressionStatementMP.
    def visitExpressionStatementMP(self, ctx:miniPythonParser.ExpressionStatementMPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPythonParser#sequenceMP.
    def visitSequenceMP(self, ctx:miniPythonParser.SequenceMPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPythonParser#moreStatementsMP.
    def visitMoreStatementsMP(self, ctx:miniPythonParser.MoreStatementsMPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPythonParser#expression.
    def visitExpression(self, ctx:miniPythonParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPythonParser#comparisonMP.
    def visitComparisonMP(self, ctx:miniPythonParser.ComparisonMPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPythonParser#additionExpressionMP.
    def visitAdditionExpressionMP(self, ctx:miniPythonParser.AdditionExpressionMPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPythonParser#additionFactorMP.
    def visitAdditionFactorMP(self, ctx:miniPythonParser.AdditionFactorMPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPythonParser#multiplicationExpressionMP.
    def visitMultiplicationExpressionMP(self, ctx:miniPythonParser.MultiplicationExpressionMPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPythonParser#multiplicationFactorMP.
    def visitMultiplicationFactorMP(self, ctx:miniPythonParser.MultiplicationFactorMPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPythonParser#elementExpressionMP.
    def visitElementExpressionMP(self, ctx:miniPythonParser.ElementExpressionMPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPythonParser#elementAccessMP.
    def visitElementAccessMP(self, ctx:miniPythonParser.ElementAccessMPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPythonParser#expressionListMP.
    def visitExpressionListMP(self, ctx:miniPythonParser.ExpressionListMPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPythonParser#moreExpressionsMP.
    def visitMoreExpressionsMP(self, ctx:miniPythonParser.MoreExpressionsMPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPythonParser#primitiveExpressionMP.
    def visitPrimitiveExpressionMP(self, ctx:miniPythonParser.PrimitiveExpressionMPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPythonParser#listExpressionMP.
    def visitListExpressionMP(self, ctx:miniPythonParser.ListExpressionMPContext):
        return self.visitChildren(ctx)



del miniPythonParser