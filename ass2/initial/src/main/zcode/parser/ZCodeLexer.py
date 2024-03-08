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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\65")
        buf.write("\u01be\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5")
        buf.write("\2\u0082\n\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26")
        buf.write("\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3")
        buf.write("!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3$\3$\3%")
        buf.write("\3%\3%\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3\'\5\'\u0110\n\'\3(\3(\5(\u0114\n(\3(\5(\u0117\n(")
        buf.write("\3)\3)\5)\u011b\n)\3)\3)\3)\5)\u0120\n)\3)\3)\3*\3*\5")
        buf.write("*\u0126\n*\3*\6*\u0129\n*\r*\16*\u012a\3*\3*\5*\u012f")
        buf.write("\n*\3*\6*\u0132\n*\r*\16*\u0133\3*\3*\3+\3+\5+\u013a\n")
        buf.write("+\3+\6+\u013d\n+\r+\16+\u013e\3+\3+\3,\3,\7,\u0145\n,")
        buf.write("\f,\16,\u0148\13,\3-\3-\7-\u014c\n-\f-\16-\u014f\13-\3")
        buf.write("-\3-\3.\6.\u0154\n.\r.\16.\u0155\3/\3/\7/\u015a\n/\f/")
        buf.write("\16/\u015d\13/\3\60\3\60\3\60\5\60\u0162\n\60\3\60\6\60")
        buf.write("\u0165\n\60\r\60\16\60\u0166\3\61\3\61\3\61\3\61\7\61")
        buf.write("\u016d\n\61\f\61\16\61\u0170\13\61\3\61\6\61\u0173\n\61")
        buf.write("\r\61\16\61\u0174\3\61\3\61\3\61\7\61\u017a\n\61\f\61")
        buf.write("\16\61\u017d\13\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62")
        buf.write("\7\62\u0186\n\62\f\62\16\62\u0189\13\62\3\62\3\62\5\62")
        buf.write("\u018d\n\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3")
        buf.write("\63\3\63\3\63\7\63\u019a\n\63\f\63\16\63\u019d\13\63\3")
        buf.write("\63\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\65\3\65\7\65")
        buf.write("\u01a9\n\65\f\65\16\65\u01ac\13\65\3\65\3\65\3\66\6\66")
        buf.write("\u01b1\n\66\r\66\16\66\u01b2\3\66\3\66\3\67\5\67\u01b8")
        buf.write("\n\67\3\67\3\67\38\38\38\3\u0187\29\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34")
        buf.write("\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[\2]\2_")
        buf.write("\2a/c\60e\61g\2i\62k\63m\64o\65\3\2\f\4\2GGgg\5\2C\\a")
        buf.write("ac|\3\2\62;\6\2\62;C\\aac|\3\2$$\6\2\f\f\17\17$$^^\7\2")
        buf.write("))^^ddhhvv\t\2))^^ddhhppttvv\4\2\f\f\17\17\5\2\13\13\16")
        buf.write("\16\"\"\2\u01de\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2o\3\2\2\2\3\u0081\3\2\2\2\5\u0083\3\2\2\2")
        buf.write("\7\u0086\3\2\2\2\t\u008b\3\2\2\2\13\u0090\3\2\2\2\r\u0094")
        buf.write("\3\2\2\2\17\u0096\3\2\2\2\21\u0098\3\2\2\2\23\u009a\3")
        buf.write("\2\2\2\25\u009c\3\2\2\2\27\u00a0\3\2\2\2\31\u00a3\3\2")
        buf.write("\2\2\33\u00a7\3\2\2\2\35\u00aa\3\2\2\2\37\u00ac\3\2\2")
        buf.write("\2!\u00af\3\2\2\2#\u00b2\3\2\2\2%\u00b4\3\2\2\2\'\u00b7")
        buf.write("\3\2\2\2)\u00b9\3\2\2\2+\u00bb\3\2\2\2-\u00bd\3\2\2\2")
        buf.write("/\u00bf\3\2\2\2\61\u00c1\3\2\2\2\63\u00c7\3\2\2\2\65\u00cb")
        buf.write("\3\2\2\2\67\u00cf\3\2\2\29\u00d2\3\2\2\2;\u00d6\3\2\2")
        buf.write("\2=\u00de\3\2\2\2?\u00e0\3\2\2\2A\u00e6\3\2\2\2C\u00ef")
        buf.write("\3\2\2\2E\u00f6\3\2\2\2G\u00fb\3\2\2\2I\u00fd\3\2\2\2")
        buf.write("K\u0103\3\2\2\2M\u010f\3\2\2\2O\u0111\3\2\2\2Q\u0118\3")
        buf.write("\2\2\2S\u0123\3\2\2\2U\u0137\3\2\2\2W\u0142\3\2\2\2Y\u0149")
        buf.write("\3\2\2\2[\u0153\3\2\2\2]\u0157\3\2\2\2_\u015e\3\2\2\2")
        buf.write("a\u0168\3\2\2\2c\u0181\3\2\2\2e\u0190\3\2\2\2g\u01a1\3")
        buf.write("\2\2\2i\u01a4\3\2\2\2k\u01b0\3\2\2\2m\u01b7\3\2\2\2o\u01bb")
        buf.write("\3\2\2\2qr\7p\2\2rs\7w\2\2st\7o\2\2tu\7d\2\2uv\7g\2\2")
        buf.write("v\u0082\7t\2\2wx\7u\2\2xy\7v\2\2yz\7t\2\2z{\7k\2\2{|\7")
        buf.write("p\2\2|\u0082\7i\2\2}~\7d\2\2~\177\7q\2\2\177\u0080\7q")
        buf.write("\2\2\u0080\u0082\7n\2\2\u0081q\3\2\2\2\u0081w\3\2\2\2")
        buf.write("\u0081}\3\2\2\2\u0082\4\3\2\2\2\u0083\u0084\7k\2\2\u0084")
        buf.write("\u0085\7h\2\2\u0085\6\3\2\2\2\u0086\u0087\7g\2\2\u0087")
        buf.write("\u0088\7n\2\2\u0088\u0089\7k\2\2\u0089\u008a\7h\2\2\u008a")
        buf.write("\b\3\2\2\2\u008b\u008c\7g\2\2\u008c\u008d\7n\2\2\u008d")
        buf.write("\u008e\7u\2\2\u008e\u008f\7g\2\2\u008f\n\3\2\2\2\u0090")
        buf.write("\u0091\7h\2\2\u0091\u0092\7q\2\2\u0092\u0093\7t\2\2\u0093")
        buf.write("\f\3\2\2\2\u0094\u0095\7/\2\2\u0095\16\3\2\2\2\u0096\u0097")
        buf.write("\7-\2\2\u0097\20\3\2\2\2\u0098\u0099\7,\2\2\u0099\22\3")
        buf.write("\2\2\2\u009a\u009b\7\61\2\2\u009b\24\3\2\2\2\u009c\u009d")
        buf.write("\7c\2\2\u009d\u009e\7p\2\2\u009e\u009f\7f\2\2\u009f\26")
        buf.write("\3\2\2\2\u00a0\u00a1\7q\2\2\u00a1\u00a2\7t\2\2\u00a2\30")
        buf.write("\3\2\2\2\u00a3\u00a4\7\60\2\2\u00a4\u00a5\7\60\2\2\u00a5")
        buf.write("\u00a6\7\60\2\2\u00a6\32\3\2\2\2\u00a7\u00a8\7>\2\2\u00a8")
        buf.write("\u00a9\7/\2\2\u00a9\34\3\2\2\2\u00aa\u00ab\7?\2\2\u00ab")
        buf.write("\36\3\2\2\2\u00ac\u00ad\7?\2\2\u00ad\u00ae\7?\2\2\u00ae")
        buf.write(" \3\2\2\2\u00af\u00b0\7@\2\2\u00b0\u00b1\7?\2\2\u00b1")
        buf.write("\"\3\2\2\2\u00b2\u00b3\7@\2\2\u00b3$\3\2\2\2\u00b4\u00b5")
        buf.write("\7>\2\2\u00b5\u00b6\7?\2\2\u00b6&\3\2\2\2\u00b7\u00b8")
        buf.write("\7>\2\2\u00b8(\3\2\2\2\u00b9\u00ba\7*\2\2\u00ba*\3\2\2")
        buf.write("\2\u00bb\u00bc\7+\2\2\u00bc,\3\2\2\2\u00bd\u00be\7]\2")
        buf.write("\2\u00be.\3\2\2\2\u00bf\u00c0\7_\2\2\u00c0\60\3\2\2\2")
        buf.write("\u00c1\u00c2\7d\2\2\u00c2\u00c3\7g\2\2\u00c3\u00c4\7i")
        buf.write("\2\2\u00c4\u00c5\7k\2\2\u00c5\u00c6\7p\2\2\u00c6\62\3")
        buf.write("\2\2\2\u00c7\u00c8\7g\2\2\u00c8\u00c9\7p\2\2\u00c9\u00ca")
        buf.write("\7f\2\2\u00ca\64\3\2\2\2\u00cb\u00cc\7p\2\2\u00cc\u00cd")
        buf.write("\7q\2\2\u00cd\u00ce\7v\2\2\u00ce\66\3\2\2\2\u00cf\u00d0")
        buf.write("\7#\2\2\u00d0\u00d1\7?\2\2\u00d18\3\2\2\2\u00d2\u00d3")
        buf.write("\7x\2\2\u00d3\u00d4\7c\2\2\u00d4\u00d5\7t\2\2\u00d5:\3")
        buf.write("\2\2\2\u00d6\u00d7\7f\2\2\u00d7\u00d8\7{\2\2\u00d8\u00d9")
        buf.write("\7p\2\2\u00d9\u00da\7c\2\2\u00da\u00db\7o\2\2\u00db\u00dc")
        buf.write("\7k\2\2\u00dc\u00dd\7e\2\2\u00dd<\3\2\2\2\u00de\u00df")
        buf.write("\7.\2\2\u00df>\3\2\2\2\u00e0\u00e1\7d\2\2\u00e1\u00e2")
        buf.write("\7t\2\2\u00e2\u00e3\7g\2\2\u00e3\u00e4\7c\2\2\u00e4\u00e5")
        buf.write("\7m\2\2\u00e5@\3\2\2\2\u00e6\u00e7\7e\2\2\u00e7\u00e8")
        buf.write("\7q\2\2\u00e8\u00e9\7p\2\2\u00e9\u00ea\7v\2\2\u00ea\u00eb")
        buf.write("\7k\2\2\u00eb\u00ec\7p\2\2\u00ec\u00ed\7w\2\2\u00ed\u00ee")
        buf.write("\7g\2\2\u00eeB\3\2\2\2\u00ef\u00f0\7t\2\2\u00f0\u00f1")
        buf.write("\7g\2\2\u00f1\u00f2\7v\2\2\u00f2\u00f3\7w\2\2\u00f3\u00f4")
        buf.write("\7t\2\2\u00f4\u00f5\7p\2\2\u00f5D\3\2\2\2\u00f6\u00f7")
        buf.write("\7h\2\2\u00f7\u00f8\7w\2\2\u00f8\u00f9\7p\2\2\u00f9\u00fa")
        buf.write("\7e\2\2\u00faF\3\2\2\2\u00fb\u00fc\7\'\2\2\u00fcH\3\2")
        buf.write("\2\2\u00fd\u00fe\7w\2\2\u00fe\u00ff\7p\2\2\u00ff\u0100")
        buf.write("\7v\2\2\u0100\u0101\7k\2\2\u0101\u0102\7n\2\2\u0102J\3")
        buf.write("\2\2\2\u0103\u0104\7d\2\2\u0104\u0105\7{\2\2\u0105L\3")
        buf.write("\2\2\2\u0106\u0107\7v\2\2\u0107\u0108\7t\2\2\u0108\u0109")
        buf.write("\7w\2\2\u0109\u0110\7g\2\2\u010a\u010b\7h\2\2\u010b\u010c")
        buf.write("\7c\2\2\u010c\u010d\7n\2\2\u010d\u010e\7u\2\2\u010e\u0110")
        buf.write("\7g\2\2\u010f\u0106\3\2\2\2\u010f\u010a\3\2\2\2\u0110")
        buf.write("N\3\2\2\2\u0111\u0113\5[.\2\u0112\u0114\5]/\2\u0113\u0112")
        buf.write("\3\2\2\2\u0113\u0114\3\2\2\2\u0114\u0116\3\2\2\2\u0115")
        buf.write("\u0117\5_\60\2\u0116\u0115\3\2\2\2\u0116\u0117\3\2\2\2")
        buf.write("\u0117P\3\2\2\2\u0118\u011a\5[.\2\u0119\u011b\5]/\2\u011a")
        buf.write("\u0119\3\2\2\2\u011a\u011b\3\2\2\2\u011b\u011c\3\2\2\2")
        buf.write("\u011c\u011f\t\2\2\2\u011d\u0120\5\17\b\2\u011e\u0120")
        buf.write("\5\r\7\2\u011f\u011d\3\2\2\2\u011f\u011e\3\2\2\2\u011f")
        buf.write("\u0120\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u0122\b)\2\2")
        buf.write("\u0122R\3\2\2\2\u0123\u0125\5[.\2\u0124\u0126\5]/\2\u0125")
        buf.write("\u0124\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u0128\3\2\2\2")
        buf.write("\u0127\u0129\t\3\2\2\u0128\u0127\3\2\2\2\u0129\u012a\3")
        buf.write("\2\2\2\u012a\u0128\3\2\2\2\u012a\u012b\3\2\2\2\u012b\u012e")
        buf.write("\3\2\2\2\u012c\u012f\5\17\b\2\u012d\u012f\5\r\7\2\u012e")
        buf.write("\u012c\3\2\2\2\u012e\u012d\3\2\2\2\u012e\u012f\3\2\2\2")
        buf.write("\u012f\u0131\3\2\2\2\u0130\u0132\t\4\2\2\u0131\u0130\3")
        buf.write("\2\2\2\u0132\u0133\3\2\2\2\u0133\u0131\3\2\2\2\u0133\u0134")
        buf.write("\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0136\b*\3\2\u0136")
        buf.write("T\3\2\2\2\u0137\u0139\5[.\2\u0138\u013a\5]/\2\u0139\u0138")
        buf.write("\3\2\2\2\u0139\u013a\3\2\2\2\u013a\u013c\3\2\2\2\u013b")
        buf.write("\u013d\t\3\2\2\u013c\u013b\3\2\2\2\u013d\u013e\3\2\2\2")
        buf.write("\u013e\u013c\3\2\2\2\u013e\u013f\3\2\2\2\u013f\u0140\3")
        buf.write("\2\2\2\u0140\u0141\b+\4\2\u0141V\3\2\2\2\u0142\u0146\t")
        buf.write("\3\2\2\u0143\u0145\t\5\2\2\u0144\u0143\3\2\2\2\u0145\u0148")
        buf.write("\3\2\2\2\u0146\u0144\3\2\2\2\u0146\u0147\3\2\2\2\u0147")
        buf.write("X\3\2\2\2\u0148\u0146\3\2\2\2\u0149\u014d\t\4\2\2\u014a")
        buf.write("\u014c\t\5\2\2\u014b\u014a\3\2\2\2\u014c\u014f\3\2\2\2")
        buf.write("\u014d\u014b\3\2\2\2\u014d\u014e\3\2\2\2\u014e\u0150\3")
        buf.write("\2\2\2\u014f\u014d\3\2\2\2\u0150\u0151\b-\5\2\u0151Z\3")
        buf.write("\2\2\2\u0152\u0154\t\4\2\2\u0153\u0152\3\2\2\2\u0154\u0155")
        buf.write("\3\2\2\2\u0155\u0153\3\2\2\2\u0155\u0156\3\2\2\2\u0156")
        buf.write("\\\3\2\2\2\u0157\u015b\7\60\2\2\u0158\u015a\t\4\2\2\u0159")
        buf.write("\u0158\3\2\2\2\u015a\u015d\3\2\2\2\u015b\u0159\3\2\2\2")
        buf.write("\u015b\u015c\3\2\2\2\u015c^\3\2\2\2\u015d\u015b\3\2\2")
        buf.write("\2\u015e\u0161\t\2\2\2\u015f\u0162\5\17\b\2\u0160\u0162")
        buf.write("\5\r\7\2\u0161\u015f\3\2\2\2\u0161\u0160\3\2\2\2\u0161")
        buf.write("\u0162\3\2\2\2\u0162\u0164\3\2\2\2\u0163\u0165\t\4\2\2")
        buf.write("\u0164\u0163\3\2\2\2\u0165\u0166\3\2\2\2\u0166\u0164\3")
        buf.write("\2\2\2\u0166\u0167\3\2\2\2\u0167`\3\2\2\2\u0168\u016e")
        buf.write("\7$\2\2\u0169\u016d\n\6\2\2\u016a\u016b\7)\2\2\u016b\u016d")
        buf.write("\7$\2\2\u016c\u0169\3\2\2\2\u016c\u016a\3\2\2\2\u016d")
        buf.write("\u0170\3\2\2\2\u016e\u016c\3\2\2\2\u016e\u016f\3\2\2\2")
        buf.write("\u016f\u0172\3\2\2\2\u0170\u016e\3\2\2\2\u0171\u0173\5")
        buf.write("g\64\2\u0172\u0171\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u0172")
        buf.write("\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u017b\3\2\2\2\u0176")
        buf.write("\u017a\n\6\2\2\u0177\u0178\7)\2\2\u0178\u017a\7$\2\2\u0179")
        buf.write("\u0176\3\2\2\2\u0179\u0177\3\2\2\2\u017a\u017d\3\2\2\2")
        buf.write("\u017b\u0179\3\2\2\2\u017b\u017c\3\2\2\2\u017c\u017e\3")
        buf.write("\2\2\2\u017d\u017b\3\2\2\2\u017e\u017f\7$\2\2\u017f\u0180")
        buf.write("\b\61\6\2\u0180b\3\2\2\2\u0181\u0187\7$\2\2\u0182\u0186")
        buf.write("\n\6\2\2\u0183\u0184\7)\2\2\u0184\u0186\7$\2\2\u0185\u0182")
        buf.write("\3\2\2\2\u0185\u0183\3\2\2\2\u0186\u0189\3\2\2\2\u0187")
        buf.write("\u0188\3\2\2\2\u0187\u0185\3\2\2\2\u0188\u018c\3\2\2\2")
        buf.write("\u0189\u0187\3\2\2\2\u018a\u018d\5m\67\2\u018b\u018d\7")
        buf.write("\2\2\3\u018c\u018a\3\2\2\2\u018c\u018b\3\2\2\2\u018d\u018e")
        buf.write("\3\2\2\2\u018e\u018f\b\62\7\2\u018fd\3\2\2\2\u0190\u019b")
        buf.write("\7$\2\2\u0191\u019a\n\7\2\2\u0192\u0193\7)\2\2\u0193\u019a")
        buf.write("\7$\2\2\u0194\u0195\7^\2\2\u0195\u0196\7)\2\2\u0196\u019a")
        buf.write("\7$\2\2\u0197\u0198\7^\2\2\u0198\u019a\t\b\2\2\u0199\u0191")
        buf.write("\3\2\2\2\u0199\u0192\3\2\2\2\u0199\u0194\3\2\2\2\u0199")
        buf.write("\u0197\3\2\2\2\u019a\u019d\3\2\2\2\u019b\u0199\3\2\2\2")
        buf.write("\u019b\u019c\3\2\2\2\u019c\u019e\3\2\2\2\u019d\u019b\3")
        buf.write("\2\2\2\u019e\u019f\7$\2\2\u019f\u01a0\b\63\b\2\u01a0f")
        buf.write("\3\2\2\2\u01a1\u01a2\7^\2\2\u01a2\u01a3\n\t\2\2\u01a3")
        buf.write("h\3\2\2\2\u01a4\u01a5\7%\2\2\u01a5\u01a6\7%\2\2\u01a6")
        buf.write("\u01aa\3\2\2\2\u01a7\u01a9\n\n\2\2\u01a8\u01a7\3\2\2\2")
        buf.write("\u01a9\u01ac\3\2\2\2\u01aa\u01a8\3\2\2\2\u01aa\u01ab\3")
        buf.write("\2\2\2\u01ab\u01ad\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ad\u01ae")
        buf.write("\b\65\t\2\u01aej\3\2\2\2\u01af\u01b1\t\13\2\2\u01b0\u01af")
        buf.write("\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b2")
        buf.write("\u01b3\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b5\b\66\t")
        buf.write("\2\u01b5l\3\2\2\2\u01b6\u01b8\7\17\2\2\u01b7\u01b6\3\2")
        buf.write("\2\2\u01b7\u01b8\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9\u01ba")
        buf.write("\7\f\2\2\u01ban\3\2\2\2\u01bb\u01bc\13\2\2\2\u01bc\u01bd")
        buf.write("\b8\n\2\u01bdp\3\2\2\2\"\2\u0081\u010f\u0113\u0116\u011a")
        buf.write("\u011f\u0125\u012a\u012e\u0133\u0139\u013e\u0146\u014d")
        buf.write("\u0155\u015b\u0161\u0166\u016c\u016e\u0174\u0179\u017b")
        buf.write("\u0185\u0187\u018c\u0199\u019b\u01aa\u01b2\u01b7\13\3")
        buf.write(")\2\3*\3\3+\4\3-\5\3\61\6\3\62\7\3\63\b\b\2\2\38\t")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TYPE = 1
    IF = 2
    ELIF = 3
    ELSE = 4
    FOR = 5
    SUB = 6
    ADD = 7
    MUL = 8
    DIV = 9
    AND = 10
    OR = 11
    CONCAT = 12
    ASSIGN = 13
    EQ = 14
    DEQ = 15
    GE = 16
    GT = 17
    LE = 18
    LT = 19
    LP = 20
    RP = 21
    LB = 22
    RB = 23
    BEGIN = 24
    END = 25
    NOT = 26
    NEQ = 27
    VAR = 28
    DYN = 29
    COMMA = 30
    BREAK = 31
    CONTINUE = 32
    RETURN = 33
    FUNC = 34
    MOD = 35
    UNTIL = 36
    BY = 37
    BoolLit = 38
    NumberLit = 39
    INVALID_NUMBER_1 = 40
    INVALID_NUMBER_2 = 41
    INVALID_NUMBER_3 = 42
    IDENTIFIER = 43
    INVALID_IDENTIFIER = 44
    ILLEGAL_ESCAPE = 45
    UNCLOSE_STRING = 46
    StringLit = 47
    COMMENT = 48
    WS = 49
    NEWLINE = 50
    ERROR_CHAR = 51

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'elif'", "'else'", "'for'", "'-'", "'+'", "'*'", "'/'", 
            "'and'", "'or'", "'...'", "'<-'", "'='", "'=='", "'>='", "'>'", 
            "'<='", "'<'", "'('", "')'", "'['", "']'", "'begin'", "'end'", 
            "'not'", "'!='", "'var'", "'dynamic'", "','", "'break'", "'continue'", 
            "'return'", "'func'", "'%'", "'until'", "'by'" ]

    symbolicNames = [ "<INVALID>",
            "TYPE", "IF", "ELIF", "ELSE", "FOR", "SUB", "ADD", "MUL", "DIV", 
            "AND", "OR", "CONCAT", "ASSIGN", "EQ", "DEQ", "GE", "GT", "LE", 
            "LT", "LP", "RP", "LB", "RB", "BEGIN", "END", "NOT", "NEQ", 
            "VAR", "DYN", "COMMA", "BREAK", "CONTINUE", "RETURN", "FUNC", 
            "MOD", "UNTIL", "BY", "BoolLit", "NumberLit", "INVALID_NUMBER_1", 
            "INVALID_NUMBER_2", "INVALID_NUMBER_3", "IDENTIFIER", "INVALID_IDENTIFIER", 
            "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "StringLit", "COMMENT", 
            "WS", "NEWLINE", "ERROR_CHAR" ]

    ruleNames = [ "TYPE", "IF", "ELIF", "ELSE", "FOR", "SUB", "ADD", "MUL", 
                  "DIV", "AND", "OR", "CONCAT", "ASSIGN", "EQ", "DEQ", "GE", 
                  "GT", "LE", "LT", "LP", "RP", "LB", "RB", "BEGIN", "END", 
                  "NOT", "NEQ", "VAR", "DYN", "COMMA", "BREAK", "CONTINUE", 
                  "RETURN", "FUNC", "MOD", "UNTIL", "BY", "BoolLit", "NumberLit", 
                  "INVALID_NUMBER_1", "INVALID_NUMBER_2", "INVALID_NUMBER_3", 
                  "IDENTIFIER", "INVALID_IDENTIFIER", "INTEGER", "DECIMAL", 
                  "EXPONENT", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "StringLit", 
                  "INVALID_ESCAPED_SEQUENCE", "COMMENT", "WS", "NEWLINE", 
                  "ERROR_CHAR" ]

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
            actions[39] = self.INVALID_NUMBER_1_action 
            actions[40] = self.INVALID_NUMBER_2_action 
            actions[41] = self.INVALID_NUMBER_3_action 
            actions[43] = self.INVALID_IDENTIFIER_action 
            actions[47] = self.ILLEGAL_ESCAPE_action 
            actions[48] = self.UNCLOSE_STRING_action 
            actions[49] = self.StringLit_action 
            actions[54] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INVALID_NUMBER_1_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     

    def INVALID_NUMBER_2_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def INVALID_NUMBER_3_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise ErrorToken(self.text)
     

    def INVALID_IDENTIFIER_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise IllegalEscape(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise UncloseString(self.text)
     

    def StringLit_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
             self.text = str(bytes(self.text, "utf-8").decode("unicode_escape"))[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:
            raise ErrorToken(self.text)
     


