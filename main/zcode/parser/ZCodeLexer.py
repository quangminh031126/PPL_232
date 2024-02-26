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
        buf.write("\4;\t;\4<\t<\3\2\3\2\5\2|\n\2\3\3\3\3\5\3\u0080\n\3\3")
        buf.write("\3\3\3\3\4\6\4\u0085\n\4\r\4\16\4\u0086\3\5\3\5\3\5\5")
        buf.write("\5\u008c\n\5\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\6\34\u0100\n\34\r\34\16\34\u0101\3\35\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3")
        buf.write("\'\3(\3(\3(\3)\3)\3)\3*\3*\3+\3+\3,\3,\3,\3-\3-\3-\3.")
        buf.write("\3.\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63")
        buf.write("\3\64\3\64\3\65\3\65\3\65\5\65\u0145\n\65\3\65\5\65\u0148")
        buf.write("\n\65\3\66\3\66\7\66\u014c\n\66\f\66\16\66\u014f\13\66")
        buf.write("\3\66\3\66\3\66\3\67\3\67\5\67\u0156\n\67\3\67\3\67\3")
        buf.write("\67\7\67\u015b\n\67\f\67\16\67\u015e\13\67\38\38\38\3")
        buf.write("8\78\u0164\n8\f8\168\u0167\138\38\78\u016a\n8\f8\168\u016d")
        buf.write("\138\38\38\39\69\u0172\n9\r9\169\u0173\39\39\3:\3:\3:")
        buf.write("\3;\3;\7;\u017d\n;\f;\16;\u0180\13;\3;\3;\5;\u0184\n;")
        buf.write("\3;\3;\3<\3<\7<\u018a\n<\f<\16<\u018d\13<\3<\3<\3<\5<")
        buf.write("\u0192\n<\3<\3<\3\u0165\2=\3\2\5\2\7\2\t\2\13\2\r\2\17")
        buf.write("\2\21\2\23\2\25\3\27\4\31\5\33\6\35\7\37\b!\t#\n%\13\'")
        buf.write("\f)\r+\16-\17/\20\61\21\63\22\65\23\67\249\25;\26=\27")
        buf.write("?\30A\31C\32E\33G\34I\35K\36M\37O Q!S\"U#W$Y%[&]\'_(a")
        buf.write(")c*e+g,i-k.m/o\60q\61s\62u\63w\64\3\2\13\4\2GGgg\4\2-")
        buf.write("-//\6\2\f\f\17\17$$^^\t\2))^^ddhhppttvv\4\2C\\c|\3\2\62")
        buf.write(";\4\2\f\f\16\17\5\2\13\13\17\17\"\"\3\2^^\2\u01a0\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i")
        buf.write("\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2")
        buf.write("s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\3y\3\2\2\2\5}\3\2\2\2")
        buf.write("\7\u0084\3\2\2\2\t\u008b\3\2\2\2\13\u008d\3\2\2\2\r\u0090")
        buf.write("\3\2\2\2\17\u0093\3\2\2\2\21\u0095\3\2\2\2\23\u0097\3")
        buf.write("\2\2\2\25\u0099\3\2\2\2\27\u009e\3\2\2\2\31\u00a4\3\2")
        buf.write("\2\2\33\u00ab\3\2\2\2\35\u00b0\3\2\2\2\37\u00b7\3\2\2")
        buf.write("\2!\u00be\3\2\2\2#\u00c2\3\2\2\2%\u00ca\3\2\2\2\'\u00cf")
        buf.write("\3\2\2\2)\u00d3\3\2\2\2+\u00d9\3\2\2\2-\u00dc\3\2\2\2")
        buf.write("/\u00e2\3\2\2\2\61\u00eb\3\2\2\2\63\u00ee\3\2\2\2\65\u00f3")
        buf.write("\3\2\2\2\67\u00f8\3\2\2\29\u0103\3\2\2\2;\u0107\3\2\2")
        buf.write("\2=\u010b\3\2\2\2?\u010f\3\2\2\2A\u0112\3\2\2\2C\u0114")
        buf.write("\3\2\2\2E\u0116\3\2\2\2G\u0118\3\2\2\2I\u011a\3\2\2\2")
        buf.write("K\u011c\3\2\2\2M\u011e\3\2\2\2O\u0121\3\2\2\2Q\u0124\3")
        buf.write("\2\2\2S\u0127\3\2\2\2U\u0129\3\2\2\2W\u012b\3\2\2\2Y\u012e")
        buf.write("\3\2\2\2[\u0131\3\2\2\2]\u0135\3\2\2\2_\u0137\3\2\2\2")
        buf.write("a\u0139\3\2\2\2c\u013b\3\2\2\2e\u013d\3\2\2\2g\u013f\3")
        buf.write("\2\2\2i\u0141\3\2\2\2k\u0149\3\2\2\2m\u0155\3\2\2\2o\u015f")
        buf.write("\3\2\2\2q\u0171\3\2\2\2s\u0177\3\2\2\2u\u017a\3\2\2\2")
        buf.write("w\u0187\3\2\2\2y{\7\60\2\2z|\5\7\4\2{z\3\2\2\2{|\3\2\2")
        buf.write("\2|\4\3\2\2\2}\177\t\2\2\2~\u0080\t\3\2\2\177~\3\2\2\2")
        buf.write("\177\u0080\3\2\2\2\u0080\u0081\3\2\2\2\u0081\u0082\5\7")
        buf.write("\4\2\u0082\6\3\2\2\2\u0083\u0085\5\23\n\2\u0084\u0083")
        buf.write("\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0084\3\2\2\2\u0086")
        buf.write("\u0087\3\2\2\2\u0087\b\3\2\2\2\u0088\u008c\n\4\2\2\u0089")
        buf.write("\u008c\5\r\7\2\u008a\u008c\5\13\6\2\u008b\u0088\3\2\2")
        buf.write("\2\u008b\u0089\3\2\2\2\u008b\u008a\3\2\2\2\u008c\n\3\2")
        buf.write("\2\2\u008d\u008e\7)\2\2\u008e\u008f\7$\2\2\u008f\f\3\2")
        buf.write("\2\2\u0090\u0091\7^\2\2\u0091\u0092\t\5\2\2\u0092\16\3")
        buf.write("\2\2\2\u0093\u0094\t\6\2\2\u0094\20\3\2\2\2\u0095\u0096")
        buf.write("\7a\2\2\u0096\22\3\2\2\2\u0097\u0098\t\7\2\2\u0098\24")
        buf.write("\3\2\2\2\u0099\u009a\7v\2\2\u009a\u009b\7t\2\2\u009b\u009c")
        buf.write("\7w\2\2\u009c\u009d\7g\2\2\u009d\26\3\2\2\2\u009e\u009f")
        buf.write("\7h\2\2\u009f\u00a0\7c\2\2\u00a0\u00a1\7n\2\2\u00a1\u00a2")
        buf.write("\7u\2\2\u00a2\u00a3\7g\2\2\u00a3\30\3\2\2\2\u00a4\u00a5")
        buf.write("\7p\2\2\u00a5\u00a6\7w\2\2\u00a6\u00a7\7o\2\2\u00a7\u00a8")
        buf.write("\7d\2\2\u00a8\u00a9\7g\2\2\u00a9\u00aa\7t\2\2\u00aa\32")
        buf.write("\3\2\2\2\u00ab\u00ac\7d\2\2\u00ac\u00ad\7q\2\2\u00ad\u00ae")
        buf.write("\7q\2\2\u00ae\u00af\7n\2\2\u00af\34\3\2\2\2\u00b0\u00b1")
        buf.write("\7u\2\2\u00b1\u00b2\7v\2\2\u00b2\u00b3\7t\2\2\u00b3\u00b4")
        buf.write("\7k\2\2\u00b4\u00b5\7p\2\2\u00b5\u00b6\7i\2\2\u00b6\36")
        buf.write("\3\2\2\2\u00b7\u00b8\7t\2\2\u00b8\u00b9\7g\2\2\u00b9\u00ba")
        buf.write("\7v\2\2\u00ba\u00bb\7w\2\2\u00bb\u00bc\7t\2\2\u00bc\u00bd")
        buf.write("\7p\2\2\u00bd \3\2\2\2\u00be\u00bf\7x\2\2\u00bf\u00c0")
        buf.write("\7c\2\2\u00c0\u00c1\7t\2\2\u00c1\"\3\2\2\2\u00c2\u00c3")
        buf.write("\7f\2\2\u00c3\u00c4\7{\2\2\u00c4\u00c5\7p\2\2\u00c5\u00c6")
        buf.write("\7c\2\2\u00c6\u00c7\7o\2\2\u00c7\u00c8\7k\2\2\u00c8\u00c9")
        buf.write("\7e\2\2\u00c9$\3\2\2\2\u00ca\u00cb\7h\2\2\u00cb\u00cc")
        buf.write("\7w\2\2\u00cc\u00cd\7p\2\2\u00cd\u00ce\7e\2\2\u00ce&\3")
        buf.write("\2\2\2\u00cf\u00d0\7h\2\2\u00d0\u00d1\7q\2\2\u00d1\u00d2")
        buf.write("\7t\2\2\u00d2(\3\2\2\2\u00d3\u00d4\7w\2\2\u00d4\u00d5")
        buf.write("\7p\2\2\u00d5\u00d6\7v\2\2\u00d6\u00d7\7k\2\2\u00d7\u00d8")
        buf.write("\7n\2\2\u00d8*\3\2\2\2\u00d9\u00da\7d\2\2\u00da\u00db")
        buf.write("\7{\2\2\u00db,\3\2\2\2\u00dc\u00dd\7d\2\2\u00dd\u00de")
        buf.write("\7t\2\2\u00de\u00df\7g\2\2\u00df\u00e0\7c\2\2\u00e0\u00e1")
        buf.write("\7m\2\2\u00e1.\3\2\2\2\u00e2\u00e3\7e\2\2\u00e3\u00e4")
        buf.write("\7q\2\2\u00e4\u00e5\7p\2\2\u00e5\u00e6\7v\2\2\u00e6\u00e7")
        buf.write("\7k\2\2\u00e7\u00e8\7p\2\2\u00e8\u00e9\7w\2\2\u00e9\u00ea")
        buf.write("\7g\2\2\u00ea\60\3\2\2\2\u00eb\u00ec\7k\2\2\u00ec\u00ed")
        buf.write("\7h\2\2\u00ed\62\3\2\2\2\u00ee\u00ef\7g\2\2\u00ef\u00f0")
        buf.write("\7n\2\2\u00f0\u00f1\7u\2\2\u00f1\u00f2\7g\2\2\u00f2\64")
        buf.write("\3\2\2\2\u00f3\u00f4\7g\2\2\u00f4\u00f5\7n\2\2\u00f5\u00f6")
        buf.write("\7k\2\2\u00f6\u00f7\7h\2\2\u00f7\66\3\2\2\2\u00f8\u00f9")
        buf.write("\7d\2\2\u00f9\u00fa\7g\2\2\u00fa\u00fb\7i\2\2\u00fb\u00fc")
        buf.write("\7k\2\2\u00fc\u00fd\7p\2\2\u00fd\u00ff\3\2\2\2\u00fe\u0100")
        buf.write("\5g\64\2\u00ff\u00fe\3\2\2\2\u0100\u0101\3\2\2\2\u0101")
        buf.write("\u00ff\3\2\2\2\u0101\u0102\3\2\2\2\u01028\3\2\2\2\u0103")
        buf.write("\u0104\7g\2\2\u0104\u0105\7p\2\2\u0105\u0106\7f\2\2\u0106")
        buf.write(":\3\2\2\2\u0107\u0108\7p\2\2\u0108\u0109\7q\2\2\u0109")
        buf.write("\u010a\7v\2\2\u010a<\3\2\2\2\u010b\u010c\7c\2\2\u010c")
        buf.write("\u010d\7p\2\2\u010d\u010e\7f\2\2\u010e>\3\2\2\2\u010f")
        buf.write("\u0110\7q\2\2\u0110\u0111\7t\2\2\u0111@\3\2\2\2\u0112")
        buf.write("\u0113\7-\2\2\u0113B\3\2\2\2\u0114\u0115\7/\2\2\u0115")
        buf.write("D\3\2\2\2\u0116\u0117\7,\2\2\u0117F\3\2\2\2\u0118\u0119")
        buf.write("\7\61\2\2\u0119H\3\2\2\2\u011a\u011b\7\'\2\2\u011bJ\3")
        buf.write("\2\2\2\u011c\u011d\7?\2\2\u011dL\3\2\2\2\u011e\u011f\7")
        buf.write(">\2\2\u011f\u0120\7/\2\2\u0120N\3\2\2\2\u0121\u0122\7")
        buf.write("?\2\2\u0122\u0123\7?\2\2\u0123P\3\2\2\2\u0124\u0125\7")
        buf.write("#\2\2\u0125\u0126\7?\2\2\u0126R\3\2\2\2\u0127\u0128\7")
        buf.write(">\2\2\u0128T\3\2\2\2\u0129\u012a\7@\2\2\u012aV\3\2\2\2")
        buf.write("\u012b\u012c\7>\2\2\u012c\u012d\7?\2\2\u012dX\3\2\2\2")
        buf.write("\u012e\u012f\7@\2\2\u012f\u0130\7?\2\2\u0130Z\3\2\2\2")
        buf.write("\u0131\u0132\7\60\2\2\u0132\u0133\7\60\2\2\u0133\u0134")
        buf.write("\7\60\2\2\u0134\\\3\2\2\2\u0135\u0136\7*\2\2\u0136^\3")
        buf.write("\2\2\2\u0137\u0138\7+\2\2\u0138`\3\2\2\2\u0139\u013a\7")
        buf.write("]\2\2\u013ab\3\2\2\2\u013b\u013c\7_\2\2\u013cd\3\2\2\2")
        buf.write("\u013d\u013e\7.\2\2\u013ef\3\2\2\2\u013f\u0140\7\f\2\2")
        buf.write("\u0140h\3\2\2\2\u0141\u0147\5\7\4\2\u0142\u0148\5\3\2")
        buf.write("\2\u0143\u0145\5\3\2\2\u0144\u0143\3\2\2\2\u0144\u0145")
        buf.write("\3\2\2\2\u0145\u0146\3\2\2\2\u0146\u0148\5\5\3\2\u0147")
        buf.write("\u0142\3\2\2\2\u0147\u0144\3\2\2\2\u0147\u0148\3\2\2\2")
        buf.write("\u0148j\3\2\2\2\u0149\u014d\7$\2\2\u014a\u014c\5\t\5\2")
        buf.write("\u014b\u014a\3\2\2\2\u014c\u014f\3\2\2\2\u014d\u014b\3")
        buf.write("\2\2\2\u014d\u014e\3\2\2\2\u014e\u0150\3\2\2\2\u014f\u014d")
        buf.write("\3\2\2\2\u0150\u0151\7$\2\2\u0151\u0152\b\66\2\2\u0152")
        buf.write("l\3\2\2\2\u0153\u0156\5\17\b\2\u0154\u0156\5\21\t\2\u0155")
        buf.write("\u0153\3\2\2\2\u0155\u0154\3\2\2\2\u0156\u015c\3\2\2\2")
        buf.write("\u0157\u015b\5\17\b\2\u0158\u015b\5\21\t\2\u0159\u015b")
        buf.write("\5\23\n\2\u015a\u0157\3\2\2\2\u015a\u0158\3\2\2\2\u015a")
        buf.write("\u0159\3\2\2\2\u015b\u015e\3\2\2\2\u015c\u015a\3\2\2\2")
        buf.write("\u015c\u015d\3\2\2\2\u015dn\3\2\2\2\u015e\u015c\3\2\2")
        buf.write("\2\u015f\u0160\7%\2\2\u0160\u0161\7%\2\2\u0161\u0165\3")
        buf.write("\2\2\2\u0162\u0164\13\2\2\2\u0163\u0162\3\2\2\2\u0164")
        buf.write("\u0167\3\2\2\2\u0165\u0166\3\2\2\2\u0165\u0163\3\2\2\2")
        buf.write("\u0166\u016b\3\2\2\2\u0167\u0165\3\2\2\2\u0168\u016a\n")
        buf.write("\b\2\2\u0169\u0168\3\2\2\2\u016a\u016d\3\2\2\2\u016b\u0169")
        buf.write("\3\2\2\2\u016b\u016c\3\2\2\2\u016c\u016e\3\2\2\2\u016d")
        buf.write("\u016b\3\2\2\2\u016e\u016f\b8\3\2\u016fp\3\2\2\2\u0170")
        buf.write("\u0172\t\t\2\2\u0171\u0170\3\2\2\2\u0172\u0173\3\2\2\2")
        buf.write("\u0173\u0171\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u0175\3")
        buf.write("\2\2\2\u0175\u0176\b9\3\2\u0176r\3\2\2\2\u0177\u0178\13")
        buf.write("\2\2\2\u0178\u0179\b:\4\2\u0179t\3\2\2\2\u017a\u017e\7")
        buf.write("$\2\2\u017b\u017d\5\t\5\2\u017c\u017b\3\2\2\2\u017d\u0180")
        buf.write("\3\2\2\2\u017e\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017f")
        buf.write("\u0183\3\2\2\2\u0180\u017e\3\2\2\2\u0181\u0184\5g\64\2")
        buf.write("\u0182\u0184\7\2\2\3\u0183\u0181\3\2\2\2\u0183\u0182\3")
        buf.write("\2\2\2\u0184\u0185\3\2\2\2\u0185\u0186\b;\5\2\u0186v\3")
        buf.write("\2\2\2\u0187\u018b\7$\2\2\u0188\u018a\5\t\5\2\u0189\u0188")
        buf.write("\3\2\2\2\u018a\u018d\3\2\2\2\u018b\u0189\3\2\2\2\u018b")
        buf.write("\u018c\3\2\2\2\u018c\u018e\3\2\2\2\u018d\u018b\3\2\2\2")
        buf.write("\u018e\u0191\7^\2\2\u018f\u0192\n\5\2\2\u0190\u0192\n")
        buf.write("\n\2\2\u0191\u018f\3\2\2\2\u0191\u0190\3\2\2\2\u0192\u0193")
        buf.write("\3\2\2\2\u0193\u0194\b<\6\2\u0194x\3\2\2\2\25\2{\177\u0086")
        buf.write("\u008b\u0101\u0144\u0147\u014d\u0155\u015a\u015c\u0165")
        buf.write("\u016b\u0173\u017e\u0183\u018b\u0191\7\3\66\2\b\2\2\3")
        buf.write(":\3\3;\4\3<\5")
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
    IDENTIFIER = 45
    COMMENT = 46
    WS = 47
    ERROR_CHAR = 48
    UNCLOSE_STRING = 49
    ILLEGAL_ESCAPE = 50

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'number'", "'bool'", "'string'", "'return'", 
            "'var'", "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
            "'break'", "'continue'", "'if'", "'else'", "'elif'", "'end'", 
            "'not'", "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", 
            "'='", "'<-'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
            "'...'", "'('", "')'", "'['", "']'", "','", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", "VAR", 
            "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
            "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "PLUS", 
            "MINUS", "MULT", "DIV", "MOD", "EQUAL", "LEFTARR", "EQUALEQUAL", 
            "NOTEQUAL", "LESS", "GREATER", "LESSOREQUAL", "GREATEROREQUAL", 
            "ELLIPSIS", "LBracket", "RBracket", "LSBracket", "RSBracket", 
            "COMMA", "NEWLINE", "NumberLit", "StringLit", "IDENTIFIER", 
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
                  "StringLit", "IDENTIFIER", "COMMENT", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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

     


