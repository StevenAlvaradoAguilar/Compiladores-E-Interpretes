from generated.miniPythonVisitor import miniPythonVisitor
from generated.miniPythonParser import miniPythonParser
from generated.miniPythonLexer import miniPythonLexer

from antlr4 import *

class codeGen(miniPythonVisitor):

    class Instr:
        def __init__(self, i, a):
            self.instr = i
            self.arg = a

    def __init__(self):
        self.codigo = []
        self.instActual = 0

    def generate(self, instr, arg):
        self.codigo.append(codeGen.Instr(instr, arg))

    def printCode(self):
        print("----- CODIGO GENERADO ------\n")
        for x in self.codigo:
            print(x.instr, end = '')
            if (x.arg):
                print(" " + x.arg)
            else:
                print(" ")

    def visitProgramAST(self, ctx: miniPythonParser.ProgramASTContext):
        super().visitProgramAST(ctx)
        self.printCode()
        return None


    def visitStatementsAST(self, ctx: miniPythonParser.StatementsASTContext):
        return super().visitStatementsAST(ctx)

    def visitStatement(self, ctx: miniPythonParser.StatementContext):
        return super().visitStatement(ctx)

    def visitDefStatAST(self, ctx: miniPythonParser.DefStatASTContext):
        return super().visitDefStatAST(ctx)

    def visitArgListAST(self, ctx: miniPythonParser.ArgListASTContext):
        return super().visitArgListAST(ctx)

    def visitIfStatAST(self, ctx: miniPythonParser.IfStatASTContext):
        return super().visitIfStatAST(ctx)

    def visitWhileStatAST(self, ctx: miniPythonParser.WhileStatASTContext):
        return super().visitWhileStatAST(ctx)

    def visitForStatAST(self, ctx: miniPythonParser.ForStatASTContext):
        return super().visitForStatAST(ctx)

    def visitReturnStatAST(self, ctx: miniPythonParser.ReturnStatASTContext):
        return super().visitReturnStatAST(ctx)

    def visitPrintStatAST(self, ctx: miniPythonParser.PrintStatASTContext):
        return super().visitPrintStatAST(ctx)

    def visitAssignStatAST(self, ctx: miniPythonParser.AssignStatASTContext):
        self.visit(ctx.expression())
        self.generate("STORE_FAST" ,ctx.IDENTIFIER().getText())
        return None

    def visitFunctionCallStatAST(self, ctx: miniPythonParser.FunctionCallStatASTContext):
        return super().visitFunctionCallStatAST(ctx)

    def visitExpressionStatAST(self, ctx: miniPythonParser.ExpressionStatASTContext):
        return super().visitExpressionStatAST(ctx)

    def visitSequenceAST(self, ctx: miniPythonParser.SequenceASTContext):
        return super().visitSequenceAST(ctx)

    def visitMoreStatAST(self, ctx: miniPythonParser.MoreStatASTContext):
        return super().visitMoreStatAST(ctx)

    def visitExpressionAST(self, ctx: miniPythonParser.ExpressionASTContext):
        return super().visitExpressionAST(ctx)

    def visitAdditionExprAST(self, ctx: miniPythonParser.AdditionExprASTContext):
        self.visit(ctx.getChild(0))
        i = 1
        while i < len(ctx.children):
            oper = ctx.children[i]
            i +=    1
            self.visit(ctx.getChild(i))
            if (oper.getText() == "+"):
                self.generate("BINARY_ADD",None)
            elif (oper.getText() == "-"):
                self.generate("BINARY_SUBSTRACT", None)
            i += 1

        return None

    def visitMultiplicationStatAST(self, ctx: miniPythonParser.MultiplicationStatASTContext):
        self.visit(ctx.getChild(0))
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

    def visitElementExprAST(self, ctx: miniPythonParser.ElementExprASTContext):
        return super().visitElementExprAST(ctx)

    def visitExpressionListAST(self, ctx: miniPythonParser.ExpressionListASTContext):
        return super().visitExpressionListAST(ctx)

    def visitNumPEAST(self, ctx: miniPythonParser.NumPEASTContext):
        self.generate("LOAD_CONST",ctx.NUM().getText())
        return None

    def visitStringPEAST(self, ctx: miniPythonParser.StringPEASTContext):
        return super().visitStringPEAST(ctx)

    def visitDesignatorPEAST(self, ctx: miniPythonParser.DesignatorPEASTContext):
        return super().visitDesignatorPEAST(ctx)

    def visitBlockPEAST(self, ctx: miniPythonParser.BlockPEASTContext):
        return super().visitBlockPEAST(ctx)

    def visitListPEAST(self, ctx: miniPythonParser.ListPEASTContext):
        return super().visitListPEAST(ctx)

    def visitLenPEAST(self, ctx: miniPythonParser.LenPEASTContext):
        return super().visitLenPEAST(ctx)

    def visitDesignatorAST(self, ctx: miniPythonParser.DesignatorASTContext):
        if (ctx.expressionList() == None):
            # Deberíamos si es FAST o GLOBAL
            self.generate("LOAD_FAST",ctx.IDENTIFIER().getText())
        else:
            self.generate("LOAD_GLOBAL",ctx.IDENTIFIER().getText())
        return None
