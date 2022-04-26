# Generated from D:/Universidad/Compiladores_e_Interpretes/Compiladores-E-Interpretes/mini-python\miniPython.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .miniPythonParser import miniPythonParser
else:
    from miniPythonParser import miniPythonParser

# This class defines a complete listener for a parse tree produced by miniPythonParser.
class miniPythonListener(ParseTreeListener):

    # Enter a parse tree produced by miniPythonParser#programMP.
    def enterProgramMP(self, ctx:miniPythonParser.ProgramMPContext):
        pass

    # Exit a parse tree produced by miniPythonParser#programMP.
    def exitProgramMP(self, ctx:miniPythonParser.ProgramMPContext):
        pass


    # Enter a parse tree produced by miniPythonParser#defStat.
    def enterDefStat(self, ctx:miniPythonParser.DefStatContext):
        pass

    # Exit a parse tree produced by miniPythonParser#defStat.
    def exitDefStat(self, ctx:miniPythonParser.DefStatContext):
        pass


    # Enter a parse tree produced by miniPythonParser#ifStat.
    def enterIfStat(self, ctx:miniPythonParser.IfStatContext):
        pass

    # Exit a parse tree produced by miniPythonParser#ifStat.
    def exitIfStat(self, ctx:miniPythonParser.IfStatContext):
        pass


    # Enter a parse tree produced by miniPythonParser#returnStat.
    def enterReturnStat(self, ctx:miniPythonParser.ReturnStatContext):
        pass

    # Exit a parse tree produced by miniPythonParser#returnStat.
    def exitReturnStat(self, ctx:miniPythonParser.ReturnStatContext):
        pass


    # Enter a parse tree produced by miniPythonParser#printStat.
    def enterPrintStat(self, ctx:miniPythonParser.PrintStatContext):
        pass

    # Exit a parse tree produced by miniPythonParser#printStat.
    def exitPrintStat(self, ctx:miniPythonParser.PrintStatContext):
        pass


    # Enter a parse tree produced by miniPythonParser#whileStat.
    def enterWhileStat(self, ctx:miniPythonParser.WhileStatContext):
        pass

    # Exit a parse tree produced by miniPythonParser#whileStat.
    def exitWhileStat(self, ctx:miniPythonParser.WhileStatContext):
        pass


    # Enter a parse tree produced by miniPythonParser#forStat.
    def enterForStat(self, ctx:miniPythonParser.ForStatContext):
        pass

    # Exit a parse tree produced by miniPythonParser#forStat.
    def exitForStat(self, ctx:miniPythonParser.ForStatContext):
        pass


    # Enter a parse tree produced by miniPythonParser#assignStat.
    def enterAssignStat(self, ctx:miniPythonParser.AssignStatContext):
        pass

    # Exit a parse tree produced by miniPythonParser#assignStat.
    def exitAssignStat(self, ctx:miniPythonParser.AssignStatContext):
        pass


    # Enter a parse tree produced by miniPythonParser#functionCallStat.
    def enterFunctionCallStat(self, ctx:miniPythonParser.FunctionCallStatContext):
        pass

    # Exit a parse tree produced by miniPythonParser#functionCallStat.
    def exitFunctionCallStat(self, ctx:miniPythonParser.FunctionCallStatContext):
        pass


    # Enter a parse tree produced by miniPythonParser#expressionSt.
    def enterExpressionSt(self, ctx:miniPythonParser.ExpressionStContext):
        pass

    # Exit a parse tree produced by miniPythonParser#expressionSt.
    def exitExpressionSt(self, ctx:miniPythonParser.ExpressionStContext):
        pass


    # Enter a parse tree produced by miniPythonParser#defStatementMP.
    def enterDefStatementMP(self, ctx:miniPythonParser.DefStatementMPContext):
        pass

    # Exit a parse tree produced by miniPythonParser#defStatementMP.
    def exitDefStatementMP(self, ctx:miniPythonParser.DefStatementMPContext):
        pass


    # Enter a parse tree produced by miniPythonParser#argListMP.
    def enterArgListMP(self, ctx:miniPythonParser.ArgListMPContext):
        pass

    # Exit a parse tree produced by miniPythonParser#argListMP.
    def exitArgListMP(self, ctx:miniPythonParser.ArgListMPContext):
        pass


    # Enter a parse tree produced by miniPythonParser#moreArgsMP.
    def enterMoreArgsMP(self, ctx:miniPythonParser.MoreArgsMPContext):
        pass

    # Exit a parse tree produced by miniPythonParser#moreArgsMP.
    def exitMoreArgsMP(self, ctx:miniPythonParser.MoreArgsMPContext):
        pass


    # Enter a parse tree produced by miniPythonParser#ifStatementMP.
    def enterIfStatementMP(self, ctx:miniPythonParser.IfStatementMPContext):
        pass

    # Exit a parse tree produced by miniPythonParser#ifStatementMP.
    def exitIfStatementMP(self, ctx:miniPythonParser.IfStatementMPContext):
        pass


    # Enter a parse tree produced by miniPythonParser#whileStatementMP.
    def enterWhileStatementMP(self, ctx:miniPythonParser.WhileStatementMPContext):
        pass

    # Exit a parse tree produced by miniPythonParser#whileStatementMP.
    def exitWhileStatementMP(self, ctx:miniPythonParser.WhileStatementMPContext):
        pass


    # Enter a parse tree produced by miniPythonParser#forStatementMP.
    def enterForStatementMP(self, ctx:miniPythonParser.ForStatementMPContext):
        pass

    # Exit a parse tree produced by miniPythonParser#forStatementMP.
    def exitForStatementMP(self, ctx:miniPythonParser.ForStatementMPContext):
        pass


    # Enter a parse tree produced by miniPythonParser#returnStatementMP.
    def enterReturnStatementMP(self, ctx:miniPythonParser.ReturnStatementMPContext):
        pass

    # Exit a parse tree produced by miniPythonParser#returnStatementMP.
    def exitReturnStatementMP(self, ctx:miniPythonParser.ReturnStatementMPContext):
        pass


    # Enter a parse tree produced by miniPythonParser#printStatementMP.
    def enterPrintStatementMP(self, ctx:miniPythonParser.PrintStatementMPContext):
        pass

    # Exit a parse tree produced by miniPythonParser#printStatementMP.
    def exitPrintStatementMP(self, ctx:miniPythonParser.PrintStatementMPContext):
        pass


    # Enter a parse tree produced by miniPythonParser#assignStatementMP.
    def enterAssignStatementMP(self, ctx:miniPythonParser.AssignStatementMPContext):
        pass

    # Exit a parse tree produced by miniPythonParser#assignStatementMP.
    def exitAssignStatementMP(self, ctx:miniPythonParser.AssignStatementMPContext):
        pass


    # Enter a parse tree produced by miniPythonParser#functionCallStatementMP.
    def enterFunctionCallStatementMP(self, ctx:miniPythonParser.FunctionCallStatementMPContext):
        pass

    # Exit a parse tree produced by miniPythonParser#functionCallStatementMP.
    def exitFunctionCallStatementMP(self, ctx:miniPythonParser.FunctionCallStatementMPContext):
        pass


    # Enter a parse tree produced by miniPythonParser#expressionStatementMP.
    def enterExpressionStatementMP(self, ctx:miniPythonParser.ExpressionStatementMPContext):
        pass

    # Exit a parse tree produced by miniPythonParser#expressionStatementMP.
    def exitExpressionStatementMP(self, ctx:miniPythonParser.ExpressionStatementMPContext):
        pass


    # Enter a parse tree produced by miniPythonParser#sequenceMP.
    def enterSequenceMP(self, ctx:miniPythonParser.SequenceMPContext):
        pass

    # Exit a parse tree produced by miniPythonParser#sequenceMP.
    def exitSequenceMP(self, ctx:miniPythonParser.SequenceMPContext):
        pass


    # Enter a parse tree produced by miniPythonParser#moreStatementsMP.
    def enterMoreStatementsMP(self, ctx:miniPythonParser.MoreStatementsMPContext):
        pass

    # Exit a parse tree produced by miniPythonParser#moreStatementsMP.
    def exitMoreStatementsMP(self, ctx:miniPythonParser.MoreStatementsMPContext):
        pass


    # Enter a parse tree produced by miniPythonParser#expressionMP.
    def enterExpressionMP(self, ctx:miniPythonParser.ExpressionMPContext):
        pass

    # Exit a parse tree produced by miniPythonParser#expressionMP.
    def exitExpressionMP(self, ctx:miniPythonParser.ExpressionMPContext):
        pass


    # Enter a parse tree produced by miniPythonParser#comparisonMP.
    def enterComparisonMP(self, ctx:miniPythonParser.ComparisonMPContext):
        pass

    # Exit a parse tree produced by miniPythonParser#comparisonMP.
    def exitComparisonMP(self, ctx:miniPythonParser.ComparisonMPContext):
        pass


    # Enter a parse tree produced by miniPythonParser#additionExpressionMP.
    def enterAdditionExpressionMP(self, ctx:miniPythonParser.AdditionExpressionMPContext):
        pass

    # Exit a parse tree produced by miniPythonParser#additionExpressionMP.
    def exitAdditionExpressionMP(self, ctx:miniPythonParser.AdditionExpressionMPContext):
        pass


    # Enter a parse tree produced by miniPythonParser#additionFactorMP.
    def enterAdditionFactorMP(self, ctx:miniPythonParser.AdditionFactorMPContext):
        pass

    # Exit a parse tree produced by miniPythonParser#additionFactorMP.
    def exitAdditionFactorMP(self, ctx:miniPythonParser.AdditionFactorMPContext):
        pass


    # Enter a parse tree produced by miniPythonParser#multiplicationExpressionMP.
    def enterMultiplicationExpressionMP(self, ctx:miniPythonParser.MultiplicationExpressionMPContext):
        pass

    # Exit a parse tree produced by miniPythonParser#multiplicationExpressionMP.
    def exitMultiplicationExpressionMP(self, ctx:miniPythonParser.MultiplicationExpressionMPContext):
        pass


    # Enter a parse tree produced by miniPythonParser#multiplicationFactorMP.
    def enterMultiplicationFactorMP(self, ctx:miniPythonParser.MultiplicationFactorMPContext):
        pass

    # Exit a parse tree produced by miniPythonParser#multiplicationFactorMP.
    def exitMultiplicationFactorMP(self, ctx:miniPythonParser.MultiplicationFactorMPContext):
        pass


    # Enter a parse tree produced by miniPythonParser#elementExpressionMP.
    def enterElementExpressionMP(self, ctx:miniPythonParser.ElementExpressionMPContext):
        pass

    # Exit a parse tree produced by miniPythonParser#elementExpressionMP.
    def exitElementExpressionMP(self, ctx:miniPythonParser.ElementExpressionMPContext):
        pass


    # Enter a parse tree produced by miniPythonParser#elementAccessMP.
    def enterElementAccessMP(self, ctx:miniPythonParser.ElementAccessMPContext):
        pass

    # Exit a parse tree produced by miniPythonParser#elementAccessMP.
    def exitElementAccessMP(self, ctx:miniPythonParser.ElementAccessMPContext):
        pass


    # Enter a parse tree produced by miniPythonParser#expressionListMP.
    def enterExpressionListMP(self, ctx:miniPythonParser.ExpressionListMPContext):
        pass

    # Exit a parse tree produced by miniPythonParser#expressionListMP.
    def exitExpressionListMP(self, ctx:miniPythonParser.ExpressionListMPContext):
        pass


    # Enter a parse tree produced by miniPythonParser#moreExpressionsMP.
    def enterMoreExpressionsMP(self, ctx:miniPythonParser.MoreExpressionsMPContext):
        pass

    # Exit a parse tree produced by miniPythonParser#moreExpressionsMP.
    def exitMoreExpressionsMP(self, ctx:miniPythonParser.MoreExpressionsMPContext):
        pass


    # Enter a parse tree produced by miniPythonParser#integersMP.
    def enterIntegersMP(self, ctx:miniPythonParser.IntegersMPContext):
        pass

    # Exit a parse tree produced by miniPythonParser#integersMP.
    def exitIntegersMP(self, ctx:miniPythonParser.IntegersMPContext):
        pass


    # Enter a parse tree produced by miniPythonParser#floatsMP.
    def enterFloatsMP(self, ctx:miniPythonParser.FloatsMPContext):
        pass

    # Exit a parse tree produced by miniPythonParser#floatsMP.
    def exitFloatsMP(self, ctx:miniPythonParser.FloatsMPContext):
        pass


    # Enter a parse tree produced by miniPythonParser#chartsMP.
    def enterChartsMP(self, ctx:miniPythonParser.ChartsMPContext):
        pass

    # Exit a parse tree produced by miniPythonParser#chartsMP.
    def exitChartsMP(self, ctx:miniPythonParser.ChartsMPContext):
        pass


    # Enter a parse tree produced by miniPythonParser#stringsMP.
    def enterStringsMP(self, ctx:miniPythonParser.StringsMPContext):
        pass

    # Exit a parse tree produced by miniPythonParser#stringsMP.
    def exitStringsMP(self, ctx:miniPythonParser.StringsMPContext):
        pass


    # Enter a parse tree produced by miniPythonParser#identifierMP.
    def enterIdentifierMP(self, ctx:miniPythonParser.IdentifierMPContext):
        pass

    # Exit a parse tree produced by miniPythonParser#identifierMP.
    def exitIdentifierMP(self, ctx:miniPythonParser.IdentifierMPContext):
        pass


    # Enter a parse tree produced by miniPythonParser#parenthesisExpressionMP.
    def enterParenthesisExpressionMP(self, ctx:miniPythonParser.ParenthesisExpressionMPContext):
        pass

    # Exit a parse tree produced by miniPythonParser#parenthesisExpressionMP.
    def exitParenthesisExpressionMP(self, ctx:miniPythonParser.ParenthesisExpressionMPContext):
        pass


    # Enter a parse tree produced by miniPythonParser#listExpMP.
    def enterListExpMP(self, ctx:miniPythonParser.ListExpMPContext):
        pass

    # Exit a parse tree produced by miniPythonParser#listExpMP.
    def exitListExpMP(self, ctx:miniPythonParser.ListExpMPContext):
        pass


    # Enter a parse tree produced by miniPythonParser#primitiveExpressionMP.
    def enterPrimitiveExpressionMP(self, ctx:miniPythonParser.PrimitiveExpressionMPContext):
        pass

    # Exit a parse tree produced by miniPythonParser#primitiveExpressionMP.
    def exitPrimitiveExpressionMP(self, ctx:miniPythonParser.PrimitiveExpressionMPContext):
        pass


    # Enter a parse tree produced by miniPythonParser#listExpressionMP.
    def enterListExpressionMP(self, ctx:miniPythonParser.ListExpressionMPContext):
        pass

    # Exit a parse tree produced by miniPythonParser#listExpressionMP.
    def exitListExpressionMP(self, ctx:miniPythonParser.ListExpressionMPContext):
        pass



del miniPythonParser