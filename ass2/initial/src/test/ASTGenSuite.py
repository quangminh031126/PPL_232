import unittest
from TestUtils import TestAST
from main.zcode.utils.AST import *

class ASTGenSuite(unittest.TestCase):
	def test_301(self):
		input = '''
func qFY (bool Kw, bool y2[52.051E39], dynamic UQi[62.137E-78])	begin
		## v|XuJ tJ
		## ]
		## 9BnV:e]1V"_{.
	end
'''
		expect = '''Program([])'''
		self.assertTrue(TestAST.test(input, expect, 301))

	def test_302(self):
		input = '''
bool Pd[813.764E+38,27.147E28] <- not - QND() = [IN, lh] ## _I $F]F+uL{Xi_GfC[r
string Mm6n[6.918E-15] ## {@g-(7?)E4SPi*v
'''
		expect = '''Program([VarDecl(Id(Pd), ArrayType([8.13764e+40, 2.7147e+29], BoolType), None, BinaryOp(=, UnaryOp(not, UnaryOp(-, CallExpr(Id(QND), []))), ArrayLit(Id(IN), Id(lh)))), VarDecl(Id(Mm6n), ArrayType([6.918e-15], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 302))

	def test_303(self):
		input = '''
## d( >pXT.3jl{+m
string vMZ ## 9fr|f1_kr0K0&`Aj4
## t?mB+I.fn4zZk
func q1 (string dOsV[3.927,516])	return

'''
		expect = '''Program([VarDecl(Id(vMZ), StringType, None, None), FuncDecl(Id(q1), [VarDecl(Id(dOsV), ArrayType([3.927, 516.0], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 303))

	def test_304(self):
		input = '''
func xBTS (number Oss, number DAS)
	return aojN
number ZkWL ## `cmRyv 10)
var Fuc[78.552,1.195E-76] ## A 9>PQ`xOw
'''
		expect = '''Program([FuncDecl(Id(xBTS), [VarDecl(Id(Oss), NumberType, None, None), VarDecl(Id(DAS), NumberType, None, None)], None), Return(Id(aojN)), VarDecl(Id(ZkWL), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 304))

	def test_305(self):
		input = '''
func Z6u (bool Xx, bool Sm[32])
	return

func f7 (number ve[2.511e+76,846.170e10])
	return D0c
'''
		expect = '''Program([FuncDecl(Id(Z6u), [VarDecl(Id(Xx), BoolType, None, None), VarDecl(Id(Sm), ArrayType([32.0], BoolType), None, None)], Return()), FuncDecl(Id(f7), [VarDecl(Id(ve), ArrayType([2.511e+76, 8461700000000.0], NumberType), None, None)], Return(Id(D0c)))])'''
		self.assertTrue(TestAST.test(input, expect, 305))

	def test_306(self):
		input = '''
func mGe (bool q_T0)	begin
	end

'''
		expect = '''Program([FuncDecl(Id(mGe), [VarDecl(Id(q_T0), BoolType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 306))

	def test_307(self):
		input = '''
func viI ()
	begin
		## Dd
	end

func cgs (dynamic tn0c)	begin
		return
	end

number CJYu[10.486E77] <- 7E-90 ## |i!+O/Q
'''
		expect = '''Program([FuncDecl(Id(viI), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 307))

	def test_308(self):
		input = '''
## K2q
## KNeG^%6
'''
		expect = '''Program([])'''
		self.assertTrue(TestAST.test(input, expect, 308))

	def test_309(self):
		input = '''
func NNYm ()	return

## <7YK-X[SC8z+Xa|AIBj
func Gp ()	begin
		number bHGf[929.037e65,57.547E59]
		continue
	end

string c3[299,12] ## 2~EHo1pmI&a
'''
		expect = '''Program([FuncDecl(Id(NNYm), [], Return()), FuncDecl(Id(Gp), [], Block([VarDecl(Id(bHGf), ArrayType([9.29037e+67, 5.7547e+60], NumberType), None, None), Continue])), VarDecl(Id(c3), ArrayType([299.0, 12.0], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 309))

	def test_310(self):
		input = '''
var X1R
## YaK
## %1v6#M@`9M7-p )F
string si ## kgtJ}
dynamic TCoa ## Vv4L9d.oz"{
'''
		expect = '''Program([])'''
		self.assertTrue(TestAST.test(input, expect, 310))

	def test_311(self):
		input = '''
func E1Y (bool CMr)	return uo

var hL2 <- Vc
'''
		expect = '''Program([FuncDecl(Id(E1Y), [VarDecl(Id(CMr), BoolType, None, None)], Return(Id(uo))), VarDecl(Id(hL2), None, var, Id(Vc))])'''
		self.assertTrue(TestAST.test(input, expect, 311))

	def test_312(self):
		input = '''
var zRh ## 9O9qLRjM"L?u{
func ID (number Jn[96.516E+74,6e+07], bool HiA[1.260E84,325E00])
	return

var cP[760,632.601,34] ## 7wLdV1iVYtC63G@vEvr
func lC (bool BtC0[327.178e-96,2.425e-75], dynamic GT[6.527E+70])
	return

'''
		expect = '''Program([])'''
		self.assertTrue(TestAST.test(input, expect, 312))

	def test_313(self):
		input = '''
dynamic Wzv[99.826E91] ## M_PM,GfL;j(Mm$"}Xwl
'''
		expect = '''Program([VarDecl(Id(Wzv), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 313))

	def test_314(self):
		input = '''
func ezP (var hBq2, dynamic kBNM)
	return
## uOy)[WYm|?nWR7<<Vfi
number Sj ## lW+RIW?U
## P-X4iO5K2RntVa
func SMo (bool vht9[5.932E+32,250.626e-92,843.974e+60], number qX[54.786e-65,3.575e-38])	return "zRD"

'''
		expect = '''Program([])'''
		self.assertTrue(TestAST.test(input, expect, 314))

	def test_315(self):
		input = '''
## !P7K{1:9*
func j_r ()
	begin
	end
## z>a
## hG5#gF6(I.!2{SA
'''
		expect = '''Program([FuncDecl(Id(j_r), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 315))

	def test_316(self):
		input = '''
func KXpC (dynamic XAoU, dynamic GI[220,66.469], var pw)
	return
'''
		expect = '''Program([])'''
		self.assertTrue(TestAST.test(input, expect, 316))

	def test_317(self):
		input = '''
func nfB4 ()
	return
'''
		expect = '''Program([FuncDecl(Id(nfB4), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 317))

	def test_318(self):
		input = '''
## 7p]K
## ?`z8lNm.hN
func DV59 (bool ZI2, dynamic P2EC[70,349e+01,2.192], number XTnn[8E61])	return
func NOv ()
	return ")'""

'''
		expect = '''Program([])'''
		self.assertTrue(TestAST.test(input, expect, 318))

	def test_319(self):
		input = '''
## hE<OJ
## Pz#ymD:A1V&z8
dynamic gcV[55e-96,9]
'''
		expect = '''Program([VarDecl(Id(gcV), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 319))

	def test_320(self):
		input = '''
func gQ6 ()	return
func KzX ()	begin
		## sTw?<K
	end

func TG3I (var mI[1.412E-61], bool zjSN[814.028,172])
	begin
		## rVAgV(pXc^H>JI
		number hB4[360.542e+54,33.312E-15] <- true
		## ?B8g*
	end
string NGUT[517e82,66,998] <- 2E36
'''
		expect = '''Program([FuncDecl(Id(gQ6), [], Return()), FuncDecl(Id(KzX), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 320))

	def test_321(self):
		input = '''
func tZ ()	return

func fU ()
	begin
		fQCN("K3'"'"", 36.788e-61, 668.977)
		## v2~lR
		return
	end

'''
		expect = '''Program([FuncDecl(Id(tZ), [], Return()), FuncDecl(Id(fU), [], Block([CallStmt(Id(fQCN), [StringLit(K3'"'"), NumLit(3.6788e-60), NumLit(668.977)]), Return()]))])'''
		self.assertTrue(TestAST.test(input, expect, 321))

	def test_322(self):
		input = '''
func YC (number gco[935.799,911,72E-26], string LzFf)	return
number Z_dP ## JYdl)/`"
'''
		expect = '''Program([FuncDecl(Id(YC), [VarDecl(Id(gco), ArrayType([935.799, 911.0, 7.2e-25], NumberType), None, None), VarDecl(Id(LzFf), StringType, None, None)], Return()), VarDecl(Id(Z_dP), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 322))

	def test_323(self):
		input = '''
## .NJ#xO.rIC_*
number pS ## (i 6"na`$
## jjuei>>i
'''
		expect = '''Program([VarDecl(Id(pS), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 323))

	def test_324(self):
		input = '''
func y6 (string WDfk, bool LJ, var J12[1E-32,1e-42])
	return

'''
		expect = '''Program([])'''
		self.assertTrue(TestAST.test(input, expect, 324))

	def test_325(self):
		input = '''
## Vh4`f"+,9~3+9W556|Bx
var pjyy
func AN (string gjMt[125.784e94,4e-77,179])	begin
		for Q2 until 2 by 93.098
			RG2L(true, "51", Jjs)
		## d)tNhF^Ye
		dynamic yGSr[68e01,2.922E90,57.008] ## [uU6
	end
## $Y-)g>Ij!F&%uXS
'''
		expect = '''Program([])'''
		self.assertTrue(TestAST.test(input, expect, 325))

	def test_326(self):
		input = '''
string AdO[85.227,57,834.831e29] ## WY/s&+{=
'''
		expect = '''Program([VarDecl(Id(AdO), ArrayType([85.227, 57.0, 8.34831e+31], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 326))

	def test_327(self):
		input = '''
var qWpj[2e+77] ## _F5O_
func Po (number LOE, dynamic go[2,497E+71])	begin
	end
func Vsy (bool ezOq, var I_cW, number zp8s[263.772e25,923e+88])
	begin
		bool K2_[3.879,890e-45,31e-26] <- fL1r
		continue
		## (~<|I*{>)(Z8}kAh"U
	end

string eSYb[13.045E00] <- "'"}'"#'"" ## |C7Kva+JP}69lNVUiK
'''
		expect = '''Program([])'''
		self.assertTrue(TestAST.test(input, expect, 327))

	def test_328(self):
		input = '''
func fnd ()
	begin
	end
'''
		expect = '''Program([FuncDecl(Id(fnd), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 328))

	def test_329(self):
		input = '''
func XiSb (bool TOTt[63.907e09], bool AIYP[67.605e12], dynamic ss[76,4E-60])	return
func wryq (var EAX[0E63,70e22], dynamic lvAR)	return
func yXy (number FbH)	return "'"'"'""

'''
		expect = '''Program([])'''
		self.assertTrue(TestAST.test(input, expect, 329))

	def test_330(self):
		input = '''
func w_ (dynamic COv5)	return
'''
		expect = '''Program([])'''
		self.assertTrue(TestAST.test(input, expect, 330))

	def test_331(self):
		input = '''
func rM ()
	return "6'"'"n("

number CuSD ## a 
bool Mr[65.879e75] ## }tsLTd-C sb3l6p
func FYNA (string Lpkb, dynamic JVj[105,4.767], dynamic mdm[555.392,243.469])	return WzB

'''
		expect = '''Program([FuncDecl(Id(rM), [], None), Return(StringLit(6'"'"n()), VarDecl(Id(CuSD), NumberType, None, None), VarDecl(Id(Mr), ArrayType([6.5879e+76], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 331))

	def test_332(self):
		input = '''
bool RAk
## TaJY
func Pgfd (number Bf[96,5], bool UPrQ, bool Kc_g[516.461e-27,94,21.093e67])
	begin
		## <n
		for MPs until wZJf by false
			qrxl(6E59, "'"O", 36.209E37)
	end

## =}q{Zxc!^@~N+OER.^?}
'''
		expect = '''Program([VarDecl(Id(RAk), BoolType, None, None), FuncDecl(Id(Pgfd), [VarDecl(Id(Bf), ArrayType([96.0, 5.0], NumberType), None, None), VarDecl(Id(UPrQ), BoolType, None, None), VarDecl(Id(Kc_g), ArrayType([5.16461e-25, 94.0, 2.1093e+68], BoolType), None, None)], Block([For(Id(MPs), Id(wZJf), BooleanLit(False), CallStmt(Id(qrxl), [NumLit(6e+59), StringLit('"O), NumLit(3.6209e+38)]))]))])'''
		self.assertTrue(TestAST.test(input, expect, 332))

	def test_333(self):
		input = '''
func PYN (string pRf, number WC, dynamic HZQW[363e+65,52.040,77])
	begin
	end
## L-S[$%3$QoeYDEDW!z.A
## }LZL$9:AR+E7(jF.jR$Y
'''
		expect = '''Program([])'''
		self.assertTrue(TestAST.test(input, expect, 333))

	def test_334(self):
		input = '''
func nUNM (bool YO[96E-42,72E+39,68e-78])	return
'''
		expect = '''Program([FuncDecl(Id(nUNM), [VarDecl(Id(YO), ArrayType([9.6e-41, 7.2e+40, 6.8e-77], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 334))

	def test_335(self):
		input = '''
## 9c42-"K#c
func Lwy (dynamic Dvh[719,99.616e+97,9E26], string OW[65e+35], dynamic uKG)	begin
		Aq(true, gC, "`e'"")
	end
func fdK (string H0bP)
	return

'''
		expect = '''Program([])'''
		self.assertTrue(TestAST.test(input, expect, 335))

	def test_336(self):
		input = '''
## lhM
number VIKB[1E82] ## 0hPy(xiGn$U<ac%u
func vqKC (string L9[37.933E+88,230.891e-57,8.040], bool Ve9)
	begin
		## "04Q33#)P.](bsztTH
	end

'''
		expect = '''Program([VarDecl(Id(VIKB), ArrayType([1e+82], NumberType), None, None), FuncDecl(Id(vqKC), [VarDecl(Id(L9), ArrayType([3.7933e+89, 2.30891e-55, 8.04], StringType), None, None), VarDecl(Id(Ve9), BoolType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 336))

	def test_337(self):
		input = '''
string Ec1
func aE (string LbIy[772,1.686e-11,65.560e77], bool e_I, var SW[502.826])
	return

## bM9*O>LfC[|h8 0z7y!
## W9JEyPo
'''
		expect = '''Program([VarDecl(Id(Ec1), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 337))

	def test_338(self):
		input = '''
func rQ1 (var PSTQ[96.409E-35])	begin
	end

'''
		expect = '''Program([])'''
		self.assertTrue(TestAST.test(input, expect, 338))

	def test_339(self):
		input = '''
## 7q(4^+5^[Ra[H=?fcI
dynamic Xz <- "'"2'"" ## TPb/fE
## =ByD7sc6!jZ/FX
## 0E<NG?q+ukyf=C
func xo_K ()	begin
	end

'''
		expect = '''Program([VarDecl(Id(Xz), None, dynamic, StringLit('"2'")), FuncDecl(Id(xo_K), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 339))

	def test_340(self):
		input = '''
func oTuQ ()
	return 9
## >n,Nl{2p)E
var Sb[682E+10] <- XT ## ")G^A_,az[!gzO
## + 4H6uZkt
'''
		expect = '''Program([FuncDecl(Id(oTuQ), [], Return(NumLit(9.0)))])'''
		self.assertTrue(TestAST.test(input, expect, 340))

	def test_341(self):
		input = '''
func o3 ()
	begin
		number tr <- false ## .YIb=BES7[[@..qy
		## }! kQt^q7fBZ
		## ^k2
	end
number WA <- qw ##  +#.[0*M
number P6 ## F+t:GZr"xrQ_wHfPzyha
## 0fxS3QA~5bH
## 2hE*_gh}k!{ZV,s!C
'''
		expect = '''Program([FuncDecl(Id(o3), [], Block([VarDecl(Id(tr), NumberType, None, BooleanLit(False))])), VarDecl(Id(WA), NumberType, None, Id(qw)), VarDecl(Id(P6), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 341))

	def test_342(self):
		input = '''
## Iss^q6zfxXZ|[1KPW|5[
'''
		expect = '''Program([])'''
		self.assertTrue(TestAST.test(input, expect, 342))

	def test_343(self):
		input = '''
## OG3GMG=/P4+Yv
string fI ## FO]1?/5-oX$UY<sv+
## nyhaXZ
var ekK ## ZjwnEkC5z4RX&=]vc0
## KsFm0GaQE.3H>N>Iy>
'''
		expect = '''Program([VarDecl(Id(fI), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 343))

	def test_344(self):
		input = '''
func ygPK ()
	return qZCM
number nRL <- 0e-99 ## >8bKX;=y6
'''
		expect = '''Program([FuncDecl(Id(ygPK), [], Return(Id(qZCM))), VarDecl(Id(nRL), NumberType, None, NumLit(0.0))])'''
		self.assertTrue(TestAST.test(input, expect, 344))

	def test_345(self):
		input = '''
## dsEdm?"7y-Q!
bool J7D[9.810,246.481] ## B*[@|^kicTKHO1MAh
func sb ()
	return "q'""

func WUM (number Ru[3.641,942.128E-40], bool WV, bool dLS[7.991,77.046])
	return "6I'"'"'""
func Yh2 ()	return false

'''
		expect = '''Program([VarDecl(Id(J7D), ArrayType([9.81, 246.481], BoolType), None, None), FuncDecl(Id(sb), [], Return(StringLit(q'"))), FuncDecl(Id(WUM), [VarDecl(Id(Ru), ArrayType([3.641, 9.42128e-38], NumberType), None, None), VarDecl(Id(WV), BoolType, None, None), VarDecl(Id(dLS), ArrayType([7.991, 77.046], BoolType), None, None)], Return(StringLit(6I'"'"'"))), FuncDecl(Id(Yh2), [], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 345))

	def test_346(self):
		input = '''
func MaSL (dynamic RJ[483.567,0E14,32.377])	return

dynamic oG
var T95 <- "f'"-"
'''
		expect = '''Program([])'''
		self.assertTrue(TestAST.test(input, expect, 346))

	def test_347(self):
		input = '''
func Xk (number eB7)
	return
bool KD[73e+79,561] <- DB
'''
		expect = '''Program([FuncDecl(Id(Xk), [VarDecl(Id(eB7), NumberType, None, None)], Return()), VarDecl(Id(KD), ArrayType([7.3e+80, 561.0], BoolType), None, Id(DB))])'''
		self.assertTrue(TestAST.test(input, expect, 347))

	def test_348(self):
		input = '''
dynamic m_ <- 0.395 ## Oce83O9b8]2x:{9}ZU
## FWqkTxr_
'''
		expect = '''Program([VarDecl(Id(m_), None, dynamic, NumLit(0.395))])'''
		self.assertTrue(TestAST.test(input, expect, 348))

	def test_349(self):
		input = '''
## #7KQNaPZOUtY
number RW3S
var Gbb ## >=z?8_b?<^(MF`nxj@N4
dynamic Orm8
func tjQ (string j7)
	return

'''
		expect = '''Program([VarDecl(Id(RW3S), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 349))

	def test_350(self):
		input = '''
func yC ()
	return

'''
		expect = '''Program([FuncDecl(Id(yC), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 350))

	def test_351(self):
		input = '''
func hTz0 (string wf2[91,73,14], dynamic g1P2)
	return

func YTd (bool ncNX[26.042,3.329,13], number hGms[993], number bNQ)
	begin
	end

func iPHy (number yDi, string ZJ[598.001])
	return

bool GQ[568.593,3.911e-33,4.228E-71] <- false ## l7e>*b4EQli1z
'''
		expect = '''Program([])'''
		self.assertTrue(TestAST.test(input, expect, 351))

	def test_352(self):
		input = '''
func y_ ()
	return true
## J5U^i6Q+W8
func Cv (number dkJ4[249])
	return
## &"x^&Vaq8
'''
		expect = '''Program([FuncDecl(Id(y_), [], Return(BooleanLit(True))), FuncDecl(Id(Cv), [VarDecl(Id(dkJ4), ArrayType([249.0], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 352))

	def test_353(self):
		input = '''
## tH>9c7v0Y,94-S9>fVN
func X8l (number OXX, dynamic Rw7[9,3.421], var EGA_)
	return

'''
		expect = '''Program([])'''
		self.assertTrue(TestAST.test(input, expect, 353))

	def test_354(self):
		input = '''
func hFc (number KS[0.060E77,7.137,276.760], var Zg)
	begin
		ws(lR2, t6I6, y4)
	end
## U
var SQ[783e08,381E-90] <- false
'''
		expect = '''Program([])'''
		self.assertTrue(TestAST.test(input, expect, 354))

	def test_355(self):
		input = '''
## ]M}L",6*aBmn0A9~0z7~
dynamic WKd
'''
		expect = '''Program([VarDecl(Id(WKd), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 355))

	def test_356(self):
		input = '''
func D70e (var cP[92.218])	return
## dV=sXh%9F
'''
		expect = '''Program([])'''
		self.assertTrue(TestAST.test(input, expect, 356))

	def test_357(self):
		input = '''
## <!`y, k.-f2SZe
'''
		expect = '''Program([])'''
		self.assertTrue(TestAST.test(input, expect, 357))

	def test_358(self):
		input = '''
var AbL[9E16] <- true
'''
		expect = '''Program([])'''
		self.assertTrue(TestAST.test(input, expect, 358))

	def test_359(self):
		input = '''
number gJgj
'''
		expect = '''Program([VarDecl(Id(gJgj), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 359))

	def test_360(self):
		input = '''
## ~s7Us(|_$,T#3
var MUG[6] ## -S
## coi%
func wi (number OAHO, bool dF[28])
	return N5
var rNKM ## r
'''
		expect = '''Program([])'''
		self.assertTrue(TestAST.test(input, expect, 360))

	def test_361(self):
		input = '''
func uLj (bool WC, dynamic tQqx)	begin
		continue
		## Hr+:/N]@JAo=[
		## =*n0jRr0Ogt5
	end

'''
		expect = '''Program([])'''
		self.assertTrue(TestAST.test(input, expect, 361))

	def test_362(self):
		input = '''
## 2j
bool Gtiv ##  Mj?zlS>]+`gI
func vO (bool ntCd, var Ls[7])
	begin
		## y!lMXz
		## |UY!zZjBGX3YnFKi7>{
	end

'''
		expect = '''Program([VarDecl(Id(Gtiv), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 362))

	def test_363(self):
		input = '''
func Em (number sB4, string pjS, string p_pO[717E+91])
	begin
		ts <- ah2
		## &.iFs`1[Xn?3Ae=8c
		## I;7jP
	end
## |]"Z+EU)
dynamic ghDQ <- "'"'"'"JY"
func xsQ (string hi)	return
func OXcJ (number eZ[98e30], var JOSF)
	begin
		## Y!MS]Pq=Lv&-#WXGwY{<
		## Bz#Y!Kj-unt"u
	end

'''
		expect = '''Program([FuncDecl(Id(Em), [VarDecl(Id(sB4), NumberType, None, None), VarDecl(Id(pjS), StringType, None, None), VarDecl(Id(p_pO), ArrayType([7.17e+93], StringType), None, None)], None), Block([AssignStmt(Id(ts), Id(ah2))]), VarDecl(Id(ghDQ), None, dynamic, StringLit('"'"'"JY)), FuncDecl(Id(xsQ), [VarDecl(Id(hi), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 363))

	def test_364(self):
		input = '''
func AFkR ()	begin
		return true
		## <tR0x
		## d[)sCa)0iqg:(_Qfz>
	end

var wEg[3,96.713E26,61] <- 408.241 ## J2}lO{-3jd34>ohSTm
'''
		expect = '''Program([FuncDecl(Id(AFkR), [], Block([Return(BooleanLit(True))]))])'''
		self.assertTrue(TestAST.test(input, expect, 364))

	def test_365(self):
		input = '''
func vVpz ()
	return

number B41t[8,4.176,53.944E75]
'''
		expect = '''Program([FuncDecl(Id(vVpz), [], Return()), VarDecl(Id(B41t), ArrayType([8.0, 4.176, 5.3944e+76], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 365))

	def test_366(self):
		input = '''
number Aonw <- Psu ## GqZBI>
func Ei (bool z9iZ[132e-58,44.454e-84,10e+78], var qS[887,9.730e06,66], dynamic au7W[62e95,44,61])
	return

## z-?.
'''
		expect = '''Program([VarDecl(Id(Aonw), NumberType, None, Id(Psu))])'''
		self.assertTrue(TestAST.test(input, expect, 366))

	def test_367(self):
		input = '''
## hpa_cGE|G)*My
func xMzW (bool dCrA[7E86], dynamic G6[0,779])
	return 6

'''
		expect = '''Program([])'''
		self.assertTrue(TestAST.test(input, expect, 367))

	def test_368(self):
		input = '''
## F=l2uq#By
## XLS69"lQc!Bv+1Y<FN9M
bool SlG3[17,94e69] <- "'"7'";<" ## k0{+TKj*lbS|k8X
'''
		expect = '''Program([VarDecl(Id(SlG3), ArrayType([17.0, 9.4e+70], BoolType), None, StringLit('"7'";<))])'''
		self.assertTrue(TestAST.test(input, expect, 368))

	def test_369(self):
		input = '''
bool b9Lc <- SW ## D1
func OQU ()	return Z1

## )-;MbcP;)jb
## 1;#>A<m+N6rWeSz
number MLmj[33E+71] ## wa
'''
		expect = '''Program([VarDecl(Id(b9Lc), BoolType, None, Id(SW)), FuncDecl(Id(OQU), [], Return(Id(Z1))), VarDecl(Id(MLmj), ArrayType([3.3e+72], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 369))

	def test_370(self):
		input = '''
func NQEJ (bool oeiF, var Wfdk[41E+62])	begin
	end
'''
		expect = '''Program([])'''
		self.assertTrue(TestAST.test(input, expect, 370))

	def test_371(self):
		input = '''
## QS$0
'''
		expect = '''Program([])'''
		self.assertTrue(TestAST.test(input, expect, 371))

	def test_372(self):
		input = '''
## +-
var jS <- VN
## P&f0r@b+)
## DV/xJyh#$Qz
func wcWy (dynamic RnpL[405,0.153E92])
	return
'''
		expect = '''Program([VarDecl(Id(jS), None, var, Id(VN))])'''
		self.assertTrue(TestAST.test(input, expect, 372))

	def test_373(self):
		input = '''
dynamic b39 <- mBn
'''
		expect = '''Program([VarDecl(Id(b39), None, dynamic, Id(mBn))])'''
		self.assertTrue(TestAST.test(input, expect, 373))

	def test_374(self):
		input = '''
## u[cmU*C
number R_P1[7.353]
## z?5T=k",fQYvKg
bool FHs[27e93] ## ^1gKogB!t
## `EhsEJ$sS-^*((VqCV!]
'''
		expect = '''Program([VarDecl(Id(R_P1), ArrayType([7.353], NumberType), None, None), VarDecl(Id(FHs), ArrayType([2.7e+94], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 374))

	def test_375(self):
		input = '''
## s)>n/JAGdlB?FcQ(~
func GMZQ ()
	return

bool RLP <- "^%sL"
'''
		expect = '''Program([FuncDecl(Id(GMZQ), [], Return()), VarDecl(Id(RLP), BoolType, None, StringLit(^%sL))])'''
		self.assertTrue(TestAST.test(input, expect, 375))

	def test_376(self):
		input = '''
## l=0klt#x
bool Xnm <- "U'"" ## 5ZjsHyO?_Z:neWAr*T
## !s
'''
		expect = '''Program([VarDecl(Id(Xnm), BoolType, None, StringLit(U'"))])'''
		self.assertTrue(TestAST.test(input, expect, 376))

	def test_377(self):
		input = '''
func pKb ()
	begin
		for db3 until RT4G by 8E+30
			return
		## i&-
	end
dynamic PmY <- 426
## N"Y3]1pO`
'''
		expect = '''Program([FuncDecl(Id(pKb), [], Block([For(Id(db3), Id(RT4G), NumLit(8e+30), Return())])), VarDecl(Id(PmY), None, dynamic, NumLit(426.0))])'''
		self.assertTrue(TestAST.test(input, expect, 377))

	def test_378(self):
		input = '''
dynamic GXdl
## .00qq5n.cV
'''
		expect = '''Program([VarDecl(Id(GXdl), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 378))

	def test_379(self):
		input = '''
func PP (string cpc[4.875E+03,2.079,228.661e-85])
	return 370E32

var UG ## _1Z&,`;*@$r<GC~=n.
'''
		expect = '''Program([FuncDecl(Id(PP), [VarDecl(Id(cpc), ArrayType([4875.0, 2.079, 2.28661e-83], StringType), None, None)], Return(NumLit(3.7e+34)))])'''
		self.assertTrue(TestAST.test(input, expect, 379))

	def test_380(self):
		input = '''
string jjSo[327.055E-42,7E-61] <- d4 ## .0FbhFk#
## SPCpn@m"`&9VIWK^NLu
'''
		expect = '''Program([VarDecl(Id(jjSo), ArrayType([3.27055e-40, 7e-61], StringType), None, Id(d4))])'''
		self.assertTrue(TestAST.test(input, expect, 380))

	def test_381(self):
		input = '''
func fb (number aO4, var pnP2[6.309])
	return

## mb]<1Ke
'''
		expect = '''Program([])'''
		self.assertTrue(TestAST.test(input, expect, 381))

	def test_382(self):
		input = '''
func VYt (bool NiTh[726], dynamic qv)
	begin
		## BLX
		return
		## Z,3HW3AS3fD{/8
	end
'''
		expect = '''Program([])'''
		self.assertTrue(TestAST.test(input, expect, 382))

	def test_383(self):
		input = '''
## Ib
##  2{%]qvB!
func EBd ()
	begin
		## y19qbQncW?
	end
'''
		expect = '''Program([FuncDecl(Id(EBd), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 383))

	def test_384(self):
		input = '''
func Ag ()	begin
	end

'''
		expect = '''Program([FuncDecl(Id(Ag), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 384))

	def test_385(self):
		input = '''
func fND ()
	return

'''
		expect = '''Program([FuncDecl(Id(fND), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 385))

	def test_386(self):
		input = '''
dynamic u8O[5.260E+45,860.199E+32,5E+26]
func oU (string YwG[31,849.088E-81], var j3, var js[3.969e88])	return

## o."=w;aOo*3UU{m
'''
		expect = '''Program([VarDecl(Id(u8O), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 386))

	def test_387(self):
		input = '''
func LD5 (dynamic hKw[455.795,547.651], var gy, bool vVy[4E19,9.437])
	return

'''
		expect = '''Program([])'''
		self.assertTrue(TestAST.test(input, expect, 387))

	def test_388(self):
		input = '''
## mG9CmEe^-mgt3kift?
bool Ib[4.691,0,9]
func Uh (string CC[690.740,56,7E65], number WN)
	begin
		return "}"
	end
'''
		expect = '''Program([VarDecl(Id(Ib), ArrayType([4.691, 0.0, 9.0], BoolType), None, None), FuncDecl(Id(Uh), [VarDecl(Id(CC), ArrayType([690.74, 56.0, 7e+65], StringType), None, None), VarDecl(Id(WN), NumberType, None, None)], Block([Return(StringLit(}))]))])'''
		self.assertTrue(TestAST.test(input, expect, 388))

	def test_389(self):
		input = '''
func hCEQ ()	return

func Mp ()
	begin
		continue
	end

func l5Y (dynamic xX[61])	begin
		## $J:j!5V
	end
dynamic FG[4,347.477e+27,79.460] <- "'"'"" ## g&,+
'''
		expect = '''Program([FuncDecl(Id(hCEQ), [], Return()), FuncDecl(Id(Mp), [], Block([Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 389))

	def test_390(self):
		input = '''
## /+5hF5p_,/11p%/u7lV
##  F*pLkZS_"
'''
		expect = '''Program([])'''
		self.assertTrue(TestAST.test(input, expect, 390))

	def test_391(self):
		input = '''
## -dz+tOC8p8P=Jz
## PI
number luXj <- 95.094 ## |BL`V{
## &?|2%
func xk (number oI, bool PM)
	return true

'''
		expect = '''Program([VarDecl(Id(luXj), NumberType, None, NumLit(95.094)), FuncDecl(Id(xk), [VarDecl(Id(oI), NumberType, None, None), VarDecl(Id(PM), BoolType, None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 391))

	def test_392(self):
		input = '''
## 793Aq$_Pg
'''
		expect = '''Program([])'''
		self.assertTrue(TestAST.test(input, expect, 392))

	def test_393(self):
		input = '''
func EeiL (dynamic vZX, var lQE)	return

'''
		expect = '''Program([])'''
		self.assertTrue(TestAST.test(input, expect, 393))

	def test_394(self):
		input = '''
func D0Y (number SzT[29,3], var Dp)	return "'"pZ'""
func Mn1w (bool ON[153.639,617,49], var IfE)	return 33.297E+19

## !^Uvy1I_2/G5GaDyy]#*
'''
		expect = '''Program([])'''
		self.assertTrue(TestAST.test(input, expect, 394))

	def test_395(self):
		input = '''
## r^tVw
bool yJI[517.870,737,13] <- R6I ## MVi(VEF=<d]50
func v1y7 (number V9tQ, number koLd[98E89,2.303,16.313e-08])	return
bool AzC <- wMm
'''
		expect = '''Program([VarDecl(Id(yJI), ArrayType([517.87, 737.0, 13.0], BoolType), None, Id(R6I)), FuncDecl(Id(v1y7), [VarDecl(Id(V9tQ), NumberType, None, None), VarDecl(Id(koLd), ArrayType([9.8e+90, 2.303, 1.6313e-07], NumberType), None, None)], Return()), VarDecl(Id(AzC), BoolType, None, Id(wMm))])'''
		self.assertTrue(TestAST.test(input, expect, 395))

	def test_396(self):
		input = '''
func wIsp (dynamic ZEb, bool j1, bool C2IX)	begin
		## RnGg]*
		break
	end

'''
		expect = '''Program([])'''
		self.assertTrue(TestAST.test(input, expect, 396))

	def test_397(self):
		input = '''
func G1dn (dynamic QGa[8.232E+90,42E96,16.613e-50], string KS)	begin
	end
func SIFU (var ByzF)	return 817
func AU (bool ZVw2[816E60], string O2q, string zHEu[5.318E54,552.871])
	return
## 1
var h5
'''
		expect = '''Program([])'''
		self.assertTrue(TestAST.test(input, expect, 397))

	def test_398(self):
		input = '''
dynamic piLi <- R5s ## OI7
## M(jHYWC4fO"n+#il
dynamic Yo <- "'"'"$o"
## gZ
'''
		expect = '''Program([VarDecl(Id(piLi), None, dynamic, Id(R5s)), VarDecl(Id(Yo), None, dynamic, StringLit('"'"$o))])'''
		self.assertTrue(TestAST.test(input, expect, 398))

	def test_399(self):
		input = '''
## V@m
func zA (string NfP)
	begin
		## Hkt;
	end

number uxxq ## Y0}pZ
## oG[jg
## ~;X aTv=dON
'''
		expect = '''Program([FuncDecl(Id(zA), [VarDecl(Id(NfP), StringType, None, None)], Block([])), VarDecl(Id(uxxq), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 399))

	def test_400(self):
		input = '''
func nrGN ()	begin
		## bNN2D24as.$x<7c
		## tv`Fe7
		## D
	end
var fSF[1E88] <- 8 ## r033n)O
var iNg <- false ## MqAd[T68Fd)4 C#{[
string r9E[23.123e+61] ## 5~uTw-X[+ysM#s
number CoF[1E30] <- false
'''
		expect = '''Program([FuncDecl(Id(nrGN), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 400))
