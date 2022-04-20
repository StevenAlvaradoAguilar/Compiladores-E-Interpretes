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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\61")
        buf.write("\u0181\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3")
        buf.write("\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3")
        buf.write("\r\3\r\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\21\3\21\3")
        buf.write("\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3!\3!\3!\3")
        buf.write("\"\3\"\3\"\3\"\3#\3#\3#\3#\3$\3$\3$\3$\3%\3%\3%\3%\3&")
        buf.write("\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\7(\u00e6")
        buf.write("\n(\f(\16(\u00e9\13(\3(\5(\u00ec\n(\3)\3)\3)\7)\u00f1")
        buf.write("\n)\f)\16)\u00f4\13)\3*\3*\3*\3*\3*\7*\u00fb\n*\f*\16")
        buf.write("*\u00fe\13*\3*\3*\3*\3*\3*\3*\7*\u0106\n*\f*\16*\u0109")
        buf.write("\13*\3*\5*\u010c\n*\3+\3+\5+\u0110\n+\3+\3+\6+\u0114\n")
        buf.write("+\r+\16+\u0115\3+\3+\6+\u011a\n+\r+\16+\u011b\3+\3+\6")
        buf.write("+\u0120\n+\r+\16+\u0121\5+\u0124\n+\3,\3,\3,\3,\3,\5,")
        buf.write("\u012b\n,\3,\5,\u012e\n,\3,\3,\3-\3-\7-\u0134\n-\f-\16")
        buf.write("-\u0137\13-\3-\3-\3-\3-\3.\3.\3.\3.\3.\7.\u0142\n.\f.")
        buf.write("\16.\u0145\13.\3.\3.\3.\3.\3.\3.\3.\3.\3/\3/\3\60\5\60")
        buf.write("\u0152\n\60\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3")
        buf.write("\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\5\62\u0170")
        buf.write("\n\62\3\63\3\63\3\64\5\64\u0175\n\64\3\64\3\64\7\64\u0179")
        buf.write("\n\64\f\64\16\64\u017c\13\64\3\65\3\65\3\65\3\65\3\u0143")
        buf.write("\2\66\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write("\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\2_\2a\2c\2e\2g\60i\61\3\2\t\4\2\f\f")
        buf.write("\17\17\3\2\62;\5\2C\\aac|\3\2\63;\t\2##%&((??AA`a\u0080")
        buf.write("\u0080\4\2\13\13\"\"\6\2\13\f\17\17\"\"--\2\u01ae\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write("\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write("/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2g\3\2")
        buf.write("\2\2\2i\3\2\2\2\3k\3\2\2\2\5m\3\2\2\2\7o\3\2\2\2\tq\3")
        buf.write("\2\2\2\13s\3\2\2\2\ru\3\2\2\2\17w\3\2\2\2\21y\3\2\2\2")
        buf.write("\23{\3\2\2\2\25}\3\2\2\2\27\177\3\2\2\2\31\u0081\3\2\2")
        buf.write("\2\33\u0083\3\2\2\2\35\u0085\3\2\2\2\37\u0088\3\2\2\2")
        buf.write("!\u008a\3\2\2\2#\u008c\3\2\2\2%\u008e\3\2\2\2\'\u0091")
        buf.write("\3\2\2\2)\u0094\3\2\2\2+\u0097\3\2\2\2-\u009a\3\2\2\2")
        buf.write("/\u009d\3\2\2\2\61\u00a0\3\2\2\2\63\u00a3\3\2\2\2\65\u00a6")
        buf.write("\3\2\2\2\67\u00ab\3\2\2\29\u00b0\3\2\2\2;\u00b6\3\2\2")
        buf.write("\2=\u00b9\3\2\2\2?\u00bd\3\2\2\2A\u00c0\3\2\2\2C\u00c6")
        buf.write("\3\2\2\2E\u00ca\3\2\2\2G\u00ce\3\2\2\2I\u00d2\3\2\2\2")
        buf.write("K\u00d6\3\2\2\2M\u00dd\3\2\2\2O\u00eb\3\2\2\2Q\u00ed\3")
        buf.write("\2\2\2S\u010b\3\2\2\2U\u0123\3\2\2\2W\u0125\3\2\2\2Y\u0131")
        buf.write("\3\2\2\2[\u013c\3\2\2\2]\u014e\3\2\2\2_\u0151\3\2\2\2")
        buf.write("a\u0153\3\2\2\2c\u016f\3\2\2\2e\u0171\3\2\2\2g\u0174\3")
        buf.write("\2\2\2i\u017d\3\2\2\2kl\7.\2\2l\4\3\2\2\2mn\7=\2\2n\6")
        buf.write("\3\2\2\2op\7?\2\2p\b\3\2\2\2qr\7*\2\2r\n\3\2\2\2st\7+")
        buf.write("\2\2t\f\3\2\2\2uv\7]\2\2v\16\3\2\2\2wx\7_\2\2x\20\3\2")
        buf.write("\2\2yz\7\u0080\2\2z\22\3\2\2\2{|\7<\2\2|\24\3\2\2\2}~")
        buf.write("\7-\2\2~\26\3\2\2\2\177\u0080\7,\2\2\u0080\30\3\2\2\2")
        buf.write("\u0081\u0082\7/\2\2\u0082\32\3\2\2\2\u0083\u0084\7\61")
        buf.write("\2\2\u0084\34\3\2\2\2\u0085\u0086\7,\2\2\u0086\u0087\7")
        buf.write(",\2\2\u0087\36\3\2\2\2\u0088\u0089\7\'\2\2\u0089 \3\2")
        buf.write("\2\2\u008a\u008b\7>\2\2\u008b\"\3\2\2\2\u008c\u008d\7")
        buf.write("@\2\2\u008d$\3\2\2\2\u008e\u008f\7>\2\2\u008f\u0090\7")
        buf.write("?\2\2\u0090&\3\2\2\2\u0091\u0092\7@\2\2\u0092\u0093\7")
        buf.write("?\2\2\u0093(\3\2\2\2\u0094\u0095\7?\2\2\u0095\u0096\7")
        buf.write("?\2\2\u0096*\3\2\2\2\u0097\u0098\7-\2\2\u0098\u0099\7")
        buf.write("?\2\2\u0099,\3\2\2\2\u009a\u009b\7/\2\2\u009b\u009c\7")
        buf.write("?\2\2\u009c.\3\2\2\2\u009d\u009e\7,\2\2\u009e\u009f\7")
        buf.write("?\2\2\u009f\60\3\2\2\2\u00a0\u00a1\7\61\2\2\u00a1\u00a2")
        buf.write("\7?\2\2\u00a2\62\3\2\2\2\u00a3\u00a4\7k\2\2\u00a4\u00a5")
        buf.write("\7h\2\2\u00a5\64\3\2\2\2\u00a6\u00a7\7v\2\2\u00a7\u00a8")
        buf.write("\7j\2\2\u00a8\u00a9\7g\2\2\u00a9\u00aa\7p\2\2\u00aa\66")
        buf.write("\3\2\2\2\u00ab\u00ac\7g\2\2\u00ac\u00ad\7n\2\2\u00ad\u00ae")
        buf.write("\7u\2\2\u00ae\u00af\7g\2\2\u00af8\3\2\2\2\u00b0\u00b1")
        buf.write("\7y\2\2\u00b1\u00b2\7j\2\2\u00b2\u00b3\7k\2\2\u00b3\u00b4")
        buf.write("\7n\2\2\u00b4\u00b5\7g\2\2\u00b5:\3\2\2\2\u00b6\u00b7")
        buf.write("\7f\2\2\u00b7\u00b8\7q\2\2\u00b8<\3\2\2\2\u00b9\u00ba")
        buf.write("\7n\2\2\u00ba\u00bb\7g\2\2\u00bb\u00bc\7v\2\2\u00bc>\3")
        buf.write("\2\2\2\u00bd\u00be\7k\2\2\u00be\u00bf\7p\2\2\u00bf@\3")
        buf.write("\2\2\2\u00c0\u00c1\7d\2\2\u00c1\u00c2\7g\2\2\u00c2\u00c3")
        buf.write("\7i\2\2\u00c3\u00c4\7k\2\2\u00c4\u00c5\7p\2\2\u00c5B\3")
        buf.write("\2\2\2\u00c6\u00c7\7g\2\2\u00c7\u00c8\7p\2\2\u00c8\u00c9")
        buf.write("\7f\2\2\u00c9D\3\2\2\2\u00ca\u00cb\7f\2\2\u00cb\u00cc")
        buf.write("\7g\2\2\u00cc\u00cd\7h\2\2\u00cdF\3\2\2\2\u00ce\u00cf")
        buf.write("\7n\2\2\u00cf\u00d0\7g\2\2\u00d0\u00d1\7p\2\2\u00d1H\3")
        buf.write("\2\2\2\u00d2\u00d3\7h\2\2\u00d3\u00d4\7q\2\2\u00d4\u00d5")
        buf.write("\7t\2\2\u00d5J\3\2\2\2\u00d6\u00d7\7t\2\2\u00d7\u00d8")
        buf.write("\7g\2\2\u00d8\u00d9\7v\2\2\u00d9\u00da\7w\2\2\u00da\u00db")
        buf.write("\7t\2\2\u00db\u00dc\7p\2\2\u00dcL\3\2\2\2\u00dd\u00de")
        buf.write("\7r\2\2\u00de\u00df\7t\2\2\u00df\u00e0\7k\2\2\u00e0\u00e1")
        buf.write("\7p\2\2\u00e1\u00e2\7v\2\2\u00e2N\3\2\2\2\u00e3\u00e7")
        buf.write("\5a\61\2\u00e4\u00e6\5]/\2\u00e5\u00e4\3\2\2\2\u00e6\u00e9")
        buf.write("\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8")
        buf.write("\u00ec\3\2\2\2\u00e9\u00e7\3\2\2\2\u00ea\u00ec\7\62\2")
        buf.write("\2\u00eb\u00e3\3\2\2\2\u00eb\u00ea\3\2\2\2\u00ecP\3\2")
        buf.write("\2\2\u00ed\u00f2\5_\60\2\u00ee\u00f1\5_\60\2\u00ef\u00f1")
        buf.write("\5]/\2\u00f0\u00ee\3\2\2\2\u00f0\u00ef\3\2\2\2\u00f1\u00f4")
        buf.write("\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3")
        buf.write("R\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f5\u00fc\7)\2\2\u00f6")
        buf.write("\u00fb\5_\60\2\u00f7\u00fb\5]/\2\u00f8\u00fb\5c\62\2\u00f9")
        buf.write("\u00fb\5e\63\2\u00fa\u00f6\3\2\2\2\u00fa\u00f7\3\2\2\2")
        buf.write("\u00fa\u00f8\3\2\2\2\u00fa\u00f9\3\2\2\2\u00fb\u00fe\3")
        buf.write("\2\2\2\u00fc\u00fa\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd\u00ff")
        buf.write("\3\2\2\2\u00fe\u00fc\3\2\2\2\u00ff\u010c\7)\2\2\u0100")
        buf.write("\u0107\7$\2\2\u0101\u0106\5_\60\2\u0102\u0106\5]/\2\u0103")
        buf.write("\u0106\5c\62\2\u0104\u0106\5e\63\2\u0105\u0101\3\2\2\2")
        buf.write("\u0105\u0102\3\2\2\2\u0105\u0103\3\2\2\2\u0105\u0104\3")
        buf.write("\2\2\2\u0106\u0109\3\2\2\2\u0107\u0105\3\2\2\2\u0107\u0108")
        buf.write("\3\2\2\2\u0108\u010a\3\2\2\2\u0109\u0107\3\2\2\2\u010a")
        buf.write("\u010c\7$\2\2\u010b\u00f5\3\2\2\2\u010b\u0100\3\2\2\2")
        buf.write("\u010cT\3\2\2\2\u010d\u0110\5a\61\2\u010e\u0110\7\62\2")
        buf.write("\2\u010f\u010d\3\2\2\2\u010f\u010e\3\2\2\2\u0110\u0111")
        buf.write("\3\2\2\2\u0111\u0113\7\60\2\2\u0112\u0114\5]/\2\u0113")
        buf.write("\u0112\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0113\3\2\2\2")
        buf.write("\u0115\u0116\3\2\2\2\u0116\u0124\3\2\2\2\u0117\u0119\5")
        buf.write("a\61\2\u0118\u011a\5]/\2\u0119\u0118\3\2\2\2\u011a\u011b")
        buf.write("\3\2\2\2\u011b\u0119\3\2\2\2\u011b\u011c\3\2\2\2\u011c")
        buf.write("\u011d\3\2\2\2\u011d\u011f\7\60\2\2\u011e\u0120\5]/\2")
        buf.write("\u011f\u011e\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u011f\3")
        buf.write("\2\2\2\u0121\u0122\3\2\2\2\u0122\u0124\3\2\2\2\u0123\u010f")
        buf.write("\3\2\2\2\u0123\u0117\3\2\2\2\u0124V\3\2\2\2\u0125\u012d")
        buf.write("\7)\2\2\u0126\u012b\5_\60\2\u0127\u012b\5]/\2\u0128\u012b")
        buf.write("\5c\62\2\u0129\u012b\5e\63\2\u012a\u0126\3\2\2\2\u012a")
        buf.write("\u0127\3\2\2\2\u012a\u0128\3\2\2\2\u012a\u0129\3\2\2\2")
        buf.write("\u012b\u012e\3\2\2\2\u012c\u012e\3\2\2\2\u012d\u012a\3")
        buf.write("\2\2\2\u012d\u012c\3\2\2\2\u012e\u012f\3\2\2\2\u012f\u0130")
        buf.write("\7)\2\2\u0130X\3\2\2\2\u0131\u0135\7%\2\2\u0132\u0134")
        buf.write("\n\2\2\2\u0133\u0132\3\2\2\2\u0134\u0137\3\2\2\2\u0135")
        buf.write("\u0133\3\2\2\2\u0135\u0136\3\2\2\2\u0136\u0138\3\2\2\2")
        buf.write("\u0137\u0135\3\2\2\2\u0138\u0139\5g\64\2\u0139\u013a\3")
        buf.write("\2\2\2\u013a\u013b\b-\2\2\u013bZ\3\2\2\2\u013c\u013d\7")
        buf.write("$\2\2\u013d\u013e\7$\2\2\u013e\u013f\7$\2\2\u013f\u0143")
        buf.write("\3\2\2\2\u0140\u0142\13\2\2\2\u0141\u0140\3\2\2\2\u0142")
        buf.write("\u0145\3\2\2\2\u0143\u0144\3\2\2\2\u0143\u0141\3\2\2\2")
        buf.write("\u0144\u0146\3\2\2\2\u0145\u0143\3\2\2\2\u0146\u0147\7")
        buf.write("$\2\2\u0147\u0148\7$\2\2\u0148\u0149\7$\2\2\u0149\u014a")
        buf.write("\3\2\2\2\u014a\u014b\5g\64\2\u014b\u014c\3\2\2\2\u014c")
        buf.write("\u014d\b.\2\2\u014d\\\3\2\2\2\u014e\u014f\t\3\2\2\u014f")
        buf.write("^\3\2\2\2\u0150\u0152\t\4\2\2\u0151\u0150\3\2\2\2\u0152")
        buf.write("`\3\2\2\2\u0153\u0154\t\5\2\2\u0154b\3\2\2\2\u0155\u0170")
        buf.write("\5\3\2\2\u0156\u0170\5\5\3\2\u0157\u0170\5\7\4\2\u0158")
        buf.write("\u0170\5\t\5\2\u0159\u0170\5\13\6\2\u015a\u0170\5\r\7")
        buf.write("\2\u015b\u0170\5\17\b\2\u015c\u0170\5\21\t\2\u015d\u0170")
        buf.write("\5\23\n\2\u015e\u0170\5\25\13\2\u015f\u0170\5\27\f\2\u0160")
        buf.write("\u0170\7\"\2\2\u0161\u0170\5\31\r\2\u0162\u0170\5\33\16")
        buf.write("\2\u0163\u0170\5\35\17\2\u0164\u0170\5\37\20\2\u0165\u0170")
        buf.write("\5!\21\2\u0166\u0170\5#\22\2\u0167\u0170\5%\23\2\u0168")
        buf.write("\u0170\5\'\24\2\u0169\u0170\5)\25\2\u016a\u0170\5\7\4")
        buf.write("\2\u016b\u0170\5+\26\2\u016c\u0170\5-\27\2\u016d\u0170")
        buf.write("\5/\30\2\u016e\u0170\5\61\31\2\u016f\u0155\3\2\2\2\u016f")
        buf.write("\u0156\3\2\2\2\u016f\u0157\3\2\2\2\u016f\u0158\3\2\2\2")
        buf.write("\u016f\u0159\3\2\2\2\u016f\u015a\3\2\2\2\u016f\u015b\3")
        buf.write("\2\2\2\u016f\u015c\3\2\2\2\u016f\u015d\3\2\2\2\u016f\u015e")
        buf.write("\3\2\2\2\u016f\u015f\3\2\2\2\u016f\u0160\3\2\2\2\u016f")
        buf.write("\u0161\3\2\2\2\u016f\u0162\3\2\2\2\u016f\u0163\3\2\2\2")
        buf.write("\u016f\u0164\3\2\2\2\u016f\u0165\3\2\2\2\u016f\u0166\3")
        buf.write("\2\2\2\u016f\u0167\3\2\2\2\u016f\u0168\3\2\2\2\u016f\u0169")
        buf.write("\3\2\2\2\u016f\u016a\3\2\2\2\u016f\u016b\3\2\2\2\u016f")
        buf.write("\u016c\3\2\2\2\u016f\u016d\3\2\2\2\u016f\u016e\3\2\2\2")
        buf.write("\u0170d\3\2\2\2\u0171\u0172\t\6\2\2\u0172f\3\2\2\2\u0173")
        buf.write("\u0175\7\17\2\2\u0174\u0173\3\2\2\2\u0174\u0175\3\2\2")
        buf.write("\2\u0175\u0176\3\2\2\2\u0176\u017a\7\f\2\2\u0177\u0179")
        buf.write("\t\7\2\2\u0178\u0177\3\2\2\2\u0179\u017c\3\2\2\2\u017a")
        buf.write("\u0178\3\2\2\2\u017a\u017b\3\2\2\2\u017bh\3\2\2\2\u017c")
        buf.write("\u017a\3\2\2\2\u017d\u017e\t\b\2\2\u017e\u017f\3\2\2\2")
        buf.write("\u017f\u0180\b\65\2\2\u0180j\3\2\2\2\31\2\u00e7\u00eb")
        buf.write("\u00f0\u00f2\u00fa\u00fc\u0105\u0107\u010b\u010f\u0115")
        buf.write("\u011b\u0121\u0123\u012a\u012d\u0135\u0143\u0151\u016f")
        buf.write("\u0174\u017a\3\b\2\2")
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
                  "SIMBOLS", "SPECIALSIMBOLS", "NEWLINE", "WS" ]

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


