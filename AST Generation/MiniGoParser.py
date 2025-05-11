# Generated from main/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3?")
        buf.write("\u0287\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u0081\n")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\5\4\u0089\n\4\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u0099\n")
        buf.write("\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\5\n\u00a6")
        buf.write("\n\n\3\13\3\13\5\13\u00aa\n\13\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\5\f\u00b3\n\f\3\r\5\r\u00b6\n\r\3\r\3\r\5\r\u00ba")
        buf.write("\n\r\3\16\3\16\3\16\5\16\u00bf\n\16\3\16\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\5\17\u00ca\n\17\3\20\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\5\20\u00d3\n\20\5\20\u00d5\n\20")
        buf.write("\3\20\3\20\3\20\7\20\u00da\n\20\f\20\16\20\u00dd\13\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u00e6\n\21\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\5\22\u00ee\n\22\3\22\3\22")
        buf.write("\3\22\3\22\7\22\u00f4\n\22\f\22\16\22\u00f7\13\22\3\23")
        buf.write("\3\23\5\23\u00fb\n\23\3\24\3\24\3\24\3\24\5\24\u0101\n")
        buf.write("\24\3\24\3\24\5\24\u0105\n\24\3\24\3\24\5\24\u0109\n\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25")
        buf.write("\u0115\n\25\3\25\3\25\5\25\u0119\n\25\3\25\5\25\u011c")
        buf.write("\n\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\5\26\u0125\n")
        buf.write("\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\5\27\u0132\n\27\3\30\3\30\3\30\3\30\3\30\3\30\3")
        buf.write("\30\3\31\3\31\3\31\5\31\u013e\n\31\3\31\3\31\5\31\u0142")
        buf.write("\n\31\3\31\3\31\3\31\3\31\3\31\5\31\u0149\n\31\3\31\3")
        buf.write("\31\5\31\u014d\n\31\3\31\5\31\u0150\n\31\3\32\3\32\5\32")
        buf.write("\u0154\n\32\3\32\3\32\3\32\3\32\5\32\u015a\n\32\3\33\3")
        buf.write("\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\5\34\u016a\n\34\3\35\3\35\3\35\3\36\3\36\3")
        buf.write("\36\3\36\3\36\5\36\u0174\n\36\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\7\37\u017c\n\37\f\37\16\37\u017f\13\37\3 \3 \3 ")
        buf.write("\3 \3 \3 \7 \u0187\n \f \16 \u018a\13 \3!\3!\3!\3!\3!")
        buf.write("\3!\7!\u0192\n!\f!\16!\u0195\13!\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\7\"\u019d\n\"\f\"\16\"\u01a0\13\"\3#\3#\3#\3#\3#\3")
        buf.write("#\7#\u01a8\n#\f#\16#\u01ab\13#\3$\3$\3$\5$\u01b0\n$\3")
        buf.write("%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\5%\u01bd\n%\3%\3%\3%\3")
        buf.write("%\3%\3%\7%\u01c5\n%\f%\16%\u01c8\13%\3&\3&\3&\3&\3&\3")
        buf.write("&\3&\5&\u01d1\n&\3\'\3\'\3\'\5\'\u01d6\n\'\3\'\3\'\3(")
        buf.write("\3(\3(\3(\3(\3(\3(\5(\u01e1\n(\3)\3)\3)\3)\3)\3)\5)\u01e9")
        buf.write("\n)\3*\3*\3*\5*\u01ee\n*\3+\3+\3+\3+\3+\3+\3+\5+\u01f7")
        buf.write("\n+\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\7,\u0204\n,\f,\16")
        buf.write(",\u0207\13,\3-\3-\3.\3.\3.\3.\3/\3/\3/\3/\3/\3/\3/\5/")
        buf.write("\u0216\n/\3/\3/\3\60\3\60\3\60\3\60\5\60\u021e\n\60\3")
        buf.write("\61\3\61\3\61\3\61\3\61\3\61\5\61\u0226\n\61\3\61\3\61")
        buf.write("\5\61\u022a\n\61\3\61\3\61\3\61\5\61\u022f\n\61\3\61\5")
        buf.write("\61\u0232\n\61\3\62\3\62\3\62\3\62\5\62\u0238\n\62\3\63")
        buf.write("\3\63\3\63\5\63\u023d\n\63\3\63\3\63\3\64\3\64\3\64\3")
        buf.write("\64\3\65\3\65\3\65\3\65\3\65\3\65\5\65\u024b\n\65\3\65")
        buf.write("\3\65\5\65\u024f\n\65\3\65\3\65\3\65\3\65\3\65\3\65\5")
        buf.write("\65\u0257\n\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\5\66\u0264\n\66\3\66\3\66\5\66\u0268\n")
        buf.write("\66\3\66\3\66\3\67\3\67\38\38\39\39\39\39\39\39\39\39")
        buf.write("\39\39\79\u027a\n9\f9\169\u027d\139\3:\3:\5:\u0281\n:")
        buf.write("\3;\3;\5;\u0285\n;\3;\2\f\36\"<>@BDHVp<\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF")
        buf.write("HJLNPRTVXZ\\^`bdfhjlnprt\2\f\3\2\13\16\3\2\678\3\2\25")
        buf.write("\26\3\2\66\67\3\2\34!\3\2\27\30\3\2\31\33\4\2\30\30$$")
        buf.write("\3\2%*\3\2%)\2\u02a3\2v\3\2\2\2\4\u0080\3\2\2\2\6\u0088")
        buf.write("\3\2\2\2\b\u008a\3\2\2\2\n\u008f\3\2\2\2\f\u009a\3\2\2")
        buf.write("\2\16\u009c\3\2\2\2\20\u009e\3\2\2\2\22\u00a5\3\2\2\2")
        buf.write("\24\u00a9\3\2\2\2\26\u00b2\3\2\2\2\30\u00b5\3\2\2\2\32")
        buf.write("\u00bb\3\2\2\2\34\u00c9\3\2\2\2\36\u00d4\3\2\2\2 \u00e5")
        buf.write("\3\2\2\2\"\u00ed\3\2\2\2$\u00fa\3\2\2\2&\u00fc\3\2\2\2")
        buf.write("(\u010c\3\2\2\2*\u0121\3\2\2\2,\u0131\3\2\2\2.\u0133\3")
        buf.write("\2\2\2\60\u014f\3\2\2\2\62\u0159\3\2\2\2\64\u015b\3\2")
        buf.write("\2\2\66\u0169\3\2\2\28\u016b\3\2\2\2:\u0173\3\2\2\2<\u0175")
        buf.write("\3\2\2\2>\u0180\3\2\2\2@\u018b\3\2\2\2B\u0196\3\2\2\2")
        buf.write("D\u01a1\3\2\2\2F\u01af\3\2\2\2H\u01b1\3\2\2\2J\u01d0\3")
        buf.write("\2\2\2L\u01d2\3\2\2\2N\u01e0\3\2\2\2P\u01e8\3\2\2\2R\u01ed")
        buf.write("\3\2\2\2T\u01f6\3\2\2\2V\u01f8\3\2\2\2X\u0208\3\2\2\2")
        buf.write("Z\u020a\3\2\2\2\\\u020e\3\2\2\2^\u021d\3\2\2\2`\u021f")
        buf.write("\3\2\2\2b\u0233\3\2\2\2d\u0239\3\2\2\2f\u0240\3\2\2\2")
        buf.write("h\u024e\3\2\2\2j\u025a\3\2\2\2l\u026b\3\2\2\2n\u026d\3")
        buf.write("\2\2\2p\u026f\3\2\2\2r\u0280\3\2\2\2t\u0282\3\2\2\2vw")
        buf.write("\5\4\3\2wx\7\2\2\3x\3\3\2\2\2yz\5\6\4\2z{\7\64\2\2{|\5")
        buf.write("\4\3\2|\u0081\3\2\2\2}~\5\6\4\2~\177\7\64\2\2\177\u0081")
        buf.write("\3\2\2\2\u0080y\3\2\2\2\u0080}\3\2\2\2\u0081\5\3\2\2\2")
        buf.write("\u0082\u0089\5\n\6\2\u0083\u0089\5\b\5\2\u0084\u0089\5")
        buf.write("&\24\2\u0085\u0089\5\64\33\2\u0086\u0089\5.\30\2\u0087")
        buf.write("\u0089\5(\25\2\u0088\u0082\3\2\2\2\u0088\u0083\3\2\2\2")
        buf.write("\u0088\u0084\3\2\2\2\u0088\u0085\3\2\2\2\u0088\u0086\3")
        buf.write("\2\2\2\u0088\u0087\3\2\2\2\u0089\7\3\2\2\2\u008a\u008b")
        buf.write("\7\17\2\2\u008b\u008c\7\66\2\2\u008c\u008d\7+\2\2\u008d")
        buf.write("\u008e\5<\37\2\u008e\t\3\2\2\2\u008f\u0090\7\20\2\2\u0090")
        buf.write("\u0098\7\66\2\2\u0091\u0099\5\30\r\2\u0092\u0093\7+\2")
        buf.write("\2\u0093\u0099\5<\37\2\u0094\u0095\5\30\r\2\u0095\u0096")
        buf.write("\7+\2\2\u0096\u0097\5<\37\2\u0097\u0099\3\2\2\2\u0098")
        buf.write("\u0091\3\2\2\2\u0098\u0092\3\2\2\2\u0098\u0094\3\2\2\2")
        buf.write("\u0099\13\3\2\2\2\u009a\u009b\t\2\2\2\u009b\r\3\2\2\2")
        buf.write("\u009c\u009d\t\3\2\2\u009d\17\3\2\2\2\u009e\u009f\t\4")
        buf.write("\2\2\u009f\21\3\2\2\2\u00a0\u00a6\7\24\2\2\u00a1\u00a6")
        buf.write("\5*\26\2\u00a2\u00a6\5\16\b\2\u00a3\u00a6\5\20\t\2\u00a4")
        buf.write("\u00a6\79\2\2\u00a5\u00a0\3\2\2\2\u00a5\u00a1\3\2\2\2")
        buf.write("\u00a5\u00a2\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a5\u00a4\3")
        buf.write("\2\2\2\u00a6\23\3\2\2\2\u00a7\u00aa\5\22\n\2\u00a8\u00aa")
        buf.write("\5\32\16\2\u00a9\u00a7\3\2\2\2\u00a9\u00a8\3\2\2\2\u00aa")
        buf.write("\25\3\2\2\2\u00ab\u00ac\7/\2\2\u00ac\u00ad\t\5\2\2\u00ad")
        buf.write("\u00ae\7\60\2\2\u00ae\u00b3\5\26\f\2\u00af\u00b0\7/\2")
        buf.write("\2\u00b0\u00b1\t\5\2\2\u00b1\u00b3\7\60\2\2\u00b2\u00ab")
        buf.write("\3\2\2\2\u00b2\u00af\3\2\2\2\u00b3\27\3\2\2\2\u00b4\u00b6")
        buf.write("\5\26\f\2\u00b5\u00b4\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6")
        buf.write("\u00b9\3\2\2\2\u00b7\u00ba\7\66\2\2\u00b8\u00ba\5\f\7")
        buf.write("\2\u00b9\u00b7\3\2\2\2\u00b9\u00b8\3\2\2\2\u00ba\31\3")
        buf.write("\2\2\2\u00bb\u00be\5\26\f\2\u00bc\u00bf\7\66\2\2\u00bd")
        buf.write("\u00bf\5\f\7\2\u00be\u00bc\3\2\2\2\u00be\u00bd\3\2\2\2")
        buf.write("\u00bf\u00c0\3\2\2\2\u00c0\u00c1\7\61\2\2\u00c1\u00c2")
        buf.write("\5\34\17\2\u00c2\u00c3\7\62\2\2\u00c3\33\3\2\2\2\u00c4")
        buf.write("\u00c5\5\36\20\2\u00c5\u00c6\7\63\2\2\u00c6\u00c7\5\36")
        buf.write("\20\2\u00c7\u00ca\3\2\2\2\u00c8\u00ca\5\36\20\2\u00c9")
        buf.write("\u00c4\3\2\2\2\u00c9\u00c8\3\2\2\2\u00ca\35\3\2\2\2\u00cb")
        buf.write("\u00cc\b\20\1\2\u00cc\u00cd\7\61\2\2\u00cd\u00ce\5\36")
        buf.write("\20\2\u00ce\u00cf\7\62\2\2\u00cf\u00d5\3\2\2\2\u00d0\u00d3")
        buf.write("\5\22\n\2\u00d1\u00d3\7\66\2\2\u00d2\u00d0\3\2\2\2\u00d2")
        buf.write("\u00d1\3\2\2\2\u00d3\u00d5\3\2\2\2\u00d4\u00cb\3\2\2\2")
        buf.write("\u00d4\u00d2\3\2\2\2\u00d5\u00db\3\2\2\2\u00d6\u00d7\f")
        buf.write("\4\2\2\u00d7\u00d8\7\63\2\2\u00d8\u00da\5\36\20\5\u00d9")
        buf.write("\u00d6\3\2\2\2\u00da\u00dd\3\2\2\2\u00db\u00d9\3\2\2\2")
        buf.write("\u00db\u00dc\3\2\2\2\u00dc\37\3\2\2\2\u00dd\u00db\3\2")
        buf.write("\2\2\u00de\u00df\7\66\2\2\u00df\u00e0\5\"\22\2\u00e0\u00e1")
        buf.write("\7\63\2\2\u00e1\u00e2\5 \21\2\u00e2\u00e6\3\2\2\2\u00e3")
        buf.write("\u00e4\7\66\2\2\u00e4\u00e6\5\"\22\2\u00e5\u00de\3\2\2")
        buf.write("\2\u00e5\u00e3\3\2\2\2\u00e6!\3\2\2\2\u00e7\u00e8\b\22")
        buf.write("\1\2\u00e8\u00e9\7/\2\2\u00e9\u00ea\t\5\2\2\u00ea\u00eb")
        buf.write("\7\60\2\2\u00eb\u00ee\5\"\22\4\u00ec\u00ee\5$\23\2\u00ed")
        buf.write("\u00e7\3\2\2\2\u00ed\u00ec\3\2\2\2\u00ee\u00f5\3\2\2\2")
        buf.write("\u00ef\u00f0\f\5\2\2\u00f0\u00f1\7/\2\2\u00f1\u00f2\t")
        buf.write("\5\2\2\u00f2\u00f4\7\60\2\2\u00f3\u00ef\3\2\2\2\u00f4")
        buf.write("\u00f7\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f5\u00f6\3\2\2\2")
        buf.write("\u00f6#\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f8\u00fb\5\f\7")
        buf.write("\2\u00f9\u00fb\7\66\2\2\u00fa\u00f8\3\2\2\2\u00fa\u00f9")
        buf.write("\3\2\2\2\u00fb%\3\2\2\2\u00fc\u00fd\7\7\2\2\u00fd\u00fe")
        buf.write("\7\66\2\2\u00fe\u0100\7-\2\2\u00ff\u0101\5\62\32\2\u0100")
        buf.write("\u00ff\3\2\2\2\u0100\u0101\3\2\2\2\u0101\u0102\3\2\2\2")
        buf.write("\u0102\u0104\7.\2\2\u0103\u0105\5\30\r\2\u0104\u0103\3")
        buf.write("\2\2\2\u0104\u0105\3\2\2\2\u0105\u0106\3\2\2\2\u0106\u0108")
        buf.write("\7\61\2\2\u0107\u0109\5T+\2\u0108\u0107\3\2\2\2\u0108")
        buf.write("\u0109\3\2\2\2\u0109\u010a\3\2\2\2\u010a\u010b\7\62\2")
        buf.write("\2\u010b\'\3\2\2\2\u010c\u010d\7\7\2\2\u010d\u010e\7-")
        buf.write("\2\2\u010e\u010f\7\66\2\2\u010f\u0110\7\66\2\2\u0110\u0111")
        buf.write("\7.\2\2\u0111\u0112\7\66\2\2\u0112\u0114\7-\2\2\u0113")
        buf.write("\u0115\5\62\32\2\u0114\u0113\3\2\2\2\u0114\u0115\3\2\2")
        buf.write("\2\u0115\u0116\3\2\2\2\u0116\u0118\7.\2\2\u0117\u0119")
        buf.write("\5<\37\2\u0118\u0117\3\2\2\2\u0118\u0119\3\2\2\2\u0119")
        buf.write("\u011b\3\2\2\2\u011a\u011c\5\30\r\2\u011b\u011a\3\2\2")
        buf.write("\2\u011b\u011c\3\2\2\2\u011c\u011d\3\2\2\2\u011d\u011e")
        buf.write("\7\61\2\2\u011e\u011f\5T+\2\u011f\u0120\7\62\2\2\u0120")
        buf.write(")\3\2\2\2\u0121\u0122\7\66\2\2\u0122\u0124\7\61\2\2\u0123")
        buf.write("\u0125\5,\27\2\u0124\u0123\3\2\2\2\u0124\u0125\3\2\2\2")
        buf.write("\u0125\u0126\3\2\2\2\u0126\u0127\7\62\2\2\u0127+\3\2\2")
        buf.write("\2\u0128\u0129\7\66\2\2\u0129\u012a\7\65\2\2\u012a\u012b")
        buf.write("\5<\37\2\u012b\u012c\7\63\2\2\u012c\u012d\5,\27\2\u012d")
        buf.write("\u0132\3\2\2\2\u012e\u012f\7\66\2\2\u012f\u0130\7\65\2")
        buf.write("\2\u0130\u0132\5<\37\2\u0131\u0128\3\2\2\2\u0131\u012e")
        buf.write("\3\2\2\2\u0132-\3\2\2\2\u0133\u0134\7\b\2\2\u0134\u0135")
        buf.write("\7\66\2\2\u0135\u0136\7\n\2\2\u0136\u0137\7\61\2\2\u0137")
        buf.write("\u0138\5\60\31\2\u0138\u0139\7\62\2\2\u0139/\3\2\2\2\u013a")
        buf.write("\u013b\7\66\2\2\u013b\u013d\7-\2\2\u013c\u013e\5\62\32")
        buf.write("\2\u013d\u013c\3\2\2\2\u013d\u013e\3\2\2\2\u013e\u013f")
        buf.write("\3\2\2\2\u013f\u0141\7.\2\2\u0140\u0142\5\30\r\2\u0141")
        buf.write("\u0140\3\2\2\2\u0141\u0142\3\2\2\2\u0142\u0143\3\2\2\2")
        buf.write("\u0143\u0144\7\64\2\2\u0144\u0150\5\60\31\2\u0145\u0146")
        buf.write("\7\66\2\2\u0146\u0148\7-\2\2\u0147\u0149\5\62\32\2\u0148")
        buf.write("\u0147\3\2\2\2\u0148\u0149\3\2\2\2\u0149\u014a\3\2\2\2")
        buf.write("\u014a\u014c\7.\2\2\u014b\u014d\5\30\r\2\u014c\u014b\3")
        buf.write("\2\2\2\u014c\u014d\3\2\2\2\u014d\u014e\3\2\2\2\u014e\u0150")
        buf.write("\7\64\2\2\u014f\u013a\3\2\2\2\u014f\u0145\3\2\2\2\u0150")
        buf.write("\61\3\2\2\2\u0151\u0153\7\66\2\2\u0152\u0154\5\30\r\2")
        buf.write("\u0153\u0152\3\2\2\2\u0153\u0154\3\2\2\2\u0154\u0155\3")
        buf.write("\2\2\2\u0155\u0156\7\63\2\2\u0156\u015a\5\62\32\2\u0157")
        buf.write("\u0158\7\66\2\2\u0158\u015a\5\30\r\2\u0159\u0151\3\2\2")
        buf.write("\2\u0159\u0157\3\2\2\2\u015a\63\3\2\2\2\u015b\u015c\7")
        buf.write("\b\2\2\u015c\u015d\7\66\2\2\u015d\u015e\7\t\2\2\u015e")
        buf.write("\u015f\7\61\2\2\u015f\u0160\5\66\34\2\u0160\u0161\7\62")
        buf.write("\2\2\u0161\65\3\2\2\2\u0162\u0163\58\35\2\u0163\u0164")
        buf.write("\7\64\2\2\u0164\u0165\5\66\34\2\u0165\u016a\3\2\2\2\u0166")
        buf.write("\u0167\58\35\2\u0167\u0168\7\64\2\2\u0168\u016a\3\2\2")
        buf.write("\2\u0169\u0162\3\2\2\2\u0169\u0166\3\2\2\2\u016a\67\3")
        buf.write("\2\2\2\u016b\u016c\7\66\2\2\u016c\u016d\5\30\r\2\u016d")
        buf.write("9\3\2\2\2\u016e\u016f\5<\37\2\u016f\u0170\7\63\2\2\u0170")
        buf.write("\u0171\5:\36\2\u0171\u0174\3\2\2\2\u0172\u0174\5<\37\2")
        buf.write("\u0173\u016e\3\2\2\2\u0173\u0172\3\2\2\2\u0174;\3\2\2")
        buf.write("\2\u0175\u0176\b\37\1\2\u0176\u0177\5> \2\u0177\u017d")
        buf.write("\3\2\2\2\u0178\u0179\f\4\2\2\u0179\u017a\7\"\2\2\u017a")
        buf.write("\u017c\5> \2\u017b\u0178\3\2\2\2\u017c\u017f\3\2\2\2\u017d")
        buf.write("\u017b\3\2\2\2\u017d\u017e\3\2\2\2\u017e=\3\2\2\2\u017f")
        buf.write("\u017d\3\2\2\2\u0180\u0181\b \1\2\u0181\u0182\5@!\2\u0182")
        buf.write("\u0188\3\2\2\2\u0183\u0184\f\4\2\2\u0184\u0185\7#\2\2")
        buf.write("\u0185\u0187\5@!\2\u0186\u0183\3\2\2\2\u0187\u018a\3\2")
        buf.write("\2\2\u0188\u0186\3\2\2\2\u0188\u0189\3\2\2\2\u0189?\3")
        buf.write("\2\2\2\u018a\u0188\3\2\2\2\u018b\u018c\b!\1\2\u018c\u018d")
        buf.write("\5B\"\2\u018d\u0193\3\2\2\2\u018e\u018f\f\4\2\2\u018f")
        buf.write("\u0190\t\6\2\2\u0190\u0192\5B\"\2\u0191\u018e\3\2\2\2")
        buf.write("\u0192\u0195\3\2\2\2\u0193\u0191\3\2\2\2\u0193\u0194\3")
        buf.write("\2\2\2\u0194A\3\2\2\2\u0195\u0193\3\2\2\2\u0196\u0197")
        buf.write("\b\"\1\2\u0197\u0198\5D#\2\u0198\u019e\3\2\2\2\u0199\u019a")
        buf.write("\f\4\2\2\u019a\u019b\t\7\2\2\u019b\u019d\5D#\2\u019c\u0199")
        buf.write("\3\2\2\2\u019d\u01a0\3\2\2\2\u019e\u019c\3\2\2\2\u019e")
        buf.write("\u019f\3\2\2\2\u019fC\3\2\2\2\u01a0\u019e\3\2\2\2\u01a1")
        buf.write("\u01a2\b#\1\2\u01a2\u01a3\5F$\2\u01a3\u01a9\3\2\2\2\u01a4")
        buf.write("\u01a5\f\4\2\2\u01a5\u01a6\t\b\2\2\u01a6\u01a8\5F$\2\u01a7")
        buf.write("\u01a4\3\2\2\2\u01a8\u01ab\3\2\2\2\u01a9\u01a7\3\2\2\2")
        buf.write("\u01a9\u01aa\3\2\2\2\u01aaE\3\2\2\2\u01ab\u01a9\3\2\2")
        buf.write("\2\u01ac\u01ad\t\t\2\2\u01ad\u01b0\5F$\2\u01ae\u01b0\5")
        buf.write("H%\2\u01af\u01ac\3\2\2\2\u01af\u01ae\3\2\2\2\u01b0G\3")
        buf.write("\2\2\2\u01b1\u01b2\b%\1\2\u01b2\u01b3\5J&\2\u01b3\u01c6")
        buf.write("\3\2\2\2\u01b4\u01b5\f\6\2\2\u01b5\u01b6\7,\2\2\u01b6")
        buf.write("\u01c5\7\66\2\2\u01b7\u01b8\f\5\2\2\u01b8\u01b9\7,\2\2")
        buf.write("\u01b9\u01ba\7\66\2\2\u01ba\u01bc\7-\2\2\u01bb\u01bd\5")
        buf.write(":\36\2\u01bc\u01bb\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd\u01be")
        buf.write("\3\2\2\2\u01be\u01c5\7.\2\2\u01bf\u01c0\f\4\2\2\u01c0")
        buf.write("\u01c1\7/\2\2\u01c1\u01c2\5<\37\2\u01c2\u01c3\7\60\2\2")
        buf.write("\u01c3\u01c5\3\2\2\2\u01c4\u01b4\3\2\2\2\u01c4\u01b7\3")
        buf.write("\2\2\2\u01c4\u01bf\3\2\2\2\u01c5\u01c8\3\2\2\2\u01c6\u01c4")
        buf.write("\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7I\3\2\2\2\u01c8\u01c6")
        buf.write("\3\2\2\2\u01c9\u01d1\7\66\2\2\u01ca\u01d1\5\24\13\2\u01cb")
        buf.write("\u01d1\5L\'\2\u01cc\u01cd\7-\2\2\u01cd\u01ce\5<\37\2\u01ce")
        buf.write("\u01cf\7.\2\2\u01cf\u01d1\3\2\2\2\u01d0\u01c9\3\2\2\2")
        buf.write("\u01d0\u01ca\3\2\2\2\u01d0\u01cb\3\2\2\2\u01d0\u01cc\3")
        buf.write("\2\2\2\u01d1K\3\2\2\2\u01d2\u01d3\7\66\2\2\u01d3\u01d5")
        buf.write("\7-\2\2\u01d4\u01d6\5:\36\2\u01d5\u01d4\3\2\2\2\u01d5")
        buf.write("\u01d6\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7\u01d8\7.\2\2")
        buf.write("\u01d8M\3\2\2\2\u01d9\u01da\5P)\2\u01da\u01db\7\64\2\2")
        buf.write("\u01db\u01dc\5N(\2\u01dc\u01e1\3\2\2\2\u01dd\u01de\5P")
        buf.write(")\2\u01de\u01df\7\64\2\2\u01df\u01e1\3\2\2\2\u01e0\u01d9")
        buf.write("\3\2\2\2\u01e0\u01dd\3\2\2\2\u01e1O\3\2\2\2\u01e2\u01e9")
        buf.write("\5\6\4\2\u01e3\u01e9\5Z.\2\u01e4\u01e9\5`\61\2\u01e5\u01e9")
        buf.write("\5b\62\2\u01e6\u01e9\5p9\2\u01e7\u01e9\5t;\2\u01e8\u01e2")
        buf.write("\3\2\2\2\u01e8\u01e3\3\2\2\2\u01e8\u01e4\3\2\2\2\u01e8")
        buf.write("\u01e5\3\2\2\2\u01e8\u01e6\3\2\2\2\u01e8\u01e7\3\2\2\2")
        buf.write("\u01e9Q\3\2\2\2\u01ea\u01ee\5P)\2\u01eb\u01ee\5l\67\2")
        buf.write("\u01ec\u01ee\5n8\2\u01ed\u01ea\3\2\2\2\u01ed\u01eb\3\2")
        buf.write("\2\2\u01ed\u01ec\3\2\2\2\u01eeS\3\2\2\2\u01ef\u01f0\5")
        buf.write("R*\2\u01f0\u01f1\7\64\2\2\u01f1\u01f2\5T+\2\u01f2\u01f7")
        buf.write("\3\2\2\2\u01f3\u01f4\5R*\2\u01f4\u01f5\7\64\2\2\u01f5")
        buf.write("\u01f7\3\2\2\2\u01f6\u01ef\3\2\2\2\u01f6\u01f3\3\2\2\2")
        buf.write("\u01f7U\3\2\2\2\u01f8\u01f9\b,\1\2\u01f9\u01fa\7\66\2")
        buf.write("\2\u01fa\u0205\3\2\2\2\u01fb\u01fc\f\5\2\2\u01fc\u01fd")
        buf.write("\7,\2\2\u01fd\u0204\7\66\2\2\u01fe\u01ff\f\4\2\2\u01ff")
        buf.write("\u0200\7/\2\2\u0200\u0201\5<\37\2\u0201\u0202\7\60\2\2")
        buf.write("\u0202\u0204\3\2\2\2\u0203\u01fb\3\2\2\2\u0203\u01fe\3")
        buf.write("\2\2\2\u0204\u0207\3\2\2\2\u0205\u0203\3\2\2\2\u0205\u0206")
        buf.write("\3\2\2\2\u0206W\3\2\2\2\u0207\u0205\3\2\2\2\u0208\u0209")
        buf.write("\t\n\2\2\u0209Y\3\2\2\2\u020a\u020b\5V,\2\u020b\u020c")
        buf.write("\5X-\2\u020c\u020d\5<\37\2\u020d[\3\2\2\2\u020e\u020f")
        buf.write("\7\4\2\2\u020f\u0210\7\3\2\2\u0210\u0211\7-\2\2\u0211")
        buf.write("\u0212\5<\37\2\u0212\u0213\7.\2\2\u0213\u0215\7\61\2\2")
        buf.write("\u0214\u0216\5T+\2\u0215\u0214\3\2\2\2\u0215\u0216\3\2")
        buf.write("\2\2\u0216\u0217\3\2\2\2\u0217\u0218\7\62\2\2\u0218]\3")
        buf.write("\2\2\2\u0219\u021e\5\\/\2\u021a\u021b\5\\/\2\u021b\u021c")
        buf.write("\5^\60\2\u021c\u021e\3\2\2\2\u021d\u0219\3\2\2\2\u021d")
        buf.write("\u021a\3\2\2\2\u021e_\3\2\2\2\u021f\u0220\7\3\2\2\u0220")
        buf.write("\u0221\7-\2\2\u0221\u0222\5<\37\2\u0222\u0223\7.\2\2\u0223")
        buf.write("\u0225\7\61\2\2\u0224\u0226\5T+\2\u0225\u0224\3\2\2\2")
        buf.write("\u0225\u0226\3\2\2\2\u0226\u0227\3\2\2\2\u0227\u0229\7")
        buf.write("\62\2\2\u0228\u022a\5^\60\2\u0229\u0228\3\2\2\2\u0229")
        buf.write("\u022a\3\2\2\2\u022a\u0231\3\2\2\2\u022b\u022c\7\4\2\2")
        buf.write("\u022c\u022e\7\61\2\2\u022d\u022f\5T+\2\u022e\u022d\3")
        buf.write("\2\2\2\u022e\u022f\3\2\2\2\u022f\u0230\3\2\2\2\u0230\u0232")
        buf.write("\7\62\2\2\u0231\u022b\3\2\2\2\u0231\u0232\3\2\2\2\u0232")
        buf.write("a\3\2\2\2\u0233\u0237\7\5\2\2\u0234\u0238\5d\63\2\u0235")
        buf.write("\u0238\5h\65\2\u0236\u0238\5j\66\2\u0237\u0234\3\2\2\2")
        buf.write("\u0237\u0235\3\2\2\2\u0237\u0236\3\2\2\2\u0238c\3\2\2")
        buf.write("\2\u0239\u023a\5<\37\2\u023a\u023c\7\61\2\2\u023b\u023d")
        buf.write("\5T+\2\u023c\u023b\3\2\2\2\u023c\u023d\3\2\2\2\u023d\u023e")
        buf.write("\3\2\2\2\u023e\u023f\7\62\2\2\u023fe\3\2\2\2\u0240\u0241")
        buf.write("\7\66\2\2\u0241\u0242\t\13\2\2\u0242\u0243\5<\37\2\u0243")
        buf.write("g\3\2\2\2\u0244\u0245\7\66\2\2\u0245\u0246\t\13\2\2\u0246")
        buf.write("\u024f\5<\37\2\u0247\u0248\7\20\2\2\u0248\u024a\7\66\2")
        buf.write("\2\u0249\u024b\5\30\r\2\u024a\u0249\3\2\2\2\u024a\u024b")
        buf.write("\3\2\2\2\u024b\u024c\3\2\2\2\u024c\u024d\7+\2\2\u024d")
        buf.write("\u024f\5<\37\2\u024e\u0244\3\2\2\2\u024e\u0247\3\2\2\2")
        buf.write("\u024f\u0250\3\2\2\2\u0250\u0251\7\64\2\2\u0251\u0252")
        buf.write("\5<\37\2\u0252\u0253\7\64\2\2\u0253\u0254\5f\64\2\u0254")
        buf.write("\u0256\7\61\2\2\u0255\u0257\5T+\2\u0256\u0255\3\2\2\2")
        buf.write("\u0256\u0257\3\2\2\2\u0257\u0258\3\2\2\2\u0258\u0259\7")
        buf.write("\62\2\2\u0259i\3\2\2\2\u025a\u025b\7\66\2\2\u025b\u025c")
        buf.write("\7\63\2\2\u025c\u025d\7\66\2\2\u025d\u025e\7%\2\2\u025e")
        buf.write("\u0263\7\23\2\2\u025f\u0264\5V,\2\u0260\u0264\7\67\2\2")
        buf.write("\u0261\u0264\5*\26\2\u0262\u0264\5\32\16\2\u0263\u025f")
        buf.write("\3\2\2\2\u0263\u0260\3\2\2\2\u0263\u0261\3\2\2\2\u0263")
        buf.write("\u0262\3\2\2\2\u0264\u0265\3\2\2\2\u0265\u0267\7\61\2")
        buf.write("\2\u0266\u0268\5T+\2\u0267\u0266\3\2\2\2\u0267\u0268\3")
        buf.write("\2\2\2\u0268\u0269\3\2\2\2\u0269\u026a\7\62\2\2\u026a")
        buf.write("k\3\2\2\2\u026b\u026c\7\22\2\2\u026cm\3\2\2\2\u026d\u026e")
        buf.write("\7\21\2\2\u026eo\3\2\2\2\u026f\u0270\b9\1\2\u0270\u0271")
        buf.write("\5r:\2\u0271\u027b\3\2\2\2\u0272\u0273\f\5\2\2\u0273\u0274")
        buf.write("\7,\2\2\u0274\u027a\5p9\6\u0275\u0276\f\4\2\2\u0276\u0277")
        buf.write("\7/\2\2\u0277\u0278\7\67\2\2\u0278\u027a\7\60\2\2\u0279")
        buf.write("\u0272\3\2\2\2\u0279\u0275\3\2\2\2\u027a\u027d\3\2\2\2")
        buf.write("\u027b\u0279\3\2\2\2\u027b\u027c\3\2\2\2\u027cq\3\2\2")
        buf.write("\2\u027d\u027b\3\2\2\2\u027e\u0281\7\66\2\2\u027f\u0281")
        buf.write("\5L\'\2\u0280\u027e\3\2\2\2\u0280\u027f\3\2\2\2\u0281")
        buf.write("s\3\2\2\2\u0282\u0284\7\6\2\2\u0283\u0285\5<\37\2\u0284")
        buf.write("\u0283\3\2\2\2\u0284\u0285\3\2\2\2\u0285u\3\2\2\2F\u0080")
        buf.write("\u0088\u0098\u00a5\u00a9\u00b2\u00b5\u00b9\u00be\u00c9")
        buf.write("\u00d2\u00d4\u00db\u00e5\u00ed\u00f5\u00fa\u0100\u0104")
        buf.write("\u0108\u0114\u0118\u011b\u0124\u0131\u013d\u0141\u0148")
        buf.write("\u014c\u014f\u0153\u0159\u0169\u0173\u017d\u0188\u0193")
        buf.write("\u019e\u01a9\u01af\u01bc\u01c4\u01c6\u01d0\u01d5\u01e0")
        buf.write("\u01e8\u01ed\u01f6\u0203\u0205\u0215\u021d\u0225\u0229")
        buf.write("\u022e\u0231\u0237\u023c\u024a\u024e\u0256\u0263\u0267")
        buf.write("\u0279\u027b\u0280\u0284")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'for'", "'return'", 
                     "'func'", "'type'", "'struct'", "'interface'", "'string'", 
                     "'int'", "'float'", "'boolean'", "'const'", "'var'", 
                     "'continue'", "'break'", "'range'", "'nil'", "'true'", 
                     "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'||'", "'&&'", 
                     "'!'", "':='", "'+='", "'-='", "'*='", "'/='", "'%='", 
                     "'='", "'.'", "'('", "')'", "'['", "']'", "'{'", "'}'", 
                     "','", "<INVALID>", "':'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
                      "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", 
                      "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", 
                      "NIL", "TRUE", "FALSE", "ADD", "SUB", "MUL", "DIV", 
                      "MOD", "EQUAL", "NOT_EQUAL", "LESS", "LESS_EQUAL", 
                      "GREATER", "GREATER_EQUAL", "OR", "AND", "NOT", "SHORT_DECL", 
                      "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", 
                      "MOD_ASSIGN", "ASSIGN", "DOT", "LPAREN", "RPAREN", 
                      "LBRACKET", "RBRACKET", "LBRACE", "RBRACE", "COMA", 
                      "SEMI", "COLON", "ID", "INT_LIT", "FLOAT_LIT", "STRING_LIT", 
                      "WS", "COMMENT", "LINE_COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_list_declared_statement = 1
    RULE_declared_statement = 2
    RULE_const_decl = 3
    RULE_var_decl = 4
    RULE_primitive_type = 5
    RULE_numeric_literal = 6
    RULE_boolean_literal = 7
    RULE_primitive_literal = 8
    RULE_literal = 9
    RULE_array_bracket = 10
    RULE_type_return = 11
    RULE_array_literal = 12
    RULE_array_lit_elements = 13
    RULE_array_lit_element = 14
    RULE_params = 15
    RULE_param_type = 16
    RULE_param_type_1 = 17
    RULE_func_decl = 18
    RULE_method_decl = 19
    RULE_struct_literal = 20
    RULE_struct_element = 21
    RULE_interface_decl = 22
    RULE_method_interface_decl = 23
    RULE_method_params = 24
    RULE_struct_decl = 25
    RULE_struct_decl_elements = 26
    RULE_struct_decl_element = 27
    RULE_list_expression = 28
    RULE_expression = 29
    RULE_expression1 = 30
    RULE_expression2 = 31
    RULE_expression3 = 32
    RULE_expression4 = 33
    RULE_expression5 = 34
    RULE_expression6 = 35
    RULE_expression7 = 36
    RULE_func_call = 37
    RULE_list_statement = 38
    RULE_statement = 39
    RULE_full_statement = 40
    RULE_statements_in_block = 41
    RULE_lhs = 42
    RULE_op_assign = 43
    RULE_assign_statement = 44
    RULE_else_if_el = 45
    RULE_else_if_statement = 46
    RULE_if_statement = 47
    RULE_for_statement = 48
    RULE_basic_for_statement = 49
    RULE_update_part = 50
    RULE_init_for_statement = 51
    RULE_range_for_statement = 52
    RULE_break_statement = 53
    RULE_continue_statement = 54
    RULE_call_statement = 55
    RULE_call_statement_1 = 56
    RULE_return_statement = 57

    ruleNames =  [ "program", "list_declared_statement", "declared_statement", 
                   "const_decl", "var_decl", "primitive_type", "numeric_literal", 
                   "boolean_literal", "primitive_literal", "literal", "array_bracket", 
                   "type_return", "array_literal", "array_lit_elements", 
                   "array_lit_element", "params", "param_type", "param_type_1", 
                   "func_decl", "method_decl", "struct_literal", "struct_element", 
                   "interface_decl", "method_interface_decl", "method_params", 
                   "struct_decl", "struct_decl_elements", "struct_decl_element", 
                   "list_expression", "expression", "expression1", "expression2", 
                   "expression3", "expression4", "expression5", "expression6", 
                   "expression7", "func_call", "list_statement", "statement", 
                   "full_statement", "statements_in_block", "lhs", "op_assign", 
                   "assign_statement", "else_if_el", "else_if_statement", 
                   "if_statement", "for_statement", "basic_for_statement", 
                   "update_part", "init_for_statement", "range_for_statement", 
                   "break_statement", "continue_statement", "call_statement", 
                   "call_statement_1", "return_statement" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    FOR=3
    RETURN=4
    FUNC=5
    TYPE=6
    STRUCT=7
    INTERFACE=8
    STRING=9
    INT=10
    FLOAT=11
    BOOLEAN=12
    CONST=13
    VAR=14
    CONTINUE=15
    BREAK=16
    RANGE=17
    NIL=18
    TRUE=19
    FALSE=20
    ADD=21
    SUB=22
    MUL=23
    DIV=24
    MOD=25
    EQUAL=26
    NOT_EQUAL=27
    LESS=28
    LESS_EQUAL=29
    GREATER=30
    GREATER_EQUAL=31
    OR=32
    AND=33
    NOT=34
    SHORT_DECL=35
    ADD_ASSIGN=36
    SUB_ASSIGN=37
    MUL_ASSIGN=38
    DIV_ASSIGN=39
    MOD_ASSIGN=40
    ASSIGN=41
    DOT=42
    LPAREN=43
    RPAREN=44
    LBRACKET=45
    RBRACKET=46
    LBRACE=47
    RBRACE=48
    COMA=49
    SEMI=50
    COLON=51
    ID=52
    INT_LIT=53
    FLOAT_LIT=54
    STRING_LIT=55
    WS=56
    COMMENT=57
    LINE_COMMENT=58
    ERROR_CHAR=59
    UNCLOSE_STRING=60
    ILLEGAL_ESCAPE=61

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_declared_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_declared_statementContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.list_declared_statement()
            self.state = 117
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_declared_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declared_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Declared_statementContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def list_declared_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_declared_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_declared_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_declared_statement" ):
                return visitor.visitList_declared_statement(self)
            else:
                return visitor.visitChildren(self)




    def list_declared_statement(self):

        localctx = MiniGoParser.List_declared_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_list_declared_statement)
        try:
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.declared_statement()
                self.state = 120
                self.match(MiniGoParser.SEMI)
                self.state = 121
                self.list_declared_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.declared_statement()
                self.state = 124
                self.match(MiniGoParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declared_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def func_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Func_declContext,0)


        def struct_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declContext,0)


        def interface_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_declContext,0)


        def method_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Method_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declared_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclared_statement" ):
                return visitor.visitDeclared_statement(self)
            else:
                return visitor.visitChildren(self)




    def declared_statement(self):

        localctx = MiniGoParser.Declared_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declared_statement)
        try:
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.const_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 130
                self.func_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 131
                self.struct_decl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 132
                self.interface_decl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 133
                self.method_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_const_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_decl" ):
                return visitor.visitConst_decl(self)
            else:
                return visitor.visitChildren(self)




    def const_decl(self):

        localctx = MiniGoParser.Const_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_const_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(MiniGoParser.CONST)
            self.state = 137
            self.match(MiniGoParser.ID)
            self.state = 138
            self.match(MiniGoParser.ASSIGN)
            self.state = 139
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def type_return(self):
            return self.getTypedRuleContext(MiniGoParser.Type_returnContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = MiniGoParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(MiniGoParser.VAR)
            self.state = 142
            self.match(MiniGoParser.ID)
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 143
                self.type_return()
                pass

            elif la_ == 2:
                self.state = 144
                self.match(MiniGoParser.ASSIGN)
                self.state = 145
                self.expression(0)
                pass

            elif la_ == 3:
                self.state = 146
                self.type_return()
                self.state = 147
                self.match(MiniGoParser.ASSIGN)
                self.state = 148
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = MiniGoParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Numeric_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_numeric_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumeric_literal" ):
                return visitor.visitNumeric_literal(self)
            else:
                return visitor.visitChildren(self)




    def numeric_literal(self):

        localctx = MiniGoParser.Numeric_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_numeric_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.INT_LIT or _la==MiniGoParser.FLOAT_LIT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boolean_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_boolean_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_literal" ):
                return visitor.visitBoolean_literal(self)
            else:
                return visitor.visitChildren(self)




    def boolean_literal(self):

        localctx = MiniGoParser.Boolean_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_boolean_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.TRUE or _la==MiniGoParser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def numeric_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Numeric_literalContext,0)


        def boolean_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Boolean_literalContext,0)


        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_primitive_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_literal" ):
                return visitor.visitPrimitive_literal(self)
            else:
                return visitor.visitChildren(self)




    def primitive_literal(self):

        localctx = MiniGoParser.Primitive_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_primitive_literal)
        try:
            self.state = 163
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.match(MiniGoParser.NIL)
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self.struct_literal()
                pass
            elif token in [MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 160
                self.numeric_literal()
                pass
            elif token in [MiniGoParser.TRUE, MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 161
                self.boolean_literal()
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 162
                self.match(MiniGoParser.STRING_LIT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_literalContext,0)


        def array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_literal)
        try:
            self.state = 167
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.primitive_literal()
                pass
            elif token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.array_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_bracketContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(MiniGoParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(MiniGoParser.RBRACKET, 0)

        def array_bracket(self):
            return self.getTypedRuleContext(MiniGoParser.Array_bracketContext,0)


        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_bracket

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_bracket" ):
                return visitor.visitArray_bracket(self)
            else:
                return visitor.visitChildren(self)




    def array_bracket(self):

        localctx = MiniGoParser.Array_bracketContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_array_bracket)
        self._la = 0 # Token type
        try:
            self.state = 176
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.match(MiniGoParser.LBRACKET)
                self.state = 170
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.ID or _la==MiniGoParser.INT_LIT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 171
                self.match(MiniGoParser.RBRACKET)
                self.state = 172
                self.array_bracket()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.match(MiniGoParser.LBRACKET)
                self.state = 174
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.ID or _la==MiniGoParser.INT_LIT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 175
                self.match(MiniGoParser.RBRACKET)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_returnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def array_bracket(self):
            return self.getTypedRuleContext(MiniGoParser.Array_bracketContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_type_return

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_return" ):
                return visitor.visitType_return(self)
            else:
                return visitor.visitChildren(self)




    def type_return(self):

        localctx = MiniGoParser.Type_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_type_return)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LBRACKET:
                self.state = 178
                self.array_bracket()


            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 181
                self.match(MiniGoParser.ID)
                pass
            elif token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 182
                self.primitive_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_bracket(self):
            return self.getTypedRuleContext(MiniGoParser.Array_bracketContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def array_lit_elements(self):
            return self.getTypedRuleContext(MiniGoParser.Array_lit_elementsContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = MiniGoParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.array_bracket()
            self.state = 188
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 186
                self.match(MiniGoParser.ID)
                pass
            elif token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 187
                self.primitive_type()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 190
            self.match(MiniGoParser.LBRACE)
            self.state = 191
            self.array_lit_elements()
            self.state = 192
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_lit_elementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_lit_element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Array_lit_elementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Array_lit_elementContext,i)


        def COMA(self):
            return self.getToken(MiniGoParser.COMA, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_lit_elements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit_elements" ):
                return visitor.visitArray_lit_elements(self)
            else:
                return visitor.visitChildren(self)




    def array_lit_elements(self):

        localctx = MiniGoParser.Array_lit_elementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_array_lit_elements)
        try:
            self.state = 199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.array_lit_element(0)
                self.state = 195
                self.match(MiniGoParser.COMA)
                self.state = 196
                self.array_lit_element(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
                self.array_lit_element(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_lit_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def array_lit_element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Array_lit_elementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Array_lit_elementContext,i)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def primitive_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_literalContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COMA(self):
            return self.getToken(MiniGoParser.COMA, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_lit_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit_element" ):
                return visitor.visitArray_lit_element(self)
            else:
                return visitor.visitChildren(self)



    def array_lit_element(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Array_lit_elementContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_array_lit_element, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LBRACE]:
                self.state = 202
                self.match(MiniGoParser.LBRACE)
                self.state = 203
                self.array_lit_element(0)
                self.state = 204
                self.match(MiniGoParser.RBRACE)
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.state = 208
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                if la_ == 1:
                    self.state = 206
                    self.primitive_literal()
                    pass

                elif la_ == 2:
                    self.state = 207
                    self.match(MiniGoParser.ID)
                    pass


                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 217
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Array_lit_elementContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_array_lit_element)
                    self.state = 212
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 213
                    self.match(MiniGoParser.COMA)
                    self.state = 214
                    self.array_lit_element(3) 
                self.state = 219
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def param_type(self):
            return self.getTypedRuleContext(MiniGoParser.Param_typeContext,0)


        def COMA(self):
            return self.getToken(MiniGoParser.COMA, 0)

        def params(self):
            return self.getTypedRuleContext(MiniGoParser.ParamsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = MiniGoParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_params)
        try:
            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.match(MiniGoParser.ID)
                self.state = 221
                self.param_type(0)
                self.state = 222
                self.match(MiniGoParser.COMA)
                self.state = 223
                self.params()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 225
                self.match(MiniGoParser.ID)
                self.state = 226
                self.param_type(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(MiniGoParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(MiniGoParser.RBRACKET, 0)

        def param_type(self):
            return self.getTypedRuleContext(MiniGoParser.Param_typeContext,0)


        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def param_type_1(self):
            return self.getTypedRuleContext(MiniGoParser.Param_type_1Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_param_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_type" ):
                return visitor.visitParam_type(self)
            else:
                return visitor.visitChildren(self)



    def param_type(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Param_typeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_param_type, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LBRACKET]:
                self.state = 230
                self.match(MiniGoParser.LBRACKET)
                self.state = 231
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.ID or _la==MiniGoParser.INT_LIT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 232
                self.match(MiniGoParser.RBRACKET)
                self.state = 233
                self.param_type(2)
                pass
            elif token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.ID]:
                self.state = 234
                self.param_type_1()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 243
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Param_typeContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_param_type)
                    self.state = 237
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 238
                    self.match(MiniGoParser.LBRACKET)
                    self.state = 239
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ID or _la==MiniGoParser.INT_LIT):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 240
                    self.match(MiniGoParser.RBRACKET) 
                self.state = 245
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Param_type_1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_param_type_1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_type_1" ):
                return visitor.visitParam_type_1(self)
            else:
                return visitor.visitChildren(self)




    def param_type_1(self):

        localctx = MiniGoParser.Param_type_1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_param_type_1)
        try:
            self.state = 248
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.primitive_type()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.match(MiniGoParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def method_params(self):
            return self.getTypedRuleContext(MiniGoParser.Method_paramsContext,0)


        def type_return(self):
            return self.getTypedRuleContext(MiniGoParser.Type_returnContext,0)


        def statements_in_block(self):
            return self.getTypedRuleContext(MiniGoParser.Statements_in_blockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = MiniGoParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.match(MiniGoParser.FUNC)
            self.state = 251
            self.match(MiniGoParser.ID)
            self.state = 252
            self.match(MiniGoParser.LPAREN)
            self.state = 254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 253
                self.method_params()


            self.state = 256
            self.match(MiniGoParser.RPAREN)
            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.ID))) != 0):
                self.state = 257
                self.type_return()


            self.state = 260
            self.match(MiniGoParser.LBRACE)
            self.state = 262
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 261
                self.statements_in_block()


            self.state = 264
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LPAREN)
            else:
                return self.getToken(MiniGoParser.LPAREN, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RPAREN)
            else:
                return self.getToken(MiniGoParser.RPAREN, i)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def statements_in_block(self):
            return self.getTypedRuleContext(MiniGoParser.Statements_in_blockContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def method_params(self):
            return self.getTypedRuleContext(MiniGoParser.Method_paramsContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def type_return(self):
            return self.getTypedRuleContext(MiniGoParser.Type_returnContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_decl" ):
                return visitor.visitMethod_decl(self)
            else:
                return visitor.visitChildren(self)




    def method_decl(self):

        localctx = MiniGoParser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_method_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(MiniGoParser.FUNC)
            self.state = 267
            self.match(MiniGoParser.LPAREN)
            self.state = 268
            self.match(MiniGoParser.ID)
            self.state = 269
            self.match(MiniGoParser.ID)
            self.state = 270
            self.match(MiniGoParser.RPAREN)
            self.state = 271
            self.match(MiniGoParser.ID)
            self.state = 272
            self.match(MiniGoParser.LPAREN)
            self.state = 274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 273
                self.method_params()


            self.state = 276
            self.match(MiniGoParser.RPAREN)
            self.state = 278
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 277
                self.expression(0)


            self.state = 281
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.ID))) != 0):
                self.state = 280
                self.type_return()


            self.state = 283
            self.match(MiniGoParser.LBRACE)
            self.state = 284
            self.statements_in_block()
            self.state = 285
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def struct_element(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_elementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_literal" ):
                return visitor.visitStruct_literal(self)
            else:
                return visitor.visitChildren(self)




    def struct_literal(self):

        localctx = MiniGoParser.Struct_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_struct_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(MiniGoParser.ID)
            self.state = 288
            self.match(MiniGoParser.LBRACE)
            self.state = 290
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 289
                self.struct_element()


            self.state = 292
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def COMA(self):
            return self.getToken(MiniGoParser.COMA, 0)

        def struct_element(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_elementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_element" ):
                return visitor.visitStruct_element(self)
            else:
                return visitor.visitChildren(self)




    def struct_element(self):

        localctx = MiniGoParser.Struct_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_struct_element)
        try:
            self.state = 303
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.match(MiniGoParser.ID)
                self.state = 295
                self.match(MiniGoParser.COLON)
                self.state = 296
                self.expression(0)
                self.state = 297
                self.match(MiniGoParser.COMA)
                self.state = 298
                self.struct_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 300
                self.match(MiniGoParser.ID)
                self.state = 301
                self.match(MiniGoParser.COLON)
                self.state = 302
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def method_interface_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Method_interface_declContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_decl" ):
                return visitor.visitInterface_decl(self)
            else:
                return visitor.visitChildren(self)




    def interface_decl(self):

        localctx = MiniGoParser.Interface_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_interface_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.match(MiniGoParser.TYPE)
            self.state = 306
            self.match(MiniGoParser.ID)
            self.state = 307
            self.match(MiniGoParser.INTERFACE)
            self.state = 308
            self.match(MiniGoParser.LBRACE)
            self.state = 309
            self.method_interface_decl()
            self.state = 310
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_interface_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def method_interface_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Method_interface_declContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def method_params(self):
            return self.getTypedRuleContext(MiniGoParser.Method_paramsContext,0)


        def type_return(self):
            return self.getTypedRuleContext(MiniGoParser.Type_returnContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_interface_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_interface_decl" ):
                return visitor.visitMethod_interface_decl(self)
            else:
                return visitor.visitChildren(self)




    def method_interface_decl(self):

        localctx = MiniGoParser.Method_interface_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_method_interface_decl)
        self._la = 0 # Token type
        try:
            self.state = 333
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                self.match(MiniGoParser.ID)
                self.state = 313
                self.match(MiniGoParser.LPAREN)
                self.state = 315
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ID:
                    self.state = 314
                    self.method_params()


                self.state = 317
                self.match(MiniGoParser.RPAREN)
                self.state = 319
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 318
                    self.type_return()


                self.state = 321
                self.match(MiniGoParser.SEMI)
                self.state = 322
                self.method_interface_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 323
                self.match(MiniGoParser.ID)
                self.state = 324
                self.match(MiniGoParser.LPAREN)
                self.state = 326
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ID:
                    self.state = 325
                    self.method_params()


                self.state = 328
                self.match(MiniGoParser.RPAREN)
                self.state = 330
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 329
                    self.type_return()


                self.state = 332
                self.match(MiniGoParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_paramsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COMA(self):
            return self.getToken(MiniGoParser.COMA, 0)

        def method_params(self):
            return self.getTypedRuleContext(MiniGoParser.Method_paramsContext,0)


        def type_return(self):
            return self.getTypedRuleContext(MiniGoParser.Type_returnContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_params" ):
                return visitor.visitMethod_params(self)
            else:
                return visitor.visitChildren(self)




    def method_params(self):

        localctx = MiniGoParser.Method_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_method_params)
        self._la = 0 # Token type
        try:
            self.state = 343
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 335
                self.match(MiniGoParser.ID)
                self.state = 337
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 336
                    self.type_return()


                self.state = 339
                self.match(MiniGoParser.COMA)
                self.state = 340
                self.method_params()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 341
                self.match(MiniGoParser.ID)
                self.state = 342
                self.type_return()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def struct_decl_elements(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_decl_elementsContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_decl" ):
                return visitor.visitStruct_decl(self)
            else:
                return visitor.visitChildren(self)




    def struct_decl(self):

        localctx = MiniGoParser.Struct_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_struct_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.match(MiniGoParser.TYPE)
            self.state = 346
            self.match(MiniGoParser.ID)
            self.state = 347
            self.match(MiniGoParser.STRUCT)
            self.state = 348
            self.match(MiniGoParser.LBRACE)
            self.state = 349
            self.struct_decl_elements()
            self.state = 350
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_decl_elementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_decl_element(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_decl_elementContext,0)


        def struct_decl_elements(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_decl_elementsContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_decl_elements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_decl_elements" ):
                return visitor.visitStruct_decl_elements(self)
            else:
                return visitor.visitChildren(self)




    def struct_decl_elements(self):

        localctx = MiniGoParser.Struct_decl_elementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_struct_decl_elements)
        try:
            self.state = 359
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 352
                self.struct_decl_element()

                self.state = 353
                self.match(MiniGoParser.SEMI)
                self.state = 354
                self.struct_decl_elements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 356
                self.struct_decl_element()

                self.state = 357
                self.match(MiniGoParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_decl_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def type_return(self):
            return self.getTypedRuleContext(MiniGoParser.Type_returnContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_decl_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_decl_element" ):
                return visitor.visitStruct_decl_element(self)
            else:
                return visitor.visitChildren(self)




    def struct_decl_element(self):

        localctx = MiniGoParser.Struct_decl_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_struct_decl_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.match(MiniGoParser.ID)
            self.state = 362
            self.type_return()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def COMA(self):
            return self.getToken(MiniGoParser.COMA, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expression" ):
                return visitor.visitList_expression(self)
            else:
                return visitor.visitChildren(self)




    def list_expression(self):

        localctx = MiniGoParser.List_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_list_expression)
        try:
            self.state = 369
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 364
                self.expression(0)
                self.state = 365
                self.match(MiniGoParser.COMA)
                self.state = 366
                self.list_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 368
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.expression1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 379
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 374
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 375
                    self.match(MiniGoParser.OR)
                    self.state = 376
                    self.expression1(0) 
                self.state = 381
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self):
            return self.getTypedRuleContext(MiniGoParser.Expression2Context,0)


        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression1" ):
                return visitor.visitExpression1(self)
            else:
                return visitor.visitChildren(self)



    def expression1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_expression1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.expression2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 390
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression1)
                    self.state = 385
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 386
                    self.match(MiniGoParser.AND)
                    self.state = 387
                    self.expression2(0) 
                self.state = 392
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression3(self):
            return self.getTypedRuleContext(MiniGoParser.Expression3Context,0)


        def expression2(self):
            return self.getTypedRuleContext(MiniGoParser.Expression2Context,0)


        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(MiniGoParser.NOT_EQUAL, 0)

        def LESS(self):
            return self.getToken(MiniGoParser.LESS, 0)

        def GREATER(self):
            return self.getToken(MiniGoParser.GREATER, 0)

        def LESS_EQUAL(self):
            return self.getToken(MiniGoParser.LESS_EQUAL, 0)

        def GREATER_EQUAL(self):
            return self.getToken(MiniGoParser.GREATER_EQUAL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression2" ):
                return visitor.visitExpression2(self)
            else:
                return visitor.visitChildren(self)



    def expression2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_expression2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 401
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 396
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 397
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQUAL) | (1 << MiniGoParser.NOT_EQUAL) | (1 << MiniGoParser.LESS) | (1 << MiniGoParser.LESS_EQUAL) | (1 << MiniGoParser.GREATER) | (1 << MiniGoParser.GREATER_EQUAL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 398
                    self.expression3(0) 
                self.state = 403
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression4(self):
            return self.getTypedRuleContext(MiniGoParser.Expression4Context,0)


        def expression3(self):
            return self.getTypedRuleContext(MiniGoParser.Expression3Context,0)


        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression3" ):
                return visitor.visitExpression3(self)
            else:
                return visitor.visitChildren(self)



    def expression3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 412
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 407
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 408
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 409
                    self.expression4(0) 
                self.state = 414
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(MiniGoParser.Expression5Context,0)


        def expression4(self):
            return self.getTypedRuleContext(MiniGoParser.Expression4Context,0)


        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression4" ):
                return visitor.visitExpression4(self)
            else:
                return visitor.visitChildren(self)



    def expression4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 423
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 418
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 419
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 420
                    self.expression5() 
                self.state = 425
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(MiniGoParser.Expression5Context,0)


        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression5" ):
                return visitor.visitExpression5(self)
            else:
                return visitor.visitChildren(self)




    def expression5(self):

        localctx = MiniGoParser.Expression5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_expression5)
        self._la = 0 # Token type
        try:
            self.state = 429
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SUB, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 426
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SUB or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 427
                self.expression5()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LPAREN, MiniGoParser.LBRACKET, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 428
                self.expression6(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression7(self):
            return self.getTypedRuleContext(MiniGoParser.Expression7Context,0)


        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def LBRACKET(self):
            return self.getToken(MiniGoParser.LBRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RBRACKET(self):
            return self.getToken(MiniGoParser.RBRACKET, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression6" ):
                return visitor.visitExpression6(self)
            else:
                return visitor.visitChildren(self)



    def expression6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_expression6, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.expression7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 452
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 450
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                        self.state = 434
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 435
                        self.match(MiniGoParser.DOT)
                        self.state = 436
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                        self.state = 437
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 438
                        self.match(MiniGoParser.DOT)
                        self.state = 439
                        self.match(MiniGoParser.ID)
                        self.state = 440
                        self.match(MiniGoParser.LPAREN)
                        self.state = 442
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                            self.state = 441
                            self.list_expression()


                        self.state = 444
                        self.match(MiniGoParser.RPAREN)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                        self.state = 445
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 446
                        self.match(MiniGoParser.LBRACKET)
                        self.state = 447
                        self.expression(0)
                        self.state = 448
                        self.match(MiniGoParser.RBRACKET)
                        pass

             
                self.state = 454
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression7" ):
                return visitor.visitExpression7(self)
            else:
                return visitor.visitChildren(self)




    def expression7(self):

        localctx = MiniGoParser.Expression7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_expression7)
        try:
            self.state = 462
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 455
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 456
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 457
                self.func_call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 458
                self.match(MiniGoParser.LPAREN)
                self.state = 459
                self.expression(0)
                self.state = 460
                self.match(MiniGoParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = MiniGoParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 464
            self.match(MiniGoParser.ID)
            self.state = 465
            self.match(MiniGoParser.LPAREN)
            self.state = 467
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 466
                self.list_expression()


            self.state = 469
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_statement" ):
                return visitor.visitList_statement(self)
            else:
                return visitor.visitChildren(self)




    def list_statement(self):

        localctx = MiniGoParser.List_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_list_statement)
        try:
            self.state = 478
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 471
                self.statement()
                self.state = 472
                self.match(MiniGoParser.SEMI)
                self.state = 473
                self.list_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 475
                self.statement()
                self.state = 476
                self.match(MiniGoParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declared_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Declared_statementContext,0)


        def assign_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(MiniGoParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(MiniGoParser.For_statementContext,0)


        def call_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Call_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Return_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_statement)
        try:
            self.state = 486
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 480
                self.declared_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 481
                self.assign_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 482
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 483
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 484
                self.call_statement(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 485
                self.return_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Full_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_full_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFull_statement" ):
                return visitor.visitFull_statement(self)
            else:
                return visitor.visitChildren(self)




    def full_statement(self):

        localctx = MiniGoParser.Full_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_full_statement)
        try:
            self.state = 491
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.FUNC, MiniGoParser.TYPE, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 488
                self.statement()
                pass
            elif token in [MiniGoParser.BREAK]:
                self.enterOuterAlt(localctx, 2)
                self.state = 489
                self.break_statement()
                pass
            elif token in [MiniGoParser.CONTINUE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 490
                self.continue_statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statements_in_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def full_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Full_statementContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def statements_in_block(self):
            return self.getTypedRuleContext(MiniGoParser.Statements_in_blockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statements_in_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements_in_block" ):
                return visitor.visitStatements_in_block(self)
            else:
                return visitor.visitChildren(self)




    def statements_in_block(self):

        localctx = MiniGoParser.Statements_in_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_statements_in_block)
        try:
            self.state = 500
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 493
                self.full_statement()
                self.state = 494
                self.match(MiniGoParser.SEMI)
                self.state = 495
                self.statements_in_block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 497
                self.full_statement()
                self.state = 498
                self.match(MiniGoParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def LBRACKET(self):
            return self.getToken(MiniGoParser.LBRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RBRACKET(self):
            return self.getToken(MiniGoParser.RBRACKET, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)



    def lhs(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.LhsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_lhs, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 503
            self.match(MiniGoParser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 515
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,50,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 513
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.LhsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                        self.state = 505
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 506
                        self.match(MiniGoParser.DOT)
                        self.state = 507
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.LhsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                        self.state = 508
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 509
                        self.match(MiniGoParser.LBRACKET)
                        self.state = 510
                        self.expression(0)
                        self.state = 511
                        self.match(MiniGoParser.RBRACKET)
                        pass

             
                self.state = 517
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,50,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Op_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SHORT_DECL(self):
            return self.getToken(MiniGoParser.SHORT_DECL, 0)

        def ADD_ASSIGN(self):
            return self.getToken(MiniGoParser.ADD_ASSIGN, 0)

        def SUB_ASSIGN(self):
            return self.getToken(MiniGoParser.SUB_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(MiniGoParser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(MiniGoParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(MiniGoParser.MOD_ASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_op_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_assign" ):
                return visitor.visitOp_assign(self)
            else:
                return visitor.visitChildren(self)




    def op_assign(self):

        localctx = MiniGoParser.Op_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_op_assign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 518
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.SHORT_DECL) | (1 << MiniGoParser.ADD_ASSIGN) | (1 << MiniGoParser.SUB_ASSIGN) | (1 << MiniGoParser.MUL_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def op_assign(self):
            return self.getTypedRuleContext(MiniGoParser.Op_assignContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_statement" ):
                return visitor.visitAssign_statement(self)
            else:
                return visitor.visitChildren(self)




    def assign_statement(self):

        localctx = MiniGoParser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_assign_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 520
            self.lhs(0)
            self.state = 521
            self.op_assign()
            self.state = 522
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_if_elContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def statements_in_block(self):
            return self.getTypedRuleContext(MiniGoParser.Statements_in_blockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_if_el

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_if_el" ):
                return visitor.visitElse_if_el(self)
            else:
                return visitor.visitChildren(self)




    def else_if_el(self):

        localctx = MiniGoParser.Else_if_elContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_else_if_el)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 524
            self.match(MiniGoParser.ELSE)
            self.state = 525
            self.match(MiniGoParser.IF)
            self.state = 526
            self.match(MiniGoParser.LPAREN)
            self.state = 527
            self.expression(0)
            self.state = 528
            self.match(MiniGoParser.RPAREN)
            self.state = 529
            self.match(MiniGoParser.LBRACE)
            self.state = 531
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 530
                self.statements_in_block()


            self.state = 533
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_if_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def else_if_el(self):
            return self.getTypedRuleContext(MiniGoParser.Else_if_elContext,0)


        def else_if_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Else_if_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_if_statement" ):
                return visitor.visitElse_if_statement(self)
            else:
                return visitor.visitChildren(self)




    def else_if_statement(self):

        localctx = MiniGoParser.Else_if_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_else_if_statement)
        try:
            self.state = 539
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 535
                self.else_if_el()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 536
                self.else_if_el()
                self.state = 537
                self.else_if_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LBRACE)
            else:
                return self.getToken(MiniGoParser.LBRACE, i)

        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RBRACE)
            else:
                return self.getToken(MiniGoParser.RBRACE, i)

        def statements_in_block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Statements_in_blockContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Statements_in_blockContext,i)


        def else_if_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Else_if_statementContext,0)


        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = MiniGoParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 541
            self.match(MiniGoParser.IF)
            self.state = 542
            self.match(MiniGoParser.LPAREN)
            self.state = 543
            self.expression(0)
            self.state = 544
            self.match(MiniGoParser.RPAREN)
            self.state = 545
            self.match(MiniGoParser.LBRACE)
            self.state = 547
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 546
                self.statements_in_block()


            self.state = 549
            self.match(MiniGoParser.RBRACE)
            self.state = 551
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.state = 550
                self.else_if_statement()


            self.state = 559
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 553
                self.match(MiniGoParser.ELSE)
                self.state = 554
                self.match(MiniGoParser.LBRACE)
                self.state = 556
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 555
                    self.statements_in_block()


                self.state = 558
                self.match(MiniGoParser.RBRACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def basic_for_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Basic_for_statementContext,0)


        def init_for_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Init_for_statementContext,0)


        def range_for_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Range_for_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = MiniGoParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 561
            self.match(MiniGoParser.FOR)
            self.state = 565
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.state = 562
                self.basic_for_statement()
                pass

            elif la_ == 2:
                self.state = 563
                self.init_for_statement()
                pass

            elif la_ == 3:
                self.state = 564
                self.range_for_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Basic_for_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def statements_in_block(self):
            return self.getTypedRuleContext(MiniGoParser.Statements_in_blockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_basic_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasic_for_statement" ):
                return visitor.visitBasic_for_statement(self)
            else:
                return visitor.visitChildren(self)




    def basic_for_statement(self):

        localctx = MiniGoParser.Basic_for_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_basic_for_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 567
            self.expression(0)
            self.state = 568
            self.match(MiniGoParser.LBRACE)
            self.state = 570
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 569
                self.statements_in_block()


            self.state = 572
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Update_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def SHORT_DECL(self):
            return self.getToken(MiniGoParser.SHORT_DECL, 0)

        def ADD_ASSIGN(self):
            return self.getToken(MiniGoParser.ADD_ASSIGN, 0)

        def SUB_ASSIGN(self):
            return self.getToken(MiniGoParser.SUB_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(MiniGoParser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(MiniGoParser.DIV_ASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_update_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdate_part" ):
                return visitor.visitUpdate_part(self)
            else:
                return visitor.visitChildren(self)




    def update_part(self):

        localctx = MiniGoParser.Update_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_update_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 574
            self.match(MiniGoParser.ID)
            self.state = 575
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.SHORT_DECL) | (1 << MiniGoParser.ADD_ASSIGN) | (1 << MiniGoParser.SUB_ASSIGN) | (1 << MiniGoParser.MUL_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 576
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_for_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def update_part(self):
            return self.getTypedRuleContext(MiniGoParser.Update_partContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMI)
            else:
                return self.getToken(MiniGoParser.SEMI, i)

        def statements_in_block(self):
            return self.getTypedRuleContext(MiniGoParser.Statements_in_blockContext,0)


        def SHORT_DECL(self):
            return self.getToken(MiniGoParser.SHORT_DECL, 0)

        def ADD_ASSIGN(self):
            return self.getToken(MiniGoParser.ADD_ASSIGN, 0)

        def SUB_ASSIGN(self):
            return self.getToken(MiniGoParser.SUB_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(MiniGoParser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(MiniGoParser.DIV_ASSIGN, 0)

        def type_return(self):
            return self.getTypedRuleContext(MiniGoParser.Type_returnContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_init_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit_for_statement" ):
                return visitor.visitInit_for_statement(self)
            else:
                return visitor.visitChildren(self)




    def init_for_statement(self):

        localctx = MiniGoParser.Init_for_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_init_for_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 588
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 578
                self.match(MiniGoParser.ID)
                self.state = 579
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.SHORT_DECL) | (1 << MiniGoParser.ADD_ASSIGN) | (1 << MiniGoParser.SUB_ASSIGN) | (1 << MiniGoParser.MUL_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 580
                self.expression(0)
                pass
            elif token in [MiniGoParser.VAR]:
                self.state = 581
                self.match(MiniGoParser.VAR)
                self.state = 582
                self.match(MiniGoParser.ID)
                self.state = 584
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 583
                    self.type_return()


                self.state = 586
                self.match(MiniGoParser.ASSIGN)
                self.state = 587
                self.expression(0)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 590
            self.match(MiniGoParser.SEMI)
            self.state = 591
            self.expression(0)

            self.state = 592
            self.match(MiniGoParser.SEMI)
            self.state = 593
            self.update_part()
            self.state = 594
            self.match(MiniGoParser.LBRACE)
            self.state = 596
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 595
                self.statements_in_block()


            self.state = 598
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Range_for_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def COMA(self):
            return self.getToken(MiniGoParser.COMA, 0)

        def SHORT_DECL(self):
            return self.getToken(MiniGoParser.SHORT_DECL, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literalContext,0)


        def statements_in_block(self):
            return self.getTypedRuleContext(MiniGoParser.Statements_in_blockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_range_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRange_for_statement" ):
                return visitor.visitRange_for_statement(self)
            else:
                return visitor.visitChildren(self)




    def range_for_statement(self):

        localctx = MiniGoParser.Range_for_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_range_for_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 600
            self.match(MiniGoParser.ID)
            self.state = 601
            self.match(MiniGoParser.COMA)
            self.state = 602
            self.match(MiniGoParser.ID)
            self.state = 603
            self.match(MiniGoParser.SHORT_DECL)
            self.state = 604
            self.match(MiniGoParser.RANGE)
            self.state = 609
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,62,self._ctx)
            if la_ == 1:
                self.state = 605
                self.lhs(0)
                pass

            elif la_ == 2:
                self.state = 606
                self.match(MiniGoParser.INT_LIT)
                pass

            elif la_ == 3:
                self.state = 607
                self.struct_literal()
                pass

            elif la_ == 4:
                self.state = 608
                self.array_literal()
                pass


            self.state = 611
            self.match(MiniGoParser.LBRACE)
            self.state = 613
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 612
                self.statements_in_block()


            self.state = 615
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = MiniGoParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 617
            self.match(MiniGoParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = MiniGoParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 619
            self.match(MiniGoParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def call_statement_1(self):
            return self.getTypedRuleContext(MiniGoParser.Call_statement_1Context,0)


        def call_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Call_statementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Call_statementContext,i)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def LBRACKET(self):
            return self.getToken(MiniGoParser.LBRACKET, 0)

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def RBRACKET(self):
            return self.getToken(MiniGoParser.RBRACKET, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_statement" ):
                return visitor.visitCall_statement(self)
            else:
                return visitor.visitChildren(self)



    def call_statement(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Call_statementContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 110
        self.enterRecursionRule(localctx, 110, self.RULE_call_statement, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 622
            self.call_statement_1()
            self._ctx.stop = self._input.LT(-1)
            self.state = 633
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,65,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 631
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Call_statementContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_call_statement)
                        self.state = 624
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 625
                        self.match(MiniGoParser.DOT)
                        self.state = 626
                        self.call_statement(4)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Call_statementContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_call_statement)
                        self.state = 627
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 628
                        self.match(MiniGoParser.LBRACKET)
                        self.state = 629
                        self.match(MiniGoParser.INT_LIT)
                        self.state = 630
                        self.match(MiniGoParser.RBRACKET)
                        pass

             
                self.state = 635
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,65,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Call_statement_1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_call_statement_1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_statement_1" ):
                return visitor.visitCall_statement_1(self)
            else:
                return visitor.visitChildren(self)




    def call_statement_1(self):

        localctx = MiniGoParser.Call_statement_1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_call_statement_1)
        try:
            self.state = 638
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 636
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 637
                self.func_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = MiniGoParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 640
            self.match(MiniGoParser.RETURN)
            self.state = 642
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 641
                self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[14] = self.array_lit_element_sempred
        self._predicates[16] = self.param_type_sempred
        self._predicates[29] = self.expression_sempred
        self._predicates[30] = self.expression1_sempred
        self._predicates[31] = self.expression2_sempred
        self._predicates[32] = self.expression3_sempred
        self._predicates[33] = self.expression4_sempred
        self._predicates[35] = self.expression6_sempred
        self._predicates[42] = self.lhs_sempred
        self._predicates[55] = self.call_statement_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def array_lit_element_sempred(self, localctx:Array_lit_elementContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def param_type_sempred(self, localctx:Param_typeContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expression1_sempred(self, localctx:Expression1Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expression2_sempred(self, localctx:Expression2Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expression3_sempred(self, localctx:Expression3Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def expression4_sempred(self, localctx:Expression4Context, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

    def expression6_sempred(self, localctx:Expression6Context, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         

    def lhs_sempred(self, localctx:LhsContext, predIndex:int):
            if predIndex == 10:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 2)
         

    def call_statement_sempred(self, localctx:Call_statementContext, predIndex:int):
            if predIndex == 12:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 2)
         




