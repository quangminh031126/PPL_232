import unittest
from TestUtils import TestAST
from main.zcode.utils.AST import *

class ASTGenSuite(unittest.TestCase):	
	def test_301(self):
		input = '''
string yEX[2] <- (kesM()) 


func E2Cq (string gDMS, number X9[23,45,991.501])
	begin
	end

'''
		expect = '''Program([VarDecl(Id(yEX), ArrayType([2.0], StringType), None, CallExpr(Id(kesM), [])), FuncDecl(Id(E2Cq), [VarDecl(Id(gDMS), StringType, None, None), VarDecl(Id(X9), ArrayType([23.0, 45.0, 991.501], NumberType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 301))


	def test_302(self):
		input = '''
func pH ()	begin
		dynamic JAN <- - YM6((false), "'"'"'"O'"") 
		break
		bool x3Po <- 96.715 
	end
'''
		expect = '''Program([FuncDecl(Id(pH), [], Block([VarDecl(Id(JAN), None, dynamic, UnaryOp(-, CallExpr(Id(YM6), [BooleanLit(False), StringLit('"'"'"O'")]))), Break, VarDecl(Id(x3Po), BoolType, None, NumLit(96.715))]))])'''
		self.assertTrue(TestAST.test(input, expect, 302))


	def test_303(self):
		input = '''
dynamic iUs4 




'''
		expect = '''Program([VarDecl(Id(iUs4), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 303))


	def test_304(self):
		input = '''

func VR (number XA[5.979e-38])
	return R0

var iB <- true 
func KM ()
	begin
		bool Yhza <- false 
	end

'''
		expect = '''Program([FuncDecl(Id(VR), [VarDecl(Id(XA), ArrayType([5.979e-38], NumberType), None, None)], Return(Id(R0))), VarDecl(Id(iB), None, var, BooleanLit(True)), FuncDecl(Id(KM), [], Block([VarDecl(Id(Yhza), BoolType, None, BooleanLit(False))]))])'''
		self.assertTrue(TestAST.test(input, expect, 304))

	def test_305(self):
		input = '''

func rUe ()
	return Yn

dynamic iB9P
'''
		expect = '''Program([FuncDecl(Id(rUe), [], Return(Id(Yn))), VarDecl(Id(iB9P), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 305))

	def test_306(self):
		input = '''

number vQ 

'''
		expect = '''Program([VarDecl(Id(vQ), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 306))


	def test_307(self):
		input = '''


func fB6 ()	return tR5s
'''
		expect = '''Program([FuncDecl(Id(fB6), [], Return(Id(tR5s)))])'''
		self.assertTrue(TestAST.test(input, expect, 307))

	def test_308(self):
		input = '''
string U9 <- ByjW
number Vg <- H74 
bool bu
dynamic od_
'''
		expect = '''Program([VarDecl(Id(U9), StringType, None, Id(ByjW)), VarDecl(Id(Vg), NumberType, None, Id(H74)), VarDecl(Id(bu), BoolType, None, None), VarDecl(Id(od_), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 308))

	def test_309(self):
		input = '''
number DJ 
'''
		expect = '''Program([VarDecl(Id(DJ), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 309))

	def test_310(self):
		input = '''


string tTws[61e+61,7.571e+90,252.442] <- "'"<'"" 

string KfY[2.235e+79,462.338] <- 152e-10
'''
		expect = '''Program([VarDecl(Id(tTws), ArrayType([6.1e+62, 7.571e+90, 252.442], StringType), None, StringLit('"<'")), VarDecl(Id(KfY), ArrayType([2.235e+79, 462.338], StringType), None, NumLit(1.52e-08))])'''
		self.assertTrue(TestAST.test(input, expect, 310))

	def test_311(self):
		input = '''
bool vH[957.504] <- 48
'''
		expect = '''Program([VarDecl(Id(vH), ArrayType([957.504], BoolType), None, NumLit(48.0))])'''
		self.assertTrue(TestAST.test(input, expect, 311))

	def test_312(self):
		input = '''
func PEP ()
	return "s"
func ADJ_ ()	return

func b5_ (string Qn[9.102,340.952,13])	return
'''
		expect = '''Program([FuncDecl(Id(PEP), [], Return(StringLit(s))), FuncDecl(Id(ADJ_), [], Return()), FuncDecl(Id(b5_), [VarDecl(Id(Qn), ArrayType([9.102, 340.952, 13.0], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 312))

	def test_313(self):
		input = '''
func Srzd ()
	begin
	end
string RVu <- false 
'''
		expect = '''Program([FuncDecl(Id(Srzd), [], Block([])), VarDecl(Id(RVu), StringType, None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 313))


	def test_314(self):
		input = '''


func EW (string zy, string BY)
	return 4.108

'''
		expect = '''Program([FuncDecl(Id(EW), [VarDecl(Id(zy), StringType, None, None), VarDecl(Id(BY), StringType, None, None)], Return(NumLit(4.108)))])'''
		self.assertTrue(TestAST.test(input, expect, 314))

	def test_315(self):
		input = '''
number n0 
dynamic Fo2 <- Yd
dynamic Udi
bool en0P <- "g'"P:'"" 
'''
		expect = '''Program([VarDecl(Id(n0), NumberType, None, None), VarDecl(Id(Fo2), None, dynamic, Id(Yd)), VarDecl(Id(Udi), None, dynamic, None), VarDecl(Id(en0P), BoolType, None, StringLit(g'"P:'"))])'''
		self.assertTrue(TestAST.test(input, expect, 315))


	def test_316(self):
		input = '''

dynamic L_9Y 
dynamic Uy <- m8xy
'''
		expect = '''Program([VarDecl(Id(L_9Y), None, dynamic, None), VarDecl(Id(Uy), None, dynamic, Id(m8xy))])'''
		self.assertTrue(TestAST.test(input, expect, 316))


	def test_317(self):
		input = '''

number m35[9] 
var lrc0 <- ";$'"g"

func Of8 (bool e8P, number IT[871], bool IJ)
	return 182.546e+00

'''
		expect = '''Program([VarDecl(Id(m35), ArrayType([9.0], NumberType), None, None), VarDecl(Id(lrc0), None, var, StringLit(;$'"g)), FuncDecl(Id(Of8), [VarDecl(Id(e8P), BoolType, None, None), VarDecl(Id(IT), ArrayType([871.0], NumberType), None, None), VarDecl(Id(IJ), BoolType, None, None)], Return(NumLit(182.546)))])'''
		self.assertTrue(TestAST.test(input, expect, 317))

	def test_318(self):
		input = '''


var lPlD <- 72
'''
		expect = '''Program([VarDecl(Id(lPlD), None, var, NumLit(72.0))])'''
		self.assertTrue(TestAST.test(input, expect, 318))

	def test_319(self):
		input = '''
func BqDe (string Qa4T)	return





'''
		expect = '''Program([FuncDecl(Id(BqDe), [VarDecl(Id(Qa4T), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 319))

	def test_320(self):
		input = '''
func sjG (bool cCE)
	return

'''
		expect = '''Program([FuncDecl(Id(sjG), [VarDecl(Id(cCE), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 320))

	def test_321(self):
		input = '''
number iX3j[9e+67] <- true
'''
		expect = '''Program([VarDecl(Id(iX3j), ArrayType([9e+67], NumberType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 321))

	def test_322(self):
		input = '''

bool FW 

func H7k (bool CSK[0e+34], bool Np1[954e+90,3.658])
	return

'''
		expect = '''Program([VarDecl(Id(FW), BoolType, None, None), FuncDecl(Id(H7k), [VarDecl(Id(CSK), ArrayType([0.0], BoolType), None, None), VarDecl(Id(Np1), ArrayType([9.54e+92, 3.658], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 322))

	def test_323(self):
		input = '''
func m3y ()	return


'''
		expect = '''Program([FuncDecl(Id(m3y), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 323))

	def test_324(self):
		input = '''
var ub <- true 
func JBU (string wc2, number ggHR[86e-23])
	begin
		bool eY[0E-59,35E+47,2.468]
	end

dynamic XQN 
func WJw (number y0A[465E+82], string aO7E, number Obi[8,4.560e88,51.774])
	return "CO."

'''
		expect = '''Program([VarDecl(Id(ub), None, var, BooleanLit(True)), FuncDecl(Id(JBU), [VarDecl(Id(wc2), StringType, None, None), VarDecl(Id(ggHR), ArrayType([8.6e-22], NumberType), None, None)], Block([VarDecl(Id(eY), ArrayType([0.0, 3.5e+48, 2.468], BoolType), None, None)])), VarDecl(Id(XQN), None, dynamic, None), FuncDecl(Id(WJw), [VarDecl(Id(y0A), ArrayType([4.65e+84], NumberType), None, None), VarDecl(Id(aO7E), StringType, None, None), VarDecl(Id(Obi), ArrayType([8.0, 4.56e+88, 51.774], NumberType), None, None)], Return(StringLit(CO.)))])'''
		self.assertTrue(TestAST.test(input, expect, 324))

	def test_325(self):
		input = '''
dynamic Sp0 
func gzwj ()
	return false

func D4k (number Him[4e-65], string BRmI[114.791E+89,612.073E94])	return true

'''
		expect = '''Program([VarDecl(Id(Sp0), None, dynamic, None), FuncDecl(Id(gzwj), [], Return(BooleanLit(False))), FuncDecl(Id(D4k), [VarDecl(Id(Him), ArrayType([4e-65], NumberType), None, None), VarDecl(Id(BRmI), ArrayType([1.14791e+91, 6.12073e+96], StringType), None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 325))

	def test_326(self):
		input = '''
func Bh3 (bool d3[5,43.942E+17,2E-36], number et)
	begin
		
	end

number HUa[79E55,621,39]

'''
		expect = '''Program([FuncDecl(Id(Bh3), [VarDecl(Id(d3), ArrayType([5.0, 4.3942e+18, 2e-36], BoolType), None, None), VarDecl(Id(et), NumberType, None, None)], Block([])), VarDecl(Id(HUa), ArrayType([7.9e+56, 621.0, 39.0], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 326))


	def test_327(self):
		input = '''
func cKA (number OW[408.080e05,2e+91], bool Jo[217.643,99e+11])
	begin
		break
	end
'''
		expect = '''Program([FuncDecl(Id(cKA), [VarDecl(Id(OW), ArrayType([40808000.0, 2e+91], NumberType), None, None), VarDecl(Id(Jo), ArrayType([217.643, 9900000000000.0], BoolType), None, None)], Block([Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 327))

	def test_328(self):
		input = '''

string qMJg
'''
		expect = '''Program([VarDecl(Id(qMJg), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 328))

	def test_329(self):
		input = '''

var DW <- 4.256

'''
		expect = '''Program([VarDecl(Id(DW), None, var, NumLit(4.256))])'''
		self.assertTrue(TestAST.test(input, expect, 329))

	def test_330(self):
		input = '''
func v8N (number jaMJ)	return

func GkA ()
	begin
		
	end



'''
		expect = '''Program([FuncDecl(Id(v8N), [VarDecl(Id(jaMJ), NumberType, None, None)], Return()), FuncDecl(Id(GkA), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 330))

	def test_331(self):
		input = '''
dynamic ZN <- true 

'''
		expect = '''Program([VarDecl(Id(ZN), None, dynamic, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 331))

	def test_332(self):
		input = '''
var jlW <- ms5L
func oC (string GDol)	begin
		
		
		begin
			
		end
	end

'''
		expect = '''Program([VarDecl(Id(jlW), None, var, Id(ms5L)), FuncDecl(Id(oC), [VarDecl(Id(GDol), StringType, None, None)], Block([Block([])]))])'''
		self.assertTrue(TestAST.test(input, expect, 332))

	def test_333(self):
		input = '''

func x8zG ()
	return
'''
		expect = '''Program([FuncDecl(Id(x8zG), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 333))

	def test_334(self):
		input = '''

dynamic Nxw <- gYEH
string Zy4[88.331,614E-64] 

'''
		expect = '''Program([VarDecl(Id(Nxw), None, dynamic, Id(gYEH)), VarDecl(Id(Zy4), ArrayType([88.331, 6.14e-62], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 334))


	def test_335(self):
		input = '''
func EjM ()	return




'''
		expect = '''Program([FuncDecl(Id(EjM), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 335))

	def test_336(self):
		input = '''
func D5I ()
	return

'''
		expect = '''Program([FuncDecl(Id(D5I), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 336))

	def test_337(self):
		input = '''
string mwzh[622.617e68,1,51.531] <- shad 

string wOB[5.677e-89] <- "'"'"" 
'''
		expect = '''Program([VarDecl(Id(mwzh), ArrayType([6.22617e+70, 1.0, 51.531], StringType), None, Id(shad)), VarDecl(Id(wOB), ArrayType([5.677e-89], StringType), None, StringLit('"'"))])'''
		self.assertTrue(TestAST.test(input, expect, 337))

	def test_338(self):
		input = '''
var s0 <- true
'''
		expect = '''Program([VarDecl(Id(s0), None, var, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 338))

	def test_339(self):
		input = '''


dynamic MlLz <- 7.492e-22

'''
		expect = '''Program([VarDecl(Id(MlLz), None, dynamic, NumLit(7.492e-22))])'''
		self.assertTrue(TestAST.test(input, expect, 339))

	def test_340(self):
		input = '''
dynamic y9W 
func Cb ()	return

bool FZ[88E31,9.390] <- 54E20

'''
		expect = '''Program([VarDecl(Id(y9W), None, dynamic, None), FuncDecl(Id(Cb), [], Return()), VarDecl(Id(FZ), ArrayType([8.8e+32, 9.39], BoolType), None, NumLit(5.4e+21))])'''
		self.assertTrue(TestAST.test(input, expect, 340))

	def test_341(self):
		input = '''
func Nq ()	return

func BZ (number nHaN[83.893e-99,16.648E-34,6], number uY)
	begin
		
		return
		break
	end
bool Pe1 <- T7DH 
dynamic qu
'''
		expect = '''Program([FuncDecl(Id(Nq), [], Return()), FuncDecl(Id(BZ), [VarDecl(Id(nHaN), ArrayType([8.3893e-98, 1.6648e-33, 6.0], NumberType), None, None), VarDecl(Id(uY), NumberType, None, None)], Block([Return(), Break])), VarDecl(Id(Pe1), BoolType, None, Id(T7DH)), VarDecl(Id(qu), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 341))

	def test_342(self):
		input = '''
string Sd <- true 
'''
		expect = '''Program([VarDecl(Id(Sd), StringType, None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 342))

	def test_343(self):
		input = '''
bool dfzL <- WRn
'''
		expect = '''Program([VarDecl(Id(dfzL), BoolType, None, Id(WRn))])'''
		self.assertTrue(TestAST.test(input, expect, 343))

	def test_344(self):
		input = '''
func Ky08 (number qTs[74E-05], number vt2N[1E80,29.899E+24,7.211E-19])	return
'''
		expect = '''Program([FuncDecl(Id(Ky08), [VarDecl(Id(qTs), ArrayType([0.00074], NumberType), None, None), VarDecl(Id(vt2N), ArrayType([1e+80, 2.9899e+25, 7.211e-19], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 344))

	def test_345(self):
		input = '''
number kOB[6.315,400] <- true 
'''
		expect = '''Program([VarDecl(Id(kOB), ArrayType([6.315, 400.0], NumberType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 345))

	def test_346(self):
		input = '''



number ShS[142.102,320,8] 
'''
		expect = '''Program([VarDecl(Id(ShS), ArrayType([142.102, 320.0, 8.0], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 346))

	def test_347(self):
		input = '''
number dR9b <- NKu
func n_H2 ()	return


'''
		expect = '''Program([VarDecl(Id(dR9b), NumberType, None, Id(NKu)), FuncDecl(Id(n_H2), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 347))

	def test_348(self):
		input = '''
number ScF6 <- 266
'''
		expect = '''Program([VarDecl(Id(ScF6), NumberType, None, NumLit(266.0))])'''
		self.assertTrue(TestAST.test(input, expect, 348))

	def test_349(self):
		input = '''
number ej <- "d"
'''
		expect = '''Program([VarDecl(Id(ej), NumberType, None, StringLit(d))])'''
		self.assertTrue(TestAST.test(input, expect, 349))

	def test_350(self):
		input = '''
bool MT <- 2
'''
		expect = '''Program([VarDecl(Id(MT), BoolType, None, NumLit(2.0))])'''
		self.assertTrue(TestAST.test(input, expect, 350))

	def test_351(self):
		input = '''
string oDO[30.805,4.707] 
'''
		expect = '''Program([VarDecl(Id(oDO), ArrayType([30.805, 4.707], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 351))

	def test_352(self):
		input = '''
func LU3 (number SF, string lzD[71.624,37])	return
func Xi (string tpsr[137e-86,81E+20])	return

func KHfo ()	return 90
'''
		expect = '''Program([FuncDecl(Id(LU3), [VarDecl(Id(SF), NumberType, None, None), VarDecl(Id(lzD), ArrayType([71.624, 37.0], StringType), None, None)], Return()), FuncDecl(Id(Xi), [VarDecl(Id(tpsr), ArrayType([1.37e-84, 8.1e+21], StringType), None, None)], Return()), FuncDecl(Id(KHfo), [], Return(NumLit(90.0)))])'''
		self.assertTrue(TestAST.test(input, expect, 352))

	def test_353(self):
		input = '''



bool CO[551] <- 8

'''
		expect = '''Program([VarDecl(Id(CO), ArrayType([551.0], BoolType), None, NumLit(8.0))])'''
		self.assertTrue(TestAST.test(input, expect, 353))

	def test_354(self):
		input = '''
func Waf (bool vTaK, bool Ggo7[946], bool GK2[792,371.205E+70])	begin
		begin
		end
		
	end

dynamic UhO <- 2
'''
		expect = '''Program([FuncDecl(Id(Waf), [VarDecl(Id(vTaK), BoolType, None, None), VarDecl(Id(Ggo7), ArrayType([946.0], BoolType), None, None), VarDecl(Id(GK2), ArrayType([792.0, 3.71205e+72], BoolType), None, None)], Block([Block([])])), VarDecl(Id(UhO), None, dynamic, NumLit(2.0))])'''
		self.assertTrue(TestAST.test(input, expect, 354))

	def test_355(self):
		input = '''
number Mls 
var zu <- "'" *"

number wX9[127E-73,8.423,121E+77]
dynamic dt <- NTF 
'''
		expect = '''Program([VarDecl(Id(Mls), NumberType, None, None), VarDecl(Id(zu), None, var, StringLit('" *)), VarDecl(Id(wX9), ArrayType([1.27e-71, 8.423, 1.21e+79], NumberType), None, None), VarDecl(Id(dt), None, dynamic, Id(NTF))])'''
		self.assertTrue(TestAST.test(input, expect, 355))

	def test_356(self):
		input = '''
var DZ2 <- "'"'"" 


func NkVC ()
	return

'''
		expect = '''Program([VarDecl(Id(DZ2), None, var, StringLit('"'")), FuncDecl(Id(NkVC), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 356))

	def test_357(self):
		input = '''

number QJIH[119.001] 

'''
		expect = '''Program([VarDecl(Id(QJIH), ArrayType([119.001], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 357))

	def test_358(self):
		input = '''
func P2z ()
	begin
		
		dynamic iiL2 <- 3 
		
	end

string tiAt[727E62,2,849.273] <- 481e+23 
number ne <- qIU 
'''
		expect = '''Program([FuncDecl(Id(P2z), [], Block([VarDecl(Id(iiL2), None, dynamic, NumLit(3.0))])), VarDecl(Id(tiAt), ArrayType([7.27e+64, 2.0, 849.273], StringType), None, NumLit(4.81e+25)), VarDecl(Id(ne), NumberType, None, Id(qIU))])'''
		self.assertTrue(TestAST.test(input, expect, 358))


	def test_359(self):
		input = '''
string GJu[171e-72] 
'''
		expect = '''Program([VarDecl(Id(GJu), ArrayType([1.71e-70], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 359))

	def test_360(self):
		input = '''
func vAFq ()	return 9.890E86

dynamic kgW <- uZ
func sKJ (bool KS[1e+25])
	return g7QG

dynamic RVj <- true
'''
		expect = '''Program([FuncDecl(Id(vAFq), [], Return(NumLit(9.89e+86))), VarDecl(Id(kgW), None, dynamic, Id(uZ)), FuncDecl(Id(sKJ), [VarDecl(Id(KS), ArrayType([1e+25], BoolType), None, None)], Return(Id(g7QG))), VarDecl(Id(RVj), None, dynamic, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 360))

	def test_361(self):
		input = '''
bool E_[108,2.878] 
'''
		expect = '''Program([VarDecl(Id(E_), ArrayType([108.0, 2.878], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 361))

	def test_362(self):
		input = '''
number nPTn[0E+60,91.316E-54] <- stQ
number bC0
'''
		expect = '''Program([VarDecl(Id(nPTn), ArrayType([0.0, 9.1316e-53], NumberType), None, Id(stQ)), VarDecl(Id(bC0), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 362))

	def test_363(self):
		input = '''

func Iy ()	return true


'''
		expect = '''Program([FuncDecl(Id(Iy), [], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 363))

	def test_364(self):
		input = '''
bool ewhv <- true
'''
		expect = '''Program([VarDecl(Id(ewhv), BoolType, None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 364))

	def test_365(self):
		input = '''
func cq2i ()
	return
string lIF[8,174]

'''
		expect = '''Program([FuncDecl(Id(cq2i), [], Return()), VarDecl(Id(lIF), ArrayType([8.0, 174.0], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 365))
