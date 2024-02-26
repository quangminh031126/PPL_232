import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
	def testCase101(self):
		self.assertTrue(TestLexer.test("639.981", "639.981,<EOF>", 101))

	def testCase102(self):
		self.assertTrue(TestLexer.test("64.507", "64.507,<EOF>", 102))

	def testCase103(self):
		self.assertTrue(TestLexer.test("118e-50", "118e-50,<EOF>", 103))

	def testCase104(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 104))

	def testCase105(self):
		self.assertTrue(TestLexer.test('''"'"\\h>}"''', '''Illegal Escape In String: '"\\h''', 105))

	def testCase106(self):
		self.assertTrue(TestLexer.test("527.288E-03", "527.288E-03,<EOF>", 106))

	def testCase107(self):
		self.assertTrue(TestLexer.test('''"SHK'"\\y'""''', '''Illegal Escape In String: SHK'"\\y''', 107))

	def testCase108(self):
		self.assertTrue(TestLexer.test('''## TSy-9''', '''<EOF>''', 108))

	def testCase109(self):
		self.assertTrue(TestLexer.test('''## w%)Kqlhp(U#`37E6_d''', '''<EOF>''', 109))

	def testCase110(self):
		self.assertTrue(TestLexer.test("73oHGMgays", "73,oHGMgays,<EOF>", 110))

	def testCase111(self):
		self.assertTrue(TestLexer.test('''## P/.*vxf2(T''', '''<EOF>''', 111))

	def testCase112(self):
		self.assertTrue(TestLexer.test("knT", "knT,<EOF>", 112))

	def testCase113(self):
		self.assertTrue(TestLexer.test("990.110e89", "990.110e89,<EOF>", 113))

	def testCase114(self):
		self.assertTrue(TestLexer.test("H", "H,<EOF>", 114))

	def testCase115(self):
		self.assertTrue(TestLexer.test('''## N+(8:Q4,E''', '''<EOF>''', 115))

	def testCase116(self):
		self.assertTrue(TestLexer.test("791.577", "791.577,<EOF>", 116))

	def testCase117(self):
		self.assertTrue(TestLexer.test('''## r,(HibfN;liQS8$E@5''', '''<EOF>''', 117))

	def testCase118(self):
		self.assertTrue(TestLexer.test('''## AlST(;K5''', '''<EOF>''', 118))

	def testCase119(self):
		self.assertTrue(TestLexer.test("uECICt", "uECICt,<EOF>", 119))

	def testCase120(self):
		self.assertTrue(TestLexer.test('''"'" ''', '''Unclosed String: '" ''', 120))

	def testCase121(self):
		self.assertTrue(TestLexer.test("5e-29", "5e-29,<EOF>", 121))

	def testCase122(self):
		self.assertTrue(TestLexer.test('''## D<k/8-~mI[YCZ''', '''<EOF>''', 122))

	def testCase123(self):
		self.assertTrue(TestLexer.test("SJF", "SJF,<EOF>", 123))

	def testCase124(self):
		self.assertTrue(TestLexer.test("4E84", "4E84,<EOF>", 124))

	def testCase125(self):
		self.assertTrue(TestLexer.test('''## -~|0FV@:Ls60!''', '''<EOF>''', 125))

	def testCase126(self):
		self.assertTrue(TestLexer.test('''## ?5Z''', '''<EOF>''', 126))

	def testCase127(self):
		self.assertTrue(TestLexer.test("155.660E-42", "155.660E-42,<EOF>", 127))

	def testCase128(self):
		self.assertTrue(TestLexer.test('''"'"'"'""''', '''\'"'"'",<EOF>''', 128))

	def testCase129(self):
		self.assertTrue(TestLexer.test("67", "67,<EOF>", 129))

	def testCase130(self):
		self.assertTrue(TestLexer.test('''"'""''', '''\'",<EOF>''', 130))

	def testCase131(self):
		self.assertTrue(TestLexer.test('''"'"'"
'""''', '''Unclosed String: '"'"''', 131))

	def testCase132(self):
		self.assertTrue(TestLexer.test('''"'""''', '''\'",<EOF>''', 132))

	def testCase133(self):
		self.assertTrue(TestLexer.test('''## PvZ:N&''', '''<EOF>''', 133))

	def testCase134(self):
		self.assertTrue(TestLexer.test('''"'"B'"5"''', '''\'"B'"5,<EOF>''', 134))

	def testCase135(self):
		self.assertTrue(TestLexer.test('''## c5Cw1OUU)&~GOMB''', '''<EOF>''', 135))

	def testCase136(self):
		self.assertTrue(TestLexer.test("cyHKFcIr", "cyHKFcIr,<EOF>", 136))

	def testCase137(self):
		self.assertTrue(TestLexer.test("Z7", "Z7,<EOF>", 137))

	def testCase138(self):
		self.assertTrue(TestLexer.test("0.364E56", "0.364E56,<EOF>", 138))

	def testCase139(self):
		self.assertTrue(TestLexer.test('''"S'"4'" ''', '''Unclosed String: S'"4'" ''', 139))

	def testCase140(self):
		self.assertTrue(TestLexer.test('''## -1BOb*&pqfO5kWqaB''', '''<EOF>''', 140))

	def testCase141(self):
		self.assertTrue(TestLexer.test("KT2tomQiJ", "KT2tomQiJ,<EOF>", 141))

	def testCase142(self):
		self.assertTrue(TestLexer.test("ecK", "ecK,<EOF>", 142))

	def testCase143(self):
		self.assertTrue(TestLexer.test('''"'"
!"''', '''Unclosed String: '"''', 143))

	def testCase144(self):
		self.assertTrue(TestLexer.test("0", "0,<EOF>", 144))

	def testCase145(self):
		self.assertTrue(TestLexer.test("poxhQtYuO", "poxhQtYuO,<EOF>", 145))

	def testCase146(self):
		self.assertTrue(TestLexer.test("1", "1,<EOF>", 146))

	def testCase147(self):
		self.assertTrue(TestLexer.test('''"'")"''', '''\'"),<EOF>''', 147))

	def testCase148(self):
		self.assertTrue(TestLexer.test("10e-36", "10e-36,<EOF>", 148))

	def testCase149(self):
		self.assertTrue(TestLexer.test('''## 04HZ%lQLJ7TE.$X''', '''<EOF>''', 149))

	def testCase150(self):
		self.assertTrue(TestLexer.test("52.410E95", "52.410E95,<EOF>", 150))

	def testCase151(self):
		self.assertTrue(TestLexer.test("4.090e41", "4.090e41,<EOF>", 151))

	def testCase152(self):
		self.assertTrue(TestLexer.test("93.032", "93.032,<EOF>", 152))

	def testCase153(self):
		self.assertTrue(TestLexer.test("w2x", "w2x,<EOF>", 153))

	def testCase154(self):
		self.assertTrue(TestLexer.test("yT$JEWSz", "yT,Error Token $", 154))

	def testCase155(self):
		self.assertTrue(TestLexer.test('''## MZ/%9,s''', '''<EOF>''', 155))

	def testCase156(self):
		self.assertTrue(TestLexer.test("f@vWmreV2", "f,Error Token @", 156))

	def testCase157(self):
		self.assertTrue(TestLexer.test("8", "8,<EOF>", 157))

	def testCase158(self):
		self.assertTrue(TestLexer.test('''"x'"~e3"''', '''x'"~e3,<EOF>''', 158))

	def testCase159(self):
		self.assertTrue(TestLexer.test("99.865e02", "99.865e02,<EOF>", 159))

	def testCase160(self):
		self.assertTrue(TestLexer.test("MVojDZ0uf", "MVojDZ0uf,<EOF>", 160))

	def testCase161(self):
		self.assertTrue(TestLexer.test('''## =C> e&)_Ym/~"vTG''', '''<EOF>''', 161))

	def testCase162(self):
		self.assertTrue(TestLexer.test('''"'"'"
z"''', '''Unclosed String: '"'"''', 162))

	def testCase163(self):
		self.assertTrue(TestLexer.test("Yxkd8EuqQ6", "Yxkd8EuqQ6,<EOF>", 163))

	def testCase164(self):
		self.assertTrue(TestLexer.test("0.166E11", "0.166E11,<EOF>", 164))

	def testCase165(self):
		self.assertTrue(TestLexer.test('''## 8''', '''<EOF>''', 165))

	def testCase166(self):
		self.assertTrue(TestLexer.test("bNq", "bNq,<EOF>", 166))

	def testCase167(self):
		self.assertTrue(TestLexer.test('''## ;GATv(Q"BQ4R5}nxi%)''', '''<EOF>''', 167))

	def testCase168(self):
		self.assertTrue(TestLexer.test('''"Wo'"'"'""''', '''Wo'"'"'",<EOF>''', 168))

	def testCase169(self):
		self.assertTrue(TestLexer.test("87e-03", "87e-03,<EOF>", 169))

	def testCase170(self):
		self.assertTrue(TestLexer.test("90", "90,<EOF>", 170))

	def testCase171(self):
		self.assertTrue(TestLexer.test('''## 3_/Cu@yW|eR6lb`""`l''', '''<EOF>''', 171))

	def testCase172(self):
		self.assertTrue(TestLexer.test("70E+09", "70E+09,<EOF>", 172))

	def testCase173(self):
		self.assertTrue(TestLexer.test("gffrS", "gffrS,<EOF>", 173))

	def testCase174(self):
		self.assertTrue(TestLexer.test("31e38", "31e38,<EOF>", 174))

	def testCase175(self):
		self.assertTrue(TestLexer.test("4e09", "4e09,<EOF>", 175))

	def testCase176(self):
		self.assertTrue(TestLexer.test('''## PoSRo&t''', '''<EOF>''', 176))

	def testCase177(self):
		self.assertTrue(TestLexer.test("RSz#d4RGZg", "RSz,Error Token #", 177))

	def testCase178(self):
		self.assertTrue(TestLexer.test('''## %''', '''<EOF>''', 178))

	def testCase179(self):
		self.assertTrue(TestLexer.test("08Z4", "08,Z4,<EOF>", 179))

	def testCase180(self):
		self.assertTrue(TestLexer.test("rn8Lw04Um", "rn8Lw04Um,<EOF>", 180))

	def testCase181(self):
		self.assertTrue(TestLexer.test("3", "3,<EOF>", 181))

	def testCase182(self):
		self.assertTrue(TestLexer.test('''## `Sr~P}EYvK''', '''<EOF>''', 182))

	def testCase183(self):
		self.assertTrue(TestLexer.test('''## XB~st@4&_P)#)`KIJ''', '''<EOF>''', 183))

	def testCase184(self):
		self.assertTrue(TestLexer.test("gfK01hwA", "gfK01hwA,<EOF>", 184))

	def testCase185(self):
		self.assertTrue(TestLexer.test("kfIK57@", "kfIK57,Error Token @", 185))

	def testCase186(self):
		self.assertTrue(TestLexer.test("206E-22", "206E-22,<EOF>", 186))

	def testCase187(self):
		self.assertTrue(TestLexer.test("492e+93", "492e+93,<EOF>", 187))

	def testCase188(self):
		self.assertTrue(TestLexer.test("oIPOW0$t&l", "oIPOW0,Error Token $", 188))

	def testCase189(self):
		self.assertTrue(TestLexer.test("g", "g,<EOF>", 189))

	def testCase190(self):
		self.assertTrue(TestLexer.test('''## k;`2jT:7cailWo13I`''', '''<EOF>''', 190))

	def testCase191(self):
		self.assertTrue(TestLexer.test("^7hY", "Error Token ^", 191))

	def testCase192(self):
		self.assertTrue(TestLexer.test('''"'";'"'""''', '''\'";'"'",<EOF>''', 192))

	def testCase193(self):
		self.assertTrue(TestLexer.test('''"\\ge'""''', '''Illegal Escape In String: \\g''', 193))

	def testCase194(self):
		self.assertTrue(TestLexer.test("6.180E11", "6.180E11,<EOF>", 194))

	def testCase195(self):
		self.assertTrue(TestLexer.test('''"\\c%T'"'""''', '''Illegal Escape In String: \\c''', 195))

	def testCase196(self):
		self.assertTrue(TestLexer.test('''## $]?z|{;''', '''<EOF>''', 196))

	def testCase197(self):
		self.assertTrue(TestLexer.test("2", "2,<EOF>", 197))

	def testCase198(self):
		self.assertTrue(TestLexer.test("21.849", "21.849,<EOF>", 198))

	def testCase199(self):
		self.assertTrue(TestLexer.test('''## Ml/<iV/xE2O<XT`&jBT1''', '''<EOF>''', 199))

	def testCase200(self):
		self.assertTrue(TestLexer.test("857.289e-44", "857.289e-44,<EOF>", 200))
