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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\37")
        buf.write("\u00b1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\5")
        buf.write("\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\7\33\u0093\n\33\f\33\16\33\u0096")
        buf.write("\13\33\3\34\3\34\3\34\7\34\u009b\n\34\f\34\16\34\u009e")
        buf.write("\13\34\3\35\3\35\3\36\3\36\3\37\5\37\u00a5\n\37\3\37\3")
        buf.write("\37\7\37\u00a9\n\37\f\37\16\37\u00ac\13\37\3 \3 \3 \3")
        buf.write(" \2\2!\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write("\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\2;\2=\36?\37\3\2\6\3\2\62")
        buf.write(";\3\2c|\4\2\13\13\"\"\6\2\13\f\17\17\"\"--\2\u00b3\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write("\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write("/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\3A\3\2\2\2\5C\3\2\2\2\7")
        buf.write("F\3\2\2\2\tH\3\2\2\2\13J\3\2\2\2\rL\3\2\2\2\17N\3\2\2")
        buf.write("\2\21P\3\2\2\2\23R\3\2\2\2\25T\3\2\2\2\27V\3\2\2\2\31")
        buf.write("Y\3\2\2\2\33[\3\2\2\2\35]\3\2\2\2\37_\3\2\2\2!b\3\2\2")
        buf.write("\2#g\3\2\2\2%l\3\2\2\2\'r\3\2\2\2)u\3\2\2\2+y\3\2\2\2")
        buf.write("-|\3\2\2\2/\u0082\3\2\2\2\61\u0086\3\2\2\2\63\u008c\3")
        buf.write("\2\2\2\65\u0090\3\2\2\2\67\u0097\3\2\2\29\u009f\3\2\2")
        buf.write("\2;\u00a1\3\2\2\2=\u00a4\3\2\2\2?\u00ad\3\2\2\2AB\7=\2")
        buf.write("\2B\4\3\2\2\2CD\7<\2\2DE\7?\2\2E\6\3\2\2\2FG\7*\2\2G\b")
        buf.write("\3\2\2\2HI\7+\2\2I\n\3\2\2\2JK\7\u0080\2\2K\f\3\2\2\2")
        buf.write("LM\7<\2\2M\16\3\2\2\2NO\7-\2\2O\20\3\2\2\2PQ\7,\2\2Q\22")
        buf.write("\3\2\2\2RS\7/\2\2S\24\3\2\2\2TU\7\61\2\2U\26\3\2\2\2V")
        buf.write("W\7,\2\2WX\7,\2\2X\30\3\2\2\2YZ\7\'\2\2Z\32\3\2\2\2[\\")
        buf.write("\7>\2\2\\\34\3\2\2\2]^\7@\2\2^\36\3\2\2\2_`\7k\2\2`a\7")
        buf.write("h\2\2a \3\2\2\2bc\7v\2\2cd\7j\2\2de\7g\2\2ef\7p\2\2f\"")
        buf.write("\3\2\2\2gh\7g\2\2hi\7n\2\2ij\7u\2\2jk\7g\2\2k$\3\2\2\2")
        buf.write("lm\7y\2\2mn\7j\2\2no\7k\2\2op\7n\2\2pq\7g\2\2q&\3\2\2")
        buf.write("\2rs\7f\2\2st\7q\2\2t(\3\2\2\2uv\7n\2\2vw\7g\2\2wx\7v")
        buf.write("\2\2x*\3\2\2\2yz\7k\2\2z{\7p\2\2{,\3\2\2\2|}\7d\2\2}~")
        buf.write("\7g\2\2~\177\7i\2\2\177\u0080\7k\2\2\u0080\u0081\7p\2")
        buf.write("\2\u0081.\3\2\2\2\u0082\u0083\7g\2\2\u0083\u0084\7p\2")
        buf.write("\2\u0084\u0085\7f\2\2\u0085\60\3\2\2\2\u0086\u0087\7e")
        buf.write("\2\2\u0087\u0088\7q\2\2\u0088\u0089\7p\2\2\u0089\u008a")
        buf.write("\7u\2\2\u008a\u008b\7v\2\2\u008b\62\3\2\2\2\u008c\u008d")
        buf.write("\7x\2\2\u008d\u008e\7c\2\2\u008e\u008f\7t\2\2\u008f\64")
        buf.write("\3\2\2\2\u0090\u0094\59\35\2\u0091\u0093\59\35\2\u0092")
        buf.write("\u0091\3\2\2\2\u0093\u0096\3\2\2\2\u0094\u0092\3\2\2\2")
        buf.write("\u0094\u0095\3\2\2\2\u0095\66\3\2\2\2\u0096\u0094\3\2")
        buf.write("\2\2\u0097\u009c\5;\36\2\u0098\u009b\5;\36\2\u0099\u009b")
        buf.write("\59\35\2\u009a\u0098\3\2\2\2\u009a\u0099\3\2\2\2\u009b")
        buf.write("\u009e\3\2\2\2\u009c\u009a\3\2\2\2\u009c\u009d\3\2\2\2")
        buf.write("\u009d8\3\2\2\2\u009e\u009c\3\2\2\2\u009f\u00a0\t\2\2")
        buf.write("\2\u00a0:\3\2\2\2\u00a1\u00a2\t\3\2\2\u00a2<\3\2\2\2\u00a3")
        buf.write("\u00a5\7\17\2\2\u00a4\u00a3\3\2\2\2\u00a4\u00a5\3\2\2")
        buf.write("\2\u00a5\u00a6\3\2\2\2\u00a6\u00aa\7\f\2\2\u00a7\u00a9")
        buf.write("\t\4\2\2\u00a8\u00a7\3\2\2\2\u00a9\u00ac\3\2\2\2\u00aa")
        buf.write("\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab>\3\2\2\2\u00ac")
        buf.write("\u00aa\3\2\2\2\u00ad\u00ae\t\5\2\2\u00ae\u00af\3\2\2\2")
        buf.write("\u00af\u00b0\b \2\2\u00b0@\3\2\2\2\b\2\u0094\u009a\u009c")
        buf.write("\u00a4\u00aa\3\b\2\2")
        return buf.getvalue()


class miniPythonLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PyCOMA = 1
    ASIGN = 2
    PIZQ = 3
    PDER = 4
    VIR = 5
    DOSPUNT = 6
    MAS = 7
    MULT = 8
    MEN = 9
    DIV = 10
    POT = 11
    MOD = 12
    MENQUE = 13
    MAYQUE = 14
    IF = 15
    THEN = 16
    ELSE = 17
    WHILE = 18
    DO = 19
    LET = 20
    IN = 21
    BEGIN = 22
    END = 23
    CONST = 24
    VAR = 25
    NUM = 26
    ID = 27
    NEWLINE = 28
    WS = 29

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "':='", "'('", "')'", "'~'", "':'", "'+'", "'*'", "'-'", 
            "'/'", "'**'", "'%'", "'<'", "'>'", "'if'", "'then'", "'else'", 
            "'while'", "'do'", "'let'", "'in'", "'begin'", "'end'", "'const'", 
            "'var'" ]

    symbolicNames = [ "<INVALID>",
            "PyCOMA", "ASIGN", "PIZQ", "PDER", "VIR", "DOSPUNT", "MAS", 
            "MULT", "MEN", "DIV", "POT", "MOD", "MENQUE", "MAYQUE", "IF", 
            "THEN", "ELSE", "WHILE", "DO", "LET", "IN", "BEGIN", "END", 
            "CONST", "VAR", "NUM", "ID", "NEWLINE", "WS" ]

    ruleNames = [ "PyCOMA", "ASIGN", "PIZQ", "PDER", "VIR", "DOSPUNT", "MAS", 
                  "MULT", "MEN", "DIV", "POT", "MOD", "MENQUE", "MAYQUE", 
                  "IF", "THEN", "ELSE", "WHILE", "DO", "LET", "IN", "BEGIN", 
                  "END", "CONST", "VAR", "NUM", "ID", "DIGIT", "LETTER", 
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


