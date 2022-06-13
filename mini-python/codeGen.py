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
        self.funcionesDefinidas = []
        self.parametrosDeclarados = []
        self.elementAccess = False

    def generate(self, instr, arg):
        self.codigo.append(codeGen.Instr(instr, arg))
        self.instActual += 1

    def printCode(self):
        print("----- CODIGO GENERA ------\n")
        for x in self.codigo:
            print(x.instr, end='')
            if (x.arg):
                FileStream
                print(" " + str(x.arg))
            else:
                print(" ")

    def generar_bytecode(self):
        f = open('bytecode.txt', 'w')
        cont = 0
        for instr in self.codigo:
            if (instr.arg == None):
                f.write("{} {}\n".format(str(cont), instr.instr))
            else:
                f.write("{} {} {}\n".format(str(cont), instr.instr, instr.arg))
            cont += 1
        f.close()

    def agregarVariableDefinida(self, nombre, lista):
        if (self.buscarVariableDefinida(nombre, lista) == False):
            lista.append(nombre)

    def buscarVariableDefinida(self, nombre, lista):
        for v in lista:
            if v == nombre:
                return True
        return False

    # Visit a parse tree produced by miniPythonParser#programMP.
    def visitProgramMP(self, ctx: miniPythonParser.ProgramMPContext):
        self.visitChildren(ctx)
        # self.printCode()
        return self.codigo

    # Visit a parse tree produced by miniPythonParser#statementMP.
    def visitStatementMP(self, ctx: miniPythonParser.StatementMPContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#defStatementMP.
    def visitDefStatementMP(self, ctx: miniPythonParser.DefStatementMPContext):
        cantidadParams = 0

        if (ctx.argList()):
            if (ctx.argList().IDENTIFIER()):
                cantidadParams = 1
            if (ctx.argList().moreArgs()):
                print(ctx.argList().moreArgs().getText())
                cantidadParams += len(ctx.argList().moreArgs().IDENTIFIER())

        if (ctx.IDENTIFIER().getText() != "Main"):
            self.parametrosDeclarados.append(cantidadParams)

        if (ctx.IDENTIFIER().getText() == "Main"):
            self.generate("DEF", "Main")
        else:
            self.funcionesDefinidas.append(ctx.IDENTIFIER().getText())
            self.generate("DEF", ctx.IDENTIFIER().getText())

        # Acá se debe de verificar el return value y return
        self.visit(ctx.argList())
        self.visit(ctx.sequence())
        if (ctx.IDENTIFIER().getText() == "Main"):
            self.generate("END", None)
        self.variablesLocalesDefinidas = []
        return None

    # Visit a parse tree produced by miniPythonParser#argListMP.
    def visitArgListMP(self, ctx: miniPythonParser.ArgListMPContext):
        if (ctx.IDENTIFIER() != None):
            self.generate("PUSH_LOCAL", ctx.IDENTIFIER().getText())
            self.agregarVariableDefinida(ctx.IDENTIFIER().getText(), self.variablesLocalesDefinidas)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#moreArgsMP.
    def visitMoreArgsMP(self, ctx: miniPythonParser.MoreArgsMPContext):
        for i in ctx.IDENTIFIER():
            self.generate("PUSH_LOCAL", i.getText())
            self.agregarVariableDefinida(i.getText(), self.variablesLocalesDefinidas)
            self.visitChildren(ctx)
        return None

    # Visit a parse tree produced by miniPythonParser#ifStatementMP.
    def visitIfStatementMP(self, ctx: miniPythonParser.IfStatementMPContext):
        self.visit(ctx.expression())
        etiq1 = self.instActual
        self.generate("JUMP_IF_FALSE", "0")
        self.visit(ctx.sequence()[0])
        if (ctx.ELSE()):
            etiq2 = self.instActual
            self.generate("JUMP_ABSOLUTE", "0")
            self.codigo[etiq1].arg = str(self.instActual)
            self.visit(ctx.sequence()[1])
            self.codigo[etiq2].arg = str(self.instActual)
        else:
            self.codigo[etiq1].arg = str(self.instActual)
        return None

    # Visit a parse tree produced by miniPythonParser#whileStatementMP.
    def visitWhileStatementMP(self, ctx: miniPythonParser.WhileStatementMPContext):
        etiq1 = self.instActual
        self.visit(ctx.expression())
        etiq2 = self.instActual
        self.generate("JUMP_IF_FALSE", "0")
        self.visit(ctx.sequence())
        self.generate("JUMP_ABSOLUTE", str(etiq1))
        self.codigo[etiq2].arg = str(self.instActual)
        self.visit(ctx.expression())
        return None

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
        self.visit(ctx.expression().additionExpression())
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
        self.visit(ctx.expressionList())
        self.visit(ctx.primitiveExpression())
        if (ctx.primitiveExpression().IDENTIFIER().getText() != "Main" and ctx.primitiveExpression().IDENTIFIER().getText() in self.funcionesDefinidas):
            contador = 0
            cantidadParam = 0
            for i in self.funcionesDefinidas:
                if (ctx.primitiveExpression().IDENTIFIER().getText() == i):
                    cantidadParam = self.parametrosDeclarados[contador]
                contador += 1
            self.generate("LOAD_GLOBAL", ctx.primitiveExpression().IDENTIFIER().getText())
            self.generate("CALL_FUNCTION", str(cantidadParam))
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
        for x in ctx.additionExpression():
            self.visit(x)
            if (ctx.MENQUE()):
                self.generate("COMPARE_OP", '<')
            elif (ctx.EQUALEQUAL()):
                self.generate("COMPARE_OP", '==')
            elif (ctx.MAYQUE()):
                self.generate("COMPARE_OP", '>')
            elif (ctx.MENQUEEQUAL()):
                self.generate("COMPARE_OP", '<=')
            elif (ctx.MAYQUEEQUAL()):
                self.generate("COMPARE_OP", '>=')
            elif (ctx.DIVEQUAL()):
                self.generate("COMPARE_OP", '/=')
            elif (ctx.MULTEQUAL()):
                self.generate("COMPARE_OP", '*=')
        return

    # Visit a parse tree produced by miniPythonParser#additionExpressionMP.
    def visitAdditionExpressionMP(self, ctx: miniPythonParser.AdditionExpressionMPContext):
        self.visit(ctx.multiplicationExpression())
        self.visit(ctx.additionFactor())
        return None

    # Visit a parse tree produced by miniPythonParser#additionFactorMP.
    def visitAdditionFactorMP(self, ctx: miniPythonParser.AdditionFactorMPContext):
        listSimbols = []
        listExpressions = []
        for x in ctx.getChildren():
            if(x.getText() == "+"):
                listSimbols.append(x.getText())
            elif(x.getText() == "-"):
                listSimbols.append(x.getText())
            else:
                listExpressions.append(x.getText())

        contador = 0
        for x in listExpressions:
            self.visit(ctx.multiplicationExpression()[contador])

            if(listSimbols[contador] == "+"):
                self.generate("BINARY_ADD", None)
            else:
                self.generate("BINARY_SUBSTRACT", None)
            contador += 1
        return

    # Visit a parse tree produced by miniPythonParser#multiplicationExpressionMP.
    def visitMultiplicationExpressionMP(self, ctx: miniPythonParser.MultiplicationExpressionMPContext):
        self.visit(ctx.elementExpression())
        self.visit(ctx.multiplicationFactor())
        return None

    # Visit a parse tree produced by miniPythonParser#multiplicationFactorMP.
    def visitMultiplicationFactorMP(self, ctx: miniPythonParser.MultiplicationFactorMPContext):
        listSimbols = []
        listExpressions = []
        for x in ctx.getChildren():
            if(x.getText() == "*"):
                listSimbols.append(x.getText())
            elif(x.getText() == "/"):
                listSimbols.append(x.getText())
            else:
                listExpressions.append(x.getText())

        contador = 0
        for x in listExpressions:
            self.visit(ctx.elementExpression()[contador])

            if(listSimbols[contador] == "*"):
                self.generate("BINARY_MULTIPLY", None)
            else:
                self.generate("BINARY_DIVIDE", None)
            contador += 1
        return

    # Visit a parse tree produced by miniPythonParser#elementExpressionMP.
    def visitElementExpressionMP(self, ctx: miniPythonParser.ElementExpressionMPContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miniPythonParser#elementAccessMP.
    def visitElementAccessMP(self, ctx: miniPythonParser.ElementAccessMPContext):
        self.visitChildren(ctx)
        if (self.elementAccess):
            self.elementAccess = False
        else:
            self.generate('BINARY_SUBSCR', None)
        return

    # Visit a parse tree produced by miniPythonParser#expressionListMP.
    def visitExpressionListMP(self, ctx: miniPythonParser.ExpressionListMPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPythonParser#moreExpressionsMP.
    def visitMoreExpressionsMP(self, ctx: miniPythonParser.MoreExpressionsMPContext):
        for e in reversed(ctx.expression()):
            self.visit(e)
        return len(ctx.expression())

    # Visit a parse tree produced by miniPythonParser#primitiveExpressionMP.
    def visitPrimitiveExpressionMP(self, ctx: miniPythonParser.PrimitiveExpressionMPContext):
        if (ctx.INTEGER()):
            self.generate("LOAD_CONST", ctx.INTEGER().getText())
        elif (ctx.FLOAT()):
            self.generate("LOAD_CONST", ctx.FLOAT().getText())
        elif (ctx.CHARCONTS()):
            self.generate("LOAD_CONST", ctx.CHARCONTS().getText())
        elif (ctx.STRING()):
            self.generate("LOAD_CONST", ctx.STRING().getText())
        if (ctx.IDENTIFIER() != None):
            if (ctx.PDER() == None and ctx.IDENTIFIER().getText() not in self.funcionesDefinidas):
                self.generate("LOAD_FAST", ctx.IDENTIFIER().getText())
        self.visitChildren(ctx)
        if (ctx.LEN()):
            self.generate("LOAD_GLOBAL", "len")
            self.generate("CALL_FUNCTION", "1")
        return

    # Visit a parse tree produced by miniPythonParser#listExpressionMP.
    def visitListExpressionMP(self, ctx: miniPythonParser.ListExpressionMPContext):
        self.visitChildren(ctx)
        cont = 0

        if (ctx.expressionList() != None):
            cont = 1
            for element in ctx.expressionList().moreExpressions().expression():
                cont += 1
        self.generate('BUILD_LIST', cont)
        return


del miniPythonParser
