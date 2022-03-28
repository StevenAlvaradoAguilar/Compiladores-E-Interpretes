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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\63")
        buf.write("\u0187\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3")
        buf.write("\f\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\21\3\21")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3!\3!\3!\3")
        buf.write("!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3$\3$\3$\3$\3%\3%")
        buf.write("\3%\3%\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("(\3(\7(\u00e9\n(\f(\16(\u00ec\13(\3)\3)\3)\7)\u00f1\n")
        buf.write(")\f)\16)\u00f4\13)\3*\3*\3*\3*\7*\u00fa\n*\f*\16*\u00fd")
        buf.write("\13*\3*\3*\3*\3*\3*\7*\u0104\n*\f*\16*\u0107\13*\3*\5")
        buf.write("*\u010a\n*\3+\3+\5+\u010e\n+\3+\3+\6+\u0112\n+\r+\16+")
        buf.write("\u0113\3+\3+\6+\u0118\n+\r+\16+\u0119\3+\3+\6+\u011e\n")
        buf.write("+\r+\16+\u011f\5+\u0122\n+\3,\3,\3,\3,\7,\u0128\n,\f,")
        buf.write("\16,\u012b\13,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-")
        buf.write("\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u0145\n-\3.\3.\7")
        buf.write(".\u0149\n.\f.\16.\u014c\13.\3.\3.\3.\3.\3/\3/\3/\3/\3")
        buf.write("/\7/\u0157\n/\f/\16/\u015a\13/\3/\3/\3/\3/\3\60\3\60\3")
        buf.write("\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\7\60\u016b")
        buf.write("\n\60\f\60\16\60\u016e\13\60\3\60\3\60\3\60\3\60\3\61")
        buf.write("\3\61\3\62\3\62\3\63\3\63\3\64\5\64\u017b\n\64\3\64\3")
        buf.write("\64\7\64\u017f\n\64\f\64\16\64\u0182\13\64\3\65\3\65\3")
        buf.write("\65\3\65\2\2\66\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A")
        buf.write("\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\2c\2e\2g\62i\63")
        buf.write("\3\2\b\4\2\f\f\17\17\3\2\62;\6\2\"\"C\\aac|\3\2\63;\4")
        buf.write("\2\13\13\"\"\7\2\13\f\17\17\"\"%%--\2\u01af\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2g\3\2\2\2\2i\3\2\2\2\3k\3\2\2\2\5m\3\2\2\2\7o")
        buf.write("\3\2\2\2\tr\3\2\2\2\13t\3\2\2\2\rv\3\2\2\2\17x\3\2\2\2")
        buf.write("\21z\3\2\2\2\23|\3\2\2\2\25~\3\2\2\2\27\u0080\3\2\2\2")
        buf.write("\31\u0082\3\2\2\2\33\u0084\3\2\2\2\35\u0086\3\2\2\2\37")
        buf.write("\u0089\3\2\2\2!\u008b\3\2\2\2#\u008d\3\2\2\2%\u008f\3")
        buf.write("\2\2\2\'\u0092\3\2\2\2)\u0095\3\2\2\2+\u0098\3\2\2\2-")
        buf.write("\u009a\3\2\2\2/\u009c\3\2\2\2\61\u009f\3\2\2\2\63\u00a4")
        buf.write("\3\2\2\2\65\u00a9\3\2\2\2\67\u00af\3\2\2\29\u00b2\3\2")
        buf.write("\2\2;\u00b6\3\2\2\2=\u00b9\3\2\2\2?\u00bf\3\2\2\2A\u00c3")
        buf.write("\3\2\2\2C\u00c9\3\2\2\2E\u00cd\3\2\2\2G\u00d1\3\2\2\2")
        buf.write("I\u00d5\3\2\2\2K\u00d9\3\2\2\2M\u00e0\3\2\2\2O\u00e6\3")
        buf.write("\2\2\2Q\u00ed\3\2\2\2S\u0109\3\2\2\2U\u0121\3\2\2\2W\u0123")
        buf.write("\3\2\2\2Y\u0144\3\2\2\2[\u0146\3\2\2\2]\u0151\3\2\2\2")
        buf.write("_\u015f\3\2\2\2a\u0173\3\2\2\2c\u0175\3\2\2\2e\u0177\3")
        buf.write("\2\2\2g\u017a\3\2\2\2i\u0183\3\2\2\2kl\7.\2\2l\4\3\2\2")
        buf.write("\2mn\7=\2\2n\6\3\2\2\2op\7<\2\2pq\7?\2\2q\b\3\2\2\2rs")
        buf.write("\7*\2\2s\n\3\2\2\2tu\7+\2\2u\f\3\2\2\2vw\7]\2\2w\16\3")
        buf.write("\2\2\2xy\7_\2\2y\20\3\2\2\2z{\7\u0080\2\2{\22\3\2\2\2")
        buf.write("|}\7<\2\2}\24\3\2\2\2~\177\7-\2\2\177\26\3\2\2\2\u0080")
        buf.write("\u0081\7,\2\2\u0081\30\3\2\2\2\u0082\u0083\7/\2\2\u0083")
        buf.write("\32\3\2\2\2\u0084\u0085\7\61\2\2\u0085\34\3\2\2\2\u0086")
        buf.write("\u0087\7,\2\2\u0087\u0088\7,\2\2\u0088\36\3\2\2\2\u0089")
        buf.write("\u008a\7\'\2\2\u008a \3\2\2\2\u008b\u008c\7>\2\2\u008c")
        buf.write("\"\3\2\2\2\u008d\u008e\7@\2\2\u008e$\3\2\2\2\u008f\u0090")
        buf.write("\7>\2\2\u0090\u0091\7?\2\2\u0091&\3\2\2\2\u0092\u0093")
        buf.write("\7@\2\2\u0093\u0094\7?\2\2\u0094(\3\2\2\2\u0095\u0096")
        buf.write("\7?\2\2\u0096\u0097\7?\2\2\u0097*\3\2\2\2\u0098\u0099")
        buf.write("\7?\2\2\u0099,\3\2\2\2\u009a\u009b\7\60\2\2\u009b.\3\2")
        buf.write("\2\2\u009c\u009d\7k\2\2\u009d\u009e\7h\2\2\u009e\60\3")
        buf.write("\2\2\2\u009f\u00a0\7v\2\2\u00a0\u00a1\7j\2\2\u00a1\u00a2")
        buf.write("\7g\2\2\u00a2\u00a3\7p\2\2\u00a3\62\3\2\2\2\u00a4\u00a5")
        buf.write("\7g\2\2\u00a5\u00a6\7n\2\2\u00a6\u00a7\7u\2\2\u00a7\u00a8")
        buf.write("\7g\2\2\u00a8\64\3\2\2\2\u00a9\u00aa\7y\2\2\u00aa\u00ab")
        buf.write("\7j\2\2\u00ab\u00ac\7k\2\2\u00ac\u00ad\7n\2\2\u00ad\u00ae")
        buf.write("\7g\2\2\u00ae\66\3\2\2\2\u00af\u00b0\7f\2\2\u00b0\u00b1")
        buf.write("\7q\2\2\u00b18\3\2\2\2\u00b2\u00b3\7n\2\2\u00b3\u00b4")
        buf.write("\7g\2\2\u00b4\u00b5\7v\2\2\u00b5:\3\2\2\2\u00b6\u00b7")
        buf.write("\7k\2\2\u00b7\u00b8\7p\2\2\u00b8<\3\2\2\2\u00b9\u00ba")
        buf.write("\7d\2\2\u00ba\u00bb\7g\2\2\u00bb\u00bc\7i\2\2\u00bc\u00bd")
        buf.write("\7k\2\2\u00bd\u00be\7p\2\2\u00be>\3\2\2\2\u00bf\u00c0")
        buf.write("\7g\2\2\u00c0\u00c1\7p\2\2\u00c1\u00c2\7f\2\2\u00c2@\3")
        buf.write("\2\2\2\u00c3\u00c4\7e\2\2\u00c4\u00c5\7q\2\2\u00c5\u00c6")
        buf.write("\7p\2\2\u00c6\u00c7\7u\2\2\u00c7\u00c8\7v\2\2\u00c8B\3")
        buf.write("\2\2\2\u00c9\u00ca\7x\2\2\u00ca\u00cb\7c\2\2\u00cb\u00cc")
        buf.write("\7t\2\2\u00ccD\3\2\2\2\u00cd\u00ce\7f\2\2\u00ce\u00cf")
        buf.write("\7g\2\2\u00cf\u00d0\7h\2\2\u00d0F\3\2\2\2\u00d1\u00d2")
        buf.write("\7n\2\2\u00d2\u00d3\7g\2\2\u00d3\u00d4\7p\2\2\u00d4H\3")
        buf.write("\2\2\2\u00d5\u00d6\7h\2\2\u00d6\u00d7\7q\2\2\u00d7\u00d8")
        buf.write("\7t\2\2\u00d8J\3\2\2\2\u00d9\u00da\7t\2\2\u00da\u00db")
        buf.write("\7g\2\2\u00db\u00dc\7v\2\2\u00dc\u00dd\7w\2\2\u00dd\u00de")
        buf.write("\7t\2\2\u00de\u00df\7p\2\2\u00dfL\3\2\2\2\u00e0\u00e1")
        buf.write("\7r\2\2\u00e1\u00e2\7t\2\2\u00e2\u00e3\7k\2\2\u00e3\u00e4")
        buf.write("\7p\2\2\u00e4\u00e5\7v\2\2\u00e5N\3\2\2\2\u00e6\u00ea")
        buf.write("\5e\63\2\u00e7\u00e9\5a\61\2\u00e8\u00e7\3\2\2\2\u00e9")
        buf.write("\u00ec\3\2\2\2\u00ea\u00e8\3\2\2\2\u00ea\u00eb\3\2\2\2")
        buf.write("\u00ebP\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ed\u00f2\5c\62")
        buf.write("\2\u00ee\u00f1\5c\62\2\u00ef\u00f1\5a\61\2\u00f0\u00ee")
        buf.write("\3\2\2\2\u00f0\u00ef\3\2\2\2\u00f1\u00f4\3\2\2\2\u00f2")
        buf.write("\u00f0\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3R\3\2\2\2\u00f4")
        buf.write("\u00f2\3\2\2\2\u00f5\u00fb\7)\2\2\u00f6\u00fa\5c\62\2")
        buf.write("\u00f7\u00fa\5a\61\2\u00f8\u00fa\5Y-\2\u00f9\u00f6\3\2")
        buf.write("\2\2\u00f9\u00f7\3\2\2\2\u00f9\u00f8\3\2\2\2\u00fa\u00fd")
        buf.write("\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc")
        buf.write("\u00fe\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fe\u010a\7)\2\2")
        buf.write("\u00ff\u0105\7$\2\2\u0100\u0104\5c\62\2\u0101\u0104\5")
        buf.write("a\61\2\u0102\u0104\5Y-\2\u0103\u0100\3\2\2\2\u0103\u0101")
        buf.write("\3\2\2\2\u0103\u0102\3\2\2\2\u0104\u0107\3\2\2\2\u0105")
        buf.write("\u0103\3\2\2\2\u0105\u0106\3\2\2\2\u0106\u0108\3\2\2\2")
        buf.write("\u0107\u0105\3\2\2\2\u0108\u010a\7$\2\2\u0109\u00f5\3")
        buf.write("\2\2\2\u0109\u00ff\3\2\2\2\u010aT\3\2\2\2\u010b\u010e")
        buf.write("\5e\63\2\u010c\u010e\7\62\2\2\u010d\u010b\3\2\2\2\u010d")
        buf.write("\u010c\3\2\2\2\u010e\u010f\3\2\2\2\u010f\u0111\7\60\2")
        buf.write("\2\u0110\u0112\5a\61\2\u0111\u0110\3\2\2\2\u0112\u0113")
        buf.write("\3\2\2\2\u0113\u0111\3\2\2\2\u0113\u0114\3\2\2\2\u0114")
        buf.write("\u0122\3\2\2\2\u0115\u0117\5e\63\2\u0116\u0118\5a\61\2")
        buf.write("\u0117\u0116\3\2\2\2\u0118\u0119\3\2\2\2\u0119\u0117\3")
        buf.write("\2\2\2\u0119\u011a\3\2\2\2\u011a\u011b\3\2\2\2\u011b\u011d")
        buf.write("\7\60\2\2\u011c\u011e\5a\61\2\u011d\u011c\3\2\2\2\u011e")
        buf.write("\u011f\3\2\2\2\u011f\u011d\3\2\2\2\u011f\u0120\3\2\2\2")
        buf.write("\u0120\u0122\3\2\2\2\u0121\u010d\3\2\2\2\u0121\u0115\3")
        buf.write("\2\2\2\u0122V\3\2\2\2\u0123\u0129\7)\2\2\u0124\u0128\5")
        buf.write("c\62\2\u0125\u0128\5a\61\2\u0126\u0128\5Y-\2\u0127\u0124")
        buf.write("\3\2\2\2\u0127\u0125\3\2\2\2\u0127\u0126\3\2\2\2\u0128")
        buf.write("\u012b\3\2\2\2\u0129\u0127\3\2\2\2\u0129\u012a\3\2\2\2")
        buf.write("\u012a\u012c\3\2\2\2\u012b\u0129\3\2\2\2\u012c\u012d\7")
        buf.write(")\2\2\u012dX\3\2\2\2\u012e\u0145\5\3\2\2\u012f\u0145\5")
        buf.write("\5\3\2\u0130\u0145\5\7\4\2\u0131\u0145\5\t\5\2\u0132\u0145")
        buf.write("\5\13\6\2\u0133\u0145\5\r\7\2\u0134\u0145\5\17\b\2\u0135")
        buf.write("\u0145\5\21\t\2\u0136\u0145\5\23\n\2\u0137\u0145\5\25")
        buf.write("\13\2\u0138\u0145\5\27\f\2\u0139\u0145\5\31\r\2\u013a")
        buf.write("\u0145\5\33\16\2\u013b\u0145\5\35\17\2\u013c\u0145\5\37")
        buf.write("\20\2\u013d\u0145\5!\21\2\u013e\u0145\5#\22\2\u013f\u0145")
        buf.write("\5%\23\2\u0140\u0145\5\'\24\2\u0141\u0145\5)\25\2\u0142")
        buf.write("\u0145\5+\26\2\u0143\u0145\5-\27\2\u0144\u012e\3\2\2\2")
        buf.write("\u0144\u012f\3\2\2\2\u0144\u0130\3\2\2\2\u0144\u0131\3")
        buf.write("\2\2\2\u0144\u0132\3\2\2\2\u0144\u0133\3\2\2\2\u0144\u0134")
        buf.write("\3\2\2\2\u0144\u0135\3\2\2\2\u0144\u0136\3\2\2\2\u0144")
        buf.write("\u0137\3\2\2\2\u0144\u0138\3\2\2\2\u0144\u0139\3\2\2\2")
        buf.write("\u0144\u013a\3\2\2\2\u0144\u013b\3\2\2\2\u0144\u013c\3")
        buf.write("\2\2\2\u0144\u013d\3\2\2\2\u0144\u013e\3\2\2\2\u0144\u013f")
        buf.write("\3\2\2\2\u0144\u0140\3\2\2\2\u0144\u0141\3\2\2\2\u0144")
        buf.write("\u0142\3\2\2\2\u0144\u0143\3\2\2\2\u0145Z\3\2\2\2\u0146")
        buf.write("\u014a\7%\2\2\u0147\u0149\n\2\2\2\u0148\u0147\3\2\2\2")
        buf.write("\u0149\u014c\3\2\2\2\u014a\u0148\3\2\2\2\u014a\u014b\3")
        buf.write("\2\2\2\u014b\u014d\3\2\2\2\u014c\u014a\3\2\2\2\u014d\u014e")
        buf.write("\5g\64\2\u014e\u014f\3\2\2\2\u014f\u0150\b.\2\2\u0150")
        buf.write("\\\3\2\2\2\u0151\u0152\7$\2\2\u0152\u0153\7$\2\2\u0153")
        buf.write("\u0154\7$\2\2\u0154\u0158\3\2\2\2\u0155\u0157\n\2\2\2")
        buf.write("\u0156\u0155\3\2\2\2\u0157\u015a\3\2\2\2\u0158\u0156\3")
        buf.write("\2\2\2\u0158\u0159\3\2\2\2\u0159\u015b\3\2\2\2\u015a\u0158")
        buf.write("\3\2\2\2\u015b\u015c\5g\64\2\u015c\u015d\3\2\2\2\u015d")
        buf.write("\u015e\b/\2\2\u015e^\3\2\2\2\u015f\u0160\7\u00e4\2\2\u0160")
        buf.write("\u0161\7\u20ae\2\2\u0161\u0162\7\u0155\2\2\u0162\u0163")
        buf.write("\7\u00e4\2\2\u0163\u0164\7\u20ae\2\2\u0164\u0165\7\uffff")
        buf.write("\2\2\u0165\u0166\7\u00e4\2\2\u0166\u0167\7\u20ae\2\2\u0167")
        buf.write("\u0168\7\uffff\2\2\u0168\u016c\3\2\2\2\u0169\u016b\n\2")
        buf.write("\2\2\u016a\u0169\3\2\2\2\u016b\u016e\3\2\2\2\u016c\u016a")
        buf.write("\3\2\2\2\u016c\u016d\3\2\2\2\u016d\u016f\3\2\2\2\u016e")
        buf.write("\u016c\3\2\2\2\u016f\u0170\5g\64\2\u0170\u0171\3\2\2\2")
        buf.write("\u0171\u0172\b\60\2\2\u0172`\3\2\2\2\u0173\u0174\t\3\2")
        buf.write("\2\u0174b\3\2\2\2\u0175\u0176\t\4\2\2\u0176d\3\2\2\2\u0177")
        buf.write("\u0178\t\5\2\2\u0178f\3\2\2\2\u0179\u017b\7\17\2\2\u017a")
        buf.write("\u0179\3\2\2\2\u017a\u017b\3\2\2\2\u017b\u017c\3\2\2\2")
        buf.write("\u017c\u0180\7\f\2\2\u017d\u017f\t\6\2\2\u017e\u017d\3")
        buf.write("\2\2\2\u017f\u0182\3\2\2\2\u0180\u017e\3\2\2\2\u0180\u0181")
        buf.write("\3\2\2\2\u0181h\3\2\2\2\u0182\u0180\3\2\2\2\u0183\u0184")
        buf.write("\t\7\2\2\u0184\u0185\3\2\2\2\u0185\u0186\b\65\2\2\u0186")
        buf.write("j\3\2\2\2\30\2\u00ea\u00f0\u00f2\u00f9\u00fb\u0103\u0105")
        buf.write("\u0109\u010d\u0113\u0119\u011f\u0121\u0127\u0129\u0144")
        buf.write("\u014a\u0158\u016c\u017a\u0180\3\b\2\2")
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
    COMENTMULTILINEA1 = 47
    NEWLINE = 48
    WS = 49

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
            "COMENTMULTILINEA", "COMENTMULTILINEA1", "NEWLINE", "WS" ]

    ruleNames = [ "COMA", "PyCOMA", "ASIGN", "PIZQ", "PDER", "CIZQ", "CDER", 
                  "VIR", "DOSPUNT", "MAS", "MULT", "MEN", "DIV", "POT", 
                  "MOD", "MENQUE", "MAYQUE", "MENQUEEQUAL", "MAYQUEEQUAL", 
                  "EQUALEQUAL", "EQUAL", "POINT", "IF", "THEN", "ELSE", 
                  "WHILE", "DO", "LET", "IN", "BEGIN", "END", "CONST", "VAR", 
                  "DEF", "LEN", "FOR", "RETURN", "PRINT", "NUM", "ID", "STRING", 
                  "FLOAT", "CHARCONTS", "SIMBOLS", "COMENTLINEA", "COMENTMULTILINEA", 
                  "COMENTMULTILINEA1", "DIGIT", "LETTER", "DIGITNOTZERO", 
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


