import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
	def test_201(self):
		input = '''
number O_ <- - [UKwh(x3e(FJm()[DWD]), false, 57)[mI2], 4] ## RPWZrii?mn
number AOKW[75] <- false ## +$,{)
## MM:!w
'''
		expect = '''Error on line 2 col 0: number'''
		self.assertTrue(TestParser.test(input, expect, 201))

	def test_202(self):
		input = '''
dynamic iJ
var f_B <- 17.665E+39 ## +3&xIiqUp&%Y9K7
string JyPi ##  A>?L#p4STeDB2o.Xi
## {gAm"
func xI ()
	return 9.978e46

'''
		expect = '''Error on line 2 col 0: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 202))

	def test_203(self):
		input = '''
string txJo <- 330.240
## )Scxlx}U2fk%:^M
var Wm[17.172e+09,49.050]
## 5|1K
'''
		expect = '''Error on line 2 col 0: string'''
		self.assertTrue(TestParser.test(input, expect, 203))

	def test_204(self):
		input = '''
## (LDt
## ez]Mdz7gOn?<t4o
func J1q (bool AAXY[565.943,288.749e34,97.166], string q_q7)
	return false

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 204))

	def test_205(self):
		input = '''
number C9[25,10.211e-21,711.048E-38]
'''
		expect = '''Error on line 2 col 0: number'''
		self.assertTrue(TestParser.test(input, expect, 205))

	def test_206(self):
		input = '''
func ZiJ7 (dynamic iXL, dynamic Mgb)
	return "0-"
string XKEJ ## X!qGjY=l=~emr
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 206))

	def test_207(self):
		input = '''
## |~`B3}9zn&-P
number Vp <- true
func Su (bool f3r[0,995], bool pCWi[831E49,68])
	return

'''
		expect = '''Error on line 3 col 0: number'''
		self.assertTrue(TestParser.test(input, expect, 207))

	def test_208(self):
		input = '''
## DJP`_3:~h{IDmDs
dynamic QB[965.888E51] ## WZ]BoC>
## E
'''
		expect = '''Error on line 3 col 0: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 208))

	def test_209(self):
		input = '''
## sf
string N06 ## `&-su:48
'''
		expect = '''Error on line 3 col 0: string'''
		self.assertTrue(TestParser.test(input, expect, 209))

	def test_210(self):
		input = '''
string w0[5E77,5E-66] <- "'"'"a"
## n`.v#9DMn
bool zm[40.890e-30,85.444E-88] ## 4XS)
string ax9n <- false
var Nz[0.499,6e+60]
'''
		expect = '''Error on line 2 col 0: string'''
		self.assertTrue(TestParser.test(input, expect, 210))

	def test_211(self):
		input = '''
dynamic vkL[258E51] ## gQWO}#*
func PN (var P4v[80.358E60], number f2dK[228E81])
	return

string wbzq
func VS (dynamic evb, var hGgk, bool NY)	begin
		## z,D|"
	end

'''
		expect = '''Error on line 2 col 0: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 211))

	def test_212(self):
		input = '''
## v$zvti6aA[Oao&Iyo
## `c^c.qnTQ
## 0r$Fg
bool pWB <- "o'"E"
## $mz]TYO88}{o68ww
'''
		expect = '''Error on line 5 col 0: bool'''
		self.assertTrue(TestParser.test(input, expect, 212))

	def test_213(self):
		input = '''
func ftc (var Nvl[50,1], bool QP[278,686.049E76,121.811E+39])	return "'""
bool Fa[3,22E+59,0] <- p22 ## !M3
func pl (number cJ0, bool iiML)	return
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 213))

	def test_214(self):
		input = '''
## 8bE&9X!Ge#
## #zGv`8P^CsRYA=ms.`f(
func Ryp ()
	return 83.196
func ox (string Uq)	begin
	end

## QqK(x_*>Fw
'''
		expect = '''Error on line 5 col 14: 
'''
		self.assertTrue(TestParser.test(input, expect, 214))

	def test_215(self):
		input = '''
## W0jaGPC+j
## ei,8sdE
## pi_HwXmI-p[ L(mr
func MFP (dynamic Zo9, number Bmr)
	return FU

'''
		expect = '''Error on line 5 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 215))

	def test_216(self):
		input = '''
number bxP[28.953E+94,9.815e41] ## +4R,{^7l k{#x$
bool S_rd
func V7u4 (number r6[24,55e+35,2.207], dynamic I4t[555,879])
	return 50E-15
## ejb
'''
		expect = '''Error on line 2 col 0: number'''
		self.assertTrue(TestParser.test(input, expect, 216))

	def test_217(self):
		input = '''
## /D *S7cEutN1AAhfyxtI
func aQ (dynamic HA[78.560,5E28,498.778E93], bool SGST[3.003,993.215e27,58.657e75], bool tW5Q[45])	begin
		for ipqE until "3s2d'"" by VZL
			string Xi
	end

number mZO[4] <- Tn
var qa[9.522e+60,6,6.298] ## i,`}m
'''
		expect = '''Error on line 3 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 217))

	def test_218(self):
		input = '''
## @8n5<vb^QOX_pC;E)(T
## wTKeC$
number a9dy <- bhKw ## )>QnDT
string qr[88,4.224,0]
'''
		expect = '''Error on line 4 col 0: number'''
		self.assertTrue(TestParser.test(input, expect, 218))

	def test_219(self):
		input = '''
bool Qo ## {^H)yawbBS`^U
number Uws[1e-19,87E07,84.874E-89] <- Kp ## .8eq;Q1O~?0/%1
## D
'''
		expect = '''Error on line 2 col 0: bool'''
		self.assertTrue(TestParser.test(input, expect, 219))

	def test_220(self):
		input = '''
## W 1y.)&`x5-Q-%(0{
func qB (string MVEb, var uSU5[432.696], string hxxw[5.884e-11])	return Czz

func lgj ()
	begin
		kvT(true, false, false)
		begin
			## U57B8rxN%19
			## ;
			## i_N; %![}
		end
		yg8[1E-50, "?'"b'"'"", "VV'"W"] <- false
	end
'''
		expect = '''Error on line 3 col 22: var'''
		self.assertTrue(TestParser.test(input, expect, 220))

	def test_221(self):
		input = '''
## vWf-hF~Ib!;D
func ikv ()
	return

## J9bG9)^{;gEq=+<66i
number a8E ## `k, +lyM-igX`LF8(f,$
'''
		expect = '''Error on line 7 col 0: number'''
		self.assertTrue(TestParser.test(input, expect, 221))

	def test_222(self):
		input = '''
func TW3 (string nMK5, bool me, var QCa)	return "c>/'""

var EQ[91,18]
var niZD
'''
		expect = '''Error on line 2 col 32: var'''
		self.assertTrue(TestParser.test(input, expect, 222))

	def test_223(self):
		input = '''
## *~([w5_`D{
## F<PHm+`J[X.
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 223))

	def test_224(self):
		input = '''
## g)/(D#P
bool C6 ## V@Jff.N.2Q
dynamic rOhL[58] ## 1R|l]>mBa8
## +_;yh/N)o
'''
		expect = '''Error on line 3 col 0: bool'''
		self.assertTrue(TestParser.test(input, expect, 224))

	def test_225(self):
		input = '''
number l_ <- 128e+86
bool cV
bool Li[451e+49,4] ## sFNQeY!m:5
dynamic gg[56.518E+55,8.604,839.386E04] ## 6w/%c&7}WmQQa
## 897BjA{!u0xN01_5v ma
'''
		expect = '''Error on line 2 col 0: number'''
		self.assertTrue(TestParser.test(input, expect, 225))

	def test_226(self):
		input = '''
## [qCq<5Pt2P7;xQS[vs
func gpl (var KmF, dynamic MBk[34.955e-60,81])	return false

bool RlJz ## 4h[cAUackWwNlRQ
## !"E1D$
## 2"1*+;?QUR]n<l={<
'''
		expect = '''Error on line 3 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 226))

	def test_227(self):
		input = '''
string rEw[5] <- niK ## %8sSC<z}!OT$$^f
number hD ## 1+
bool hOFY[6.130e+89] ## FT&De8
func eQD (bool pni)
	return 556
number o0oj <- inV9 ## Y;_US Zi|
'''
		expect = '''Error on line 2 col 0: string'''
		self.assertTrue(TestParser.test(input, expect, 227))

	def test_228(self):
		input = '''
func CYjm (var wZG, number rs[9E20,1.907E+41,742.584], dynamic vWUV)	begin
		## 7>tkF1ku"Y#qGcx$
		## AQ
		return r4j
	end

func GSlp (bool KCP, var goo, var Ga)
	begin
		if (EG)
		for xWY until " '"" by 279
			continue
		elif ("'"_'"vW") c0w()
		elif (false)
		dynamic m8m ## /VHFFlTD
		elif (le2L) begin
			## oE
			for LRj until Jt5C by true
				for rB until "?c'"" by "q4'"'""
					MLPY()
			number eE[76.818,46.539] ## iZpVW
		end
		else if (8.552E52)
		cl[79, false] <- "?'"'"7"
		elif ("'"%h")
		Vg[false] <- 5.035E28
		elif (oR5) for nWz until false by R0UW
			begin
				## Xuf?Ss`Coi 
			end
		elif (s8Pq) hWz()
		elif ("D'"JW") Sh("'"'"^'"", qvvX)
		## LQ
	end
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 228))

	def test_229(self):
		input = '''
## `^sV83ks
func V_Ak ()
	begin
		break
	end
func iCJk (dynamic edpY[8.779,121.998])	return
func ogV8 (var ro[0.603,4.138E-68,51.199E47])	return
bool cR6i ## W%
'''
		expect = '''Error on line 5 col 2: break'''
		self.assertTrue(TestParser.test(input, expect, 229))

	def test_230(self):
		input = '''
## >62`d[*&C7$Y-z,w^
func tl (string DCe)	begin
		## WqrhO;7]7ZDB
		## &bp|39{UWnLP(S/{`j y
	end
dynamic uqUG ## ]tGU
'''
		expect = '''Error on line 6 col 1: end'''
		self.assertTrue(TestParser.test(input, expect, 230))

	def test_231(self):
		input = '''
func DtWG ()
	return uZrh
func eckU (number Hz7x[761.085,54.581e84], bool ky[207.736,9.199E-64], var ZC)	return w_
string pCa1 ## DY
string jSJ_
dynamic C4j[225e-98,4.493,2E80] <- "'"-C]'""
'''
		expect = '''Error on line 3 col 12: 
'''
		self.assertTrue(TestParser.test(input, expect, 231))

	def test_232(self):
		input = '''
string c0[613.249,192E93,95.839e-77] ## >
## Z <zb^YKq_
'''
		expect = '''Error on line 2 col 0: string'''
		self.assertTrue(TestParser.test(input, expect, 232))

	def test_233(self):
		input = '''
string iquT
func tO (string Q4nX[74.238e+85,0,2], dynamic yS)
	begin
		Dr <- "RrD3D"
		return
	end
number eFc
func iK ()
	begin
	end

func kR4 (string E3n)
	return KL4b
'''
		expect = '''Error on line 2 col 0: string'''
		self.assertTrue(TestParser.test(input, expect, 233))

	def test_234(self):
		input = '''
func CjiW (string hZ[10.344,4e+03,21.222], number z1F[18,5e+73])
	return
func yOt (number etqg[2e24], dynamic N0, number Ds)	return
## *mjkAV$TP9
'''
		expect = '''Error on line 3 col 7: 
'''
		self.assertTrue(TestParser.test(input, expect, 234))

	def test_235(self):
		input = '''
string kxct[659.510e+80] <- TuI ## 1(E2w?`<Bs
bool RF6
## 3pbM9}gVM
## <a8TsS0
number ar[59,78.373e-15,1] ## S7
'''
		expect = '''Error on line 2 col 0: string'''
		self.assertTrue(TestParser.test(input, expect, 235))

	def test_236(self):
		input = '''
dynamic dk4A ## 4v @N]G4Z+
func hz (number Y3fl, number jUAI, var hw7U[48.625E+79,37.535E59])	return

func x7 (string vQ, number N7H[418e+42,78E+06,38.130])	return 478.115E-04

## E|guQ
func VPh (bool cYRm)	return

'''
		expect = '''Error on line 2 col 0: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 236))

	def test_237(self):
		input = '''
func hxD (bool OZsv[97E-00,5.921], bool xVVf, var VxiM)
	begin
	end

## de;#dC=$C 4dbi!}x(
func FXz ()
	return
'''
		expect = '''Error on line 2 col 46: var'''
		self.assertTrue(TestParser.test(input, expect, 237))

	def test_238(self):
		input = '''
## K#"q0B:3&;
func Zr (dynamic JJZ)	return

func Ry (string mBJW, string FX[22E-26,0.142,86.260])
	return "'"'"'" "
bool ERA[7e-76,895.267] <- true
'''
		expect = '''Error on line 3 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 238))

	def test_239(self):
		input = '''
func AYP ()	return

string WPM[172,609.010] <- 71.062e40 ## @!Dh};/J]^Q"^
number q6PH[639.474,887.250,0.689E-15] <- "'"M" ## |iXPU
dynamic HH4c <- KEp
## j4|OR
'''
		expect = '''Error on line 4 col 0: string'''
		self.assertTrue(TestParser.test(input, expect, 239))

	def test_240(self):
		input = '''
## )}hDIX(H99:iFv9%J
func mH (number Pw[532], number AS, string Yyn[901e27,1.883])
	return
string Zs[8.380e+20,428.427]
'''
		expect = '''Error on line 4 col 7: 
'''
		self.assertTrue(TestParser.test(input, expect, 240))

	def test_241(self):
		input = '''
func u2 (bool R04[80])
	begin
		ZL(false, true, true)
		## Zyom(iwN-Fm#4?
	end
bool Zd[100.567e-50,6.804e-56,282] <- "C4+"
## hO]+}Kw*E[R4;nhp|
## /?? N$$_8u
'''
		expect = '''Error on line 4 col 2: ZL'''
		self.assertTrue(TestParser.test(input, expect, 241))

	def test_242(self):
		input = '''
dynamic P_G
## w~*<,HInmpsl
dynamic jRS6 <- Xlm ## t
number tY <- 3.332
func MG1 (var Ps[58e47,304E+49,2.508e-11], string H96X)
	return

'''
		expect = '''Error on line 2 col 0: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 242))

	def test_243(self):
		input = '''
func kd (string HBl[35e-48,8], bool Zn[3,641])	begin
		## PIQ4mL^l=3sx2yf
		Fk5[3.787, 171e-17] <- 132.147
	end
dynamic wtt ## il6$}_UJ4stJ#.
number e0[62e52,579.266e-00]
'''
		expect = '''Error on line 4 col 2: Fk5'''
		self.assertTrue(TestParser.test(input, expect, 243))

	def test_244(self):
		input = '''
func lb5 (bool cr[85E+57,940.238e00,47.344e46])	return B0xG
string mi9[34.573,2] <- SH9y ## 1L/dZW%(L 9hj`#
func xp (string zQy, var xzJp, dynamic i9T)
	begin
		return 1
	end
func RtS (string DP72[58,547e+77,436E-24])
	return true

number Zn[0E+89,241.499e+29,47e+34]
'''
		expect = '''Error on line 2 col 59: 
'''
		self.assertTrue(TestParser.test(input, expect, 244))

	def test_245(self):
		input = '''
## [A%f_J@<R?0=Sat#L]
func tK (string De5[1.990E-67,79.302e+07], string a3Hi)
	return
func XES (string Jc[2e44])	begin
		begin
		end
		begin
		end
	end
'''
		expect = '''Error on line 4 col 7: 
'''
		self.assertTrue(TestParser.test(input, expect, 245))

	def test_246(self):
		input = '''
## ^QKto!&*X"s9zQ0nFD
## TMdN9@@ly MI(Gt:-M:
func l3Bb ()
	return
'''
		expect = '''Error on line 5 col 7: 
'''
		self.assertTrue(TestParser.test(input, expect, 246))

	def test_247(self):
		input = '''
func nk (dynamic M6, string Wv[71], bool bUwz[3e36,0.448])
	return false
func PT (number Xlu, string ohG[7.664E-62])
	begin
		## Bs? R6fz(!#K
	end
'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 247))

	def test_248(self):
		input = '''
dynamic LTup ## GGnbW;<"p|Bc&<|B,(9
func t71 ()	return

func XN (string y2ZY)
	return false

string F12[91.125,793] ## c^kD)7.==eu
dynamic Rjv[88e93] ## qWjD,=u
'''
		expect = '''Error on line 2 col 0: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 248))

	def test_249(self):
		input = '''
number b2Tc[151E+37,456.976E-32]
## wCpd
## 6^~;JcQ4$,sa,%_hq
'''
		expect = '''Error on line 2 col 0: number'''
		self.assertTrue(TestParser.test(input, expect, 249))

	def test_250(self):
		input = '''
bool kTiu[20E+33,2.691e83,87e+09] <- "'"n" ## F]|57DzEs|%
'''
		expect = '''Error on line 2 col 0: bool'''
		self.assertTrue(TestParser.test(input, expect, 250))

	def test_251(self):
		input = '''
func nG5R (bool H1M1, var dNKK, var hT[3.012,8.482,2e84])	begin
		## #gmVU%8kardA%"#"
	end

dynamic gv[72E+95,603.544,733.045e02] ## +U*0/v7#[/Biz%M+
func eeb (string cf4X[4.093E-87,459.059E15], string UR)
	return lytS
func x1Cq (string xo8[25,94.891E+28,611.540E33])
	begin
		break
		## o!czQAR>QL~<j4qdA9%
		## HsPXGz-Gj5"FQAI;x
	end
'''
		expect = '''Error on line 2 col 22: var'''
		self.assertTrue(TestParser.test(input, expect, 251))

	def test_252(self):
		input = '''
func dY7 (number xnS, bool G5, var Ii[946.791,236,791])
	begin
		continue
		## =)A,SQ|z%c5 uA6cvI
	end
func nM4 (bool oX[0.954E73])
	begin
	end

func ss_y (var XzY)	return

'''
		expect = '''Error on line 2 col 31: var'''
		self.assertTrue(TestParser.test(input, expect, 252))

	def test_253(self):
		input = '''
dynamic bbA[83.750,0e-17,68e-32]
## cI]kcK(ty4VUKCzB3
'''
		expect = '''Error on line 2 col 0: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 253))

	def test_254(self):
		input = '''
var gBES <- false ## %3,
number g5u <- false
dynamic Zsfq[242.766e61,25.218e90,9E-32] ## ND=PI9IIh
## qLR@Yh8P["Y#`
func H8f ()	begin
	end
'''
		expect = '''Error on line 2 col 4: gBES'''
		self.assertTrue(TestParser.test(input, expect, 254))

	def test_255(self):
		input = '''
## N//}EMR
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 255))

	def test_256(self):
		input = '''
## &T*)Jm
## yQyI)g(KUw/^l:>
number Cn <- Sdv
'''
		expect = '''Error on line 4 col 0: number'''
		self.assertTrue(TestParser.test(input, expect, 256))

	def test_257(self):
		input = '''
## >`Ft%{&|Gj,r?
func WE (bool tQsh[286,36,921])	return
bool GAq[675.524E+06,81,8] ## "eCkfD3%>d&awU
'''
		expect = '''Error on line 3 col 38: 
'''
		self.assertTrue(TestParser.test(input, expect, 257))

	def test_258(self):
		input = '''
## NtYK
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 258))

	def test_259(self):
		input = '''
## o,~]I
var ts[11.998]
func ubfQ (string jWG, bool hEdZ)
	return

## &W#A<
'''
		expect = '''Error on line 3 col 4: ts'''
		self.assertTrue(TestParser.test(input, expect, 259))

	def test_260(self):
		input = '''
## bajSL|*56y?6O;)"2e
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 260))

	def test_261(self):
		input = '''
dynamic QFx <- " '"Y|" ## zY&(=&J3MjB_
## +~h-HIH
'''
		expect = '''Error on line 2 col 0: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 261))

	def test_262(self):
		input = '''
## %k<_
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 262))

	def test_263(self):
		input = '''
func fn ()
	return false

## G1dZs
## -TBH.Sxq[B0ZmT-[!+LP
func ahX ()	return "'"l'"h"
'''
		expect = '''Error on line 7 col 27: 
'''
		self.assertTrue(TestParser.test(input, expect, 263))

	def test_264(self):
		input = '''
## SuJ]t
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 264))

	def test_265(self):
		input = '''
func KlvK (string W53[0,11.501e-08], dynamic cNTe)	begin
		## Fa$CG=n<~Yd
	end
func vFn (number MS2[43.820,20.221,759.073], bool DaC7[89e43,2E47])
	begin
		## u[a
	end

'''
		expect = '''Error on line 2 col 37: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 265))

	def test_266(self):
		input = '''
## )
func Gisx ()
	return "'">"
bool BB[48.085] <- true ## A"UwQ&SV$
## Vo";deD:Kz/ X]RdZ[@
func tM ()	return

'''
		expect = '''Error on line 4 col 13: 
'''
		self.assertTrue(TestParser.test(input, expect, 266))

	def test_267(self):
		input = '''
func igN (dynamic Lj5f[953.223E+20,586.232,52e08], string GHNg[86.577,11.371])
	return

func lu (bool v8JH, var vk[3,7e81,46.345E+00], bool Pp[22.537E-19,357.354e+37,98e-13])	return

## 5
## .fJcSa#I[mQ
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 267))

	def test_268(self):
		input = '''
dynamic dV07[420.824e-98,95] ## [hf9ch_x
## >JV
'''
		expect = '''Error on line 2 col 0: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 268))

	def test_269(self):
		input = '''
## o$Oeb>qa(K9Dj
func ziI (string eX3D, string qfn[161.345e+35,562,0])
	return
dynamic nSog
func UDjh ()
	return
## ~mG8Bje>Z}aD=!.#
'''
		expect = '''Error on line 4 col 7: 
'''
		self.assertTrue(TestParser.test(input, expect, 269))

	def test_270(self):
		input = '''
func RX5j (bool NC[29.608e-00,83.095e-72,24.901], string sMW)	return mAl
## ?EdOK|c~^fF,@z[<U^
func Un (bool rR)	begin
	end
dynamic TP ## RfijQ;
func M3jc ()
	return 6.850E+93

'''
		expect = '''Error on line 2 col 72: 
'''
		self.assertTrue(TestParser.test(input, expect, 270))

	def test_271(self):
		input = '''
string LDK5 ## i.Jz27zp`!LcWJ`
number Su ## a >%g|e}!}5
'''
		expect = '''Error on line 2 col 0: string'''
		self.assertTrue(TestParser.test(input, expect, 271))

	def test_272(self):
		input = '''
func TbrS (string BG, string LTC)	return

string tNP <- o39 ## #&f;Hh)nA` ^w1Ga
## Ij
bool y8K2 ## T0KXZY),=T3dL#lD<VJ
'''
		expect = '''Error on line 4 col 0: string'''
		self.assertTrue(TestParser.test(input, expect, 272))

	def test_273(self):
		input = '''
## j}clgH&5rF
var MO[945e+78,60.047,217.192] ## JJ,XTot
func Wm (bool vhVy, dynamic XJ, dynamic RvY[56])	begin
	end

## g;|a.
var WTlf ## VmykA!
'''
		expect = '''Error on line 3 col 4: MO'''
		self.assertTrue(TestParser.test(input, expect, 273))

	def test_274(self):
		input = '''
## $I<KE=.s3~,Q=x~ak{
## TS{`i)%eJ/e
func GFj (bool td)	begin
		## +ZNjkNjzfu
	end

'''
		expect = '''Error on line 6 col 1: end'''
		self.assertTrue(TestParser.test(input, expect, 274))

	def test_275(self):
		input = '''
## 2`;!1hM;
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 275))

	def test_276(self):
		input = '''
string A60A[1e63] <- "j'",'""
func FB (dynamic kHQY[3.411E-73,58])	begin
		## iRf34y9?j5R;L
		## d"m{K#{;z*%3[
		## [8x3l_Qq2BBHzxl
	end
'''
		expect = '''Error on line 2 col 0: string'''
		self.assertTrue(TestParser.test(input, expect, 276))

	def test_277(self):
		input = '''
number Bn[231.258,94.767E-39,96.502]
dynamic x3fO <- gAzF
bool pt[1.743,29,9.372] <- 5.110
'''
		expect = '''Error on line 2 col 0: number'''
		self.assertTrue(TestParser.test(input, expect, 277))

	def test_278(self):
		input = '''
func rYW (dynamic HZs[2.688], number NSBv[137.969])	return 0.416E-41
func uH (dynamic Pljy, dynamic S_b[6], bool lV)
	return

func gG0 ()	return false

'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 278))

	def test_279(self):
		input = '''
func Z_X (number sF[193.562e60,18.360E02], var S3[4.081E04], bool nF)
	return

func L1 (bool jc, bool oeI, dynamic ff3)	return dGP

func rm ()	begin
		ICv(75)
		if (171.802E-61) for fJ until "'"'">'"'"" by 4
			break
		elif ("M:'"")
		if (605.281E78)
		if (6.647)
		begin
			begin
				## /8g2C3mHa7
			end
			## ]
			## ).c6nSmL9{%rV$uf
		end
		elif (0e25)
		if (false)
		bGC <- "'"'""
		elif ("h")
		xdTM <- lNPk
		elif ("'"")
		if (867.318E39)
		continue
		elif ("?[k'"0")
		begin
			U2oU()
			continue
		end
		elif (true) SNGd <- "'"'"'"'"'""
		elif (9.640E-96) break
		elif (false) wRx()
		elif ("q3'"") F6m()
		elif (8.048) begin
			## !
		end
		else begin
			## `L~zBpms-i ?2GlF[O
		end
		elif (bh)
		for db until "'"'"'"" by 81e40
			return wp
		else return "E'"'""
		elif (wUH)
		continue
		elif (4.493)
		for b0tE until false by HDP0
			continue
		elif (62.509) for isK until "n'"l'"'"" by 65.685E-37
			SLWH(NJ3n)
	end

func e5P (number Vqy)
	begin
		## gVQr@BufCJ{7ut
		## d4l/k<k?Ico-p$e
		dynamic m8M4 ## W
	end
bool d9[22.110] <- "'" '"'"'"" ## 6
'''
		expect = '''Error on line 2 col 43: var'''
		self.assertTrue(TestParser.test(input, expect, 279))

	def test_280(self):
		input = '''
func OHNU (string zB[9E+44,40.717,357], number jXX[4E69,772])	return vOnl
## zX;C>6/cCV{h7qbq
number lzF[8,772.425,100.532e-34] ## Yd_N`43vA7qhRm>
'''
		expect = '''Error on line 2 col 73: 
'''
		self.assertTrue(TestParser.test(input, expect, 280))

	def test_281(self):
		input = '''
## cu"c|Rs
number RL <- true ## =
bool NoOY[87.420e-13,64.916] ## vHB2Oy
'''
		expect = '''Error on line 3 col 0: number'''
		self.assertTrue(TestParser.test(input, expect, 281))

	def test_282(self):
		input = '''
## L:Purg:r|H)@
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 282))

	def test_283(self):
		input = '''
dynamic GHd3
'''
		expect = '''Error on line 2 col 0: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 283))

	def test_284(self):
		input = '''
func ViRk (var dX, string TMFm)
	begin
	end
func ONpH (bool CQ_)	return true

## c}
## w|n& -Hr
func PcH (number heY0, var iMI)	begin
		if ("'"7y'"S")
		begin
		end
		elif ("T'"3'"") break
		elif (Gm8m) return lpU
		elif (XMZ) continue
		elif (false)
		hAMk("~'"", true, 751)[true] <- "a'"'""
		elif ("<") if (true) hf("'"CE", false)
		elif (29.572e-16)
		q9 <- 54.847
		elif (true) mB["'"'"#'"'"", true, false] <- 2.691E-99
		elif (j_V) if ("P'"'"")
		begin
			break
			continue
		end
		elif (true)
		return
		else break
		for F5s until true by 77.150E-11
			FD("'"'"", "'"")
		## |-
	end
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 284))

	def test_285(self):
		input = '''
number Yy98 ## ?j1Gla}1 2{5fW
## (}zdiNh5+e1%|q1#UipI
func s_qB (string U2, string mm[95.249E+49], var rgO)
	return

'''
		expect = '''Error on line 2 col 0: number'''
		self.assertTrue(TestParser.test(input, expect, 285))

	def test_286(self):
		input = '''
## Qh[7z].!*B#
## %tr[(We^~!n):
func sg ()	return L_

func vsn (number Q1kr)
	begin
		## QKp5a[fR
	end

'''
		expect = '''Error on line 9 col 1: end'''
		self.assertTrue(TestParser.test(input, expect, 286))

	def test_287(self):
		input = '''
func nIj ()	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 287))

	def test_288(self):
		input = '''
func Ss ()	return

bool te <- AOit
func AT1A ()
	begin
		if (false)
		return
	end

func qf1 (number r7)
	return Qf
dynamic Ar <- "$'""
'''
		expect = '''Error on line 4 col 0: bool'''
		self.assertTrue(TestParser.test(input, expect, 288))

	def test_289(self):
		input = '''
## pAMRumHYBAtTjCR(
func SwI5 (bool uz, bool rVp[903.207,697.666], bool zwtt[0,20e+47,26e-74])
	begin
	end

## 7kBVVDal8
func Kc ()	begin
		## 1|}O)EIV
	end
'''
		expect = '''Error on line 5 col 1: end'''
		self.assertTrue(TestParser.test(input, expect, 289))

	def test_290(self):
		input = '''
dynamic fyf[91.177e05] <- vjb
number auq ## `Y{ET?8
func Iv (var Eez, string Qr8D)	return 310.321

## <W4G~InCI(mZ
'''
		expect = '''Error on line 2 col 0: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 290))

	def test_291(self):
		input = '''
bool xD2[388.528e-05,19.869] ## +J=h-NBK|bt3S tu_
func DWYk ()
	return false

'''
		expect = '''Error on line 2 col 0: bool'''
		self.assertTrue(TestParser.test(input, expect, 291))

	def test_292(self):
		input = '''
## Eq>U&p6C
func JZ5 (bool Db[2.867e19], string ZP[7.591e+38,7e+53], string SJfU[9,91.879,9E-94])
	begin
	end

## P ;L+c"`o
var BNB[184.338,82e83] <- 1.180 ## _t>@
number sBwL[0,26.429,0]
'''
		expect = '''Error on line 5 col 1: end'''
		self.assertTrue(TestParser.test(input, expect, 292))

	def test_293(self):
		input = '''
var LJlF[3.438] <- 2.209 ## hVZ33K<Mqdw@:>P]uLQ
## YR[$i8q
'''
		expect = '''Error on line 2 col 4: LJlF'''
		self.assertTrue(TestParser.test(input, expect, 293))

	def test_294(self):
		input = '''
bool kE <- true ## 6i.(2
func zpU (string wocH, dynamic Xp)	return false
## 66nu
'''
		expect = '''Error on line 2 col 0: bool'''
		self.assertTrue(TestParser.test(input, expect, 294))

	def test_295(self):
		input = '''
number VrK8
bool Ez0s[877e-41,58.575,88.301E09] <- EMR
func yC (number iA[6,676.238])
	begin
	end
func s6t ()
	begin
		## .mt&|G5Uk08eay
	end

func WC ()
	begin
		## 1xo6{
		## .D;6&r#GN+?D[`OW
	end

'''
		expect = '''Error on line 2 col 0: number'''
		self.assertTrue(TestParser.test(input, expect, 295))

	def test_296(self):
		input = '''
func zM2 (dynamic OYAE[2.688])
	begin
	end

## %lOIRdSlRDR.$78aT
string Cwrt
func BGh (string Nwpb, number i2[25,2])
	return
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 296))

	def test_297(self):
		input = '''
dynamic aq8[83E-55,160.370,59E-15] <- 50E-73
func Nx (bool P99, var J0XS[8], bool vsr[8.700,6e+42,234])	return
func YB4 (string sUGE, dynamic imEW, var kZ4G[514,4.078,67e+44])	return Q8
'''
		expect = '''Error on line 2 col 0: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 297))

	def test_298(self):
		input = '''
bool R9LO <- "0'"Lw{"
'''
		expect = '''Error on line 2 col 0: bool'''
		self.assertTrue(TestParser.test(input, expect, 298))

	def test_299(self):
		input = '''
func EUK3 ()
	return
'''
		expect = '''Error on line 3 col 7: 
'''
		self.assertTrue(TestParser.test(input, expect, 299))

	def test_300(self):
		input = '''
func uF (dynamic sDl[23.822e20], dynamic Dj16, dynamic BX29[1.076,91.920e-40])
	begin
	end

func sKgW (bool yw4)
	return

func zfF ()	return "'""

func bF (dynamic J7, dynamic OOHX[10.755,777e88,7.780e-13], var qr)	return

## Zh?}Ou$:n&35
'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 300))
	def test_301(self):
		input = """func main() return 1
"""
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 301))