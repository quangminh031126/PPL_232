# Generated from ./main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\64")
        buf.write("\u01f3\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\3\2\3\2\3\2\3\2\3\2\3\2\7\2\u0083")
        buf.write("\n\2\f\2\16\2\u0086\13\2\3\2\3\2\5\2\u008a\n\2\3\3\7\3")
        buf.write("\u008d\n\3\f\3\16\3\u0090\13\3\3\3\3\3\7\3\u0094\n\3\f")
        buf.write("\3\16\3\u0097\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\5\3\5\3\5\3\5\5\5\u00a7\n\5\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u00b9")
        buf.write("\n\6\3\7\3\7\5\7\u00bd\n\7\3\b\3\b\3\b\3\b\5\b\u00c3\n")
        buf.write("\b\3\t\3\t\5\t\u00c7\n\t\3\n\3\n\3\n\3\n\5\n\u00cd\n\n")
        buf.write("\3\13\3\13\5\13\u00d1\n\13\3\f\3\f\3\f\3\f\5\f\u00d7\n")
        buf.write("\f\3\r\3\r\5\r\u00db\n\r\3\16\3\16\3\16\3\16\3\16\5\16")
        buf.write("\u00e2\n\16\3\17\3\17\3\17\3\17\3\17\3\17\7\17\u00ea\n")
        buf.write("\17\f\17\16\17\u00ed\13\17\3\20\3\20\3\20\3\20\3\20\3")
        buf.write("\20\7\20\u00f5\n\20\f\20\16\20\u00f8\13\20\3\21\3\21\3")
        buf.write("\21\5\21\u00fd\n\21\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\7\23\u0107\n\23\f\23\16\23\u010a\13\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\7\24\u0112\n\24\f\24\16\24\u0115")
        buf.write("\13\24\3\25\3\25\3\25\5\25\u011a\n\25\3\26\3\26\3\27\3")
        buf.write("\27\3\27\5\27\u0121\n\27\3\27\3\27\3\27\7\27\u0126\n\27")
        buf.write("\f\27\16\27\u0129\13\27\3\30\3\30\5\30\u012d\n\30\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\5\36\u0143\n")
        buf.write("\36\3\37\3\37\3\37\3\37\3\37\5\37\u014a\n\37\3 \3 \3 ")
        buf.write("\3 \3 \3!\3!\5!\u0153\n!\3\"\3\"\3\"\3\"\3\"\5\"\u015a")
        buf.write("\n\"\3#\3#\3$\3$\3$\3$\3$\3$\3$\5$\u0165\n$\3$\6$\u0168")
        buf.write("\n$\r$\16$\u0169\3%\3%\3%\3%\5%\u0170\n%\3&\3&\5&\u0174")
        buf.write("\n&\3\'\3\'\3(\3(\3(\3)\3)\5)\u017d\n)\3*\3*\3*\3+\3+")
        buf.write("\3+\3+\3+\3+\5+\u0188\n+\3,\3,\5,\u018c\n,\3-\3-\3-\3")
        buf.write("-\3-\5-\u0193\n-\3.\3.\3.\3.\3.\3.\5.\u019b\n.\3/\3/\3")
        buf.write("/\3/\3/\3/\3/\3/\5/\u01a5\n/\3\60\3\60\3\60\5\60\u01aa")
        buf.write("\n\60\3\61\3\61\3\61\3\61\3\61\5\61\u01b1\n\61\3\62\3")
        buf.write("\62\5\62\u01b5\n\62\3\63\3\63\3\63\3\63\3\63\5\63\u01bc")
        buf.write("\n\63\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\67\3\67\38\38\3")
        buf.write("9\39\3:\3:\5:\u01d7\n:\3;\3;\3<\3<\6<\u01dd\n<\r<\16<")
        buf.write("\u01de\3<\3<\3<\6<\u01e4\n<\r<\16<\u01e5\3<\5<\u01e9\n")
        buf.write("<\3=\3=\3>\3>\3>\3>\5>\u01f1\n>\3>\2\7\34\36$&,?\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66")
        buf.write("8:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz\2\b\3\2\4\6\3\2\30")
        buf.write("\31\3\2\32\34\4\2,,//\4\2--//\4\2\35\35 $\2\u01f3\2|\3")
        buf.write("\2\2\2\4\u008e\3\2\2\2\6\u0098\3\2\2\2\b\u00a6\3\2\2\2")
        buf.write("\n\u00b8\3\2\2\2\f\u00bc\3\2\2\2\16\u00c2\3\2\2\2\20\u00c6")
        buf.write("\3\2\2\2\22\u00cc\3\2\2\2\24\u00d0\3\2\2\2\26\u00d6\3")
        buf.write("\2\2\2\30\u00da\3\2\2\2\32\u00e1\3\2\2\2\34\u00e3\3\2")
        buf.write("\2\2\36\u00ee\3\2\2\2 \u00fc\3\2\2\2\"\u00fe\3\2\2\2$")
        buf.write("\u0100\3\2\2\2&\u010b\3\2\2\2(\u0119\3\2\2\2*\u011b\3")
        buf.write("\2\2\2,\u0120\3\2\2\2.\u012c\3\2\2\2\60\u012e\3\2\2\2")
        buf.write("\62\u0132\3\2\2\2\64\u0136\3\2\2\2\66\u0138\3\2\2\28\u013a")
        buf.write("\3\2\2\2:\u0142\3\2\2\2<\u0149\3\2\2\2>\u014b\3\2\2\2")
        buf.write("@\u0152\3\2\2\2B\u0159\3\2\2\2D\u015b\3\2\2\2F\u0164\3")
        buf.write("\2\2\2H\u016f\3\2\2\2J\u0171\3\2\2\2L\u0175\3\2\2\2N\u0177")
        buf.write("\3\2\2\2P\u017a\3\2\2\2R\u017e\3\2\2\2T\u0187\3\2\2\2")
        buf.write("V\u018b\3\2\2\2X\u0192\3\2\2\2Z\u0194\3\2\2\2\\\u019c")
        buf.write("\3\2\2\2^\u01a9\3\2\2\2`\u01ab\3\2\2\2b\u01b4\3\2\2\2")
        buf.write("d\u01bb\3\2\2\2f\u01bd\3\2\2\2h\u01c1\3\2\2\2j\u01c5\3")
        buf.write("\2\2\2l\u01ce\3\2\2\2n\u01d0\3\2\2\2p\u01d2\3\2\2\2r\u01d4")
        buf.write("\3\2\2\2t\u01d8\3\2\2\2v\u01da\3\2\2\2x\u01ea\3\2\2\2")
        buf.write("z\u01f0\3\2\2\2|}\7\n\2\2}~\7\3\2\2~\177\7&\2\2\177\u0080")
        buf.write("\5V,\2\u0080\u0084\7\'\2\2\u0081\u0083\7+\2\2\u0082\u0081")
        buf.write("\3\2\2\2\u0083\u0086\3\2\2\2\u0084\u0082\3\2\2\2\u0084")
        buf.write("\u0085\3\2\2\2\u0085\u0089\3\2\2\2\u0086\u0084\3\2\2\2")
        buf.write("\u0087\u008a\5r:\2\u0088\u008a\5v<\2\u0089\u0087\3\2\2")
        buf.write("\2\u0089\u0088\3\2\2\2\u0089\u008a\3\2\2\2\u008a\3\3\2")
        buf.write("\2\2\u008b\u008d\5\\/\2\u008c\u008b\3\2\2\2\u008d\u0090")
        buf.write("\3\2\2\2\u008e\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f")
        buf.write("\u0091\3\2\2\2\u0090\u008e\3\2\2\2\u0091\u0095\5\2\2\2")
        buf.write("\u0092\u0094\5\\/\2\u0093\u0092\3\2\2\2\u0094\u0097\3")
        buf.write("\2\2\2\u0095\u0093\3\2\2\2\u0095\u0096\3\2\2\2\u0096\5")
        buf.write("\3\2\2\2\u0097\u0095\3\2\2\2\u0098\u0099\t\2\2\2\u0099")
        buf.write("\u009a\7/\2\2\u009a\u009b\7(\2\2\u009b\u009c\5\b\5\2\u009c")
        buf.write("\u009d\7)\2\2\u009d\u009e\7\36\2\2\u009e\u009f\7(\2\2")
        buf.write("\u009f\u00a0\5\n\6\2\u00a0\u00a1\7)\2\2\u00a1\7\3\2\2")
        buf.write("\2\u00a2\u00a3\7,\2\2\u00a3\u00a4\7*\2\2\u00a4\u00a7\5")
        buf.write("\b\5\2\u00a5\u00a7\7,\2\2\u00a6\u00a2\3\2\2\2\u00a6\u00a5")
        buf.write("\3\2\2\2\u00a7\t\3\2\2\2\u00a8\u00a9\7(\2\2\u00a9\u00aa")
        buf.write("\5\f\7\2\u00aa\u00ab\7)\2\2\u00ab\u00b9\3\2\2\2\u00ac")
        buf.write("\u00ad\7(\2\2\u00ad\u00ae\5\20\t\2\u00ae\u00af\7)\2\2")
        buf.write("\u00af\u00b9\3\2\2\2\u00b0\u00b1\7(\2\2\u00b1\u00b2\5")
        buf.write("\24\13\2\u00b2\u00b3\7)\2\2\u00b3\u00b9\3\2\2\2\u00b4")
        buf.write("\u00b5\7(\2\2\u00b5\u00b6\5\30\r\2\u00b6\u00b7\7)\2\2")
        buf.write("\u00b7\u00b9\3\2\2\2\u00b8\u00a8\3\2\2\2\u00b8\u00ac\3")
        buf.write("\2\2\2\u00b8\u00b0\3\2\2\2\u00b8\u00b4\3\2\2\2\u00b9\13")
        buf.write("\3\2\2\2\u00ba\u00bd\5\16\b\2\u00bb\u00bd\3\2\2\2\u00bc")
        buf.write("\u00ba\3\2\2\2\u00bc\u00bb\3\2\2\2\u00bd\r\3\2\2\2\u00be")
        buf.write("\u00bf\7,\2\2\u00bf\u00c0\7*\2\2\u00c0\u00c3\5\16\b\2")
        buf.write("\u00c1\u00c3\7,\2\2\u00c2\u00be\3\2\2\2\u00c2\u00c1\3")
        buf.write("\2\2\2\u00c3\17\3\2\2\2\u00c4\u00c7\5\22\n\2\u00c5\u00c7")
        buf.write("\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6\u00c5\3\2\2\2\u00c7")
        buf.write("\21\3\2\2\2\u00c8\u00c9\7-\2\2\u00c9\u00ca\7*\2\2\u00ca")
        buf.write("\u00cd\5\22\n\2\u00cb\u00cd\7-\2\2\u00cc\u00c8\3\2\2\2")
        buf.write("\u00cc\u00cb\3\2\2\2\u00cd\23\3\2\2\2\u00ce\u00d1\5\26")
        buf.write("\f\2\u00cf\u00d1\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d0\u00cf")
        buf.write("\3\2\2\2\u00d1\25\3\2\2\2\u00d2\u00d3\7.\2\2\u00d3\u00d4")
        buf.write("\7*\2\2\u00d4\u00d7\5\26\f\2\u00d5\u00d7\7.\2\2\u00d6")
        buf.write("\u00d2\3\2\2\2\u00d6\u00d5\3\2\2\2\u00d7\27\3\2\2\2\u00d8")
        buf.write("\u00db\5\32\16\2\u00d9\u00db\3\2\2\2\u00da\u00d8\3\2\2")
        buf.write("\2\u00da\u00d9\3\2\2\2\u00db\31\3\2\2\2\u00dc\u00dd\5")
        buf.write("\n\6\2\u00dd\u00de\7*\2\2\u00de\u00df\5\32\16\2\u00df")
        buf.write("\u00e2\3\2\2\2\u00e0\u00e2\5\n\6\2\u00e1\u00dc\3\2\2\2")
        buf.write("\u00e1\u00e0\3\2\2\2\u00e2\33\3\2\2\2\u00e3\u00e4\b\17")
        buf.write("\1\2\u00e4\u00e5\5\36\20\2\u00e5\u00eb\3\2\2\2\u00e6\u00e7")
        buf.write("\f\4\2\2\u00e7\u00e8\t\3\2\2\u00e8\u00ea\5\36\20\2\u00e9")
        buf.write("\u00e6\3\2\2\2\u00ea\u00ed\3\2\2\2\u00eb\u00e9\3\2\2\2")
        buf.write("\u00eb\u00ec\3\2\2\2\u00ec\35\3\2\2\2\u00ed\u00eb\3\2")
        buf.write("\2\2\u00ee\u00ef\b\20\1\2\u00ef\u00f0\5 \21\2\u00f0\u00f6")
        buf.write("\3\2\2\2\u00f1\u00f2\f\4\2\2\u00f2\u00f3\t\4\2\2\u00f3")
        buf.write("\u00f5\5 \21\2\u00f4\u00f1\3\2\2\2\u00f5\u00f8\3\2\2\2")
        buf.write("\u00f6\u00f4\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\37\3\2")
        buf.write("\2\2\u00f8\u00f6\3\2\2\2\u00f9\u00fa\7\31\2\2\u00fa\u00fd")
        buf.write("\5 \21\2\u00fb\u00fd\5\"\22\2\u00fc\u00f9\3\2\2\2\u00fc")
        buf.write("\u00fb\3\2\2\2\u00fd!\3\2\2\2\u00fe\u00ff\t\5\2\2\u00ff")
        buf.write("#\3\2\2\2\u0100\u0101\b\23\1\2\u0101\u0102\5&\24\2\u0102")
        buf.write("\u0108\3\2\2\2\u0103\u0104\f\4\2\2\u0104\u0105\7\27\2")
        buf.write("\2\u0105\u0107\5&\24\2\u0106\u0103\3\2\2\2\u0107\u010a")
        buf.write("\3\2\2\2\u0108\u0106\3\2\2\2\u0108\u0109\3\2\2\2\u0109")
        buf.write("%\3\2\2\2\u010a\u0108\3\2\2\2\u010b\u010c\b\24\1\2\u010c")
        buf.write("\u010d\5(\25\2\u010d\u0113\3\2\2\2\u010e\u010f\f\4\2\2")
        buf.write("\u010f\u0110\7\26\2\2\u0110\u0112\5(\25\2\u0111\u010e")
        buf.write("\3\2\2\2\u0112\u0115\3\2\2\2\u0113\u0111\3\2\2\2\u0113")
        buf.write("\u0114\3\2\2\2\u0114\'\3\2\2\2\u0115\u0113\3\2\2\2\u0116")
        buf.write("\u0117\7\25\2\2\u0117\u011a\5(\25\2\u0118\u011a\5*\26")
        buf.write("\2\u0119\u0116\3\2\2\2\u0119\u0118\3\2\2\2\u011a)\3\2")
        buf.write("\2\2\u011b\u011c\t\6\2\2\u011c+\3\2\2\2\u011d\u011e\b")
        buf.write("\27\1\2\u011e\u0121\7.\2\2\u011f\u0121\7/\2\2\u0120\u011d")
        buf.write("\3\2\2\2\u0120\u011f\3\2\2\2\u0121\u0127\3\2\2\2\u0122")
        buf.write("\u0123\f\5\2\2\u0123\u0124\7%\2\2\u0124\u0126\5,\27\6")
        buf.write("\u0125\u0122\3\2\2\2\u0126\u0129\3\2\2\2\u0127\u0125\3")
        buf.write("\2\2\2\u0127\u0128\3\2\2\2\u0128-\3\2\2\2\u0129\u0127")
        buf.write("\3\2\2\2\u012a\u012d\5\60\31\2\u012b\u012d\5\62\32\2\u012c")
        buf.write("\u012a\3\2\2\2\u012c\u012b\3\2\2\2\u012d/\3\2\2\2\u012e")
        buf.write("\u012f\5\34\17\2\u012f\u0130\5\64\33\2\u0130\u0131\5\34")
        buf.write("\17\2\u0131\61\3\2\2\2\u0132\u0133\5,\27\2\u0133\u0134")
        buf.write("\5\66\34\2\u0134\u0135\5,\27\2\u0135\63\3\2\2\2\u0136")
        buf.write("\u0137\t\7\2\2\u0137\65\3\2\2\2\u0138\u0139\7\37\2\2\u0139")
        buf.write("\67\3\2\2\2\u013a\u013b\5:\36\2\u013b\u013c\7(\2\2\u013c")
        buf.write("\u013d\5<\37\2\u013d\u013e\7)\2\2\u013e9\3\2\2\2\u013f")
        buf.write("\u0143\7/\2\2\u0140\u0143\5> \2\u0141\u0143\7,\2\2\u0142")
        buf.write("\u013f\3\2\2\2\u0142\u0140\3\2\2\2\u0142\u0141\3\2\2\2")
        buf.write("\u0143;\3\2\2\2\u0144\u0145\5:\36\2\u0145\u0146\7*\2\2")
        buf.write("\u0146\u0147\5<\37\2\u0147\u014a\3\2\2\2\u0148\u014a\5")
        buf.write(":\36\2\u0149\u0144\3\2\2\2\u0149\u0148\3\2\2\2\u014a=")
        buf.write("\3\2\2\2\u014b\u014c\7/\2\2\u014c\u014d\7&\2\2\u014d\u014e")
        buf.write("\5@!\2\u014e\u014f\7\'\2\2\u014f?\3\2\2\2\u0150\u0153")
        buf.write("\5B\"\2\u0151\u0153\3\2\2\2\u0152\u0150\3\2\2\2\u0152")
        buf.write("\u0151\3\2\2\2\u0153A\3\2\2\2\u0154\u0155\5D#\2\u0155")
        buf.write("\u0156\7*\2\2\u0156\u0157\5B\"\2\u0157\u015a\3\2\2\2\u0158")
        buf.write("\u015a\5D#\2\u0159\u0154\3\2\2\2\u0159\u0158\3\2\2\2\u015a")
        buf.write("C\3\2\2\2\u015b\u015c\5T+\2\u015cE\3\2\2\2\u015d\u0165")
        buf.write("\5t;\2\u015e\u0165\5p9\2\u015f\u0165\5r:\2\u0160\u0165")
        buf.write("\5n8\2\u0161\u0165\5v<\2\u0162\u0165\5`\61\2\u0163\u0165")
        buf.write("\5j\66\2\u0164\u015d\3\2\2\2\u0164\u015e\3\2\2\2\u0164")
        buf.write("\u015f\3\2\2\2\u0164\u0160\3\2\2\2\u0164\u0161\3\2\2\2")
        buf.write("\u0164\u0162\3\2\2\2\u0164\u0163\3\2\2\2\u0165\u0167\3")
        buf.write("\2\2\2\u0166\u0168\7+\2\2\u0167\u0166\3\2\2\2\u0168\u0169")
        buf.write("\3\2\2\2\u0169\u0167\3\2\2\2\u0169\u016a\3\2\2\2\u016a")
        buf.write("G\3\2\2\2\u016b\u0170\5J&\2\u016c\u0170\5\6\4\2\u016d")
        buf.write("\u0170\5N(\2\u016e\u0170\5P)\2\u016f\u016b\3\2\2\2\u016f")
        buf.write("\u016c\3\2\2\2\u016f\u016d\3\2\2\2\u016f\u016e\3\2\2\2")
        buf.write("\u0170I\3\2\2\2\u0171\u0173\5L\'\2\u0172\u0174\5R*\2\u0173")
        buf.write("\u0172\3\2\2\2\u0173\u0174\3\2\2\2\u0174K\3\2\2\2\u0175")
        buf.write("\u0176\t\2\2\2\u0176M\3\2\2\2\u0177\u0178\7\b\2\2\u0178")
        buf.write("\u0179\5R*\2\u0179O\3\2\2\2\u017a\u017c\7\t\2\2\u017b")
        buf.write("\u017d\5R*\2\u017c\u017b\3\2\2\2\u017c\u017d\3\2\2\2\u017d")
        buf.write("Q\3\2\2\2\u017e\u017f\7\36\2\2\u017f\u0180\5T+\2\u0180")
        buf.write("S\3\2\2\2\u0181\u0188\5\34\17\2\u0182\u0188\5,\27\2\u0183")
        buf.write("\u0188\5.\30\2\u0184\u0188\5$\23\2\u0185\u0188\58\35\2")
        buf.write("\u0186\u0188\5> \2\u0187\u0181\3\2\2\2\u0187\u0182\3\2")
        buf.write("\2\2\u0187\u0183\3\2\2\2\u0187\u0184\3\2\2\2\u0187\u0185")
        buf.write("\3\2\2\2\u0187\u0186\3\2\2\2\u0188U\3\2\2\2\u0189\u018c")
        buf.write("\5X-\2\u018a\u018c\3\2\2\2\u018b\u0189\3\2\2\2\u018b\u018a")
        buf.write("\3\2\2\2\u018cW\3\2\2\2\u018d\u018e\5Z.\2\u018e\u018f")
        buf.write("\7*\2\2\u018f\u0190\5X-\2\u0190\u0193\3\2\2\2\u0191\u0193")
        buf.write("\5Z.\2\u0192\u018d\3\2\2\2\u0192\u0191\3\2\2\2\u0193Y")
        buf.write("\3\2\2\2\u0194\u0195\5L\'\2\u0195\u019a\7/\2\2\u0196\u0197")
        buf.write("\7(\2\2\u0197\u0198\5\b\5\2\u0198\u0199\7)\2\2\u0199\u019b")
        buf.write("\3\2\2\2\u019a\u0196\3\2\2\2\u019a\u019b\3\2\2\2\u019b")
        buf.write("[\3\2\2\2\u019c\u019d\7\n\2\2\u019d\u019e\7/\2\2\u019e")
        buf.write("\u019f\7&\2\2\u019f\u01a0\5V,\2\u01a0\u01a1\7\'\2\2\u01a1")
        buf.write("\u01a4\5^\60\2\u01a2\u01a5\5r:\2\u01a3\u01a5\5v<\2\u01a4")
        buf.write("\u01a2\3\2\2\2\u01a4\u01a3\3\2\2\2\u01a4\u01a5\3\2\2\2")
        buf.write("\u01a5]\3\2\2\2\u01a6\u01a7\7+\2\2\u01a7\u01aa\5^\60\2")
        buf.write("\u01a8\u01aa\3\2\2\2\u01a9\u01a6\3\2\2\2\u01a9\u01a8\3")
        buf.write("\2\2\2\u01aa_\3\2\2\2\u01ab\u01ac\7\20\2\2\u01ac\u01ad")
        buf.write("\5$\23\2\u01ad\u01ae\5F$\2\u01ae\u01b0\5b\62\2\u01af\u01b1")
        buf.write("\5h\65\2\u01b0\u01af\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1")
        buf.write("a\3\2\2\2\u01b2\u01b5\5d\63\2\u01b3\u01b5\3\2\2\2\u01b4")
        buf.write("\u01b2\3\2\2\2\u01b4\u01b3\3\2\2\2\u01b5c\3\2\2\2\u01b6")
        buf.write("\u01b7\5f\64\2\u01b7\u01b8\5^\60\2\u01b8\u01b9\5d\63\2")
        buf.write("\u01b9\u01bc\3\2\2\2\u01ba\u01bc\5f\64\2\u01bb\u01b6\3")
        buf.write("\2\2\2\u01bb\u01ba\3\2\2\2\u01bce\3\2\2\2\u01bd\u01be")
        buf.write("\7\22\2\2\u01be\u01bf\5$\23\2\u01bf\u01c0\5F$\2\u01c0")
        buf.write("g\3\2\2\2\u01c1\u01c2\7\21\2\2\u01c2\u01c3\5$\23\2\u01c3")
        buf.write("\u01c4\5F$\2\u01c4i\3\2\2\2\u01c5\u01c6\7\13\2\2\u01c6")
        buf.write("\u01c7\7/\2\2\u01c7\u01c8\7\f\2\2\u01c8\u01c9\5$\23\2")
        buf.write("\u01c9\u01ca\7\r\2\2\u01ca\u01cb\5l\67\2\u01cb\u01cc\5")
        buf.write("^\60\2\u01cc\u01cd\5F$\2\u01cdk\3\2\2\2\u01ce\u01cf\5")
        buf.write("T+\2\u01cfm\3\2\2\2\u01d0\u01d1\7\16\2\2\u01d1o\3\2\2")
        buf.write("\2\u01d2\u01d3\7\17\2\2\u01d3q\3\2\2\2\u01d4\u01d6\7\7")
        buf.write("\2\2\u01d5\u01d7\5T+\2\u01d6\u01d5\3\2\2\2\u01d6\u01d7")
        buf.write("\3\2\2\2\u01d7s\3\2\2\2\u01d8\u01d9\5> \2\u01d9u\3\2\2")
        buf.write("\2\u01da\u01dc\7\23\2\2\u01db\u01dd\7+\2\2\u01dc\u01db")
        buf.write("\3\2\2\2\u01dd\u01de\3\2\2\2\u01de\u01dc\3\2\2\2\u01de")
        buf.write("\u01df\3\2\2\2\u01df\u01e0\3\2\2\2\u01e0\u01e1\5x=\2\u01e1")
        buf.write("\u01e8\7\24\2\2\u01e2\u01e4\7+\2\2\u01e3\u01e2\3\2\2\2")
        buf.write("\u01e4\u01e5\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e5\u01e6\3")
        buf.write("\2\2\2\u01e6\u01e9\3\2\2\2\u01e7\u01e9\7\2\2\3\u01e8\u01e3")
        buf.write("\3\2\2\2\u01e8\u01e7\3\2\2\2\u01e9w\3\2\2\2\u01ea\u01eb")
        buf.write("\5z>\2\u01eby\3\2\2\2\u01ec\u01ed\5F$\2\u01ed\u01ee\5")
        buf.write("z>\2\u01ee\u01f1\3\2\2\2\u01ef\u01f1\3\2\2\2\u01f0\u01ec")
        buf.write("\3\2\2\2\u01f0\u01ef\3\2\2\2\u01f1{\3\2\2\2\60\u0084\u0089")
        buf.write("\u008e\u0095\u00a6\u00b8\u00bc\u00c2\u00c6\u00cc\u00d0")
        buf.write("\u00d6\u00da\u00e1\u00eb\u00f6\u00fc\u0108\u0113\u0119")
        buf.write("\u0120\u0127\u012c\u0142\u0149\u0152\u0159\u0164\u0169")
        buf.write("\u016f\u0173\u017c\u0187\u018b\u0192\u019a\u01a4\u01a9")
        buf.write("\u01b0\u01b4\u01bb\u01d6\u01de\u01e5\u01e8\u01f0")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "'number'", "'bool'", "'string'", 
                     "'return'", "'var'", "'dynamic'", "'func'", "'for'", 
                     "'until'", "'by'", "'break'", "'continue'", "'if'", 
                     "'else'", "'elif'", "'begin'", "'end'", "'not'", "'and'", 
                     "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", "'='", "'<-'", 
                     "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'...'", 
                     "'('", "')'", "'['", "']'", "','", "'\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "NUMBER", "BOOL", "STRING", 
                      "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", 
                      "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", 
                      "END", "NOT", "AND", "OR", "PLUS", "MINUS", "MULT", 
                      "DIV", "MOD", "EQUAL", "LEFTARR", "EQUALEQUAL", "NOTEQUAL", 
                      "LESS", "GREATER", "LESSOREQUAL", "GREATEROREQUAL", 
                      "ELLIPSIS", "LBracket", "RBracket", "LSBracket", "RSBracket", 
                      "COMMA", "NEWLINE", "NumberLit", "BooleanLit", "StringLit", 
                      "IDENTIFIER", "COMMENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_mainFunction = 0
    RULE_program = 1
    RULE_arrayDeclaration = 2
    RULE_arrayDim = 3
    RULE_arrayInit = 4
    RULE_numberList = 5
    RULE_numberPrime = 6
    RULE_boolList = 7
    RULE_boolPrime = 8
    RULE_stringList = 9
    RULE_stringPrime = 10
    RULE_arrayList = 11
    RULE_arrayPrime = 12
    RULE_arithExpr = 13
    RULE_arithExpr1 = 14
    RULE_arithExpr2 = 15
    RULE_arithExpr3 = 16
    RULE_logicExpr = 17
    RULE_logicExpr1 = 18
    RULE_logicExpr2 = 19
    RULE_logicExpr3 = 20
    RULE_stringConcatExpr = 21
    RULE_relExpr = 22
    RULE_arithComp = 23
    RULE_literalComp = 24
    RULE_arithRelOp = 25
    RULE_literalOp = 26
    RULE_elementAccessExpr = 27
    RULE_arrExpr = 28
    RULE_indexOp = 29
    RULE_functionCall = 30
    RULE_functionArgsList = 31
    RULE_argsPrime = 32
    RULE_arg = 33
    RULE_statement = 34
    RULE_variableDeclaration = 35
    RULE_normalDeclaration = 36
    RULE_varType = 37
    RULE_varDecl = 38
    RULE_dynamicDecl = 39
    RULE_variableInitialization = 40
    RULE_expression = 41
    RULE_paramDeclList = 42
    RULE_paramDeclPrime = 43
    RULE_paramDeclAtom = 44
    RULE_function = 45
    RULE_nullableListOfNEWLINE = 46
    RULE_ifStatement = 47
    RULE_elifStatementList = 48
    RULE_elifStatementPrime = 49
    RULE_elifStatement = 50
    RULE_elseStatement = 51
    RULE_forStatement = 52
    RULE_updateExpr = 53
    RULE_breakStatement = 54
    RULE_continueStatement = 55
    RULE_returnStatement = 56
    RULE_functionCallStatement = 57
    RULE_blockStatement = 58
    RULE_blockStatementBody = 59
    RULE_nullableListOfStatement = 60

    ruleNames =  [ "mainFunction", "program", "arrayDeclaration", "arrayDim", 
                   "arrayInit", "numberList", "numberPrime", "boolList", 
                   "boolPrime", "stringList", "stringPrime", "arrayList", 
                   "arrayPrime", "arithExpr", "arithExpr1", "arithExpr2", 
                   "arithExpr3", "logicExpr", "logicExpr1", "logicExpr2", 
                   "logicExpr3", "stringConcatExpr", "relExpr", "arithComp", 
                   "literalComp", "arithRelOp", "literalOp", "elementAccessExpr", 
                   "arrExpr", "indexOp", "functionCall", "functionArgsList", 
                   "argsPrime", "arg", "statement", "variableDeclaration", 
                   "normalDeclaration", "varType", "varDecl", "dynamicDecl", 
                   "variableInitialization", "expression", "paramDeclList", 
                   "paramDeclPrime", "paramDeclAtom", "function", "nullableListOfNEWLINE", 
                   "ifStatement", "elifStatementList", "elifStatementPrime", 
                   "elifStatement", "elseStatement", "forStatement", "updateExpr", 
                   "breakStatement", "continueStatement", "returnStatement", 
                   "functionCallStatement", "blockStatement", "blockStatementBody", 
                   "nullableListOfStatement" ]

    EOF = Token.EOF
    T__0=1
    NUMBER=2
    BOOL=3
    STRING=4
    RETURN=5
    VAR=6
    DYNAMIC=7
    FUNC=8
    FOR=9
    UNTIL=10
    BY=11
    BREAK=12
    CONTINUE=13
    IF=14
    ELSE=15
    ELIF=16
    BEGIN=17
    END=18
    NOT=19
    AND=20
    OR=21
    PLUS=22
    MINUS=23
    MULT=24
    DIV=25
    MOD=26
    EQUAL=27
    LEFTARR=28
    EQUALEQUAL=29
    NOTEQUAL=30
    LESS=31
    GREATER=32
    LESSOREQUAL=33
    GREATEROREQUAL=34
    ELLIPSIS=35
    LBracket=36
    RBracket=37
    LSBracket=38
    RSBracket=39
    COMMA=40
    NEWLINE=41
    NumberLit=42
    BooleanLit=43
    StringLit=44
    IDENTIFIER=45
    COMMENT=46
    WS=47
    ERROR_CHAR=48
    UNCLOSE_STRING=49
    ILLEGAL_ESCAPE=50

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class MainFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def LBracket(self):
            return self.getToken(ZCodeParser.LBracket, 0)

        def paramDeclList(self):
            return self.getTypedRuleContext(ZCodeParser.ParamDeclListContext,0)


        def RBracket(self):
            return self.getToken(ZCodeParser.RBracket, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def returnStatement(self):
            return self.getTypedRuleContext(ZCodeParser.ReturnStatementContext,0)


        def blockStatement(self):
            return self.getTypedRuleContext(ZCodeParser.BlockStatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_mainFunction

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMainFunction" ):
                return visitor.visitMainFunction(self)
            else:
                return visitor.visitChildren(self)




    def mainFunction(self):

        localctx = ZCodeParser.MainFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_mainFunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(ZCodeParser.FUNC)
            self.state = 123
            self.match(ZCodeParser.T__0)
            self.state = 124
            self.match(ZCodeParser.LBracket)
            self.state = 125
            self.paramDeclList()
            self.state = 126
            self.match(ZCodeParser.RBracket)
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 127
                self.match(ZCodeParser.NEWLINE)
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 135
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN]:
                self.state = 133
                self.returnStatement()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.state = 134
                self.blockStatement()
                pass
            elif token in [ZCodeParser.EOF, ZCodeParser.FUNC]:
                pass
            else:
                pass
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mainFunction(self):
            return self.getTypedRuleContext(ZCodeParser.MainFunctionContext,0)


        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.FunctionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.FunctionContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 137
                    self.function() 
                self.state = 142
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 143
            self.mainFunction()
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.FUNC:
                self.state = 144
                self.function()
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LSBracket(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.LSBracket)
            else:
                return self.getToken(ZCodeParser.LSBracket, i)

        def arrayDim(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayDimContext,0)


        def RSBracket(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.RSBracket)
            else:
                return self.getToken(ZCodeParser.RSBracket, i)

        def LEFTARR(self):
            return self.getToken(ZCodeParser.LEFTARR, 0)

        def arrayInit(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayInitContext,0)


        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayDeclaration" ):
                return visitor.visitArrayDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def arrayDeclaration(self):

        localctx = ZCodeParser.ArrayDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_arrayDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 151
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 152
            self.match(ZCodeParser.LSBracket)
            self.state = 153
            self.arrayDim()
            self.state = 154
            self.match(ZCodeParser.RSBracket)
            self.state = 155
            self.match(ZCodeParser.LEFTARR)
            self.state = 156
            self.match(ZCodeParser.LSBracket)
            self.state = 157
            self.arrayInit()
            self.state = 158
            self.match(ZCodeParser.RSBracket)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayDimContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NumberLit(self):
            return self.getToken(ZCodeParser.NumberLit, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def arrayDim(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayDimContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayDim

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayDim" ):
                return visitor.visitArrayDim(self)
            else:
                return visitor.visitChildren(self)




    def arrayDim(self):

        localctx = ZCodeParser.ArrayDimContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_arrayDim)
        try:
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.match(ZCodeParser.NumberLit)
                self.state = 161
                self.match(ZCodeParser.COMMA)
                self.state = 162
                self.arrayDim()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.match(ZCodeParser.NumberLit)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSBracket(self):
            return self.getToken(ZCodeParser.LSBracket, 0)

        def numberList(self):
            return self.getTypedRuleContext(ZCodeParser.NumberListContext,0)


        def RSBracket(self):
            return self.getToken(ZCodeParser.RSBracket, 0)

        def boolList(self):
            return self.getTypedRuleContext(ZCodeParser.BoolListContext,0)


        def stringList(self):
            return self.getTypedRuleContext(ZCodeParser.StringListContext,0)


        def arrayList(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayListContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayInit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayInit" ):
                return visitor.visitArrayInit(self)
            else:
                return visitor.visitChildren(self)




    def arrayInit(self):

        localctx = ZCodeParser.ArrayInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_arrayInit)
        try:
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.match(ZCodeParser.LSBracket)
                self.state = 167
                self.numberList()
                self.state = 168
                self.match(ZCodeParser.RSBracket)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.match(ZCodeParser.LSBracket)
                self.state = 171
                self.boolList()
                self.state = 172
                self.match(ZCodeParser.RSBracket)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 174
                self.match(ZCodeParser.LSBracket)
                self.state = 175
                self.stringList()
                self.state = 176
                self.match(ZCodeParser.RSBracket)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 178
                self.match(ZCodeParser.LSBracket)
                self.state = 179
                self.arrayList()
                self.state = 180
                self.match(ZCodeParser.RSBracket)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numberPrime(self):
            return self.getTypedRuleContext(ZCodeParser.NumberPrimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_numberList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberList" ):
                return visitor.visitNumberList(self)
            else:
                return visitor.visitChildren(self)




    def numberList(self):

        localctx = ZCodeParser.NumberListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_numberList)
        try:
            self.state = 186
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NumberLit]:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.numberPrime()
                pass
            elif token in [ZCodeParser.RSBracket]:
                self.enterOuterAlt(localctx, 2)

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


    class NumberPrimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NumberLit(self):
            return self.getToken(ZCodeParser.NumberLit, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def numberPrime(self):
            return self.getTypedRuleContext(ZCodeParser.NumberPrimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_numberPrime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberPrime" ):
                return visitor.visitNumberPrime(self)
            else:
                return visitor.visitChildren(self)




    def numberPrime(self):

        localctx = ZCodeParser.NumberPrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_numberPrime)
        try:
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.match(ZCodeParser.NumberLit)
                self.state = 189
                self.match(ZCodeParser.COMMA)
                self.state = 190
                self.numberPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self.match(ZCodeParser.NumberLit)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolPrime(self):
            return self.getTypedRuleContext(ZCodeParser.BoolPrimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_boolList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolList" ):
                return visitor.visitBoolList(self)
            else:
                return visitor.visitChildren(self)




    def boolList(self):

        localctx = ZCodeParser.BoolListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_boolList)
        try:
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BooleanLit]:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.boolPrime()
                pass
            elif token in [ZCodeParser.RSBracket]:
                self.enterOuterAlt(localctx, 2)

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


    class BoolPrimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BooleanLit(self):
            return self.getToken(ZCodeParser.BooleanLit, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def boolPrime(self):
            return self.getTypedRuleContext(ZCodeParser.BoolPrimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_boolPrime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolPrime" ):
                return visitor.visitBoolPrime(self)
            else:
                return visitor.visitChildren(self)




    def boolPrime(self):

        localctx = ZCodeParser.BoolPrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_boolPrime)
        try:
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.match(ZCodeParser.BooleanLit)
                self.state = 199
                self.match(ZCodeParser.COMMA)
                self.state = 200
                self.boolPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.match(ZCodeParser.BooleanLit)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stringPrime(self):
            return self.getTypedRuleContext(ZCodeParser.StringPrimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stringList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringList" ):
                return visitor.visitStringList(self)
            else:
                return visitor.visitChildren(self)




    def stringList(self):

        localctx = ZCodeParser.StringListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_stringList)
        try:
            self.state = 206
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.StringLit]:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.stringPrime()
                pass
            elif token in [ZCodeParser.RSBracket]:
                self.enterOuterAlt(localctx, 2)

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


    class StringPrimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def StringLit(self):
            return self.getToken(ZCodeParser.StringLit, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def stringPrime(self):
            return self.getTypedRuleContext(ZCodeParser.StringPrimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stringPrime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringPrime" ):
                return visitor.visitStringPrime(self)
            else:
                return visitor.visitChildren(self)




    def stringPrime(self):

        localctx = ZCodeParser.StringPrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_stringPrime)
        try:
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.match(ZCodeParser.StringLit)
                self.state = 209
                self.match(ZCodeParser.COMMA)
                self.state = 210
                self.stringPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 211
                self.match(ZCodeParser.StringLit)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayPrime(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayPrimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayList" ):
                return visitor.visitArrayList(self)
            else:
                return visitor.visitChildren(self)




    def arrayList(self):

        localctx = ZCodeParser.ArrayListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_arrayList)
        try:
            self.state = 216
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LSBracket]:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.arrayPrime()
                pass
            elif token in [ZCodeParser.RSBracket]:
                self.enterOuterAlt(localctx, 2)

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


    class ArrayPrimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayInit(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayInitContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def arrayPrime(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayPrimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayPrime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayPrime" ):
                return visitor.visitArrayPrime(self)
            else:
                return visitor.visitChildren(self)




    def arrayPrime(self):

        localctx = ZCodeParser.ArrayPrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_arrayPrime)
        try:
            self.state = 223
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.arrayInit()
                self.state = 219
                self.match(ZCodeParser.COMMA)
                self.state = 220
                self.arrayPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                self.arrayInit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithExpr1(self):
            return self.getTypedRuleContext(ZCodeParser.ArithExpr1Context,0)


        def arithExpr(self):
            return self.getTypedRuleContext(ZCodeParser.ArithExprContext,0)


        def PLUS(self):
            return self.getToken(ZCodeParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arithExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithExpr" ):
                return visitor.visitArithExpr(self)
            else:
                return visitor.visitChildren(self)



    def arithExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.ArithExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_arithExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.arithExpr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 233
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.ArithExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_arithExpr)
                    self.state = 228
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 229
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.PLUS or _la==ZCodeParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 230
                    self.arithExpr1(0) 
                self.state = 235
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ArithExpr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithExpr2(self):
            return self.getTypedRuleContext(ZCodeParser.ArithExpr2Context,0)


        def arithExpr1(self):
            return self.getTypedRuleContext(ZCodeParser.ArithExpr1Context,0)


        def MULT(self):
            return self.getToken(ZCodeParser.MULT, 0)

        def DIV(self):
            return self.getToken(ZCodeParser.DIV, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arithExpr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithExpr1" ):
                return visitor.visitArithExpr1(self)
            else:
                return visitor.visitChildren(self)



    def arithExpr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.ArithExpr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_arithExpr1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.arithExpr2()
            self._ctx.stop = self._input.LT(-1)
            self.state = 244
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.ArithExpr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_arithExpr1)
                    self.state = 239
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 240
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MULT) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 241
                    self.arithExpr2() 
                self.state = 246
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ArithExpr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def arithExpr2(self):
            return self.getTypedRuleContext(ZCodeParser.ArithExpr2Context,0)


        def arithExpr3(self):
            return self.getTypedRuleContext(ZCodeParser.ArithExpr3Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arithExpr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithExpr2" ):
                return visitor.visitArithExpr2(self)
            else:
                return visitor.visitChildren(self)




    def arithExpr2(self):

        localctx = ZCodeParser.ArithExpr2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_arithExpr2)
        try:
            self.state = 250
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.match(ZCodeParser.MINUS)
                self.state = 248
                self.arithExpr2()
                pass
            elif token in [ZCodeParser.NumberLit, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 249
                self.arithExpr3()
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


    class ArithExpr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def NumberLit(self):
            return self.getToken(ZCodeParser.NumberLit, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arithExpr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithExpr3" ):
                return visitor.visitArithExpr3(self)
            else:
                return visitor.visitChildren(self)




    def arithExpr3(self):

        localctx = ZCodeParser.ArithExpr3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_arithExpr3)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.NumberLit or _la==ZCodeParser.IDENTIFIER):
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


    class LogicExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicExpr1(self):
            return self.getTypedRuleContext(ZCodeParser.LogicExpr1Context,0)


        def logicExpr(self):
            return self.getTypedRuleContext(ZCodeParser.LogicExprContext,0)


        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_logicExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicExpr" ):
                return visitor.visitLogicExpr(self)
            else:
                return visitor.visitChildren(self)



    def logicExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.LogicExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_logicExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.logicExpr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 262
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.LogicExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicExpr)
                    self.state = 257
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 258
                    self.match(ZCodeParser.OR)
                    self.state = 259
                    self.logicExpr1(0) 
                self.state = 264
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LogicExpr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicExpr2(self):
            return self.getTypedRuleContext(ZCodeParser.LogicExpr2Context,0)


        def logicExpr1(self):
            return self.getTypedRuleContext(ZCodeParser.LogicExpr1Context,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_logicExpr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicExpr1" ):
                return visitor.visitLogicExpr1(self)
            else:
                return visitor.visitChildren(self)



    def logicExpr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.LogicExpr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_logicExpr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.logicExpr2()
            self._ctx.stop = self._input.LT(-1)
            self.state = 273
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.LogicExpr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicExpr1)
                    self.state = 268
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 269
                    self.match(ZCodeParser.AND)
                    self.state = 270
                    self.logicExpr2() 
                self.state = 275
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LogicExpr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def logicExpr2(self):
            return self.getTypedRuleContext(ZCodeParser.LogicExpr2Context,0)


        def logicExpr3(self):
            return self.getTypedRuleContext(ZCodeParser.LogicExpr3Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_logicExpr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicExpr2" ):
                return visitor.visitLogicExpr2(self)
            else:
                return visitor.visitChildren(self)




    def logicExpr2(self):

        localctx = ZCodeParser.LogicExpr2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_logicExpr2)
        try:
            self.state = 279
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.match(ZCodeParser.NOT)
                self.state = 277
                self.logicExpr2()
                pass
            elif token in [ZCodeParser.BooleanLit, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 278
                self.logicExpr3()
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


    class LogicExpr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BooleanLit(self):
            return self.getToken(ZCodeParser.BooleanLit, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_logicExpr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicExpr3" ):
                return visitor.visitLogicExpr3(self)
            else:
                return visitor.visitChildren(self)




    def logicExpr3(self):

        localctx = ZCodeParser.LogicExpr3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_logicExpr3)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.BooleanLit or _la==ZCodeParser.IDENTIFIER):
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


    class StringConcatExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def StringLit(self):
            return self.getToken(ZCodeParser.StringLit, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def stringConcatExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StringConcatExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StringConcatExprContext,i)


        def ELLIPSIS(self):
            return self.getToken(ZCodeParser.ELLIPSIS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_stringConcatExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringConcatExpr" ):
                return visitor.visitStringConcatExpr(self)
            else:
                return visitor.visitChildren(self)



    def stringConcatExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.StringConcatExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_stringConcatExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.StringLit]:
                self.state = 284
                self.match(ZCodeParser.StringLit)
                pass
            elif token in [ZCodeParser.IDENTIFIER]:
                self.state = 285
                self.match(ZCodeParser.IDENTIFIER)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 293
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.StringConcatExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_stringConcatExpr)
                    self.state = 288
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 289
                    self.match(ZCodeParser.ELLIPSIS)
                    self.state = 290
                    self.stringConcatExpr(4) 
                self.state = 295
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class RelExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithComp(self):
            return self.getTypedRuleContext(ZCodeParser.ArithCompContext,0)


        def literalComp(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralCompContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_relExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelExpr" ):
                return visitor.visitRelExpr(self)
            else:
                return visitor.visitChildren(self)




    def relExpr(self):

        localctx = ZCodeParser.RelExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_relExpr)
        try:
            self.state = 298
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.arithComp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 297
                self.literalComp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithCompContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ArithExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ArithExprContext,i)


        def arithRelOp(self):
            return self.getTypedRuleContext(ZCodeParser.ArithRelOpContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arithComp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithComp" ):
                return visitor.visitArithComp(self)
            else:
                return visitor.visitChildren(self)




    def arithComp(self):

        localctx = ZCodeParser.ArithCompContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_arithComp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.arithExpr(0)
            self.state = 301
            self.arithRelOp()
            self.state = 302
            self.arithExpr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralCompContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stringConcatExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StringConcatExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StringConcatExprContext,i)


        def literalOp(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralOpContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_literalComp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralComp" ):
                return visitor.visitLiteralComp(self)
            else:
                return visitor.visitChildren(self)




    def literalComp(self):

        localctx = ZCodeParser.LiteralCompContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_literalComp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.stringConcatExpr(0)
            self.state = 305
            self.literalOp()
            self.state = 306
            self.stringConcatExpr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithRelOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(ZCodeParser.EQUAL, 0)

        def NOTEQUAL(self):
            return self.getToken(ZCodeParser.NOTEQUAL, 0)

        def LESS(self):
            return self.getToken(ZCodeParser.LESS, 0)

        def GREATER(self):
            return self.getToken(ZCodeParser.GREATER, 0)

        def LESSOREQUAL(self):
            return self.getToken(ZCodeParser.LESSOREQUAL, 0)

        def GREATEROREQUAL(self):
            return self.getToken(ZCodeParser.GREATEROREQUAL, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arithRelOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithRelOp" ):
                return visitor.visitArithRelOp(self)
            else:
                return visitor.visitChildren(self)




    def arithRelOp(self):

        localctx = ZCodeParser.ArithRelOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_arithRelOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQUAL) | (1 << ZCodeParser.NOTEQUAL) | (1 << ZCodeParser.LESS) | (1 << ZCodeParser.GREATER) | (1 << ZCodeParser.LESSOREQUAL) | (1 << ZCodeParser.GREATEROREQUAL))) != 0)):
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


    class LiteralOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUALEQUAL(self):
            return self.getToken(ZCodeParser.EQUALEQUAL, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_literalOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralOp" ):
                return visitor.visitLiteralOp(self)
            else:
                return visitor.visitChildren(self)




    def literalOp(self):

        localctx = ZCodeParser.LiteralOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_literalOp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.match(ZCodeParser.EQUALEQUAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementAccessExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrExpr(self):
            return self.getTypedRuleContext(ZCodeParser.ArrExprContext,0)


        def LSBracket(self):
            return self.getToken(ZCodeParser.LSBracket, 0)

        def indexOp(self):
            return self.getTypedRuleContext(ZCodeParser.IndexOpContext,0)


        def RSBracket(self):
            return self.getToken(ZCodeParser.RSBracket, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_elementAccessExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElementAccessExpr" ):
                return visitor.visitElementAccessExpr(self)
            else:
                return visitor.visitChildren(self)




    def elementAccessExpr(self):

        localctx = ZCodeParser.ElementAccessExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_elementAccessExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.arrExpr()
            self.state = 313
            self.match(ZCodeParser.LSBracket)
            self.state = 314
            self.indexOp()
            self.state = 315
            self.match(ZCodeParser.RSBracket)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def functionCall(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionCallContext,0)


        def NumberLit(self):
            return self.getToken(ZCodeParser.NumberLit, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arrExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrExpr" ):
                return visitor.visitArrExpr(self)
            else:
                return visitor.visitChildren(self)




    def arrExpr(self):

        localctx = ZCodeParser.ArrExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_arrExpr)
        try:
            self.state = 320
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 317
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 318
                self.functionCall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 319
                self.match(ZCodeParser.NumberLit)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrExpr(self):
            return self.getTypedRuleContext(ZCodeParser.ArrExprContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def indexOp(self):
            return self.getTypedRuleContext(ZCodeParser.IndexOpContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_indexOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexOp" ):
                return visitor.visitIndexOp(self)
            else:
                return visitor.visitChildren(self)




    def indexOp(self):

        localctx = ZCodeParser.IndexOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_indexOp)
        try:
            self.state = 327
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 322
                self.arrExpr()
                self.state = 323
                self.match(ZCodeParser.COMMA)
                self.state = 324
                self.indexOp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 326
                self.arrExpr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LBracket(self):
            return self.getToken(ZCodeParser.LBracket, 0)

        def functionArgsList(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionArgsListContext,0)


        def RBracket(self):
            return self.getToken(ZCodeParser.RBracket, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_functionCall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = ZCodeParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_functionCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 330
            self.match(ZCodeParser.LBracket)
            self.state = 331
            self.functionArgsList()
            self.state = 332
            self.match(ZCodeParser.RBracket)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionArgsListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argsPrime(self):
            return self.getTypedRuleContext(ZCodeParser.ArgsPrimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_functionArgsList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionArgsList" ):
                return visitor.visitFunctionArgsList(self)
            else:
                return visitor.visitChildren(self)




    def functionArgsList(self):

        localctx = ZCodeParser.FunctionArgsListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_functionArgsList)
        try:
            self.state = 336
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT, ZCodeParser.MINUS, ZCodeParser.NumberLit, ZCodeParser.BooleanLit, ZCodeParser.StringLit, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.argsPrime()
                pass
            elif token in [ZCodeParser.RBracket]:
                self.enterOuterAlt(localctx, 2)

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


    class ArgsPrimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arg(self):
            return self.getTypedRuleContext(ZCodeParser.ArgContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def argsPrime(self):
            return self.getTypedRuleContext(ZCodeParser.ArgsPrimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_argsPrime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgsPrime" ):
                return visitor.visitArgsPrime(self)
            else:
                return visitor.visitChildren(self)




    def argsPrime(self):

        localctx = ZCodeParser.ArgsPrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_argsPrime)
        try:
            self.state = 343
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.arg()
                self.state = 339
                self.match(ZCodeParser.COMMA)
                self.state = 340
                self.argsPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 342
                self.arg()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arg

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg" ):
                return visitor.visitArg(self)
            else:
                return visitor.visitChildren(self)




    def arg(self):

        localctx = ZCodeParser.ArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.expression()
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

        def functionCallStatement(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionCallStatementContext,0)


        def continueStatement(self):
            return self.getTypedRuleContext(ZCodeParser.ContinueStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(ZCodeParser.ReturnStatementContext,0)


        def breakStatement(self):
            return self.getTypedRuleContext(ZCodeParser.BreakStatementContext,0)


        def blockStatement(self):
            return self.getTypedRuleContext(ZCodeParser.BlockStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(ZCodeParser.IfStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(ZCodeParser.ForStatementContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.IDENTIFIER]:
                self.state = 347
                self.functionCallStatement()
                pass
            elif token in [ZCodeParser.CONTINUE]:
                self.state = 348
                self.continueStatement()
                pass
            elif token in [ZCodeParser.RETURN]:
                self.state = 349
                self.returnStatement()
                pass
            elif token in [ZCodeParser.BREAK]:
                self.state = 350
                self.breakStatement()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.state = 351
                self.blockStatement()
                pass
            elif token in [ZCodeParser.IF]:
                self.state = 352
                self.ifStatement()
                pass
            elif token in [ZCodeParser.FOR]:
                self.state = 353
                self.forStatement()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 357 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 356
                    self.match(ZCodeParser.NEWLINE)

                else:
                    raise NoViableAltException(self)
                self.state = 359 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def normalDeclaration(self):
            return self.getTypedRuleContext(ZCodeParser.NormalDeclarationContext,0)


        def arrayDeclaration(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayDeclarationContext,0)


        def varDecl(self):
            return self.getTypedRuleContext(ZCodeParser.VarDeclContext,0)


        def dynamicDecl(self):
            return self.getTypedRuleContext(ZCodeParser.DynamicDeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_variableDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclaration" ):
                return visitor.visitVariableDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclaration(self):

        localctx = ZCodeParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_variableDeclaration)
        try:
            self.state = 365
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 361
                self.normalDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 362
                self.arrayDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 363
                self.varDecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 364
                self.dynamicDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NormalDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varType(self):
            return self.getTypedRuleContext(ZCodeParser.VarTypeContext,0)


        def variableInitialization(self):
            return self.getTypedRuleContext(ZCodeParser.VariableInitializationContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_normalDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormalDeclaration" ):
                return visitor.visitNormalDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def normalDeclaration(self):

        localctx = ZCodeParser.NormalDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_normalDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.varType()
            self.state = 369
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LEFTARR:
                self.state = 368
                self.variableInitialization()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_varType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarType" ):
                return visitor.visitVarType(self)
            else:
                return visitor.visitChildren(self)




    def varType(self):

        localctx = ZCodeParser.VarTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_varType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
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


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def variableInitialization(self):
            return self.getTypedRuleContext(ZCodeParser.VariableInitializationContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_varDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = ZCodeParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_varDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self.match(ZCodeParser.VAR)
            self.state = 374
            self.variableInitialization()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DynamicDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def variableInitialization(self):
            return self.getTypedRuleContext(ZCodeParser.VariableInitializationContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_dynamicDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDynamicDecl" ):
                return visitor.visitDynamicDecl(self)
            else:
                return visitor.visitChildren(self)




    def dynamicDecl(self):

        localctx = ZCodeParser.DynamicDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_dynamicDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.match(ZCodeParser.DYNAMIC)
            self.state = 378
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LEFTARR:
                self.state = 377
                self.variableInitialization()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableInitializationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFTARR(self):
            return self.getToken(ZCodeParser.LEFTARR, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_variableInitialization

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableInitialization" ):
                return visitor.visitVariableInitialization(self)
            else:
                return visitor.visitChildren(self)




    def variableInitialization(self):

        localctx = ZCodeParser.VariableInitializationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_variableInitialization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.match(ZCodeParser.LEFTARR)
            self.state = 381
            self.expression()
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

        def arithExpr(self):
            return self.getTypedRuleContext(ZCodeParser.ArithExprContext,0)


        def stringConcatExpr(self):
            return self.getTypedRuleContext(ZCodeParser.StringConcatExprContext,0)


        def relExpr(self):
            return self.getTypedRuleContext(ZCodeParser.RelExprContext,0)


        def logicExpr(self):
            return self.getTypedRuleContext(ZCodeParser.LogicExprContext,0)


        def elementAccessExpr(self):
            return self.getTypedRuleContext(ZCodeParser.ElementAccessExprContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = ZCodeParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_expression)
        try:
            self.state = 389
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 383
                self.arithExpr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 384
                self.stringConcatExpr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 385
                self.relExpr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 386
                self.logicExpr(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 387
                self.elementAccessExpr()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 388
                self.functionCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamDeclListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramDeclPrime(self):
            return self.getTypedRuleContext(ZCodeParser.ParamDeclPrimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramDeclList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamDeclList" ):
                return visitor.visitParamDeclList(self)
            else:
                return visitor.visitChildren(self)




    def paramDeclList(self):

        localctx = ZCodeParser.ParamDeclListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_paramDeclList)
        try:
            self.state = 393
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 391
                self.paramDeclPrime()
                pass
            elif token in [ZCodeParser.RBracket]:
                self.enterOuterAlt(localctx, 2)

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


    class ParamDeclPrimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramDeclAtom(self):
            return self.getTypedRuleContext(ZCodeParser.ParamDeclAtomContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def paramDeclPrime(self):
            return self.getTypedRuleContext(ZCodeParser.ParamDeclPrimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramDeclPrime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamDeclPrime" ):
                return visitor.visitParamDeclPrime(self)
            else:
                return visitor.visitChildren(self)




    def paramDeclPrime(self):

        localctx = ZCodeParser.ParamDeclPrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_paramDeclPrime)
        try:
            self.state = 400
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 395
                self.paramDeclAtom()
                self.state = 396
                self.match(ZCodeParser.COMMA)
                self.state = 397
                self.paramDeclPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 399
                self.paramDeclAtom()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamDeclAtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varType(self):
            return self.getTypedRuleContext(ZCodeParser.VarTypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LSBracket(self):
            return self.getToken(ZCodeParser.LSBracket, 0)

        def arrayDim(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayDimContext,0)


        def RSBracket(self):
            return self.getToken(ZCodeParser.RSBracket, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_paramDeclAtom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamDeclAtom" ):
                return visitor.visitParamDeclAtom(self)
            else:
                return visitor.visitChildren(self)




    def paramDeclAtom(self):

        localctx = ZCodeParser.ParamDeclAtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_paramDeclAtom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.varType()
            self.state = 403
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 408
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LSBracket:
                self.state = 404
                self.match(ZCodeParser.LSBracket)
                self.state = 405
                self.arrayDim()
                self.state = 406
                self.match(ZCodeParser.RSBracket)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LBracket(self):
            return self.getToken(ZCodeParser.LBracket, 0)

        def paramDeclList(self):
            return self.getTypedRuleContext(ZCodeParser.ParamDeclListContext,0)


        def RBracket(self):
            return self.getToken(ZCodeParser.RBracket, 0)

        def nullableListOfNEWLINE(self):
            return self.getTypedRuleContext(ZCodeParser.NullableListOfNEWLINEContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(ZCodeParser.ReturnStatementContext,0)


        def blockStatement(self):
            return self.getTypedRuleContext(ZCodeParser.BlockStatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = ZCodeParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.match(ZCodeParser.FUNC)
            self.state = 411
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 412
            self.match(ZCodeParser.LBracket)
            self.state = 413
            self.paramDeclList()
            self.state = 414
            self.match(ZCodeParser.RBracket)
            self.state = 415
            self.nullableListOfNEWLINE()
            self.state = 418
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN]:
                self.state = 416
                self.returnStatement()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.state = 417
                self.blockStatement()
                pass
            elif token in [ZCodeParser.EOF, ZCodeParser.FUNC]:
                pass
            else:
                pass
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NullableListOfNEWLINEContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def nullableListOfNEWLINE(self):
            return self.getTypedRuleContext(ZCodeParser.NullableListOfNEWLINEContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_nullableListOfNEWLINE

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullableListOfNEWLINE" ):
                return visitor.visitNullableListOfNEWLINE(self)
            else:
                return visitor.visitChildren(self)




    def nullableListOfNEWLINE(self):

        localctx = ZCodeParser.NullableListOfNEWLINEContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_nullableListOfNEWLINE)
        try:
            self.state = 423
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 420
                self.match(ZCodeParser.NEWLINE)
                self.state = 421
                self.nullableListOfNEWLINE()
                pass
            elif token in [ZCodeParser.EOF, ZCodeParser.RETURN, ZCodeParser.FUNC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.ELIF, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)

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


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def logicExpr(self):
            return self.getTypedRuleContext(ZCodeParser.LogicExprContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def elifStatementList(self):
            return self.getTypedRuleContext(ZCodeParser.ElifStatementListContext,0)


        def elseStatement(self):
            return self.getTypedRuleContext(ZCodeParser.ElseStatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_ifStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = ZCodeParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self.match(ZCodeParser.IF)
            self.state = 426
            self.logicExpr(0)
            self.state = 427
            self.statement()
            self.state = 428
            self.elifStatementList()
            self.state = 430
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ELSE:
                self.state = 429
                self.elseStatement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifStatementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elifStatementPrime(self):
            return self.getTypedRuleContext(ZCodeParser.ElifStatementPrimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elifStatementList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifStatementList" ):
                return visitor.visitElifStatementList(self)
            else:
                return visitor.visitChildren(self)




    def elifStatementList(self):

        localctx = ZCodeParser.ElifStatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_elifStatementList)
        try:
            self.state = 434
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ELIF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 432
                self.elifStatementPrime()
                pass
            elif token in [ZCodeParser.ELSE, ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)

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


    class ElifStatementPrimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elifStatement(self):
            return self.getTypedRuleContext(ZCodeParser.ElifStatementContext,0)


        def nullableListOfNEWLINE(self):
            return self.getTypedRuleContext(ZCodeParser.NullableListOfNEWLINEContext,0)


        def elifStatementPrime(self):
            return self.getTypedRuleContext(ZCodeParser.ElifStatementPrimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elifStatementPrime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifStatementPrime" ):
                return visitor.visitElifStatementPrime(self)
            else:
                return visitor.visitChildren(self)




    def elifStatementPrime(self):

        localctx = ZCodeParser.ElifStatementPrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_elifStatementPrime)
        try:
            self.state = 441
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 436
                self.elifStatement()
                self.state = 437
                self.nullableListOfNEWLINE()
                self.state = 438
                self.elifStatementPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 440
                self.elifStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def logicExpr(self):
            return self.getTypedRuleContext(ZCodeParser.LogicExprContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elifStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifStatement" ):
                return visitor.visitElifStatement(self)
            else:
                return visitor.visitChildren(self)




    def elifStatement(self):

        localctx = ZCodeParser.ElifStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_elifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            self.match(ZCodeParser.ELIF)
            self.state = 444
            self.logicExpr(0)
            self.state = 445
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def logicExpr(self):
            return self.getTypedRuleContext(ZCodeParser.LogicExprContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elseStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseStatement" ):
                return visitor.visitElseStatement(self)
            else:
                return visitor.visitChildren(self)




    def elseStatement(self):

        localctx = ZCodeParser.ElseStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_elseStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            self.match(ZCodeParser.ELSE)
            self.state = 448
            self.logicExpr(0)
            self.state = 449
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def logicExpr(self):
            return self.getTypedRuleContext(ZCodeParser.LogicExprContext,0)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def updateExpr(self):
            return self.getTypedRuleContext(ZCodeParser.UpdateExprContext,0)


        def nullableListOfNEWLINE(self):
            return self.getTypedRuleContext(ZCodeParser.NullableListOfNEWLINEContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_forStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = ZCodeParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.match(ZCodeParser.FOR)
            self.state = 452
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 453
            self.match(ZCodeParser.UNTIL)
            self.state = 454
            self.logicExpr(0)
            self.state = 455
            self.match(ZCodeParser.BY)
            self.state = 456
            self.updateExpr()
            self.state = 457
            self.nullableListOfNEWLINE()
            self.state = 458
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpdateExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_updateExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdateExpr" ):
                return visitor.visitUpdateExpr(self)
            else:
                return visitor.visitChildren(self)




    def updateExpr(self):

        localctx = ZCodeParser.UpdateExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_updateExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_breakStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStatement" ):
                return visitor.visitBreakStatement(self)
            else:
                return visitor.visitChildren(self)




    def breakStatement(self):

        localctx = ZCodeParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self.match(ZCodeParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_continueStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStatement" ):
                return visitor.visitContinueStatement(self)
            else:
                return visitor.visitChildren(self)




    def continueStatement(self):

        localctx = ZCodeParser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 464
            self.match(ZCodeParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_returnStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = ZCodeParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            self.match(ZCodeParser.RETURN)
            self.state = 468
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NOT) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.NumberLit) | (1 << ZCodeParser.BooleanLit) | (1 << ZCodeParser.StringLit) | (1 << ZCodeParser.IDENTIFIER))) != 0):
                self.state = 467
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionCall(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_functionCallStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCallStatement" ):
                return visitor.visitFunctionCallStatement(self)
            else:
                return visitor.visitChildren(self)




    def functionCallStatement(self):

        localctx = ZCodeParser.FunctionCallStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_functionCallStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
            self.functionCall()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def blockStatementBody(self):
            return self.getTypedRuleContext(ZCodeParser.BlockStatementBodyContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_blockStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStatement" ):
                return visitor.visitBlockStatement(self)
            else:
                return visitor.visitChildren(self)




    def blockStatement(self):

        localctx = ZCodeParser.BlockStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_blockStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            self.match(ZCodeParser.BEGIN)
            self.state = 474 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 473
                self.match(ZCodeParser.NEWLINE)
                self.state = 476 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZCodeParser.NEWLINE):
                    break

            self.state = 478
            self.blockStatementBody()
            self.state = 479
            self.match(ZCodeParser.END)
            self.state = 486
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEWLINE]:
                self.state = 481 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 480
                        self.match(ZCodeParser.NEWLINE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 483 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

                pass
            elif token in [ZCodeParser.EOF]:
                self.state = 485
                self.match(ZCodeParser.EOF)
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


    class BlockStatementBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nullableListOfStatement(self):
            return self.getTypedRuleContext(ZCodeParser.NullableListOfStatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_blockStatementBody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStatementBody" ):
                return visitor.visitBlockStatementBody(self)
            else:
                return visitor.visitChildren(self)




    def blockStatementBody(self):

        localctx = ZCodeParser.BlockStatementBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_blockStatementBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488
            self.nullableListOfStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NullableListOfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def nullableListOfStatement(self):
            return self.getTypedRuleContext(ZCodeParser.NullableListOfStatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_nullableListOfStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullableListOfStatement" ):
                return visitor.visitNullableListOfStatement(self)
            else:
                return visitor.visitChildren(self)




    def nullableListOfStatement(self):

        localctx = ZCodeParser.NullableListOfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_nullableListOfStatement)
        try:
            self.state = 494
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 490
                self.statement()
                self.state = 491
                self.nullableListOfStatement()
                pass
            elif token in [ZCodeParser.END]:
                self.enterOuterAlt(localctx, 2)

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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[13] = self.arithExpr_sempred
        self._predicates[14] = self.arithExpr1_sempred
        self._predicates[17] = self.logicExpr_sempred
        self._predicates[18] = self.logicExpr1_sempred
        self._predicates[21] = self.stringConcatExpr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def arithExpr_sempred(self, localctx:ArithExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def arithExpr1_sempred(self, localctx:ArithExpr1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def logicExpr_sempred(self, localctx:LogicExprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def logicExpr1_sempred(self, localctx:LogicExpr1Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def stringConcatExpr_sempred(self, localctx:StringConcatExprContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         




