# Generated from D:/Universidad/Compiladores_e_Interpretes/Compiladores-E-Interpretes/mini-python\miniPython.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2/")
        buf.write("\u0143\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\3\2\3\2\3\3\3\3\3\4\3\4")
        buf.write("\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3")
        buf.write("\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3")
        buf.write("#\3#\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3")
        buf.write("&\3\'\3\'\7\'\u00df\n\'\f\'\16\'\u00e2\13\'\3(\3(\3(\7")
        buf.write("(\u00e7\n(\f(\16(\u00ea\13(\3)\3)\3)\3)\7)\u00f0\n)\f")
        buf.write(")\16)\u00f3\13)\3)\3)\3)\3)\3)\7)\u00fa\n)\f)\16)\u00fd")
        buf.write("\13)\3)\5)\u0100\n)\3*\6*\u0103\n*\r*\16*\u0104\3*\3*")
        buf.write("\6*\u0109\n*\r*\16*\u010a\3+\3+\3+\3+\7+\u0111\n+\f+\16")
        buf.write("+\u0114\13+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,")
        buf.write("\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\5,\u012e\n,\3-\3-\3.\3")
        buf.write(".\3/\3/\3\60\5\60\u0137\n\60\3\60\3\60\7\60\u013b\n\60")
        buf.write("\f\60\16\60\u013e\13\60\3\61\3\61\3\61\3\61\2\2\62\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y\2[\2]\2_.a/\3\2\7\3\2\62;\6\2\"\"C\\aac|\3\2\63")
        buf.write(";\4\2\13\13\"\"\6\2\13\f\17\17\"\"--\2\u0163\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\3c\3\2\2\2\5e\3")
        buf.write("\2\2\2\7g\3\2\2\2\tj\3\2\2\2\13l\3\2\2\2\rn\3\2\2\2\17")
        buf.write("p\3\2\2\2\21r\3\2\2\2\23t\3\2\2\2\25v\3\2\2\2\27x\3\2")
        buf.write("\2\2\31z\3\2\2\2\33|\3\2\2\2\35~\3\2\2\2\37\u0081\3\2")
        buf.write("\2\2!\u0083\3\2\2\2#\u0085\3\2\2\2%\u0087\3\2\2\2\'\u008a")
        buf.write("\3\2\2\2)\u008d\3\2\2\2+\u0090\3\2\2\2-\u0092\3\2\2\2")
        buf.write("/\u0095\3\2\2\2\61\u009a\3\2\2\2\63\u009f\3\2\2\2\65\u00a5")
        buf.write("\3\2\2\2\67\u00a8\3\2\2\29\u00ac\3\2\2\2;\u00af\3\2\2")
        buf.write("\2=\u00b5\3\2\2\2?\u00b9\3\2\2\2A\u00bf\3\2\2\2C\u00c3")
        buf.write("\3\2\2\2E\u00c7\3\2\2\2G\u00cb\3\2\2\2I\u00cf\3\2\2\2")
        buf.write("K\u00d6\3\2\2\2M\u00dc\3\2\2\2O\u00e3\3\2\2\2Q\u00ff\3")
        buf.write("\2\2\2S\u0102\3\2\2\2U\u010c\3\2\2\2W\u012d\3\2\2\2Y\u012f")
        buf.write("\3\2\2\2[\u0131\3\2\2\2]\u0133\3\2\2\2_\u0136\3\2\2\2")
        buf.write("a\u013f\3\2\2\2cd\7.\2\2d\4\3\2\2\2ef\7=\2\2f\6\3\2\2")
        buf.write("\2gh\7<\2\2hi\7?\2\2i\b\3\2\2\2jk\7*\2\2k\n\3\2\2\2lm")
        buf.write("\7+\2\2m\f\3\2\2\2no\7]\2\2o\16\3\2\2\2pq\7_\2\2q\20\3")
        buf.write("\2\2\2rs\7\u0080\2\2s\22\3\2\2\2tu\7<\2\2u\24\3\2\2\2")
        buf.write("vw\7-\2\2w\26\3\2\2\2xy\7,\2\2y\30\3\2\2\2z{\7/\2\2{\32")
        buf.write("\3\2\2\2|}\7\61\2\2}\34\3\2\2\2~\177\7,\2\2\177\u0080")
        buf.write("\7,\2\2\u0080\36\3\2\2\2\u0081\u0082\7\'\2\2\u0082 \3")
        buf.write("\2\2\2\u0083\u0084\7>\2\2\u0084\"\3\2\2\2\u0085\u0086")
        buf.write("\7@\2\2\u0086$\3\2\2\2\u0087\u0088\7>\2\2\u0088\u0089")
        buf.write("\7?\2\2\u0089&\3\2\2\2\u008a\u008b\7@\2\2\u008b\u008c")
        buf.write("\7?\2\2\u008c(\3\2\2\2\u008d\u008e\7?\2\2\u008e\u008f")
        buf.write("\7?\2\2\u008f*\3\2\2\2\u0090\u0091\7?\2\2\u0091,\3\2\2")
        buf.write("\2\u0092\u0093\7k\2\2\u0093\u0094\7h\2\2\u0094.\3\2\2")
        buf.write("\2\u0095\u0096\7v\2\2\u0096\u0097\7j\2\2\u0097\u0098\7")
        buf.write("g\2\2\u0098\u0099\7p\2\2\u0099\60\3\2\2\2\u009a\u009b")
        buf.write("\7g\2\2\u009b\u009c\7n\2\2\u009c\u009d\7u\2\2\u009d\u009e")
        buf.write("\7g\2\2\u009e\62\3\2\2\2\u009f\u00a0\7y\2\2\u00a0\u00a1")
        buf.write("\7j\2\2\u00a1\u00a2\7k\2\2\u00a2\u00a3\7n\2\2\u00a3\u00a4")
        buf.write("\7g\2\2\u00a4\64\3\2\2\2\u00a5\u00a6\7f\2\2\u00a6\u00a7")
        buf.write("\7q\2\2\u00a7\66\3\2\2\2\u00a8\u00a9\7n\2\2\u00a9\u00aa")
        buf.write("\7g\2\2\u00aa\u00ab\7v\2\2\u00ab8\3\2\2\2\u00ac\u00ad")
        buf.write("\7k\2\2\u00ad\u00ae\7p\2\2\u00ae:\3\2\2\2\u00af\u00b0")
        buf.write("\7d\2\2\u00b0\u00b1\7g\2\2\u00b1\u00b2\7i\2\2\u00b2\u00b3")
        buf.write("\7k\2\2\u00b3\u00b4\7p\2\2\u00b4<\3\2\2\2\u00b5\u00b6")
        buf.write("\7g\2\2\u00b6\u00b7\7p\2\2\u00b7\u00b8\7f\2\2\u00b8>\3")
        buf.write("\2\2\2\u00b9\u00ba\7e\2\2\u00ba\u00bb\7q\2\2\u00bb\u00bc")
        buf.write("\7p\2\2\u00bc\u00bd\7u\2\2\u00bd\u00be\7v\2\2\u00be@\3")
        buf.write("\2\2\2\u00bf\u00c0\7x\2\2\u00c0\u00c1\7c\2\2\u00c1\u00c2")
        buf.write("\7t\2\2\u00c2B\3\2\2\2\u00c3\u00c4\7f\2\2\u00c4\u00c5")
        buf.write("\7g\2\2\u00c5\u00c6\7h\2\2\u00c6D\3\2\2\2\u00c7\u00c8")
        buf.write("\7n\2\2\u00c8\u00c9\7g\2\2\u00c9\u00ca\7p\2\2\u00caF\3")
        buf.write("\2\2\2\u00cb\u00cc\7h\2\2\u00cc\u00cd\7q\2\2\u00cd\u00ce")
        buf.write("\7t\2\2\u00ceH\3\2\2\2\u00cf\u00d0\7t\2\2\u00d0\u00d1")
        buf.write("\7g\2\2\u00d1\u00d2\7v\2\2\u00d2\u00d3\7w\2\2\u00d3\u00d4")
        buf.write("\7t\2\2\u00d4\u00d5\7p\2\2\u00d5J\3\2\2\2\u00d6\u00d7")
        buf.write("\7r\2\2\u00d7\u00d8\7t\2\2\u00d8\u00d9\7k\2\2\u00d9\u00da")
        buf.write("\7p\2\2\u00da\u00db\7v\2\2\u00dbL\3\2\2\2\u00dc\u00e0")
        buf.write("\5]/\2\u00dd\u00df\5Y-\2\u00de\u00dd\3\2\2\2\u00df\u00e2")
        buf.write("\3\2\2\2\u00e0\u00de\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1")
        buf.write("N\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e3\u00e8\5[.\2\u00e4")
        buf.write("\u00e7\5[.\2\u00e5\u00e7\5Y-\2\u00e6\u00e4\3\2\2\2\u00e6")
        buf.write("\u00e5\3\2\2\2\u00e7\u00ea\3\2\2\2\u00e8\u00e6\3\2\2\2")
        buf.write("\u00e8\u00e9\3\2\2\2\u00e9P\3\2\2\2\u00ea\u00e8\3\2\2")
        buf.write("\2\u00eb\u00f1\7)\2\2\u00ec\u00f0\5[.\2\u00ed\u00f0\5")
        buf.write("Y-\2\u00ee\u00f0\5W,\2\u00ef\u00ec\3\2\2\2\u00ef\u00ed")
        buf.write("\3\2\2\2\u00ef\u00ee\3\2\2\2\u00f0\u00f3\3\2\2\2\u00f1")
        buf.write("\u00ef\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f4\3\2\2\2")
        buf.write("\u00f3\u00f1\3\2\2\2\u00f4\u0100\7)\2\2\u00f5\u00fb\7")
        buf.write("$\2\2\u00f6\u00fa\5[.\2\u00f7\u00fa\5Y-\2\u00f8\u00fa")
        buf.write("\5W,\2\u00f9\u00f6\3\2\2\2\u00f9\u00f7\3\2\2\2\u00f9\u00f8")
        buf.write("\3\2\2\2\u00fa\u00fd\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fb")
        buf.write("\u00fc\3\2\2\2\u00fc\u00fe\3\2\2\2\u00fd\u00fb\3\2\2\2")
        buf.write("\u00fe\u0100\7$\2\2\u00ff\u00eb\3\2\2\2\u00ff\u00f5\3")
        buf.write("\2\2\2\u0100R\3\2\2\2\u0101\u0103\5Y-\2\u0102\u0101\3")
        buf.write("\2\2\2\u0103\u0104\3\2\2\2\u0104\u0102\3\2\2\2\u0104\u0105")
        buf.write("\3\2\2\2\u0105\u0106\3\2\2\2\u0106\u0108\13\2\2\2\u0107")
        buf.write("\u0109\5Y-\2\u0108\u0107\3\2\2\2\u0109\u010a\3\2\2\2\u010a")
        buf.write("\u0108\3\2\2\2\u010a\u010b\3\2\2\2\u010bT\3\2\2\2\u010c")
        buf.write("\u0112\7)\2\2\u010d\u0111\5[.\2\u010e\u0111\5Y-\2\u010f")
        buf.write("\u0111\5W,\2\u0110\u010d\3\2\2\2\u0110\u010e\3\2\2\2\u0110")
        buf.write("\u010f\3\2\2\2\u0111\u0114\3\2\2\2\u0112\u0110\3\2\2\2")
        buf.write("\u0112\u0113\3\2\2\2\u0113\u0115\3\2\2\2\u0114\u0112\3")
        buf.write("\2\2\2\u0115\u0116\7)\2\2\u0116V\3\2\2\2\u0117\u012e\5")
        buf.write("\3\2\2\u0118\u012e\5\5\3\2\u0119\u012e\5\7\4\2\u011a\u012e")
        buf.write("\5\t\5\2\u011b\u012e\5\13\6\2\u011c\u012e\5\r\7\2\u011d")
        buf.write("\u012e\5\17\b\2\u011e\u012e\5\21\t\2\u011f\u012e\5\23")
        buf.write("\n\2\u0120\u012e\5\25\13\2\u0121\u012e\5\27\f\2\u0122")
        buf.write("\u012e\5\31\r\2\u0123\u012e\5\33\16\2\u0124\u012e\5\35")
        buf.write("\17\2\u0125\u0126\5\37\20\2\u0126\u0127\5!\21\2\u0127")
        buf.write("\u012e\3\2\2\2\u0128\u012e\5#\22\2\u0129\u012e\5%\23\2")
        buf.write("\u012a\u012e\5\'\24\2\u012b\u012e\5)\25\2\u012c\u012e")
        buf.write("\5+\26\2\u012d\u0117\3\2\2\2\u012d\u0118\3\2\2\2\u012d")
        buf.write("\u0119\3\2\2\2\u012d\u011a\3\2\2\2\u012d\u011b\3\2\2\2")
        buf.write("\u012d\u011c\3\2\2\2\u012d\u011d\3\2\2\2\u012d\u011e\3")
        buf.write("\2\2\2\u012d\u011f\3\2\2\2\u012d\u0120\3\2\2\2\u012d\u0121")
        buf.write("\3\2\2\2\u012d\u0122\3\2\2\2\u012d\u0123\3\2\2\2\u012d")
        buf.write("\u0124\3\2\2\2\u012d\u0125\3\2\2\2\u012d\u0128\3\2\2\2")
        buf.write("\u012d\u0129\3\2\2\2\u012d\u012a\3\2\2\2\u012d\u012b\3")
        buf.write("\2\2\2\u012d\u012c\3\2\2\2\u012eX\3\2\2\2\u012f\u0130")
        buf.write("\t\2\2\2\u0130Z\3\2\2\2\u0131\u0132\t\3\2\2\u0132\\\3")
        buf.write("\2\2\2\u0133\u0134\t\4\2\2\u0134^\3\2\2\2\u0135\u0137")
        buf.write("\7\17\2\2\u0136\u0135\3\2\2\2\u0136\u0137\3\2\2\2\u0137")
        buf.write("\u0138\3\2\2\2\u0138\u013c\7\f\2\2\u0139\u013b\t\5\2\2")
        buf.write("\u013a\u0139\3\2\2\2\u013b\u013e\3\2\2\2\u013c\u013a\3")
        buf.write("\2\2\2\u013c\u013d\3\2\2\2\u013d`\3\2\2\2\u013e\u013c")
        buf.write("\3\2\2\2\u013f\u0140\t\6\2\2\u0140\u0141\3\2\2\2\u0141")
        buf.write("\u0142\b\61\2\2\u0142b\3\2\2\2\22\2\u00e0\u00e6\u00e8")
        buf.write("\u00ef\u00f1\u00f9\u00fb\u00ff\u0104\u010a\u0110\u0112")
        buf.write("\u012d\u0136\u013c\3\b\2\2")
        return buf.getvalue()


class miniPythonLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMA = 1
    PyCOMA = 2
    ASIGN = 3
    PIZQ = 4
    PDER = 5
    CIZQ = 6
    CDER = 7
    VIR = 8
    DOSPUNT = 9
    MAS = 10
    MULT = 11
    MEN = 12
    DIV = 13
    POT = 14
    MOD = 15
    MENQUE = 16
    MAYQUE = 17
    MENQUEEQUAL = 18
    MAYQUEEQUAL = 19
    EQUALEQUAL = 20
    EQUAL = 21
    IF = 22
    THEN = 23
    ELSE = 24
    WHILE = 25
    DO = 26
    LET = 27
    IN = 28
    BEGIN = 29
    END = 30
    CONST = 31
    VAR = 32
    DEF = 33
    LEN = 34
    FOR = 35
    RETURN = 36
    PRINT = 37
    NUM = 38
    ID = 39
    STRING = 40
    FLOAT = 41
    CHARCONTS = 42
    SIMBOLS = 43
    NEWLINE = 44
    WS = 45

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "';'", "':='", "'('", "')'", "'['", "']'", "'~'", "':'", 
            "'+'", "'*'", "'-'", "'/'", "'**'", "'%'", "'<'", "'>'", "'<='", 
            "'>='", "'=='", "'='", "'if'", "'then'", "'else'", "'while'", 
            "'do'", "'let'", "'in'", "'begin'", "'end'", "'const'", "'var'", 
            "'def'", "'len'", "'for'", "'return'", "'print'" ]

    symbolicNames = [ "<INVALID>",
            "COMA", "PyCOMA", "ASIGN", "PIZQ", "PDER", "CIZQ", "CDER", "VIR", 
            "DOSPUNT", "MAS", "MULT", "MEN", "DIV", "POT", "MOD", "MENQUE", 
            "MAYQUE", "MENQUEEQUAL", "MAYQUEEQUAL", "EQUALEQUAL", "EQUAL", 
            "IF", "THEN", "ELSE", "WHILE", "DO", "LET", "IN", "BEGIN", "END", 
            "CONST", "VAR", "DEF", "LEN", "FOR", "RETURN", "PRINT", "NUM", 
            "ID", "STRING", "FLOAT", "CHARCONTS", "SIMBOLS", "NEWLINE", 
            "WS" ]

    ruleNames = [ "COMA", "PyCOMA", "ASIGN", "PIZQ", "PDER", "CIZQ", "CDER", 
                  "VIR", "DOSPUNT", "MAS", "MULT", "MEN", "DIV", "POT", 
                  "MOD", "MENQUE", "MAYQUE", "MENQUEEQUAL", "MAYQUEEQUAL", 
                  "EQUALEQUAL", "EQUAL", "IF", "THEN", "ELSE", "WHILE", 
                  "DO", "LET", "IN", "BEGIN", "END", "CONST", "VAR", "DEF", 
                  "LEN", "FOR", "RETURN", "PRINT", "NUM", "ID", "STRING", 
                  "FLOAT", "CHARCONTS", "SIMBOLS", "DIGIT", "LETTER", "DIGITNOTZERO", 
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


