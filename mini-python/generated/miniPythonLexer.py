# Generated from D:/Universidad/Compiladores_e_Interpretes/Compiladores-E-Interpretes/Compiladores-E-Interpretes/mini-python\miniPython.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\61")
        buf.write("\u017a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7")
        buf.write("\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3 \3 \3 \3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"")
        buf.write("\3#\3#\3#\3#\3$\3$\3$\3$\3%\3%\3%\3%\3&\3&\3&\3&\3&\3")
        buf.write("&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\7(\u00e4\n(\f(\16(")
        buf.write("\u00e7\13(\3(\5(\u00ea\n(\3)\3)\3)\7)\u00ef\n)\f)\16)")
        buf.write("\u00f2\13)\3*\3*\3*\3*\7*\u00f8\n*\f*\16*\u00fb\13*\3")
        buf.write("*\3*\3*\3*\3*\7*\u0102\n*\f*\16*\u0105\13*\3*\5*\u0108")
        buf.write("\n*\3+\3+\5+\u010c\n+\3+\3+\6+\u0110\n+\r+\16+\u0111\3")
        buf.write("+\3+\6+\u0116\n+\r+\16+\u0117\3+\3+\6+\u011c\n+\r+\16")
        buf.write("+\u011d\5+\u0120\n+\3,\3,\3,\3,\5,\u0126\n,\3,\5,\u0129")
        buf.write("\n,\3,\3,\3-\3-\7-\u012f\n-\f-\16-\u0132\13-\3-\3-\3-")
        buf.write("\3-\3.\3.\3.\3.\3.\7.\u013d\n.\f.\16.\u0140\13.\3.\3.")
        buf.write("\3.\3.\3.\3.\3.\3.\3/\3/\3\60\5\60\u014d\n\60\3\61\3\61")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\5\62\u016b\n\62\3\63\5\63\u016e\n")
        buf.write("\63\3\63\3\63\7\63\u0172\n\63\f\63\16\63\u0175\13\63\3")
        buf.write("\64\3\64\3\64\3\64\3\u013e\2\65\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!")
        buf.write("\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\2_\2a\2")
        buf.write("c\2e\60g\61\3\2\b\4\2\f\f\17\17\3\2\62;\5\2C\\aac|\3\2")
        buf.write("\63;\4\2\13\13\"\"\6\2\13\f\17\17\"\"--\2\u01a5\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2")
        buf.write("\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3")
        buf.write("\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2")
        buf.write("\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3")
        buf.write("\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K")
        buf.write("\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2")
        buf.write("U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2e\3\2\2\2")
        buf.write("\2g\3\2\2\2\3i\3\2\2\2\5k\3\2\2\2\7m\3\2\2\2\to\3\2\2")
        buf.write("\2\13q\3\2\2\2\rs\3\2\2\2\17u\3\2\2\2\21w\3\2\2\2\23y")
        buf.write("\3\2\2\2\25{\3\2\2\2\27}\3\2\2\2\31\177\3\2\2\2\33\u0081")
        buf.write("\3\2\2\2\35\u0083\3\2\2\2\37\u0086\3\2\2\2!\u0088\3\2")
        buf.write("\2\2#\u008a\3\2\2\2%\u008c\3\2\2\2\'\u008f\3\2\2\2)\u0092")
        buf.write("\3\2\2\2+\u0095\3\2\2\2-\u0098\3\2\2\2/\u009b\3\2\2\2")
        buf.write("\61\u009e\3\2\2\2\63\u00a1\3\2\2\2\65\u00a4\3\2\2\2\67")
        buf.write("\u00a9\3\2\2\29\u00ae\3\2\2\2;\u00b4\3\2\2\2=\u00b7\3")
        buf.write("\2\2\2?\u00bb\3\2\2\2A\u00be\3\2\2\2C\u00c4\3\2\2\2E\u00c8")
        buf.write("\3\2\2\2G\u00cc\3\2\2\2I\u00d0\3\2\2\2K\u00d4\3\2\2\2")
        buf.write("M\u00db\3\2\2\2O\u00e9\3\2\2\2Q\u00eb\3\2\2\2S\u0107\3")
        buf.write("\2\2\2U\u011f\3\2\2\2W\u0121\3\2\2\2Y\u012c\3\2\2\2[\u0137")
        buf.write("\3\2\2\2]\u0149\3\2\2\2_\u014c\3\2\2\2a\u014e\3\2\2\2")
        buf.write("c\u016a\3\2\2\2e\u016d\3\2\2\2g\u0176\3\2\2\2ij\7.\2\2")
        buf.write("j\4\3\2\2\2kl\7=\2\2l\6\3\2\2\2mn\7?\2\2n\b\3\2\2\2op")
        buf.write("\7*\2\2p\n\3\2\2\2qr\7+\2\2r\f\3\2\2\2st\7]\2\2t\16\3")
        buf.write("\2\2\2uv\7_\2\2v\20\3\2\2\2wx\7\u0080\2\2x\22\3\2\2\2")
        buf.write("yz\7<\2\2z\24\3\2\2\2{|\7-\2\2|\26\3\2\2\2}~\7,\2\2~\30")
        buf.write("\3\2\2\2\177\u0080\7/\2\2\u0080\32\3\2\2\2\u0081\u0082")
        buf.write("\7\61\2\2\u0082\34\3\2\2\2\u0083\u0084\7,\2\2\u0084\u0085")
        buf.write("\7,\2\2\u0085\36\3\2\2\2\u0086\u0087\7\'\2\2\u0087 \3")
        buf.write("\2\2\2\u0088\u0089\7>\2\2\u0089\"\3\2\2\2\u008a\u008b")
        buf.write("\7@\2\2\u008b$\3\2\2\2\u008c\u008d\7>\2\2\u008d\u008e")
        buf.write("\7?\2\2\u008e&\3\2\2\2\u008f\u0090\7@\2\2\u0090\u0091")
        buf.write("\7?\2\2\u0091(\3\2\2\2\u0092\u0093\7?\2\2\u0093\u0094")
        buf.write("\7?\2\2\u0094*\3\2\2\2\u0095\u0096\7-\2\2\u0096\u0097")
        buf.write("\7?\2\2\u0097,\3\2\2\2\u0098\u0099\7/\2\2\u0099\u009a")
        buf.write("\7?\2\2\u009a.\3\2\2\2\u009b\u009c\7,\2\2\u009c\u009d")
        buf.write("\7?\2\2\u009d\60\3\2\2\2\u009e\u009f\7\61\2\2\u009f\u00a0")
        buf.write("\7?\2\2\u00a0\62\3\2\2\2\u00a1\u00a2\7k\2\2\u00a2\u00a3")
        buf.write("\7h\2\2\u00a3\64\3\2\2\2\u00a4\u00a5\7v\2\2\u00a5\u00a6")
        buf.write("\7j\2\2\u00a6\u00a7\7g\2\2\u00a7\u00a8\7p\2\2\u00a8\66")
        buf.write("\3\2\2\2\u00a9\u00aa\7g\2\2\u00aa\u00ab\7n\2\2\u00ab\u00ac")
        buf.write("\7u\2\2\u00ac\u00ad\7g\2\2\u00ad8\3\2\2\2\u00ae\u00af")
        buf.write("\7y\2\2\u00af\u00b0\7j\2\2\u00b0\u00b1\7k\2\2\u00b1\u00b2")
        buf.write("\7n\2\2\u00b2\u00b3\7g\2\2\u00b3:\3\2\2\2\u00b4\u00b5")
        buf.write("\7f\2\2\u00b5\u00b6\7q\2\2\u00b6<\3\2\2\2\u00b7\u00b8")
        buf.write("\7n\2\2\u00b8\u00b9\7g\2\2\u00b9\u00ba\7v\2\2\u00ba>\3")
        buf.write("\2\2\2\u00bb\u00bc\7k\2\2\u00bc\u00bd\7p\2\2\u00bd@\3")
        buf.write("\2\2\2\u00be\u00bf\7d\2\2\u00bf\u00c0\7g\2\2\u00c0\u00c1")
        buf.write("\7i\2\2\u00c1\u00c2\7k\2\2\u00c2\u00c3\7p\2\2\u00c3B\3")
        buf.write("\2\2\2\u00c4\u00c5\7g\2\2\u00c5\u00c6\7p\2\2\u00c6\u00c7")
        buf.write("\7f\2\2\u00c7D\3\2\2\2\u00c8\u00c9\7f\2\2\u00c9\u00ca")
        buf.write("\7g\2\2\u00ca\u00cb\7h\2\2\u00cbF\3\2\2\2\u00cc\u00cd")
        buf.write("\7n\2\2\u00cd\u00ce\7g\2\2\u00ce\u00cf\7p\2\2\u00cfH\3")
        buf.write("\2\2\2\u00d0\u00d1\7h\2\2\u00d1\u00d2\7q\2\2\u00d2\u00d3")
        buf.write("\7t\2\2\u00d3J\3\2\2\2\u00d4\u00d5\7t\2\2\u00d5\u00d6")
        buf.write("\7g\2\2\u00d6\u00d7\7v\2\2\u00d7\u00d8\7w\2\2\u00d8\u00d9")
        buf.write("\7t\2\2\u00d9\u00da\7p\2\2\u00daL\3\2\2\2\u00db\u00dc")
        buf.write("\7r\2\2\u00dc\u00dd\7t\2\2\u00dd\u00de\7k\2\2\u00de\u00df")
        buf.write("\7p\2\2\u00df\u00e0\7v\2\2\u00e0N\3\2\2\2\u00e1\u00e5")
        buf.write("\5a\61\2\u00e2\u00e4\5]/\2\u00e3\u00e2\3\2\2\2\u00e4\u00e7")
        buf.write("\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6")
        buf.write("\u00ea\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e8\u00ea\7\62\2")
        buf.write("\2\u00e9\u00e1\3\2\2\2\u00e9\u00e8\3\2\2\2\u00eaP\3\2")
        buf.write("\2\2\u00eb\u00f0\5_\60\2\u00ec\u00ef\5_\60\2\u00ed\u00ef")
        buf.write("\5]/\2\u00ee\u00ec\3\2\2\2\u00ee\u00ed\3\2\2\2\u00ef\u00f2")
        buf.write("\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1")
        buf.write("R\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f3\u00f9\7)\2\2\u00f4")
        buf.write("\u00f8\5_\60\2\u00f5\u00f8\5]/\2\u00f6\u00f8\5c\62\2\u00f7")
        buf.write("\u00f4\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f7\u00f6\3\2\2\2")
        buf.write("\u00f8\u00fb\3\2\2\2\u00f9\u00f7\3\2\2\2\u00f9\u00fa\3")
        buf.write("\2\2\2\u00fa\u00fc\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fc\u0108")
        buf.write("\7)\2\2\u00fd\u0103\7$\2\2\u00fe\u0102\5_\60\2\u00ff\u0102")
        buf.write("\5]/\2\u0100\u0102\5c\62\2\u0101\u00fe\3\2\2\2\u0101\u00ff")
        buf.write("\3\2\2\2\u0101\u0100\3\2\2\2\u0102\u0105\3\2\2\2\u0103")
        buf.write("\u0101\3\2\2\2\u0103\u0104\3\2\2\2\u0104\u0106\3\2\2\2")
        buf.write("\u0105\u0103\3\2\2\2\u0106\u0108\7$\2\2\u0107\u00f3\3")
        buf.write("\2\2\2\u0107\u00fd\3\2\2\2\u0108T\3\2\2\2\u0109\u010c")
        buf.write("\5a\61\2\u010a\u010c\7\62\2\2\u010b\u0109\3\2\2\2\u010b")
        buf.write("\u010a\3\2\2\2\u010c\u010d\3\2\2\2\u010d\u010f\7\60\2")
        buf.write("\2\u010e\u0110\5]/\2\u010f\u010e\3\2\2\2\u0110\u0111\3")
        buf.write("\2\2\2\u0111\u010f\3\2\2\2\u0111\u0112\3\2\2\2\u0112\u0120")
        buf.write("\3\2\2\2\u0113\u0115\5a\61\2\u0114\u0116\5]/\2\u0115\u0114")
        buf.write("\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u0115\3\2\2\2\u0117")
        buf.write("\u0118\3\2\2\2\u0118\u0119\3\2\2\2\u0119\u011b\7\60\2")
        buf.write("\2\u011a\u011c\5]/\2\u011b\u011a\3\2\2\2\u011c\u011d\3")
        buf.write("\2\2\2\u011d\u011b\3\2\2\2\u011d\u011e\3\2\2\2\u011e\u0120")
        buf.write("\3\2\2\2\u011f\u010b\3\2\2\2\u011f\u0113\3\2\2\2\u0120")
        buf.write("V\3\2\2\2\u0121\u0128\7)\2\2\u0122\u0126\5_\60\2\u0123")
        buf.write("\u0126\5]/\2\u0124\u0126\5c\62\2\u0125\u0122\3\2\2\2\u0125")
        buf.write("\u0123\3\2\2\2\u0125\u0124\3\2\2\2\u0126\u0129\3\2\2\2")
        buf.write("\u0127\u0129\3\2\2\2\u0128\u0125\3\2\2\2\u0128\u0127\3")
        buf.write("\2\2\2\u0129\u012a\3\2\2\2\u012a\u012b\7)\2\2\u012bX\3")
        buf.write("\2\2\2\u012c\u0130\7%\2\2\u012d\u012f\n\2\2\2\u012e\u012d")
        buf.write("\3\2\2\2\u012f\u0132\3\2\2\2\u0130\u012e\3\2\2\2\u0130")
        buf.write("\u0131\3\2\2\2\u0131\u0133\3\2\2\2\u0132\u0130\3\2\2\2")
        buf.write("\u0133\u0134\5e\63\2\u0134\u0135\3\2\2\2\u0135\u0136\b")
        buf.write("-\2\2\u0136Z\3\2\2\2\u0137\u0138\7$\2\2\u0138\u0139\7")
        buf.write("$\2\2\u0139\u013a\7$\2\2\u013a\u013e\3\2\2\2\u013b\u013d")
        buf.write("\13\2\2\2\u013c\u013b\3\2\2\2\u013d\u0140\3\2\2\2\u013e")
        buf.write("\u013f\3\2\2\2\u013e\u013c\3\2\2\2\u013f\u0141\3\2\2\2")
        buf.write("\u0140\u013e\3\2\2\2\u0141\u0142\7$\2\2\u0142\u0143\7")
        buf.write("$\2\2\u0143\u0144\7$\2\2\u0144\u0145\3\2\2\2\u0145\u0146")
        buf.write("\5e\63\2\u0146\u0147\3\2\2\2\u0147\u0148\b.\2\2\u0148")
        buf.write("\\\3\2\2\2\u0149\u014a\t\3\2\2\u014a^\3\2\2\2\u014b\u014d")
        buf.write("\t\4\2\2\u014c\u014b\3\2\2\2\u014d`\3\2\2\2\u014e\u014f")
        buf.write("\t\5\2\2\u014fb\3\2\2\2\u0150\u016b\5\3\2\2\u0151\u016b")
        buf.write("\5\5\3\2\u0152\u016b\5\7\4\2\u0153\u016b\5\t\5\2\u0154")
        buf.write("\u016b\5\13\6\2\u0155\u016b\5\r\7\2\u0156\u016b\5\17\b")
        buf.write("\2\u0157\u016b\5\21\t\2\u0158\u016b\5\23\n\2\u0159\u016b")
        buf.write("\5\25\13\2\u015a\u016b\5\27\f\2\u015b\u016b\7\"\2\2\u015c")
        buf.write("\u016b\5\31\r\2\u015d\u016b\5\33\16\2\u015e\u016b\5\35")
        buf.write("\17\2\u015f\u016b\5\37\20\2\u0160\u016b\5!\21\2\u0161")
        buf.write("\u016b\5#\22\2\u0162\u016b\5%\23\2\u0163\u016b\5\'\24")
        buf.write("\2\u0164\u016b\5)\25\2\u0165\u016b\5\7\4\2\u0166\u016b")
        buf.write("\5+\26\2\u0167\u016b\5-\27\2\u0168\u016b\5/\30\2\u0169")
        buf.write("\u016b\5\61\31\2\u016a\u0150\3\2\2\2\u016a\u0151\3\2\2")
        buf.write("\2\u016a\u0152\3\2\2\2\u016a\u0153\3\2\2\2\u016a\u0154")
        buf.write("\3\2\2\2\u016a\u0155\3\2\2\2\u016a\u0156\3\2\2\2\u016a")
        buf.write("\u0157\3\2\2\2\u016a\u0158\3\2\2\2\u016a\u0159\3\2\2\2")
        buf.write("\u016a\u015a\3\2\2\2\u016a\u015b\3\2\2\2\u016a\u015c\3")
        buf.write("\2\2\2\u016a\u015d\3\2\2\2\u016a\u015e\3\2\2\2\u016a\u015f")
        buf.write("\3\2\2\2\u016a\u0160\3\2\2\2\u016a\u0161\3\2\2\2\u016a")
        buf.write("\u0162\3\2\2\2\u016a\u0163\3\2\2\2\u016a\u0164\3\2\2\2")
        buf.write("\u016a\u0165\3\2\2\2\u016a\u0166\3\2\2\2\u016a\u0167\3")
        buf.write("\2\2\2\u016a\u0168\3\2\2\2\u016a\u0169\3\2\2\2\u016bd")
        buf.write("\3\2\2\2\u016c\u016e\7\17\2\2\u016d\u016c\3\2\2\2\u016d")
        buf.write("\u016e\3\2\2\2\u016e\u016f\3\2\2\2\u016f\u0173\7\f\2\2")
        buf.write("\u0170\u0172\t\6\2\2\u0171\u0170\3\2\2\2\u0172\u0175\3")
        buf.write("\2\2\2\u0173\u0171\3\2\2\2\u0173\u0174\3\2\2\2\u0174f")
        buf.write("\3\2\2\2\u0175\u0173\3\2\2\2\u0176\u0177\t\7\2\2\u0177")
        buf.write("\u0178\3\2\2\2\u0178\u0179\b\64\2\2\u0179h\3\2\2\2\31")
        buf.write("\2\u00e5\u00e9\u00ee\u00f0\u00f7\u00f9\u0101\u0103\u0107")
        buf.write("\u010b\u0111\u0117\u011d\u011f\u0125\u0128\u0130\u013e")
        buf.write("\u014c\u016a\u016d\u0173\3\b\2\2")
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
    MULTEQUAL = 23
    DIVEQUAL = 24
    IF = 25
    THEN = 26
    ELSE = 27
    WHILE = 28
    DO = 29
    LET = 30
    IN = 31
    BEGIN = 32
    END = 33
    DEF = 34
    LEN = 35
    FOR = 36
    RETURN = 37
    PRINT = 38
    INTEGER = 39
    IDENTIFIER = 40
    STRING = 41
    FLOAT = 42
    CHARCONTS = 43
    COMENTLINEA = 44
    COMENTMULTILINEA = 45
    NEWLINE = 46
    WS = 47

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "';'", "'='", "'('", "')'", "'['", "']'", "'~'", "':'", 
            "'+'", "'*'", "'-'", "'/'", "'**'", "'%'", "'<'", "'>'", "'<='", 
            "'>='", "'=='", "'+='", "'-='", "'*='", "'/='", "'if'", "'then'", 
            "'else'", "'while'", "'do'", "'let'", "'in'", "'begin'", "'end'", 
            "'def'", "'len'", "'for'", "'return'", "'print'" ]

    symbolicNames = [ "<INVALID>",
            "COMA", "PyCOMA", "ASIGN", "PIZQ", "PDER", "CIZQ", "CDER", "VIR", 
            "DOSPUNT", "MAS", "MULT", "MEN", "DIV", "POT", "MOD", "MENQUE", 
            "MAYQUE", "MENQUEEQUAL", "MAYQUEEQUAL", "EQUALEQUAL", "MASEQUAL", 
            "MENEQUAL", "MULTEQUAL", "DIVEQUAL", "IF", "THEN", "ELSE", "WHILE", 
            "DO", "LET", "IN", "BEGIN", "END", "DEF", "LEN", "FOR", "RETURN", 
            "PRINT", "INTEGER", "IDENTIFIER", "STRING", "FLOAT", "CHARCONTS", 
            "COMENTLINEA", "COMENTMULTILINEA", "NEWLINE", "WS" ]

    ruleNames = [ "COMA", "PyCOMA", "ASIGN", "PIZQ", "PDER", "CIZQ", "CDER", 
                  "VIR", "DOSPUNT", "MAS", "MULT", "MEN", "DIV", "POT", 
                  "MOD", "MENQUE", "MAYQUE", "MENQUEEQUAL", "MAYQUEEQUAL", 
                  "EQUALEQUAL", "MASEQUAL", "MENEQUAL", "MULTEQUAL", "DIVEQUAL", 
                  "IF", "THEN", "ELSE", "WHILE", "DO", "LET", "IN", "BEGIN", 
                  "END", "DEF", "LEN", "FOR", "RETURN", "PRINT", "INTEGER", 
                  "IDENTIFIER", "STRING", "FLOAT", "CHARCONTS", "COMENTLINEA", 
                  "COMENTMULTILINEA", "DIGIT", "LETTER", "DIGITNOTZERO", 
                  "SIMBOLS", "NEWLINE", "WS" ]

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


