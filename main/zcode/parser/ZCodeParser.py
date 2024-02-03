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
        buf.write("\u01fd\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
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
        buf.write("\u008d\n\3\f\3\16\3\u0090\13\3\3\3\7\3\u0093\n\3\f\3\16")
        buf.write("\3\u0096\13\3\3\3\5\3\u0099\n\3\3\3\7\3\u009c\n\3\f\3")
        buf.write("\16\3\u009f\13\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\5\5\5\u00b1\n\5\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6")
        buf.write("\u00c3\n\6\3\7\3\7\5\7\u00c7\n\7\3\b\3\b\3\b\3\b\5\b\u00cd")
        buf.write("\n\b\3\t\3\t\5\t\u00d1\n\t\3\n\3\n\3\n\3\n\5\n\u00d7\n")
        buf.write("\n\3\13\3\13\5\13\u00db\n\13\3\f\3\f\3\f\3\f\5\f\u00e1")
        buf.write("\n\f\3\r\3\r\5\r\u00e5\n\r\3\16\3\16\3\16\3\16\3\16\5")
        buf.write("\16\u00ec\n\16\3\17\3\17\3\17\3\17\3\17\3\17\7\17\u00f4")
        buf.write("\n\17\f\17\16\17\u00f7\13\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\7\20\u00ff\n\20\f\20\16\20\u0102\13\20\3\21\3\21")
        buf.write("\3\21\5\21\u0107\n\21\3\22\3\22\3\23\3\23\3\23\3\23\3")
        buf.write("\23\3\23\7\23\u0111\n\23\f\23\16\23\u0114\13\23\3\24\3")
        buf.write("\24\3\24\3\24\3\24\3\24\7\24\u011c\n\24\f\24\16\24\u011f")
        buf.write("\13\24\3\25\3\25\3\25\5\25\u0124\n\25\3\26\3\26\3\27\3")
        buf.write("\27\3\27\5\27\u012b\n\27\3\27\3\27\3\27\7\27\u0130\n\27")
        buf.write("\f\27\16\27\u0133\13\27\3\30\3\30\5\30\u0137\n\30\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\5\36\u014d\n")
        buf.write("\36\3\37\3\37\3\37\3\37\3\37\5\37\u0154\n\37\3 \3 \3 ")
        buf.write("\3 \3 \3!\3!\5!\u015d\n!\3\"\3\"\3\"\3\"\3\"\5\"\u0164")
        buf.write("\n\"\3#\3#\3$\3$\3$\3$\3$\3$\3$\5$\u016f\n$\3$\6$\u0172")
        buf.write("\n$\r$\16$\u0173\3%\3%\3%\3%\5%\u017a\n%\3&\3&\5&\u017e")
        buf.write("\n&\3\'\3\'\3(\3(\3(\3)\3)\5)\u0187\n)\3*\3*\3*\3+\3+")
        buf.write("\3+\3+\3+\3+\5+\u0192\n+\3,\3,\5,\u0196\n,\3-\3-\3-\3")
        buf.write("-\3-\5-\u019d\n-\3.\3.\3.\3.\3.\3.\5.\u01a5\n.\3/\3/\3")
        buf.write("/\3/\3/\3/\3/\3/\5/\u01af\n/\3\60\3\60\3\60\5\60\u01b4")
        buf.write("\n\60\3\61\3\61\3\61\3\61\3\61\5\61\u01bb\n\61\3\62\3")
        buf.write("\62\5\62\u01bf\n\62\3\63\3\63\3\63\3\63\3\63\5\63\u01c6")
        buf.write("\n\63\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\67\3\67\38\38\3")
        buf.write("9\39\3:\3:\5:\u01e1\n:\3;\3;\3<\3<\6<\u01e7\n<\r<\16<")
        buf.write("\u01e8\3<\3<\3<\6<\u01ee\n<\r<\16<\u01ef\3<\5<\u01f3\n")
        buf.write("<\3=\3=\3>\3>\3>\3>\5>\u01fb\n>\3>\2\7\34\36$&,?\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66")
        buf.write("8:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz\2\b\3\2\4\6\3\2\30")
        buf.write("\31\3\2\32\34\4\2,,//\4\2--//\4\2\35\35 $\2\u01ff\2|\3")
        buf.write("\2\2\2\4\u008e\3\2\2\2\6\u00a2\3\2\2\2\b\u00b0\3\2\2\2")
        buf.write("\n\u00c2\3\2\2\2\f\u00c6\3\2\2\2\16\u00cc\3\2\2\2\20\u00d0")
        buf.write("\3\2\2\2\22\u00d6\3\2\2\2\24\u00da\3\2\2\2\26\u00e0\3")
        buf.write("\2\2\2\30\u00e4\3\2\2\2\32\u00eb\3\2\2\2\34\u00ed\3\2")
        buf.write("\2\2\36\u00f8\3\2\2\2 \u0106\3\2\2\2\"\u0108\3\2\2\2$")
        buf.write("\u010a\3\2\2\2&\u0115\3\2\2\2(\u0123\3\2\2\2*\u0125\3")
        buf.write("\2\2\2,\u012a\3\2\2\2.\u0136\3\2\2\2\60\u0138\3\2\2\2")
        buf.write("\62\u013c\3\2\2\2\64\u0140\3\2\2\2\66\u0142\3\2\2\28\u0144")
        buf.write("\3\2\2\2:\u014c\3\2\2\2<\u0153\3\2\2\2>\u0155\3\2\2\2")
        buf.write("@\u015c\3\2\2\2B\u0163\3\2\2\2D\u0165\3\2\2\2F\u016e\3")
        buf.write("\2\2\2H\u0179\3\2\2\2J\u017b\3\2\2\2L\u017f\3\2\2\2N\u0181")
        buf.write("\3\2\2\2P\u0184\3\2\2\2R\u0188\3\2\2\2T\u0191\3\2\2\2")
        buf.write("V\u0195\3\2\2\2X\u019c\3\2\2\2Z\u019e\3\2\2\2\\\u01a6")
        buf.write("\3\2\2\2^\u01b3\3\2\2\2`\u01b5\3\2\2\2b\u01be\3\2\2\2")
        buf.write("d\u01c5\3\2\2\2f\u01c7\3\2\2\2h\u01cb\3\2\2\2j\u01cf\3")
        buf.write("\2\2\2l\u01d8\3\2\2\2n\u01da\3\2\2\2p\u01dc\3\2\2\2r\u01de")
        buf.write("\3\2\2\2t\u01e2\3\2\2\2v\u01e4\3\2\2\2x\u01f4\3\2\2\2")
        buf.write("z\u01fa\3\2\2\2|}\7\n\2\2}~\7\3\2\2~\177\7&\2\2\177\u0080")
        buf.write("\5V,\2\u0080\u0084\7\'\2\2\u0081\u0083\7+\2\2\u0082\u0081")
        buf.write("\3\2\2\2\u0083\u0086\3\2\2\2\u0084\u0082\3\2\2\2\u0084")
        buf.write("\u0085\3\2\2\2\u0085\u0089\3\2\2\2\u0086\u0084\3\2\2\2")
        buf.write("\u0087\u008a\5r:\2\u0088\u008a\5v<\2\u0089\u0087\3\2\2")
        buf.write("\2\u0089\u0088\3\2\2\2\u0089\u008a\3\2\2\2\u008a\3\3\2")
        buf.write("\2\2\u008b\u008d\7+\2\2\u008c\u008b\3\2\2\2\u008d\u0090")
        buf.write("\3\2\2\2\u008e\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f")
        buf.write("\u0094\3\2\2\2\u0090\u008e\3\2\2\2\u0091\u0093\5\\/\2")
        buf.write("\u0092\u0091\3\2\2\2\u0093\u0096\3\2\2\2\u0094\u0092\3")
        buf.write("\2\2\2\u0094\u0095\3\2\2\2\u0095\u0098\3\2\2\2\u0096\u0094")
        buf.write("\3\2\2\2\u0097\u0099\5\2\2\2\u0098\u0097\3\2\2\2\u0098")
        buf.write("\u0099\3\2\2\2\u0099\u009d\3\2\2\2\u009a\u009c\5\\/\2")
        buf.write("\u009b\u009a\3\2\2\2\u009c\u009f\3\2\2\2\u009d\u009b\3")
        buf.write("\2\2\2\u009d\u009e\3\2\2\2\u009e\u00a0\3\2\2\2\u009f\u009d")
        buf.write("\3\2\2\2\u00a0\u00a1\7\2\2\3\u00a1\5\3\2\2\2\u00a2\u00a3")
        buf.write("\t\2\2\2\u00a3\u00a4\7/\2\2\u00a4\u00a5\7(\2\2\u00a5\u00a6")
        buf.write("\5\b\5\2\u00a6\u00a7\7)\2\2\u00a7\u00a8\7\36\2\2\u00a8")
        buf.write("\u00a9\7(\2\2\u00a9\u00aa\5\n\6\2\u00aa\u00ab\7)\2\2\u00ab")
        buf.write("\7\3\2\2\2\u00ac\u00ad\7,\2\2\u00ad\u00ae\7*\2\2\u00ae")
        buf.write("\u00b1\5\b\5\2\u00af\u00b1\7,\2\2\u00b0\u00ac\3\2\2\2")
        buf.write("\u00b0\u00af\3\2\2\2\u00b1\t\3\2\2\2\u00b2\u00b3\7(\2")
        buf.write("\2\u00b3\u00b4\5\f\7\2\u00b4\u00b5\7)\2\2\u00b5\u00c3")
        buf.write("\3\2\2\2\u00b6\u00b7\7(\2\2\u00b7\u00b8\5\20\t\2\u00b8")
        buf.write("\u00b9\7)\2\2\u00b9\u00c3\3\2\2\2\u00ba\u00bb\7(\2\2\u00bb")
        buf.write("\u00bc\5\24\13\2\u00bc\u00bd\7)\2\2\u00bd\u00c3\3\2\2")
        buf.write("\2\u00be\u00bf\7(\2\2\u00bf\u00c0\5\30\r\2\u00c0\u00c1")
        buf.write("\7)\2\2\u00c1\u00c3\3\2\2\2\u00c2\u00b2\3\2\2\2\u00c2")
        buf.write("\u00b6\3\2\2\2\u00c2\u00ba\3\2\2\2\u00c2\u00be\3\2\2\2")
        buf.write("\u00c3\13\3\2\2\2\u00c4\u00c7\5\16\b\2\u00c5\u00c7\3\2")
        buf.write("\2\2\u00c6\u00c4\3\2\2\2\u00c6\u00c5\3\2\2\2\u00c7\r\3")
        buf.write("\2\2\2\u00c8\u00c9\7,\2\2\u00c9\u00ca\7*\2\2\u00ca\u00cd")
        buf.write("\5\16\b\2\u00cb\u00cd\7,\2\2\u00cc\u00c8\3\2\2\2\u00cc")
        buf.write("\u00cb\3\2\2\2\u00cd\17\3\2\2\2\u00ce\u00d1\5\22\n\2\u00cf")
        buf.write("\u00d1\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d0\u00cf\3\2\2\2")
        buf.write("\u00d1\21\3\2\2\2\u00d2\u00d3\7-\2\2\u00d3\u00d4\7*\2")
        buf.write("\2\u00d4\u00d7\5\22\n\2\u00d5\u00d7\7-\2\2\u00d6\u00d2")
        buf.write("\3\2\2\2\u00d6\u00d5\3\2\2\2\u00d7\23\3\2\2\2\u00d8\u00db")
        buf.write("\5\26\f\2\u00d9\u00db\3\2\2\2\u00da\u00d8\3\2\2\2\u00da")
        buf.write("\u00d9\3\2\2\2\u00db\25\3\2\2\2\u00dc\u00dd\7.\2\2\u00dd")
        buf.write("\u00de\7*\2\2\u00de\u00e1\5\26\f\2\u00df\u00e1\7.\2\2")
        buf.write("\u00e0\u00dc\3\2\2\2\u00e0\u00df\3\2\2\2\u00e1\27\3\2")
        buf.write("\2\2\u00e2\u00e5\5\32\16\2\u00e3\u00e5\3\2\2\2\u00e4\u00e2")
        buf.write("\3\2\2\2\u00e4\u00e3\3\2\2\2\u00e5\31\3\2\2\2\u00e6\u00e7")
        buf.write("\5\n\6\2\u00e7\u00e8\7*\2\2\u00e8\u00e9\5\32\16\2\u00e9")
        buf.write("\u00ec\3\2\2\2\u00ea\u00ec\5\n\6\2\u00eb\u00e6\3\2\2\2")
        buf.write("\u00eb\u00ea\3\2\2\2\u00ec\33\3\2\2\2\u00ed\u00ee\b\17")
        buf.write("\1\2\u00ee\u00ef\5\36\20\2\u00ef\u00f5\3\2\2\2\u00f0\u00f1")
        buf.write("\f\4\2\2\u00f1\u00f2\t\3\2\2\u00f2\u00f4\5\36\20\2\u00f3")
        buf.write("\u00f0\3\2\2\2\u00f4\u00f7\3\2\2\2\u00f5\u00f3\3\2\2\2")
        buf.write("\u00f5\u00f6\3\2\2\2\u00f6\35\3\2\2\2\u00f7\u00f5\3\2")
        buf.write("\2\2\u00f8\u00f9\b\20\1\2\u00f9\u00fa\5 \21\2\u00fa\u0100")
        buf.write("\3\2\2\2\u00fb\u00fc\f\4\2\2\u00fc\u00fd\t\4\2\2\u00fd")
        buf.write("\u00ff\5 \21\2\u00fe\u00fb\3\2\2\2\u00ff\u0102\3\2\2\2")
        buf.write("\u0100\u00fe\3\2\2\2\u0100\u0101\3\2\2\2\u0101\37\3\2")
        buf.write("\2\2\u0102\u0100\3\2\2\2\u0103\u0104\7\31\2\2\u0104\u0107")
        buf.write("\5 \21\2\u0105\u0107\5\"\22\2\u0106\u0103\3\2\2\2\u0106")
        buf.write("\u0105\3\2\2\2\u0107!\3\2\2\2\u0108\u0109\t\5\2\2\u0109")
        buf.write("#\3\2\2\2\u010a\u010b\b\23\1\2\u010b\u010c\5&\24\2\u010c")
        buf.write("\u0112\3\2\2\2\u010d\u010e\f\4\2\2\u010e\u010f\7\27\2")
        buf.write("\2\u010f\u0111\5&\24\2\u0110\u010d\3\2\2\2\u0111\u0114")
        buf.write("\3\2\2\2\u0112\u0110\3\2\2\2\u0112\u0113\3\2\2\2\u0113")
        buf.write("%\3\2\2\2\u0114\u0112\3\2\2\2\u0115\u0116\b\24\1\2\u0116")
        buf.write("\u0117\5(\25\2\u0117\u011d\3\2\2\2\u0118\u0119\f\4\2\2")
        buf.write("\u0119\u011a\7\26\2\2\u011a\u011c\5(\25\2\u011b\u0118")
        buf.write("\3\2\2\2\u011c\u011f\3\2\2\2\u011d\u011b\3\2\2\2\u011d")
        buf.write("\u011e\3\2\2\2\u011e\'\3\2\2\2\u011f\u011d\3\2\2\2\u0120")
        buf.write("\u0121\7\25\2\2\u0121\u0124\5(\25\2\u0122\u0124\5*\26")
        buf.write("\2\u0123\u0120\3\2\2\2\u0123\u0122\3\2\2\2\u0124)\3\2")
        buf.write("\2\2\u0125\u0126\t\6\2\2\u0126+\3\2\2\2\u0127\u0128\b")
        buf.write("\27\1\2\u0128\u012b\7.\2\2\u0129\u012b\7/\2\2\u012a\u0127")
        buf.write("\3\2\2\2\u012a\u0129\3\2\2\2\u012b\u0131\3\2\2\2\u012c")
        buf.write("\u012d\f\5\2\2\u012d\u012e\7%\2\2\u012e\u0130\5,\27\6")
        buf.write("\u012f\u012c\3\2\2\2\u0130\u0133\3\2\2\2\u0131\u012f\3")
        buf.write("\2\2\2\u0131\u0132\3\2\2\2\u0132-\3\2\2\2\u0133\u0131")
        buf.write("\3\2\2\2\u0134\u0137\5\60\31\2\u0135\u0137\5\62\32\2\u0136")
        buf.write("\u0134\3\2\2\2\u0136\u0135\3\2\2\2\u0137/\3\2\2\2\u0138")
        buf.write("\u0139\5\34\17\2\u0139\u013a\5\64\33\2\u013a\u013b\5\34")
        buf.write("\17\2\u013b\61\3\2\2\2\u013c\u013d\5,\27\2\u013d\u013e")
        buf.write("\5\66\34\2\u013e\u013f\5,\27\2\u013f\63\3\2\2\2\u0140")
        buf.write("\u0141\t\7\2\2\u0141\65\3\2\2\2\u0142\u0143\7\37\2\2\u0143")
        buf.write("\67\3\2\2\2\u0144\u0145\5:\36\2\u0145\u0146\7(\2\2\u0146")
        buf.write("\u0147\5<\37\2\u0147\u0148\7)\2\2\u01489\3\2\2\2\u0149")
        buf.write("\u014d\7/\2\2\u014a\u014d\5> \2\u014b\u014d\7,\2\2\u014c")
        buf.write("\u0149\3\2\2\2\u014c\u014a\3\2\2\2\u014c\u014b\3\2\2\2")
        buf.write("\u014d;\3\2\2\2\u014e\u014f\5:\36\2\u014f\u0150\7*\2\2")
        buf.write("\u0150\u0151\5<\37\2\u0151\u0154\3\2\2\2\u0152\u0154\5")
        buf.write(":\36\2\u0153\u014e\3\2\2\2\u0153\u0152\3\2\2\2\u0154=")
        buf.write("\3\2\2\2\u0155\u0156\7/\2\2\u0156\u0157\7&\2\2\u0157\u0158")
        buf.write("\5@!\2\u0158\u0159\7\'\2\2\u0159?\3\2\2\2\u015a\u015d")
        buf.write("\5B\"\2\u015b\u015d\3\2\2\2\u015c\u015a\3\2\2\2\u015c")
        buf.write("\u015b\3\2\2\2\u015dA\3\2\2\2\u015e\u015f\5D#\2\u015f")
        buf.write("\u0160\7*\2\2\u0160\u0161\5B\"\2\u0161\u0164\3\2\2\2\u0162")
        buf.write("\u0164\5D#\2\u0163\u015e\3\2\2\2\u0163\u0162\3\2\2\2\u0164")
        buf.write("C\3\2\2\2\u0165\u0166\5T+\2\u0166E\3\2\2\2\u0167\u016f")
        buf.write("\5t;\2\u0168\u016f\5p9\2\u0169\u016f\5r:\2\u016a\u016f")
        buf.write("\5n8\2\u016b\u016f\5v<\2\u016c\u016f\5`\61\2\u016d\u016f")
        buf.write("\5j\66\2\u016e\u0167\3\2\2\2\u016e\u0168\3\2\2\2\u016e")
        buf.write("\u0169\3\2\2\2\u016e\u016a\3\2\2\2\u016e\u016b\3\2\2\2")
        buf.write("\u016e\u016c\3\2\2\2\u016e\u016d\3\2\2\2\u016f\u0171\3")
        buf.write("\2\2\2\u0170\u0172\7+\2\2\u0171\u0170\3\2\2\2\u0172\u0173")
        buf.write("\3\2\2\2\u0173\u0171\3\2\2\2\u0173\u0174\3\2\2\2\u0174")
        buf.write("G\3\2\2\2\u0175\u017a\5J&\2\u0176\u017a\5\6\4\2\u0177")
        buf.write("\u017a\5N(\2\u0178\u017a\5P)\2\u0179\u0175\3\2\2\2\u0179")
        buf.write("\u0176\3\2\2\2\u0179\u0177\3\2\2\2\u0179\u0178\3\2\2\2")
        buf.write("\u017aI\3\2\2\2\u017b\u017d\5L\'\2\u017c\u017e\5R*\2\u017d")
        buf.write("\u017c\3\2\2\2\u017d\u017e\3\2\2\2\u017eK\3\2\2\2\u017f")
        buf.write("\u0180\t\2\2\2\u0180M\3\2\2\2\u0181\u0182\7\b\2\2\u0182")
        buf.write("\u0183\5R*\2\u0183O\3\2\2\2\u0184\u0186\7\t\2\2\u0185")
        buf.write("\u0187\5R*\2\u0186\u0185\3\2\2\2\u0186\u0187\3\2\2\2\u0187")
        buf.write("Q\3\2\2\2\u0188\u0189\7\36\2\2\u0189\u018a\5T+\2\u018a")
        buf.write("S\3\2\2\2\u018b\u0192\5\34\17\2\u018c\u0192\5,\27\2\u018d")
        buf.write("\u0192\5.\30\2\u018e\u0192\5$\23\2\u018f\u0192\58\35\2")
        buf.write("\u0190\u0192\5> \2\u0191\u018b\3\2\2\2\u0191\u018c\3\2")
        buf.write("\2\2\u0191\u018d\3\2\2\2\u0191\u018e\3\2\2\2\u0191\u018f")
        buf.write("\3\2\2\2\u0191\u0190\3\2\2\2\u0192U\3\2\2\2\u0193\u0196")
        buf.write("\5X-\2\u0194\u0196\3\2\2\2\u0195\u0193\3\2\2\2\u0195\u0194")
        buf.write("\3\2\2\2\u0196W\3\2\2\2\u0197\u0198\5Z.\2\u0198\u0199")
        buf.write("\7*\2\2\u0199\u019a\5X-\2\u019a\u019d\3\2\2\2\u019b\u019d")
        buf.write("\5Z.\2\u019c\u0197\3\2\2\2\u019c\u019b\3\2\2\2\u019dY")
        buf.write("\3\2\2\2\u019e\u019f\5L\'\2\u019f\u01a4\7/\2\2\u01a0\u01a1")
        buf.write("\7(\2\2\u01a1\u01a2\5\b\5\2\u01a2\u01a3\7)\2\2\u01a3\u01a5")
        buf.write("\3\2\2\2\u01a4\u01a0\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5")
        buf.write("[\3\2\2\2\u01a6\u01a7\7\n\2\2\u01a7\u01a8\7/\2\2\u01a8")
        buf.write("\u01a9\7&\2\2\u01a9\u01aa\5V,\2\u01aa\u01ab\7\'\2\2\u01ab")
        buf.write("\u01ae\5^\60\2\u01ac\u01af\5r:\2\u01ad\u01af\5v<\2\u01ae")
        buf.write("\u01ac\3\2\2\2\u01ae\u01ad\3\2\2\2\u01ae\u01af\3\2\2\2")
        buf.write("\u01af]\3\2\2\2\u01b0\u01b1\7+\2\2\u01b1\u01b4\5^\60\2")
        buf.write("\u01b2\u01b4\3\2\2\2\u01b3\u01b0\3\2\2\2\u01b3\u01b2\3")
        buf.write("\2\2\2\u01b4_\3\2\2\2\u01b5\u01b6\7\20\2\2\u01b6\u01b7")
        buf.write("\5$\23\2\u01b7\u01b8\5F$\2\u01b8\u01ba\5b\62\2\u01b9\u01bb")
        buf.write("\5h\65\2\u01ba\u01b9\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb")
        buf.write("a\3\2\2\2\u01bc\u01bf\5d\63\2\u01bd\u01bf\3\2\2\2\u01be")
        buf.write("\u01bc\3\2\2\2\u01be\u01bd\3\2\2\2\u01bfc\3\2\2\2\u01c0")
        buf.write("\u01c1\5f\64\2\u01c1\u01c2\5^\60\2\u01c2\u01c3\5d\63\2")
        buf.write("\u01c3\u01c6\3\2\2\2\u01c4\u01c6\5f\64\2\u01c5\u01c0\3")
        buf.write("\2\2\2\u01c5\u01c4\3\2\2\2\u01c6e\3\2\2\2\u01c7\u01c8")
        buf.write("\7\22\2\2\u01c8\u01c9\5$\23\2\u01c9\u01ca\5F$\2\u01ca")
        buf.write("g\3\2\2\2\u01cb\u01cc\7\21\2\2\u01cc\u01cd\5$\23\2\u01cd")
        buf.write("\u01ce\5F$\2\u01cei\3\2\2\2\u01cf\u01d0\7\13\2\2\u01d0")
        buf.write("\u01d1\7/\2\2\u01d1\u01d2\7\f\2\2\u01d2\u01d3\5$\23\2")
        buf.write("\u01d3\u01d4\7\r\2\2\u01d4\u01d5\5l\67\2\u01d5\u01d6\5")
        buf.write("^\60\2\u01d6\u01d7\5F$\2\u01d7k\3\2\2\2\u01d8\u01d9\5")
        buf.write("T+\2\u01d9m\3\2\2\2\u01da\u01db\7\16\2\2\u01dbo\3\2\2")
        buf.write("\2\u01dc\u01dd\7\17\2\2\u01ddq\3\2\2\2\u01de\u01e0\7\7")
        buf.write("\2\2\u01df\u01e1\5T+\2\u01e0\u01df\3\2\2\2\u01e0\u01e1")
        buf.write("\3\2\2\2\u01e1s\3\2\2\2\u01e2\u01e3\5> \2\u01e3u\3\2\2")
        buf.write("\2\u01e4\u01e6\7\23\2\2\u01e5\u01e7\7+\2\2\u01e6\u01e5")
        buf.write("\3\2\2\2\u01e7\u01e8\3\2\2\2\u01e8\u01e6\3\2\2\2\u01e8")
        buf.write("\u01e9\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea\u01eb\5x=\2\u01eb")
        buf.write("\u01f2\7\24\2\2\u01ec\u01ee\7+\2\2\u01ed\u01ec\3\2\2\2")
        buf.write("\u01ee\u01ef\3\2\2\2\u01ef\u01ed\3\2\2\2\u01ef\u01f0\3")
        buf.write("\2\2\2\u01f0\u01f3\3\2\2\2\u01f1\u01f3\7\2\2\3\u01f2\u01ed")
        buf.write("\3\2\2\2\u01f2\u01f1\3\2\2\2\u01f3w\3\2\2\2\u01f4\u01f5")
        buf.write("\5z>\2\u01f5y\3\2\2\2\u01f6\u01f7\5F$\2\u01f7\u01f8\5")
        buf.write("z>\2\u01f8\u01fb\3\2\2\2\u01f9\u01fb\3\2\2\2\u01fa\u01f6")
        buf.write("\3\2\2\2\u01fa\u01f9\3\2\2\2\u01fb{\3\2\2\2\62\u0084\u0089")
        buf.write("\u008e\u0094\u0098\u009d\u00b0\u00c2\u00c6\u00cc\u00d0")
        buf.write("\u00d6\u00da\u00e0\u00e4\u00eb\u00f5\u0100\u0106\u0112")
        buf.write("\u011d\u0123\u012a\u0131\u0136\u014c\u0153\u015c\u0163")
        buf.write("\u016e\u0173\u0179\u017d\u0186\u0191\u0195\u019c\u01a4")
        buf.write("\u01ae\u01b3\u01ba\u01be\u01c5\u01e0\u01e8\u01ef\u01f2")
        buf.write("\u01fa")
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
    RULE_functionDecl = 45
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
                   "paramDeclPrime", "paramDeclAtom", "functionDecl", "nullableListOfNEWLINE", 
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

        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def functionDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.FunctionDeclContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.FunctionDeclContext,i)


        def mainFunction(self):
            return self.getTypedRuleContext(ZCodeParser.MainFunctionContext,0)


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
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 137
                self.match(ZCodeParser.NEWLINE)
                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 146
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 143
                    self.functionDecl() 
                self.state = 148
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 149
                self.mainFunction()


            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.FUNC:
                self.state = 152
                self.functionDecl()
                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 158
            self.match(ZCodeParser.EOF)
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
            self.state = 160
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 161
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 162
            self.match(ZCodeParser.LSBracket)
            self.state = 163
            self.arrayDim()
            self.state = 164
            self.match(ZCodeParser.RSBracket)
            self.state = 165
            self.match(ZCodeParser.LEFTARR)
            self.state = 166
            self.match(ZCodeParser.LSBracket)
            self.state = 167
            self.arrayInit()
            self.state = 168
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
            self.state = 174
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.match(ZCodeParser.NumberLit)
                self.state = 171
                self.match(ZCodeParser.COMMA)
                self.state = 172
                self.arrayDim()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
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
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.match(ZCodeParser.LSBracket)
                self.state = 177
                self.numberList()
                self.state = 178
                self.match(ZCodeParser.RSBracket)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self.match(ZCodeParser.LSBracket)
                self.state = 181
                self.boolList()
                self.state = 182
                self.match(ZCodeParser.RSBracket)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 184
                self.match(ZCodeParser.LSBracket)
                self.state = 185
                self.stringList()
                self.state = 186
                self.match(ZCodeParser.RSBracket)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 188
                self.match(ZCodeParser.LSBracket)
                self.state = 189
                self.arrayList()
                self.state = 190
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
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NumberLit]:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
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
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.match(ZCodeParser.NumberLit)
                self.state = 199
                self.match(ZCodeParser.COMMA)
                self.state = 200
                self.numberPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
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
            self.state = 206
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BooleanLit]:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
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
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.match(ZCodeParser.BooleanLit)
                self.state = 209
                self.match(ZCodeParser.COMMA)
                self.state = 210
                self.boolPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 211
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
            self.state = 216
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.StringLit]:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
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
            self.state = 222
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.match(ZCodeParser.StringLit)
                self.state = 219
                self.match(ZCodeParser.COMMA)
                self.state = 220
                self.stringPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
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
            self.state = 226
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LSBracket]:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
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
            self.state = 233
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.arrayInit()
                self.state = 229
                self.match(ZCodeParser.COMMA)
                self.state = 230
                self.arrayPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 232
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
            self.state = 236
            self.arithExpr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 243
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.ArithExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_arithExpr)
                    self.state = 238
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 239
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.PLUS or _la==ZCodeParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 240
                    self.arithExpr1(0) 
                self.state = 245
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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
            self.state = 247
            self.arithExpr2()
            self._ctx.stop = self._input.LT(-1)
            self.state = 254
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.ArithExpr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_arithExpr1)
                    self.state = 249
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 250
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MULT) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 251
                    self.arithExpr2() 
                self.state = 256
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
            self.state = 260
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                self.match(ZCodeParser.MINUS)
                self.state = 258
                self.arithExpr2()
                pass
            elif token in [ZCodeParser.NumberLit, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
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
            self.state = 262
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
            self.state = 265
            self.logicExpr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 272
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.LogicExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicExpr)
                    self.state = 267
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 268
                    self.match(ZCodeParser.OR)
                    self.state = 269
                    self.logicExpr1(0) 
                self.state = 274
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
            self.state = 276
            self.logicExpr2()
            self._ctx.stop = self._input.LT(-1)
            self.state = 283
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.LogicExpr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicExpr1)
                    self.state = 278
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 279
                    self.match(ZCodeParser.AND)
                    self.state = 280
                    self.logicExpr2() 
                self.state = 285
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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
            self.state = 289
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                self.match(ZCodeParser.NOT)
                self.state = 287
                self.logicExpr2()
                pass
            elif token in [ZCodeParser.BooleanLit, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 288
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
            self.state = 291
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
            self.state = 296
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.StringLit]:
                self.state = 294
                self.match(ZCodeParser.StringLit)
                pass
            elif token in [ZCodeParser.IDENTIFIER]:
                self.state = 295
                self.match(ZCodeParser.IDENTIFIER)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 303
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.StringConcatExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_stringConcatExpr)
                    self.state = 298
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 299
                    self.match(ZCodeParser.ELLIPSIS)
                    self.state = 300
                    self.stringConcatExpr(4) 
                self.state = 305
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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
            self.state = 308
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 306
                self.arithComp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 307
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
            self.state = 310
            self.arithExpr(0)
            self.state = 311
            self.arithRelOp()
            self.state = 312
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
            self.state = 314
            self.stringConcatExpr(0)
            self.state = 315
            self.literalOp()
            self.state = 316
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
            self.state = 318
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
            self.state = 320
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
            self.state = 322
            self.arrExpr()
            self.state = 323
            self.match(ZCodeParser.LSBracket)
            self.state = 324
            self.indexOp()
            self.state = 325
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
            self.state = 330
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 327
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 328
                self.functionCall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 329
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
            self.state = 337
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self.arrExpr()
                self.state = 333
                self.match(ZCodeParser.COMMA)
                self.state = 334
                self.indexOp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
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
            self.state = 339
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 340
            self.match(ZCodeParser.LBracket)
            self.state = 341
            self.functionArgsList()
            self.state = 342
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
            self.state = 346
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT, ZCodeParser.MINUS, ZCodeParser.NumberLit, ZCodeParser.BooleanLit, ZCodeParser.StringLit, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 344
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
            self.state = 353
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 348
                self.arg()
                self.state = 349
                self.match(ZCodeParser.COMMA)
                self.state = 350
                self.argsPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 352
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
            self.state = 355
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
            self.state = 364
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.IDENTIFIER]:
                self.state = 357
                self.functionCallStatement()
                pass
            elif token in [ZCodeParser.CONTINUE]:
                self.state = 358
                self.continueStatement()
                pass
            elif token in [ZCodeParser.RETURN]:
                self.state = 359
                self.returnStatement()
                pass
            elif token in [ZCodeParser.BREAK]:
                self.state = 360
                self.breakStatement()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.state = 361
                self.blockStatement()
                pass
            elif token in [ZCodeParser.IF]:
                self.state = 362
                self.ifStatement()
                pass
            elif token in [ZCodeParser.FOR]:
                self.state = 363
                self.forStatement()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 367 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 366
                    self.match(ZCodeParser.NEWLINE)

                else:
                    raise NoViableAltException(self)
                self.state = 369 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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
            self.state = 375
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 371
                self.normalDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 372
                self.arrayDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 373
                self.varDecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 374
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
            self.state = 377
            self.varType()
            self.state = 379
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LEFTARR:
                self.state = 378
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
            self.state = 381
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
            self.state = 383
            self.match(ZCodeParser.VAR)
            self.state = 384
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
            self.state = 386
            self.match(ZCodeParser.DYNAMIC)
            self.state = 388
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LEFTARR:
                self.state = 387
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
            self.state = 390
            self.match(ZCodeParser.LEFTARR)
            self.state = 391
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
            self.state = 399
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 393
                self.arithExpr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 394
                self.stringConcatExpr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 395
                self.relExpr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 396
                self.logicExpr(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 397
                self.elementAccessExpr()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 398
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
            self.state = 403
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 401
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
            self.state = 410
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 405
                self.paramDeclAtom()
                self.state = 406
                self.match(ZCodeParser.COMMA)
                self.state = 407
                self.paramDeclPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 409
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
            self.state = 412
            self.varType()
            self.state = 413
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 418
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LSBracket:
                self.state = 414
                self.match(ZCodeParser.LSBracket)
                self.state = 415
                self.arrayDim()
                self.state = 416
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
        self.enterRule(localctx, 90, self.RULE_functionDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.match(ZCodeParser.FUNC)
            self.state = 421
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 422
            self.match(ZCodeParser.LBracket)
            self.state = 423
            self.paramDeclList()
            self.state = 424
            self.match(ZCodeParser.RBracket)
            self.state = 425
            self.nullableListOfNEWLINE()
            self.state = 428
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN]:
                self.state = 426
                self.returnStatement()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.state = 427
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
            self.state = 433
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 430
                self.match(ZCodeParser.NEWLINE)
                self.state = 431
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
            self.state = 435
            self.match(ZCodeParser.IF)
            self.state = 436
            self.logicExpr(0)
            self.state = 437
            self.statement()
            self.state = 438
            self.elifStatementList()
            self.state = 440
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ELSE:
                self.state = 439
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
            self.state = 444
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ELIF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 442
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
            self.state = 451
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 446
                self.elifStatement()
                self.state = 447
                self.nullableListOfNEWLINE()
                self.state = 448
                self.elifStatementPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 450
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
            self.state = 453
            self.match(ZCodeParser.ELIF)
            self.state = 454
            self.logicExpr(0)
            self.state = 455
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
            self.state = 457
            self.match(ZCodeParser.ELSE)
            self.state = 458
            self.logicExpr(0)
            self.state = 459
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
            self.state = 461
            self.match(ZCodeParser.FOR)
            self.state = 462
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 463
            self.match(ZCodeParser.UNTIL)
            self.state = 464
            self.logicExpr(0)
            self.state = 465
            self.match(ZCodeParser.BY)
            self.state = 466
            self.updateExpr()
            self.state = 467
            self.nullableListOfNEWLINE()
            self.state = 468
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
            self.state = 470
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
            self.state = 472
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
            self.state = 474
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
            self.state = 476
            self.match(ZCodeParser.RETURN)
            self.state = 478
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NOT) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.NumberLit) | (1 << ZCodeParser.BooleanLit) | (1 << ZCodeParser.StringLit) | (1 << ZCodeParser.IDENTIFIER))) != 0):
                self.state = 477
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
            self.state = 480
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
            self.state = 482
            self.match(ZCodeParser.BEGIN)
            self.state = 484 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 483
                self.match(ZCodeParser.NEWLINE)
                self.state = 486 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZCodeParser.NEWLINE):
                    break

            self.state = 488
            self.blockStatementBody()
            self.state = 489
            self.match(ZCodeParser.END)
            self.state = 496
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEWLINE]:
                self.state = 491 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 490
                        self.match(ZCodeParser.NEWLINE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 493 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

                pass
            elif token in [ZCodeParser.EOF]:
                self.state = 495
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
            self.state = 498
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
            self.state = 504
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 500
                self.statement()
                self.state = 501
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
         




