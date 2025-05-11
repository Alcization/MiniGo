# Generated from main/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2?")
        buf.write("\u01e9\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3")
        buf.write("$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3")
        buf.write("*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3")
        buf.write("\62\3\62\3\63\3\63\5\63\u014f\n\63\3\63\3\63\5\63\u0153")
        buf.write("\n\63\3\64\3\64\3\65\3\65\7\65\u0159\n\65\f\65\16\65\u015c")
        buf.write("\13\65\3\66\3\66\3\66\3\66\5\66\u0162\n\66\3\67\3\67\3")
        buf.write("\67\7\67\u0167\n\67\f\67\16\67\u016a\13\67\5\67\u016c")
        buf.write("\n\67\38\38\38\68\u0171\n8\r8\168\u0172\39\39\39\69\u0178")
        buf.write("\n9\r9\169\u0179\3:\3:\3:\6:\u017f\n:\r:\16:\u0180\3;")
        buf.write("\3;\3;\5;\u0186\n;\3;\5;\u0189\n;\3<\6<\u018c\n<\r<\16")
        buf.write("<\u018d\3=\3=\5=\u0192\n=\3=\3=\3>\3>\7>\u0198\n>\f>\16")
        buf.write(">\u019b\13>\3>\3>\3?\3?\3?\3@\3@\5@\u01a4\n@\3A\3A\3A")
        buf.write("\3B\3B\3B\5B\u01ac\nB\3C\6C\u01af\nC\rC\16C\u01b0\3C\3")
        buf.write("C\3D\3D\3D\3D\3D\7D\u01ba\nD\fD\16D\u01bd\13D\3D\3D\3")
        buf.write("D\3D\3D\3E\3E\3E\3E\7E\u01c8\nE\fE\16E\u01cb\13E\3E\3")
        buf.write("E\3F\3F\3F\3G\3G\7G\u01d4\nG\fG\16G\u01d7\13G\3G\3G\3")
        buf.write("G\5G\u01dc\nG\3G\3G\3H\3H\7H\u01e2\nH\fH\16H\u01e5\13")
        buf.write("H\3H\3H\3H\3\u01bb\2I\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37")
        buf.write("= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64")
        buf.write("g\65i\66k\67m\2o\2q\2s\2u8w\2y\2{9}\2\177\2\u0081\2\u0083")
        buf.write("\2\u0085:\u0087;\u0089<\u008b=\u008d>\u008f?\3\2\25\5")
        buf.write("\2C\\aac|\6\2\62;C\\aac|\3\2\63;\3\2\62;\4\2DDdd\3\2\62")
        buf.write("\63\4\2QQqq\3\2\629\4\2ZZzz\5\2\62;CHch\4\2GGgg\4\2--")
        buf.write("//\7\2$$^^ppttvv\6\2\f\f\17\17$$^^\3\2\17\17\7\2))^^p")
        buf.write("pttvv\5\2\13\13\16\17\"\"\4\2\f\f\17\17\3\3\f\f\2\u01f7")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2u\3\2\2\2\2{\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2")
        buf.write("\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\3\u0091\3\2\2\2\5\u0094")
        buf.write("\3\2\2\2\7\u0099\3\2\2\2\t\u009d\3\2\2\2\13\u00a4\3\2")
        buf.write("\2\2\r\u00a9\3\2\2\2\17\u00ae\3\2\2\2\21\u00b5\3\2\2\2")
        buf.write("\23\u00bf\3\2\2\2\25\u00c6\3\2\2\2\27\u00ca\3\2\2\2\31")
        buf.write("\u00d0\3\2\2\2\33\u00d8\3\2\2\2\35\u00de\3\2\2\2\37\u00e2")
        buf.write("\3\2\2\2!\u00eb\3\2\2\2#\u00f1\3\2\2\2%\u00f7\3\2\2\2")
        buf.write("\'\u00fb\3\2\2\2)\u0100\3\2\2\2+\u0106\3\2\2\2-\u0108")
        buf.write("\3\2\2\2/\u010a\3\2\2\2\61\u010c\3\2\2\2\63\u010e\3\2")
        buf.write("\2\2\65\u0110\3\2\2\2\67\u0113\3\2\2\29\u0116\3\2\2\2")
        buf.write(";\u0118\3\2\2\2=\u011b\3\2\2\2?\u011d\3\2\2\2A\u0120\3")
        buf.write("\2\2\2C\u0123\3\2\2\2E\u0126\3\2\2\2G\u0128\3\2\2\2I\u012b")
        buf.write("\3\2\2\2K\u012e\3\2\2\2M\u0131\3\2\2\2O\u0134\3\2\2\2")
        buf.write("Q\u0137\3\2\2\2S\u013a\3\2\2\2U\u013c\3\2\2\2W\u013e\3")
        buf.write("\2\2\2Y\u0140\3\2\2\2[\u0142\3\2\2\2]\u0144\3\2\2\2_\u0146")
        buf.write("\3\2\2\2a\u0148\3\2\2\2c\u014a\3\2\2\2e\u0152\3\2\2\2")
        buf.write("g\u0154\3\2\2\2i\u0156\3\2\2\2k\u0161\3\2\2\2m\u016b\3")
        buf.write("\2\2\2o\u016d\3\2\2\2q\u0174\3\2\2\2s\u017b\3\2\2\2u\u0182")
        buf.write("\3\2\2\2w\u018b\3\2\2\2y\u018f\3\2\2\2{\u0195\3\2\2\2")
        buf.write("}\u019e\3\2\2\2\177\u01a3\3\2\2\2\u0081\u01a5\3\2\2\2")
        buf.write("\u0083\u01ab\3\2\2\2\u0085\u01ae\3\2\2\2\u0087\u01b4\3")
        buf.write("\2\2\2\u0089\u01c3\3\2\2\2\u008b\u01ce\3\2\2\2\u008d\u01d1")
        buf.write("\3\2\2\2\u008f\u01df\3\2\2\2\u0091\u0092\7k\2\2\u0092")
        buf.write("\u0093\7h\2\2\u0093\4\3\2\2\2\u0094\u0095\7g\2\2\u0095")
        buf.write("\u0096\7n\2\2\u0096\u0097\7u\2\2\u0097\u0098\7g\2\2\u0098")
        buf.write("\6\3\2\2\2\u0099\u009a\7h\2\2\u009a\u009b\7q\2\2\u009b")
        buf.write("\u009c\7t\2\2\u009c\b\3\2\2\2\u009d\u009e\7t\2\2\u009e")
        buf.write("\u009f\7g\2\2\u009f\u00a0\7v\2\2\u00a0\u00a1\7w\2\2\u00a1")
        buf.write("\u00a2\7t\2\2\u00a2\u00a3\7p\2\2\u00a3\n\3\2\2\2\u00a4")
        buf.write("\u00a5\7h\2\2\u00a5\u00a6\7w\2\2\u00a6\u00a7\7p\2\2\u00a7")
        buf.write("\u00a8\7e\2\2\u00a8\f\3\2\2\2\u00a9\u00aa\7v\2\2\u00aa")
        buf.write("\u00ab\7{\2\2\u00ab\u00ac\7r\2\2\u00ac\u00ad\7g\2\2\u00ad")
        buf.write("\16\3\2\2\2\u00ae\u00af\7u\2\2\u00af\u00b0\7v\2\2\u00b0")
        buf.write("\u00b1\7t\2\2\u00b1\u00b2\7w\2\2\u00b2\u00b3\7e\2\2\u00b3")
        buf.write("\u00b4\7v\2\2\u00b4\20\3\2\2\2\u00b5\u00b6\7k\2\2\u00b6")
        buf.write("\u00b7\7p\2\2\u00b7\u00b8\7v\2\2\u00b8\u00b9\7g\2\2\u00b9")
        buf.write("\u00ba\7t\2\2\u00ba\u00bb\7h\2\2\u00bb\u00bc\7c\2\2\u00bc")
        buf.write("\u00bd\7e\2\2\u00bd\u00be\7g\2\2\u00be\22\3\2\2\2\u00bf")
        buf.write("\u00c0\7u\2\2\u00c0\u00c1\7v\2\2\u00c1\u00c2\7t\2\2\u00c2")
        buf.write("\u00c3\7k\2\2\u00c3\u00c4\7p\2\2\u00c4\u00c5\7i\2\2\u00c5")
        buf.write("\24\3\2\2\2\u00c6\u00c7\7k\2\2\u00c7\u00c8\7p\2\2\u00c8")
        buf.write("\u00c9\7v\2\2\u00c9\26\3\2\2\2\u00ca\u00cb\7h\2\2\u00cb")
        buf.write("\u00cc\7n\2\2\u00cc\u00cd\7q\2\2\u00cd\u00ce\7c\2\2\u00ce")
        buf.write("\u00cf\7v\2\2\u00cf\30\3\2\2\2\u00d0\u00d1\7d\2\2\u00d1")
        buf.write("\u00d2\7q\2\2\u00d2\u00d3\7q\2\2\u00d3\u00d4\7n\2\2\u00d4")
        buf.write("\u00d5\7g\2\2\u00d5\u00d6\7c\2\2\u00d6\u00d7\7p\2\2\u00d7")
        buf.write("\32\3\2\2\2\u00d8\u00d9\7e\2\2\u00d9\u00da\7q\2\2\u00da")
        buf.write("\u00db\7p\2\2\u00db\u00dc\7u\2\2\u00dc\u00dd\7v\2\2\u00dd")
        buf.write("\34\3\2\2\2\u00de\u00df\7x\2\2\u00df\u00e0\7c\2\2\u00e0")
        buf.write("\u00e1\7t\2\2\u00e1\36\3\2\2\2\u00e2\u00e3\7e\2\2\u00e3")
        buf.write("\u00e4\7q\2\2\u00e4\u00e5\7p\2\2\u00e5\u00e6\7v\2\2\u00e6")
        buf.write("\u00e7\7k\2\2\u00e7\u00e8\7p\2\2\u00e8\u00e9\7w\2\2\u00e9")
        buf.write("\u00ea\7g\2\2\u00ea \3\2\2\2\u00eb\u00ec\7d\2\2\u00ec")
        buf.write("\u00ed\7t\2\2\u00ed\u00ee\7g\2\2\u00ee\u00ef\7c\2\2\u00ef")
        buf.write("\u00f0\7m\2\2\u00f0\"\3\2\2\2\u00f1\u00f2\7t\2\2\u00f2")
        buf.write("\u00f3\7c\2\2\u00f3\u00f4\7p\2\2\u00f4\u00f5\7i\2\2\u00f5")
        buf.write("\u00f6\7g\2\2\u00f6$\3\2\2\2\u00f7\u00f8\7p\2\2\u00f8")
        buf.write("\u00f9\7k\2\2\u00f9\u00fa\7n\2\2\u00fa&\3\2\2\2\u00fb")
        buf.write("\u00fc\7v\2\2\u00fc\u00fd\7t\2\2\u00fd\u00fe\7w\2\2\u00fe")
        buf.write("\u00ff\7g\2\2\u00ff(\3\2\2\2\u0100\u0101\7h\2\2\u0101")
        buf.write("\u0102\7c\2\2\u0102\u0103\7n\2\2\u0103\u0104\7u\2\2\u0104")
        buf.write("\u0105\7g\2\2\u0105*\3\2\2\2\u0106\u0107\7-\2\2\u0107")
        buf.write(",\3\2\2\2\u0108\u0109\7/\2\2\u0109.\3\2\2\2\u010a\u010b")
        buf.write("\7,\2\2\u010b\60\3\2\2\2\u010c\u010d\7\61\2\2\u010d\62")
        buf.write("\3\2\2\2\u010e\u010f\7\'\2\2\u010f\64\3\2\2\2\u0110\u0111")
        buf.write("\7?\2\2\u0111\u0112\7?\2\2\u0112\66\3\2\2\2\u0113\u0114")
        buf.write("\7#\2\2\u0114\u0115\7?\2\2\u01158\3\2\2\2\u0116\u0117")
        buf.write("\7>\2\2\u0117:\3\2\2\2\u0118\u0119\7>\2\2\u0119\u011a")
        buf.write("\7?\2\2\u011a<\3\2\2\2\u011b\u011c\7@\2\2\u011c>\3\2\2")
        buf.write("\2\u011d\u011e\7@\2\2\u011e\u011f\7?\2\2\u011f@\3\2\2")
        buf.write("\2\u0120\u0121\7~\2\2\u0121\u0122\7~\2\2\u0122B\3\2\2")
        buf.write("\2\u0123\u0124\7(\2\2\u0124\u0125\7(\2\2\u0125D\3\2\2")
        buf.write("\2\u0126\u0127\7#\2\2\u0127F\3\2\2\2\u0128\u0129\7<\2")
        buf.write("\2\u0129\u012a\7?\2\2\u012aH\3\2\2\2\u012b\u012c\7-\2")
        buf.write("\2\u012c\u012d\7?\2\2\u012dJ\3\2\2\2\u012e\u012f\7/\2")
        buf.write("\2\u012f\u0130\7?\2\2\u0130L\3\2\2\2\u0131\u0132\7,\2")
        buf.write("\2\u0132\u0133\7?\2\2\u0133N\3\2\2\2\u0134\u0135\7\61")
        buf.write("\2\2\u0135\u0136\7?\2\2\u0136P\3\2\2\2\u0137\u0138\7\'")
        buf.write("\2\2\u0138\u0139\7?\2\2\u0139R\3\2\2\2\u013a\u013b\7?")
        buf.write("\2\2\u013bT\3\2\2\2\u013c\u013d\7\60\2\2\u013dV\3\2\2")
        buf.write("\2\u013e\u013f\7*\2\2\u013fX\3\2\2\2\u0140\u0141\7+\2")
        buf.write("\2\u0141Z\3\2\2\2\u0142\u0143\7]\2\2\u0143\\\3\2\2\2\u0144")
        buf.write("\u0145\7_\2\2\u0145^\3\2\2\2\u0146\u0147\7}\2\2\u0147")
        buf.write("`\3\2\2\2\u0148\u0149\7\177\2\2\u0149b\3\2\2\2\u014a\u014b")
        buf.write("\7.\2\2\u014bd\3\2\2\2\u014c\u0153\7=\2\2\u014d\u014f")
        buf.write("\7\17\2\2\u014e\u014d\3\2\2\2\u014e\u014f\3\2\2\2\u014f")
        buf.write("\u0150\3\2\2\2\u0150\u0151\7\f\2\2\u0151\u0153\b\63\2")
        buf.write("\2\u0152\u014c\3\2\2\2\u0152\u014e\3\2\2\2\u0153f\3\2")
        buf.write("\2\2\u0154\u0155\7<\2\2\u0155h\3\2\2\2\u0156\u015a\t\2")
        buf.write("\2\2\u0157\u0159\t\3\2\2\u0158\u0157\3\2\2\2\u0159\u015c")
        buf.write("\3\2\2\2\u015a\u0158\3\2\2\2\u015a\u015b\3\2\2\2\u015b")
        buf.write("j\3\2\2\2\u015c\u015a\3\2\2\2\u015d\u0162\5m\67\2\u015e")
        buf.write("\u0162\5o8\2\u015f\u0162\5q9\2\u0160\u0162\5s:\2\u0161")
        buf.write("\u015d\3\2\2\2\u0161\u015e\3\2\2\2\u0161\u015f\3\2\2\2")
        buf.write("\u0161\u0160\3\2\2\2\u0162l\3\2\2\2\u0163\u016c\7\62\2")
        buf.write("\2\u0164\u0168\t\4\2\2\u0165\u0167\t\5\2\2\u0166\u0165")
        buf.write("\3\2\2\2\u0167\u016a\3\2\2\2\u0168\u0166\3\2\2\2\u0168")
        buf.write("\u0169\3\2\2\2\u0169\u016c\3\2\2\2\u016a\u0168\3\2\2\2")
        buf.write("\u016b\u0163\3\2\2\2\u016b\u0164\3\2\2\2\u016cn\3\2\2")
        buf.write("\2\u016d\u016e\7\62\2\2\u016e\u0170\t\6\2\2\u016f\u0171")
        buf.write("\t\7\2\2\u0170\u016f\3\2\2\2\u0171\u0172\3\2\2\2\u0172")
        buf.write("\u0170\3\2\2\2\u0172\u0173\3\2\2\2\u0173p\3\2\2\2\u0174")
        buf.write("\u0175\7\62\2\2\u0175\u0177\t\b\2\2\u0176\u0178\t\t\2")
        buf.write("\2\u0177\u0176\3\2\2\2\u0178\u0179\3\2\2\2\u0179\u0177")
        buf.write("\3\2\2\2\u0179\u017a\3\2\2\2\u017ar\3\2\2\2\u017b\u017c")
        buf.write("\7\62\2\2\u017c\u017e\t\n\2\2\u017d\u017f\t\13\2\2\u017e")
        buf.write("\u017d\3\2\2\2\u017f\u0180\3\2\2\2\u0180\u017e\3\2\2\2")
        buf.write("\u0180\u0181\3\2\2\2\u0181t\3\2\2\2\u0182\u0183\5w<\2")
        buf.write("\u0183\u0185\7\60\2\2\u0184\u0186\5w<\2\u0185\u0184\3")
        buf.write("\2\2\2\u0185\u0186\3\2\2\2\u0186\u0188\3\2\2\2\u0187\u0189")
        buf.write("\5y=\2\u0188\u0187\3\2\2\2\u0188\u0189\3\2\2\2\u0189v")
        buf.write("\3\2\2\2\u018a\u018c\t\5\2\2\u018b\u018a\3\2\2\2\u018c")
        buf.write("\u018d\3\2\2\2\u018d\u018b\3\2\2\2\u018d\u018e\3\2\2\2")
        buf.write("\u018ex\3\2\2\2\u018f\u0191\t\f\2\2\u0190\u0192\t\r\2")
        buf.write("\2\u0191\u0190\3\2\2\2\u0191\u0192\3\2\2\2\u0192\u0193")
        buf.write("\3\2\2\2\u0193\u0194\5w<\2\u0194z\3\2\2\2\u0195\u0199")
        buf.write("\7$\2\2\u0196\u0198\5\177@\2\u0197\u0196\3\2\2\2\u0198")
        buf.write("\u019b\3\2\2\2\u0199\u0197\3\2\2\2\u0199\u019a\3\2\2\2")
        buf.write("\u019a\u019c\3\2\2\2\u019b\u0199\3\2\2\2\u019c\u019d\7")
        buf.write("$\2\2\u019d|\3\2\2\2\u019e\u019f\7^\2\2\u019f\u01a0\t")
        buf.write("\16\2\2\u01a0~\3\2\2\2\u01a1\u01a4\n\17\2\2\u01a2\u01a4")
        buf.write("\5\u0081A\2\u01a3\u01a1\3\2\2\2\u01a3\u01a2\3\2\2\2\u01a4")
        buf.write("\u0080\3\2\2\2\u01a5\u01a6\7^\2\2\u01a6\u01a7\t\16\2\2")
        buf.write("\u01a7\u0082\3\2\2\2\u01a8\u01ac\t\20\2\2\u01a9\u01aa")
        buf.write("\7^\2\2\u01aa\u01ac\n\21\2\2\u01ab\u01a8\3\2\2\2\u01ab")
        buf.write("\u01a9\3\2\2\2\u01ac\u0084\3\2\2\2\u01ad\u01af\t\22\2")
        buf.write("\2\u01ae\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0\u01ae")
        buf.write("\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2")
        buf.write("\u01b3\bC\3\2\u01b3\u0086\3\2\2\2\u01b4\u01b5\7\61\2\2")
        buf.write("\u01b5\u01b6\7,\2\2\u01b6\u01bb\3\2\2\2\u01b7\u01ba\5")
        buf.write("\u0087D\2\u01b8\u01ba\13\2\2\2\u01b9\u01b7\3\2\2\2\u01b9")
        buf.write("\u01b8\3\2\2\2\u01ba\u01bd\3\2\2\2\u01bb\u01bc\3\2\2\2")
        buf.write("\u01bb\u01b9\3\2\2\2\u01bc\u01be\3\2\2\2\u01bd\u01bb\3")
        buf.write("\2\2\2\u01be\u01bf\7,\2\2\u01bf\u01c0\7\61\2\2\u01c0\u01c1")
        buf.write("\3\2\2\2\u01c1\u01c2\bD\3\2\u01c2\u0088\3\2\2\2\u01c3")
        buf.write("\u01c4\7\61\2\2\u01c4\u01c5\7\61\2\2\u01c5\u01c9\3\2\2")
        buf.write("\2\u01c6\u01c8\n\23\2\2\u01c7\u01c6\3\2\2\2\u01c8\u01cb")
        buf.write("\3\2\2\2\u01c9\u01c7\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca")
        buf.write("\u01cc\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cc\u01cd\bE\3\2")
        buf.write("\u01cd\u008a\3\2\2\2\u01ce\u01cf\13\2\2\2\u01cf\u01d0")
        buf.write("\bF\4\2\u01d0\u008c\3\2\2\2\u01d1\u01d5\7$\2\2\u01d2\u01d4")
        buf.write("\5\177@\2\u01d3\u01d2\3\2\2\2\u01d4\u01d7\3\2\2\2\u01d5")
        buf.write("\u01d3\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01db\3\2\2\2")
        buf.write("\u01d7\u01d5\3\2\2\2\u01d8\u01d9\7\17\2\2\u01d9\u01dc")
        buf.write("\7\f\2\2\u01da\u01dc\t\24\2\2\u01db\u01d8\3\2\2\2\u01db")
        buf.write("\u01da\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd\u01de\bG\5\2")
        buf.write("\u01de\u008e\3\2\2\2\u01df\u01e3\7$\2\2\u01e0\u01e2\5")
        buf.write("\177@\2\u01e1\u01e0\3\2\2\2\u01e2\u01e5\3\2\2\2\u01e3")
        buf.write("\u01e1\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4\u01e6\3\2\2\2")
        buf.write("\u01e5\u01e3\3\2\2\2\u01e6\u01e7\5\u0083B\2\u01e7\u01e8")
        buf.write("\bH\6\2\u01e8\u0090\3\2\2\2\32\2\u014e\u0152\u015a\u0161")
        buf.write("\u0168\u016b\u0172\u0179\u0180\u0185\u0188\u018d\u0191")
        buf.write("\u0199\u01a3\u01ab\u01b0\u01b9\u01bb\u01c9\u01d5\u01db")
        buf.write("\u01e3\7\3\63\2\b\2\2\3F\3\3G\4\3H\5")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IF = 1
    ELSE = 2
    FOR = 3
    RETURN = 4
    FUNC = 5
    TYPE = 6
    STRUCT = 7
    INTERFACE = 8
    STRING = 9
    INT = 10
    FLOAT = 11
    BOOLEAN = 12
    CONST = 13
    VAR = 14
    CONTINUE = 15
    BREAK = 16
    RANGE = 17
    NIL = 18
    TRUE = 19
    FALSE = 20
    ADD = 21
    SUB = 22
    MUL = 23
    DIV = 24
    MOD = 25
    EQUAL = 26
    NOT_EQUAL = 27
    LESS = 28
    LESS_EQUAL = 29
    GREATER = 30
    GREATER_EQUAL = 31
    OR = 32
    AND = 33
    NOT = 34
    SHORT_DECL = 35
    ADD_ASSIGN = 36
    SUB_ASSIGN = 37
    MUL_ASSIGN = 38
    DIV_ASSIGN = 39
    MOD_ASSIGN = 40
    ASSIGN = 41
    DOT = 42
    LPAREN = 43
    RPAREN = 44
    LBRACKET = 45
    RBRACKET = 46
    LBRACE = 47
    RBRACE = 48
    COMA = 49
    SEMI = 50
    COLON = 51
    ID = 52
    INT_LIT = 53
    FLOAT_LIT = 54
    STRING_LIT = 55
    WS = 56
    COMMENT = 57
    LINE_COMMENT = 58
    ERROR_CHAR = 59
    UNCLOSE_STRING = 60
    ILLEGAL_ESCAPE = 61

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", "'struct'", 
            "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'nil'", 
            "'true'", "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'||'", "'&&'", "'!'", 
            "':='", "'+='", "'-='", "'*='", "'/='", "'%='", "'='", "'.'", 
            "'('", "')'", "'['", "']'", "'{'", "'}'", "','", "':'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
            "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
            "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "ADD", "SUB", "MUL", 
            "DIV", "MOD", "EQUAL", "NOT_EQUAL", "LESS", "LESS_EQUAL", "GREATER", 
            "GREATER_EQUAL", "OR", "AND", "NOT", "SHORT_DECL", "ADD_ASSIGN", 
            "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "ASSIGN", 
            "DOT", "LPAREN", "RPAREN", "LBRACKET", "RBRACKET", "LBRACE", 
            "RBRACE", "COMA", "SEMI", "COLON", "ID", "INT_LIT", "FLOAT_LIT", 
            "STRING_LIT", "WS", "COMMENT", "LINE_COMMENT", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
                  "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", 
                  "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", "FALSE", 
                  "ADD", "SUB", "MUL", "DIV", "MOD", "EQUAL", "NOT_EQUAL", 
                  "LESS", "LESS_EQUAL", "GREATER", "GREATER_EQUAL", "OR", 
                  "AND", "NOT", "SHORT_DECL", "ADD_ASSIGN", "SUB_ASSIGN", 
                  "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "ASSIGN", "DOT", 
                  "LPAREN", "RPAREN", "LBRACKET", "RBRACKET", "LBRACE", 
                  "RBRACE", "COMA", "SEMI", "COLON", "ID", "INT_LIT", "DEC_LIT", 
                  "BIN_LIT", "OCT_LIT", "HEX_LIT", "FLOAT_LIT", "DEC_PART", 
                  "EXP_PART", "STRING_LIT", "ESCAPED_VALUE", "STR_CHAR", 
                  "ESC_SEQ", "ESC_ILLEGAL", "WS", "COMMENT", "LINE_COMMENT", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None
        self.preType = None

    def emit(self):
        tk = self.type
        self.preType = tk;
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[49] = self.SEMI_action 
            actions[68] = self.ERROR_CHAR_action 
            actions[69] = self.UNCLOSE_STRING_action 
            actions[70] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def SEMI_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                if self.preType in {
                    self.RPAREN, self.RBRACE, self.RBRACKET, 
                    self.INT_LIT, 
                    self.FLOAT_LIT, self.STRING_LIT, self.TRUE, 
                    self.FALSE, self.ID, self.BREAK, 
                    self.CONTINUE, self.RETURN, self.NIL
                }:
                    self.text = ';'
                else:
                    self.skip()

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
                    raise UncloseString(self.text[:-2])
                elif (self.text[-1] == '\n'):
                    raise UncloseString(self.text[:-1])
                else:
                    raise UncloseString(self.text)

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                raise IllegalEscape(self.text)

     


