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
        buf.write("\u01fb\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\3\2\3\2\3\2\3\2\3\2\3\2\7\2")
        buf.write("\u0085\n\2\f\2\16\2\u0088\13\2\3\2\3\2\5\2\u008c\n\2\3")
        buf.write("\3\7\3\u008f\n\3\f\3\16\3\u0092\13\3\3\3\7\3\u0095\n\3")
        buf.write("\f\3\16\3\u0098\13\3\3\3\3\3\3\4\3\4\3\4\5\4\u009f\n\4")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3")
        buf.write("\6\5\6\u00af\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00c1\n\7\3\b\3\b\5\b\u00c5")
        buf.write("\n\b\3\t\3\t\3\t\3\t\5\t\u00cb\n\t\3\n\3\n\5\n\u00cf\n")
        buf.write("\n\3\13\3\13\3\13\3\13\5\13\u00d5\n\13\3\f\3\f\5\f\u00d9")
        buf.write("\n\f\3\r\3\r\3\r\3\r\5\r\u00df\n\r\3\16\3\16\5\16\u00e3")
        buf.write("\n\16\3\17\3\17\3\17\3\17\3\17\5\17\u00ea\n\17\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\7\20\u00f2\n\20\f\20\16\20\u00f5")
        buf.write("\13\20\3\21\3\21\3\21\3\21\3\21\3\21\7\21\u00fd\n\21\f")
        buf.write("\21\16\21\u0100\13\21\3\22\3\22\3\22\5\22\u0105\n\22\3")
        buf.write("\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\7\24\u010f\n\24")
        buf.write("\f\24\16\24\u0112\13\24\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\7\25\u011a\n\25\f\25\16\25\u011d\13\25\3\26\3\26\3\26")
        buf.write("\5\26\u0122\n\26\3\27\3\27\3\30\3\30\3\30\5\30\u0129\n")
        buf.write("\30\3\30\3\30\3\30\7\30\u012e\n\30\f\30\16\30\u0131\13")
        buf.write("\30\3\31\3\31\5\31\u0135\n\31\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\5\37\u014b\n\37\3 \3 \3 \3 \3 \5")
        buf.write(" \u0152\n \3!\3!\3!\3!\3!\3\"\3\"\5\"\u015b\n\"\3#\3#")
        buf.write("\3#\3#\3#\5#\u0162\n#\3$\3$\3%\3%\3%\3%\3%\3%\3%\5%\u016d")
        buf.write("\n%\3%\6%\u0170\n%\r%\16%\u0171\3&\3&\3&\3&\5&\u0178\n")
        buf.write("&\3\'\3\'\5\'\u017c\n\'\3(\3(\3)\3)\3)\3*\3*\5*\u0185")
        buf.write("\n*\3+\3+\3+\3,\3,\3,\3,\3,\3,\5,\u0190\n,\3-\3-\5-\u0194")
        buf.write("\n-\3.\3.\3.\3.\3.\5.\u019b\n.\3/\3/\3/\3/\3/\3/\5/\u01a3")
        buf.write("\n/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\5\60\u01ad")
        buf.write("\n\60\3\61\3\61\3\61\5\61\u01b2\n\61\3\62\3\62\3\62\3")
        buf.write("\62\3\62\5\62\u01b9\n\62\3\63\3\63\5\63\u01bd\n\63\3\64")
        buf.write("\3\64\3\64\3\64\3\64\5\64\u01c4\n\64\3\65\3\65\3\65\3")
        buf.write("\65\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write("\3\67\3\67\3\67\38\38\39\39\3:\3:\3;\3;\5;\u01df\n;\3")
        buf.write("<\3<\3=\3=\6=\u01e5\n=\r=\16=\u01e6\3=\3=\3=\6=\u01ec")
        buf.write("\n=\r=\16=\u01ed\3=\5=\u01f1\n=\3>\3>\3?\3?\3?\3?\5?\u01f9")
        buf.write("\n?\3?\2\7\36 &(.@\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjln")
        buf.write("prtvxz|\2\b\3\2\4\6\3\2\30\31\3\2\32\34\4\2,,//\4\2--")
        buf.write("//\4\2\35\35 $\2\u01fc\2~\3\2\2\2\4\u0090\3\2\2\2\6\u009e")
        buf.write("\3\2\2\2\b\u00a0\3\2\2\2\n\u00ae\3\2\2\2\f\u00c0\3\2\2")
        buf.write("\2\16\u00c4\3\2\2\2\20\u00ca\3\2\2\2\22\u00ce\3\2\2\2")
        buf.write("\24\u00d4\3\2\2\2\26\u00d8\3\2\2\2\30\u00de\3\2\2\2\32")
        buf.write("\u00e2\3\2\2\2\34\u00e9\3\2\2\2\36\u00eb\3\2\2\2 \u00f6")
        buf.write("\3\2\2\2\"\u0104\3\2\2\2$\u0106\3\2\2\2&\u0108\3\2\2\2")
        buf.write("(\u0113\3\2\2\2*\u0121\3\2\2\2,\u0123\3\2\2\2.\u0128\3")
        buf.write("\2\2\2\60\u0134\3\2\2\2\62\u0136\3\2\2\2\64\u013a\3\2")
        buf.write("\2\2\66\u013e\3\2\2\28\u0140\3\2\2\2:\u0142\3\2\2\2<\u014a")
        buf.write("\3\2\2\2>\u0151\3\2\2\2@\u0153\3\2\2\2B\u015a\3\2\2\2")
        buf.write("D\u0161\3\2\2\2F\u0163\3\2\2\2H\u016c\3\2\2\2J\u0177\3")
        buf.write("\2\2\2L\u0179\3\2\2\2N\u017d\3\2\2\2P\u017f\3\2\2\2R\u0182")
        buf.write("\3\2\2\2T\u0186\3\2\2\2V\u018f\3\2\2\2X\u0193\3\2\2\2")
        buf.write("Z\u019a\3\2\2\2\\\u019c\3\2\2\2^\u01a4\3\2\2\2`\u01b1")
        buf.write("\3\2\2\2b\u01b3\3\2\2\2d\u01bc\3\2\2\2f\u01c3\3\2\2\2")
        buf.write("h\u01c5\3\2\2\2j\u01c9\3\2\2\2l\u01cd\3\2\2\2n\u01d6\3")
        buf.write("\2\2\2p\u01d8\3\2\2\2r\u01da\3\2\2\2t\u01dc\3\2\2\2v\u01e0")
        buf.write("\3\2\2\2x\u01e2\3\2\2\2z\u01f2\3\2\2\2|\u01f8\3\2\2\2")
        buf.write("~\177\7\n\2\2\177\u0080\7\3\2\2\u0080\u0081\7&\2\2\u0081")
        buf.write("\u0082\5X-\2\u0082\u0086\7\'\2\2\u0083\u0085\7+\2\2\u0084")
        buf.write("\u0083\3\2\2\2\u0085\u0088\3\2\2\2\u0086\u0084\3\2\2\2")
        buf.write("\u0086\u0087\3\2\2\2\u0087\u008b\3\2\2\2\u0088\u0086\3")
        buf.write("\2\2\2\u0089\u008c\5t;\2\u008a\u008c\5x=\2\u008b\u0089")
        buf.write("\3\2\2\2\u008b\u008a\3\2\2\2\u008b\u008c\3\2\2\2\u008c")
        buf.write("\3\3\2\2\2\u008d\u008f\7+\2\2\u008e\u008d\3\2\2\2\u008f")
        buf.write("\u0092\3\2\2\2\u0090\u008e\3\2\2\2\u0090\u0091\3\2\2\2")
        buf.write("\u0091\u0096\3\2\2\2\u0092\u0090\3\2\2\2\u0093\u0095\5")
        buf.write("\6\4\2\u0094\u0093\3\2\2\2\u0095\u0098\3\2\2\2\u0096\u0094")
        buf.write("\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0099\3\2\2\2\u0098")
        buf.write("\u0096\3\2\2\2\u0099\u009a\7\2\2\3\u009a\5\3\2\2\2\u009b")
        buf.write("\u009f\5\2\2\2\u009c\u009f\5^\60\2\u009d\u009f\5P)\2\u009e")
        buf.write("\u009b\3\2\2\2\u009e\u009c\3\2\2\2\u009e\u009d\3\2\2\2")
        buf.write("\u009f\7\3\2\2\2\u00a0\u00a1\t\2\2\2\u00a1\u00a2\7/\2")
        buf.write("\2\u00a2\u00a3\7(\2\2\u00a3\u00a4\5\n\6\2\u00a4\u00a5")
        buf.write("\7)\2\2\u00a5\u00a6\7\36\2\2\u00a6\u00a7\7(\2\2\u00a7")
        buf.write("\u00a8\5\f\7\2\u00a8\u00a9\7)\2\2\u00a9\t\3\2\2\2\u00aa")
        buf.write("\u00ab\7,\2\2\u00ab\u00ac\7*\2\2\u00ac\u00af\5\n\6\2\u00ad")
        buf.write("\u00af\7,\2\2\u00ae\u00aa\3\2\2\2\u00ae\u00ad\3\2\2\2")
        buf.write("\u00af\13\3\2\2\2\u00b0\u00b1\7(\2\2\u00b1\u00b2\5\16")
        buf.write("\b\2\u00b2\u00b3\7)\2\2\u00b3\u00c1\3\2\2\2\u00b4\u00b5")
        buf.write("\7(\2\2\u00b5\u00b6\5\22\n\2\u00b6\u00b7\7)\2\2\u00b7")
        buf.write("\u00c1\3\2\2\2\u00b8\u00b9\7(\2\2\u00b9\u00ba\5\26\f\2")
        buf.write("\u00ba\u00bb\7)\2\2\u00bb\u00c1\3\2\2\2\u00bc\u00bd\7")
        buf.write("(\2\2\u00bd\u00be\5\32\16\2\u00be\u00bf\7)\2\2\u00bf\u00c1")
        buf.write("\3\2\2\2\u00c0\u00b0\3\2\2\2\u00c0\u00b4\3\2\2\2\u00c0")
        buf.write("\u00b8\3\2\2\2\u00c0\u00bc\3\2\2\2\u00c1\r\3\2\2\2\u00c2")
        buf.write("\u00c5\5\20\t\2\u00c3\u00c5\3\2\2\2\u00c4\u00c2\3\2\2")
        buf.write("\2\u00c4\u00c3\3\2\2\2\u00c5\17\3\2\2\2\u00c6\u00c7\7")
        buf.write(",\2\2\u00c7\u00c8\7*\2\2\u00c8\u00cb\5\20\t\2\u00c9\u00cb")
        buf.write("\7,\2\2\u00ca\u00c6\3\2\2\2\u00ca\u00c9\3\2\2\2\u00cb")
        buf.write("\21\3\2\2\2\u00cc\u00cf\5\24\13\2\u00cd\u00cf\3\2\2\2")
        buf.write("\u00ce\u00cc\3\2\2\2\u00ce\u00cd\3\2\2\2\u00cf\23\3\2")
        buf.write("\2\2\u00d0\u00d1\7-\2\2\u00d1\u00d2\7*\2\2\u00d2\u00d5")
        buf.write("\5\24\13\2\u00d3\u00d5\7-\2\2\u00d4\u00d0\3\2\2\2\u00d4")
        buf.write("\u00d3\3\2\2\2\u00d5\25\3\2\2\2\u00d6\u00d9\5\30\r\2\u00d7")
        buf.write("\u00d9\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d8\u00d7\3\2\2\2")
        buf.write("\u00d9\27\3\2\2\2\u00da\u00db\7.\2\2\u00db\u00dc\7*\2")
        buf.write("\2\u00dc\u00df\5\30\r\2\u00dd\u00df\7.\2\2\u00de\u00da")
        buf.write("\3\2\2\2\u00de\u00dd\3\2\2\2\u00df\31\3\2\2\2\u00e0\u00e3")
        buf.write("\5\34\17\2\u00e1\u00e3\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e2")
        buf.write("\u00e1\3\2\2\2\u00e3\33\3\2\2\2\u00e4\u00e5\5\f\7\2\u00e5")
        buf.write("\u00e6\7*\2\2\u00e6\u00e7\5\34\17\2\u00e7\u00ea\3\2\2")
        buf.write("\2\u00e8\u00ea\5\f\7\2\u00e9\u00e4\3\2\2\2\u00e9\u00e8")
        buf.write("\3\2\2\2\u00ea\35\3\2\2\2\u00eb\u00ec\b\20\1\2\u00ec\u00ed")
        buf.write("\5 \21\2\u00ed\u00f3\3\2\2\2\u00ee\u00ef\f\4\2\2\u00ef")
        buf.write("\u00f0\t\3\2\2\u00f0\u00f2\5 \21\2\u00f1\u00ee\3\2\2\2")
        buf.write("\u00f2\u00f5\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f3\u00f4\3")
        buf.write("\2\2\2\u00f4\37\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f6\u00f7")
        buf.write("\b\21\1\2\u00f7\u00f8\5\"\22\2\u00f8\u00fe\3\2\2\2\u00f9")
        buf.write("\u00fa\f\4\2\2\u00fa\u00fb\t\4\2\2\u00fb\u00fd\5\"\22")
        buf.write("\2\u00fc\u00f9\3\2\2\2\u00fd\u0100\3\2\2\2\u00fe\u00fc")
        buf.write("\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff!\3\2\2\2\u0100\u00fe")
        buf.write("\3\2\2\2\u0101\u0102\7\31\2\2\u0102\u0105\5\"\22\2\u0103")
        buf.write("\u0105\5$\23\2\u0104\u0101\3\2\2\2\u0104\u0103\3\2\2\2")
        buf.write("\u0105#\3\2\2\2\u0106\u0107\t\5\2\2\u0107%\3\2\2\2\u0108")
        buf.write("\u0109\b\24\1\2\u0109\u010a\5(\25\2\u010a\u0110\3\2\2")
        buf.write("\2\u010b\u010c\f\4\2\2\u010c\u010d\7\27\2\2\u010d\u010f")
        buf.write("\5(\25\2\u010e\u010b\3\2\2\2\u010f\u0112\3\2\2\2\u0110")
        buf.write("\u010e\3\2\2\2\u0110\u0111\3\2\2\2\u0111\'\3\2\2\2\u0112")
        buf.write("\u0110\3\2\2\2\u0113\u0114\b\25\1\2\u0114\u0115\5*\26")
        buf.write("\2\u0115\u011b\3\2\2\2\u0116\u0117\f\4\2\2\u0117\u0118")
        buf.write("\7\26\2\2\u0118\u011a\5*\26\2\u0119\u0116\3\2\2\2\u011a")
        buf.write("\u011d\3\2\2\2\u011b\u0119\3\2\2\2\u011b\u011c\3\2\2\2")
        buf.write("\u011c)\3\2\2\2\u011d\u011b\3\2\2\2\u011e\u011f\7\25\2")
        buf.write("\2\u011f\u0122\5*\26\2\u0120\u0122\5,\27\2\u0121\u011e")
        buf.write("\3\2\2\2\u0121\u0120\3\2\2\2\u0122+\3\2\2\2\u0123\u0124")
        buf.write("\t\6\2\2\u0124-\3\2\2\2\u0125\u0126\b\30\1\2\u0126\u0129")
        buf.write("\7.\2\2\u0127\u0129\7/\2\2\u0128\u0125\3\2\2\2\u0128\u0127")
        buf.write("\3\2\2\2\u0129\u012f\3\2\2\2\u012a\u012b\f\5\2\2\u012b")
        buf.write("\u012c\7%\2\2\u012c\u012e\5.\30\6\u012d\u012a\3\2\2\2")
        buf.write("\u012e\u0131\3\2\2\2\u012f\u012d\3\2\2\2\u012f\u0130\3")
        buf.write("\2\2\2\u0130/\3\2\2\2\u0131\u012f\3\2\2\2\u0132\u0135")
        buf.write("\5\62\32\2\u0133\u0135\5\64\33\2\u0134\u0132\3\2\2\2\u0134")
        buf.write("\u0133\3\2\2\2\u0135\61\3\2\2\2\u0136\u0137\5\36\20\2")
        buf.write("\u0137\u0138\5\66\34\2\u0138\u0139\5\36\20\2\u0139\63")
        buf.write("\3\2\2\2\u013a\u013b\5.\30\2\u013b\u013c\58\35\2\u013c")
        buf.write("\u013d\5.\30\2\u013d\65\3\2\2\2\u013e\u013f\t\7\2\2\u013f")
        buf.write("\67\3\2\2\2\u0140\u0141\7\37\2\2\u01419\3\2\2\2\u0142")
        buf.write("\u0143\5<\37\2\u0143\u0144\7(\2\2\u0144\u0145\5> \2\u0145")
        buf.write("\u0146\7)\2\2\u0146;\3\2\2\2\u0147\u014b\7/\2\2\u0148")
        buf.write("\u014b\5@!\2\u0149\u014b\7,\2\2\u014a\u0147\3\2\2\2\u014a")
        buf.write("\u0148\3\2\2\2\u014a\u0149\3\2\2\2\u014b=\3\2\2\2\u014c")
        buf.write("\u014d\5<\37\2\u014d\u014e\7*\2\2\u014e\u014f\5> \2\u014f")
        buf.write("\u0152\3\2\2\2\u0150\u0152\5<\37\2\u0151\u014c\3\2\2\2")
        buf.write("\u0151\u0150\3\2\2\2\u0152?\3\2\2\2\u0153\u0154\7/\2\2")
        buf.write("\u0154\u0155\7&\2\2\u0155\u0156\5B\"\2\u0156\u0157\7\'")
        buf.write("\2\2\u0157A\3\2\2\2\u0158\u015b\5D#\2\u0159\u015b\3\2")
        buf.write("\2\2\u015a\u0158\3\2\2\2\u015a\u0159\3\2\2\2\u015bC\3")
        buf.write("\2\2\2\u015c\u015d\5F$\2\u015d\u015e\7*\2\2\u015e\u015f")
        buf.write("\5D#\2\u015f\u0162\3\2\2\2\u0160\u0162\5F$\2\u0161\u015c")
        buf.write("\3\2\2\2\u0161\u0160\3\2\2\2\u0162E\3\2\2\2\u0163\u0164")
        buf.write("\5V,\2\u0164G\3\2\2\2\u0165\u016d\5v<\2\u0166\u016d\5")
        buf.write("r:\2\u0167\u016d\5t;\2\u0168\u016d\5p9\2\u0169\u016d\5")
        buf.write("x=\2\u016a\u016d\5b\62\2\u016b\u016d\5l\67\2\u016c\u0165")
        buf.write("\3\2\2\2\u016c\u0166\3\2\2\2\u016c\u0167\3\2\2\2\u016c")
        buf.write("\u0168\3\2\2\2\u016c\u0169\3\2\2\2\u016c\u016a\3\2\2\2")
        buf.write("\u016c\u016b\3\2\2\2\u016d\u016f\3\2\2\2\u016e\u0170\7")
        buf.write("+\2\2\u016f\u016e\3\2\2\2\u0170\u0171\3\2\2\2\u0171\u016f")
        buf.write("\3\2\2\2\u0171\u0172\3\2\2\2\u0172I\3\2\2\2\u0173\u0178")
        buf.write("\5L\'\2\u0174\u0178\5\b\5\2\u0175\u0178\5P)\2\u0176\u0178")
        buf.write("\5R*\2\u0177\u0173\3\2\2\2\u0177\u0174\3\2\2\2\u0177\u0175")
        buf.write("\3\2\2\2\u0177\u0176\3\2\2\2\u0178K\3\2\2\2\u0179\u017b")
        buf.write("\5N(\2\u017a\u017c\5T+\2\u017b\u017a\3\2\2\2\u017b\u017c")
        buf.write("\3\2\2\2\u017cM\3\2\2\2\u017d\u017e\t\2\2\2\u017eO\3\2")
        buf.write("\2\2\u017f\u0180\7\b\2\2\u0180\u0181\5T+\2\u0181Q\3\2")
        buf.write("\2\2\u0182\u0184\7\t\2\2\u0183\u0185\5T+\2\u0184\u0183")
        buf.write("\3\2\2\2\u0184\u0185\3\2\2\2\u0185S\3\2\2\2\u0186\u0187")
        buf.write("\7\36\2\2\u0187\u0188\5V,\2\u0188U\3\2\2\2\u0189\u0190")
        buf.write("\5\36\20\2\u018a\u0190\5.\30\2\u018b\u0190\5\60\31\2\u018c")
        buf.write("\u0190\5&\24\2\u018d\u0190\5:\36\2\u018e\u0190\5@!\2\u018f")
        buf.write("\u0189\3\2\2\2\u018f\u018a\3\2\2\2\u018f\u018b\3\2\2\2")
        buf.write("\u018f\u018c\3\2\2\2\u018f\u018d\3\2\2\2\u018f\u018e\3")
        buf.write("\2\2\2\u0190W\3\2\2\2\u0191\u0194\5Z.\2\u0192\u0194\3")
        buf.write("\2\2\2\u0193\u0191\3\2\2\2\u0193\u0192\3\2\2\2\u0194Y")
        buf.write("\3\2\2\2\u0195\u0196\5\\/\2\u0196\u0197\7*\2\2\u0197\u0198")
        buf.write("\5Z.\2\u0198\u019b\3\2\2\2\u0199\u019b\5\\/\2\u019a\u0195")
        buf.write("\3\2\2\2\u019a\u0199\3\2\2\2\u019b[\3\2\2\2\u019c\u019d")
        buf.write("\5N(\2\u019d\u01a2\7/\2\2\u019e\u019f\7(\2\2\u019f\u01a0")
        buf.write("\5\n\6\2\u01a0\u01a1\7)\2\2\u01a1\u01a3\3\2\2\2\u01a2")
        buf.write("\u019e\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3]\3\2\2\2\u01a4")
        buf.write("\u01a5\7\n\2\2\u01a5\u01a6\7/\2\2\u01a6\u01a7\7&\2\2\u01a7")
        buf.write("\u01a8\5X-\2\u01a8\u01a9\7\'\2\2\u01a9\u01ac\5`\61\2\u01aa")
        buf.write("\u01ad\5t;\2\u01ab\u01ad\5x=\2\u01ac\u01aa\3\2\2\2\u01ac")
        buf.write("\u01ab\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad_\3\2\2\2\u01ae")
        buf.write("\u01af\7+\2\2\u01af\u01b2\5`\61\2\u01b0\u01b2\3\2\2\2")
        buf.write("\u01b1\u01ae\3\2\2\2\u01b1\u01b0\3\2\2\2\u01b2a\3\2\2")
        buf.write("\2\u01b3\u01b4\7\20\2\2\u01b4\u01b5\5&\24\2\u01b5\u01b6")
        buf.write("\5H%\2\u01b6\u01b8\5d\63\2\u01b7\u01b9\5j\66\2\u01b8\u01b7")
        buf.write("\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9c\3\2\2\2\u01ba\u01bd")
        buf.write("\5f\64\2\u01bb\u01bd\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bc")
        buf.write("\u01bb\3\2\2\2\u01bde\3\2\2\2\u01be\u01bf\5h\65\2\u01bf")
        buf.write("\u01c0\5`\61\2\u01c0\u01c1\5f\64\2\u01c1\u01c4\3\2\2\2")
        buf.write("\u01c2\u01c4\5h\65\2\u01c3\u01be\3\2\2\2\u01c3\u01c2\3")
        buf.write("\2\2\2\u01c4g\3\2\2\2\u01c5\u01c6\7\22\2\2\u01c6\u01c7")
        buf.write("\5&\24\2\u01c7\u01c8\5H%\2\u01c8i\3\2\2\2\u01c9\u01ca")
        buf.write("\7\21\2\2\u01ca\u01cb\5&\24\2\u01cb\u01cc\5H%\2\u01cc")
        buf.write("k\3\2\2\2\u01cd\u01ce\7\13\2\2\u01ce\u01cf\7/\2\2\u01cf")
        buf.write("\u01d0\7\f\2\2\u01d0\u01d1\5&\24\2\u01d1\u01d2\7\r\2\2")
        buf.write("\u01d2\u01d3\5n8\2\u01d3\u01d4\5`\61\2\u01d4\u01d5\5H")
        buf.write("%\2\u01d5m\3\2\2\2\u01d6\u01d7\5V,\2\u01d7o\3\2\2\2\u01d8")
        buf.write("\u01d9\7\16\2\2\u01d9q\3\2\2\2\u01da\u01db\7\17\2\2\u01db")
        buf.write("s\3\2\2\2\u01dc\u01de\7\7\2\2\u01dd\u01df\5V,\2\u01de")
        buf.write("\u01dd\3\2\2\2\u01de\u01df\3\2\2\2\u01dfu\3\2\2\2\u01e0")
        buf.write("\u01e1\5@!\2\u01e1w\3\2\2\2\u01e2\u01e4\7\23\2\2\u01e3")
        buf.write("\u01e5\7+\2\2\u01e4\u01e3\3\2\2\2\u01e5\u01e6\3\2\2\2")
        buf.write("\u01e6\u01e4\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7\u01e8\3")
        buf.write("\2\2\2\u01e8\u01e9\5z>\2\u01e9\u01f0\7\24\2\2\u01ea\u01ec")
        buf.write("\7+\2\2\u01eb\u01ea\3\2\2\2\u01ec\u01ed\3\2\2\2\u01ed")
        buf.write("\u01eb\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee\u01f1\3\2\2\2")
        buf.write("\u01ef\u01f1\7\2\2\3\u01f0\u01eb\3\2\2\2\u01f0\u01ef\3")
        buf.write("\2\2\2\u01f1y\3\2\2\2\u01f2\u01f3\5|?\2\u01f3{\3\2\2\2")
        buf.write("\u01f4\u01f5\5H%\2\u01f5\u01f6\5|?\2\u01f6\u01f9\3\2\2")
        buf.write("\2\u01f7\u01f9\3\2\2\2\u01f8\u01f4\3\2\2\2\u01f8\u01f7")
        buf.write("\3\2\2\2\u01f9}\3\2\2\2\61\u0086\u008b\u0090\u0096\u009e")
        buf.write("\u00ae\u00c0\u00c4\u00ca\u00ce\u00d4\u00d8\u00de\u00e2")
        buf.write("\u00e9\u00f3\u00fe\u0104\u0110\u011b\u0121\u0128\u012f")
        buf.write("\u0134\u014a\u0151\u015a\u0161\u016c\u0171\u0177\u017b")
        buf.write("\u0184\u018f\u0193\u019a\u01a2\u01ac\u01b1\u01b8\u01bc")
        buf.write("\u01c3\u01de\u01e6\u01ed\u01f0\u01f8")
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
    RULE_decl = 2
    RULE_arrayDeclaration = 3
    RULE_arrayDim = 4
    RULE_arrayInit = 5
    RULE_numberList = 6
    RULE_numberPrime = 7
    RULE_boolList = 8
    RULE_boolPrime = 9
    RULE_stringList = 10
    RULE_stringPrime = 11
    RULE_arrayList = 12
    RULE_arrayPrime = 13
    RULE_arithExpr = 14
    RULE_arithExpr1 = 15
    RULE_arithExpr2 = 16
    RULE_arithExpr3 = 17
    RULE_logicExpr = 18
    RULE_logicExpr1 = 19
    RULE_logicExpr2 = 20
    RULE_logicExpr3 = 21
    RULE_stringConcatExpr = 22
    RULE_relExpr = 23
    RULE_arithComp = 24
    RULE_literalComp = 25
    RULE_arithRelOp = 26
    RULE_literalOp = 27
    RULE_elementAccessExpr = 28
    RULE_arrExpr = 29
    RULE_indexOp = 30
    RULE_functionCall = 31
    RULE_functionArgsList = 32
    RULE_argsPrime = 33
    RULE_arg = 34
    RULE_statement = 35
    RULE_variableDeclaration = 36
    RULE_normalDeclaration = 37
    RULE_varType = 38
    RULE_varDecl = 39
    RULE_dynamicDecl = 40
    RULE_variableInitialization = 41
    RULE_expression = 42
    RULE_paramDeclList = 43
    RULE_paramDeclPrime = 44
    RULE_paramDeclAtom = 45
    RULE_functionDecl = 46
    RULE_nullableListOfNEWLINE = 47
    RULE_ifStatement = 48
    RULE_elifStatementList = 49
    RULE_elifStatementPrime = 50
    RULE_elifStatement = 51
    RULE_elseStatement = 52
    RULE_forStatement = 53
    RULE_updateExpr = 54
    RULE_breakStatement = 55
    RULE_continueStatement = 56
    RULE_returnStatement = 57
    RULE_functionCallStatement = 58
    RULE_blockStatement = 59
    RULE_blockStatementBody = 60
    RULE_nullableListOfStatement = 61

    ruleNames =  [ "mainFunction", "program", "decl", "arrayDeclaration", 
                   "arrayDim", "arrayInit", "numberList", "numberPrime", 
                   "boolList", "boolPrime", "stringList", "stringPrime", 
                   "arrayList", "arrayPrime", "arithExpr", "arithExpr1", 
                   "arithExpr2", "arithExpr3", "logicExpr", "logicExpr1", 
                   "logicExpr2", "logicExpr3", "stringConcatExpr", "relExpr", 
                   "arithComp", "literalComp", "arithRelOp", "literalOp", 
                   "elementAccessExpr", "arrExpr", "indexOp", "functionCall", 
                   "functionArgsList", "argsPrime", "arg", "statement", 
                   "variableDeclaration", "normalDeclaration", "varType", 
                   "varDecl", "dynamicDecl", "variableInitialization", "expression", 
                   "paramDeclList", "paramDeclPrime", "paramDeclAtom", "functionDecl", 
                   "nullableListOfNEWLINE", "ifStatement", "elifStatementList", 
                   "elifStatementPrime", "elifStatement", "elseStatement", 
                   "forStatement", "updateExpr", "breakStatement", "continueStatement", 
                   "returnStatement", "functionCallStatement", "blockStatement", 
                   "blockStatementBody", "nullableListOfStatement" ]

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
            self.state = 124
            self.match(ZCodeParser.FUNC)
            self.state = 125
            self.match(ZCodeParser.T__0)
            self.state = 126
            self.match(ZCodeParser.LBracket)
            self.state = 127
            self.paramDeclList()
            self.state = 128
            self.match(ZCodeParser.RBracket)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 129
                self.match(ZCodeParser.NEWLINE)
                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 137
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN]:
                self.state = 135
                self.returnStatement()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.state = 136
                self.blockStatement()
                pass
            elif token in [ZCodeParser.EOF, ZCodeParser.VAR, ZCodeParser.FUNC]:
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

        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.DeclContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.DeclContext,i)


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
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 139
                self.match(ZCodeParser.NEWLINE)
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.VAR or _la==ZCodeParser.FUNC:
                self.state = 145
                self.decl()
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 151
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mainFunction(self):
            return self.getTypedRuleContext(ZCodeParser.MainFunctionContext,0)


        def functionDecl(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionDeclContext,0)


        def varDecl(self):
            return self.getTypedRuleContext(ZCodeParser.VarDeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.mainFunction()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self.functionDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 155
                self.varDecl()
                pass


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
        self.enterRule(localctx, 6, self.RULE_arrayDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 159
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 160
            self.match(ZCodeParser.LSBracket)
            self.state = 161
            self.arrayDim()
            self.state = 162
            self.match(ZCodeParser.RSBracket)
            self.state = 163
            self.match(ZCodeParser.LEFTARR)
            self.state = 164
            self.match(ZCodeParser.LSBracket)
            self.state = 165
            self.arrayInit()
            self.state = 166
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
        self.enterRule(localctx, 8, self.RULE_arrayDim)
        try:
            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.match(ZCodeParser.NumberLit)
                self.state = 169
                self.match(ZCodeParser.COMMA)
                self.state = 170
                self.arrayDim()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
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
        self.enterRule(localctx, 10, self.RULE_arrayInit)
        try:
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.match(ZCodeParser.LSBracket)
                self.state = 175
                self.numberList()
                self.state = 176
                self.match(ZCodeParser.RSBracket)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.match(ZCodeParser.LSBracket)
                self.state = 179
                self.boolList()
                self.state = 180
                self.match(ZCodeParser.RSBracket)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 182
                self.match(ZCodeParser.LSBracket)
                self.state = 183
                self.stringList()
                self.state = 184
                self.match(ZCodeParser.RSBracket)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 186
                self.match(ZCodeParser.LSBracket)
                self.state = 187
                self.arrayList()
                self.state = 188
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
        self.enterRule(localctx, 12, self.RULE_numberList)
        try:
            self.state = 194
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NumberLit]:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
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
        self.enterRule(localctx, 14, self.RULE_numberPrime)
        try:
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.match(ZCodeParser.NumberLit)
                self.state = 197
                self.match(ZCodeParser.COMMA)
                self.state = 198
                self.numberPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
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
        self.enterRule(localctx, 16, self.RULE_boolList)
        try:
            self.state = 204
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BooleanLit]:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
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
        self.enterRule(localctx, 18, self.RULE_boolPrime)
        try:
            self.state = 210
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.match(ZCodeParser.BooleanLit)
                self.state = 207
                self.match(ZCodeParser.COMMA)
                self.state = 208
                self.boolPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
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
        self.enterRule(localctx, 20, self.RULE_stringList)
        try:
            self.state = 214
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.StringLit]:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
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
        self.enterRule(localctx, 22, self.RULE_stringPrime)
        try:
            self.state = 220
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.match(ZCodeParser.StringLit)
                self.state = 217
                self.match(ZCodeParser.COMMA)
                self.state = 218
                self.stringPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
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
        self.enterRule(localctx, 24, self.RULE_arrayList)
        try:
            self.state = 224
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LSBracket]:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
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
        self.enterRule(localctx, 26, self.RULE_arrayPrime)
        try:
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.arrayInit()
                self.state = 227
                self.match(ZCodeParser.COMMA)
                self.state = 228
                self.arrayPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
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
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_arithExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.arithExpr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 241
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.ArithExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_arithExpr)
                    self.state = 236
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 237
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.PLUS or _la==ZCodeParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 238
                    self.arithExpr1(0) 
                self.state = 243
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_arithExpr1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.arithExpr2()
            self._ctx.stop = self._input.LT(-1)
            self.state = 252
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.ArithExpr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_arithExpr1)
                    self.state = 247
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 248
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MULT) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 249
                    self.arithExpr2() 
                self.state = 254
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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
        self.enterRule(localctx, 32, self.RULE_arithExpr2)
        try:
            self.state = 258
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                self.match(ZCodeParser.MINUS)
                self.state = 256
                self.arithExpr2()
                pass
            elif token in [ZCodeParser.NumberLit, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
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
        self.enterRule(localctx, 34, self.RULE_arithExpr3)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
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
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_logicExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.logicExpr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 270
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.LogicExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicExpr)
                    self.state = 265
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 266
                    self.match(ZCodeParser.OR)
                    self.state = 267
                    self.logicExpr1(0) 
                self.state = 272
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_logicExpr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.logicExpr2()
            self._ctx.stop = self._input.LT(-1)
            self.state = 281
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.LogicExpr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicExpr1)
                    self.state = 276
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 277
                    self.match(ZCodeParser.AND)
                    self.state = 278
                    self.logicExpr2() 
                self.state = 283
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
        self.enterRule(localctx, 40, self.RULE_logicExpr2)
        try:
            self.state = 287
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 284
                self.match(ZCodeParser.NOT)
                self.state = 285
                self.logicExpr2()
                pass
            elif token in [ZCodeParser.BooleanLit, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 286
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
        self.enterRule(localctx, 42, self.RULE_logicExpr3)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
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
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_stringConcatExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.StringLit]:
                self.state = 292
                self.match(ZCodeParser.StringLit)
                pass
            elif token in [ZCodeParser.IDENTIFIER]:
                self.state = 293
                self.match(ZCodeParser.IDENTIFIER)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 301
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.StringConcatExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_stringConcatExpr)
                    self.state = 296
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 297
                    self.match(ZCodeParser.ELLIPSIS)
                    self.state = 298
                    self.stringConcatExpr(4) 
                self.state = 303
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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
        self.enterRule(localctx, 46, self.RULE_relExpr)
        try:
            self.state = 306
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 304
                self.arithComp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 305
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
        self.enterRule(localctx, 48, self.RULE_arithComp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.arithExpr(0)
            self.state = 309
            self.arithRelOp()
            self.state = 310
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
        self.enterRule(localctx, 50, self.RULE_literalComp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.stringConcatExpr(0)
            self.state = 313
            self.literalOp()
            self.state = 314
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
        self.enterRule(localctx, 52, self.RULE_arithRelOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
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
        self.enterRule(localctx, 54, self.RULE_literalOp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
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
        self.enterRule(localctx, 56, self.RULE_elementAccessExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.arrExpr()
            self.state = 321
            self.match(ZCodeParser.LSBracket)
            self.state = 322
            self.indexOp()
            self.state = 323
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
        self.enterRule(localctx, 58, self.RULE_arrExpr)
        try:
            self.state = 328
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 325
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 326
                self.functionCall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 327
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
        self.enterRule(localctx, 60, self.RULE_indexOp)
        try:
            self.state = 335
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 330
                self.arrExpr()
                self.state = 331
                self.match(ZCodeParser.COMMA)
                self.state = 332
                self.indexOp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 334
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
        self.enterRule(localctx, 62, self.RULE_functionCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 338
            self.match(ZCodeParser.LBracket)
            self.state = 339
            self.functionArgsList()
            self.state = 340
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
        self.enterRule(localctx, 64, self.RULE_functionArgsList)
        try:
            self.state = 344
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT, ZCodeParser.MINUS, ZCodeParser.NumberLit, ZCodeParser.BooleanLit, ZCodeParser.StringLit, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 342
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
        self.enterRule(localctx, 66, self.RULE_argsPrime)
        try:
            self.state = 351
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 346
                self.arg()
                self.state = 347
                self.match(ZCodeParser.COMMA)
                self.state = 348
                self.argsPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 350
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
        self.enterRule(localctx, 68, self.RULE_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
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
        self.enterRule(localctx, 70, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.IDENTIFIER]:
                self.state = 355
                self.functionCallStatement()
                pass
            elif token in [ZCodeParser.CONTINUE]:
                self.state = 356
                self.continueStatement()
                pass
            elif token in [ZCodeParser.RETURN]:
                self.state = 357
                self.returnStatement()
                pass
            elif token in [ZCodeParser.BREAK]:
                self.state = 358
                self.breakStatement()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.state = 359
                self.blockStatement()
                pass
            elif token in [ZCodeParser.IF]:
                self.state = 360
                self.ifStatement()
                pass
            elif token in [ZCodeParser.FOR]:
                self.state = 361
                self.forStatement()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 365 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 364
                    self.match(ZCodeParser.NEWLINE)

                else:
                    raise NoViableAltException(self)
                self.state = 367 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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
        self.enterRule(localctx, 72, self.RULE_variableDeclaration)
        try:
            self.state = 373
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 369
                self.normalDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 370
                self.arrayDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 371
                self.varDecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 372
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
        self.enterRule(localctx, 74, self.RULE_normalDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.varType()
            self.state = 377
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LEFTARR:
                self.state = 376
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
        self.enterRule(localctx, 76, self.RULE_varType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
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
        self.enterRule(localctx, 78, self.RULE_varDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.match(ZCodeParser.VAR)
            self.state = 382
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
        self.enterRule(localctx, 80, self.RULE_dynamicDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.match(ZCodeParser.DYNAMIC)
            self.state = 386
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LEFTARR:
                self.state = 385
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
        self.enterRule(localctx, 82, self.RULE_variableInitialization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.match(ZCodeParser.LEFTARR)
            self.state = 389
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
        self.enterRule(localctx, 84, self.RULE_expression)
        try:
            self.state = 397
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 391
                self.arithExpr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 392
                self.stringConcatExpr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 393
                self.relExpr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 394
                self.logicExpr(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 395
                self.elementAccessExpr()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 396
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
        self.enterRule(localctx, 86, self.RULE_paramDeclList)
        try:
            self.state = 401
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 399
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
        self.enterRule(localctx, 88, self.RULE_paramDeclPrime)
        try:
            self.state = 408
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 403
                self.paramDeclAtom()
                self.state = 404
                self.match(ZCodeParser.COMMA)
                self.state = 405
                self.paramDeclPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 407
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
        self.enterRule(localctx, 90, self.RULE_paramDeclAtom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.varType()
            self.state = 411
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 416
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LSBracket:
                self.state = 412
                self.match(ZCodeParser.LSBracket)
                self.state = 413
                self.arrayDim()
                self.state = 414
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
            return ZCodeParser.RULE_functionDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDecl" ):
                return visitor.visitFunctionDecl(self)
            else:
                return visitor.visitChildren(self)




    def functionDecl(self):

        localctx = ZCodeParser.FunctionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_functionDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self.match(ZCodeParser.FUNC)
            self.state = 419
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 420
            self.match(ZCodeParser.LBracket)
            self.state = 421
            self.paramDeclList()
            self.state = 422
            self.match(ZCodeParser.RBracket)
            self.state = 423
            self.nullableListOfNEWLINE()
            self.state = 426
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN]:
                self.state = 424
                self.returnStatement()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.state = 425
                self.blockStatement()
                pass
            elif token in [ZCodeParser.EOF, ZCodeParser.VAR, ZCodeParser.FUNC]:
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
        self.enterRule(localctx, 94, self.RULE_nullableListOfNEWLINE)
        try:
            self.state = 431
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 428
                self.match(ZCodeParser.NEWLINE)
                self.state = 429
                self.nullableListOfNEWLINE()
                pass
            elif token in [ZCodeParser.EOF, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.FUNC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.ELIF, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
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
        self.enterRule(localctx, 96, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            self.match(ZCodeParser.IF)
            self.state = 434
            self.logicExpr(0)
            self.state = 435
            self.statement()
            self.state = 436
            self.elifStatementList()
            self.state = 438
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ELSE:
                self.state = 437
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
        self.enterRule(localctx, 98, self.RULE_elifStatementList)
        try:
            self.state = 442
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ELIF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 440
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
        self.enterRule(localctx, 100, self.RULE_elifStatementPrime)
        try:
            self.state = 449
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 444
                self.elifStatement()
                self.state = 445
                self.nullableListOfNEWLINE()
                self.state = 446
                self.elifStatementPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 448
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
        self.enterRule(localctx, 102, self.RULE_elifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.match(ZCodeParser.ELIF)
            self.state = 452
            self.logicExpr(0)
            self.state = 453
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
        self.enterRule(localctx, 104, self.RULE_elseStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455
            self.match(ZCodeParser.ELSE)
            self.state = 456
            self.logicExpr(0)
            self.state = 457
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
        self.enterRule(localctx, 106, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459
            self.match(ZCodeParser.FOR)
            self.state = 460
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 461
            self.match(ZCodeParser.UNTIL)
            self.state = 462
            self.logicExpr(0)
            self.state = 463
            self.match(ZCodeParser.BY)
            self.state = 464
            self.updateExpr()
            self.state = 465
            self.nullableListOfNEWLINE()
            self.state = 466
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
        self.enterRule(localctx, 108, self.RULE_updateExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
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
        self.enterRule(localctx, 110, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
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
        self.enterRule(localctx, 112, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
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
        self.enterRule(localctx, 114, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self.match(ZCodeParser.RETURN)
            self.state = 476
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NOT) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.NumberLit) | (1 << ZCodeParser.BooleanLit) | (1 << ZCodeParser.StringLit) | (1 << ZCodeParser.IDENTIFIER))) != 0):
                self.state = 475
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
        self.enterRule(localctx, 116, self.RULE_functionCallStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
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
        self.enterRule(localctx, 118, self.RULE_blockStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
            self.match(ZCodeParser.BEGIN)
            self.state = 482 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 481
                self.match(ZCodeParser.NEWLINE)
                self.state = 484 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZCodeParser.NEWLINE):
                    break

            self.state = 486
            self.blockStatementBody()
            self.state = 487
            self.match(ZCodeParser.END)
            self.state = 494
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEWLINE]:
                self.state = 489 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 488
                        self.match(ZCodeParser.NEWLINE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 491 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

                pass
            elif token in [ZCodeParser.EOF]:
                self.state = 493
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
        self.enterRule(localctx, 120, self.RULE_blockStatementBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 496
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
        self.enterRule(localctx, 122, self.RULE_nullableListOfStatement)
        try:
            self.state = 502
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 498
                self.statement()
                self.state = 499
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
        self._predicates[14] = self.arithExpr_sempred
        self._predicates[15] = self.arithExpr1_sempred
        self._predicates[18] = self.logicExpr_sempred
        self._predicates[19] = self.logicExpr1_sempred
        self._predicates[22] = self.stringConcatExpr_sempred
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
         




