import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
	def testCase201(self):
		input = '''
## A3nF5H6n/G#[W*<}
## me=)b!9=
number bBWg <- ((not - true != 0E40)) ## FH1QX`:3IBR73KgW),:1
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 201))

	def testCase202(self):
		input = '''
## tXZD3?;]%H2
## +R+u;bFgMRs9WMt`V
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 202))

	def testCase203(self):
		input = '''
## _bI=gm^q!D3W(/"
number mY[367.725E+13]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 203))

	def testCase204(self):
		input = '''
## yG3D0
## 3peu)@IlXrA`<,[vVb9
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 204))

	def testCase205(self):
		input = '''
## tVHN]N>iBANE-J
## q yzM@}"vx2Dl0uxKVR6
var Zx0n[56.855] ## s]*}={O>o75
bool j61[1E01,543e-20,126.909E45]
## v1+.V
'''
		expect = '''Error on line 4 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 205))

	def testCase206(self):
		input = '''
number eSY[68.825,2e51,324] <- "'"s"
string TNe <- K2
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 206))

	def testCase207(self):
		input = '''
func qUvk (dynamic jb[7.795,99.189e+60], bool bP)
	return

## TOr(
## @s-T**< 
bool l6H ## Q4+uDP|
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 207))

	def testCase208(self):
		input = '''
func rc (bool n5[606e-78,3.611], var IM22[5E+14])
	begin
	end

'''
		expect = '''Error on line 2 col 33: var'''
		self.assertTrue(TestParser.test(input, expect, 208))

	def testCase209(self):
		input = '''
bool xjhh <- 5.729
var O2tI[65,757,85E-53]
## vTv2eNr#E
'''
		expect = '''Error on line 3 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 209))

	def testCase210(self):
		input = '''
func lYH (bool qTXR[3,63.063], dynamic HF, bool oR[9E33,8E+68])
	return
string Ir <- 92e36
'''
		expect = '''Error on line 2 col 31: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 210))

	def testCase211(self):
		input = '''
func WNd ()	begin
		## JJa5
		## kI=I&}%e=&</gg9IiZI
		for Z51A until 912E38 by true
			begin
				## 6-d2>$<GL91
				for TGwI until "'">" by "<`"
					begin
					end
			end
	end
## {]-c(9C]WufckW=kn8;
## d8%*~]jAr:JC+8r%
'''
		expect = '''Error on line 3 col 9: 
'''
		self.assertTrue(TestParser.test(input, expect, 211))

	def testCase212(self):
		input = '''
## ]|a@~2J,w;R.,
## mTtj.O8g6nb83
## Qc1&tx
dynamic sE0 ## VsEM8Vf0>KPQM^&c1|]y
bool YR7[10e88,92,4E28]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 212))

	def testCase213(self):
		input = '''
## Z^7#
func AC ()	begin
		## gV4umo)`>N|G`pZ2A
	end
func G5kN (bool r2[8])
	begin
		begin
			FVH(false, KM8b)
			## B;,@?5.eoCi 1<LQz"J
		end
	end

var g34[5] ## -wy-jK@Wl"Szw[~L;P&
'''
		expect = '''Error on line 4 col 22: 
'''
		self.assertTrue(TestParser.test(input, expect, 213))

	def testCase214(self):
		input = '''
bool eH5[855E56,46E-99,534.820e68] <- 785.661 ## fV1F@X
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 214))

	def testCase215(self):
		input = '''
## a< .eKf7wE3[y+
number DAOG[611.079] <- fhv
bool Ec9h[45,4,92E05] ## 3U1O:^2{
## fxOu8#@O"kxT
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 215))

	def testCase216(self):
		input = '''
bool OS2
func MN (dynamic vu[5.457e-92,1,85.876], dynamic WiP, number mdLd)
	return

var vs7
## wEP.l~INA^
func L4V (number VI)
	return true

'''
		expect = '''Error on line 3 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 216))

	def testCase217(self):
		input = '''
string MqB ## ^,,HZknC4C;Zr
func bH2 (var F9v)
	return

func po (bool bCHl[39.603,41.787E93], number lE6, bool xN9)	return "'""
string gIK0[5E+34,158e-08] <- 266
string YIk
'''
		expect = '''Error on line 3 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 217))

	def testCase218(self):
		input = '''
string p1k
bool b5J[659E14,419.767e+81]
var eJhK ## 2"-Ys3
'''
		expect = '''Error on line 4 col 18: 
'''
		self.assertTrue(TestParser.test(input, expect, 218))

	def testCase219(self):
		input = '''
## WhQ,bG`2E
bool aj5x[0] <- q2
number yTKh ## JNy
## R>%O34|}I(p
func v6 (var Spj, bool fY[128E+09,1e-72,947.097])	return

'''
		expect = '''Error on line 6 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 219))

	def testCase220(self):
		input = '''
var Sr[2.805] ## Cdf_+Z
## dEpV5g
## rL>`Bu?o
string lmZK <- fqZ
## ~FQ=
'''
		expect = '''Error on line 2 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 220))

	def testCase221(self):
		input = '''
func TayO (bool A2, number QU)
	return "o"

## _qN@t^C?c@*f.Xk
var XK7 ## G>r6k-{@}@W_,iVYY/!
'''
		expect = '''Error on line 6 col 30: 
'''
		self.assertTrue(TestParser.test(input, expect, 221))

	def testCase222(self):
		input = '''
func KDg (number Gi_Y[5.684e01])	begin
		## 9
	end
dynamic U__0[89.249e-90,21.160E09,69.997E21] <- false
'''
		expect = '''Error on line 3 col 6: 
'''
		self.assertTrue(TestParser.test(input, expect, 222))

	def testCase223(self):
		input = '''
func ty7a (string S5D3)	return

func KbF (string wp_, dynamic qvoN[9.293,13,5.464E-67])	return false
func UD (string Xn[253.250,24.958e+31], dynamic qGC1, dynamic qM8)
	return

## Lk5# HZ^:8!&
'''
		expect = '''Error on line 4 col 22: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 223))

	def testCase224(self):
		input = '''
## W%C62~YZbI.o[eEOj|
string UzT <- xLh
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 224))

	def testCase225(self):
		input = '''
func y3 (bool PKHT[2,1.695], bool gd[259e+07,6E+33,5.188e27])
	return

## "su9"a
dynamic T5[4.138] ## TCs=%nBR-5y6
## 2^nBKw0m5f l%8BZQo:
## P!GGA`&!ucH +
'''
		expect = '''Error on line 6 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 225))

	def testCase226(self):
		input = '''
## Q]6
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 226))

	def testCase227(self):
		input = '''
## Y^9}QY
## ^k9#$]gUrqS
func QrHh (bool uV8[70.580e50,21,941], string Qtf[37e98,3.079E-30,922], dynamic zdWh[11,51])	begin
		## vhd#~,*p1j5q]#be
	end

'''
		expect = '''Error on line 4 col 72: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 227))

	def testCase228(self):
		input = '''
## b$;{qk!AWF1L
func f3 ()	return

func Rz (bool MIfS[593,8])
	begin
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 228))

	def testCase229(self):
		input = '''
func WY (string fY3[898.568E+66,65], dynamic nx[67.385E-03])	begin
		for cYTj until true by "'""
			dynamic xqk4[33,90,333] <- "'"'"'"'"'""
		## Hg8
		for wr until 0.671e+45 by YbkK
			begin
			end
	end

string FTcL[524.123E55,988E+13,60.709E12] <- true
bool WYt7
bool zv <- false ## m#)
## -;
'''
		expect = '''Error on line 2 col 37: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 229))

	def testCase230(self):
		input = '''
dynamic UjQo <- 1E-64
## l#N9C;3]+wR^iY 2,
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 230))

	def testCase231(self):
		input = '''
## 1SQSW~sXO+HV}w
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 231))

	def testCase232(self):
		input = '''
## Pq12;sh^z!
string EpNi[55E+88,5.134,77.333] <- Y7KN ## 3t!E0^>r;,ty:Tf
string RfFU[24,19e+70] ## #+i/9|
## 5q#Z@y)|Gg!{rw}
number T0[2.419e+48,5] ## S^pgI
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 232))

	def testCase233(self):
		input = '''
## cSAKe6o =C
## kC|0K^VV]yN
number dmo ## @3&Ex(g%g
func QySb (string sj, number Lo[15.307,0.098])
	return

func zO ()	begin
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 233))

	def testCase234(self):
		input = '''
## iwv+*QP"f|tRlu+/
func M1 (bool MPYw, dynamic Vy[365E99,3e+41])	begin
	end

'''
		expect = '''Error on line 3 col 20: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 234))

	def testCase235(self):
		input = '''
## ^}A}2rMdrqi"0+dcUa
## (n
## ~)V%X?$LM]X0zxwcLD
var I6A[33e97] <- "J'""
func ncu ()
	return
'''
		expect = '''Error on line 5 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 235))

	def testCase236(self):
		input = '''
func AB (bool fKlS[4.381,474.626], string n05l[45,62.262e+62,4.010e-83])
	return r60V
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 236))

	def testCase237(self):
		input = '''
bool uVk1[82.257E71,371.022] <- bOQ
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 237))

	def testCase238(self):
		input = '''
func on5D (string xN[5,4.457,5], string DGPZ, number Fi)	begin
		break
		## -EaL0Z
		## fLPzu6b8C0UFtK
	end
## Q$.(`gvTE:
func Bp2 (number ct)	begin
	end
var onl <- 19e+00
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 238))

	def testCase239(self):
		input = '''
func amoF (var LR, dynamic QIN)
	begin
		iQ()[false] <- "'"'"K'"C"
		## +%??0OU
	end
## _Z@HQx2K?
## #2
bool d8T
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 239))

	def testCase240(self):
		input = '''
func ttV (var XbU2)	begin
	end
func me8O (number mW, var DtY)
	return true

## ` 9oPei5
var ub5_ <- 482e-70 ## QUr
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 240))

	def testCase241(self):
		input = '''
## RPu>mY/Iyq8tD
## wGk5@F3@m[1Qm
var Pj1 <- "'"3r" ## u_J4D_@zq0~FE 2k4
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 241))

	def testCase242(self):
		input = '''
func mHRi (var PwX, number Wh[7e+76,789.387E-44], bool X1t[73])	begin
		var Aj[2,8E-50,8] <- false
	end
## ^$Mv}_|1g43HS6vT&M
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 242))

	def testCase243(self):
		input = '''
func BPK ()
	return false
## p=dD}?FD<.;js
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 243))

	def testCase244(self):
		input = '''
string woZv[1E+35,924.230]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 244))

	def testCase245(self):
		input = '''
func lq (number oGX4[260.878,8e+04,8], bool wNvh, string Z1F[91.471E-10,936,165.399E+01])	return true

func gyEX ()	return

## X^|%!M-df,uvb
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 245))

	def testCase246(self):
		input = '''
## JP%85"9m
func XgSL (string tSHa[175,646.079], bool ng[466.435e+67,95.783e60,32E96])
	begin
		## Yk8pT
		c1 <- true
		return 544.050e-75
	end

func cu (number Si5)
	begin
	end
func cQUq ()
	return Ucd
var AN[12]
'''
		expect = '''Error on line 4 col 1: begin
'''
		self.assertTrue(TestParser.test(input, expect, 246))

	def testCase247(self):
		input = '''
## 8O!6
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 247))

	def testCase248(self):
		input = '''
func mR ()
	begin
		for UfTi until true by 7
			break
		## )
	end

func xOU (var hm[84.659e-75,0.868e14,33], dynamic RpE[86E-23], string OZ[73.088e+81,142,2.722E91])	return "'"'"'"'""

func xHt (number M3eM[84.307])
	return lb
'''
		expect = '''Error on line 9 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 248))

	def testCase249(self):
		input = '''
number FfF0 <- true ## i7zM:S9%gw
bool ng[954] ## xWSWd!>uER
bool AoU
## tcAYC+b3bh5M<
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 249))

	def testCase250(self):
		input = '''
## 5*j,C*7uE7yf
number Jh[3,407.618,27.535e40]
## WNA-/0+/4rZ:J
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 250))

	def testCase251(self):
		input = '''
func dDK_ ()
	begin
	end
bool lMT
## `{QSc+rj@f(3IHF-Pn
func xN ()
	begin
		## fF
	end
## mW>(pi/}4=#YM
'''
		expect = '''Error on line 8 col 1: begin
'''
		self.assertTrue(TestParser.test(input, expect, 251))

	def testCase252(self):
		input = '''
string qBj[37,1E+79,541]
func VdCZ ()	return "'"'"'"'""

func fY (string CW6)
	return

bool CVh6[95.753,335.757,9.338e-24] <- true ## {.M9Ftolslu+^gb
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 252))

	def testCase253(self):
		input = '''
dynamic NC[69.813e-23,5E63,0.644] <- DdZO
## NEJ-:^uw{y}Lc
'''
		expect = '''Error on line 2 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 253))

	def testCase254(self):
		input = '''
func LnWP (string mN[3e+34])
	return

func OZwT (number ZE)	return at
func Pi (string og[0.856E59,297.576e+35,3])
	begin
		ZX1 <- wHA
		if (false)
		break
		elif ("N") for D9 until "'"'"^" by "'"x'"6'""
			if ("t%")
			lw()
			elif (false) dynamic km0 <- gMVJ
			elif (9)
			begin
				## 9mlWy((q
				## -xTiHZY=cb"]Yxw9
				return "'""
			end
			elif (asz)
			for t4LS until 4e-20 by true
				sz72("YV4'"!")
			else begin
				for OTz until "'"K'"" by "'"A"
					kX(JX)[83.669E+60, false, 0.198e-34] <- 7.362
				break
				## CAh=<@m?Y+
			end
		elif ("`") continue
		elif ("G'"A") xT()
		elif ("M'"")
		if (lJA1) continue
		elif (wiq)
		continue
		elif (Jtxx) dynamic Zzm ## 9lHG2ls"eJQHDH
		elif (true) PL(72.085e58, true, 62.427)
		elif (880)
		RWI[".nK", "'"'"KA", 516.676] <- false
		elif (MHR)
		if (sVI) if (false) jT(aQ, oZ)
		elif (6.571e-29)
		number StI[887] ## Z
		elif (3)
		lAQ <- "Ia"
		elif (391e07) begin
			xuqb()
			## m
			bool a1X
		end
		elif (true) if (24E+73) continue
		elif (true) break
		elif (true)
		Dy_ <- 2
		elif ("'"'"") for fMg2 until "88Nk" by "'""
			if (8) tnVj(8, 19, "0'"Nq")[308] <- "B'"'"'""
		elif (2) for L0 until false by "'""
			if (Rv_V) var gd <- I0p ## $2pS5 >Vd,V.+XY&6w1
			elif (Y_9L) DJ(178.062)
		elif ("@'"") break
		elif ("'"fB") for tpw until 77e-02 by AdEq
			return true
		elif (sPBd) pF(b9l)
		elif ("'"'"'"")
		break
		else begin
			continue
			## r=2W6`c3].
			## JS1!7V}pVC[?g
		end
		begin
		end
	end
var Qtu <- "'"'"o>"
number es[1.476E-69] ## dJSze,tFkNYe<WlQ,B 
'''
		expect = '''Error on line 7 col 1: begin
'''
		self.assertTrue(TestParser.test(input, expect, 254))

	def testCase255(self):
		input = '''
bool IliV[34.625e-85] <- true
func YWr (dynamic t_iz[4.141E+07,421.709])	return "u"

'''
		expect = '''Error on line 3 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 255))

	def testCase256(self):
		input = '''
## e5cWk>q
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 256))

	def testCase257(self):
		input = '''
func arJ_ (bool aQgf, dynamic x9H[37.329E38])
	begin
		IPWa(1.736, false)
	end
func ugqI (number HRR[291.924,5.897], bool aSiB)	return 60

'''
		expect = '''Error on line 2 col 22: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 257))

	def testCase258(self):
		input = '''
func S3xA (number cGhi)	return

func Lf9K (bool mCjS)
	return ")'"E"

func H3r ()	begin
		## 9fI
		## nO
	end
func fg (bool G7, dynamic nPm[61e-68,5,35], dynamic Q8)	begin
	end

'''
		expect = '''Error on line 8 col 8: 
'''
		self.assertTrue(TestParser.test(input, expect, 258))

	def testCase259(self):
		input = '''
## d5PMx/`"Y,W4<_E5W
func jNb (bool D5i4)
	return

## bIX?Am}E*
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 259))

	def testCase260(self):
		input = '''
func FIH8 (string obJI[0,89.940e56,30.679e64], bool CB[555.274], var JF97)	return 0.727E-77

'''
		expect = '''Error on line 2 col 65: var'''
		self.assertTrue(TestParser.test(input, expect, 260))

	def testCase261(self):
		input = '''
## rL93iK
var qzm[31.113E17,366]
'''
		expect = '''Error on line 3 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 261))

	def testCase262(self):
		input = '''
func Zp1G (var wY, var xq, var aDIH)
	return
## K0H[9mPK`@%-
## %/2c3Ano^ql*0jsfr
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 262))

	def testCase263(self):
		input = '''
func Wt7O (dynamic OnVt, dynamic NSt, dynamic jSm[582.208,1.581e97,815E+52])
	return
## fe}V
## ,,U;}s.kxRs
number Nzq <- zV
## }6%?5{(-)<
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 263))

	def testCase264(self):
		input = '''
func VPXy (bool uu, var ThPy[9.061e+00,81], string lVL[7.734,21])	return

'''
		expect = '''Error on line 2 col 20: var'''
		self.assertTrue(TestParser.test(input, expect, 264))

	def testCase265(self):
		input = '''
string HPoN[39.492,3,422E-99] <- 5E+60 ## i1(Vy?_9`sk{*%fT.u__
## @7$_.s^9UA:7s!oC!s
bool zVV ## (qmar:;8$9_{[-b9,
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 265))

	def testCase266(self):
		input = '''
number VHqI[983.580,64.551] <- "6'"" ## <
func lD ()
	begin
		QkSt[kxZ] <- 4.061
		## nd9Lrvplx#DA
		## [2B
	end
var M5[297.644] <- "2"
func PRA (bool j9K, number o4P[0,6.434,24], bool ZXdG[2.799e+06])	return 12

'''
		expect = '''Error on line 9 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 266))

	def testCase267(self):
		input = '''
dynamic sM3b[40.416E+67,4.269E-16]
func H3rb (bool Gd)
	return 29e-63

func Fa (number LNw)	begin
		break
	end

'''
		expect = '''Error on line 2 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 267))

	def testCase268(self):
		input = '''
var bR[8e+39,8.445e-62] <- 415.186
number Rho ## ~ .B<kqP8`,WeIY}
bool clb <- 411.614E96 ## sBg U$z|H:UTP4!^eL|
func b5 (number xdtJ, number Cu[515E60,7E99])
	begin
		## g"Q
		break
	end

'''
		expect = '''Error on line 2 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 268))

	def testCase269(self):
		input = '''
## [
## >A~d
func lE7e (bool G0t, string sAk[27.968E22,93.452,6])
	return true

bool Y3QO ## ~}s9l3QSCD{
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 269))

	def testCase270(self):
		input = '''
## b6IWY}T76Op
func LVwY ()	return 5E+26

## T{L#hp;vMRayrZ:zu^
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 270))

	def testCase271(self):
		input = '''
## Dq]IJ*%-@uOwG{&&Nyu
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 271))

	def testCase272(self):
		input = '''
func ON ()	begin
		V2mf <- 9
		if ("D'"V'"'"") I13z(QRJ)[jA, "n", 650] <- 74
	end

'''
		expect = '''Error on line 5 col 1: end'''
		self.assertTrue(TestParser.test(input, expect, 272))

	def testCase273(self):
		input = '''
func H_E (number BilV, bool TBJq)
	return
func M1cW (number FRd[102.981E+65,1], dynamic c0, string LLeB)	return 87e+75

func Ybro (dynamic Mgr[4.382,75.514e91], dynamic Gf[303,803.923e+12])	return
'''
		expect = '''Error on line 4 col 38: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 273))

	def testCase274(self):
		input = '''
func xD (bool iU[4,95])
	return
dynamic Evn[2.979E98,471E45,2.109e62]
## 7WU</dnm,BL
number aX <- 132.983 ## ^YXi
func Xb ()
	return

'''
		expect = '''Error on line 4 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 274))

	def testCase275(self):
		input = '''
dynamic qpS[498.853] <- true ## yK "b$wv_
'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 275))

	def testCase276(self):
		input = '''
func xRLz (var HO0[634.161E+63])	begin
		## Wf><[mBWd
		## yFf!]73!O E|P%!? n^z
	end
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 276))

	def testCase277(self):
		input = '''
dynamic wvZt[5.466E40,760.646] <- false ## Hl!B-k"%gV=0
func liS_ (var Wcf[875.902,862.513], bool MG2[3.985e-07], dynamic dI[3E+36,0,8.471])	return 87.871

func SH (string eJss[3.361E+71])	return
func EH ()	return

## L>)r-J3zLw6-8X.a
'''
		expect = '''Error on line 2 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 277))

	def testCase278(self):
		input = '''
## Ufks><Q
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 278))

	def testCase279(self):
		input = '''
bool Zl[20]
func RBR (bool Sob6)
	return LtwE
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 279))

	def testCase280(self):
		input = '''
## tdJp1$u
func m8Y0 (var xLZD, number p7)	return
func YDCQ (string q9p[11])
	return "*6'"'"'""

## gY!1V-mx`+K?
dynamic Yzj0 <- "'""
'''
		expect = '''Error on line 3 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 280))

	def testCase281(self):
		input = '''
## kJyn4w~=S!+=
## XA aA
func SDOu ()
	return
dynamic S5FK ## Jsy!.D 1n.N9#?>4
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 281))

	def testCase282(self):
		input = '''
## =9Rq2a`^600r9
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 282))

	def testCase283(self):
		input = '''
## F#6A#$^yfIAf
bool z1 <- "N'"" ## B"/EW 8S
## S#GF
func V2 ()	return true
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 283))

	def testCase284(self):
		input = '''
func H_A7 (var DSl_[1E-55,4.623], bool MZ4g[85], string PU)	return "U5'""

var ffS[92.121,3e94,715.706] ## %]s?2S%YxIa
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 284))

	def testCase285(self):
		input = '''
func C3I (number LLL, number ipN)
	return

func Y0X (var Dsrn[141.844E21,878.198,0E-69], number YVyH)
	return false

func p7 (string B62, string wo)	begin
	end
## l
number fi[8.006e+20,222.776E92,89.459E-63] ## =xXj8ZlxM`
'''
		expect = '''Error on line 5 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 285))

	def testCase286(self):
		input = '''
number ZRDk ## HsIp6y*q}A/430
## nq0ATE
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 286))

	def testCase287(self):
		input = '''
## %GwOC<b
## T%xC[Cx
var x5m[2e94,540]
func AG (bool au_[5.072E+18,80e70,920.396], bool CIg[9.686E58], dynamic y2E1)
	begin
	end

var Hn <- bNJ ## $#Q;Qjw~Y<1t
'''
		expect = '''Error on line 4 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 287))

	def testCase288(self):
		input = '''
## <}qDw,Y"VEn6;&"HHY:
## ^k-g~*b]F^.9Y^ }
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 288))

	def testCase289(self):
		input = '''
bool RP74 <- true ## y]8y"//1
func q6w (dynamic Ea[849.527,429])	return
func DK (var iA0T[6E-20,933.700e+65], dynamic B1Ig, string wx[4.306e+26])
	begin
	end
bool uc <- 1
'''
		expect = '''Error on line 3 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 289))

	def testCase290(self):
		input = '''
## Xm82]cYD<)v"A7
## nGdscTP2t2DW=#0
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 290))

	def testCase291(self):
		input = '''
## ^nKCx
## mtp:Hw6xlx6$#/.IUi-M
func tKr (dynamic YZx0, number WJts[59.856e01])	return 3.872
## j028
'''
		expect = '''Error on line 4 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 291))

	def testCase292(self):
		input = '''
var Cw_[558.777E89]
'''
		expect = '''Error on line 2 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 292))

	def testCase293(self):
		input = '''
func PaL5 (number hnCL)	return false
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 293))

	def testCase294(self):
		input = '''
func RJW (dynamic Um[28.534,39.774e+15], string xhn, var cJ)
	return ":'"'"'"'""

func pQ3 (number jzt[526,157.820E-72], bool c3J[20.321])	begin
		## 1De:i<,F)`lbG1ia
		continue
	end
## )z3JH
string rTS
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 294))

	def testCase295(self):
		input = '''
number np[374,678.113] <- "'"'"+" ## ;
## T.C:
number Qv[46.776e-41,6.444,489e+25] <- "4j'"'""
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 295))

	def testCase296(self):
		input = '''
## ( 
dynamic t1 <- 85.999e94
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 296))

	def testCase297(self):
		input = '''
string PsUy <- 260E55 ## )yUR
func Tf (dynamic ST, number pY[7.595,663.524e+87,8e-04], number aX8k[89E-12])
	return "'"'"tr"

var wD4d[48.636,275] <- true ## vTQDdDK(nT?ZBy
func c4 ()
	begin
		## 6M4cJtY
	end
bool bEt ## ,uP?RqDJ4<0M6
'''
		expect = '''Error on line 3 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 297))

	def testCase298(self):
		input = '''
number Vm[35.632]
bool MO <- 59 ## 3+"
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 298))

	def testCase299(self):
		input = '''
func JK3 ()
	begin
		kq2 <- "n"
		## B
	end
func Mo ()	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 299))

	def testCase300(self):
		input = '''
string OOs[824.832,8e75] <- iJjN
string dJW[7] ## RXc=>[a21QK<:6kg^"E_
func QOP (var O4[9E59,51], string eSk, number eJ)
	return 438.588E-43

bool w34[191.647,9.103,5.579] ## X8{oT$y@1q(1
'''
		expect = '''Error on line 4 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 300))
