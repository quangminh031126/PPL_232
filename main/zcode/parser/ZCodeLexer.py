# Generated from ./main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\64")
        buf.write("\u0195\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\3\2\3\2\3\2\3\2\3\2\3\3\3\3\7\3\u0081\n\3")
        buf.write("\f\3\16\3\u0084\13\3\3\4\3\4\5\4\u0088\n\4\3\4\3\4\3\5")
        buf.write("\6\5\u008d\n\5\r\5\16\5\u008e\3\6\3\6\3\6\5\6\u0094\n")
        buf.write("\6\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3")
        buf.write("%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3+\3+\3")
        buf.write("+\3,\3,\3,\3-\3-\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61")
        buf.write("\3\62\3\62\3\63\3\63\3\64\3\64\3\64\5\64\u013d\n\64\3")
        buf.write("\64\5\64\u0140\n\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\5\65\u014b\n\65\3\66\3\66\7\66\u014f\n\66\f")
        buf.write("\66\16\66\u0152\13\66\3\66\3\66\3\66\3\67\3\67\5\67\u0159")
        buf.write("\n\67\3\67\3\67\3\67\7\67\u015e\n\67\f\67\16\67\u0161")
        buf.write("\13\67\38\38\38\38\78\u0167\n8\f8\168\u016a\138\38\58")
        buf.write("\u016d\n8\38\38\39\69\u0172\n9\r9\169\u0173\39\39\3:\3")
        buf.write(":\3:\3;\3;\7;\u017d\n;\f;\16;\u0180\13;\3;\3;\5;\u0184")
        buf.write("\n;\3;\3;\3<\3<\7<\u018a\n<\f<\16<\u018d\13<\3<\3<\3<")
        buf.write("\5<\u0192\n<\3<\3<\3\u0168\2=\3\3\5\2\7\2\t\2\13\2\r\2")
        buf.write("\17\2\21\2\23\2\25\2\27\4\31\5\33\6\35\7\37\b!\t#\n%\13")
        buf.write("\'\f)\r+\16-\17/\20\61\21\63\22\65\23\67\249\25;\26=\27")
        buf.write("?\30A\31C\32E\33G\34I\35K\36M\37O Q!S\"U#W$Y%[&]\'_(a")
        buf.write(")c*e+g,i-k.m/o\60q\61s\62u\63w\64\3\2\13\4\2GGgg\4\2-")
        buf.write("-//\6\2\f\f\17\17$$^^\t\2))^^ddhhppttvv\4\2C\\c|\3\2\62")
        buf.write(";\3\3\f\f\5\2\13\f\17\17\"\"\3\2^^\2\u019f\2\3\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2")
        buf.write("\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3")
        buf.write("\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2")
        buf.write("\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2")
        buf.write("\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3")
        buf.write("\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W")
        buf.write("\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2")
        buf.write("a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2")
        buf.write("\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2")
        buf.write("\2\2u\3\2\2\2\2w\3\2\2\2\3y\3\2\2\2\5~\3\2\2\2\7\u0085")
        buf.write("\3\2\2\2\t\u008c\3\2\2\2\13\u0093\3\2\2\2\r\u0095\3\2")
        buf.write("\2\2\17\u0098\3\2\2\2\21\u009b\3\2\2\2\23\u009d\3\2\2")
        buf.write("\2\25\u009f\3\2\2\2\27\u00a1\3\2\2\2\31\u00a8\3\2\2\2")
        buf.write("\33\u00ad\3\2\2\2\35\u00b4\3\2\2\2\37\u00bb\3\2\2\2!\u00bf")
        buf.write("\3\2\2\2#\u00c7\3\2\2\2%\u00cc\3\2\2\2\'\u00d0\3\2\2\2")
        buf.write(")\u00d6\3\2\2\2+\u00d9\3\2\2\2-\u00df\3\2\2\2/\u00e8\3")
        buf.write("\2\2\2\61\u00eb\3\2\2\2\63\u00f0\3\2\2\2\65\u00f5\3\2")
        buf.write("\2\2\67\u00fb\3\2\2\29\u00ff\3\2\2\2;\u0103\3\2\2\2=\u0107")
        buf.write("\3\2\2\2?\u010a\3\2\2\2A\u010c\3\2\2\2C\u010e\3\2\2\2")
        buf.write("E\u0110\3\2\2\2G\u0112\3\2\2\2I\u0114\3\2\2\2K\u0116\3")
        buf.write("\2\2\2M\u0119\3\2\2\2O\u011c\3\2\2\2Q\u011f\3\2\2\2S\u0121")
        buf.write("\3\2\2\2U\u0123\3\2\2\2W\u0126\3\2\2\2Y\u0129\3\2\2\2")
        buf.write("[\u012d\3\2\2\2]\u012f\3\2\2\2_\u0131\3\2\2\2a\u0133\3")
        buf.write("\2\2\2c\u0135\3\2\2\2e\u0137\3\2\2\2g\u0139\3\2\2\2i\u014a")
        buf.write("\3\2\2\2k\u014c\3\2\2\2m\u0158\3\2\2\2o\u0162\3\2\2\2")
        buf.write("q\u0171\3\2\2\2s\u0177\3\2\2\2u\u017a\3\2\2\2w\u0187\3")
        buf.write("\2\2\2yz\7o\2\2z{\7c\2\2{|\7k\2\2|}\7p\2\2}\4\3\2\2\2")
        buf.write("~\u0082\7\60\2\2\177\u0081\5\t\5\2\u0080\177\3\2\2\2\u0081")
        buf.write("\u0084\3\2\2\2\u0082\u0080\3\2\2\2\u0082\u0083\3\2\2\2")
        buf.write("\u0083\6\3\2\2\2\u0084\u0082\3\2\2\2\u0085\u0087\t\2\2")
        buf.write("\2\u0086\u0088\t\3\2\2\u0087\u0086\3\2\2\2\u0087\u0088")
        buf.write("\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008a\5\t\5\2\u008a")
        buf.write("\b\3\2\2\2\u008b\u008d\5\25\13\2\u008c\u008b\3\2\2\2\u008d")
        buf.write("\u008e\3\2\2\2\u008e\u008c\3\2\2\2\u008e\u008f\3\2\2\2")
        buf.write("\u008f\n\3\2\2\2\u0090\u0094\n\4\2\2\u0091\u0094\5\17")
        buf.write("\b\2\u0092\u0094\5\r\7\2\u0093\u0090\3\2\2\2\u0093\u0091")
        buf.write("\3\2\2\2\u0093\u0092\3\2\2\2\u0094\f\3\2\2\2\u0095\u0096")
        buf.write("\7)\2\2\u0096\u0097\7$\2\2\u0097\16\3\2\2\2\u0098\u0099")
        buf.write("\7^\2\2\u0099\u009a\t\5\2\2\u009a\20\3\2\2\2\u009b\u009c")
        buf.write("\t\6\2\2\u009c\22\3\2\2\2\u009d\u009e\7a\2\2\u009e\24")
        buf.write("\3\2\2\2\u009f\u00a0\t\7\2\2\u00a0\26\3\2\2\2\u00a1\u00a2")
        buf.write("\7p\2\2\u00a2\u00a3\7w\2\2\u00a3\u00a4\7o\2\2\u00a4\u00a5")
        buf.write("\7d\2\2\u00a5\u00a6\7g\2\2\u00a6\u00a7\7t\2\2\u00a7\30")
        buf.write("\3\2\2\2\u00a8\u00a9\7d\2\2\u00a9\u00aa\7q\2\2\u00aa\u00ab")
        buf.write("\7q\2\2\u00ab\u00ac\7n\2\2\u00ac\32\3\2\2\2\u00ad\u00ae")
        buf.write("\7u\2\2\u00ae\u00af\7v\2\2\u00af\u00b0\7t\2\2\u00b0\u00b1")
        buf.write("\7k\2\2\u00b1\u00b2\7p\2\2\u00b2\u00b3\7i\2\2\u00b3\34")
        buf.write("\3\2\2\2\u00b4\u00b5\7t\2\2\u00b5\u00b6\7g\2\2\u00b6\u00b7")
        buf.write("\7v\2\2\u00b7\u00b8\7w\2\2\u00b8\u00b9\7t\2\2\u00b9\u00ba")
        buf.write("\7p\2\2\u00ba\36\3\2\2\2\u00bb\u00bc\7x\2\2\u00bc\u00bd")
        buf.write("\7c\2\2\u00bd\u00be\7t\2\2\u00be \3\2\2\2\u00bf\u00c0")
        buf.write("\7f\2\2\u00c0\u00c1\7{\2\2\u00c1\u00c2\7p\2\2\u00c2\u00c3")
        buf.write("\7c\2\2\u00c3\u00c4\7o\2\2\u00c4\u00c5\7k\2\2\u00c5\u00c6")
        buf.write("\7e\2\2\u00c6\"\3\2\2\2\u00c7\u00c8\7h\2\2\u00c8\u00c9")
        buf.write("\7w\2\2\u00c9\u00ca\7p\2\2\u00ca\u00cb\7e\2\2\u00cb$\3")
        buf.write("\2\2\2\u00cc\u00cd\7h\2\2\u00cd\u00ce\7q\2\2\u00ce\u00cf")
        buf.write("\7t\2\2\u00cf&\3\2\2\2\u00d0\u00d1\7w\2\2\u00d1\u00d2")
        buf.write("\7p\2\2\u00d2\u00d3\7v\2\2\u00d3\u00d4\7k\2\2\u00d4\u00d5")
        buf.write("\7n\2\2\u00d5(\3\2\2\2\u00d6\u00d7\7d\2\2\u00d7\u00d8")
        buf.write("\7{\2\2\u00d8*\3\2\2\2\u00d9\u00da\7d\2\2\u00da\u00db")
        buf.write("\7t\2\2\u00db\u00dc\7g\2\2\u00dc\u00dd\7c\2\2\u00dd\u00de")
        buf.write("\7m\2\2\u00de,\3\2\2\2\u00df\u00e0\7e\2\2\u00e0\u00e1")
        buf.write("\7q\2\2\u00e1\u00e2\7p\2\2\u00e2\u00e3\7v\2\2\u00e3\u00e4")
        buf.write("\7k\2\2\u00e4\u00e5\7p\2\2\u00e5\u00e6\7w\2\2\u00e6\u00e7")
        buf.write("\7g\2\2\u00e7.\3\2\2\2\u00e8\u00e9\7k\2\2\u00e9\u00ea")
        buf.write("\7h\2\2\u00ea\60\3\2\2\2\u00eb\u00ec\7g\2\2\u00ec\u00ed")
        buf.write("\7n\2\2\u00ed\u00ee\7u\2\2\u00ee\u00ef\7g\2\2\u00ef\62")
        buf.write("\3\2\2\2\u00f0\u00f1\7g\2\2\u00f1\u00f2\7n\2\2\u00f2\u00f3")
        buf.write("\7k\2\2\u00f3\u00f4\7h\2\2\u00f4\64\3\2\2\2\u00f5\u00f6")
        buf.write("\7d\2\2\u00f6\u00f7\7g\2\2\u00f7\u00f8\7i\2\2\u00f8\u00f9")
        buf.write("\7k\2\2\u00f9\u00fa\7p\2\2\u00fa\66\3\2\2\2\u00fb\u00fc")
        buf.write("\7g\2\2\u00fc\u00fd\7p\2\2\u00fd\u00fe\7f\2\2\u00fe8\3")
        buf.write("\2\2\2\u00ff\u0100\7p\2\2\u0100\u0101\7q\2\2\u0101\u0102")
        buf.write("\7v\2\2\u0102:\3\2\2\2\u0103\u0104\7c\2\2\u0104\u0105")
        buf.write("\7p\2\2\u0105\u0106\7f\2\2\u0106<\3\2\2\2\u0107\u0108")
        buf.write("\7q\2\2\u0108\u0109\7t\2\2\u0109>\3\2\2\2\u010a\u010b")
        buf.write("\7-\2\2\u010b@\3\2\2\2\u010c\u010d\7/\2\2\u010dB\3\2\2")
        buf.write("\2\u010e\u010f\7,\2\2\u010fD\3\2\2\2\u0110\u0111\7\61")
        buf.write("\2\2\u0111F\3\2\2\2\u0112\u0113\7\'\2\2\u0113H\3\2\2\2")
        buf.write("\u0114\u0115\7?\2\2\u0115J\3\2\2\2\u0116\u0117\7>\2\2")
        buf.write("\u0117\u0118\7/\2\2\u0118L\3\2\2\2\u0119\u011a\7?\2\2")
        buf.write("\u011a\u011b\7?\2\2\u011bN\3\2\2\2\u011c\u011d\7#\2\2")
        buf.write("\u011d\u011e\7?\2\2\u011eP\3\2\2\2\u011f\u0120\7>\2\2")
        buf.write("\u0120R\3\2\2\2\u0121\u0122\7@\2\2\u0122T\3\2\2\2\u0123")
        buf.write("\u0124\7>\2\2\u0124\u0125\7?\2\2\u0125V\3\2\2\2\u0126")
        buf.write("\u0127\7@\2\2\u0127\u0128\7?\2\2\u0128X\3\2\2\2\u0129")
        buf.write("\u012a\7\60\2\2\u012a\u012b\7\60\2\2\u012b\u012c\7\60")
        buf.write("\2\2\u012cZ\3\2\2\2\u012d\u012e\7*\2\2\u012e\\\3\2\2\2")
        buf.write("\u012f\u0130\7+\2\2\u0130^\3\2\2\2\u0131\u0132\7]\2\2")
        buf.write("\u0132`\3\2\2\2\u0133\u0134\7_\2\2\u0134b\3\2\2\2\u0135")
        buf.write("\u0136\7.\2\2\u0136d\3\2\2\2\u0137\u0138\7\f\2\2\u0138")
        buf.write("f\3\2\2\2\u0139\u013f\5\t\5\2\u013a\u0140\5\5\3\2\u013b")
        buf.write("\u013d\5\5\3\2\u013c\u013b\3\2\2\2\u013c\u013d\3\2\2\2")
        buf.write("\u013d\u013e\3\2\2\2\u013e\u0140\5\7\4\2\u013f\u013a\3")
        buf.write("\2\2\2\u013f\u013c\3\2\2\2\u013f\u0140\3\2\2\2\u0140h")
        buf.write("\3\2\2\2\u0141\u0142\7v\2\2\u0142\u0143\7t\2\2\u0143\u0144")
        buf.write("\7w\2\2\u0144\u014b\7g\2\2\u0145\u0146\7h\2\2\u0146\u0147")
        buf.write("\7c\2\2\u0147\u0148\7n\2\2\u0148\u0149\7u\2\2\u0149\u014b")
        buf.write("\7g\2\2\u014a\u0141\3\2\2\2\u014a\u0145\3\2\2\2\u014b")
        buf.write("j\3\2\2\2\u014c\u0150\7$\2\2\u014d\u014f\5\13\6\2\u014e")
        buf.write("\u014d\3\2\2\2\u014f\u0152\3\2\2\2\u0150\u014e\3\2\2\2")
        buf.write("\u0150\u0151\3\2\2\2\u0151\u0153\3\2\2\2\u0152\u0150\3")
        buf.write("\2\2\2\u0153\u0154\7$\2\2\u0154\u0155\b\66\2\2\u0155l")
        buf.write("\3\2\2\2\u0156\u0159\5\21\t\2\u0157\u0159\5\23\n\2\u0158")
        buf.write("\u0156\3\2\2\2\u0158\u0157\3\2\2\2\u0159\u015f\3\2\2\2")
        buf.write("\u015a\u015e\5\21\t\2\u015b\u015e\5\23\n\2\u015c\u015e")
        buf.write("\5\25\13\2\u015d\u015a\3\2\2\2\u015d\u015b\3\2\2\2\u015d")
        buf.write("\u015c\3\2\2\2\u015e\u0161\3\2\2\2\u015f\u015d\3\2\2\2")
        buf.write("\u015f\u0160\3\2\2\2\u0160n\3\2\2\2\u0161\u015f\3\2\2")
        buf.write("\2\u0162\u0163\7%\2\2\u0163\u0164\7%\2\2\u0164\u0168\3")
        buf.write("\2\2\2\u0165\u0167\13\2\2\2\u0166\u0165\3\2\2\2\u0167")
        buf.write("\u016a\3\2\2\2\u0168\u0169\3\2\2\2\u0168\u0166\3\2\2\2")
        buf.write("\u0169\u016c\3\2\2\2\u016a\u0168\3\2\2\2\u016b\u016d\t")
        buf.write("\b\2\2\u016c\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016e\u016f")
        buf.write("\b8\3\2\u016fp\3\2\2\2\u0170\u0172\t\t\2\2\u0171\u0170")
        buf.write("\3\2\2\2\u0172\u0173\3\2\2\2\u0173\u0171\3\2\2\2\u0173")
        buf.write("\u0174\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u0176\b9\3\2")
        buf.write("\u0176r\3\2\2\2\u0177\u0178\13\2\2\2\u0178\u0179\b:\4")
        buf.write("\2\u0179t\3\2\2\2\u017a\u017e\7$\2\2\u017b\u017d\5\13")
        buf.write("\6\2\u017c\u017b\3\2\2\2\u017d\u0180\3\2\2\2\u017e\u017c")
        buf.write("\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0183\3\2\2\2\u0180")
        buf.write("\u017e\3\2\2\2\u0181\u0184\5e\63\2\u0182\u0184\7\2\2\3")
        buf.write("\u0183\u0181\3\2\2\2\u0183\u0182\3\2\2\2\u0184\u0185\3")
        buf.write("\2\2\2\u0185\u0186\b;\5\2\u0186v\3\2\2\2\u0187\u018b\7")
        buf.write("$\2\2\u0188\u018a\5\13\6\2\u0189\u0188\3\2\2\2\u018a\u018d")
        buf.write("\3\2\2\2\u018b\u0189\3\2\2\2\u018b\u018c\3\2\2\2\u018c")
        buf.write("\u018e\3\2\2\2\u018d\u018b\3\2\2\2\u018e\u0191\7^\2\2")
        buf.write("\u018f\u0192\n\5\2\2\u0190\u0192\n\n\2\2\u0191\u018f\3")
        buf.write("\2\2\2\u0191\u0190\3\2\2\2\u0192\u0193\3\2\2\2\u0193\u0194")
        buf.write("\b<\6\2\u0194x\3\2\2\2\25\2\u0082\u0087\u008e\u0093\u013c")
        buf.write("\u013f\u014a\u0150\u0158\u015d\u015f\u0168\u016c\u0173")
        buf.write("\u017e\u0183\u018b\u0191\7\3\66\2\b\2\2\3:\3\3;\4\3<\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    NUMBER = 2
    BOOL = 3
    STRING = 4
    RETURN = 5
    VAR = 6
    DYNAMIC = 7
    FUNC = 8
    FOR = 9
    UNTIL = 10
    BY = 11
    BREAK = 12
    CONTINUE = 13
    IF = 14
    ELSE = 15
    ELIF = 16
    BEGIN = 17
    END = 18
    NOT = 19
    AND = 20
    OR = 21
    PLUS = 22
    MINUS = 23
    MULT = 24
    DIV = 25
    MOD = 26
    EQUAL = 27
    LEFTARR = 28
    EQUALEQUAL = 29
    NOTEQUAL = 30
    LESS = 31
    GREATER = 32
    LESSOREQUAL = 33
    GREATEROREQUAL = 34
    ELLIPSIS = 35
    LBracket = 36
    RBracket = 37
    LSBracket = 38
    RSBracket = 39
    COMMA = 40
    NEWLINE = 41
    NumberLit = 42
    BooleanLit = 43
    StringLit = 44
    IDENTIFIER = 45
    COMMENT = 46
    WS = 47
    ERROR_CHAR = 48
    UNCLOSE_STRING = 49
    ILLEGAL_ESCAPE = 50

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'number'", "'bool'", "'string'", "'return'", "'var'", 
            "'dynamic'", "'func'", "'for'", "'until'", "'by'", "'break'", 
            "'continue'", "'if'", "'else'", "'elif'", "'begin'", "'end'", 
            "'not'", "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", 
            "'='", "'<-'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
            "'...'", "'('", "')'", "'['", "']'", "','", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", "FUNC", 
            "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", 
            "BEGIN", "END", "NOT", "AND", "OR", "PLUS", "MINUS", "MULT", 
            "DIV", "MOD", "EQUAL", "LEFTARR", "EQUALEQUAL", "NOTEQUAL", 
            "LESS", "GREATER", "LESSOREQUAL", "GREATEROREQUAL", "ELLIPSIS", 
            "LBracket", "RBracket", "LSBracket", "RSBracket", "COMMA", "NEWLINE", 
            "NumberLit", "BooleanLit", "StringLit", "IDENTIFIER", "COMMENT", 
            "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "DECIMAL", "EXPONENT", "INTEGER", "StringChar", 
                  "DoubleQuote", "EscapedSequence", "LETTER", "UNDERSCORE", 
                  "DIGIT", "NUMBER", "BOOL", "STRING", "RETURN", "VAR", 
                  "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
                  "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", 
                  "PLUS", "MINUS", "MULT", "DIV", "MOD", "EQUAL", "LEFTARR", 
                  "EQUALEQUAL", "NOTEQUAL", "LESS", "GREATER", "LESSOREQUAL", 
                  "GREATEROREQUAL", "ELLIPSIS", "LBracket", "RBracket", 
                  "LSBracket", "RSBracket", "COMMA", "NEWLINE", "NumberLit", 
                  "BooleanLit", "StringLit", "IDENTIFIER", "COMMENT", "WS", 
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
            actions[56] = self.ERROR_CHAR_action 
            actions[57] = self.UNCLOSE_STRING_action 
            actions[58] = self.ILLEGAL_ESCAPE_action 
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

     


