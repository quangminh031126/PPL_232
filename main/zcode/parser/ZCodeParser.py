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
        buf.write("\u01e1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\3\2\3\2\3\3\7\3|\n\3\f\3\16\3\177\13\3\3\3\7\3")
        buf.write("\u0082\n\3\f\3\16\3\u0085\13\3\3\3\3\3\3\4\3\4\5\4\u008b")
        buf.write("\n\4\3\4\6\4\u008e\n\4\r\4\16\4\u008f\3\4\5\4\u0093\n")
        buf.write("\4\3\5\3\5\5\5\u0097\n\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\5\7\u00a1\n\7\3\b\3\b\3\b\3\b\5\b\u00a7\n\b\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\5\t\u00af\n\t\3\n\3\n\3\n\5\n\u00b4\n")
        buf.write("\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5")
        buf.write("\13\u00c0\n\13\3\f\3\f\3\f\3\f\3\f\5\f\u00c7\n\f\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\16\3\16\5\16\u00d0\n\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\5\17\u00d7\n\17\3\20\3\20\3\20\3\20\3\20\3")
        buf.write("\21\3\21\5\21\u00e0\n\21\3\22\3\22\3\22\3\22\3\22\5\22")
        buf.write("\u00e7\n\22\3\23\3\23\3\24\3\24\5\24\u00ed\n\24\3\25\3")
        buf.write("\25\3\25\3\25\3\26\3\26\5\26\u00f5\n\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u0101\n\27\3")
        buf.write("\27\6\27\u0104\n\27\r\27\16\27\u0105\3\27\5\27\u0109\n")
        buf.write("\27\3\30\3\30\3\30\3\30\5\30\u010f\n\30\3\31\3\31\3\31")
        buf.write("\5\31\u0114\n\31\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3")
        buf.write("\34\3\34\5\34\u011f\n\34\3\35\3\35\3\35\3\36\3\36\5\36")
        buf.write("\u0126\n\36\3\37\3\37\3\37\3\37\3\37\5\37\u012d\n\37\3")
        buf.write(" \3 \3 \3 \3 \3 \5 \u0135\n \3!\3!\3!\3!\7!\u013b\n!\f")
        buf.write("!\16!\u013e\13!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3$\3")
        buf.write("$\5$\u014c\n$\3%\3%\3%\3%\3%\5%\u0153\n%\3&\3&\5&\u0157")
        buf.write("\n&\3\'\3\'\7\'\u015b\n\'\f\'\16\'\u015e\13\'\3\'\3\'")
        buf.write("\3\'\5\'\u0163\n\'\3(\3(\3(\3(\3)\3)\3)\3)\3*\3*\3*\3")
        buf.write("*\3*\3*\3*\7*\u0174\n*\f*\16*\u0177\13*\3*\3*\3+\3+\3")
        buf.write(",\3,\3-\3-\3.\3.\5.\u0183\n.\3/\3/\3\60\3\60\3\60\3\60")
        buf.write("\3\61\3\61\3\62\3\62\7\62\u018f\n\62\f\62\16\62\u0192")
        buf.write("\13\62\3\63\3\63\3\63\3\63\3\63\5\63\u0199\n\63\3\64\3")
        buf.write("\64\3\64\3\64\3\64\5\64\u01a0\n\64\3\65\3\65\3\65\3\65")
        buf.write("\3\65\5\65\u01a7\n\65\3\66\3\66\3\66\3\66\3\66\3\66\7")
        buf.write("\66\u01af\n\66\f\66\16\66\u01b2\13\66\3\67\3\67\3\67\3")
        buf.write("\67\3\67\3\67\7\67\u01ba\n\67\f\67\16\67\u01bd\13\67\3")
        buf.write("8\38\38\38\38\38\78\u01c5\n8\f8\168\u01c8\138\39\39\3")
        buf.write("9\59\u01cd\n9\3:\3:\3:\5:\u01d2\n:\3;\3;\5;\u01d6\n;\3")
        buf.write("<\3<\3<\3<\3<\3<\3<\5<\u01df\n<\3<\2\5jln=\2\4\6\b\n\f")
        buf.write("\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@")
        buf.write("BDFHJLNPRTVXZ\\^`bdfhjlnprtv\2\b\4\2\3\4-.\3\2\5\7\4\2")
        buf.write("\36\36 %\3\2\27\30\3\2\31\32\3\2\33\35\2\u01df\2x\3\2")
        buf.write("\2\2\4}\3\2\2\2\6\u008a\3\2\2\2\b\u0096\3\2\2\2\n\u0098")
        buf.write("\3\2\2\2\f\u009a\3\2\2\2\16\u00a6\3\2\2\2\20\u00a8\3\2")
        buf.write("\2\2\22\u00b3\3\2\2\2\24\u00bf\3\2\2\2\26\u00c6\3\2\2")
        buf.write("\2\30\u00c8\3\2\2\2\32\u00cf\3\2\2\2\34\u00d6\3\2\2\2")
        buf.write("\36\u00d8\3\2\2\2 \u00df\3\2\2\2\"\u00e6\3\2\2\2$\u00e8")
        buf.write("\3\2\2\2&\u00ec\3\2\2\2(\u00ee\3\2\2\2*\u00f4\3\2\2\2")
        buf.write(",\u0100\3\2\2\2.\u010e\3\2\2\2\60\u0110\3\2\2\2\62\u0115")
        buf.write("\3\2\2\2\64\u0117\3\2\2\2\66\u011b\3\2\2\28\u0120\3\2")
        buf.write("\2\2:\u0125\3\2\2\2<\u012c\3\2\2\2>\u012e\3\2\2\2@\u0136")
        buf.write("\3\2\2\2B\u0141\3\2\2\2D\u0145\3\2\2\2F\u014b\3\2\2\2")
        buf.write("H\u014d\3\2\2\2J\u0156\3\2\2\2L\u0162\3\2\2\2N\u0164\3")
        buf.write("\2\2\2P\u0168\3\2\2\2R\u016c\3\2\2\2T\u017a\3\2\2\2V\u017c")
        buf.write("\3\2\2\2X\u017e\3\2\2\2Z\u0180\3\2\2\2\\\u0184\3\2\2\2")
        buf.write("^\u0186\3\2\2\2`\u018a\3\2\2\2b\u0190\3\2\2\2d\u0198\3")
        buf.write("\2\2\2f\u019f\3\2\2\2h\u01a6\3\2\2\2j\u01a8\3\2\2\2l\u01b3")
        buf.write("\3\2\2\2n\u01be\3\2\2\2p\u01cc\3\2\2\2r\u01d1\3\2\2\2")
        buf.write("t\u01d5\3\2\2\2v\u01de\3\2\2\2xy\t\2\2\2y\3\3\2\2\2z|")
        buf.write("\7,\2\2{z\3\2\2\2|\177\3\2\2\2}{\3\2\2\2}~\3\2\2\2~\u0083")
        buf.write("\3\2\2\2\177}\3\2\2\2\u0080\u0082\5\6\4\2\u0081\u0080")
        buf.write("\3\2\2\2\u0082\u0085\3\2\2\2\u0083\u0081\3\2\2\2\u0083")
        buf.write("\u0084\3\2\2\2\u0084\u0086\3\2\2\2\u0085\u0083\3\2\2\2")
        buf.write("\u0086\u0087\7\2\2\3\u0087\5\3\2\2\2\u0088\u008b\5\b\5")
        buf.write("\2\u0089\u008b\5.\30\2\u008a\u0088\3\2\2\2\u008a\u0089")
        buf.write("\3\2\2\2\u008b\u0092\3\2\2\2\u008c\u008e\7,\2\2\u008d")
        buf.write("\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u008d\3\2\2\2")
        buf.write("\u008f\u0090\3\2\2\2\u0090\u0093\3\2\2\2\u0091\u0093\7")
        buf.write("\2\2\3\u0092\u008d\3\2\2\2\u0092\u0091\3\2\2\2\u0093\7")
        buf.write("\3\2\2\2\u0094\u0097\5\n\6\2\u0095\u0097\5B\"\2\u0096")
        buf.write("\u0094\3\2\2\2\u0096\u0095\3\2\2\2\u0097\t\3\2\2\2\u0098")
        buf.write("\u0099\5@!\2\u0099\13\3\2\2\2\u009a\u009b\5\62\32\2\u009b")
        buf.write("\u009c\7/\2\2\u009c\u009d\7)\2\2\u009d\u009e\5\16\b\2")
        buf.write("\u009e\u00a0\7*\2\2\u009f\u00a1\5\20\t\2\u00a0\u009f\3")
        buf.write("\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\r\3\2\2\2\u00a2\u00a3")
        buf.write("\7-\2\2\u00a3\u00a4\7+\2\2\u00a4\u00a7\5\16\b\2\u00a5")
        buf.write("\u00a7\7-\2\2\u00a6\u00a2\3\2\2\2\u00a6\u00a5\3\2\2\2")
        buf.write("\u00a7\17\3\2\2\2\u00a8\u00ae\7\37\2\2\u00a9\u00aa\7)")
        buf.write("\2\2\u00aa\u00ab\5\22\n\2\u00ab\u00ac\7*\2\2\u00ac\u00af")
        buf.write("\3\2\2\2\u00ad\u00af\5f\64\2\u00ae\u00a9\3\2\2\2\u00ae")
        buf.write("\u00ad\3\2\2\2\u00af\21\3\2\2\2\u00b0\u00b4\5\26\f\2\u00b1")
        buf.write("\u00b4\5\24\13\2\u00b2\u00b4\5d\63\2\u00b3\u00b0\3\2\2")
        buf.write("\2\u00b3\u00b1\3\2\2\2\u00b3\u00b2\3\2\2\2\u00b4\23\3")
        buf.write("\2\2\2\u00b5\u00b6\7)\2\2\u00b6\u00b7\5\22\n\2\u00b7\u00b8")
        buf.write("\7*\2\2\u00b8\u00b9\7+\2\2\u00b9\u00ba\5\24\13\2\u00ba")
        buf.write("\u00c0\3\2\2\2\u00bb\u00bc\7)\2\2\u00bc\u00bd\5\22\n\2")
        buf.write("\u00bd\u00be\7*\2\2\u00be\u00c0\3\2\2\2\u00bf\u00b5\3")
        buf.write("\2\2\2\u00bf\u00bb\3\2\2\2\u00c0\25\3\2\2\2\u00c1\u00c2")
        buf.write("\5\2\2\2\u00c2\u00c3\7+\2\2\u00c3\u00c4\5\26\f\2\u00c4")
        buf.write("\u00c7\3\2\2\2\u00c5\u00c7\5\2\2\2\u00c6\u00c1\3\2\2\2")
        buf.write("\u00c6\u00c5\3\2\2\2\u00c7\27\3\2\2\2\u00c8\u00c9\5\32")
        buf.write("\16\2\u00c9\u00ca\7)\2\2\u00ca\u00cb\5\34\17\2\u00cb\u00cc")
        buf.write("\7*\2\2\u00cc\31\3\2\2\2\u00cd\u00d0\7/\2\2\u00ce\u00d0")
        buf.write("\5\36\20\2\u00cf\u00cd\3\2\2\2\u00cf\u00ce\3\2\2\2\u00d0")
        buf.write("\33\3\2\2\2\u00d1\u00d2\5f\64\2\u00d2\u00d3\7+\2\2\u00d3")
        buf.write("\u00d4\5\34\17\2\u00d4\u00d7\3\2\2\2\u00d5\u00d7\5f\64")
        buf.write("\2\u00d6\u00d1\3\2\2\2\u00d6\u00d5\3\2\2\2\u00d7\35\3")
        buf.write("\2\2\2\u00d8\u00d9\7/\2\2\u00d9\u00da\7\'\2\2\u00da\u00db")
        buf.write("\5 \21\2\u00db\u00dc\7(\2\2\u00dc\37\3\2\2\2\u00dd\u00e0")
        buf.write("\5\"\22\2\u00de\u00e0\3\2\2\2\u00df\u00dd\3\2\2\2\u00df")
        buf.write("\u00de\3\2\2\2\u00e0!\3\2\2\2\u00e1\u00e2\5$\23\2\u00e2")
        buf.write("\u00e3\7+\2\2\u00e3\u00e4\5\"\22\2\u00e4\u00e7\3\2\2\2")
        buf.write("\u00e5\u00e7\5$\23\2\u00e6\u00e1\3\2\2\2\u00e6\u00e5\3")
        buf.write("\2\2\2\u00e7#\3\2\2\2\u00e8\u00e9\5f\64\2\u00e9%\3\2\2")
        buf.write("\2\u00ea\u00ed\5(\25\2\u00eb\u00ed\5*\26\2\u00ec\u00ea")
        buf.write("\3\2\2\2\u00ec\u00eb\3\2\2\2\u00ed\'\3\2\2\2\u00ee\u00ef")
        buf.write("\7/\2\2\u00ef\u00f0\7\37\2\2\u00f0\u00f1\5f\64\2\u00f1")
        buf.write(")\3\2\2\2\u00f2\u00f5\7/\2\2\u00f3\u00f5\5\30\r\2\u00f4")
        buf.write("\u00f2\3\2\2\2\u00f4\u00f3\3\2\2\2\u00f5\u00f6\3\2\2\2")
        buf.write("\u00f6\u00f7\5\20\t\2\u00f7+\3\2\2\2\u00f8\u0101\5H%\2")
        buf.write("\u00f9\u0101\5R*\2\u00fa\u0101\5V,\2\u00fb\u0101\5X-\2")
        buf.write("\u00fc\u0101\5Z.\2\u00fd\u0101\5\\/\2\u00fe\u0101\5^\60")
        buf.write("\2\u00ff\u0101\5&\24\2\u0100\u00f8\3\2\2\2\u0100\u00f9")
        buf.write("\3\2\2\2\u0100\u00fa\3\2\2\2\u0100\u00fb\3\2\2\2\u0100")
        buf.write("\u00fc\3\2\2\2\u0100\u00fd\3\2\2\2\u0100\u00fe\3\2\2\2")
        buf.write("\u0100\u00ff\3\2\2\2\u0101\u0108\3\2\2\2\u0102\u0104\7")
        buf.write(",\2\2\u0103\u0102\3\2\2\2\u0104\u0105\3\2\2\2\u0105\u0103")
        buf.write("\3\2\2\2\u0105\u0106\3\2\2\2\u0106\u0109\3\2\2\2\u0107")
        buf.write("\u0109\7\2\2\3\u0108\u0103\3\2\2\2\u0108\u0107\3\2\2\2")
        buf.write("\u0109-\3\2\2\2\u010a\u010f\5\60\31\2\u010b\u010f\5\f")
        buf.write("\7\2\u010c\u010f\5\64\33\2\u010d\u010f\5\66\34\2\u010e")
        buf.write("\u010a\3\2\2\2\u010e\u010b\3\2\2\2\u010e\u010c\3\2\2\2")
        buf.write("\u010e\u010d\3\2\2\2\u010f/\3\2\2\2\u0110\u0111\5\62\32")
        buf.write("\2\u0111\u0113\7/\2\2\u0112\u0114\58\35\2\u0113\u0112")
        buf.write("\3\2\2\2\u0113\u0114\3\2\2\2\u0114\61\3\2\2\2\u0115\u0116")
        buf.write("\t\3\2\2\u0116\63\3\2\2\2\u0117\u0118\7\t\2\2\u0118\u0119")
        buf.write("\7/\2\2\u0119\u011a\58\35\2\u011a\65\3\2\2\2\u011b\u011c")
        buf.write("\7\n\2\2\u011c\u011e\7/\2\2\u011d\u011f\58\35\2\u011e")
        buf.write("\u011d\3\2\2\2\u011e\u011f\3\2\2\2\u011f\67\3\2\2\2\u0120")
        buf.write("\u0121\7\37\2\2\u0121\u0122\5f\64\2\u01229\3\2\2\2\u0123")
        buf.write("\u0126\5<\37\2\u0124\u0126\3\2\2\2\u0125\u0123\3\2\2\2")
        buf.write("\u0125\u0124\3\2\2\2\u0126;\3\2\2\2\u0127\u0128\5> \2")
        buf.write("\u0128\u0129\7+\2\2\u0129\u012a\5<\37\2\u012a\u012d\3")
        buf.write("\2\2\2\u012b\u012d\5> \2\u012c\u0127\3\2\2\2\u012c\u012b")
        buf.write("\3\2\2\2\u012d=\3\2\2\2\u012e\u012f\5\62\32\2\u012f\u0134")
        buf.write("\7/\2\2\u0130\u0131\7)\2\2\u0131\u0132\5\16\b\2\u0132")
        buf.write("\u0133\7*\2\2\u0133\u0135\3\2\2\2\u0134\u0130\3\2\2\2")
        buf.write("\u0134\u0135\3\2\2\2\u0135?\3\2\2\2\u0136\u0137\7\13\2")
        buf.write("\2\u0137\u0138\7/\2\2\u0138\u013c\5D#\2\u0139\u013b\7")
        buf.write(",\2\2\u013a\u0139\3\2\2\2\u013b\u013e\3\2\2\2\u013c\u013a")
        buf.write("\3\2\2\2\u013c\u013d\3\2\2\2\u013d\u013f\3\2\2\2\u013e")
        buf.write("\u013c\3\2\2\2\u013f\u0140\5F$\2\u0140A\3\2\2\2\u0141")
        buf.write("\u0142\7\13\2\2\u0142\u0143\7/\2\2\u0143\u0144\5D#\2\u0144")
        buf.write("C\3\2\2\2\u0145\u0146\7\'\2\2\u0146\u0147\5:\36\2\u0147")
        buf.write("\u0148\7(\2\2\u0148E\3\2\2\2\u0149\u014c\5^\60\2\u014a")
        buf.write("\u014c\5Z.\2\u014b\u0149\3\2\2\2\u014b\u014a\3\2\2\2\u014c")
        buf.write("G\3\2\2\2\u014d\u014e\7\21\2\2\u014e\u014f\5f\64\2\u014f")
        buf.write("\u0150\5,\27\2\u0150\u0152\5J&\2\u0151\u0153\5P)\2\u0152")
        buf.write("\u0151\3\2\2\2\u0152\u0153\3\2\2\2\u0153I\3\2\2\2\u0154")
        buf.write("\u0157\5L\'\2\u0155\u0157\3\2\2\2\u0156\u0154\3\2\2\2")
        buf.write("\u0156\u0155\3\2\2\2\u0157K\3\2\2\2\u0158\u015c\5N(\2")
        buf.write("\u0159\u015b\7,\2\2\u015a\u0159\3\2\2\2\u015b\u015e\3")
        buf.write("\2\2\2\u015c\u015a\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u015f")
        buf.write("\3\2\2\2\u015e\u015c\3\2\2\2\u015f\u0160\5L\'\2\u0160")
        buf.write("\u0163\3\2\2\2\u0161\u0163\5N(\2\u0162\u0158\3\2\2\2\u0162")
        buf.write("\u0161\3\2\2\2\u0163M\3\2\2\2\u0164\u0165\7\23\2\2\u0165")
        buf.write("\u0166\5f\64\2\u0166\u0167\5,\27\2\u0167O\3\2\2\2\u0168")
        buf.write("\u0169\7\22\2\2\u0169\u016a\5f\64\2\u016a\u016b\5,\27")
        buf.write("\2\u016bQ\3\2\2\2\u016c\u016d\7\f\2\2\u016d\u016e\7/\2")
        buf.write("\2\u016e\u016f\7\r\2\2\u016f\u0170\5f\64\2\u0170\u0171")
        buf.write("\7\16\2\2\u0171\u0175\5T+\2\u0172\u0174\7,\2\2\u0173\u0172")
        buf.write("\3\2\2\2\u0174\u0177\3\2\2\2\u0175\u0173\3\2\2\2\u0175")
        buf.write("\u0176\3\2\2\2\u0176\u0178\3\2\2\2\u0177\u0175\3\2\2\2")
        buf.write("\u0178\u0179\5,\27\2\u0179S\3\2\2\2\u017a\u017b\5f\64")
        buf.write("\2\u017bU\3\2\2\2\u017c\u017d\7\17\2\2\u017dW\3\2\2\2")
        buf.write("\u017e\u017f\7\20\2\2\u017fY\3\2\2\2\u0180\u0182\7\b\2")
        buf.write("\2\u0181\u0183\5f\64\2\u0182\u0181\3\2\2\2\u0182\u0183")
        buf.write("\3\2\2\2\u0183[\3\2\2\2\u0184\u0185\5\36\20\2\u0185]\3")
        buf.write("\2\2\2\u0186\u0187\7\24\2\2\u0187\u0188\5`\61\2\u0188")
        buf.write("\u0189\7\25\2\2\u0189_\3\2\2\2\u018a\u018b\5b\62\2\u018b")
        buf.write("a\3\2\2\2\u018c\u018f\5,\27\2\u018d\u018f\5\6\4\2\u018e")
        buf.write("\u018c\3\2\2\2\u018e\u018d\3\2\2\2\u018f\u0192\3\2\2\2")
        buf.write("\u0190\u018e\3\2\2\2\u0190\u0191\3\2\2\2\u0191c\3\2\2")
        buf.write("\2\u0192\u0190\3\2\2\2\u0193\u0194\5f\64\2\u0194\u0195")
        buf.write("\7+\2\2\u0195\u0196\5d\63\2\u0196\u0199\3\2\2\2\u0197")
        buf.write("\u0199\5f\64\2\u0198\u0193\3\2\2\2\u0198\u0197\3\2\2\2")
        buf.write("\u0199e\3\2\2\2\u019a\u019b\5h\65\2\u019b\u019c\7&\2\2")
        buf.write("\u019c\u019d\5h\65\2\u019d\u01a0\3\2\2\2\u019e\u01a0\5")
        buf.write("h\65\2\u019f\u019a\3\2\2\2\u019f\u019e\3\2\2\2\u01a0g")
        buf.write("\3\2\2\2\u01a1\u01a2\5j\66\2\u01a2\u01a3\t\4\2\2\u01a3")
        buf.write("\u01a4\5j\66\2\u01a4\u01a7\3\2\2\2\u01a5\u01a7\5j\66\2")
        buf.write("\u01a6\u01a1\3\2\2\2\u01a6\u01a5\3\2\2\2\u01a7i\3\2\2")
        buf.write("\2\u01a8\u01a9\b\66\1\2\u01a9\u01aa\5l\67\2\u01aa\u01b0")
        buf.write("\3\2\2\2\u01ab\u01ac\f\4\2\2\u01ac\u01ad\t\5\2\2\u01ad")
        buf.write("\u01af\5l\67\2\u01ae\u01ab\3\2\2\2\u01af\u01b2\3\2\2\2")
        buf.write("\u01b0\u01ae\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1k\3\2\2")
        buf.write("\2\u01b2\u01b0\3\2\2\2\u01b3\u01b4\b\67\1\2\u01b4\u01b5")
        buf.write("\5n8\2\u01b5\u01bb\3\2\2\2\u01b6\u01b7\f\4\2\2\u01b7\u01b8")
        buf.write("\t\6\2\2\u01b8\u01ba\5n8\2\u01b9\u01b6\3\2\2\2\u01ba\u01bd")
        buf.write("\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc")
        buf.write("m\3\2\2\2\u01bd\u01bb\3\2\2\2\u01be\u01bf\b8\1\2\u01bf")
        buf.write("\u01c0\5p9\2\u01c0\u01c6\3\2\2\2\u01c1\u01c2\f\4\2\2\u01c2")
        buf.write("\u01c3\t\7\2\2\u01c3\u01c5\5p9\2\u01c4\u01c1\3\2\2\2\u01c5")
        buf.write("\u01c8\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c6\u01c7\3\2\2\2")
        buf.write("\u01c7o\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c9\u01ca\7\26\2")
        buf.write("\2\u01ca\u01cd\5p9\2\u01cb\u01cd\5r:\2\u01cc\u01c9\3\2")
        buf.write("\2\2\u01cc\u01cb\3\2\2\2\u01cdq\3\2\2\2\u01ce\u01cf\7")
        buf.write("\32\2\2\u01cf\u01d2\5r:\2\u01d0\u01d2\5t;\2\u01d1\u01ce")
        buf.write("\3\2\2\2\u01d1\u01d0\3\2\2\2\u01d2s\3\2\2\2\u01d3\u01d6")
        buf.write("\5\30\r\2\u01d4\u01d6\5v<\2\u01d5\u01d3\3\2\2\2\u01d5")
        buf.write("\u01d4\3\2\2\2\u01d6u\3\2\2\2\u01d7\u01df\5\2\2\2\u01d8")
        buf.write("\u01df\7/\2\2\u01d9\u01da\7\'\2\2\u01da\u01db\5f\64\2")
        buf.write("\u01db\u01dc\7(\2\2\u01dc\u01df\3\2\2\2\u01dd\u01df\5")
        buf.write("\36\20\2\u01de\u01d7\3\2\2\2\u01de\u01d8\3\2\2\2\u01de")
        buf.write("\u01d9\3\2\2\2\u01de\u01dd\3\2\2\2\u01dfw\3\2\2\2\61}")
        buf.write("\u0083\u008a\u008f\u0092\u0096\u00a0\u00a6\u00ae\u00b3")
        buf.write("\u00bf\u00c6\u00cf\u00d6\u00df\u00e6\u00ec\u00f4\u0100")
        buf.write("\u0105\u0108\u010e\u0113\u011e\u0125\u012c\u0134\u013c")
        buf.write("\u014b\u0152\u0156\u015c\u0162\u0175\u0182\u018e\u0190")
        buf.write("\u0198\u019f\u01a6\u01b0\u01bb\u01c6\u01cc\u01d1\u01d5")
        buf.write("\u01de")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'true'", "'false'", "'number'", "'bool'", 
                     "'string'", "'return'", "'var'", "'dynamic'", "'func'", 
                     "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "<INVALID>", "'end'", "'not'", 
                     "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'='", "'<-'", "'=='", "'!='", "'<'", "'>'", "'<='", 
                     "'>='", "'...'", "'('", "')'", "'['", "']'", "','", 
                     "'\n'" ]

    symbolicNames = [ "<INVALID>", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
                      "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", 
                      "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", 
                      "END", "NOT", "AND", "OR", "PLUS", "MINUS", "MULT", 
                      "DIV", "MOD", "EQUAL", "LEFTARR", "EQUALEQUAL", "NOTEQUAL", 
                      "LESS", "GREATER", "LESSOREQUAL", "GREATEROREQUAL", 
                      "ELLIPSIS", "LBracket", "RBracket", "LSBracket", "RSBracket", 
                      "COMMA", "NEWLINE", "NumberLit", "StringLit", "IDENTIFIER", 
                      "COMMENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_literal = 0
    RULE_program = 1
    RULE_declaration = 2
    RULE_function = 3
    RULE_function1 = 4
    RULE_arrayDeclaration = 5
    RULE_arrayDim = 6
    RULE_arrayAssign = 7
    RULE_arrayElementList = 8
    RULE_arrayList = 9
    RULE_literalList = 10
    RULE_elementAccessExpr = 11
    RULE_arrExpr = 12
    RULE_indexList = 13
    RULE_functionCall = 14
    RULE_functionArgsList = 15
    RULE_argsPrime = 16
    RULE_arg = 17
    RULE_assignStatement = 18
    RULE_scalarAssignStatement = 19
    RULE_arrayAssignStatement = 20
    RULE_statement = 21
    RULE_variableDeclaration = 22
    RULE_normalDeclaration = 23
    RULE_varType = 24
    RULE_varDecl = 25
    RULE_dynamicDecl = 26
    RULE_variableInitialization = 27
    RULE_paramDeclList = 28
    RULE_paramDeclPrime = 29
    RULE_paramDeclAtom = 30
    RULE_functionDecl = 31
    RULE_functionPreDecl = 32
    RULE_paramDecl = 33
    RULE_functionBody = 34
    RULE_ifStatement = 35
    RULE_elifStatementList = 36
    RULE_elifStatementPrime = 37
    RULE_elifStatement = 38
    RULE_elseStatement = 39
    RULE_forStatement = 40
    RULE_updateExpr = 41
    RULE_breakStatement = 42
    RULE_continueStatement = 43
    RULE_returnStatement = 44
    RULE_functionCallStatement = 45
    RULE_blockStatement = 46
    RULE_blockStatementBody = 47
    RULE_nullableListOfStatement = 48
    RULE_expressionList = 49
    RULE_expression = 50
    RULE_expression1 = 51
    RULE_expression2 = 52
    RULE_expression3 = 53
    RULE_expression4 = 54
    RULE_expression5 = 55
    RULE_expression6 = 56
    RULE_expression7 = 57
    RULE_operands = 58

    ruleNames =  [ "literal", "program", "declaration", "function", "function1", 
                   "arrayDeclaration", "arrayDim", "arrayAssign", "arrayElementList", 
                   "arrayList", "literalList", "elementAccessExpr", "arrExpr", 
                   "indexList", "functionCall", "functionArgsList", "argsPrime", 
                   "arg", "assignStatement", "scalarAssignStatement", "arrayAssignStatement", 
                   "statement", "variableDeclaration", "normalDeclaration", 
                   "varType", "varDecl", "dynamicDecl", "variableInitialization", 
                   "paramDeclList", "paramDeclPrime", "paramDeclAtom", "functionDecl", 
                   "functionPreDecl", "paramDecl", "functionBody", "ifStatement", 
                   "elifStatementList", "elifStatementPrime", "elifStatement", 
                   "elseStatement", "forStatement", "updateExpr", "breakStatement", 
                   "continueStatement", "returnStatement", "functionCallStatement", 
                   "blockStatement", "blockStatementBody", "nullableListOfStatement", 
                   "expressionList", "expression", "expression1", "expression2", 
                   "expression3", "expression4", "expression5", "expression6", 
                   "expression7", "operands" ]

    EOF = Token.EOF
    TRUE=1
    FALSE=2
    NUMBER=3
    BOOL=4
    STRING=5
    RETURN=6
    VAR=7
    DYNAMIC=8
    FUNC=9
    FOR=10
    UNTIL=11
    BY=12
    BREAK=13
    CONTINUE=14
    IF=15
    ELSE=16
    ELIF=17
    BEGIN=18
    END=19
    NOT=20
    AND=21
    OR=22
    PLUS=23
    MINUS=24
    MULT=25
    DIV=26
    MOD=27
    EQUAL=28
    LEFTARR=29
    EQUALEQUAL=30
    NOTEQUAL=31
    LESS=32
    GREATER=33
    LESSOREQUAL=34
    GREATEROREQUAL=35
    ELLIPSIS=36
    LBracket=37
    RBracket=38
    LSBracket=39
    RSBracket=40
    COMMA=41
    NEWLINE=42
    NumberLit=43
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




    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NumberLit(self):
            return self.getToken(ZCodeParser.NumberLit, 0)

        def TRUE(self):
            return self.getToken(ZCodeParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ZCodeParser.FALSE, 0)

        def StringLit(self):
            return self.getToken(ZCodeParser.StringLit, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ZCodeParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.NumberLit) | (1 << ZCodeParser.StringLit))) != 0)):
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


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.DeclarationContext,i)


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
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 120
                self.match(ZCodeParser.NEWLINE)
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING) | (1 << ZCodeParser.VAR) | (1 << ZCodeParser.DYNAMIC) | (1 << ZCodeParser.FUNC))) != 0):
                self.state = 126
                self.declaration()
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 132
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionContext,0)


        def variableDeclaration(self):
            return self.getTypedRuleContext(ZCodeParser.VariableDeclarationContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = ZCodeParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.FUNC]:
                self.state = 134
                self.function()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.state = 135
                self.variableDeclaration()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 144
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEWLINE]:
                self.state = 139 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 138
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 141 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZCodeParser.NEWLINE):
                        break

                pass
            elif token in [ZCodeParser.EOF]:
                self.state = 143
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


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function1(self):
            return self.getTypedRuleContext(ZCodeParser.Function1Context,0)


        def functionPreDecl(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionPreDeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = ZCodeParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_function)
        try:
            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.function1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.functionPreDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionDecl(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionDeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction1" ):
                return visitor.visitFunction1(self)
            else:
                return visitor.visitChildren(self)




    def function1(self):

        localctx = ZCodeParser.Function1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_function1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.functionDecl()
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

        def arrayAssign(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayAssignContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayDeclaration" ):
                return visitor.visitArrayDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def arrayDeclaration(self):

        localctx = ZCodeParser.ArrayDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_arrayDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.varType()
            self.state = 153
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 154
            self.match(ZCodeParser.LSBracket)
            self.state = 155
            self.arrayDim()
            self.state = 156
            self.match(ZCodeParser.RSBracket)
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LEFTARR:
                self.state = 157
                self.arrayAssign()


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
        self.enterRule(localctx, 12, self.RULE_arrayDim)
        try:
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
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


    class ArrayAssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFTARR(self):
            return self.getToken(ZCodeParser.LEFTARR, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def LSBracket(self):
            return self.getToken(ZCodeParser.LSBracket, 0)

        def arrayElementList(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayElementListContext,0)


        def RSBracket(self):
            return self.getToken(ZCodeParser.RSBracket, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayAssign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayAssign" ):
                return visitor.visitArrayAssign(self)
            else:
                return visitor.visitChildren(self)




    def arrayAssign(self):

        localctx = ZCodeParser.ArrayAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_arrayAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(ZCodeParser.LEFTARR)
            self.state = 172
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LSBracket]:
                self.state = 167
                self.match(ZCodeParser.LSBracket)
                self.state = 168
                self.arrayElementList()
                self.state = 169
                self.match(ZCodeParser.RSBracket)
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.NOT, ZCodeParser.MINUS, ZCodeParser.LBracket, ZCodeParser.NumberLit, ZCodeParser.StringLit, ZCodeParser.IDENTIFIER]:
                self.state = 171
                self.expression()
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


    class ArrayElementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literalList(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralListContext,0)


        def arrayList(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayListContext,0)


        def expressionList(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayElementList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayElementList" ):
                return visitor.visitArrayElementList(self)
            else:
                return visitor.visitChildren(self)




    def arrayElementList(self):

        localctx = ZCodeParser.ArrayElementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_arrayElementList)
        try:
            self.state = 177
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.literalList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.arrayList()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 176
                self.expressionList()
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

        def LSBracket(self):
            return self.getToken(ZCodeParser.LSBracket, 0)

        def arrayElementList(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayElementListContext,0)


        def RSBracket(self):
            return self.getToken(ZCodeParser.RSBracket, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def arrayList(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayListContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayList" ):
                return visitor.visitArrayList(self)
            else:
                return visitor.visitChildren(self)




    def arrayList(self):

        localctx = ZCodeParser.ArrayListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_arrayList)
        try:
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.match(ZCodeParser.LSBracket)
                self.state = 180
                self.arrayElementList()
                self.state = 181
                self.match(ZCodeParser.RSBracket)
                self.state = 182
                self.match(ZCodeParser.COMMA)
                self.state = 183
                self.arrayList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                self.match(ZCodeParser.LSBracket)
                self.state = 186
                self.arrayElementList()
                self.state = 187
                self.match(ZCodeParser.RSBracket)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def literalList(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralListContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_literalList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralList" ):
                return visitor.visitLiteralList(self)
            else:
                return visitor.visitChildren(self)




    def literalList(self):

        localctx = ZCodeParser.LiteralListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_literalList)
        try:
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.literal()
                self.state = 192
                self.match(ZCodeParser.COMMA)
                self.state = 193
                self.literalList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 195
                self.literal()
                pass


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

        def indexList(self):
            return self.getTypedRuleContext(ZCodeParser.IndexListContext,0)


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
        self.enterRule(localctx, 22, self.RULE_elementAccessExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.arrExpr()
            self.state = 199
            self.match(ZCodeParser.LSBracket)
            self.state = 200
            self.indexList()
            self.state = 201
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


        def getRuleIndex(self):
            return ZCodeParser.RULE_arrExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrExpr" ):
                return visitor.visitArrExpr(self)
            else:
                return visitor.visitChildren(self)




    def arrExpr(self):

        localctx = ZCodeParser.ArrExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_arrExpr)
        try:
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
                self.functionCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def indexList(self):
            return self.getTypedRuleContext(ZCodeParser.IndexListContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_indexList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexList" ):
                return visitor.visitIndexList(self)
            else:
                return visitor.visitChildren(self)




    def indexList(self):

        localctx = ZCodeParser.IndexListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_indexList)
        try:
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.expression()
                self.state = 208
                self.match(ZCodeParser.COMMA)
                self.state = 209
                self.indexList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 211
                self.expression()
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
        self.enterRule(localctx, 28, self.RULE_functionCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 215
            self.match(ZCodeParser.LBracket)
            self.state = 216
            self.functionArgsList()
            self.state = 217
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
        self.enterRule(localctx, 30, self.RULE_functionArgsList)
        try:
            self.state = 221
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.NOT, ZCodeParser.MINUS, ZCodeParser.LBracket, ZCodeParser.NumberLit, ZCodeParser.StringLit, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
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
        self.enterRule(localctx, 32, self.RULE_argsPrime)
        try:
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.arg()
                self.state = 224
                self.match(ZCodeParser.COMMA)
                self.state = 225
                self.argsPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
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
        self.enterRule(localctx, 34, self.RULE_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalarAssignStatement(self):
            return self.getTypedRuleContext(ZCodeParser.ScalarAssignStatementContext,0)


        def arrayAssignStatement(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayAssignStatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStatement" ):
                return visitor.visitAssignStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignStatement(self):

        localctx = ZCodeParser.AssignStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_assignStatement)
        try:
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.scalarAssignStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.arrayAssignStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScalarAssignStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LEFTARR(self):
            return self.getToken(ZCodeParser.LEFTARR, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_scalarAssignStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalarAssignStatement" ):
                return visitor.visitScalarAssignStatement(self)
            else:
                return visitor.visitChildren(self)




    def scalarAssignStatement(self):

        localctx = ZCodeParser.ScalarAssignStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_scalarAssignStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 237
            self.match(ZCodeParser.LEFTARR)
            self.state = 238
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayAssignStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayAssign(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayAssignContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def elementAccessExpr(self):
            return self.getTypedRuleContext(ZCodeParser.ElementAccessExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayAssignStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayAssignStatement" ):
                return visitor.visitArrayAssignStatement(self)
            else:
                return visitor.visitChildren(self)




    def arrayAssignStatement(self):

        localctx = ZCodeParser.ArrayAssignStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_arrayAssignStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 240
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 241
                self.elementAccessExpr()
                pass


            self.state = 244
            self.arrayAssign()
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

        def ifStatement(self):
            return self.getTypedRuleContext(ZCodeParser.IfStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(ZCodeParser.ForStatementContext,0)


        def breakStatement(self):
            return self.getTypedRuleContext(ZCodeParser.BreakStatementContext,0)


        def continueStatement(self):
            return self.getTypedRuleContext(ZCodeParser.ContinueStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(ZCodeParser.ReturnStatementContext,0)


        def functionCallStatement(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionCallStatementContext,0)


        def blockStatement(self):
            return self.getTypedRuleContext(ZCodeParser.BlockStatementContext,0)


        def assignStatement(self):
            return self.getTypedRuleContext(ZCodeParser.AssignStatementContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

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
        self.enterRule(localctx, 42, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 246
                self.ifStatement()
                pass

            elif la_ == 2:
                self.state = 247
                self.forStatement()
                pass

            elif la_ == 3:
                self.state = 248
                self.breakStatement()
                pass

            elif la_ == 4:
                self.state = 249
                self.continueStatement()
                pass

            elif la_ == 5:
                self.state = 250
                self.returnStatement()
                pass

            elif la_ == 6:
                self.state = 251
                self.functionCallStatement()
                pass

            elif la_ == 7:
                self.state = 252
                self.blockStatement()
                pass

            elif la_ == 8:
                self.state = 253
                self.assignStatement()
                pass


            self.state = 262
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEWLINE]:
                self.state = 257 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 256
                        self.match(ZCodeParser.NEWLINE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 259 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

                pass
            elif token in [ZCodeParser.EOF]:
                self.state = 261
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
        self.enterRule(localctx, 44, self.RULE_variableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 264
                self.normalDeclaration()
                pass

            elif la_ == 2:
                self.state = 265
                self.arrayDeclaration()
                pass

            elif la_ == 3:
                self.state = 266
                self.varDecl()
                pass

            elif la_ == 4:
                self.state = 267
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


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

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
        self.enterRule(localctx, 46, self.RULE_normalDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.varType()
            self.state = 271
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 273
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LEFTARR:
                self.state = 272
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
        self.enterRule(localctx, 48, self.RULE_varType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
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

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

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
        self.enterRule(localctx, 50, self.RULE_varDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(ZCodeParser.VAR)
            self.state = 278
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 279
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

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

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
        self.enterRule(localctx, 52, self.RULE_dynamicDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(ZCodeParser.DYNAMIC)
            self.state = 282
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 284
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LEFTARR:
                self.state = 283
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
        self.enterRule(localctx, 54, self.RULE_variableInitialization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(ZCodeParser.LEFTARR)
            self.state = 287
            self.expression()
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
        self.enterRule(localctx, 56, self.RULE_paramDeclList)
        try:
            self.state = 291
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 289
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
        self.enterRule(localctx, 58, self.RULE_paramDeclPrime)
        try:
            self.state = 298
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 293
                self.paramDeclAtom()
                self.state = 294
                self.match(ZCodeParser.COMMA)
                self.state = 295
                self.paramDeclPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 297
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
        self.enterRule(localctx, 60, self.RULE_paramDeclAtom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.varType()
            self.state = 301
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 306
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LSBracket:
                self.state = 302
                self.match(ZCodeParser.LSBracket)
                self.state = 303
                self.arrayDim()
                self.state = 304
                self.match(ZCodeParser.RSBracket)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def paramDecl(self):
            return self.getTypedRuleContext(ZCodeParser.ParamDeclContext,0)


        def functionBody(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionBodyContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_functionDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDecl" ):
                return visitor.visitFunctionDecl(self)
            else:
                return visitor.visitChildren(self)




    def functionDecl(self):

        localctx = ZCodeParser.FunctionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(ZCodeParser.FUNC)
            self.state = 309
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 310
            self.paramDecl()
            self.state = 314
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 311
                self.match(ZCodeParser.NEWLINE)
                self.state = 316
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 317
            self.functionBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionPreDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def paramDecl(self):
            return self.getTypedRuleContext(ZCodeParser.ParamDeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_functionPreDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionPreDecl" ):
                return visitor.visitFunctionPreDecl(self)
            else:
                return visitor.visitChildren(self)




    def functionPreDecl(self):

        localctx = ZCodeParser.FunctionPreDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_functionPreDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(ZCodeParser.FUNC)
            self.state = 320
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 321
            self.paramDecl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBracket(self):
            return self.getToken(ZCodeParser.LBracket, 0)

        def paramDeclList(self):
            return self.getTypedRuleContext(ZCodeParser.ParamDeclListContext,0)


        def RBracket(self):
            return self.getToken(ZCodeParser.RBracket, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_paramDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamDecl" ):
                return visitor.visitParamDecl(self)
            else:
                return visitor.visitChildren(self)




    def paramDecl(self):

        localctx = ZCodeParser.ParamDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_paramDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.match(ZCodeParser.LBracket)
            self.state = 324
            self.paramDeclList()
            self.state = 325
            self.match(ZCodeParser.RBracket)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockStatement(self):
            return self.getTypedRuleContext(ZCodeParser.BlockStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(ZCodeParser.ReturnStatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_functionBody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionBody" ):
                return visitor.visitFunctionBody(self)
            else:
                return visitor.visitChildren(self)




    def functionBody(self):

        localctx = ZCodeParser.FunctionBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_functionBody)
        try:
            self.state = 329
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 327
                self.blockStatement()
                pass
            elif token in [ZCodeParser.RETURN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 328
                self.returnStatement()
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

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


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
        self.enterRule(localctx, 70, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(ZCodeParser.IF)
            self.state = 332
            self.expression()
            self.state = 333
            self.statement()
            self.state = 334
            self.elifStatementList()
            self.state = 336
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ELSE:
                self.state = 335
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
        self.enterRule(localctx, 72, self.RULE_elifStatementList)
        try:
            self.state = 340
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ELIF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.elifStatementPrime()
                pass
            elif token in [ZCodeParser.EOF, ZCodeParser.ELSE, ZCodeParser.NEWLINE]:
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


        def elifStatementPrime(self):
            return self.getTypedRuleContext(ZCodeParser.ElifStatementPrimeContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_elifStatementPrime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifStatementPrime" ):
                return visitor.visitElifStatementPrime(self)
            else:
                return visitor.visitChildren(self)




    def elifStatementPrime(self):

        localctx = ZCodeParser.ElifStatementPrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_elifStatementPrime)
        self._la = 0 # Token type
        try:
            self.state = 352
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 342
                self.elifStatement()
                self.state = 346
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZCodeParser.NEWLINE:
                    self.state = 343
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 348
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 349
                self.elifStatementPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 351
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

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


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
        self.enterRule(localctx, 76, self.RULE_elifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.match(ZCodeParser.ELIF)
            self.state = 355
            self.expression()
            self.state = 356
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

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


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
        self.enterRule(localctx, 78, self.RULE_elseStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.match(ZCodeParser.ELSE)
            self.state = 359
            self.expression()
            self.state = 360
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

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def updateExpr(self):
            return self.getTypedRuleContext(ZCodeParser.UpdateExprContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_forStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = ZCodeParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.match(ZCodeParser.FOR)
            self.state = 363
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 364
            self.match(ZCodeParser.UNTIL)
            self.state = 365
            self.expression()
            self.state = 366
            self.match(ZCodeParser.BY)
            self.state = 367
            self.updateExpr()
            self.state = 371
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 368
                self.match(ZCodeParser.NEWLINE)
                self.state = 373
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 374
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
        self.enterRule(localctx, 82, self.RULE_updateExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
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
        self.enterRule(localctx, 84, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
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
        self.enterRule(localctx, 86, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
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
        self.enterRule(localctx, 88, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.match(ZCodeParser.RETURN)
            self.state = 384
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.LBracket) | (1 << ZCodeParser.NumberLit) | (1 << ZCodeParser.StringLit) | (1 << ZCodeParser.IDENTIFIER))) != 0):
                self.state = 383
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
        self.enterRule(localctx, 90, self.RULE_functionCallStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
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

        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def blockStatementBody(self):
            return self.getTypedRuleContext(ZCodeParser.BlockStatementBodyContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_blockStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStatement" ):
                return visitor.visitBlockStatement(self)
            else:
                return visitor.visitChildren(self)




    def blockStatement(self):

        localctx = ZCodeParser.BlockStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_blockStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.match(ZCodeParser.BEGIN)

            self.state = 389
            self.blockStatementBody()
            self.state = 390
            self.match(ZCodeParser.END)
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
        self.enterRule(localctx, 94, self.RULE_blockStatementBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
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

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StatementContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StatementContext,i)


        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.DeclarationContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_nullableListOfStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullableListOfStatement" ):
                return visitor.visitNullableListOfStatement(self)
            else:
                return visitor.visitChildren(self)




    def nullableListOfStatement(self):

        localctx = ZCodeParser.NullableListOfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_nullableListOfStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING) | (1 << ZCodeParser.RETURN) | (1 << ZCodeParser.VAR) | (1 << ZCodeParser.DYNAMIC) | (1 << ZCodeParser.FUNC) | (1 << ZCodeParser.FOR) | (1 << ZCodeParser.BREAK) | (1 << ZCodeParser.CONTINUE) | (1 << ZCodeParser.IF) | (1 << ZCodeParser.BEGIN) | (1 << ZCodeParser.IDENTIFIER))) != 0):
                self.state = 396
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.RETURN, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                    self.state = 394
                    self.statement()
                    pass
                elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FUNC]:
                    self.state = 395
                    self.declaration()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 400
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def expressionList(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expressionList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionList" ):
                return visitor.visitExpressionList(self)
            else:
                return visitor.visitChildren(self)




    def expressionList(self):

        localctx = ZCodeParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_expressionList)
        try:
            self.state = 406
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 401
                self.expression()
                self.state = 402
                self.match(ZCodeParser.COMMA)
                self.state = 403
                self.expressionList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 405
                self.expression()
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

        def expression1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expression1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expression1Context,i)


        def ELLIPSIS(self):
            return self.getToken(ZCodeParser.ELLIPSIS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = ZCodeParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_expression)
        try:
            self.state = 413
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 408
                self.expression1()
                self.state = 409
                self.match(ZCodeParser.ELLIPSIS)
                self.state = 410
                self.expression1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 412
                self.expression1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expression2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expression2Context,i)


        def EQUAL(self):
            return self.getToken(ZCodeParser.EQUAL, 0)

        def EQUALEQUAL(self):
            return self.getToken(ZCodeParser.EQUALEQUAL, 0)

        def NOTEQUAL(self):
            return self.getToken(ZCodeParser.NOTEQUAL, 0)

        def LESS(self):
            return self.getToken(ZCodeParser.LESS, 0)

        def LESSOREQUAL(self):
            return self.getToken(ZCodeParser.LESSOREQUAL, 0)

        def GREATER(self):
            return self.getToken(ZCodeParser.GREATER, 0)

        def GREATEROREQUAL(self):
            return self.getToken(ZCodeParser.GREATEROREQUAL, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression1" ):
                return visitor.visitExpression1(self)
            else:
                return visitor.visitChildren(self)




    def expression1(self):

        localctx = ZCodeParser.Expression1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_expression1)
        self._la = 0 # Token type
        try:
            self.state = 420
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 415
                self.expression2(0)
                self.state = 416
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQUAL) | (1 << ZCodeParser.EQUALEQUAL) | (1 << ZCodeParser.NOTEQUAL) | (1 << ZCodeParser.LESS) | (1 << ZCodeParser.GREATER) | (1 << ZCodeParser.LESSOREQUAL) | (1 << ZCodeParser.GREATEROREQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 417
                self.expression2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 419
                self.expression2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression3(self):
            return self.getTypedRuleContext(ZCodeParser.Expression3Context,0)


        def expression2(self):
            return self.getTypedRuleContext(ZCodeParser.Expression2Context,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression2" ):
                return visitor.visitExpression2(self)
            else:
                return visitor.visitChildren(self)



    def expression2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expression2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 104
        self.enterRecursionRule(localctx, 104, self.RULE_expression2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 430
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 425
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 426
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 427
                    self.expression3(0) 
                self.state = 432
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

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
            return self.getTypedRuleContext(ZCodeParser.Expression4Context,0)


        def expression3(self):
            return self.getTypedRuleContext(ZCodeParser.Expression3Context,0)


        def PLUS(self):
            return self.getToken(ZCodeParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression3" ):
                return visitor.visitExpression3(self)
            else:
                return visitor.visitChildren(self)



    def expression3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expression3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 106
        self.enterRecursionRule(localctx, 106, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 441
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 436
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 437
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.PLUS or _la==ZCodeParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 438
                    self.expression4(0) 
                self.state = 443
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

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
            return self.getTypedRuleContext(ZCodeParser.Expression5Context,0)


        def expression4(self):
            return self.getTypedRuleContext(ZCodeParser.Expression4Context,0)


        def MULT(self):
            return self.getToken(ZCodeParser.MULT, 0)

        def DIV(self):
            return self.getToken(ZCodeParser.DIV, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression4" ):
                return visitor.visitExpression4(self)
            else:
                return visitor.visitChildren(self)



    def expression4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expression4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 108
        self.enterRecursionRule(localctx, 108, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 452
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 447
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 448
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MULT) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 449
                    self.expression5() 
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


    class Expression5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def expression5(self):
            return self.getTypedRuleContext(ZCodeParser.Expression5Context,0)


        def expression6(self):
            return self.getTypedRuleContext(ZCodeParser.Expression6Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression5" ):
                return visitor.visitExpression5(self)
            else:
                return visitor.visitChildren(self)




    def expression5(self):

        localctx = ZCodeParser.Expression5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_expression5)
        try:
            self.state = 458
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 455
                self.match(ZCodeParser.NOT)
                self.state = 456
                self.expression5()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.MINUS, ZCodeParser.LBracket, ZCodeParser.NumberLit, ZCodeParser.StringLit, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 457
                self.expression6()
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

        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def expression6(self):
            return self.getTypedRuleContext(ZCodeParser.Expression6Context,0)


        def expression7(self):
            return self.getTypedRuleContext(ZCodeParser.Expression7Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression6" ):
                return visitor.visitExpression6(self)
            else:
                return visitor.visitChildren(self)




    def expression6(self):

        localctx = ZCodeParser.Expression6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_expression6)
        try:
            self.state = 463
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 460
                self.match(ZCodeParser.MINUS)
                self.state = 461
                self.expression6()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.LBracket, ZCodeParser.NumberLit, ZCodeParser.StringLit, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 462
                self.expression7()
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


    class Expression7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elementAccessExpr(self):
            return self.getTypedRuleContext(ZCodeParser.ElementAccessExprContext,0)


        def operands(self):
            return self.getTypedRuleContext(ZCodeParser.OperandsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression7" ):
                return visitor.visitExpression7(self)
            else:
                return visitor.visitChildren(self)




    def expression7(self):

        localctx = ZCodeParser.Expression7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_expression7)
        try:
            self.state = 467
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 465
                self.elementAccessExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 466
                self.operands()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LBracket(self):
            return self.getToken(ZCodeParser.LBracket, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RBracket(self):
            return self.getToken(ZCodeParser.RBracket, 0)

        def functionCall(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_operands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)




    def operands(self):

        localctx = ZCodeParser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_operands)
        try:
            self.state = 476
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 469
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 470
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 471
                self.match(ZCodeParser.LBracket)
                self.state = 472
                self.expression()
                self.state = 473
                self.match(ZCodeParser.RBracket)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 475
                self.functionCall()
                pass


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
        self._predicates[52] = self.expression2_sempred
        self._predicates[53] = self.expression3_sempred
        self._predicates[54] = self.expression4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression2_sempred(self, localctx:Expression2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression3_sempred(self, localctx:Expression3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression4_sempred(self, localctx:Expression4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




