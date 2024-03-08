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
	
	def test_366(self):
		input = """
            number QuangMinh
        """
		expect = str(Program([
                VarDecl(Id("QuangMinh"), NumberType())
            ]))
		self.assertTrue(TestAST.test(input, expect, 366))
	def test_367(self):
		input = """
            string QuangMinh <- 13412
        """
		expect = str(Program([
                VarDecl(Id("QuangMinh"), StringType(), None, NumberLiteral(13412.0))
            ]))

		self.assertTrue(TestAST.test(input, expect, 367))
	def test_368(self):
		input = """
            dynamic QuangMinh <- 1
            dynamic QuangMinh
        """
		expect = str(Program([
                    VarDecl(Id("QuangMinh"), None, "dynamic", NumberLiteral(1.0)),
                    VarDecl(Id("QuangMinh"), None, "dynamic")
                ]))
		self.assertTrue(TestAST.test(input, expect, 368))
	def test_369(self):
		input = """
            var QuangMinh <- 12
        """
		expect = str(Program([
                    VarDecl(Id("QuangMinh"), None, "var", NumberLiteral(12.0))
                ]))

		self.assertTrue(TestAST.test(input, expect, 369))
	def test_370(self):
		input = """
            func main()
                begin
                end
        """
		expect = str(Program([
                    FuncDecl(Id("main"), [], Block([]))
                ]))
		self.assertTrue(TestAST.test(input, expect, 370))
	def test_371(self):
		input = """
            func main()
                begin
                break
                end
        """
		expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    Break()]))
                ]))
		self.assertTrue(TestAST.test(input, expect, 371))
	def test_372(self):
		input = """
            var x <- [1, "a", true, false]
        """
		expect = str(Program([
                    VarDecl(Id("x"), None, "var",  ArrayLiteral([NumberLiteral(1.0), StringLiteral("a"), BooleanLiteral(True), BooleanLiteral(False)]))
                ]))
		self.assertTrue(TestAST.test(input, expect, 372))
	def test_373(self):
		input = """
            var x <- 1 ... "2"
            var x <- 1 <= "2"
            var x <- 1 and 2 or 3
            var x <- 1 + 2 - 3
            var x <- 1 * 2 / 3 % 4
            var x <- ---1
            var x <- not not 1
            var x <- x 
            var x <- a[1,2,3]
        """
		expect = str(Program([
                    VarDecl(Id("x"), None, "var",  BinaryOp("...", NumberLiteral(1.0), StringLiteral("2"))),
                    VarDecl(Id("x"), None, "var",  BinaryOp("<=", NumberLiteral(1.0), StringLiteral("2"))),
                    VarDecl(Id("x"), None, "var",  BinaryOp("or", BinaryOp("and", NumberLiteral(1.0), NumberLiteral(2.0)), NumberLiteral(3.0))),
                    VarDecl(Id("x"), None, "var",  BinaryOp("-", BinaryOp("+", NumberLiteral(1.0), NumberLiteral(2.0)), NumberLiteral(3.0))),
                    VarDecl(Id("x"), None, "var",  BinaryOp("%", BinaryOp("/", BinaryOp("*", NumberLiteral(1.0), NumberLiteral(2.0)), NumberLiteral(3.0)), NumberLiteral(4.0))),
                    VarDecl(Id("x"), None, "var",  UnaryOp("-", UnaryOp("-", UnaryOp("-", NumberLiteral(1.0))))),
                    VarDecl(Id("x"), None, "var",  UnaryOp("not", UnaryOp("not", NumberLiteral(1.0)))),
                    VarDecl(Id("x"), None, "var",  Id("x")),
                    VarDecl(Id("x"), None, "var",  ArrayCell(Id("a"), [NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)]))
                ]))
		self.assertTrue(TestAST.test(input, expect, 373))
	def test_374(self):
		input = """
            var x <- 2 or 3 and 1 <= 2 ... 4 <= 5 + a * 3 + c - -1 + not - 2
        """
		expect = str(Program([
                VarDecl(Id("x"), None, "var",  BinaryOp("...", BinaryOp("<=", BinaryOp("and", BinaryOp("or", NumberLiteral(2.0), NumberLiteral(3.0)), NumberLiteral(1.0)), NumberLiteral(2.0)), BinaryOp("<=", NumberLiteral(4.0), BinaryOp("+", BinaryOp("-", BinaryOp("+", BinaryOp("+", NumberLiteral(5.0), BinaryOp("*", Id("a"), NumberLiteral(3.0))), Id("c")), UnaryOp("-", NumberLiteral(1.0))), UnaryOp("not", UnaryOp("-", NumberLiteral(2.0)))))))
            ]))
        
		self.assertTrue(TestAST.test(input, expect, 374))
	def test_375(self):
		input = """
            var x <- -a[1+2] ... 2
        """
		expect = str(Program([
                    VarDecl(Id("x"), None, "var",  BinaryOp("...", UnaryOp("-", ArrayCell(Id("a"), [BinaryOp("+", NumberLiteral(1.0), NumberLiteral(2.0))])), NumberLiteral(2.0)))
                ]))
        
		self.assertTrue(TestAST.test(input, expect, 375))
	def test_376(self):
		input = """
            func main()
                begin
                    continue
                    continue
                    break
                    begin
                        continue
                        continue
                        break                    
                    end
                end
        """
		expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    Continue(),
                    Continue(),
                    Break(),
                        Block([
                        Continue(),
                        Continue(),
                        Break()])]))
                ]))
        
		self.assertTrue(TestAST.test(input, expect, 376))
	def test_377(self):
		input = """
            func main()
                begin
                    return  25 + 37
                    return
                end
            func main()
                return 9
        """
		expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    Return(BinaryOp("+", NumberLiteral(25.0), NumberLiteral(37.0))),
                    Return()])),
                    FuncDecl(Id("main"), [], Return(NumberLiteral(9.0)))
                ]))
        
		self.assertTrue(TestAST.test(input, expect, 377))
	def test_378(self):
		input = """
            func main()
            begin
                dynamic a <- 3.14
                var b <- 1e5
                string d[4.567]
                dynamic e
                number f[3e2, 1] <- 2.7
            end
        """
		expect = str(Program([
            FuncDecl(Id("main"), [], Block(
                [VarDecl(Id("a"), None, "dynamic", NumberLiteral(3.14)), 
                 VarDecl(Id("b"), None, "var", NumberLiteral(100000.0)), 
                 VarDecl(Id("d"), ArrayType([4.567], StringType()), None),
                 VarDecl(Id("e"), None, "dynamic"),
                 VarDecl(Id("f"), ArrayType([300.0, 1.0], NumberType()), None, NumberLiteral(2.7))
            ]))]))

		self.assertTrue(TestAST.test(input, expect, 378))
	def test_379(self):
		input = """
            func main()
                begin
                    if (true)
                        if(true) return 1
                        else return 1
                end

        """
		expect =str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True), 
               If(BooleanLiteral(True), Return(NumberLiteral(1.0)), [], Return(NumberLiteral(1.0))), [], None)
            ]))]))
        
		self.assertTrue(TestAST.test(input, expect, 379))
	def test_380(self):
		input = """## expresion in array lit 
func foo(number a) begin
if ((a=1) or (a=0)) return 1
return a*foo(a)
end

number arr[2,3] <- [[1,2,3],[5*6,7%2,-3.13E-6*foo(foo(3))]]

func main()
begin
number a<- arr[foo(1),foo(3)%3]
return
end
"""
		expect = '''Program([FuncDecl(Id(foo), [VarDecl(Id(a), NumberType, None, None)], Block([If((BinaryOp(or, BinaryOp(=, Id(a), NumLit(1.0)), BinaryOp(=, Id(a), NumLit(0.0))), Return(NumLit(1.0))), [], None), Return(BinaryOp(*, Id(a), CallExpr(Id(foo), [Id(a)])))])), VarDecl(Id(arr), ArrayType([2.0, 3.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(BinaryOp(*, NumLit(5.0), NumLit(6.0)), BinaryOp(%, NumLit(7.0), NumLit(2.0)), BinaryOp(*, UnaryOp(-, NumLit(3.13e-06)), CallExpr(Id(foo), [CallExpr(Id(foo), [NumLit(3.0)])]))))), FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, ArrayCell(Id(arr), [CallExpr(Id(foo), [NumLit(1.0)]), BinaryOp(%, CallExpr(Id(foo), [NumLit(3.0)]), NumLit(3.0))])), Return()]))])'''
        
		self.assertTrue(TestAST.test(input, expect, 380))
	def test_381(self):
		input = """## complex bool expresion 
func main() 
begin
dynamic a
a <- ((A or B and C + 3*2%4/3)<=(not(-1+foo(x+y*(z-1)))))...(x!=y)
end
"""
		expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), None, dynamic, None), AssignStmt(Id(a), BinaryOp(..., BinaryOp(<=, BinaryOp(and, BinaryOp(or, Id(A), Id(B)), BinaryOp(+, Id(C), BinaryOp(/, BinaryOp(%, BinaryOp(*, NumLit(3.0), NumLit(2.0)), NumLit(4.0)), NumLit(3.0)))), UnaryOp(not, BinaryOp(+, UnaryOp(-, NumLit(1.0)), CallExpr(Id(foo), [BinaryOp(+, Id(x), BinaryOp(*, Id(y), BinaryOp(-, Id(z), NumLit(1.0))))])))), BinaryOp(!=, Id(x), Id(y))))]))])'''
        
		self.assertTrue(TestAST.test(input, expect, 381))
	def test_382(self):
		input = """## function without implementation
func main()
func a(number b)
func c(number g[10],string s[10], bool bo[10])
"""
		expect = '''Program([FuncDecl(Id(main), [], None), FuncDecl(Id(a), [VarDecl(Id(b), NumberType, None, None)], None), FuncDecl(Id(c), [VarDecl(Id(g), ArrayType([10.0], NumberType), None, None), VarDecl(Id(s), ArrayType([10.0], StringType), None, None), VarDecl(Id(bo), ArrayType([10.0], BoolType), None, None)], None)])'''
        
		self.assertTrue(TestAST.test(input, expect, 382))
	def test_383(self):
		input = """## array as expr
func main()
begin
number b<-1
var a<- --------[1,2]*----------------b
end
"""
		expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(b), NumberType, None, NumLit(1.0)), VarDecl(Id(a), None, var, BinaryOp(*, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, ArrayLit(NumLit(1.0), NumLit(2.0)))))))))), UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, Id(b)))))))))))))))))))]))])'''
        
		self.assertTrue(TestAST.test(input, expect, 383))
	def test_384(self):
		input = """## minus 
func main()
begin
number b<-1
var a<- --------1*----------------b
end
"""
		expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(b), NumberType, None, NumLit(1.0)), VarDecl(Id(a), None, var, BinaryOp(*, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, NumLit(1.0))))))))), UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, Id(b)))))))))))))))))))]))])'''
        
		self.assertTrue(TestAST.test(input, expect, 384))
	def test_385(self):
		input = """## this code with alot of newline


func main()


begin 
if (a=2) 



a<-2


end 

"""
		expect = '''Program([FuncDecl(Id(main), [], Block([If((BinaryOp(=, Id(a), NumLit(2.0)), AssignStmt(Id(a), NumLit(2.0))), [], None)]))])'''
        
		self.assertTrue(TestAST.test(input, expect, 385))
	def test_386(self):
		input = """## if if else else 
func main() begin 
bool a<-true 
bool b<-false 
if (not a) 
    if (b) writeString("b is correct")
    else writeString("b is not correct")
else writeString("a is correct")
return
end
"""
		expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), BoolType, None, BooleanLit(True)), VarDecl(Id(b), BoolType, None, BooleanLit(False)), If((UnaryOp(not, Id(a)), If((Id(b), CallStmt(Id(writeString), [StringLit(b is correct)])), [], CallStmt(Id(writeString), [StringLit(b is not correct)]))), [], CallStmt(Id(writeString), [StringLit(a is correct)])), Return()]))])'''

		self.assertTrue(TestAST.test(input, expect, 386))
	def test_387(self):
		input = """##BST with Zcode 
func initTree(number tree[100,3]) begin 
    var i<-0 
    for i until i=100 by 1
        begin 
            tree[i,0] <- -1
            tree[i,1] <- -1
            tree[i,2] <- -1
        end
end

func appendNode(number val,number head,number tree[100,3],bool freeNode[100])
begin 
number node <- 0 
for node until node=100 by 1
    if (freeNode[node]) break 
freeNode[node] <- false 
tree[node,0] <- val 
if (head = -1) return node 
var i <- 0 
number currNode <- 0
for i until i=100 by 1 
begin 
if (tree[node,0] < tree[currNode,0])
    begin 
        if (tree[currNode,1]!=-1) currNode <- tree[currNode,1]
        else tree[currNode,1] <- node 
    end
else begin
    if (tree[currNode,2]!=-1) currNode <- tree[currNode,2]
    else tree[currNode,2] <- node
end
end 
return head
end 

func main() begin 
number tree[100,3]
bool freeNode[100]
number head <- -1
initTree(tree)
var i<-0 
for i until i=100 by 1
    freeNode[i] <- true
i<-0 
for i until i=100 by 1
    begin 
        number val <- readNumber()
        head <- appendNode(val,head,tree, freeNode)
    end
end
"""
		expect = '''Program([FuncDecl(Id(initTree), [VarDecl(Id(tree), ArrayType([100.0, 3.0], NumberType), None, None)], Block([VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(=, Id(i), NumLit(100.0)), NumLit(1.0), Block([AssignStmt(ArrayCell(Id(tree), [Id(i), NumLit(0.0)]), UnaryOp(-, NumLit(1.0))), AssignStmt(ArrayCell(Id(tree), [Id(i), NumLit(1.0)]), UnaryOp(-, NumLit(1.0))), AssignStmt(ArrayCell(Id(tree), [Id(i), NumLit(2.0)]), UnaryOp(-, NumLit(1.0)))]))])), FuncDecl(Id(appendNode), [VarDecl(Id(val), NumberType, None, None), VarDecl(Id(head), NumberType, None, None), VarDecl(Id(tree), ArrayType([100.0, 3.0], NumberType), None, None), VarDecl(Id(freeNode), ArrayType([100.0], BoolType), None, None)], Block([VarDecl(Id(node), NumberType, None, NumLit(0.0)), For(Id(node), BinaryOp(=, Id(node), NumLit(100.0)), NumLit(1.0), If((ArrayCell(Id(freeNode), [Id(node)]), Break), [], None)), AssignStmt(ArrayCell(Id(freeNode), [Id(node)]), BooleanLit(False)), AssignStmt(ArrayCell(Id(tree), [Id(node), NumLit(0.0)]), Id(val)), If((BinaryOp(=, Id(head), UnaryOp(-, NumLit(1.0))), Return(Id(node))), [], None), VarDecl(Id(i), None, var, NumLit(0.0)), VarDecl(Id(currNode), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(=, Id(i), NumLit(100.0)), NumLit(1.0), Block([If((BinaryOp(<, ArrayCell(Id(tree), [Id(node), NumLit(0.0)]), ArrayCell(Id(tree), [Id(currNode), NumLit(0.0)])), Block([If((BinaryOp(!=, ArrayCell(Id(tree), [Id(currNode), NumLit(1.0)]), UnaryOp(-, NumLit(1.0))), AssignStmt(Id(currNode), ArrayCell(Id(tree), [Id(currNode), NumLit(1.0)]))), [], AssignStmt(ArrayCell(Id(tree), [Id(currNode), NumLit(1.0)]), Id(node)))])), [], Block([If((BinaryOp(!=, ArrayCell(Id(tree), [Id(currNode), NumLit(2.0)]), UnaryOp(-, NumLit(1.0))), AssignStmt(Id(currNode), ArrayCell(Id(tree), [Id(currNode), NumLit(2.0)]))), [], AssignStmt(ArrayCell(Id(tree), [Id(currNode), NumLit(2.0)]), Id(node)))]))])), Return(Id(head))])), FuncDecl(Id(main), [], Block([VarDecl(Id(tree), ArrayType([100.0, 3.0], NumberType), None, None), VarDecl(Id(freeNode), ArrayType([100.0], BoolType), None, None), VarDecl(Id(head), NumberType, None, UnaryOp(-, NumLit(1.0))), CallStmt(Id(initTree), [Id(tree)]), VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(=, Id(i), NumLit(100.0)), NumLit(1.0), AssignStmt(ArrayCell(Id(freeNode), [Id(i)]), BooleanLit(True))), AssignStmt(Id(i), NumLit(0.0)), For(Id(i), BinaryOp(=, Id(i), NumLit(100.0)), NumLit(1.0), Block([VarDecl(Id(val), NumberType, None, CallExpr(Id(readNumber), [])), AssignStmt(Id(head), CallExpr(Id(appendNode), [Id(val), Id(head), Id(tree), Id(freeNode)]))]))]))])'''
        
		self.assertTrue(TestAST.test(input, expect, 387))
	def test_388(self):
		input = """##declare in statement without block
func main() 
begin 
    if (1) number a[3,2] <- [[1,2],[3,4],[5,6]]
end
"""
		expect = '''Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), VarDecl(Id(a), ArrayType([3.0, 2.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(3.0), NumLit(4.0)), ArrayLit(NumLit(5.0), NumLit(6.0))))), [], None)]))])'''
        
		self.assertTrue(TestAST.test(input, expect, 388))
	def test_389(self):
		input = """## use identifier nearly the same with key words
func main()
begin 
    dynamic for_ 
    var var_  <- for_ 
    if_ (var_)
end
"""
		expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(for_), None, dynamic, None), VarDecl(Id(var_), None, var, Id(for_)), CallStmt(Id(if_), [Id(var_)])]))])'''
        
		self.assertTrue(TestAST.test(input, expect, 389))
	def test_390(self):
		input = """## find GCD 
func gcd(number a, number b)
begin
    if (b = 0) return a
    return gcd(b, a % b)
end

func main() begin
    writeNumber(gcd(6, 9))
    writeNumber(gcd(24, 16))
    writeNumber(gcd(1, 7))
end
"""
		expect = '''Program([FuncDecl(Id(gcd), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([If((BinaryOp(=, Id(b), NumLit(0.0)), Return(Id(a))), [], None), Return(CallExpr(Id(gcd), [Id(b), BinaryOp(%, Id(a), Id(b))]))])), FuncDecl(Id(main), [], Block([CallStmt(Id(writeNumber), [CallExpr(Id(gcd), [NumLit(6.0), NumLit(9.0)])]), CallStmt(Id(writeNumber), [CallExpr(Id(gcd), [NumLit(24.0), NumLit(16.0)])]), CallStmt(Id(writeNumber), [CallExpr(Id(gcd), [NumLit(1.0), NumLit(7.0)])])]))])'''
        
		self.assertTrue(TestAST.test(input, expect, 390))
	def test_391(self):
		input = """##palindrome string 
func isPalindrome(string s[100], number left, number right)
begin
    ## Because ZCode string cannot be indexed, cut, etc...
    ## We assume that s is an array of 1-length strings, aka characters
    ## And we will check whether characters from left to right (inclusively) can make a palindrome string
    
    if (left > right + 1) return false
    if ((left = right) or (left = right + 1)) return true
    return (s[left] == s[right]) and isPalindrome(s, left + 1, right - 1)
end

func main()
begin
    isPalindrome(["m", "o", "m"], 0, 2)
    isPalindrome(["d", "o", "g", "e", "e", "s", "e", "s", "e", "e", "g", "o", "d"], 0, 12)
end
"""
		expect = '''Program([FuncDecl(Id(isPalindrome), [VarDecl(Id(s), ArrayType([100.0], StringType), None, None), VarDecl(Id(left), NumberType, None, None), VarDecl(Id(right), NumberType, None, None)], Block([If((BinaryOp(>, Id(left), BinaryOp(+, Id(right), NumLit(1.0))), Return(BooleanLit(False))), [], None), If((BinaryOp(or, BinaryOp(=, Id(left), Id(right)), BinaryOp(=, Id(left), BinaryOp(+, Id(right), NumLit(1.0)))), Return(BooleanLit(True))), [], None), Return(BinaryOp(and, BinaryOp(==, ArrayCell(Id(s), [Id(left)]), ArrayCell(Id(s), [Id(right)])), CallExpr(Id(isPalindrome), [Id(s), BinaryOp(+, Id(left), NumLit(1.0)), BinaryOp(-, Id(right), NumLit(1.0))])))])), FuncDecl(Id(main), [], Block([CallStmt(Id(isPalindrome), [ArrayLit(StringLit(m), StringLit(o), StringLit(m)), NumLit(0.0), NumLit(2.0)]), CallStmt(Id(isPalindrome), [ArrayLit(StringLit(d), StringLit(o), StringLit(g), StringLit(e), StringLit(e), StringLit(s), StringLit(e), StringLit(s), StringLit(e), StringLit(e), StringLit(g), StringLit(o), StringLit(d)), NumLit(0.0), NumLit(12.0)])]))])'''
        
		self.assertTrue(TestAST.test(input, expect, 391))
	def test_392(self):
		input = """##for check
func main()
begin
    string words[4] <- ["apple", "banana", "cherry", "date"]
    dynamic i<-0
    for  i until i > size(words) - 1 by 1
        writeString(words[i])
end
"""
		expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(words), ArrayType([4.0], StringType), None, ArrayLit(StringLit(apple), StringLit(banana), StringLit(cherry), StringLit(date))), VarDecl(Id(i), None, dynamic, NumLit(0.0)), For(Id(i), BinaryOp(>, Id(i), BinaryOp(-, CallExpr(Id(size), [Id(words)]), NumLit(1.0))), NumLit(1.0), CallStmt(Id(writeString), [ArrayCell(Id(words), [Id(i)])]))]))])'''
        
		self.assertTrue(TestAST.test(input, expect, 392))
	def test_393(self):
		input = """## sum of array
func sum(number a[100], number length)
begin
    var i <- 0
    var sum <- 0
    for i until i >= length by 1
        sum <- sum + a[i]
    return sum
end

func main() begin
    writeNumber(sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))
    writeNumber(sum([2, 0, 2, 4], 4))
end
"""
		expect = '''Program([FuncDecl(Id(sum), [VarDecl(Id(a), ArrayType([100.0], NumberType), None, None), VarDecl(Id(length), NumberType, None, None)], Block([VarDecl(Id(i), None, var, NumLit(0.0)), VarDecl(Id(sum), None, var, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), Id(length)), NumLit(1.0), AssignStmt(Id(sum), BinaryOp(+, Id(sum), ArrayCell(Id(a), [Id(i)])))), Return(Id(sum))])), FuncDecl(Id(main), [], Block([CallStmt(Id(writeNumber), [CallExpr(Id(sum), [ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0), NumLit(5.0), NumLit(6.0), NumLit(7.0), NumLit(8.0), NumLit(9.0), NumLit(10.0)), NumLit(10.0)])]), CallStmt(Id(writeNumber), [CallExpr(Id(sum), [ArrayLit(NumLit(2.0), NumLit(0.0), NumLit(2.0), NumLit(4.0)), NumLit(4.0)])])]))])'''
        
		self.assertTrue(TestAST.test(input, expect, 393))
	def test_394(self):
		input = """## sum of array
func sum(number a[100], number length)
begin
    var i <- 0
    var sum <- 0
    for i until i >= length by 1
        sum <- sum + a[i]
    return sum
end

func main() begin
    writeNumber(sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))
    writeNumber(sum([2, 0, 2, 4], 4))
end
"""
		expect = '''Program([FuncDecl(Id(sum), [VarDecl(Id(a), ArrayType([100.0], NumberType), None, None), VarDecl(Id(length), NumberType, None, None)], Block([VarDecl(Id(i), None, var, NumLit(0.0)), VarDecl(Id(sum), None, var, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), Id(length)), NumLit(1.0), AssignStmt(Id(sum), BinaryOp(+, Id(sum), ArrayCell(Id(a), [Id(i)])))), Return(Id(sum))])), FuncDecl(Id(main), [], Block([CallStmt(Id(writeNumber), [CallExpr(Id(sum), [ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0), NumLit(5.0), NumLit(6.0), NumLit(7.0), NumLit(8.0), NumLit(9.0), NumLit(10.0)), NumLit(10.0)])]), CallStmt(Id(writeNumber), [CallExpr(Id(sum), [ArrayLit(NumLit(2.0), NumLit(0.0), NumLit(2.0), NumLit(4.0)), NumLit(4.0)])])]))])'''
        
		self.assertTrue(TestAST.test(input, expect, 394))
	def test_395(self):
		input = """
            number qmi[5,3,4.2] <- 1
            bool riley[2,3,4]
        """
		expect = str(Program([
                VarDecl(Id("qmi"), ArrayType([5.0, 3.0, 4.2], NumberType()), None, NumberLiteral(1.0)),
                VarDecl(Id("riley"), ArrayType([2.0, 3.0, 4.0], BoolType()))
            ]))
		self.assertTrue(TestAST.test(input, expect, 395))
	def test_396(self):
		input = """
            string qmi
            bool bucwanha
            string qmi <- 1
            bool bucwanha <- 1
        """
		expect = str(Program([
                VarDecl(Id("qmi"), StringType()),
                VarDecl(Id("bucwanha"), BoolType()),
                VarDecl(Id("qmi"), StringType(), None, NumberLiteral(1.0)),
                VarDecl(Id("bucwanha"), BoolType(), None, NumberLiteral(1.0))
            ]))
        
		self.assertTrue(TestAST.test(input, expect, 396))
	def test_397(self):
		input = """
            dynamic QuangMinh <- 1
            dynamic QuangMinh
        """
		expect = str(Program([
                    VarDecl(Id("QuangMinh"), None, "dynamic", NumberLiteral(1.0)),
                    VarDecl(Id("QuangMinh"), None, "dynamic")
                ]))
        
		self.assertTrue(TestAST.test(input, expect, 397))
	def test_398(self):
		input = """
            func main()
                begin
                    continue
                end
        """
		expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    Continue()]))
                ]))
        
		self.assertTrue(TestAST.test(input, expect, 398))
	def test_399(self):
		input = """
            func main()
                begin
                    return  12 + 14
                    return
                end
            func main()
                return 15
        """
		expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    Return(BinaryOp("+", NumberLiteral(12.0), NumberLiteral(14.0))),
                    Return()])),
                    FuncDecl(Id("main"), [], Return(NumberLiteral(15.0)))
                ]))
        
		self.assertTrue(TestAST.test(input, expect, 399))
	def test_400(self):
		input = """
            func main()
                begin
                    if (true) return 10
                end
            func main()
                begin
                    if (true) return 28
                    else return 36
                end
        """
		expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    If(BooleanLiteral(True), Return(NumberLiteral(10.0)), [] , None)])),
                    FuncDecl(Id("main"), [], Block([
                    If(BooleanLiteral(True), Return(NumberLiteral(28.0)), [] ,Return(NumberLiteral(36.0)))]))
                ]))
        
		self.assertTrue(TestAST.test(input, expect, 400))
