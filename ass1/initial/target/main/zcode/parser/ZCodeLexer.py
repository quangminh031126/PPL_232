# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\65")
        buf.write("\u0196\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\3\2\3\2\5\2~\n\2\3\3\3\3\5\3\u0082")
        buf.write("\n\3\3\3\3\3\3\4\6\4\u0087\n\4\r\4\16\4\u0088\3\5\3\5")
        buf.write("\3\5\5\5\u008e\n\5\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\t")
        buf.write("\3\t\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3")
        buf.write("$\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3+\3")
        buf.write("+\3,\3,\3,\3-\3-\3-\3.\3.\3.\3.\3/\3/\3\60\3\60\3\61\3")
        buf.write("\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\65\5\65")
        buf.write("\u0142\n\65\3\65\5\65\u0145\n\65\3\66\3\66\7\66\u0149")
        buf.write("\n\66\f\66\16\66\u014c\13\66\3\66\3\66\3\66\3\67\3\67")
        buf.write("\5\67\u0153\n\67\38\38\58\u0157\n8\38\38\38\78\u015c\n")
        buf.write("8\f8\168\u015f\138\39\39\39\39\79\u0165\n9\f9\169\u0168")
        buf.write("\139\39\79\u016b\n9\f9\169\u016e\139\39\39\3:\6:\u0173")
        buf.write("\n:\r:\16:\u0174\3:\3:\3;\3;\3;\3<\3<\7<\u017e\n<\f<\16")
        buf.write("<\u0181\13<\3<\3<\5<\u0185\n<\3<\3<\3=\3=\7=\u018b\n=")
        buf.write("\f=\16=\u018e\13=\3=\3=\3=\5=\u0193\n=\3=\3=\3\u0166\2")
        buf.write(">\3\2\5\2\7\2\t\2\13\2\r\2\17\2\21\2\23\2\25\3\27\4\31")
        buf.write("\5\33\6\35\7\37\b!\t#\n%\13\'\f)\r+\16-\17/\20\61\21\63")
        buf.write("\22\65\23\67\249\25;\26=\27?\30A\31C\32E\33G\34I\35K\36")
        buf.write("M\37O Q!S\"U#W$Y%[&]\'_(a)c*e+g,i-k.m/o\60q\61s\62u\63")
        buf.write("w\64y\65\3\2\13\4\2GGgg\4\2--//\6\2\f\f\17\17$$^^\t\2")
        buf.write("))^^ddhhppttvv\4\2C\\c|\3\2\62;\4\2\f\f\16\17\5\2\13\13")
        buf.write("\16\17\"\"\3\2^^\2\u01a1\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3")
        buf.write("\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G")
        buf.write("\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2")
        buf.write("Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2")
        buf.write("\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2")
        buf.write("\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2")
        buf.write("\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3")
        buf.write("\2\2\2\2y\3\2\2\2\3{\3\2\2\2\5\177\3\2\2\2\7\u0086\3\2")
        buf.write("\2\2\t\u008d\3\2\2\2\13\u008f\3\2\2\2\r\u0092\3\2\2\2")
        buf.write("\17\u0095\3\2\2\2\21\u0097\3\2\2\2\23\u0099\3\2\2\2\25")
        buf.write("\u009b\3\2\2\2\27\u00a0\3\2\2\2\31\u00a6\3\2\2\2\33\u00ad")
        buf.write("\3\2\2\2\35\u00b2\3\2\2\2\37\u00b9\3\2\2\2!\u00c0\3\2")
        buf.write("\2\2#\u00c4\3\2\2\2%\u00cc\3\2\2\2\'\u00d1\3\2\2\2)\u00d5")
        buf.write("\3\2\2\2+\u00db\3\2\2\2-\u00de\3\2\2\2/\u00e4\3\2\2\2")
        buf.write("\61\u00ed\3\2\2\2\63\u00f0\3\2\2\2\65\u00f5\3\2\2\2\67")
        buf.write("\u00fa\3\2\2\29\u0100\3\2\2\2;\u0104\3\2\2\2=\u0108\3")
        buf.write("\2\2\2?\u010c\3\2\2\2A\u010f\3\2\2\2C\u0111\3\2\2\2E\u0113")
        buf.write("\3\2\2\2G\u0115\3\2\2\2I\u0117\3\2\2\2K\u0119\3\2\2\2")
        buf.write("M\u011b\3\2\2\2O\u011e\3\2\2\2Q\u0121\3\2\2\2S\u0124\3")
        buf.write("\2\2\2U\u0126\3\2\2\2W\u0128\3\2\2\2Y\u012b\3\2\2\2[\u012e")
        buf.write("\3\2\2\2]\u0132\3\2\2\2_\u0134\3\2\2\2a\u0136\3\2\2\2")
        buf.write("c\u0138\3\2\2\2e\u013a\3\2\2\2g\u013c\3\2\2\2i\u013e\3")
        buf.write("\2\2\2k\u0146\3\2\2\2m\u0152\3\2\2\2o\u0156\3\2\2\2q\u0160")
        buf.write("\3\2\2\2s\u0172\3\2\2\2u\u0178\3\2\2\2w\u017b\3\2\2\2")
        buf.write("y\u0188\3\2\2\2{}\7\60\2\2|~\5\7\4\2}|\3\2\2\2}~\3\2\2")
        buf.write("\2~\4\3\2\2\2\177\u0081\t\2\2\2\u0080\u0082\t\3\2\2\u0081")
        buf.write("\u0080\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0083\3\2\2\2")
        buf.write("\u0083\u0084\5\7\4\2\u0084\6\3\2\2\2\u0085\u0087\5\23")
        buf.write("\n\2\u0086\u0085\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u0086")
        buf.write("\3\2\2\2\u0088\u0089\3\2\2\2\u0089\b\3\2\2\2\u008a\u008e")
        buf.write("\n\4\2\2\u008b\u008e\5\r\7\2\u008c\u008e\5\13\6\2\u008d")
        buf.write("\u008a\3\2\2\2\u008d\u008b\3\2\2\2\u008d\u008c\3\2\2\2")
        buf.write("\u008e\n\3\2\2\2\u008f\u0090\7)\2\2\u0090\u0091\7$\2\2")
        buf.write("\u0091\f\3\2\2\2\u0092\u0093\7^\2\2\u0093\u0094\t\5\2")
        buf.write("\2\u0094\16\3\2\2\2\u0095\u0096\t\6\2\2\u0096\20\3\2\2")
        buf.write("\2\u0097\u0098\7a\2\2\u0098\22\3\2\2\2\u0099\u009a\t\7")
        buf.write("\2\2\u009a\24\3\2\2\2\u009b\u009c\7v\2\2\u009c\u009d\7")
        buf.write("t\2\2\u009d\u009e\7w\2\2\u009e\u009f\7g\2\2\u009f\26\3")
        buf.write("\2\2\2\u00a0\u00a1\7h\2\2\u00a1\u00a2\7c\2\2\u00a2\u00a3")
        buf.write("\7n\2\2\u00a3\u00a4\7u\2\2\u00a4\u00a5\7g\2\2\u00a5\30")
        buf.write("\3\2\2\2\u00a6\u00a7\7p\2\2\u00a7\u00a8\7w\2\2\u00a8\u00a9")
        buf.write("\7o\2\2\u00a9\u00aa\7d\2\2\u00aa\u00ab\7g\2\2\u00ab\u00ac")
        buf.write("\7t\2\2\u00ac\32\3\2\2\2\u00ad\u00ae\7d\2\2\u00ae\u00af")
        buf.write("\7q\2\2\u00af\u00b0\7q\2\2\u00b0\u00b1\7n\2\2\u00b1\34")
        buf.write("\3\2\2\2\u00b2\u00b3\7u\2\2\u00b3\u00b4\7v\2\2\u00b4\u00b5")
        buf.write("\7t\2\2\u00b5\u00b6\7k\2\2\u00b6\u00b7\7p\2\2\u00b7\u00b8")
        buf.write("\7i\2\2\u00b8\36\3\2\2\2\u00b9\u00ba\7t\2\2\u00ba\u00bb")
        buf.write("\7g\2\2\u00bb\u00bc\7v\2\2\u00bc\u00bd\7w\2\2\u00bd\u00be")
        buf.write("\7t\2\2\u00be\u00bf\7p\2\2\u00bf \3\2\2\2\u00c0\u00c1")
        buf.write("\7x\2\2\u00c1\u00c2\7c\2\2\u00c2\u00c3\7t\2\2\u00c3\"")
        buf.write("\3\2\2\2\u00c4\u00c5\7f\2\2\u00c5\u00c6\7{\2\2\u00c6\u00c7")
        buf.write("\7p\2\2\u00c7\u00c8\7c\2\2\u00c8\u00c9\7o\2\2\u00c9\u00ca")
        buf.write("\7k\2\2\u00ca\u00cb\7e\2\2\u00cb$\3\2\2\2\u00cc\u00cd")
        buf.write("\7h\2\2\u00cd\u00ce\7w\2\2\u00ce\u00cf\7p\2\2\u00cf\u00d0")
        buf.write("\7e\2\2\u00d0&\3\2\2\2\u00d1\u00d2\7h\2\2\u00d2\u00d3")
        buf.write("\7q\2\2\u00d3\u00d4\7t\2\2\u00d4(\3\2\2\2\u00d5\u00d6")
        buf.write("\7w\2\2\u00d6\u00d7\7p\2\2\u00d7\u00d8\7v\2\2\u00d8\u00d9")
        buf.write("\7k\2\2\u00d9\u00da\7n\2\2\u00da*\3\2\2\2\u00db\u00dc")
        buf.write("\7d\2\2\u00dc\u00dd\7{\2\2\u00dd,\3\2\2\2\u00de\u00df")
        buf.write("\7d\2\2\u00df\u00e0\7t\2\2\u00e0\u00e1\7g\2\2\u00e1\u00e2")
        buf.write("\7c\2\2\u00e2\u00e3\7m\2\2\u00e3.\3\2\2\2\u00e4\u00e5")
        buf.write("\7e\2\2\u00e5\u00e6\7q\2\2\u00e6\u00e7\7p\2\2\u00e7\u00e8")
        buf.write("\7v\2\2\u00e8\u00e9\7k\2\2\u00e9\u00ea\7p\2\2\u00ea\u00eb")
        buf.write("\7w\2\2\u00eb\u00ec\7g\2\2\u00ec\60\3\2\2\2\u00ed\u00ee")
        buf.write("\7k\2\2\u00ee\u00ef\7h\2\2\u00ef\62\3\2\2\2\u00f0\u00f1")
        buf.write("\7g\2\2\u00f1\u00f2\7n\2\2\u00f2\u00f3\7u\2\2\u00f3\u00f4")
        buf.write("\7g\2\2\u00f4\64\3\2\2\2\u00f5\u00f6\7g\2\2\u00f6\u00f7")
        buf.write("\7n\2\2\u00f7\u00f8\7k\2\2\u00f8\u00f9\7h\2\2\u00f9\66")
        buf.write("\3\2\2\2\u00fa\u00fb\7d\2\2\u00fb\u00fc\7g\2\2\u00fc\u00fd")
        buf.write("\7i\2\2\u00fd\u00fe\7k\2\2\u00fe\u00ff\7p\2\2\u00ff8\3")
        buf.write("\2\2\2\u0100\u0101\7g\2\2\u0101\u0102\7p\2\2\u0102\u0103")
        buf.write("\7f\2\2\u0103:\3\2\2\2\u0104\u0105\7p\2\2\u0105\u0106")
        buf.write("\7q\2\2\u0106\u0107\7v\2\2\u0107<\3\2\2\2\u0108\u0109")
        buf.write("\7c\2\2\u0109\u010a\7p\2\2\u010a\u010b\7f\2\2\u010b>\3")
        buf.write("\2\2\2\u010c\u010d\7q\2\2\u010d\u010e\7t\2\2\u010e@\3")
        buf.write("\2\2\2\u010f\u0110\7-\2\2\u0110B\3\2\2\2\u0111\u0112\7")
        buf.write("/\2\2\u0112D\3\2\2\2\u0113\u0114\7,\2\2\u0114F\3\2\2\2")
        buf.write("\u0115\u0116\7\61\2\2\u0116H\3\2\2\2\u0117\u0118\7\'\2")
        buf.write("\2\u0118J\3\2\2\2\u0119\u011a\7?\2\2\u011aL\3\2\2\2\u011b")
        buf.write("\u011c\7>\2\2\u011c\u011d\7/\2\2\u011dN\3\2\2\2\u011e")
        buf.write("\u011f\7?\2\2\u011f\u0120\7?\2\2\u0120P\3\2\2\2\u0121")
        buf.write("\u0122\7#\2\2\u0122\u0123\7?\2\2\u0123R\3\2\2\2\u0124")
        buf.write("\u0125\7>\2\2\u0125T\3\2\2\2\u0126\u0127\7@\2\2\u0127")
        buf.write("V\3\2\2\2\u0128\u0129\7>\2\2\u0129\u012a\7?\2\2\u012a")
        buf.write("X\3\2\2\2\u012b\u012c\7@\2\2\u012c\u012d\7?\2\2\u012d")
        buf.write("Z\3\2\2\2\u012e\u012f\7\60\2\2\u012f\u0130\7\60\2\2\u0130")
        buf.write("\u0131\7\60\2\2\u0131\\\3\2\2\2\u0132\u0133\7*\2\2\u0133")
        buf.write("^\3\2\2\2\u0134\u0135\7+\2\2\u0135`\3\2\2\2\u0136\u0137")
        buf.write("\7]\2\2\u0137b\3\2\2\2\u0138\u0139\7_\2\2\u0139d\3\2\2")
        buf.write("\2\u013a\u013b\7.\2\2\u013bf\3\2\2\2\u013c\u013d\7\f\2")
        buf.write("\2\u013dh\3\2\2\2\u013e\u0144\5\7\4\2\u013f\u0145\5\3")
        buf.write("\2\2\u0140\u0142\5\3\2\2\u0141\u0140\3\2\2\2\u0141\u0142")
        buf.write("\3\2\2\2\u0142\u0143\3\2\2\2\u0143\u0145\5\5\3\2\u0144")
        buf.write("\u013f\3\2\2\2\u0144\u0141\3\2\2\2\u0144\u0145\3\2\2\2")
        buf.write("\u0145j\3\2\2\2\u0146\u014a\7$\2\2\u0147\u0149\5\t\5\2")
        buf.write("\u0148\u0147\3\2\2\2\u0149\u014c\3\2\2\2\u014a\u0148\3")
        buf.write("\2\2\2\u014a\u014b\3\2\2\2\u014b\u014d\3\2\2\2\u014c\u014a")
        buf.write("\3\2\2\2\u014d\u014e\7$\2\2\u014e\u014f\b\66\2\2\u014f")
        buf.write("l\3\2\2\2\u0150\u0153\5\25\13\2\u0151\u0153\5\27\f\2\u0152")
        buf.write("\u0150\3\2\2\2\u0152\u0151\3\2\2\2\u0153n\3\2\2\2\u0154")
        buf.write("\u0157\5\17\b\2\u0155\u0157\5\21\t\2\u0156\u0154\3\2\2")
        buf.write("\2\u0156\u0155\3\2\2\2\u0157\u015d\3\2\2\2\u0158\u015c")
        buf.write("\5\17\b\2\u0159\u015c\5\21\t\2\u015a\u015c\5\23\n\2\u015b")
        buf.write("\u0158\3\2\2\2\u015b\u0159\3\2\2\2\u015b\u015a\3\2\2\2")
        buf.write("\u015c\u015f\3\2\2\2\u015d\u015b\3\2\2\2\u015d\u015e\3")
        buf.write("\2\2\2\u015ep\3\2\2\2\u015f\u015d\3\2\2\2\u0160\u0161")
        buf.write("\7%\2\2\u0161\u0162\7%\2\2\u0162\u0166\3\2\2\2\u0163\u0165")
        buf.write("\13\2\2\2\u0164\u0163\3\2\2\2\u0165\u0168\3\2\2\2\u0166")
        buf.write("\u0167\3\2\2\2\u0166\u0164\3\2\2\2\u0167\u016c\3\2\2\2")
        buf.write("\u0168\u0166\3\2\2\2\u0169\u016b\n\b\2\2\u016a\u0169\3")
        buf.write("\2\2\2\u016b\u016e\3\2\2\2\u016c\u016a\3\2\2\2\u016c\u016d")
        buf.write("\3\2\2\2\u016d\u016f\3\2\2\2\u016e\u016c\3\2\2\2\u016f")
        buf.write("\u0170\b9\3\2\u0170r\3\2\2\2\u0171\u0173\t\t\2\2\u0172")
        buf.write("\u0171\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u0172\3\2\2\2")
        buf.write("\u0174\u0175\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u0177\b")
        buf.write(":\3\2\u0177t\3\2\2\2\u0178\u0179\13\2\2\2\u0179\u017a")
        buf.write("\b;\4\2\u017av\3\2\2\2\u017b\u017f\7$\2\2\u017c\u017e")
        buf.write("\5\t\5\2\u017d\u017c\3\2\2\2\u017e\u0181\3\2\2\2\u017f")
        buf.write("\u017d\3\2\2\2\u017f\u0180\3\2\2\2\u0180\u0184\3\2\2\2")
        buf.write("\u0181\u017f\3\2\2\2\u0182\u0185\5g\64\2\u0183\u0185\7")
        buf.write("\2\2\3\u0184\u0182\3\2\2\2\u0184\u0183\3\2\2\2\u0185\u0186")
        buf.write("\3\2\2\2\u0186\u0187\b<\5\2\u0187x\3\2\2\2\u0188\u018c")
        buf.write("\7$\2\2\u0189\u018b\5\t\5\2\u018a\u0189\3\2\2\2\u018b")
        buf.write("\u018e\3\2\2\2\u018c\u018a\3\2\2\2\u018c\u018d\3\2\2\2")
        buf.write("\u018d\u018f\3\2\2\2\u018e\u018c\3\2\2\2\u018f\u0192\7")
        buf.write("^\2\2\u0190\u0193\n\5\2\2\u0191\u0193\n\n\2\2\u0192\u0190")
        buf.write("\3\2\2\2\u0192\u0191\3\2\2\2\u0193\u0194\3\2\2\2\u0194")
        buf.write("\u0195\b=\6\2\u0195z\3\2\2\2\25\2}\u0081\u0088\u008d\u0141")
        buf.write("\u0144\u014a\u0152\u0156\u015b\u015d\u0166\u016c\u0174")
        buf.write("\u017f\u0184\u018c\u0192\7\3\66\2\b\2\2\3;\3\3<\4\3=\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TRUE = 1
    FALSE = 2
    NUMBER = 3
    BOOL = 4
    STRING = 5
    RETURN = 6
    VAR = 7
    DYNAMIC = 8
    FUNC = 9
    FOR = 10
    UNTIL = 11
    BY = 12
    BREAK = 13
    CONTINUE = 14
    IF = 15
    ELSE = 16
    ELIF = 17
    BEGIN = 18
    END = 19
    NOT = 20
    AND = 21
    OR = 22
    PLUS = 23
    MINUS = 24
    MULT = 25
    DIV = 26
    MOD = 27
    EQUAL = 28
    LEFTARR = 29
    EQUALEQUAL = 30
    NOTEQUAL = 31
    LESS = 32
    GREATER = 33
    LESSOREQUAL = 34
    GREATEROREQUAL = 35
    ELLIPSIS = 36
    LBracket = 37
    RBracket = 38
    LSBracket = 39
    RSBracket = 40
    COMMA = 41
    NEWLINE = 42
    NumberLit = 43
    StringLit = 44
    BoolLit = 45
    IDENTIFIER = 46
    COMMENT = 47
    WS = 48
    ERROR_CHAR = 49
    UNCLOSE_STRING = 50
    ILLEGAL_ESCAPE = 51

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'number'", "'bool'", "'string'", "'return'", 
            "'var'", "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
            "'break'", "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
            "'end'", "'not'", "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'='", "'<-'", "'=='", "'!='", "'<'", "'>'", "'<='", 
            "'>='", "'...'", "'('", "')'", "'['", "']'", "','", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", "VAR", 
            "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
            "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "PLUS", 
            "MINUS", "MULT", "DIV", "MOD", "EQUAL", "LEFTARR", "EQUALEQUAL", 
            "NOTEQUAL", "LESS", "GREATER", "LESSOREQUAL", "GREATEROREQUAL", 
            "ELLIPSIS", "LBracket", "RBracket", "LSBracket", "RSBracket", 
            "COMMA", "NEWLINE", "NumberLit", "StringLit", "BoolLit", "IDENTIFIER", 
            "COMMENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "DECIMAL", "EXPONENT", "INTEGER", "StringChar", "DoubleQuote", 
                  "EscapedSequence", "LETTER", "UNDERSCORE", "DIGIT", "TRUE", 
                  "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", "VAR", 
                  "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
                  "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", 
                  "PLUS", "MINUS", "MULT", "DIV", "MOD", "EQUAL", "LEFTARR", 
                  "EQUALEQUAL", "NOTEQUAL", "LESS", "GREATER", "LESSOREQUAL", 
                  "GREATEROREQUAL", "ELLIPSIS", "LBracket", "RBracket", 
                  "LSBracket", "RSBracket", "COMMA", "NEWLINE", "NumberLit", 
                  "StringLit", "BoolLit", "IDENTIFIER", "COMMENT", "WS", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[52] = self.StringLit_action 
            actions[57] = self.ERROR_CHAR_action 
            actions[58] = self.UNCLOSE_STRING_action 
            actions[59] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def StringLit_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
                    
                temp = self.text
                temp = temp[1:-1]  # Remove the opening and closing quotes
                self.text = temp

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                esc = ['\n']
                temp = str(self.text)
                if (temp[-1] in esc):
                    raise UncloseString(temp[1:-1])
                else:
                    raise UncloseString(temp[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                temp = self.text
                raise IllegalEscape(temp[1:])

     


