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
        buf.write("\u016e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\3\2\3\2\3\3\3")
        buf.write("\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n")
        buf.write("\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3 \3!\3!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3")
        buf.write("#\3#\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3&\3&\7&\u00da")
        buf.write("\n&\f&\16&\u00dd\13&\3&\5&\u00e0\n&\3\'\3\'\3\'\7\'\u00e5")
        buf.write("\n\'\f\'\16\'\u00e8\13\'\3(\3(\3(\3(\7(\u00ee\n(\f(\16")
        buf.write("(\u00f1\13(\3(\3(\3(\3(\3(\7(\u00f8\n(\f(\16(\u00fb\13")
        buf.write("(\3(\5(\u00fe\n(\3)\3)\5)\u0102\n)\3)\3)\6)\u0106\n)\r")
        buf.write(")\16)\u0107\3)\3)\6)\u010c\n)\r)\16)\u010d\3)\3)\6)\u0112")
        buf.write("\n)\r)\16)\u0113\5)\u0116\n)\3*\3*\3*\3*\5*\u011c\n*\3")
        buf.write("*\5*\u011f\n*\3*\3*\3+\3+\7+\u0125\n+\f+\16+\u0128\13")
        buf.write("+\3+\3+\3+\3+\3,\3,\3,\3,\3,\7,\u0133\n,\f,\16,\u0136")
        buf.write("\13,\3,\3,\3,\3,\3,\3,\3,\3,\3-\3-\3.\5.\u0143\n.\3/\3")
        buf.write("/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3")
        buf.write("\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\60\5\60\u015f\n\60\3\61\5\61\u0162\n\61\3")
        buf.write("\61\3\61\7\61\u0166\n\61\f\61\16\61\u0169\13\61\3\62\3")
        buf.write("\62\3\62\3\62\3\u0134\2\63\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y\2[\2]\2_\2a.c/\3\2")
        buf.write("\b\4\2\f\f\17\17\3\2\62;\5\2C\\aac|\3\2\63;\4\2\13\13")
        buf.write("\"\"\6\2\13\f\17\17\"\"--\2\u0197\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37")
        buf.write("\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2")
        buf.write("\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2")
        buf.write("\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2")
        buf.write("\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2")
        buf.write("\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2")
        buf.write("\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\3e\3\2\2\2\5g\3\2\2\2\7i")
        buf.write("\3\2\2\2\tk\3\2\2\2\13m\3\2\2\2\ro\3\2\2\2\17q\3\2\2\2")
        buf.write("\21s\3\2\2\2\23u\3\2\2\2\25w\3\2\2\2\27y\3\2\2\2\31{\3")
        buf.write("\2\2\2\33}\3\2\2\2\35\177\3\2\2\2\37\u0082\3\2\2\2!\u0084")
        buf.write("\3\2\2\2#\u0086\3\2\2\2%\u0088\3\2\2\2\'\u008b\3\2\2\2")
        buf.write(")\u008e\3\2\2\2+\u0091\3\2\2\2-\u0094\3\2\2\2/\u0097\3")
        buf.write("\2\2\2\61\u009a\3\2\2\2\63\u009f\3\2\2\2\65\u00a4\3\2")
        buf.write("\2\2\67\u00aa\3\2\2\29\u00ad\3\2\2\2;\u00b1\3\2\2\2=\u00b4")
        buf.write("\3\2\2\2?\u00ba\3\2\2\2A\u00be\3\2\2\2C\u00c2\3\2\2\2")
        buf.write("E\u00c6\3\2\2\2G\u00ca\3\2\2\2I\u00d1\3\2\2\2K\u00df\3")
        buf.write("\2\2\2M\u00e1\3\2\2\2O\u00fd\3\2\2\2Q\u0115\3\2\2\2S\u0117")
        buf.write("\3\2\2\2U\u0122\3\2\2\2W\u012d\3\2\2\2Y\u013f\3\2\2\2")
        buf.write("[\u0142\3\2\2\2]\u0144\3\2\2\2_\u015e\3\2\2\2a\u0161\3")
        buf.write("\2\2\2c\u016a\3\2\2\2ef\7.\2\2f\4\3\2\2\2gh\7=\2\2h\6")
        buf.write("\3\2\2\2ij\7?\2\2j\b\3\2\2\2kl\7*\2\2l\n\3\2\2\2mn\7+")
        buf.write("\2\2n\f\3\2\2\2op\7]\2\2p\16\3\2\2\2qr\7_\2\2r\20\3\2")
        buf.write("\2\2st\7\u0080\2\2t\22\3\2\2\2uv\7<\2\2v\24\3\2\2\2wx")
        buf.write("\7-\2\2x\26\3\2\2\2yz\7,\2\2z\30\3\2\2\2{|\7/\2\2|\32")
        buf.write("\3\2\2\2}~\7\61\2\2~\34\3\2\2\2\177\u0080\7,\2\2\u0080")
        buf.write("\u0081\7,\2\2\u0081\36\3\2\2\2\u0082\u0083\7\'\2\2\u0083")
        buf.write(" \3\2\2\2\u0084\u0085\7>\2\2\u0085\"\3\2\2\2\u0086\u0087")
        buf.write("\7@\2\2\u0087$\3\2\2\2\u0088\u0089\7>\2\2\u0089\u008a")
        buf.write("\7?\2\2\u008a&\3\2\2\2\u008b\u008c\7@\2\2\u008c\u008d")
        buf.write("\7?\2\2\u008d(\3\2\2\2\u008e\u008f\7?\2\2\u008f\u0090")
        buf.write("\7?\2\2\u0090*\3\2\2\2\u0091\u0092\7-\2\2\u0092\u0093")
        buf.write("\7?\2\2\u0093,\3\2\2\2\u0094\u0095\7/\2\2\u0095\u0096")
        buf.write("\7?\2\2\u0096.\3\2\2\2\u0097\u0098\7k\2\2\u0098\u0099")
        buf.write("\7h\2\2\u0099\60\3\2\2\2\u009a\u009b\7v\2\2\u009b\u009c")
        buf.write("\7j\2\2\u009c\u009d\7g\2\2\u009d\u009e\7p\2\2\u009e\62")
        buf.write("\3\2\2\2\u009f\u00a0\7g\2\2\u00a0\u00a1\7n\2\2\u00a1\u00a2")
        buf.write("\7u\2\2\u00a2\u00a3\7g\2\2\u00a3\64\3\2\2\2\u00a4\u00a5")
        buf.write("\7y\2\2\u00a5\u00a6\7j\2\2\u00a6\u00a7\7k\2\2\u00a7\u00a8")
        buf.write("\7n\2\2\u00a8\u00a9\7g\2\2\u00a9\66\3\2\2\2\u00aa\u00ab")
        buf.write("\7f\2\2\u00ab\u00ac\7q\2\2\u00ac8\3\2\2\2\u00ad\u00ae")
        buf.write("\7n\2\2\u00ae\u00af\7g\2\2\u00af\u00b0\7v\2\2\u00b0:\3")
        buf.write("\2\2\2\u00b1\u00b2\7k\2\2\u00b2\u00b3\7p\2\2\u00b3<\3")
        buf.write("\2\2\2\u00b4\u00b5\7d\2\2\u00b5\u00b6\7g\2\2\u00b6\u00b7")
        buf.write("\7i\2\2\u00b7\u00b8\7k\2\2\u00b8\u00b9\7p\2\2\u00b9>\3")
        buf.write("\2\2\2\u00ba\u00bb\7g\2\2\u00bb\u00bc\7p\2\2\u00bc\u00bd")
        buf.write("\7f\2\2\u00bd@\3\2\2\2\u00be\u00bf\7f\2\2\u00bf\u00c0")
        buf.write("\7g\2\2\u00c0\u00c1\7h\2\2\u00c1B\3\2\2\2\u00c2\u00c3")
        buf.write("\7n\2\2\u00c3\u00c4\7g\2\2\u00c4\u00c5\7p\2\2\u00c5D\3")
        buf.write("\2\2\2\u00c6\u00c7\7h\2\2\u00c7\u00c8\7q\2\2\u00c8\u00c9")
        buf.write("\7t\2\2\u00c9F\3\2\2\2\u00ca\u00cb\7t\2\2\u00cb\u00cc")
        buf.write("\7g\2\2\u00cc\u00cd\7v\2\2\u00cd\u00ce\7w\2\2\u00ce\u00cf")
        buf.write("\7t\2\2\u00cf\u00d0\7p\2\2\u00d0H\3\2\2\2\u00d1\u00d2")
        buf.write("\7r\2\2\u00d2\u00d3\7t\2\2\u00d3\u00d4\7k\2\2\u00d4\u00d5")
        buf.write("\7p\2\2\u00d5\u00d6\7v\2\2\u00d6J\3\2\2\2\u00d7\u00db")
        buf.write("\5]/\2\u00d8\u00da\5Y-\2\u00d9\u00d8\3\2\2\2\u00da\u00dd")
        buf.write("\3\2\2\2\u00db\u00d9\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc")
        buf.write("\u00e0\3\2\2\2\u00dd\u00db\3\2\2\2\u00de\u00e0\7\62\2")
        buf.write("\2\u00df\u00d7\3\2\2\2\u00df\u00de\3\2\2\2\u00e0L\3\2")
        buf.write("\2\2\u00e1\u00e6\5[.\2\u00e2\u00e5\5[.\2\u00e3\u00e5\5")
        buf.write("Y-\2\u00e4\u00e2\3\2\2\2\u00e4\u00e3\3\2\2\2\u00e5\u00e8")
        buf.write("\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7")
        buf.write("N\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e9\u00ef\7)\2\2\u00ea")
        buf.write("\u00ee\5[.\2\u00eb\u00ee\5Y-\2\u00ec\u00ee\5_\60\2\u00ed")
        buf.write("\u00ea\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ed\u00ec\3\2\2\2")
        buf.write("\u00ee\u00f1\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef\u00f0\3")
        buf.write("\2\2\2\u00f0\u00f2\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f2\u00fe")
        buf.write("\7)\2\2\u00f3\u00f9\7$\2\2\u00f4\u00f8\5[.\2\u00f5\u00f8")
        buf.write("\5Y-\2\u00f6\u00f8\5_\60\2\u00f7\u00f4\3\2\2\2\u00f7\u00f5")
        buf.write("\3\2\2\2\u00f7\u00f6\3\2\2\2\u00f8\u00fb\3\2\2\2\u00f9")
        buf.write("\u00f7\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00fc\3\2\2\2")
        buf.write("\u00fb\u00f9\3\2\2\2\u00fc\u00fe\7$\2\2\u00fd\u00e9\3")
        buf.write("\2\2\2\u00fd\u00f3\3\2\2\2\u00feP\3\2\2\2\u00ff\u0102")
        buf.write("\5]/\2\u0100\u0102\7\62\2\2\u0101\u00ff\3\2\2\2\u0101")
        buf.write("\u0100\3\2\2\2\u0102\u0103\3\2\2\2\u0103\u0105\7\60\2")
        buf.write("\2\u0104\u0106\5Y-\2\u0105\u0104\3\2\2\2\u0106\u0107\3")
        buf.write("\2\2\2\u0107\u0105\3\2\2\2\u0107\u0108\3\2\2\2\u0108\u0116")
        buf.write("\3\2\2\2\u0109\u010b\5]/\2\u010a\u010c\5Y-\2\u010b\u010a")
        buf.write("\3\2\2\2\u010c\u010d\3\2\2\2\u010d\u010b\3\2\2\2\u010d")
        buf.write("\u010e\3\2\2\2\u010e\u010f\3\2\2\2\u010f\u0111\7\60\2")
        buf.write("\2\u0110\u0112\5Y-\2\u0111\u0110\3\2\2\2\u0112\u0113\3")
        buf.write("\2\2\2\u0113\u0111\3\2\2\2\u0113\u0114\3\2\2\2\u0114\u0116")
        buf.write("\3\2\2\2\u0115\u0101\3\2\2\2\u0115\u0109\3\2\2\2\u0116")
        buf.write("R\3\2\2\2\u0117\u011e\7)\2\2\u0118\u011c\5[.\2\u0119\u011c")
        buf.write("\5Y-\2\u011a\u011c\5_\60\2\u011b\u0118\3\2\2\2\u011b\u0119")
        buf.write("\3\2\2\2\u011b\u011a\3\2\2\2\u011c\u011f\3\2\2\2\u011d")
        buf.write("\u011f\3\2\2\2\u011e\u011b\3\2\2\2\u011e\u011d\3\2\2\2")
        buf.write("\u011f\u0120\3\2\2\2\u0120\u0121\7)\2\2\u0121T\3\2\2\2")
        buf.write("\u0122\u0126\7%\2\2\u0123\u0125\n\2\2\2\u0124\u0123\3")
        buf.write("\2\2\2\u0125\u0128\3\2\2\2\u0126\u0124\3\2\2\2\u0126\u0127")
        buf.write("\3\2\2\2\u0127\u0129\3\2\2\2\u0128\u0126\3\2\2\2\u0129")
        buf.write("\u012a\5a\61\2\u012a\u012b\3\2\2\2\u012b\u012c\b+\2\2")
        buf.write("\u012cV\3\2\2\2\u012d\u012e\7$\2\2\u012e\u012f\7$\2\2")
        buf.write("\u012f\u0130\7$\2\2\u0130\u0134\3\2\2\2\u0131\u0133\13")
        buf.write("\2\2\2\u0132\u0131\3\2\2\2\u0133\u0136\3\2\2\2\u0134\u0135")
        buf.write("\3\2\2\2\u0134\u0132\3\2\2\2\u0135\u0137\3\2\2\2\u0136")
        buf.write("\u0134\3\2\2\2\u0137\u0138\7$\2\2\u0138\u0139\7$\2\2\u0139")
        buf.write("\u013a\7$\2\2\u013a\u013b\3\2\2\2\u013b\u013c\5a\61\2")
        buf.write("\u013c\u013d\3\2\2\2\u013d\u013e\b,\2\2\u013eX\3\2\2\2")
        buf.write("\u013f\u0140\t\3\2\2\u0140Z\3\2\2\2\u0141\u0143\t\4\2")
        buf.write("\2\u0142\u0141\3\2\2\2\u0143\\\3\2\2\2\u0144\u0145\t\5")
        buf.write("\2\2\u0145^\3\2\2\2\u0146\u015f\5\3\2\2\u0147\u015f\5")
        buf.write("\5\3\2\u0148\u015f\5\7\4\2\u0149\u015f\5\t\5\2\u014a\u015f")
        buf.write("\5\13\6\2\u014b\u015f\5\r\7\2\u014c\u015f\5\17\b\2\u014d")
        buf.write("\u015f\5\21\t\2\u014e\u015f\5\23\n\2\u014f\u015f\5\25")
        buf.write("\13\2\u0150\u015f\5\27\f\2\u0151\u015f\7\"\2\2\u0152\u015f")
        buf.write("\5\31\r\2\u0153\u015f\5\33\16\2\u0154\u015f\5\35\17\2")
        buf.write("\u0155\u015f\5\37\20\2\u0156\u015f\5!\21\2\u0157\u015f")
        buf.write("\5#\22\2\u0158\u015f\5%\23\2\u0159\u015f\5\'\24\2\u015a")
        buf.write("\u015f\5)\25\2\u015b\u015f\5\7\4\2\u015c\u015f\5+\26\2")
        buf.write("\u015d\u015f\5-\27\2\u015e\u0146\3\2\2\2\u015e\u0147\3")
        buf.write("\2\2\2\u015e\u0148\3\2\2\2\u015e\u0149\3\2\2\2\u015e\u014a")
        buf.write("\3\2\2\2\u015e\u014b\3\2\2\2\u015e\u014c\3\2\2\2\u015e")
        buf.write("\u014d\3\2\2\2\u015e\u014e\3\2\2\2\u015e\u014f\3\2\2\2")
        buf.write("\u015e\u0150\3\2\2\2\u015e\u0151\3\2\2\2\u015e\u0152\3")
        buf.write("\2\2\2\u015e\u0153\3\2\2\2\u015e\u0154\3\2\2\2\u015e\u0155")
        buf.write("\3\2\2\2\u015e\u0156\3\2\2\2\u015e\u0157\3\2\2\2\u015e")
        buf.write("\u0158\3\2\2\2\u015e\u0159\3\2\2\2\u015e\u015a\3\2\2\2")
        buf.write("\u015e\u015b\3\2\2\2\u015e\u015c\3\2\2\2\u015e\u015d\3")
        buf.write("\2\2\2\u015f`\3\2\2\2\u0160\u0162\7\17\2\2\u0161\u0160")
        buf.write("\3\2\2\2\u0161\u0162\3\2\2\2\u0162\u0163\3\2\2\2\u0163")
        buf.write("\u0167\7\f\2\2\u0164\u0166\t\6\2\2\u0165\u0164\3\2\2\2")
        buf.write("\u0166\u0169\3\2\2\2\u0167\u0165\3\2\2\2\u0167\u0168\3")
        buf.write("\2\2\2\u0168b\3\2\2\2\u0169\u0167\3\2\2\2\u016a\u016b")
        buf.write("\t\7\2\2\u016b\u016c\3\2\2\2\u016c\u016d\b\62\2\2\u016d")
        buf.write("d\3\2\2\2\31\2\u00db\u00df\u00e4\u00e6\u00ed\u00ef\u00f7")
        buf.write("\u00f9\u00fd\u0101\u0107\u010d\u0113\u0115\u011b\u011e")
        buf.write("\u0126\u0134\u0142\u015e\u0161\u0167\3\b\2\2")
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
    MASEQUAL = 21
    MENEQUAL = 22
    IF = 23
    THEN = 24
    ELSE = 25
    WHILE = 26
    DO = 27
    LET = 28
    IN = 29
    BEGIN = 30
    END = 31
    DEF = 32
    LEN = 33
    FOR = 34
    RETURN = 35
    PRINT = 36
    INTEGER = 37
    IDENTIFIER = 38
    STRING = 39
    FLOAT = 40
    CHARCONTS = 41
    COMENTLINEA = 42
    COMENTMULTILINEA = 43
    NEWLINE = 44
    WS = 45

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "';'", "'='", "'('", "')'", "'['", "']'", "'~'", "':'", 
            "'+'", "'*'", "'-'", "'/'", "'**'", "'%'", "'<'", "'>'", "'<='", 
            "'>='", "'=='", "'+='", "'-='", "'if'", "'then'", "'else'", 
            "'while'", "'do'", "'let'", "'in'", "'begin'", "'end'", "'def'", 
            "'len'", "'for'", "'return'", "'print'" ]

    symbolicNames = [ "<INVALID>",
            "COMA", "PyCOMA", "ASIGN", "PIZQ", "PDER", "CIZQ", "CDER", "VIR", 
            "DOSPUNT", "MAS", "MULT", "MEN", "DIV", "POT", "MOD", "MENQUE", 
            "MAYQUE", "MENQUEEQUAL", "MAYQUEEQUAL", "EQUALEQUAL", "MASEQUAL", 
            "MENEQUAL", "IF", "THEN", "ELSE", "WHILE", "DO", "LET", "IN", 
            "BEGIN", "END", "DEF", "LEN", "FOR", "RETURN", "PRINT", "INTEGER", 
            "IDENTIFIER", "STRING", "FLOAT", "CHARCONTS", "COMENTLINEA", 
            "COMENTMULTILINEA", "NEWLINE", "WS" ]

    ruleNames = [ "COMA", "PyCOMA", "ASIGN", "PIZQ", "PDER", "CIZQ", "CDER", 
                  "VIR", "DOSPUNT", "MAS", "MULT", "MEN", "DIV", "POT", 
                  "MOD", "MENQUE", "MAYQUE", "MENQUEEQUAL", "MAYQUEEQUAL", 
                  "EQUALEQUAL", "MASEQUAL", "MENEQUAL", "IF", "THEN", "ELSE", 
                  "WHILE", "DO", "LET", "IN", "BEGIN", "END", "DEF", "LEN", 
                  "FOR", "RETURN", "PRINT", "INTEGER", "IDENTIFIER", "STRING", 
                  "FLOAT", "CHARCONTS", "COMENTLINEA", "COMENTMULTILINEA", 
                  "DIGIT", "LETTER", "DIGITNOTZERO", "SIMBOLS", "NEWLINE", 
                  "WS" ]

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


