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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65")
        buf.write("\u0196\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\3\2\3\2\3\2")
        buf.write("\3\3\3\3\5\3N\n\3\3\3\3\3\3\3\5\3S\n\3\3\3\5\3V\n\3\3")
        buf.write("\4\3\4\3\4\3\4\3\4\5\4]\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5n\n\5\3\6\3\6\3")
        buf.write("\7\3\7\3\b\3\b\3\b\5\bw\n\b\3\t\3\t\3\t\3\t\3\t\3\t\5")
        buf.write("\t\177\n\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u0089\n")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u0094\n\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u009f\n\t\3\t\3")
        buf.write("\t\3\t\3\t\5\t\u00a5\n\t\3\n\3\n\3\n\3\n\5\n\u00ab\n\n")
        buf.write("\3\13\3\13\5\13\u00af\n\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\5\13\u00b7\n\13\3\13\3\13\3\f\3\f\5\f\u00bd\n\f\3")
        buf.write("\f\3\f\3\f\5\f\u00c2\n\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\5\r\u00ce\n\r\3\r\3\r\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\5\16\u00d8\n\16\3\16\3\16\3\17\3\17\3\17\3\17")
        buf.write("\3\17\5\17\u00e1\n\17\3\20\3\20\3\20\3\20\3\20\5\20\u00e8")
        buf.write("\n\20\3\20\3\20\5\20\u00ec\n\20\3\20\5\20\u00ef\n\20\3")
        buf.write("\21\3\21\3\21\3\21\3\22\3\22\5\22\u00f7\n\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\5\23\u00fe\n\23\3\24\3\24\3\24\3\24\5")
        buf.write("\24\u0104\n\24\3\25\3\25\3\25\3\25\3\26\3\26\5\26\u010c")
        buf.write("\n\26\3\27\3\27\3\27\3\27\5\27\u0112\n\27\3\30\3\30\3")
        buf.write("\30\3\30\3\31\3\31\3\31\3\31\5\31\u011c\n\31\3\31\3\31")
        buf.write("\3\31\5\31\u0121\n\31\3\31\3\31\3\31\3\31\3\31\3\31\3")
        buf.write("\31\3\31\3\31\5\31\u012c\n\31\5\31\u012e\n\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\5\32\u0135\n\32\3\33\3\33\3\33\3\33\3")
        buf.write("\33\5\33\u013c\n\33\3\34\3\34\3\34\3\34\3\34\3\34\7\34")
        buf.write("\u0144\n\34\f\34\16\34\u0147\13\34\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\7\35\u014f\n\35\f\35\16\35\u0152\13\35\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\7\36\u015a\n\36\f\36\16\36\u015d")
        buf.write("\13\36\3\37\3\37\3\37\3\37\3\37\5\37\u0164\n\37\3 \3 ")
        buf.write("\3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \7 \u0173\n \f \16 \u0176")
        buf.write("\13 \3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\5!\u0184\n!\3")
        buf.write("\"\3\"\5\"\u0188\n\"\3#\3#\3#\3#\3#\5#\u018f\n#\3$\3$")
        buf.write("\3$\5$\u0194\n$\3$\2\6\668:>%\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF\2\6\4\2\20")
        buf.write("\25\35\35\3\2\f\r\3\2\b\t\4\2\n\13%%\2\u01ae\2H\3\2\2")
        buf.write("\2\4U\3\2\2\2\6\\\3\2\2\2\bm\3\2\2\2\no\3\2\2\2\fq\3\2")
        buf.write("\2\2\16s\3\2\2\2\20\u00a4\3\2\2\2\22\u00aa\3\2\2\2\24")
        buf.write("\u00ae\3\2\2\2\26\u00bc\3\2\2\2\30\u00c5\3\2\2\2\32\u00d1")
        buf.write("\3\2\2\2\34\u00e0\3\2\2\2\36\u00e2\3\2\2\2 \u00f0\3\2")
        buf.write("\2\2\"\u00f6\3\2\2\2$\u00fd\3\2\2\2&\u00ff\3\2\2\2(\u0105")
        buf.write("\3\2\2\2*\u010b\3\2\2\2,\u0111\3\2\2\2.\u0113\3\2\2\2")
        buf.write("\60\u012d\3\2\2\2\62\u0134\3\2\2\2\64\u013b\3\2\2\2\66")
        buf.write("\u013d\3\2\2\28\u0148\3\2\2\2:\u0153\3\2\2\2<\u0163\3")
        buf.write("\2\2\2>\u0165\3\2\2\2@\u0183\3\2\2\2B\u0187\3\2\2\2D\u018e")
        buf.write("\3\2\2\2F\u0193\3\2\2\2HI\5\4\3\2IJ\7\2\2\3J\3\3\2\2\2")
        buf.write("KN\5F$\2LN\3\2\2\2MK\3\2\2\2ML\3\2\2\2NO\3\2\2\2OR\5\6")
        buf.write("\4\2PS\5F$\2QS\3\2\2\2RP\3\2\2\2RQ\3\2\2\2SV\3\2\2\2T")
        buf.write("V\3\2\2\2UM\3\2\2\2UT\3\2\2\2V\5\3\2\2\2W]\5\b\5\2XY\5")
        buf.write("\b\5\2YZ\5F$\2Z[\5\6\4\2[]\3\2\2\2\\W\3\2\2\2\\X\3\2\2")
        buf.write("\2]\7\3\2\2\2^_\5> \2_`\7\26\2\2`a\5B\"\2ab\7\27\2\2b")
        buf.write("n\3\2\2\2cn\5\62\32\2dn\5\60\31\2en\5.\30\2fn\5\32\16")
        buf.write("\2gn\5\36\20\2hn\5\n\6\2in\5\f\7\2jn\5\16\b\2kn\5\20\t")
        buf.write("\2ln\5\30\r\2m^\3\2\2\2mc\3\2\2\2md\3\2\2\2me\3\2\2\2")
        buf.write("mf\3\2\2\2mg\3\2\2\2mh\3\2\2\2mi\3\2\2\2mj\3\2\2\2mk\3")
        buf.write("\2\2\2ml\3\2\2\2n\t\3\2\2\2op\7!\2\2p\13\3\2\2\2qr\7\"")
        buf.write("\2\2r\r\3\2\2\2sv\7#\2\2tw\5\62\32\2uw\3\2\2\2vt\3\2\2")
        buf.write("\2vu\3\2\2\2w\17\3\2\2\2xy\7\4\2\2yz\7\26\2\2z{\5\62\32")
        buf.write("\2{~\7\27\2\2|\177\5F$\2}\177\3\2\2\2~|\3\2\2\2~}\3\2")
        buf.write("\2\2\177\u0080\3\2\2\2\u0080\u0081\5\b\5\2\u0081\u00a5")
        buf.write("\3\2\2\2\u0082\u0083\7\4\2\2\u0083\u0084\7\26\2\2\u0084")
        buf.write("\u0085\5\62\32\2\u0085\u0088\7\27\2\2\u0086\u0089\5F$")
        buf.write("\2\u0087\u0089\3\2\2\2\u0088\u0086\3\2\2\2\u0088\u0087")
        buf.write("\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u008b\5\b\5\2\u008b")
        buf.write("\u008c\5\22\n\2\u008c\u00a5\3\2\2\2\u008d\u008e\7\4\2")
        buf.write("\2\u008e\u008f\7\26\2\2\u008f\u0090\5\62\32\2\u0090\u0093")
        buf.write("\7\27\2\2\u0091\u0094\5F$\2\u0092\u0094\3\2\2\2\u0093")
        buf.write("\u0091\3\2\2\2\u0093\u0092\3\2\2\2\u0094\u0095\3\2\2\2")
        buf.write("\u0095\u0096\5\b\5\2\u0096\u0097\5\26\f\2\u0097\u00a5")
        buf.write("\3\2\2\2\u0098\u0099\7\4\2\2\u0099\u009a\7\26\2\2\u009a")
        buf.write("\u009b\5\62\32\2\u009b\u009e\7\27\2\2\u009c\u009f\5F$")
        buf.write("\2\u009d\u009f\3\2\2\2\u009e\u009c\3\2\2\2\u009e\u009d")
        buf.write("\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a1\5\b\5\2\u00a1")
        buf.write("\u00a2\5\22\n\2\u00a2\u00a3\5\26\f\2\u00a3\u00a5\3\2\2")
        buf.write("\2\u00a4x\3\2\2\2\u00a4\u0082\3\2\2\2\u00a4\u008d\3\2")
        buf.write("\2\2\u00a4\u0098\3\2\2\2\u00a5\21\3\2\2\2\u00a6\u00ab")
        buf.write("\5\24\13\2\u00a7\u00a8\5\24\13\2\u00a8\u00a9\5\22\n\2")
        buf.write("\u00a9\u00ab\3\2\2\2\u00aa\u00a6\3\2\2\2\u00aa\u00a7\3")
        buf.write("\2\2\2\u00ab\23\3\2\2\2\u00ac\u00af\5F$\2\u00ad\u00af")
        buf.write("\3\2\2\2\u00ae\u00ac\3\2\2\2\u00ae\u00ad\3\2\2\2\u00af")
        buf.write("\u00b0\3\2\2\2\u00b0\u00b1\7\5\2\2\u00b1\u00b2\7\26\2")
        buf.write("\2\u00b2\u00b3\5\62\32\2\u00b3\u00b6\7\27\2\2\u00b4\u00b7")
        buf.write("\5F$\2\u00b5\u00b7\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b6\u00b5")
        buf.write("\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00b9\5\b\5\2\u00b9")
        buf.write("\25\3\2\2\2\u00ba\u00bd\5F$\2\u00bb\u00bd\3\2\2\2\u00bc")
        buf.write("\u00ba\3\2\2\2\u00bc\u00bb\3\2\2\2\u00bd\u00be\3\2\2\2")
        buf.write("\u00be\u00c1\7\6\2\2\u00bf\u00c2\5F$\2\u00c0\u00c2\3\2")
        buf.write("\2\2\u00c1\u00bf\3\2\2\2\u00c1\u00c0\3\2\2\2\u00c2\u00c3")
        buf.write("\3\2\2\2\u00c3\u00c4\5\b\5\2\u00c4\27\3\2\2\2\u00c5\u00c6")
        buf.write("\7\7\2\2\u00c6\u00c7\7-\2\2\u00c7\u00c8\7&\2\2\u00c8\u00c9")
        buf.write("\5\62\32\2\u00c9\u00ca\7\'\2\2\u00ca\u00cd\5\62\32\2\u00cb")
        buf.write("\u00ce\5F$\2\u00cc\u00ce\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd")
        buf.write("\u00cc\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d0\5\b\5\2")
        buf.write("\u00d0\31\3\2\2\2\u00d1\u00d7\7\32\2\2\u00d2\u00d3\5F")
        buf.write("$\2\u00d3\u00d4\5\34\17\2\u00d4\u00d5\5F$\2\u00d5\u00d8")
        buf.write("\3\2\2\2\u00d6\u00d8\5F$\2\u00d7\u00d2\3\2\2\2\u00d7\u00d6")
        buf.write("\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9\u00da\7\33\2\2\u00da")
        buf.write("\33\3\2\2\2\u00db\u00e1\5\b\5\2\u00dc\u00dd\5\b\5\2\u00dd")
        buf.write("\u00de\5F$\2\u00de\u00df\5\34\17\2\u00df\u00e1\3\2\2\2")
        buf.write("\u00e0\u00db\3\2\2\2\u00e0\u00dc\3\2\2\2\u00e1\35\3\2")
        buf.write("\2\2\u00e2\u00e3\7$\2\2\u00e3\u00e4\7-\2\2\u00e4\u00ee")
        buf.write("\5 \21\2\u00e5\u00e8\5F$\2\u00e6\u00e8\3\2\2\2\u00e7\u00e5")
        buf.write("\3\2\2\2\u00e7\u00e6\3\2\2\2\u00e8\u00eb\3\2\2\2\u00e9")
        buf.write("\u00ec\5\16\b\2\u00ea\u00ec\5\32\16\2\u00eb\u00e9\3\2")
        buf.write("\2\2\u00eb\u00ea\3\2\2\2\u00ec\u00ef\3\2\2\2\u00ed\u00ef")
        buf.write("\3\2\2\2\u00ee\u00e7\3\2\2\2\u00ee\u00ed\3\2\2\2\u00ef")
        buf.write("\37\3\2\2\2\u00f0\u00f1\7\26\2\2\u00f1\u00f2\5\"\22\2")
        buf.write("\u00f2\u00f3\7\27\2\2\u00f3!\3\2\2\2\u00f4\u00f7\5$\23")
        buf.write("\2\u00f5\u00f7\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f6\u00f5")
        buf.write("\3\2\2\2\u00f7#\3\2\2\2\u00f8\u00fe\5&\24\2\u00f9\u00fa")
        buf.write("\5&\24\2\u00fa\u00fb\7 \2\2\u00fb\u00fc\5$\23\2\u00fc")
        buf.write("\u00fe\3\2\2\2\u00fd\u00f8\3\2\2\2\u00fd\u00f9\3\2\2\2")
        buf.write("\u00fe%\3\2\2\2\u00ff\u0100\7\3\2\2\u0100\u0103\7-\2\2")
        buf.write("\u0101\u0104\5(\25\2\u0102\u0104\3\2\2\2\u0103\u0101\3")
        buf.write("\2\2\2\u0103\u0102\3\2\2\2\u0104\'\3\2\2\2\u0105\u0106")
        buf.write("\7\30\2\2\u0106\u0107\5*\26\2\u0107\u0108\7\31\2\2\u0108")
        buf.write(")\3\2\2\2\u0109\u010c\5,\27\2\u010a\u010c\3\2\2\2\u010b")
        buf.write("\u0109\3\2\2\2\u010b\u010a\3\2\2\2\u010c+\3\2\2\2\u010d")
        buf.write("\u0112\7)\2\2\u010e\u010f\7)\2\2\u010f\u0110\7 \2\2\u0110")
        buf.write("\u0112\5,\27\2\u0111\u010d\3\2\2\2\u0111\u010e\3\2\2\2")
        buf.write("\u0112-\3\2\2\2\u0113\u0114\5\62\32\2\u0114\u0115\7\17")
        buf.write("\2\2\u0115\u0116\5\62\32\2\u0116/\3\2\2\2\u0117\u0118")
        buf.write("\7\3\2\2\u0118\u011b\7-\2\2\u0119\u011c\5(\25\2\u011a")
        buf.write("\u011c\3\2\2\2\u011b\u0119\3\2\2\2\u011b\u011a\3\2\2\2")
        buf.write("\u011c\u0120\3\2\2\2\u011d\u011e\7\17\2\2\u011e\u0121")
        buf.write("\5\62\32\2\u011f\u0121\3\2\2\2\u0120\u011d\3\2\2\2\u0120")
        buf.write("\u011f\3\2\2\2\u0121\u012e\3\2\2\2\u0122\u0123\7\36\2")
        buf.write("\2\u0123\u0124\7-\2\2\u0124\u0125\7\17\2\2\u0125\u012e")
        buf.write("\5\62\32\2\u0126\u0127\7\37\2\2\u0127\u012b\7-\2\2\u0128")
        buf.write("\u0129\7\17\2\2\u0129\u012c\5\62\32\2\u012a\u012c\3\2")
        buf.write("\2\2\u012b\u0128\3\2\2\2\u012b\u012a\3\2\2\2\u012c\u012e")
        buf.write("\3\2\2\2\u012d\u0117\3\2\2\2\u012d\u0122\3\2\2\2\u012d")
        buf.write("\u0126\3\2\2\2\u012e\61\3\2\2\2\u012f\u0130\5\64\33\2")
        buf.write("\u0130\u0131\7\16\2\2\u0131\u0132\5\64\33\2\u0132\u0135")
        buf.write("\3\2\2\2\u0133\u0135\5\64\33\2\u0134\u012f\3\2\2\2\u0134")
        buf.write("\u0133\3\2\2\2\u0135\63\3\2\2\2\u0136\u0137\5\66\34\2")
        buf.write("\u0137\u0138\t\2\2\2\u0138\u0139\5\66\34\2\u0139\u013c")
        buf.write("\3\2\2\2\u013a\u013c\5\66\34\2\u013b\u0136\3\2\2\2\u013b")
        buf.write("\u013a\3\2\2\2\u013c\65\3\2\2\2\u013d\u013e\b\34\1\2\u013e")
        buf.write("\u013f\58\35\2\u013f\u0145\3\2\2\2\u0140\u0141\f\4\2\2")
        buf.write("\u0141\u0142\t\3\2\2\u0142\u0144\58\35\2\u0143\u0140\3")
        buf.write("\2\2\2\u0144\u0147\3\2\2\2\u0145\u0143\3\2\2\2\u0145\u0146")
        buf.write("\3\2\2\2\u0146\67\3\2\2\2\u0147\u0145\3\2\2\2\u0148\u0149")
        buf.write("\b\35\1\2\u0149\u014a\5:\36\2\u014a\u0150\3\2\2\2\u014b")
        buf.write("\u014c\f\4\2\2\u014c\u014d\t\4\2\2\u014d\u014f\5:\36\2")
        buf.write("\u014e\u014b\3\2\2\2\u014f\u0152\3\2\2\2\u0150\u014e\3")
        buf.write("\2\2\2\u0150\u0151\3\2\2\2\u01519\3\2\2\2\u0152\u0150")
        buf.write("\3\2\2\2\u0153\u0154\b\36\1\2\u0154\u0155\5<\37\2\u0155")
        buf.write("\u015b\3\2\2\2\u0156\u0157\f\4\2\2\u0157\u0158\t\5\2\2")
        buf.write("\u0158\u015a\5<\37\2\u0159\u0156\3\2\2\2\u015a\u015d\3")
        buf.write("\2\2\2\u015b\u0159\3\2\2\2\u015b\u015c\3\2\2\2\u015c;")
        buf.write("\3\2\2\2\u015d\u015b\3\2\2\2\u015e\u015f\7\b\2\2\u015f")
        buf.write("\u0164\5<\37\2\u0160\u0161\7\34\2\2\u0161\u0164\5<\37")
        buf.write("\2\u0162\u0164\5> \2\u0163\u015e\3\2\2\2\u0163\u0160\3")
        buf.write("\2\2\2\u0163\u0162\3\2\2\2\u0164=\3\2\2\2\u0165\u0166")
        buf.write("\b \1\2\u0166\u0167\5@!\2\u0167\u0174\3\2\2\2\u0168\u0169")
        buf.write("\f\5\2\2\u0169\u016a\7\30\2\2\u016a\u016b\5B\"\2\u016b")
        buf.write("\u016c\7\31\2\2\u016c\u0173\3\2\2\2\u016d\u016e\f\4\2")
        buf.write("\2\u016e\u016f\7\26\2\2\u016f\u0170\5B\"\2\u0170\u0171")
        buf.write("\7\27\2\2\u0171\u0173\3\2\2\2\u0172\u0168\3\2\2\2\u0172")
        buf.write("\u016d\3\2\2\2\u0173\u0176\3\2\2\2\u0174\u0172\3\2\2\2")
        buf.write("\u0174\u0175\3\2\2\2\u0175?\3\2\2\2\u0176\u0174\3\2\2")
        buf.write("\2\u0177\u0184\7)\2\2\u0178\u0184\7\61\2\2\u0179\u0184")
        buf.write("\7(\2\2\u017a\u0184\7-\2\2\u017b\u017c\7\30\2\2\u017c")
        buf.write("\u017d\5B\"\2\u017d\u017e\7\31\2\2\u017e\u0184\3\2\2\2")
        buf.write("\u017f\u0180\7\26\2\2\u0180\u0181\5\62\32\2\u0181\u0182")
        buf.write("\7\27\2\2\u0182\u0184\3\2\2\2\u0183\u0177\3\2\2\2\u0183")
        buf.write("\u0178\3\2\2\2\u0183\u0179\3\2\2\2\u0183\u017a\3\2\2\2")
        buf.write("\u0183\u017b\3\2\2\2\u0183\u017f\3\2\2\2\u0184A\3\2\2")
        buf.write("\2\u0185\u0188\5D#\2\u0186\u0188\3\2\2\2\u0187\u0185\3")
        buf.write("\2\2\2\u0187\u0186\3\2\2\2\u0188C\3\2\2\2\u0189\u018f")
        buf.write("\5\62\32\2\u018a\u018b\5\62\32\2\u018b\u018c\7 \2\2\u018c")
        buf.write("\u018d\5D#\2\u018d\u018f\3\2\2\2\u018e\u0189\3\2\2\2\u018e")
        buf.write("\u018a\3\2\2\2\u018fE\3\2\2\2\u0190\u0191\7\64\2\2\u0191")
        buf.write("\u0194\5F$\2\u0192\u0194\7\64\2\2\u0193\u0190\3\2\2\2")
        buf.write("\u0193\u0192\3\2\2\2\u0194G\3\2\2\2-MRU\\mv~\u0088\u0093")
        buf.write("\u009e\u00a4\u00aa\u00ae\u00b6\u00bc\u00c1\u00cd\u00d7")
        buf.write("\u00e0\u00e7\u00eb\u00ee\u00f6\u00fd\u0103\u010b\u0111")
        buf.write("\u011b\u0120\u012b\u012d\u0134\u013b\u0145\u0150\u015b")
        buf.write("\u0163\u0172\u0174\u0183\u0187\u018e\u0193")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'if'", "'elif'", "'else'", 
                     "'for'", "'-'", "'+'", "'*'", "'/'", "'and'", "'or'", 
                     "'...'", "'<-'", "'='", "'=='", "'>='", "'>'", "'<='", 
                     "'<'", "'('", "')'", "'['", "']'", "'begin'", "'end'", 
                     "'not'", "'!='", "'var'", "'dynamic'", "','", "'break'", 
                     "'continue'", "'return'", "'func'", "'%'", "'until'", 
                     "'by'" ]

    symbolicNames = [ "<INVALID>", "TYPE", "IF", "ELIF", "ELSE", "FOR", 
                      "SUB", "ADD", "MUL", "DIV", "AND", "OR", "CONCAT", 
                      "ASSIGN", "EQ", "DEQ", "GE", "GT", "LE", "LT", "LP", 
                      "RP", "LB", "RB", "BEGIN", "END", "NOT", "NEQ", "VAR", 
                      "DYN", "COMMA", "BREAK", "CONTINUE", "RETURN", "FUNC", 
                      "MOD", "UNTIL", "BY", "BoolLit", "NumberLit", "INVALID_NUMBER_1", 
                      "INVALID_NUMBER_2", "INVALID_NUMBER_3", "IDENTIFIER", 
                      "INVALID_IDENTIFIER", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                      "StringLit", "COMMENT", "WS", "NEWLINE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_stms = 1
    RULE_stm_lists = 2
    RULE_stm = 3
    RULE_r_break = 4
    RULE_r_continue = 5
    RULE_r_return = 6
    RULE_r_if = 7
    RULE_r_elifs = 8
    RULE_r_elif = 9
    RULE_r_else = 10
    RULE_r_for = 11
    RULE_block = 12
    RULE_block_stms = 13
    RULE_func = 14
    RULE_arg_group = 15
    RULE_args = 16
    RULE_arg_list = 17
    RULE_arg = 18
    RULE_type_index = 19
    RULE_type_index_nums = 20
    RULE_type_index_num_list = 21
    RULE_ass = 22
    RULE_decl = 23
    RULE_expr = 24
    RULE_expr1 = 25
    RULE_expr2 = 26
    RULE_expr3 = 27
    RULE_expr4 = 28
    RULE_expr5 = 29
    RULE_expr6 = 30
    RULE_term = 31
    RULE_expr_list = 32
    RULE_exprPrime = 33
    RULE_listOfNEWLINE = 34

    ruleNames =  [ "program", "stms", "stm_lists", "stm", "r_break", "r_continue", 
                   "r_return", "r_if", "r_elifs", "r_elif", "r_else", "r_for", 
                   "block", "block_stms", "func", "arg_group", "args", "arg_list", 
                   "arg", "type_index", "type_index_nums", "type_index_num_list", 
                   "ass", "decl", "expr", "expr1", "expr2", "expr3", "expr4", 
                   "expr5", "expr6", "term", "expr_list", "exprPrime", "listOfNEWLINE" ]

    EOF = Token.EOF
    TYPE=1
    IF=2
    ELIF=3
    ELSE=4
    FOR=5
    SUB=6
    ADD=7
    MUL=8
    DIV=9
    AND=10
    OR=11
    CONCAT=12
    ASSIGN=13
    EQ=14
    DEQ=15
    GE=16
    GT=17
    LE=18
    LT=19
    LP=20
    RP=21
    LB=22
    RB=23
    BEGIN=24
    END=25
    NOT=26
    NEQ=27
    VAR=28
    DYN=29
    COMMA=30
    BREAK=31
    CONTINUE=32
    RETURN=33
    FUNC=34
    MOD=35
    UNTIL=36
    BY=37
    BoolLit=38
    NumberLit=39
    INVALID_NUMBER_1=40
    INVALID_NUMBER_2=41
    INVALID_NUMBER_3=42
    IDENTIFIER=43
    INVALID_IDENTIFIER=44
    ILLEGAL_ESCAPE=45
    UNCLOSE_STRING=46
    StringLit=47
    COMMENT=48
    WS=49
    NEWLINE=50
    ERROR_CHAR=51

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

        def stms(self):
            return self.getTypedRuleContext(ZCodeParser.StmsContext,0)


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
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.stms()
            self.state = 71
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stm_lists(self):
            return self.getTypedRuleContext(ZCodeParser.Stm_listsContext,0)


        def listOfNEWLINE(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ListOfNEWLINEContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ListOfNEWLINEContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stms

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStms" ):
                return visitor.visitStms(self)
            else:
                return visitor.visitChildren(self)




    def stms(self):

        localctx = ZCodeParser.StmsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stms)
        try:
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TYPE, ZCodeParser.IF, ZCodeParser.FOR, ZCodeParser.SUB, ZCodeParser.LP, ZCodeParser.LB, ZCodeParser.BEGIN, ZCodeParser.NOT, ZCodeParser.VAR, ZCodeParser.DYN, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.RETURN, ZCodeParser.FUNC, ZCodeParser.BoolLit, ZCodeParser.NumberLit, ZCodeParser.IDENTIFIER, ZCodeParser.StringLit, ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.NEWLINE]:
                    self.state = 73
                    self.listOfNEWLINE()
                    pass
                elif token in [ZCodeParser.TYPE, ZCodeParser.IF, ZCodeParser.FOR, ZCodeParser.SUB, ZCodeParser.LP, ZCodeParser.LB, ZCodeParser.BEGIN, ZCodeParser.NOT, ZCodeParser.VAR, ZCodeParser.DYN, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.RETURN, ZCodeParser.FUNC, ZCodeParser.BoolLit, ZCodeParser.NumberLit, ZCodeParser.IDENTIFIER, ZCodeParser.StringLit]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 77
                self.stm_lists()
                self.state = 80
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.NEWLINE]:
                    self.state = 78
                    self.listOfNEWLINE()
                    pass
                elif token in [ZCodeParser.EOF]:
                    pass
                else:
                    raise NoViableAltException(self)

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


    class Stm_listsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stm(self):
            return self.getTypedRuleContext(ZCodeParser.StmContext,0)


        def listOfNEWLINE(self):
            return self.getTypedRuleContext(ZCodeParser.ListOfNEWLINEContext,0)


        def stm_lists(self):
            return self.getTypedRuleContext(ZCodeParser.Stm_listsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stm_lists

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStm_lists" ):
                return visitor.visitStm_lists(self)
            else:
                return visitor.visitChildren(self)




    def stm_lists(self):

        localctx = ZCodeParser.Stm_listsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stm_lists)
        try:
            self.state = 90
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.stm()
                self.state = 87
                self.listOfNEWLINE()
                self.state = 88
                self.stm_lists()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def expr_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_listContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def decl(self):
            return self.getTypedRuleContext(ZCodeParser.DeclContext,0)


        def ass(self):
            return self.getTypedRuleContext(ZCodeParser.AssContext,0)


        def block(self):
            return self.getTypedRuleContext(ZCodeParser.BlockContext,0)


        def func(self):
            return self.getTypedRuleContext(ZCodeParser.FuncContext,0)


        def r_break(self):
            return self.getTypedRuleContext(ZCodeParser.R_breakContext,0)


        def r_continue(self):
            return self.getTypedRuleContext(ZCodeParser.R_continueContext,0)


        def r_return(self):
            return self.getTypedRuleContext(ZCodeParser.R_returnContext,0)


        def r_if(self):
            return self.getTypedRuleContext(ZCodeParser.R_ifContext,0)


        def r_for(self):
            return self.getTypedRuleContext(ZCodeParser.R_forContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStm" ):
                return visitor.visitStm(self)
            else:
                return visitor.visitChildren(self)




    def stm(self):

        localctx = ZCodeParser.StmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stm)
        try:
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.expr6(0)
                self.state = 93
                self.match(ZCodeParser.LP)
                self.state = 94
                self.expr_list()
                self.state = 95
                self.match(ZCodeParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 97
                self.expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 98
                self.decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 99
                self.ass()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 100
                self.block()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 101
                self.func()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 102
                self.r_break()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 103
                self.r_continue()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 104
                self.r_return()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 105
                self.r_if()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 106
                self.r_for()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class R_breakContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_r_break

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitR_break" ):
                return visitor.visitR_break(self)
            else:
                return visitor.visitChildren(self)




    def r_break(self):

        localctx = ZCodeParser.R_breakContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_r_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(ZCodeParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class R_continueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_r_continue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitR_continue" ):
                return visitor.visitR_continue(self)
            else:
                return visitor.visitChildren(self)




    def r_continue(self):

        localctx = ZCodeParser.R_continueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_r_continue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(ZCodeParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class R_returnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_r_return

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitR_return" ):
                return visitor.visitR_return(self)
            else:
                return visitor.visitChildren(self)




    def r_return(self):

        localctx = ZCodeParser.R_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_r_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(ZCodeParser.RETURN)
            self.state = 116
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUB, ZCodeParser.LP, ZCodeParser.LB, ZCodeParser.NOT, ZCodeParser.BoolLit, ZCodeParser.NumberLit, ZCodeParser.IDENTIFIER, ZCodeParser.StringLit]:
                self.state = 114
                self.expr()
                pass
            elif token in [ZCodeParser.EOF, ZCodeParser.ELIF, ZCodeParser.ELSE, ZCodeParser.NEWLINE]:
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


    class R_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def stm(self):
            return self.getTypedRuleContext(ZCodeParser.StmContext,0)


        def listOfNEWLINE(self):
            return self.getTypedRuleContext(ZCodeParser.ListOfNEWLINEContext,0)


        def r_elifs(self):
            return self.getTypedRuleContext(ZCodeParser.R_elifsContext,0)


        def r_else(self):
            return self.getTypedRuleContext(ZCodeParser.R_elseContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_r_if

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitR_if" ):
                return visitor.visitR_if(self)
            else:
                return visitor.visitChildren(self)




    def r_if(self):

        localctx = ZCodeParser.R_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_r_if)
        try:
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.match(ZCodeParser.IF)
                self.state = 119
                self.match(ZCodeParser.LP)
                self.state = 120
                self.expr()
                self.state = 121
                self.match(ZCodeParser.RP)
                self.state = 124
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.NEWLINE]:
                    self.state = 122
                    self.listOfNEWLINE()
                    pass
                elif token in [ZCodeParser.TYPE, ZCodeParser.IF, ZCodeParser.FOR, ZCodeParser.SUB, ZCodeParser.LP, ZCodeParser.LB, ZCodeParser.BEGIN, ZCodeParser.NOT, ZCodeParser.VAR, ZCodeParser.DYN, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.RETURN, ZCodeParser.FUNC, ZCodeParser.BoolLit, ZCodeParser.NumberLit, ZCodeParser.IDENTIFIER, ZCodeParser.StringLit]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 126
                self.stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.match(ZCodeParser.IF)
                self.state = 129
                self.match(ZCodeParser.LP)
                self.state = 130
                self.expr()
                self.state = 131
                self.match(ZCodeParser.RP)
                self.state = 134
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.NEWLINE]:
                    self.state = 132
                    self.listOfNEWLINE()
                    pass
                elif token in [ZCodeParser.TYPE, ZCodeParser.IF, ZCodeParser.FOR, ZCodeParser.SUB, ZCodeParser.LP, ZCodeParser.LB, ZCodeParser.BEGIN, ZCodeParser.NOT, ZCodeParser.VAR, ZCodeParser.DYN, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.RETURN, ZCodeParser.FUNC, ZCodeParser.BoolLit, ZCodeParser.NumberLit, ZCodeParser.IDENTIFIER, ZCodeParser.StringLit]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 136
                self.stm()
                self.state = 137
                self.r_elifs()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 139
                self.match(ZCodeParser.IF)
                self.state = 140
                self.match(ZCodeParser.LP)
                self.state = 141
                self.expr()
                self.state = 142
                self.match(ZCodeParser.RP)
                self.state = 145
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.NEWLINE]:
                    self.state = 143
                    self.listOfNEWLINE()
                    pass
                elif token in [ZCodeParser.TYPE, ZCodeParser.IF, ZCodeParser.FOR, ZCodeParser.SUB, ZCodeParser.LP, ZCodeParser.LB, ZCodeParser.BEGIN, ZCodeParser.NOT, ZCodeParser.VAR, ZCodeParser.DYN, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.RETURN, ZCodeParser.FUNC, ZCodeParser.BoolLit, ZCodeParser.NumberLit, ZCodeParser.IDENTIFIER, ZCodeParser.StringLit]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 147
                self.stm()
                self.state = 148
                self.r_else()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 150
                self.match(ZCodeParser.IF)
                self.state = 151
                self.match(ZCodeParser.LP)
                self.state = 152
                self.expr()
                self.state = 153
                self.match(ZCodeParser.RP)
                self.state = 156
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.NEWLINE]:
                    self.state = 154
                    self.listOfNEWLINE()
                    pass
                elif token in [ZCodeParser.TYPE, ZCodeParser.IF, ZCodeParser.FOR, ZCodeParser.SUB, ZCodeParser.LP, ZCodeParser.LB, ZCodeParser.BEGIN, ZCodeParser.NOT, ZCodeParser.VAR, ZCodeParser.DYN, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.RETURN, ZCodeParser.FUNC, ZCodeParser.BoolLit, ZCodeParser.NumberLit, ZCodeParser.IDENTIFIER, ZCodeParser.StringLit]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 158
                self.stm()
                self.state = 159
                self.r_elifs()
                self.state = 160
                self.r_else()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class R_elifsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def r_elif(self):
            return self.getTypedRuleContext(ZCodeParser.R_elifContext,0)


        def r_elifs(self):
            return self.getTypedRuleContext(ZCodeParser.R_elifsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_r_elifs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitR_elifs" ):
                return visitor.visitR_elifs(self)
            else:
                return visitor.visitChildren(self)




    def r_elifs(self):

        localctx = ZCodeParser.R_elifsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_r_elifs)
        try:
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.r_elif()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
                self.r_elif()
                self.state = 166
                self.r_elifs()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class R_elifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def stm(self):
            return self.getTypedRuleContext(ZCodeParser.StmContext,0)


        def listOfNEWLINE(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ListOfNEWLINEContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ListOfNEWLINEContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_r_elif

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitR_elif" ):
                return visitor.visitR_elif(self)
            else:
                return visitor.visitChildren(self)




    def r_elif(self):

        localctx = ZCodeParser.R_elifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_r_elif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEWLINE]:
                self.state = 170
                self.listOfNEWLINE()
                pass
            elif token in [ZCodeParser.ELIF]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 174
            self.match(ZCodeParser.ELIF)
            self.state = 175
            self.match(ZCodeParser.LP)
            self.state = 176
            self.expr()
            self.state = 177
            self.match(ZCodeParser.RP)
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEWLINE]:
                self.state = 178
                self.listOfNEWLINE()
                pass
            elif token in [ZCodeParser.TYPE, ZCodeParser.IF, ZCodeParser.FOR, ZCodeParser.SUB, ZCodeParser.LP, ZCodeParser.LB, ZCodeParser.BEGIN, ZCodeParser.NOT, ZCodeParser.VAR, ZCodeParser.DYN, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.RETURN, ZCodeParser.FUNC, ZCodeParser.BoolLit, ZCodeParser.NumberLit, ZCodeParser.IDENTIFIER, ZCodeParser.StringLit]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 182
            self.stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class R_elseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def stm(self):
            return self.getTypedRuleContext(ZCodeParser.StmContext,0)


        def listOfNEWLINE(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ListOfNEWLINEContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ListOfNEWLINEContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_r_else

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitR_else" ):
                return visitor.visitR_else(self)
            else:
                return visitor.visitChildren(self)




    def r_else(self):

        localctx = ZCodeParser.R_elseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_r_else)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEWLINE]:
                self.state = 184
                self.listOfNEWLINE()
                pass
            elif token in [ZCodeParser.ELSE]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 188
            self.match(ZCodeParser.ELSE)
            self.state = 191
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEWLINE]:
                self.state = 189
                self.listOfNEWLINE()
                pass
            elif token in [ZCodeParser.TYPE, ZCodeParser.IF, ZCodeParser.FOR, ZCodeParser.SUB, ZCodeParser.LP, ZCodeParser.LB, ZCodeParser.BEGIN, ZCodeParser.NOT, ZCodeParser.VAR, ZCodeParser.DYN, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.RETURN, ZCodeParser.FUNC, ZCodeParser.BoolLit, ZCodeParser.NumberLit, ZCodeParser.IDENTIFIER, ZCodeParser.StringLit]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 193
            self.stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class R_forContext(ParserRuleContext):
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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def stm(self):
            return self.getTypedRuleContext(ZCodeParser.StmContext,0)


        def listOfNEWLINE(self):
            return self.getTypedRuleContext(ZCodeParser.ListOfNEWLINEContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_r_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitR_for" ):
                return visitor.visitR_for(self)
            else:
                return visitor.visitChildren(self)




    def r_for(self):

        localctx = ZCodeParser.R_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_r_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(ZCodeParser.FOR)
            self.state = 196
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 197
            self.match(ZCodeParser.UNTIL)
            self.state = 198
            self.expr()
            self.state = 199
            self.match(ZCodeParser.BY)
            self.state = 200
            self.expr()
            self.state = 203
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEWLINE]:
                self.state = 201
                self.listOfNEWLINE()
                pass
            elif token in [ZCodeParser.TYPE, ZCodeParser.IF, ZCodeParser.FOR, ZCodeParser.SUB, ZCodeParser.LP, ZCodeParser.LB, ZCodeParser.BEGIN, ZCodeParser.NOT, ZCodeParser.VAR, ZCodeParser.DYN, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.RETURN, ZCodeParser.FUNC, ZCodeParser.BoolLit, ZCodeParser.NumberLit, ZCodeParser.IDENTIFIER, ZCodeParser.StringLit]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 205
            self.stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def listOfNEWLINE(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ListOfNEWLINEContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ListOfNEWLINEContext,i)


        def block_stms(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = ZCodeParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(ZCodeParser.BEGIN)
            self.state = 213
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 208
                self.listOfNEWLINE()
                self.state = 209
                self.block_stms()
                self.state = 210
                self.listOfNEWLINE()
                pass

            elif la_ == 2:
                self.state = 212
                self.listOfNEWLINE()
                pass


            self.state = 215
            self.match(ZCodeParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stm(self):
            return self.getTypedRuleContext(ZCodeParser.StmContext,0)


        def listOfNEWLINE(self):
            return self.getTypedRuleContext(ZCodeParser.ListOfNEWLINEContext,0)


        def block_stms(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_block_stms

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stms" ):
                return visitor.visitBlock_stms(self)
            else:
                return visitor.visitChildren(self)




    def block_stms(self):

        localctx = ZCodeParser.Block_stmsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_block_stms)
        try:
            self.state = 222
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self.stm()
                self.state = 219
                self.listOfNEWLINE()
                self.state = 220
                self.block_stms()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def arg_group(self):
            return self.getTypedRuleContext(ZCodeParser.Arg_groupContext,0)


        def listOfNEWLINE(self):
            return self.getTypedRuleContext(ZCodeParser.ListOfNEWLINEContext,0)


        def r_return(self):
            return self.getTypedRuleContext(ZCodeParser.R_returnContext,0)


        def block(self):
            return self.getTypedRuleContext(ZCodeParser.BlockContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc" ):
                return visitor.visitFunc(self)
            else:
                return visitor.visitChildren(self)




    def func(self):

        localctx = ZCodeParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(ZCodeParser.FUNC)
            self.state = 225
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 226
            self.arg_group()
            self.state = 236
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 229
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.NEWLINE]:
                    self.state = 227
                    self.listOfNEWLINE()
                    pass
                elif token in [ZCodeParser.BEGIN, ZCodeParser.RETURN]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 233
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.RETURN]:
                    self.state = 231
                    self.r_return()
                    pass
                elif token in [ZCodeParser.BEGIN]:
                    self.state = 232
                    self.block()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arg_groupContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def args(self):
            return self.getTypedRuleContext(ZCodeParser.ArgsContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arg_group

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg_group" ):
                return visitor.visitArg_group(self)
            else:
                return visitor.visitChildren(self)




    def arg_group(self):

        localctx = ZCodeParser.Arg_groupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_arg_group)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(ZCodeParser.LP)
            self.state = 239
            self.args()
            self.state = 240
            self.match(ZCodeParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arg_list(self):
            return self.getTypedRuleContext(ZCodeParser.Arg_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_args

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)




    def args(self):

        localctx = ZCodeParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_args)
        try:
            self.state = 244
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                self.arg_list()
                pass
            elif token in [ZCodeParser.RP]:
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


    class Arg_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arg(self):
            return self.getTypedRuleContext(ZCodeParser.ArgContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def arg_list(self):
            return self.getTypedRuleContext(ZCodeParser.Arg_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arg_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg_list" ):
                return visitor.visitArg_list(self)
            else:
                return visitor.visitChildren(self)




    def arg_list(self):

        localctx = ZCodeParser.Arg_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_arg_list)
        try:
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.arg()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.arg()
                self.state = 248
                self.match(ZCodeParser.COMMA)
                self.state = 249
                self.arg_list()
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

        def TYPE(self):
            return self.getToken(ZCodeParser.TYPE, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def type_index(self):
            return self.getTypedRuleContext(ZCodeParser.Type_indexContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arg

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg" ):
                return visitor.visitArg(self)
            else:
                return visitor.visitChildren(self)




    def arg(self):

        localctx = ZCodeParser.ArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(ZCodeParser.TYPE)
            self.state = 254
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 257
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LB]:
                self.state = 255
                self.type_index()
                pass
            elif token in [ZCodeParser.RP, ZCodeParser.COMMA]:
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


    class Type_indexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def type_index_nums(self):
            return self.getTypedRuleContext(ZCodeParser.Type_index_numsContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_type_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_index" ):
                return visitor.visitType_index(self)
            else:
                return visitor.visitChildren(self)




    def type_index(self):

        localctx = ZCodeParser.Type_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_type_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(ZCodeParser.LB)
            self.state = 260
            self.type_index_nums()
            self.state = 261
            self.match(ZCodeParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_index_numsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_index_num_list(self):
            return self.getTypedRuleContext(ZCodeParser.Type_index_num_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_type_index_nums

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_index_nums" ):
                return visitor.visitType_index_nums(self)
            else:
                return visitor.visitChildren(self)




    def type_index_nums(self):

        localctx = ZCodeParser.Type_index_numsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_type_index_nums)
        try:
            self.state = 265
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NumberLit]:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.type_index_num_list()
                pass
            elif token in [ZCodeParser.RB]:
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


    class Type_index_num_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NumberLit(self):
            return self.getToken(ZCodeParser.NumberLit, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def type_index_num_list(self):
            return self.getTypedRuleContext(ZCodeParser.Type_index_num_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_type_index_num_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_index_num_list" ):
                return visitor.visitType_index_num_list(self)
            else:
                return visitor.visitChildren(self)




    def type_index_num_list(self):

        localctx = ZCodeParser.Type_index_num_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_type_index_num_list)
        try:
            self.state = 271
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.match(ZCodeParser.NumberLit)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
                self.match(ZCodeParser.NumberLit)
                self.state = 269
                self.match(ZCodeParser.COMMA)
                self.state = 270
                self.type_index_num_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_ass

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAss" ):
                return visitor.visitAss(self)
            else:
                return visitor.visitChildren(self)




    def ass(self):

        localctx = ZCodeParser.AssContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_ass)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.expr()
            self.state = 274
            self.match(ZCodeParser.ASSIGN)
            self.state = 275
            self.expr()
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

        def TYPE(self):
            return self.getToken(ZCodeParser.TYPE, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def type_index(self):
            return self.getTypedRuleContext(ZCodeParser.Type_indexContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def DYN(self):
            return self.getToken(ZCodeParser.DYN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_decl)
        try:
            self.state = 299
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 277
                self.match(ZCodeParser.TYPE)
                self.state = 278
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 281
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.LB]:
                    self.state = 279
                    self.type_index()
                    pass
                elif token in [ZCodeParser.EOF, ZCodeParser.ELIF, ZCodeParser.ELSE, ZCodeParser.ASSIGN, ZCodeParser.NEWLINE]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 286
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.ASSIGN]:
                    self.state = 283
                    self.match(ZCodeParser.ASSIGN)
                    self.state = 284
                    self.expr()
                    pass
                elif token in [ZCodeParser.EOF, ZCodeParser.ELIF, ZCodeParser.ELSE, ZCodeParser.NEWLINE]:
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [ZCodeParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 288
                self.match(ZCodeParser.VAR)
                self.state = 289
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 290
                self.match(ZCodeParser.ASSIGN)
                self.state = 291
                self.expr()
                pass
            elif token in [ZCodeParser.DYN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 292
                self.match(ZCodeParser.DYN)
                self.state = 293
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 297
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.ASSIGN]:
                    self.state = 294
                    self.match(ZCodeParser.ASSIGN)
                    self.state = 295
                    self.expr()
                    pass
                elif token in [ZCodeParser.EOF, ZCodeParser.ELIF, ZCodeParser.ELSE, ZCodeParser.NEWLINE]:
                    pass
                else:
                    raise NoViableAltException(self)

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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr1Context,i)


        def CONCAT(self):
            return self.getToken(ZCodeParser.CONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ZCodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_expr)
        try:
            self.state = 306
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 301
                self.expr1()
                self.state = 302
                localctx.op = self.match(ZCodeParser.CONCAT)
                self.state = 303
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 305
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr2Context,i)


        def EQ(self):
            return self.getToken(ZCodeParser.EQ, 0)

        def DEQ(self):
            return self.getToken(ZCodeParser.DEQ, 0)

        def NEQ(self):
            return self.getToken(ZCodeParser.NEQ, 0)

        def LT(self):
            return self.getToken(ZCodeParser.LT, 0)

        def GT(self):
            return self.getToken(ZCodeParser.GT, 0)

        def LE(self):
            return self.getToken(ZCodeParser.LE, 0)

        def GE(self):
            return self.getToken(ZCodeParser.GE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = ZCodeParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 313
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 308
                self.expr2(0)
                self.state = 309
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQ) | (1 << ZCodeParser.DEQ) | (1 << ZCodeParser.GE) | (1 << ZCodeParser.GT) | (1 << ZCodeParser.LE) | (1 << ZCodeParser.LT) | (1 << ZCodeParser.NEQ))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 310
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 312
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(ZCodeParser.Expr2Context,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 323
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 318
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 319
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 320
                    self.expr3(0) 
                self.state = 325
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 334
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 329
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 330
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.SUB or _la==ZCodeParser.ADD):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 331
                    self.expr4(0) 
                self.state = 336
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def MUL(self):
            return self.getToken(ZCodeParser.MUL, 0)

        def DIV(self):
            return self.getToken(ZCodeParser.DIV, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 345
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 340
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 341
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 342
                    self.expr5() 
                self.state = 347
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = ZCodeParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_expr5)
        try:
            self.state = 353
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 348
                self.match(ZCodeParser.SUB)
                self.state = 349
                self.expr5()
                pass
            elif token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 350
                self.match(ZCodeParser.NOT)
                self.state = 351
                self.expr5()
                pass
            elif token in [ZCodeParser.LP, ZCodeParser.LB, ZCodeParser.BoolLit, ZCodeParser.NumberLit, ZCodeParser.IDENTIFIER, ZCodeParser.StringLit]:
                self.enterOuterAlt(localctx, 3)
                self.state = 352
                self.expr6(0)
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


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(ZCodeParser.TermContext,0)


        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def expr_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_listContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)



    def expr6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_expr6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self.term()
            self._ctx.stop = self._input.LT(-1)
            self.state = 370
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 368
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 358
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 359
                        self.match(ZCodeParser.LB)
                        self.state = 360
                        self.expr_list()
                        self.state = 361
                        self.match(ZCodeParser.RB)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 363
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 364
                        self.match(ZCodeParser.LP)
                        self.state = 365
                        self.expr_list()
                        self.state = 366
                        self.match(ZCodeParser.RP)
                        pass

             
                self.state = 372
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NumberLit(self):
            return self.getToken(ZCodeParser.NumberLit, 0)

        def StringLit(self):
            return self.getToken(ZCodeParser.StringLit, 0)

        def BoolLit(self):
            return self.getToken(ZCodeParser.BoolLit, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def expr_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_listContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_term

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = ZCodeParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_term)
        try:
            self.state = 385
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NumberLit]:
                self.enterOuterAlt(localctx, 1)
                self.state = 373
                self.match(ZCodeParser.NumberLit)
                pass
            elif token in [ZCodeParser.StringLit]:
                self.enterOuterAlt(localctx, 2)
                self.state = 374
                self.match(ZCodeParser.StringLit)
                pass
            elif token in [ZCodeParser.BoolLit]:
                self.enterOuterAlt(localctx, 3)
                self.state = 375
                self.match(ZCodeParser.BoolLit)
                pass
            elif token in [ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 4)
                self.state = 376
                self.match(ZCodeParser.IDENTIFIER)
                pass
            elif token in [ZCodeParser.LB]:
                self.enterOuterAlt(localctx, 5)
                self.state = 377
                self.match(ZCodeParser.LB)
                self.state = 378
                self.expr_list()
                self.state = 379
                self.match(ZCodeParser.RB)
                pass
            elif token in [ZCodeParser.LP]:
                self.enterOuterAlt(localctx, 6)
                self.state = 381
                self.match(ZCodeParser.LP)
                self.state = 382
                self.expr()
                self.state = 383
                self.match(ZCodeParser.RP)
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


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprPrime(self):
            return self.getTypedRuleContext(ZCodeParser.ExprPrimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_list(self):

        localctx = ZCodeParser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_expr_list)
        try:
            self.state = 389
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUB, ZCodeParser.LP, ZCodeParser.LB, ZCodeParser.NOT, ZCodeParser.BoolLit, ZCodeParser.NumberLit, ZCodeParser.IDENTIFIER, ZCodeParser.StringLit]:
                self.enterOuterAlt(localctx, 1)
                self.state = 387
                self.exprPrime()
                pass
            elif token in [ZCodeParser.RP, ZCodeParser.RB]:
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


    class ExprPrimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def exprPrime(self):
            return self.getTypedRuleContext(ZCodeParser.ExprPrimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exprPrime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprPrime" ):
                return visitor.visitExprPrime(self)
            else:
                return visitor.visitChildren(self)




    def exprPrime(self):

        localctx = ZCodeParser.ExprPrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_exprPrime)
        try:
            self.state = 396
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 391
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 392
                self.expr()
                self.state = 393
                self.match(ZCodeParser.COMMA)
                self.state = 394
                self.exprPrime()
                pass


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
        self.enterRule(localctx, 68, self.RULE_listOfNEWLINE)
        try:
            self.state = 401
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 398
                self.match(ZCodeParser.NEWLINE)
                self.state = 399
                self.listOfNEWLINE()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 400
                self.match(ZCodeParser.NEWLINE)
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
        self._predicates[26] = self.expr2_sempred
        self._predicates[27] = self.expr3_sempred
        self._predicates[28] = self.expr4_sempred
        self._predicates[30] = self.expr6_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr6_sempred(self, localctx:Expr6Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




