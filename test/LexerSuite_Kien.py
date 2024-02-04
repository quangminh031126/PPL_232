import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
	def test_101(self):
		self.assertTrue(TestLexer.test('''## z`Mv?gm@.G3#EC /[m"''', '''<EOF>''', 101))

	def test_102(self):
		self.assertTrue(TestLexer.test("EQ_aE", "EQ_aE,<EOF>", 102))

	def test_103(self):
		self.assertTrue(TestLexer.test('''## &*G''', '''<EOF>''', 103))

	def test_104(self):
		self.assertTrue(TestLexer.test("4E-66", "4E-66,<EOF>", 104))

	def test_105(self):
		self.assertTrue(TestLexer.test('''" :\\wR'""''', '''Illegal Escape In String:  :\\w''', 105))

	def test_106(self):
		self.assertTrue(TestLexer.test('''"p
'"Zi"''', '''Unclosed String: p''', 106))

	def test_107(self):
		self.assertTrue(TestLexer.test("VJTzir", "VJTzir,<EOF>", 107))

	def test_108(self):
		self.assertTrue(TestLexer.test("Jd7Sd", "Jd7Sd,<EOF>", 108))

	def test_109(self):
		self.assertTrue(TestLexer.test("613", "613,<EOF>", 109))

	def test_110(self):
		self.assertTrue(TestLexer.test("NE", "NE,<EOF>", 110))

	def test_111(self):
		self.assertTrue(TestLexer.test('''"\\unL'"V"''', '''Illegal Escape In String: \\u''', 111))

	def test_112(self):
		self.assertTrue(TestLexer.test('''"'"'""''', '''\'"'",<EOF>''', 112))

	def test_113(self):
		self.assertTrue(TestLexer.test("505E-92", "505E-92,<EOF>", 113))

	def test_114(self):
		self.assertTrue(TestLexer.test("0", "0,<EOF>", 114))

	def test_115(self):
		self.assertTrue(TestLexer.test("554", "554,<EOF>", 115))

	def test_116(self):
		self.assertTrue(TestLexer.test("21.430e81", "21.430e81,<EOF>", 116))

	def test_117(self):
		self.assertTrue(TestLexer.test('''"'"\\i?d'""''', '''Illegal Escape In String: '"\\i''', 117))

	def test_118(self):
		self.assertTrue(TestLexer.test('''## {}t6qYo"oJ=f5:vdV|?p''', '''<EOF>''', 118))

	def test_119(self):
		self.assertTrue(TestLexer.test('''## E&<eU''', '''<EOF>''', 119))

	def test_120(self):
		self.assertTrue(TestLexer.test('''## +''', '''<EOF>''', 120))

	def test_121(self):
		self.assertTrue(TestLexer.test("hi", "hi,<EOF>", 121))

	def test_122(self):
		self.assertTrue(TestLexer.test('''"'") ''', '''Unclosed String: '") ''', 122))

	def test_123(self):
		self.assertTrue(TestLexer.test("31.669E-08", "31.669E-08,<EOF>", 123))

	def test_124(self):
		self.assertTrue(TestLexer.test("g7SbkeEG2", "g7SbkeEG2,<EOF>", 124))

	def test_125(self):
		self.assertTrue(TestLexer.test("24E+22", "24E+22,<EOF>", 125))

	def test_126(self):
		self.assertTrue(TestLexer.test('''## #Um@$93''', '''<EOF>''', 126))

	def test_127(self):
		self.assertTrue(TestLexer.test("12.561", "12.561,<EOF>", 127))

	def test_128(self):
		self.assertTrue(TestLexer.test("J", "J,<EOF>", 128))

	def test_129(self):
		self.assertTrue(TestLexer.test("635.030", "635.030,<EOF>", 129))

	def test_130(self):
		self.assertTrue(TestLexer.test('''## 7m2||Wz=*X+''', '''<EOF>''', 130))

	def test_131(self):
		self.assertTrue(TestLexer.test("_VD@Ry", "_VD,Error Token @", 131))

	def test_132(self):
		self.assertTrue(TestLexer.test('''"\\z^"''', '''Illegal Escape In String: \\z''', 132))

	def test_133(self):
		self.assertTrue(TestLexer.test('''"\\x "''', '''Illegal Escape In String: \\x''', 133))

	def test_134(self):
		self.assertTrue(TestLexer.test('''## +` rA5vImM''', '''<EOF>''', 134))

	def test_135(self):
		self.assertTrue(TestLexer.test("730.362", "730.362,<EOF>", 135))

	def test_136(self):
		self.assertTrue(TestLexer.test("97.575E44", "97.575E44,<EOF>", 136))

	def test_137(self):
		self.assertTrue(TestLexer.test('''"s\\h'"'""''', '''Illegal Escape In String: s\\h''', 137))

	def test_138(self):
		self.assertTrue(TestLexer.test("2", "2,<EOF>", 138))

	def test_139(self):
		self.assertTrue(TestLexer.test("jWm", "jWm,<EOF>", 139))

	def test_140(self):
		self.assertTrue(TestLexer.test('''"cv"''', '''cv,<EOF>''', 140))

	def test_141(self):
		self.assertTrue(TestLexer.test('''## ]?nH=''', '''<EOF>''', 141))

	def test_142(self):
		self.assertTrue(TestLexer.test("f", "f,<EOF>", 142))

	def test_143(self):
		self.assertTrue(TestLexer.test("o8$^6Om1", "o8,Error Token $", 143))

	def test_144(self):
		self.assertTrue(TestLexer.test('''## C85(.)[''', '''<EOF>''', 144))

	def test_145(self):
		self.assertTrue(TestLexer.test("3lPeT", "3,lPeT,<EOF>", 145))

	def test_146(self):
		self.assertTrue(TestLexer.test("732E-94", "732E-94,<EOF>", 146))

	def test_147(self):
		self.assertTrue(TestLexer.test('''## `y-hB}Vs}xAv-Hm=FN''', '''<EOF>''', 147))

	def test_148(self):
		self.assertTrue(TestLexer.test('''## x##+xNQBON''', '''<EOF>''', 148))

	def test_149(self):
		self.assertTrue(TestLexer.test("5DO2Ei6$1&", "5,DO2Ei6,Error Token $", 149))

	def test_150(self):
		self.assertTrue(TestLexer.test('''## =tCD!_H+<i.+7^:i}''', '''<EOF>''', 150))

	def test_151(self):
		self.assertTrue(TestLexer.test('''## >]UT$nZV''', '''<EOF>''', 151))

	def test_152(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 152))

	def test_153(self):
		self.assertTrue(TestLexer.test('''"\\yz'""''', '''Illegal Escape In String: \\y''', 153))

	def test_154(self):
		self.assertTrue(TestLexer.test("38.673e+64", "38.673e+64,<EOF>", 154))

	def test_155(self):
		self.assertTrue(TestLexer.test("8E-67", "8E-67,<EOF>", 155))

	def test_156(self):
		self.assertTrue(TestLexer.test("0", "0,<EOF>", 156))

	def test_157(self):
		self.assertTrue(TestLexer.test('''"o\\h'"'"h"''', '''Illegal Escape In String: o\\h''', 157))

	def test_158(self):
		self.assertTrue(TestLexer.test('''" s'"'""''', ''' s'"'",<EOF>''', 158))

	def test_159(self):
		self.assertTrue(TestLexer.test("UUO8IVl", "UUO8IVl,<EOF>", 159))

	def test_160(self):
		self.assertTrue(TestLexer.test('''"L'"W ''', '''Unclosed String: L'"W ''', 160))

	def test_161(self):
		self.assertTrue(TestLexer.test("8H1@O", "8,H1,Error Token @", 161))

	def test_162(self):
		self.assertTrue(TestLexer.test('''"^'"e-"''', '''^'"e-,<EOF>''', 162))

	def test_163(self):
		self.assertTrue(TestLexer.test("er528U1", "er528U1,<EOF>", 163))

	def test_164(self):
		self.assertTrue(TestLexer.test('''"'"\\u'"B'""''', '''Illegal Escape In String: '"\\u''', 164))

	def test_165(self):
		self.assertTrue(TestLexer.test('''## @pdILp1''', '''<EOF>''', 165))

	def test_166(self):
		self.assertTrue(TestLexer.test('''## (ek?&lST$T&"~v''', '''<EOF>''', 166))

	def test_167(self):
		self.assertTrue(TestLexer.test("963e48", "963e48,<EOF>", 167))

	def test_168(self):
		self.assertTrue(TestLexer.test("1.727E31", "1.727E31,<EOF>", 168))

	def test_169(self):
		self.assertTrue(TestLexer.test("116", "116,<EOF>", 169))

	def test_170(self):
		self.assertTrue(TestLexer.test('''## aHfG>''', '''<EOF>''', 170))

	def test_171(self):
		self.assertTrue(TestLexer.test('''## y@0g$ZbDaQ>!yvoC''', '''<EOF>''', 171))

	def test_172(self):
		self.assertTrue(TestLexer.test('''"'" ''', '''Unclosed String: '" ''', 172))

	def test_173(self):
		self.assertTrue(TestLexer.test('''## MQ0!''', '''<EOF>''', 173))

	def test_174(self):
		self.assertTrue(TestLexer.test("v8u0hQrx&", "v8u0hQrx,Error Token &", 174))

	def test_175(self):
		self.assertTrue(TestLexer.test("dL", "dL,<EOF>", 175))

	def test_176(self):
		self.assertTrue(TestLexer.test("MQzpmIJ", "MQzpmIJ,<EOF>", 176))

	def test_177(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 177))

	def test_178(self):
		self.assertTrue(TestLexer.test("stxZ", "stxZ,<EOF>", 178))

	def test_179(self):
		self.assertTrue(TestLexer.test("3E+06", "3E+06,<EOF>", 179))

	def test_180(self):
		self.assertTrue(TestLexer.test("8E-69", "8E-69,<EOF>", 180))

	def test_181(self):
		self.assertTrue(TestLexer.test('''## Yn3 a0QU=WUq;*Wz]e ''', '''<EOF>''', 181))

	def test_182(self):
		self.assertTrue(TestLexer.test("ZlM", "ZlM,<EOF>", 182))

	def test_183(self):
		self.assertTrue(TestLexer.test('''## LVK{^P/2tE,''', '''<EOF>''', 183))

	def test_184(self):
		self.assertTrue(TestLexer.test('''## T{njZ''', '''<EOF>''', 184))

	def test_185(self):
		self.assertTrue(TestLexer.test('''## 0Gf|mxe[C.pK{Z;%i0W''', '''<EOF>''', 185))

	def test_186(self):
		self.assertTrue(TestLexer.test("63", "63,<EOF>", 186))

	def test_187(self):
		self.assertTrue(TestLexer.test('''## `{5N:0 U)''', '''<EOF>''', 187))

	def test_188(self):
		self.assertTrue(TestLexer.test("13e51", "13e51,<EOF>", 188))

	def test_189(self):
		self.assertTrue(TestLexer.test('''## ^r>;[^l@z''', '''<EOF>''', 189))

	def test_190(self):
		self.assertTrue(TestLexer.test('''"\\j'"3"''', '''Illegal Escape In String: \\j''', 190))

	def test_191(self):
		self.assertTrue(TestLexer.test('''"'""''', '''\'",<EOF>''', 191))

	def test_192(self):
		self.assertTrue(TestLexer.test('''"\\h'""''', '''Illegal Escape In String: \\h''', 192))

	def test_193(self):
		self.assertTrue(TestLexer.test('''## 8M~Pg"''', '''<EOF>''', 193))

	def test_194(self):
		self.assertTrue(TestLexer.test("69.153E35", "69.153E35,<EOF>", 194))

	def test_195(self):
		self.assertTrue(TestLexer.test('''## XtEe''', '''<EOF>''', 195))

	def test_196(self):
		self.assertTrue(TestLexer.test("232.876", "232.876,<EOF>", 196))

	def test_197(self):
		self.assertTrue(TestLexer.test("80E-13", "80E-13,<EOF>", 197))

	def test_198(self):
		self.assertTrue(TestLexer.test("FMbgtu", "FMbgtu,<EOF>", 198))

	def test_199(self):
		self.assertTrue(TestLexer.test("&IhUBL4z0m", "Error Token &", 199))

	def test_200(self):
		self.assertTrue(TestLexer.test('''## V9:GXkA0&PbnD''', '''<EOF>''', 200))
