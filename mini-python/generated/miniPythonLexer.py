# Generated from D:/Universidad/2022/Compiladores_e_Interpretes/Compiladores-E-Interpretes/mini-python\miniPython.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from antlr_denter.DenterHelper import DenterHelper
from miniPythonParser import miniPythonParser



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2!")
        buf.write("\u00bb\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\3\2\3\2\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n")
        buf.write("\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\17\3\17")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34")
        buf.write("\3\35\3\35\7\35\u009d\n\35\f\35\16\35\u00a0\13\35\3\36")
        buf.write("\3\36\3\36\7\36\u00a5\n\36\f\36\16\36\u00a8\13\36\3\37")
        buf.write("\3\37\3 \3 \3!\5!\u00af\n!\3!\3!\7!\u00b3\n!\f!\16!\u00b6")
        buf.write("\13!\3\"\3\"\3\"\3\"\2\2#\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37=\2?\2A C!\3\2\6\3\2\62;\3\2c|\4\2\13\13\"\"\6\2\13")
        buf.write("\f\17\17\"\"--\2\u00bd\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2")
        buf.write("\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!")
        buf.write("\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2A\3\2\2\2\2C\3\2\2\2\3E\3\2\2\2\5G\3\2\2\2\7I\3\2\2")
        buf.write("\2\tL\3\2\2\2\13N\3\2\2\2\rP\3\2\2\2\17R\3\2\2\2\21T\3")
        buf.write("\2\2\2\23V\3\2\2\2\25X\3\2\2\2\27Z\3\2\2\2\31\\\3\2\2")
        buf.write("\2\33_\3\2\2\2\35a\3\2\2\2\37c\3\2\2\2!e\3\2\2\2#h\3\2")
        buf.write("\2\2%m\3\2\2\2\'r\3\2\2\2)x\3\2\2\2+{\3\2\2\2-\177\3\2")
        buf.write("\2\2/\u0082\3\2\2\2\61\u0088\3\2\2\2\63\u008c\3\2\2\2")
        buf.write("\65\u0092\3\2\2\2\67\u0096\3\2\2\29\u009a\3\2\2\2;\u00a1")
        buf.write("\3\2\2\2=\u00a9\3\2\2\2?\u00ab\3\2\2\2A\u00ae\3\2\2\2")
        buf.write("C\u00b7\3\2\2\2EF\7.\2\2F\4\3\2\2\2GH\7=\2\2H\6\3\2\2")
        buf.write("\2IJ\7<\2\2JK\7?\2\2K\b\3\2\2\2LM\7*\2\2M\n\3\2\2\2NO")
        buf.write("\7+\2\2O\f\3\2\2\2PQ\7\u0080\2\2Q\16\3\2\2\2RS\7<\2\2")
        buf.write("S\20\3\2\2\2TU\7-\2\2U\22\3\2\2\2VW\7,\2\2W\24\3\2\2\2")
        buf.write("XY\7/\2\2Y\26\3\2\2\2Z[\7\61\2\2[\30\3\2\2\2\\]\7,\2\2")
        buf.write("]^\7,\2\2^\32\3\2\2\2_`\7\'\2\2`\34\3\2\2\2ab\7>\2\2b")
        buf.write("\36\3\2\2\2cd\7@\2\2d \3\2\2\2ef\7k\2\2fg\7h\2\2g\"\3")
        buf.write("\2\2\2hi\7v\2\2ij\7j\2\2jk\7g\2\2kl\7p\2\2l$\3\2\2\2m")
        buf.write("n\7g\2\2no\7n\2\2op\7u\2\2pq\7g\2\2q&\3\2\2\2rs\7y\2\2")
        buf.write("st\7j\2\2tu\7k\2\2uv\7n\2\2vw\7g\2\2w(\3\2\2\2xy\7f\2")
        buf.write("\2yz\7q\2\2z*\3\2\2\2{|\7n\2\2|}\7g\2\2}~\7v\2\2~,\3\2")
        buf.write("\2\2\177\u0080\7k\2\2\u0080\u0081\7p\2\2\u0081.\3\2\2")
        buf.write("\2\u0082\u0083\7d\2\2\u0083\u0084\7g\2\2\u0084\u0085\7")
        buf.write("i\2\2\u0085\u0086\7k\2\2\u0086\u0087\7p\2\2\u0087\60\3")
        buf.write("\2\2\2\u0088\u0089\7g\2\2\u0089\u008a\7p\2\2\u008a\u008b")
        buf.write("\7f\2\2\u008b\62\3\2\2\2\u008c\u008d\7e\2\2\u008d\u008e")
        buf.write("\7q\2\2\u008e\u008f\7p\2\2\u008f\u0090\7u\2\2\u0090\u0091")
        buf.write("\7v\2\2\u0091\64\3\2\2\2\u0092\u0093\7x\2\2\u0093\u0094")
        buf.write("\7c\2\2\u0094\u0095\7t\2\2\u0095\66\3\2\2\2\u0096\u0097")
        buf.write("\7f\2\2\u0097\u0098\7g\2\2\u0098\u0099\7h\2\2\u00998\3")
        buf.write("\2\2\2\u009a\u009e\5=\37\2\u009b\u009d\5=\37\2\u009c\u009b")
        buf.write("\3\2\2\2\u009d\u00a0\3\2\2\2\u009e\u009c\3\2\2\2\u009e")
        buf.write("\u009f\3\2\2\2\u009f:\3\2\2\2\u00a0\u009e\3\2\2\2\u00a1")
        buf.write("\u00a6\5? \2\u00a2\u00a5\5? \2\u00a3\u00a5\5=\37\2\u00a4")
        buf.write("\u00a2\3\2\2\2\u00a4\u00a3\3\2\2\2\u00a5\u00a8\3\2\2\2")
        buf.write("\u00a6\u00a4\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7<\3\2\2")
        buf.write("\2\u00a8\u00a6\3\2\2\2\u00a9\u00aa\t\2\2\2\u00aa>\3\2")
        buf.write("\2\2\u00ab\u00ac\t\3\2\2\u00ac@\3\2\2\2\u00ad\u00af\7")
        buf.write("\17\2\2\u00ae\u00ad\3\2\2\2\u00ae\u00af\3\2\2\2\u00af")
        buf.write("\u00b0\3\2\2\2\u00b0\u00b4\7\f\2\2\u00b1\u00b3\t\4\2\2")
        buf.write("\u00b2\u00b1\3\2\2\2\u00b3\u00b6\3\2\2\2\u00b4\u00b2\3")
        buf.write("\2\2\2\u00b4\u00b5\3\2\2\2\u00b5B\3\2\2\2\u00b6\u00b4")
        buf.write("\3\2\2\2\u00b7\u00b8\t\5\2\2\u00b8\u00b9\3\2\2\2\u00b9")
        buf.write("\u00ba\b\"\2\2\u00baD\3\2\2\2\b\2\u009e\u00a4\u00a6\u00ae")
        buf.write("\u00b4\3\b\2\2")
        return buf.getvalue()


class miniPythonLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMA = 1
    PyCOMA = 2
    ASIGN = 3
    PIZQ = 4
    PDER = 5
    VIR = 6
    DOSPUNT = 7
    MAS = 8
    MULT = 9
    MEN = 10
    DIV = 11
    POT = 12
    MOD = 13
    MENQUE = 14
    MAYQUE = 15
    IF = 16
    THEN = 17
    ELSE = 18
    WHILE = 19
    DO = 20
    LET = 21
    IN = 22
    BEGIN = 23
    END = 24
    CONST = 25
    VAR = 26
    DEF = 27
    NUM = 28
    ID = 29
    NEWLINE = 30
    WS = 31

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "';'", "':='", "'('", "')'", "'~'", "':'", "'+'", "'*'", 
            "'-'", "'/'", "'**'", "'%'", "'<'", "'>'", "'if'", "'then'", 
            "'else'", "'while'", "'do'", "'let'", "'in'", "'begin'", "'end'", 
            "'const'", "'var'", "'def'" ]

    symbolicNames = [ "<INVALID>",
            "COMA", "PyCOMA", "ASIGN", "PIZQ", "PDER", "VIR", "DOSPUNT", 
            "MAS", "MULT", "MEN", "DIV", "POT", "MOD", "MENQUE", "MAYQUE", 
            "IF", "THEN", "ELSE", "WHILE", "DO", "LET", "IN", "BEGIN", "END", 
            "CONST", "VAR", "DEF", "NUM", "ID", "NEWLINE", "WS" ]

    ruleNames = [ "COMA", "PyCOMA", "ASIGN", "PIZQ", "PDER", "VIR", "DOSPUNT", 
                  "MAS", "MULT", "MEN", "DIV", "POT", "MOD", "MENQUE", "MAYQUE", 
                  "IF", "THEN", "ELSE", "WHILE", "DO", "LET", "IN", "BEGIN", 
                  "END", "CONST", "VAR", "DEF", "NUM", "ID", "DIGIT", "LETTER", 
                  "NEWLINE", "WS" ]

    grammarFileName = "miniPython.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    class MyCoolDenter(DenterHelper):
        def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
            super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
            self.lexer: miniPythonLexer = lexer

        def pull_token(self):
            return super(miniPythonLexer, self.lexer).nextToken()

    denter = None

    def nextToken(self):
        if not self.denter:
            self.denter = self.MyCoolDenter(self, self.NEWLINE, miniPythonParser.INDENT, miniPythonParser.DEDENT, False)
        return self.denter.next_token()


