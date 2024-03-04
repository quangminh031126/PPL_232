# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65")
        buf.write("\u0203\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\3\2\3\2\3\3\3\3\3\3\5\3\u008e\n\3\3\4\3\4\3\4\5\4\u0093")
        buf.write("\n\4\3\5\3\5\3\5\3\5\3\6\3\6\5\6\u009b\n\6\3\7\3\7\5\7")
        buf.write("\u009f\n\7\3\b\3\b\3\b\3\b\3\b\5\b\u00a6\n\b\3\t\3\t\5")
        buf.write("\t\u00aa\n\t\3\n\3\n\5\n\u00ae\n\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\5\13\u00b5\n\13\3\f\3\f\5\f\u00b9\n\f\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\5\16\u00c3\n\16\3\17\3\17")
        buf.write("\3\17\3\17\5\17\u00c9\n\17\3\20\3\20\3\20\3\20\3\20\3")
        buf.write("\20\5\20\u00d1\n\20\3\21\3\21\3\21\5\21\u00d6\n\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u00e2")
        buf.write("\n\22\3\23\3\23\3\23\3\23\3\23\5\23\u00e9\n\23\3\24\3")
        buf.write("\24\3\24\3\24\3\24\3\25\3\25\5\25\u00f2\n\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\5\26\u00f9\n\26\3\27\3\27\3\27\3\27\3")
        buf.write("\27\3\30\3\30\5\30\u0102\n\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\5\31\u0109\n\31\3\32\3\32\3\33\3\33\5\33\u010f\n\33\3")
        buf.write("\34\3\34\3\34\3\34\3\35\3\35\5\35\u0117\n\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u0123\n")
        buf.write("\36\3\36\6\36\u0126\n\36\r\36\16\36\u0127\3\36\5\36\u012b")
        buf.write("\n\36\3\37\3\37\3\37\3\37\5\37\u0131\n\37\3 \3 \3 \5 ")
        buf.write("\u0136\n \3!\3!\3\"\3\"\3\"\3\"\3#\3#\3#\5#\u0141\n#\3")
        buf.write("$\3$\3$\3%\3%\5%\u0148\n%\3&\3&\3&\3&\3&\5&\u014f\n&\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\5\'\u0157\n\'\3(\3(\3(\3(\3(\3")
        buf.write("(\3)\3)\3)\3)\3)\3)\3)\3)\3*\3*\3+\3+\5+\u016b\n+\3,\3")
        buf.write(",\3,\3,\3,\3,\5,\u0173\n,\3-\3-\5-\u0177\n-\3.\3.\3.\3")
        buf.write(".\3.\5.\u017e\n.\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3")
        buf.write("\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\62")
        buf.write("\3\62\3\63\3\63\3\64\3\64\3\65\3\65\5\65\u019b\n\65\3")
        buf.write("\66\3\66\3\67\3\67\3\67\3\67\38\38\39\39\59\u01a7\n9\3")
        buf.write(":\3:\5:\u01ab\n:\3:\3:\3:\3:\3:\5:\u01b2\n:\5:\u01b4\n")
        buf.write(":\3;\3;\3;\3;\3;\5;\u01bb\n;\3<\3<\3<\3<\3<\5<\u01c2\n")
        buf.write("<\3=\3=\3=\3=\3=\5=\u01c9\n=\3>\3>\3>\3>\3>\3>\7>\u01d1")
        buf.write("\n>\f>\16>\u01d4\13>\3?\3?\3?\3?\3?\3?\7?\u01dc\n?\f?")
        buf.write("\16?\u01df\13?\3@\3@\3@\3@\3@\3@\7@\u01e7\n@\f@\16@\u01ea")
        buf.write("\13@\3A\3A\3A\5A\u01ef\nA\3B\3B\3B\5B\u01f4\nB\3C\3C\5")
        buf.write("C\u01f8\nC\3D\3D\3D\3D\3D\3D\3D\5D\u0201\nD\3D\2\5z|~")
        buf.write("E\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082")
        buf.write("\u0084\u0086\2\b\3\2-/\3\2\5\7\4\2\36\36 %\3\2\27\30\3")
        buf.write("\2\31\32\3\2\33\35\2\u01fb\2\u0088\3\2\2\2\4\u008d\3\2")
        buf.write("\2\2\6\u0092\3\2\2\2\b\u0094\3\2\2\2\n\u009a\3\2\2\2\f")
        buf.write("\u009e\3\2\2\2\16\u00a5\3\2\2\2\20\u00a9\3\2\2\2\22\u00ad")
        buf.write("\3\2\2\2\24\u00b4\3\2\2\2\26\u00b8\3\2\2\2\30\u00ba\3")
        buf.write("\2\2\2\32\u00bc\3\2\2\2\34\u00c8\3\2\2\2\36\u00ca\3\2")
        buf.write("\2\2 \u00d5\3\2\2\2\"\u00e1\3\2\2\2$\u00e8\3\2\2\2&\u00ea")
        buf.write("\3\2\2\2(\u00f1\3\2\2\2*\u00f8\3\2\2\2,\u00fa\3\2\2\2")
        buf.write(".\u0101\3\2\2\2\60\u0108\3\2\2\2\62\u010a\3\2\2\2\64\u010e")
        buf.write("\3\2\2\2\66\u0110\3\2\2\28\u0116\3\2\2\2:\u0122\3\2\2")
        buf.write("\2<\u0130\3\2\2\2>\u0132\3\2\2\2@\u0137\3\2\2\2B\u0139")
        buf.write("\3\2\2\2D\u013d\3\2\2\2F\u0142\3\2\2\2H\u0147\3\2\2\2")
        buf.write("J\u014e\3\2\2\2L\u0150\3\2\2\2N\u0158\3\2\2\2P\u015e\3")
        buf.write("\2\2\2R\u0166\3\2\2\2T\u016a\3\2\2\2V\u016c\3\2\2\2X\u0176")
        buf.write("\3\2\2\2Z\u017d\3\2\2\2\\\u017f\3\2\2\2^\u0184\3\2\2\2")
        buf.write("`\u0189\3\2\2\2b\u0192\3\2\2\2d\u0194\3\2\2\2f\u0196\3")
        buf.write("\2\2\2h\u0198\3\2\2\2j\u019c\3\2\2\2l\u019e\3\2\2\2n\u01a2")
        buf.write("\3\2\2\2p\u01a6\3\2\2\2r\u01b3\3\2\2\2t\u01ba\3\2\2\2")
        buf.write("v\u01c1\3\2\2\2x\u01c8\3\2\2\2z\u01ca\3\2\2\2|\u01d5\3")
        buf.write("\2\2\2~\u01e0\3\2\2\2\u0080\u01ee\3\2\2\2\u0082\u01f3")
        buf.write("\3\2\2\2\u0084\u01f7\3\2\2\2\u0086\u0200\3\2\2\2\u0088")
        buf.write("\u0089\t\2\2\2\u0089\3\3\2\2\2\u008a\u008b\7,\2\2\u008b")
        buf.write("\u008e\5\4\3\2\u008c\u008e\3\2\2\2\u008d\u008a\3\2\2\2")
        buf.write("\u008d\u008c\3\2\2\2\u008e\5\3\2\2\2\u008f\u0090\7,\2")
        buf.write("\2\u0090\u0093\5\6\4\2\u0091\u0093\7,\2\2\u0092\u008f")
        buf.write("\3\2\2\2\u0092\u0091\3\2\2\2\u0093\7\3\2\2\2\u0094\u0095")
        buf.write("\5\4\3\2\u0095\u0096\5\f\7\2\u0096\u0097\7\2\2\3\u0097")
        buf.write("\t\3\2\2\2\u0098\u009b\5\26\f\2\u0099\u009b\5<\37\2\u009a")
        buf.write("\u0098\3\2\2\2\u009a\u0099\3\2\2\2\u009b\13\3\2\2\2\u009c")
        buf.write("\u009f\5\16\b\2\u009d\u009f\3\2\2\2\u009e\u009c\3\2\2")
        buf.write("\2\u009e\u009d\3\2\2\2\u009f\r\3\2\2\2\u00a0\u00a1\5\n")
        buf.write("\6\2\u00a1\u00a2\5\6\4\2\u00a2\u00a3\5\16\b\2\u00a3\u00a6")
        buf.write("\3\2\2\2\u00a4\u00a6\5\n\6\2\u00a5\u00a0\3\2\2\2\u00a5")
        buf.write("\u00a4\3\2\2\2\u00a6\17\3\2\2\2\u00a7\u00aa\5\26\f\2\u00a8")
        buf.write("\u00aa\5<\37\2\u00a9\u00a7\3\2\2\2\u00a9\u00a8\3\2\2\2")
        buf.write("\u00aa\21\3\2\2\2\u00ab\u00ae\5\24\13\2\u00ac\u00ae\3")
        buf.write("\2\2\2\u00ad\u00ab\3\2\2\2\u00ad\u00ac\3\2\2\2\u00ae\23")
        buf.write("\3\2\2\2\u00af\u00b0\5\20\t\2\u00b0\u00b1\5\6\4\2\u00b1")
        buf.write("\u00b2\5\24\13\2\u00b2\u00b5\3\2\2\2\u00b3\u00b5\5\20")
        buf.write("\t\2\u00b4\u00af\3\2\2\2\u00b4\u00b3\3\2\2\2\u00b5\25")
        buf.write("\3\2\2\2\u00b6\u00b9\5\30\r\2\u00b7\u00b9\5N(\2\u00b8")
        buf.write("\u00b6\3\2\2\2\u00b8\u00b7\3\2\2\2\u00b9\27\3\2\2\2\u00ba")
        buf.write("\u00bb\5P)\2\u00bb\31\3\2\2\2\u00bc\u00bd\5@!\2\u00bd")
        buf.write("\u00be\7\60\2\2\u00be\u00bf\7)\2\2\u00bf\u00c0\5\34\17")
        buf.write("\2\u00c0\u00c2\7*\2\2\u00c1\u00c3\5\36\20\2\u00c2\u00c1")
        buf.write("\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\33\3\2\2\2\u00c4\u00c5")
        buf.write("\7-\2\2\u00c5\u00c6\7+\2\2\u00c6\u00c9\5\34\17\2\u00c7")
        buf.write("\u00c9\7-\2\2\u00c8\u00c4\3\2\2\2\u00c8\u00c7\3\2\2\2")
        buf.write("\u00c9\35\3\2\2\2\u00ca\u00d0\7\37\2\2\u00cb\u00cc\7)")
        buf.write("\2\2\u00cc\u00cd\5 \21\2\u00cd\u00ce\7*\2\2\u00ce\u00d1")
        buf.write("\3\2\2\2\u00cf\u00d1\5v<\2\u00d0\u00cb\3\2\2\2\u00d0\u00cf")
        buf.write("\3\2\2\2\u00d1\37\3\2\2\2\u00d2\u00d6\5$\23\2\u00d3\u00d6")
        buf.write("\5\"\22\2\u00d4\u00d6\5t;\2\u00d5\u00d2\3\2\2\2\u00d5")
        buf.write("\u00d3\3\2\2\2\u00d5\u00d4\3\2\2\2\u00d6!\3\2\2\2\u00d7")
        buf.write("\u00d8\7)\2\2\u00d8\u00d9\5 \21\2\u00d9\u00da\7*\2\2\u00da")
        buf.write("\u00db\7+\2\2\u00db\u00dc\5\"\22\2\u00dc\u00e2\3\2\2\2")
        buf.write("\u00dd\u00de\7)\2\2\u00de\u00df\5 \21\2\u00df\u00e0\7")
        buf.write("*\2\2\u00e0\u00e2\3\2\2\2\u00e1\u00d7\3\2\2\2\u00e1\u00dd")
        buf.write("\3\2\2\2\u00e2#\3\2\2\2\u00e3\u00e4\5\2\2\2\u00e4\u00e5")
        buf.write("\7+\2\2\u00e5\u00e6\5$\23\2\u00e6\u00e9\3\2\2\2\u00e7")
        buf.write("\u00e9\5\2\2\2\u00e8\u00e3\3\2\2\2\u00e8\u00e7\3\2\2\2")
        buf.write("\u00e9%\3\2\2\2\u00ea\u00eb\5(\25\2\u00eb\u00ec\7)\2\2")
        buf.write("\u00ec\u00ed\5*\26\2\u00ed\u00ee\7*\2\2\u00ee\'\3\2\2")
        buf.write("\2\u00ef\u00f2\7\60\2\2\u00f0\u00f2\5,\27\2\u00f1\u00ef")
        buf.write("\3\2\2\2\u00f1\u00f0\3\2\2\2\u00f2)\3\2\2\2\u00f3\u00f4")
        buf.write("\5v<\2\u00f4\u00f5\7+\2\2\u00f5\u00f6\5*\26\2\u00f6\u00f9")
        buf.write("\3\2\2\2\u00f7\u00f9\5v<\2\u00f8\u00f3\3\2\2\2\u00f8\u00f7")
        buf.write("\3\2\2\2\u00f9+\3\2\2\2\u00fa\u00fb\7\60\2\2\u00fb\u00fc")
        buf.write("\7\'\2\2\u00fc\u00fd\5.\30\2\u00fd\u00fe\7(\2\2\u00fe")
        buf.write("-\3\2\2\2\u00ff\u0102\5\60\31\2\u0100\u0102\3\2\2\2\u0101")
        buf.write("\u00ff\3\2\2\2\u0101\u0100\3\2\2\2\u0102/\3\2\2\2\u0103")
        buf.write("\u0104\5\62\32\2\u0104\u0105\7+\2\2\u0105\u0106\5\60\31")
        buf.write("\2\u0106\u0109\3\2\2\2\u0107\u0109\5\62\32\2\u0108\u0103")
        buf.write("\3\2\2\2\u0108\u0107\3\2\2\2\u0109\61\3\2\2\2\u010a\u010b")
        buf.write("\5v<\2\u010b\63\3\2\2\2\u010c\u010f\5\66\34\2\u010d\u010f")
        buf.write("\58\35\2\u010e\u010c\3\2\2\2\u010e\u010d\3\2\2\2\u010f")
        buf.write("\65\3\2\2\2\u0110\u0111\7\60\2\2\u0111\u0112\7\37\2\2")
        buf.write("\u0112\u0113\5v<\2\u0113\67\3\2\2\2\u0114\u0117\7\60\2")
        buf.write("\2\u0115\u0117\5&\24\2\u0116\u0114\3\2\2\2\u0116\u0115")
        buf.write("\3\2\2\2\u0117\u0118\3\2\2\2\u0118\u0119\5\36\20\2\u0119")
        buf.write("9\3\2\2\2\u011a\u0123\5V,\2\u011b\u0123\5`\61\2\u011c")
        buf.write("\u0123\5d\63\2\u011d\u0123\5f\64\2\u011e\u0123\5h\65\2")
        buf.write("\u011f\u0123\5j\66\2\u0120\u0123\5l\67\2\u0121\u0123\5")
        buf.write("\64\33\2\u0122\u011a\3\2\2\2\u0122\u011b\3\2\2\2\u0122")
        buf.write("\u011c\3\2\2\2\u0122\u011d\3\2\2\2\u0122\u011e\3\2\2\2")
        buf.write("\u0122\u011f\3\2\2\2\u0122\u0120\3\2\2\2\u0122\u0121\3")
        buf.write("\2\2\2\u0123\u012a\3\2\2\2\u0124\u0126\7,\2\2\u0125\u0124")
        buf.write("\3\2\2\2\u0126\u0127\3\2\2\2\u0127\u0125\3\2\2\2\u0127")
        buf.write("\u0128\3\2\2\2\u0128\u012b\3\2\2\2\u0129\u012b\7\2\2\3")
        buf.write("\u012a\u0125\3\2\2\2\u012a\u0129\3\2\2\2\u012b;\3\2\2")
        buf.write("\2\u012c\u0131\5> \2\u012d\u0131\5\32\16\2\u012e\u0131")
        buf.write("\5B\"\2\u012f\u0131\5D#\2\u0130\u012c\3\2\2\2\u0130\u012d")
        buf.write("\3\2\2\2\u0130\u012e\3\2\2\2\u0130\u012f\3\2\2\2\u0131")
        buf.write("=\3\2\2\2\u0132\u0133\5@!\2\u0133\u0135\7\60\2\2\u0134")
        buf.write("\u0136\5F$\2\u0135\u0134\3\2\2\2\u0135\u0136\3\2\2\2\u0136")
        buf.write("?\3\2\2\2\u0137\u0138\t\3\2\2\u0138A\3\2\2\2\u0139\u013a")
        buf.write("\7\t\2\2\u013a\u013b\7\60\2\2\u013b\u013c\5F$\2\u013c")
        buf.write("C\3\2\2\2\u013d\u013e\7\n\2\2\u013e\u0140\7\60\2\2\u013f")
        buf.write("\u0141\5F$\2\u0140\u013f\3\2\2\2\u0140\u0141\3\2\2\2\u0141")
        buf.write("E\3\2\2\2\u0142\u0143\7\37\2\2\u0143\u0144\5v<\2\u0144")
        buf.write("G\3\2\2\2\u0145\u0148\5J&\2\u0146\u0148\3\2\2\2\u0147")
        buf.write("\u0145\3\2\2\2\u0147\u0146\3\2\2\2\u0148I\3\2\2\2\u0149")
        buf.write("\u014a\5L\'\2\u014a\u014b\7+\2\2\u014b\u014c\5J&\2\u014c")
        buf.write("\u014f\3\2\2\2\u014d\u014f\5L\'\2\u014e\u0149\3\2\2\2")
        buf.write("\u014e\u014d\3\2\2\2\u014fK\3\2\2\2\u0150\u0151\5@!\2")
        buf.write("\u0151\u0156\7\60\2\2\u0152\u0153\7)\2\2\u0153\u0154\5")
        buf.write("\34\17\2\u0154\u0155\7*\2\2\u0155\u0157\3\2\2\2\u0156")
        buf.write("\u0152\3\2\2\2\u0156\u0157\3\2\2\2\u0157M\3\2\2\2\u0158")
        buf.write("\u0159\7\13\2\2\u0159\u015a\7\60\2\2\u015a\u015b\7\'\2")
        buf.write("\2\u015b\u015c\5R*\2\u015c\u015d\7(\2\2\u015dO\3\2\2\2")
        buf.write("\u015e\u015f\7\13\2\2\u015f\u0160\7\60\2\2\u0160\u0161")
        buf.write("\7\'\2\2\u0161\u0162\5R*\2\u0162\u0163\7(\2\2\u0163\u0164")
        buf.write("\5\4\3\2\u0164\u0165\5T+\2\u0165Q\3\2\2\2\u0166\u0167")
        buf.write("\5H%\2\u0167S\3\2\2\2\u0168\u016b\5l\67\2\u0169\u016b")
        buf.write("\5h\65\2\u016a\u0168\3\2\2\2\u016a\u0169\3\2\2\2\u016b")
        buf.write("U\3\2\2\2\u016c\u016d\7\21\2\2\u016d\u016e\5v<\2\u016e")
        buf.write("\u016f\5\4\3\2\u016f\u0170\5:\36\2\u0170\u0172\5X-\2\u0171")
        buf.write("\u0173\5^\60\2\u0172\u0171\3\2\2\2\u0172\u0173\3\2\2\2")
        buf.write("\u0173W\3\2\2\2\u0174\u0177\5Z.\2\u0175\u0177\3\2\2\2")
        buf.write("\u0176\u0174\3\2\2\2\u0176\u0175\3\2\2\2\u0177Y\3\2\2")
        buf.write("\2\u0178\u0179\5\\/\2\u0179\u017a\5\4\3\2\u017a\u017b")
        buf.write("\5Z.\2\u017b\u017e\3\2\2\2\u017c\u017e\5\\/\2\u017d\u0178")
        buf.write("\3\2\2\2\u017d\u017c\3\2\2\2\u017e[\3\2\2\2\u017f\u0180")
        buf.write("\7\23\2\2\u0180\u0181\5v<\2\u0181\u0182\5\4\3\2\u0182")
        buf.write("\u0183\5:\36\2\u0183]\3\2\2\2\u0184\u0185\7\22\2\2\u0185")
        buf.write("\u0186\5v<\2\u0186\u0187\5\4\3\2\u0187\u0188\5:\36\2\u0188")
        buf.write("_\3\2\2\2\u0189\u018a\7\f\2\2\u018a\u018b\7\60\2\2\u018b")
        buf.write("\u018c\7\r\2\2\u018c\u018d\5v<\2\u018d\u018e\7\16\2\2")
        buf.write("\u018e\u018f\5b\62\2\u018f\u0190\5\4\3\2\u0190\u0191\5")
        buf.write(":\36\2\u0191a\3\2\2\2\u0192\u0193\5v<\2\u0193c\3\2\2\2")
        buf.write("\u0194\u0195\7\17\2\2\u0195e\3\2\2\2\u0196\u0197\7\20")
        buf.write("\2\2\u0197g\3\2\2\2\u0198\u019a\7\b\2\2\u0199\u019b\5")
        buf.write("v<\2\u019a\u0199\3\2\2\2\u019a\u019b\3\2\2\2\u019bi\3")
        buf.write("\2\2\2\u019c\u019d\5,\27\2\u019dk\3\2\2\2\u019e\u019f")
        buf.write("\7\24\2\2\u019f\u01a0\5n8\2\u01a0\u01a1\7\25\2\2\u01a1")
        buf.write("m\3\2\2\2\u01a2\u01a3\5p9\2\u01a3o\3\2\2\2\u01a4\u01a7")
        buf.write("\5r:\2\u01a5\u01a7\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a6\u01a5")
        buf.write("\3\2\2\2\u01a7q\3\2\2\2\u01a8\u01ab\5:\36\2\u01a9\u01ab")
        buf.write("\5\20\t\2\u01aa\u01a8\3\2\2\2\u01aa\u01a9\3\2\2\2\u01ab")
        buf.write("\u01ac\3\2\2\2\u01ac\u01ad\5\6\4\2\u01ad\u01ae\5r:\2\u01ae")
        buf.write("\u01b4\3\2\2\2\u01af\u01b2\5:\36\2\u01b0\u01b2\5\20\t")
        buf.write("\2\u01b1\u01af\3\2\2\2\u01b1\u01b0\3\2\2\2\u01b2\u01b4")
        buf.write("\3\2\2\2\u01b3\u01aa\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b4")
        buf.write("s\3\2\2\2\u01b5\u01b6\5v<\2\u01b6\u01b7\7+\2\2\u01b7\u01b8")
        buf.write("\5t;\2\u01b8\u01bb\3\2\2\2\u01b9\u01bb\5v<\2\u01ba\u01b5")
        buf.write("\3\2\2\2\u01ba\u01b9\3\2\2\2\u01bbu\3\2\2\2\u01bc\u01bd")
        buf.write("\5x=\2\u01bd\u01be\7&\2\2\u01be\u01bf\5x=\2\u01bf\u01c2")
        buf.write("\3\2\2\2\u01c0\u01c2\5x=\2\u01c1\u01bc\3\2\2\2\u01c1\u01c0")
        buf.write("\3\2\2\2\u01c2w\3\2\2\2\u01c3\u01c4\5z>\2\u01c4\u01c5")
        buf.write("\t\4\2\2\u01c5\u01c6\5z>\2\u01c6\u01c9\3\2\2\2\u01c7\u01c9")
        buf.write("\5z>\2\u01c8\u01c3\3\2\2\2\u01c8\u01c7\3\2\2\2\u01c9y")
        buf.write("\3\2\2\2\u01ca\u01cb\b>\1\2\u01cb\u01cc\5|?\2\u01cc\u01d2")
        buf.write("\3\2\2\2\u01cd\u01ce\f\4\2\2\u01ce\u01cf\t\5\2\2\u01cf")
        buf.write("\u01d1\5|?\2\u01d0\u01cd\3\2\2\2\u01d1\u01d4\3\2\2\2\u01d2")
        buf.write("\u01d0\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d3{\3\2\2\2\u01d4")
        buf.write("\u01d2\3\2\2\2\u01d5\u01d6\b?\1\2\u01d6\u01d7\5~@\2\u01d7")
        buf.write("\u01dd\3\2\2\2\u01d8\u01d9\f\4\2\2\u01d9\u01da\t\6\2\2")
        buf.write("\u01da\u01dc\5~@\2\u01db\u01d8\3\2\2\2\u01dc\u01df\3\2")
        buf.write("\2\2\u01dd\u01db\3\2\2\2\u01dd\u01de\3\2\2\2\u01de}\3")
        buf.write("\2\2\2\u01df\u01dd\3\2\2\2\u01e0\u01e1\b@\1\2\u01e1\u01e2")
        buf.write("\5\u0080A\2\u01e2\u01e8\3\2\2\2\u01e3\u01e4\f\4\2\2\u01e4")
        buf.write("\u01e5\t\7\2\2\u01e5\u01e7\5\u0080A\2\u01e6\u01e3\3\2")
        buf.write("\2\2\u01e7\u01ea\3\2\2\2\u01e8\u01e6\3\2\2\2\u01e8\u01e9")
        buf.write("\3\2\2\2\u01e9\177\3\2\2\2\u01ea\u01e8\3\2\2\2\u01eb\u01ec")
        buf.write("\7\26\2\2\u01ec\u01ef\5\u0080A\2\u01ed\u01ef\5\u0082B")
        buf.write("\2\u01ee\u01eb\3\2\2\2\u01ee\u01ed\3\2\2\2\u01ef\u0081")
        buf.write("\3\2\2\2\u01f0\u01f1\7\32\2\2\u01f1\u01f4\5\u0082B\2\u01f2")
        buf.write("\u01f4\5\u0084C\2\u01f3\u01f0\3\2\2\2\u01f3\u01f2\3\2")
        buf.write("\2\2\u01f4\u0083\3\2\2\2\u01f5\u01f8\5&\24\2\u01f6\u01f8")
        buf.write("\5\u0086D\2\u01f7\u01f5\3\2\2\2\u01f7\u01f6\3\2\2\2\u01f8")
        buf.write("\u0085\3\2\2\2\u01f9\u0201\5\2\2\2\u01fa\u0201\7\60\2")
        buf.write("\2\u01fb\u01fc\7\'\2\2\u01fc\u01fd\5v<\2\u01fd\u01fe\7")
        buf.write("(\2\2\u01fe\u0201\3\2\2\2\u01ff\u0201\5,\27\2\u0200\u01f9")
        buf.write("\3\2\2\2\u0200\u01fa\3\2\2\2\u0200\u01fb\3\2\2\2\u0200")
        buf.write("\u01ff\3\2\2\2\u0201\u0087\3\2\2\2\63\u008d\u0092\u009a")
        buf.write("\u009e\u00a5\u00a9\u00ad\u00b4\u00b8\u00c2\u00c8\u00d0")
        buf.write("\u00d5\u00e1\u00e8\u00f1\u00f8\u0101\u0108\u010e\u0116")
        buf.write("\u0122\u0127\u012a\u0130\u0135\u0140\u0147\u014e\u0156")
        buf.write("\u016a\u0172\u0176\u017d\u019a\u01a6\u01aa\u01b1\u01b3")
        buf.write("\u01ba\u01c1\u01c8\u01d2\u01dd\u01e8\u01ee\u01f3\u01f7")
        buf.write("\u0200")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'true'", "'false'", "'number'", "'bool'", 
                     "'string'", "'return'", "'var'", "'dynamic'", "'func'", 
                     "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'not'", 
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
                      "COMMA", "NEWLINE", "NumberLit", "StringLit", "BoolLit", 
                      "IDENTIFIER", "COMMENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_literal = 0
    RULE_nullableListOfNEWLINE = 1
    RULE_listOfNEWLINE = 2
    RULE_program = 3
    RULE_globalLevelDecl = 4
    RULE_globalLevelDeclList = 5
    RULE_globalLevelDeclListPrime = 6
    RULE_blockLevelDecl = 7
    RULE_blockLevelDeclList = 8
    RULE_blockLevelDeclListPrime = 9
    RULE_functionDecl = 10
    RULE_functionDecl1 = 11
    RULE_arrayDeclaration = 12
    RULE_arrayDim = 13
    RULE_arrayAssign = 14
    RULE_arrayElementList = 15
    RULE_arrayList = 16
    RULE_literalList = 17
    RULE_elementAccessExpr = 18
    RULE_arrExpr = 19
    RULE_indexList = 20
    RULE_functionCall = 21
    RULE_functionArgsList = 22
    RULE_argsPrime = 23
    RULE_arg = 24
    RULE_assignStatement = 25
    RULE_scalarAssignStatement = 26
    RULE_arrayAssignStatement = 27
    RULE_statement = 28
    RULE_variableDeclaration = 29
    RULE_normalDeclaration = 30
    RULE_varType = 31
    RULE_varDecl = 32
    RULE_dynamicDecl = 33
    RULE_variableInitialization = 34
    RULE_paramDeclList = 35
    RULE_paramDeclPrime = 36
    RULE_paramDeclAtom = 37
    RULE_functionPreDecl = 38
    RULE_functionFullDecl = 39
    RULE_paramDecl = 40
    RULE_functionBody = 41
    RULE_ifStatement = 42
    RULE_elifStatementList = 43
    RULE_elifStatementPrime = 44
    RULE_elifStatement = 45
    RULE_elseStatement = 46
    RULE_forStatement = 47
    RULE_updateExpr = 48
    RULE_breakStatement = 49
    RULE_continueStatement = 50
    RULE_returnStatement = 51
    RULE_functionCallStatement = 52
    RULE_blockStatement = 53
    RULE_blockStatementBody = 54
    RULE_nullableListOfStatement = 55
    RULE_nullableListOfStatementPrime = 56
    RULE_expressionList = 57
    RULE_expression = 58
    RULE_expression1 = 59
    RULE_expression2 = 60
    RULE_expression3 = 61
    RULE_expression4 = 62
    RULE_expression5 = 63
    RULE_expression6 = 64
    RULE_expression7 = 65
    RULE_operands = 66

    ruleNames =  [ "literal", "nullableListOfNEWLINE", "listOfNEWLINE", 
                   "program", "globalLevelDecl", "globalLevelDeclList", 
                   "globalLevelDeclListPrime", "blockLevelDecl", "blockLevelDeclList", 
                   "blockLevelDeclListPrime", "functionDecl", "functionDecl1", 
                   "arrayDeclaration", "arrayDim", "arrayAssign", "arrayElementList", 
                   "arrayList", "literalList", "elementAccessExpr", "arrExpr", 
                   "indexList", "functionCall", "functionArgsList", "argsPrime", 
                   "arg", "assignStatement", "scalarAssignStatement", "arrayAssignStatement", 
                   "statement", "variableDeclaration", "normalDeclaration", 
                   "varType", "varDecl", "dynamicDecl", "variableInitialization", 
                   "paramDeclList", "paramDeclPrime", "paramDeclAtom", "functionPreDecl", 
                   "functionFullDecl", "paramDecl", "functionBody", "ifStatement", 
                   "elifStatementList", "elifStatementPrime", "elifStatement", 
                   "elseStatement", "forStatement", "updateExpr", "breakStatement", 
                   "continueStatement", "returnStatement", "functionCallStatement", 
                   "blockStatement", "blockStatementBody", "nullableListOfStatement", 
                   "nullableListOfStatementPrime", "expressionList", "expression", 
                   "expression1", "expression2", "expression3", "expression4", 
                   "expression5", "expression6", "expression7", "operands" ]

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
    BoolLit=45
    IDENTIFIER=46
    COMMENT=47
    WS=48
    ERROR_CHAR=49
    UNCLOSE_STRING=50
    ILLEGAL_ESCAPE=51

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

        def BoolLit(self):
            return self.getToken(ZCodeParser.BoolLit, 0)

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
            self.state = 134
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NumberLit) | (1 << ZCodeParser.StringLit) | (1 << ZCodeParser.BoolLit))) != 0)):
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
        self.enterRule(localctx, 2, self.RULE_nullableListOfNEWLINE)
        try:
            self.state = 139
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.match(ZCodeParser.NEWLINE)
                self.state = 137
                self.nullableListOfNEWLINE()
                pass
            elif token in [ZCodeParser.EOF, ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FUNC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.ELIF, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
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


    class ListOfNEWLINEContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def listOfNEWLINE(self):
            return self.getTypedRuleContext(ZCodeParser.ListOfNEWLINEContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_listOfNEWLINE

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListOfNEWLINE" ):
                return visitor.visitListOfNEWLINE(self)
            else:
                return visitor.visitChildren(self)




    def listOfNEWLINE(self):

        localctx = ZCodeParser.ListOfNEWLINEContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_listOfNEWLINE)
        try:
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.match(ZCodeParser.NEWLINE)
                self.state = 142
                self.listOfNEWLINE()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.match(ZCodeParser.NEWLINE)
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

        def nullableListOfNEWLINE(self):
            return self.getTypedRuleContext(ZCodeParser.NullableListOfNEWLINEContext,0)


        def globalLevelDeclList(self):
            return self.getTypedRuleContext(ZCodeParser.GlobalLevelDeclListContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.nullableListOfNEWLINE()
            self.state = 147
            self.globalLevelDeclList()
            self.state = 148
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GlobalLevelDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionDecl(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionDeclContext,0)


        def variableDeclaration(self):
            return self.getTypedRuleContext(ZCodeParser.VariableDeclarationContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_globalLevelDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlobalLevelDecl" ):
                return visitor.visitGlobalLevelDecl(self)
            else:
                return visitor.visitChildren(self)




    def globalLevelDecl(self):

        localctx = ZCodeParser.GlobalLevelDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_globalLevelDecl)
        try:
            self.state = 152
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.functionDecl()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.variableDeclaration()
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


    class GlobalLevelDeclListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def globalLevelDeclListPrime(self):
            return self.getTypedRuleContext(ZCodeParser.GlobalLevelDeclListPrimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_globalLevelDeclList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlobalLevelDeclList" ):
                return visitor.visitGlobalLevelDeclList(self)
            else:
                return visitor.visitChildren(self)




    def globalLevelDeclList(self):

        localctx = ZCodeParser.GlobalLevelDeclListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_globalLevelDeclList)
        try:
            self.state = 156
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.globalLevelDeclListPrime()
                pass
            elif token in [ZCodeParser.EOF]:
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


    class GlobalLevelDeclListPrimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def globalLevelDecl(self):
            return self.getTypedRuleContext(ZCodeParser.GlobalLevelDeclContext,0)


        def listOfNEWLINE(self):
            return self.getTypedRuleContext(ZCodeParser.ListOfNEWLINEContext,0)


        def globalLevelDeclListPrime(self):
            return self.getTypedRuleContext(ZCodeParser.GlobalLevelDeclListPrimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_globalLevelDeclListPrime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlobalLevelDeclListPrime" ):
                return visitor.visitGlobalLevelDeclListPrime(self)
            else:
                return visitor.visitChildren(self)




    def globalLevelDeclListPrime(self):

        localctx = ZCodeParser.GlobalLevelDeclListPrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_globalLevelDeclListPrime)
        try:
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.globalLevelDecl()
                self.state = 159
                self.listOfNEWLINE()
                self.state = 160
                self.globalLevelDeclListPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.globalLevelDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockLevelDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionDecl(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionDeclContext,0)


        def variableDeclaration(self):
            return self.getTypedRuleContext(ZCodeParser.VariableDeclarationContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_blockLevelDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockLevelDecl" ):
                return visitor.visitBlockLevelDecl(self)
            else:
                return visitor.visitChildren(self)




    def blockLevelDecl(self):

        localctx = ZCodeParser.BlockLevelDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_blockLevelDecl)
        try:
            self.state = 167
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.functionDecl()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.variableDeclaration()
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


    class BlockLevelDeclListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockLevelDeclListPrime(self):
            return self.getTypedRuleContext(ZCodeParser.BlockLevelDeclListPrimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_blockLevelDeclList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockLevelDeclList" ):
                return visitor.visitBlockLevelDeclList(self)
            else:
                return visitor.visitChildren(self)




    def blockLevelDeclList(self):

        localctx = ZCodeParser.BlockLevelDeclListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_blockLevelDeclList)
        try:
            self.state = 171
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.blockLevelDeclListPrime()
                pass
            elif token in [ZCodeParser.EOF]:
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


    class BlockLevelDeclListPrimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockLevelDecl(self):
            return self.getTypedRuleContext(ZCodeParser.BlockLevelDeclContext,0)


        def listOfNEWLINE(self):
            return self.getTypedRuleContext(ZCodeParser.ListOfNEWLINEContext,0)


        def blockLevelDeclListPrime(self):
            return self.getTypedRuleContext(ZCodeParser.BlockLevelDeclListPrimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_blockLevelDeclListPrime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockLevelDeclListPrime" ):
                return visitor.visitBlockLevelDeclListPrime(self)
            else:
                return visitor.visitChildren(self)




    def blockLevelDeclListPrime(self):

        localctx = ZCodeParser.BlockLevelDeclListPrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_blockLevelDeclListPrime)
        try:
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.blockLevelDecl()
                self.state = 174
                self.listOfNEWLINE()
                self.state = 175
                self.blockLevelDeclListPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
                self.blockLevelDecl()
                pass


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

        def functionDecl1(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionDecl1Context,0)


        def functionPreDecl(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionPreDeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_functionDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDecl" ):
                return visitor.visitFunctionDecl(self)
            else:
                return visitor.visitChildren(self)




    def functionDecl(self):

        localctx = ZCodeParser.FunctionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_functionDecl)
        try:
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.functionDecl1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.functionPreDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDecl1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionFullDecl(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionFullDeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_functionDecl1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDecl1" ):
                return visitor.visitFunctionDecl1(self)
            else:
                return visitor.visitChildren(self)




    def functionDecl1(self):

        localctx = ZCodeParser.FunctionDecl1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_functionDecl1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.functionFullDecl()
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
        self.enterRule(localctx, 24, self.RULE_arrayDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.varType()
            self.state = 187
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 188
            self.match(ZCodeParser.LSBracket)
            self.state = 189
            self.arrayDim()
            self.state = 190
            self.match(ZCodeParser.RSBracket)
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LEFTARR:
                self.state = 191
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
        self.enterRule(localctx, 26, self.RULE_arrayDim)
        try:
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.match(ZCodeParser.NumberLit)
                self.state = 195
                self.match(ZCodeParser.COMMA)
                self.state = 196
                self.arrayDim()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
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
        self.enterRule(localctx, 28, self.RULE_arrayAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(ZCodeParser.LEFTARR)
            self.state = 206
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LSBracket]:
                self.state = 201
                self.match(ZCodeParser.LSBracket)
                self.state = 202
                self.arrayElementList()
                self.state = 203
                self.match(ZCodeParser.RSBracket)
                pass
            elif token in [ZCodeParser.NOT, ZCodeParser.MINUS, ZCodeParser.LBracket, ZCodeParser.NumberLit, ZCodeParser.StringLit, ZCodeParser.BoolLit, ZCodeParser.IDENTIFIER]:
                self.state = 205
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
        self.enterRule(localctx, 30, self.RULE_arrayElementList)
        try:
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.literalList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                self.arrayList()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 210
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
        self.enterRule(localctx, 32, self.RULE_arrayList)
        try:
            self.state = 223
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.match(ZCodeParser.LSBracket)
                self.state = 214
                self.arrayElementList()
                self.state = 215
                self.match(ZCodeParser.RSBracket)
                self.state = 216
                self.match(ZCodeParser.COMMA)
                self.state = 217
                self.arrayList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
                self.match(ZCodeParser.LSBracket)
                self.state = 220
                self.arrayElementList()
                self.state = 221
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
        self.enterRule(localctx, 34, self.RULE_literalList)
        try:
            self.state = 230
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.literal()
                self.state = 226
                self.match(ZCodeParser.COMMA)
                self.state = 227
                self.literalList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 229
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
        self.enterRule(localctx, 36, self.RULE_elementAccessExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.arrExpr()
            self.state = 233
            self.match(ZCodeParser.LSBracket)
            self.state = 234
            self.indexList()
            self.state = 235
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
        self.enterRule(localctx, 38, self.RULE_arrExpr)
        try:
            self.state = 239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
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
        self.enterRule(localctx, 40, self.RULE_indexList)
        try:
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 241
                self.expression()
                self.state = 242
                self.match(ZCodeParser.COMMA)
                self.state = 243
                self.indexList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
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
        self.enterRule(localctx, 42, self.RULE_functionCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 249
            self.match(ZCodeParser.LBracket)
            self.state = 250
            self.functionArgsList()
            self.state = 251
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
        self.enterRule(localctx, 44, self.RULE_functionArgsList)
        try:
            self.state = 255
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT, ZCodeParser.MINUS, ZCodeParser.LBracket, ZCodeParser.NumberLit, ZCodeParser.StringLit, ZCodeParser.BoolLit, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
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
        self.enterRule(localctx, 46, self.RULE_argsPrime)
        try:
            self.state = 262
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                self.arg()
                self.state = 258
                self.match(ZCodeParser.COMMA)
                self.state = 259
                self.argsPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 261
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
        self.enterRule(localctx, 48, self.RULE_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
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
        self.enterRule(localctx, 50, self.RULE_assignStatement)
        try:
            self.state = 268
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.scalarAssignStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 267
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
        self.enterRule(localctx, 52, self.RULE_scalarAssignStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 271
            self.match(ZCodeParser.LEFTARR)
            self.state = 272
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
        self.enterRule(localctx, 54, self.RULE_arrayAssignStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 274
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 275
                self.elementAccessExpr()
                pass


            self.state = 278
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
        self.enterRule(localctx, 56, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 280
                self.ifStatement()
                pass

            elif la_ == 2:
                self.state = 281
                self.forStatement()
                pass

            elif la_ == 3:
                self.state = 282
                self.breakStatement()
                pass

            elif la_ == 4:
                self.state = 283
                self.continueStatement()
                pass

            elif la_ == 5:
                self.state = 284
                self.returnStatement()
                pass

            elif la_ == 6:
                self.state = 285
                self.functionCallStatement()
                pass

            elif la_ == 7:
                self.state = 286
                self.blockStatement()
                pass

            elif la_ == 8:
                self.state = 287
                self.assignStatement()
                pass


            self.state = 296
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEWLINE]:
                self.state = 291 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 290
                        self.match(ZCodeParser.NEWLINE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 293 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

                pass
            elif token in [ZCodeParser.EOF]:
                self.state = 295
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
        self.enterRule(localctx, 58, self.RULE_variableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 298
                self.normalDeclaration()
                pass

            elif la_ == 2:
                self.state = 299
                self.arrayDeclaration()
                pass

            elif la_ == 3:
                self.state = 300
                self.varDecl()
                pass

            elif la_ == 4:
                self.state = 301
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
        self.enterRule(localctx, 60, self.RULE_normalDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.varType()
            self.state = 305
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 307
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LEFTARR:
                self.state = 306
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
        self.enterRule(localctx, 62, self.RULE_varType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
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
        self.enterRule(localctx, 64, self.RULE_varDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.match(ZCodeParser.VAR)
            self.state = 312
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 313
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
        self.enterRule(localctx, 66, self.RULE_dynamicDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(ZCodeParser.DYNAMIC)
            self.state = 316
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LEFTARR:
                self.state = 317
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
        self.enterRule(localctx, 68, self.RULE_variableInitialization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.match(ZCodeParser.LEFTARR)
            self.state = 321
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
        self.enterRule(localctx, 70, self.RULE_paramDeclList)
        try:
            self.state = 325
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 323
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
        self.enterRule(localctx, 72, self.RULE_paramDeclPrime)
        try:
            self.state = 332
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 327
                self.paramDeclAtom()
                self.state = 328
                self.match(ZCodeParser.COMMA)
                self.state = 329
                self.paramDeclPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 331
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
        self.enterRule(localctx, 74, self.RULE_paramDeclAtom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.varType()
            self.state = 335
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 340
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LSBracket:
                self.state = 336
                self.match(ZCodeParser.LSBracket)
                self.state = 337
                self.arrayDim()
                self.state = 338
                self.match(ZCodeParser.RSBracket)


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

        def LBracket(self):
            return self.getToken(ZCodeParser.LBracket, 0)

        def paramDecl(self):
            return self.getTypedRuleContext(ZCodeParser.ParamDeclContext,0)


        def RBracket(self):
            return self.getToken(ZCodeParser.RBracket, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_functionPreDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionPreDecl" ):
                return visitor.visitFunctionPreDecl(self)
            else:
                return visitor.visitChildren(self)




    def functionPreDecl(self):

        localctx = ZCodeParser.FunctionPreDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_functionPreDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(ZCodeParser.FUNC)
            self.state = 343
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 344
            self.match(ZCodeParser.LBracket)
            self.state = 345
            self.paramDecl()
            self.state = 346
            self.match(ZCodeParser.RBracket)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionFullDeclContext(ParserRuleContext):
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

        def paramDecl(self):
            return self.getTypedRuleContext(ZCodeParser.ParamDeclContext,0)


        def RBracket(self):
            return self.getToken(ZCodeParser.RBracket, 0)

        def nullableListOfNEWLINE(self):
            return self.getTypedRuleContext(ZCodeParser.NullableListOfNEWLINEContext,0)


        def functionBody(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionBodyContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_functionFullDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionFullDecl" ):
                return visitor.visitFunctionFullDecl(self)
            else:
                return visitor.visitChildren(self)




    def functionFullDecl(self):

        localctx = ZCodeParser.FunctionFullDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_functionFullDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.match(ZCodeParser.FUNC)
            self.state = 349
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 350
            self.match(ZCodeParser.LBracket)
            self.state = 351
            self.paramDecl()
            self.state = 352
            self.match(ZCodeParser.RBracket)
            self.state = 353
            self.nullableListOfNEWLINE()
            self.state = 354
            self.functionBody()
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

        def paramDeclList(self):
            return self.getTypedRuleContext(ZCodeParser.ParamDeclListContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamDecl" ):
                return visitor.visitParamDecl(self)
            else:
                return visitor.visitChildren(self)




    def paramDecl(self):

        localctx = ZCodeParser.ParamDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_paramDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self.paramDeclList()
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
        self.enterRule(localctx, 82, self.RULE_functionBody)
        try:
            self.state = 360
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 358
                self.blockStatement()
                pass
            elif token in [ZCodeParser.RETURN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 359
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


        def nullableListOfNEWLINE(self):
            return self.getTypedRuleContext(ZCodeParser.NullableListOfNEWLINEContext,0)


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
        self.enterRule(localctx, 84, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.match(ZCodeParser.IF)
            self.state = 363
            self.expression()
            self.state = 364
            self.nullableListOfNEWLINE()
            self.state = 365
            self.statement()
            self.state = 366
            self.elifStatementList()
            self.state = 368
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ELSE:
                self.state = 367
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
        self.enterRule(localctx, 86, self.RULE_elifStatementList)
        try:
            self.state = 372
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ELIF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 370
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
        self.enterRule(localctx, 88, self.RULE_elifStatementPrime)
        try:
            self.state = 379
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.elifStatement()
                self.state = 375
                self.nullableListOfNEWLINE()
                self.state = 376
                self.elifStatementPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 378
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


        def nullableListOfNEWLINE(self):
            return self.getTypedRuleContext(ZCodeParser.NullableListOfNEWLINEContext,0)


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
        self.enterRule(localctx, 90, self.RULE_elifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.match(ZCodeParser.ELIF)
            self.state = 382
            self.expression()
            self.state = 383
            self.nullableListOfNEWLINE()
            self.state = 384
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


        def nullableListOfNEWLINE(self):
            return self.getTypedRuleContext(ZCodeParser.NullableListOfNEWLINEContext,0)


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
        self.enterRule(localctx, 92, self.RULE_elseStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.match(ZCodeParser.ELSE)
            self.state = 387
            self.expression()
            self.state = 388
            self.nullableListOfNEWLINE()
            self.state = 389
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
        self.enterRule(localctx, 94, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.match(ZCodeParser.FOR)
            self.state = 392
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 393
            self.match(ZCodeParser.UNTIL)
            self.state = 394
            self.expression()
            self.state = 395
            self.match(ZCodeParser.BY)
            self.state = 396
            self.updateExpr()
            self.state = 397
            self.nullableListOfNEWLINE()
            self.state = 398
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
        self.enterRule(localctx, 96, self.RULE_updateExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
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
        self.enterRule(localctx, 98, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
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
        self.enterRule(localctx, 100, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
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
        self.enterRule(localctx, 102, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.match(ZCodeParser.RETURN)
            self.state = 408
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NOT) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.LBracket) | (1 << ZCodeParser.NumberLit) | (1 << ZCodeParser.StringLit) | (1 << ZCodeParser.BoolLit) | (1 << ZCodeParser.IDENTIFIER))) != 0):
                self.state = 407
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
        self.enterRule(localctx, 104, self.RULE_functionCallStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
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
        self.enterRule(localctx, 106, self.RULE_blockStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self.match(ZCodeParser.BEGIN)

            self.state = 413
            self.blockStatementBody()
            self.state = 414
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
        self.enterRule(localctx, 108, self.RULE_blockStatementBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
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

        def nullableListOfStatementPrime(self):
            return self.getTypedRuleContext(ZCodeParser.NullableListOfStatementPrimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_nullableListOfStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullableListOfStatement" ):
                return visitor.visitNullableListOfStatement(self)
            else:
                return visitor.visitChildren(self)




    def nullableListOfStatement(self):

        localctx = ZCodeParser.NullableListOfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_nullableListOfStatement)
        try:
            self.state = 420
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FUNC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 418
                self.nullableListOfStatementPrime()
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


    class NullableListOfStatementPrimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listOfNEWLINE(self):
            return self.getTypedRuleContext(ZCodeParser.ListOfNEWLINEContext,0)


        def nullableListOfStatementPrime(self):
            return self.getTypedRuleContext(ZCodeParser.NullableListOfStatementPrimeContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def blockLevelDecl(self):
            return self.getTypedRuleContext(ZCodeParser.BlockLevelDeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_nullableListOfStatementPrime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullableListOfStatementPrime" ):
                return visitor.visitNullableListOfStatementPrime(self)
            else:
                return visitor.visitChildren(self)




    def nullableListOfStatementPrime(self):

        localctx = ZCodeParser.NullableListOfStatementPrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_nullableListOfStatementPrime)
        try:
            self.state = 433
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 424
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.RETURN, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                    self.state = 422
                    self.statement()
                    pass
                elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FUNC]:
                    self.state = 423
                    self.blockLevelDecl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 426
                self.listOfNEWLINE()
                self.state = 427
                self.nullableListOfStatementPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 431
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.RETURN, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                    self.state = 429
                    self.statement()
                    pass
                elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FUNC]:
                    self.state = 430
                    self.blockLevelDecl()
                    pass
                else:
                    raise NoViableAltException(self)

                pass


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
        self.enterRule(localctx, 114, self.RULE_expressionList)
        try:
            self.state = 440
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 435
                self.expression()
                self.state = 436
                self.match(ZCodeParser.COMMA)
                self.state = 437
                self.expressionList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 439
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
        self.enterRule(localctx, 116, self.RULE_expression)
        try:
            self.state = 447
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 442
                self.expression1()
                self.state = 443
                self.match(ZCodeParser.ELLIPSIS)
                self.state = 444
                self.expression1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 446
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
        self.enterRule(localctx, 118, self.RULE_expression1)
        self._la = 0 # Token type
        try:
            self.state = 454
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 449
                self.expression2(0)
                self.state = 450
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQUAL) | (1 << ZCodeParser.EQUALEQUAL) | (1 << ZCodeParser.NOTEQUAL) | (1 << ZCodeParser.LESS) | (1 << ZCodeParser.GREATER) | (1 << ZCodeParser.LESSOREQUAL) | (1 << ZCodeParser.GREATEROREQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 451
                self.expression2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 453
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
        _startState = 120
        self.enterRecursionRule(localctx, 120, self.RULE_expression2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 464
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 459
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 460
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 461
                    self.expression3(0) 
                self.state = 466
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

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
        _startState = 122
        self.enterRecursionRule(localctx, 122, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 475
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 470
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 471
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.PLUS or _la==ZCodeParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 472
                    self.expression4(0) 
                self.state = 477
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

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
        _startState = 124
        self.enterRecursionRule(localctx, 124, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 479
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 486
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 481
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 482
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MULT) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 483
                    self.expression5() 
                self.state = 488
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

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
        self.enterRule(localctx, 126, self.RULE_expression5)
        try:
            self.state = 492
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 489
                self.match(ZCodeParser.NOT)
                self.state = 490
                self.expression5()
                pass
            elif token in [ZCodeParser.MINUS, ZCodeParser.LBracket, ZCodeParser.NumberLit, ZCodeParser.StringLit, ZCodeParser.BoolLit, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 491
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
        self.enterRule(localctx, 128, self.RULE_expression6)
        try:
            self.state = 497
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 494
                self.match(ZCodeParser.MINUS)
                self.state = 495
                self.expression6()
                pass
            elif token in [ZCodeParser.LBracket, ZCodeParser.NumberLit, ZCodeParser.StringLit, ZCodeParser.BoolLit, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 496
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
        self.enterRule(localctx, 130, self.RULE_expression7)
        try:
            self.state = 501
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 499
                self.elementAccessExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 500
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
        self.enterRule(localctx, 132, self.RULE_operands)
        try:
            self.state = 510
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 503
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 504
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 505
                self.match(ZCodeParser.LBracket)
                self.state = 506
                self.expression()
                self.state = 507
                self.match(ZCodeParser.RBracket)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 509
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
        self._predicates[60] = self.expression2_sempred
        self._predicates[61] = self.expression3_sempred
        self._predicates[62] = self.expression4_sempred
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
         




