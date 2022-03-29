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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\62")
        buf.write("\u0178\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7")
        buf.write("\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3\"")
        buf.write("\3\"\3\"\3\"\3#\3#\3#\3#\3$\3$\3$\3$\3%\3%\3%\3%\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\7(\u00e7")
        buf.write("\n(\f(\16(\u00ea\13(\3(\5(\u00ed\n(\3)\3)\3)\7)\u00f2")
        buf.write("\n)\f)\16)\u00f5\13)\3*\3*\3*\3*\7*\u00fb\n*\f*\16*\u00fe")
        buf.write("\13*\3*\3*\3*\3*\3*\7*\u0105\n*\f*\16*\u0108\13*\3*\5")
        buf.write("*\u010b\n*\3+\3+\5+\u010f\n+\3+\3+\6+\u0113\n+\r+\16+")
        buf.write("\u0114\3+\3+\6+\u0119\n+\r+\16+\u011a\3+\3+\6+\u011f\n")
        buf.write("+\r+\16+\u0120\5+\u0123\n+\3,\3,\3,\3,\7,\u0129\n,\f,")
        buf.write("\16,\u012c\13,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-")
        buf.write("\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u0146\n-\3.\3.\7")
        buf.write(".\u014a\n.\f.\16.\u014d\13.\3.\3.\3.\3.\3/\3/\3/\3/\3")
        buf.write("/\7/\u0158\n/\f/\16/\u015b\13/\3/\3/\3/\3/\3/\3/\3/\3")
        buf.write("/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\5\63\u016c\n\63\3")
        buf.write("\63\3\63\7\63\u0170\n\63\f\63\16\63\u0173\13\63\3\64\3")
        buf.write("\64\3\64\3\64\3\u0159\2\65\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\2a\2c\2e\61")
        buf.write("g\62\3\2\b\4\2\f\f\17\17\3\2\62;\6\2\"\"C\\aac|\3\2\63")
        buf.write(";\4\2\13\13\"\"\7\2\13\f\17\17\"\"%%--\2\u01a0\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\3i\3\2\2\2\5k\3\2\2\2\7m\3\2\2\2\t")
        buf.write("p\3\2\2\2\13r\3\2\2\2\rt\3\2\2\2\17v\3\2\2\2\21x\3\2\2")
        buf.write("\2\23z\3\2\2\2\25|\3\2\2\2\27~\3\2\2\2\31\u0080\3\2\2")
        buf.write("\2\33\u0082\3\2\2\2\35\u0084\3\2\2\2\37\u0087\3\2\2\2")
        buf.write("!\u0089\3\2\2\2#\u008b\3\2\2\2%\u008d\3\2\2\2\'\u0090")
        buf.write("\3\2\2\2)\u0093\3\2\2\2+\u0096\3\2\2\2-\u0098\3\2\2\2")
        buf.write("/\u009a\3\2\2\2\61\u009d\3\2\2\2\63\u00a2\3\2\2\2\65\u00a7")
        buf.write("\3\2\2\2\67\u00ad\3\2\2\29\u00b0\3\2\2\2;\u00b4\3\2\2")
        buf.write("\2=\u00b7\3\2\2\2?\u00bd\3\2\2\2A\u00c1\3\2\2\2C\u00c7")
        buf.write("\3\2\2\2E\u00cb\3\2\2\2G\u00cf\3\2\2\2I\u00d3\3\2\2\2")
        buf.write("K\u00d7\3\2\2\2M\u00de\3\2\2\2O\u00ec\3\2\2\2Q\u00ee\3")
        buf.write("\2\2\2S\u010a\3\2\2\2U\u0122\3\2\2\2W\u0124\3\2\2\2Y\u0145")
        buf.write("\3\2\2\2[\u0147\3\2\2\2]\u0152\3\2\2\2_\u0164\3\2\2\2")
        buf.write("a\u0166\3\2\2\2c\u0168\3\2\2\2e\u016b\3\2\2\2g\u0174\3")
        buf.write("\2\2\2ij\7.\2\2j\4\3\2\2\2kl\7=\2\2l\6\3\2\2\2mn\7<\2")
        buf.write("\2no\7?\2\2o\b\3\2\2\2pq\7*\2\2q\n\3\2\2\2rs\7+\2\2s\f")
        buf.write("\3\2\2\2tu\7]\2\2u\16\3\2\2\2vw\7_\2\2w\20\3\2\2\2xy\7")
        buf.write("\u0080\2\2y\22\3\2\2\2z{\7<\2\2{\24\3\2\2\2|}\7-\2\2}")
        buf.write("\26\3\2\2\2~\177\7,\2\2\177\30\3\2\2\2\u0080\u0081\7/")
        buf.write("\2\2\u0081\32\3\2\2\2\u0082\u0083\7\61\2\2\u0083\34\3")
        buf.write("\2\2\2\u0084\u0085\7,\2\2\u0085\u0086\7,\2\2\u0086\36")
        buf.write("\3\2\2\2\u0087\u0088\7\'\2\2\u0088 \3\2\2\2\u0089\u008a")
        buf.write("\7>\2\2\u008a\"\3\2\2\2\u008b\u008c\7@\2\2\u008c$\3\2")
        buf.write("\2\2\u008d\u008e\7>\2\2\u008e\u008f\7?\2\2\u008f&\3\2")
        buf.write("\2\2\u0090\u0091\7@\2\2\u0091\u0092\7?\2\2\u0092(\3\2")
        buf.write("\2\2\u0093\u0094\7?\2\2\u0094\u0095\7?\2\2\u0095*\3\2")
        buf.write("\2\2\u0096\u0097\7?\2\2\u0097,\3\2\2\2\u0098\u0099\7\60")
        buf.write("\2\2\u0099.\3\2\2\2\u009a\u009b\7k\2\2\u009b\u009c\7h")
        buf.write("\2\2\u009c\60\3\2\2\2\u009d\u009e\7v\2\2\u009e\u009f\7")
        buf.write("j\2\2\u009f\u00a0\7g\2\2\u00a0\u00a1\7p\2\2\u00a1\62\3")
        buf.write("\2\2\2\u00a2\u00a3\7g\2\2\u00a3\u00a4\7n\2\2\u00a4\u00a5")
        buf.write("\7u\2\2\u00a5\u00a6\7g\2\2\u00a6\64\3\2\2\2\u00a7\u00a8")
        buf.write("\7y\2\2\u00a8\u00a9\7j\2\2\u00a9\u00aa\7k\2\2\u00aa\u00ab")
        buf.write("\7n\2\2\u00ab\u00ac\7g\2\2\u00ac\66\3\2\2\2\u00ad\u00ae")
        buf.write("\7f\2\2\u00ae\u00af\7q\2\2\u00af8\3\2\2\2\u00b0\u00b1")
        buf.write("\7n\2\2\u00b1\u00b2\7g\2\2\u00b2\u00b3\7v\2\2\u00b3:\3")
        buf.write("\2\2\2\u00b4\u00b5\7k\2\2\u00b5\u00b6\7p\2\2\u00b6<\3")
        buf.write("\2\2\2\u00b7\u00b8\7d\2\2\u00b8\u00b9\7g\2\2\u00b9\u00ba")
        buf.write("\7i\2\2\u00ba\u00bb\7k\2\2\u00bb\u00bc\7p\2\2\u00bc>\3")
        buf.write("\2\2\2\u00bd\u00be\7g\2\2\u00be\u00bf\7p\2\2\u00bf\u00c0")
        buf.write("\7f\2\2\u00c0@\3\2\2\2\u00c1\u00c2\7e\2\2\u00c2\u00c3")
        buf.write("\7q\2\2\u00c3\u00c4\7p\2\2\u00c4\u00c5\7u\2\2\u00c5\u00c6")
        buf.write("\7v\2\2\u00c6B\3\2\2\2\u00c7\u00c8\7x\2\2\u00c8\u00c9")
        buf.write("\7c\2\2\u00c9\u00ca\7t\2\2\u00caD\3\2\2\2\u00cb\u00cc")
        buf.write("\7f\2\2\u00cc\u00cd\7g\2\2\u00cd\u00ce\7h\2\2\u00ceF\3")
        buf.write("\2\2\2\u00cf\u00d0\7n\2\2\u00d0\u00d1\7g\2\2\u00d1\u00d2")
        buf.write("\7p\2\2\u00d2H\3\2\2\2\u00d3\u00d4\7h\2\2\u00d4\u00d5")
        buf.write("\7q\2\2\u00d5\u00d6\7t\2\2\u00d6J\3\2\2\2\u00d7\u00d8")
        buf.write("\7t\2\2\u00d8\u00d9\7g\2\2\u00d9\u00da\7v\2\2\u00da\u00db")
        buf.write("\7w\2\2\u00db\u00dc\7t\2\2\u00dc\u00dd\7p\2\2\u00ddL\3")
        buf.write("\2\2\2\u00de\u00df\7r\2\2\u00df\u00e0\7t\2\2\u00e0\u00e1")
        buf.write("\7k\2\2\u00e1\u00e2\7p\2\2\u00e2\u00e3\7v\2\2\u00e3N\3")
        buf.write("\2\2\2\u00e4\u00e8\5c\62\2\u00e5\u00e7\5_\60\2\u00e6\u00e5")
        buf.write("\3\2\2\2\u00e7\u00ea\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e8")
        buf.write("\u00e9\3\2\2\2\u00e9\u00ed\3\2\2\2\u00ea\u00e8\3\2\2\2")
        buf.write("\u00eb\u00ed\7\62\2\2\u00ec\u00e4\3\2\2\2\u00ec\u00eb")
        buf.write("\3\2\2\2\u00edP\3\2\2\2\u00ee\u00f3\5a\61\2\u00ef\u00f2")
        buf.write("\5a\61\2\u00f0\u00f2\5_\60\2\u00f1\u00ef\3\2\2\2\u00f1")
        buf.write("\u00f0\3\2\2\2\u00f2\u00f5\3\2\2\2\u00f3\u00f1\3\2\2\2")
        buf.write("\u00f3\u00f4\3\2\2\2\u00f4R\3\2\2\2\u00f5\u00f3\3\2\2")
        buf.write("\2\u00f6\u00fc\7)\2\2\u00f7\u00fb\5a\61\2\u00f8\u00fb")
        buf.write("\5_\60\2\u00f9\u00fb\5Y-\2\u00fa\u00f7\3\2\2\2\u00fa\u00f8")
        buf.write("\3\2\2\2\u00fa\u00f9\3\2\2\2\u00fb\u00fe\3\2\2\2\u00fc")
        buf.write("\u00fa\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd\u00ff\3\2\2\2")
        buf.write("\u00fe\u00fc\3\2\2\2\u00ff\u010b\7)\2\2\u0100\u0106\7")
        buf.write("$\2\2\u0101\u0105\5a\61\2\u0102\u0105\5_\60\2\u0103\u0105")
        buf.write("\5Y-\2\u0104\u0101\3\2\2\2\u0104\u0102\3\2\2\2\u0104\u0103")
        buf.write("\3\2\2\2\u0105\u0108\3\2\2\2\u0106\u0104\3\2\2\2\u0106")
        buf.write("\u0107\3\2\2\2\u0107\u0109\3\2\2\2\u0108\u0106\3\2\2\2")
        buf.write("\u0109\u010b\7$\2\2\u010a\u00f6\3\2\2\2\u010a\u0100\3")
        buf.write("\2\2\2\u010bT\3\2\2\2\u010c\u010f\5c\62\2\u010d\u010f")
        buf.write("\7\62\2\2\u010e\u010c\3\2\2\2\u010e\u010d\3\2\2\2\u010f")
        buf.write("\u0110\3\2\2\2\u0110\u0112\5-\27\2\u0111\u0113\5_\60\2")
        buf.write("\u0112\u0111\3\2\2\2\u0113\u0114\3\2\2\2\u0114\u0112\3")
        buf.write("\2\2\2\u0114\u0115\3\2\2\2\u0115\u0123\3\2\2\2\u0116\u0118")
        buf.write("\5c\62\2\u0117\u0119\5_\60\2\u0118\u0117\3\2\2\2\u0119")
        buf.write("\u011a\3\2\2\2\u011a\u0118\3\2\2\2\u011a\u011b\3\2\2\2")
        buf.write("\u011b\u011c\3\2\2\2\u011c\u011e\5-\27\2\u011d\u011f\5")
        buf.write("_\60\2\u011e\u011d\3\2\2\2\u011f\u0120\3\2\2\2\u0120\u011e")
        buf.write("\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u0123\3\2\2\2\u0122")
        buf.write("\u010e\3\2\2\2\u0122\u0116\3\2\2\2\u0123V\3\2\2\2\u0124")
        buf.write("\u012a\7)\2\2\u0125\u0129\5a\61\2\u0126\u0129\5_\60\2")
        buf.write("\u0127\u0129\5Y-\2\u0128\u0125\3\2\2\2\u0128\u0126\3\2")
        buf.write("\2\2\u0128\u0127\3\2\2\2\u0129\u012c\3\2\2\2\u012a\u0128")
        buf.write("\3\2\2\2\u012a\u012b\3\2\2\2\u012b\u012d\3\2\2\2\u012c")
        buf.write("\u012a\3\2\2\2\u012d\u012e\7)\2\2\u012eX\3\2\2\2\u012f")
        buf.write("\u0146\5\3\2\2\u0130\u0146\5\5\3\2\u0131\u0146\5\7\4\2")
        buf.write("\u0132\u0146\5\t\5\2\u0133\u0146\5\13\6\2\u0134\u0146")
        buf.write("\5\r\7\2\u0135\u0146\5\17\b\2\u0136\u0146\5\21\t\2\u0137")
        buf.write("\u0146\5\23\n\2\u0138\u0146\5\25\13\2\u0139\u0146\5\27")
        buf.write("\f\2\u013a\u0146\5\31\r\2\u013b\u0146\5\33\16\2\u013c")
        buf.write("\u0146\5\35\17\2\u013d\u0146\5\37\20\2\u013e\u0146\5!")
        buf.write("\21\2\u013f\u0146\5#\22\2\u0140\u0146\5%\23\2\u0141\u0146")
        buf.write("\5\'\24\2\u0142\u0146\5)\25\2\u0143\u0146\5+\26\2\u0144")
        buf.write("\u0146\5-\27\2\u0145\u012f\3\2\2\2\u0145\u0130\3\2\2\2")
        buf.write("\u0145\u0131\3\2\2\2\u0145\u0132\3\2\2\2\u0145\u0133\3")
        buf.write("\2\2\2\u0145\u0134\3\2\2\2\u0145\u0135\3\2\2\2\u0145\u0136")
        buf.write("\3\2\2\2\u0145\u0137\3\2\2\2\u0145\u0138\3\2\2\2\u0145")
        buf.write("\u0139\3\2\2\2\u0145\u013a\3\2\2\2\u0145\u013b\3\2\2\2")
        buf.write("\u0145\u013c\3\2\2\2\u0145\u013d\3\2\2\2\u0145\u013e\3")
        buf.write("\2\2\2\u0145\u013f\3\2\2\2\u0145\u0140\3\2\2\2\u0145\u0141")
        buf.write("\3\2\2\2\u0145\u0142\3\2\2\2\u0145\u0143\3\2\2\2\u0145")
        buf.write("\u0144\3\2\2\2\u0146Z\3\2\2\2\u0147\u014b\7%\2\2\u0148")
        buf.write("\u014a\n\2\2\2\u0149\u0148\3\2\2\2\u014a\u014d\3\2\2\2")
        buf.write("\u014b\u0149\3\2\2\2\u014b\u014c\3\2\2\2\u014c\u014e\3")
        buf.write("\2\2\2\u014d\u014b\3\2\2\2\u014e\u014f\5e\63\2\u014f\u0150")
        buf.write("\3\2\2\2\u0150\u0151\b.\2\2\u0151\\\3\2\2\2\u0152\u0153")
        buf.write("\7$\2\2\u0153\u0154\7$\2\2\u0154\u0155\7$\2\2\u0155\u0159")
        buf.write("\3\2\2\2\u0156\u0158\13\2\2\2\u0157\u0156\3\2\2\2\u0158")
        buf.write("\u015b\3\2\2\2\u0159\u015a\3\2\2\2\u0159\u0157\3\2\2\2")
        buf.write("\u015a\u015c\3\2\2\2\u015b\u0159\3\2\2\2\u015c\u015d\7")
        buf.write("$\2\2\u015d\u015e\7$\2\2\u015e\u015f\7$\2\2\u015f\u0160")
        buf.write("\3\2\2\2\u0160\u0161\5e\63\2\u0161\u0162\3\2\2\2\u0162")
        buf.write("\u0163\b/\2\2\u0163^\3\2\2\2\u0164\u0165\t\3\2\2\u0165")
        buf.write("`\3\2\2\2\u0166\u0167\t\4\2\2\u0167b\3\2\2\2\u0168\u0169")
        buf.write("\t\5\2\2\u0169d\3\2\2\2\u016a\u016c\7\17\2\2\u016b\u016a")
        buf.write("\3\2\2\2\u016b\u016c\3\2\2\2\u016c\u016d\3\2\2\2\u016d")
        buf.write("\u0171\7\f\2\2\u016e\u0170\t\6\2\2\u016f\u016e\3\2\2\2")
        buf.write("\u0170\u0173\3\2\2\2\u0171\u016f\3\2\2\2\u0171\u0172\3")
        buf.write("\2\2\2\u0172f\3\2\2\2\u0173\u0171\3\2\2\2\u0174\u0175")
        buf.write("\t\7\2\2\u0175\u0176\3\2\2\2\u0176\u0177\b\64\2\2\u0177")
        buf.write("h\3\2\2\2\30\2\u00e8\u00ec\u00f1\u00f3\u00fa\u00fc\u0104")
        buf.write("\u0106\u010a\u010e\u0114\u011a\u0120\u0122\u0128\u012a")
        buf.write("\u0145\u014b\u0159\u016b\u0171\3\b\2\2")
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
    POINT = 22
    IF = 23
    THEN = 24
    ELSE = 25
    WHILE = 26
    DO = 27
    LET = 28
    IN = 29
    BEGIN = 30
    END = 31
    CONST = 32
    VAR = 33
    DEF = 34
    LEN = 35
    FOR = 36
    RETURN = 37
    PRINT = 38
    NUM = 39
    ID = 40
    STRING = 41
    FLOAT = 42
    CHARCONTS = 43
    SIMBOLS = 44
    COMENTLINEA = 45
    COMENTMULTILINEA = 46
    NEWLINE = 47
    WS = 48

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "';'", "':='", "'('", "')'", "'['", "']'", "'~'", "':'", 
            "'+'", "'*'", "'-'", "'/'", "'**'", "'%'", "'<'", "'>'", "'<='", 
            "'>='", "'=='", "'='", "'.'", "'if'", "'then'", "'else'", "'while'", 
            "'do'", "'let'", "'in'", "'begin'", "'end'", "'const'", "'var'", 
            "'def'", "'len'", "'for'", "'return'", "'print'" ]

    symbolicNames = [ "<INVALID>",
            "COMA", "PyCOMA", "ASIGN", "PIZQ", "PDER", "CIZQ", "CDER", "VIR", 
            "DOSPUNT", "MAS", "MULT", "MEN", "DIV", "POT", "MOD", "MENQUE", 
            "MAYQUE", "MENQUEEQUAL", "MAYQUEEQUAL", "EQUALEQUAL", "EQUAL", 
            "POINT", "IF", "THEN", "ELSE", "WHILE", "DO", "LET", "IN", "BEGIN", 
            "END", "CONST", "VAR", "DEF", "LEN", "FOR", "RETURN", "PRINT", 
            "NUM", "ID", "STRING", "FLOAT", "CHARCONTS", "SIMBOLS", "COMENTLINEA", 
            "COMENTMULTILINEA", "NEWLINE", "WS" ]

    ruleNames = [ "COMA", "PyCOMA", "ASIGN", "PIZQ", "PDER", "CIZQ", "CDER", 
                  "VIR", "DOSPUNT", "MAS", "MULT", "MEN", "DIV", "POT", 
                  "MOD", "MENQUE", "MAYQUE", "MENQUEEQUAL", "MAYQUEEQUAL", 
                  "EQUALEQUAL", "EQUAL", "POINT", "IF", "THEN", "ELSE", 
                  "WHILE", "DO", "LET", "IN", "BEGIN", "END", "CONST", "VAR", 
                  "DEF", "LEN", "FOR", "RETURN", "PRINT", "NUM", "ID", "STRING", 
                  "FLOAT", "CHARCONTS", "SIMBOLS", "COMENTLINEA", "COMENTMULTILINEA", 
                  "DIGIT", "LETTER", "DIGITNOTZERO", "NEWLINE", "WS" ]

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


