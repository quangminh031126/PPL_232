import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase): 
        
    def test_case_0(self):
        input = """ func main()
	return
 """
        expect = "successful"
        try:
            self.assertTrue(TestParser.test(input,expect,200))
        except:
            print("fail testcase 0")
    def test_case_1(self):
        input = """ dynamic a
var b<-2
func main()
	begin
if (b=2)
	a <- b
elif (b=3)
	a <- b*2 + 1
else a <- -1
return
end

 """
        expect = "successful"
        try:
            self.assertTrue(TestParser.test(input,expect,201))
        except:
            print("fail testcase 1")
        
    def test_case_2(self):
        input = """ func foo(number a) return a*a
func main() begin
number a
a<-0
writeString(foo(a))
return
end

 """
        expect = "successful"
        try:
            self.assertTrue(TestParser.test(input,expect,202))
        except:
            print("fail testcase 2")
        
    def test_case_3(self):
        input = """ func main()
func foo()
func f()
func main() return
func foo() return
func f() return

 """
        expect = "successful"
        try:
            self.assertTrue(TestParser.test(input,expect,203))
        except:
            print("fail testcase 3")
        
    def test_case_4(self):
        input = """ var a<-2
var b<-3

 """
        expect = "successful"
        try:
            self.assertTrue(TestParser.test(input,expect,204))
        except:
            print("fail testcase 4")
        
    def test_case_5(self):
        input = """ 




func main() begin





end


 """
        expect = "successful"
        try:
            self.assertTrue(TestParser.test(input,expect,205))
        except:
            print("fail testcase 5")
        
    def test_case_6(self):
        input = """ if (a=2) a<--3

 """
        expect = "Error on line 1 col 1: if"
        try:
            self.assertTrue(TestParser.test(input,expect,206))
        except:
            print("fail testcase 6")
        
    def test_case_7(self):
        input = """ func main() begin
var a<-2 dynamic b<-3
end


 """
        expect = "Error on line 2 col 9: dynamic"
        try:
            self.assertTrue(TestParser.test(input,expect,207))
        except:
            print("fail testcase 7")
        
    def test_case_8(self):
        input = """ func main() begin var a<-2 end

 """
        expect = "Error on line 1 col 19: var"
        try:
            self.assertTrue(TestParser.test(input,expect,208))
        except:
            print("fail testcase 8")
        
    def test_case_9(self):
        input = """ func main()
begin
##"comment"
string a <- "abcd"
var i<-0
for i until a=="abcd" by a<-a..."a"
writeString(a) end
 """
        expect = "Error on line 6 col 26: <-"
        try:
            self.assertTrue(TestParser.test(input,expect,209))
        except:
            print("fail testcase 9")
        
    def test_case_10(self):
        input = """ func main()
begin
##this test case is to test if else
dynamic a <- readNumber()
if ((a>0) and (a<10))
	a<-a*2
else if ((a>10) and (a<20) )
a<-a*3
else a <- a*4
return
end
 
 """
        expect = "successful"
        try:
            self.assertTrue(TestParser.test(input,expect,210))
        except:
            print("fail testcase 10")
        
    def test_case_11(self):
        input = """ ##if else case
func main()
begin
var a<-3
var b<-4
if (a<b) a<-b+a
if (b<a) 
	if (a=3) b<-b-a
	elif (b=4)
		if (a=7)
			b<-a%b
		else b<-b%a
	else b<-b-a
else b <- 3

end
 """
        expect = "successful"
        try:
            self.assertTrue(TestParser.test(input,expect,211))
        except:
            print("fail testcase 11")
        
    def test_case_12(self):
        input = """ var _globalVar <- -1e-9
number pi <- 3.1415926535897
dynamic e <- 2.71828182846
func exp(number n)
begin
var ans <- 1
var i<-0
for i until i=n by 1
ans*=e
return ans
end
func main()
begin
	var a<-exp(10)
end
 """
        expect = "Error on line 9 col 3: *"
        try:
            self.assertTrue(TestParser.test(input,expect,212))
        except:
            print("fail testcase 12")
        
    def test_case_13(self):
        input = """ var _globalVar <- -1e-9
number pi <- 3.1415926535897
dynamic e <- 2.71828182846
func exp(number n)
begin
var ans <- 1
var i<-0
for i until i=n by 1
ans <- ans*e
return ans
end
func main()
begin
var a = 2
print(exp(a))

end
 """
        expect = "Error on line 14 col 6: ="
        try:
            self.assertTrue(TestParser.test(input,expect,213))
        except:
            print("fail testcase 13")
        
    def test_case_14(self):
        input = """ ## var without init
var _globalVar <- -1e-9
dynamic e <- 2.71828182846
func exp(number n)
begin
var ans <- 1
var i<-0
for i until i=n by 1
ans<-ans*e
return ans
end
func sum(number a[100],number n)
begin
var ans
var i <- 0
for 
end
func softmax(number a[100],number n)
begin

end
func main()
begin

end
 """
        expect = "Error on line 14 col 8: \n"
        try:
            self.assertTrue(TestParser.test(input,expect,214))
        except:
            print("fail testcase 14")
        
    def test_case_15(self):
        input = """ ##dynamic function
dynamic func a() return 3

 """
        expect = "Error on line 2 col 8: func"
        try:
            self.assertTrue(TestParser.test(input,expect,215))
        except:
            print("fail testcase 15")
        
    def test_case_16(self):
        input = """ ##diffifcult expresion
func root(number n)
func exp(number n)
func log(number n)
number pi <- 3.14
number True <- 1
bool a <- root(exp(3*pi)-log(pi%2)) = True and ("abcd" == "acc'""..."a")
 
 """
        expect = "successful"
        try:
            self.assertTrue(TestParser.test(input,expect,216))
        except:
            print("fail testcase 16")
        
    def test_case_17(self):
        input = """ ##None assoc expression
var a<- "a"..."b"..."c"

 """
        expect = "Error on line 2 col 17: ..."
        try:
            self.assertTrue(TestParser.test(input,expect,217))
        except:
            print("fail testcase 17")
        
    def test_case_18(self):
        input = """ ##None assoc expression
dynamic a
func main()
begin
a<- "a"..."b"=="ab"=true
end

 """
        expect = "Error on line 5 col 19: ="
        try:
            self.assertTrue(TestParser.test(input,expect,218))
        except:
            print("fail testcase 18")
        
    def test_case_19(self):
        input = """ ## None assoc 
func main() 
					begin
number a<- -3+2*sqrt(3)
dynamic s
s <- str(a)..."cde" == "ghi" == "mmm"
end
 """
        expect = "Error on line 6 col 29: =="
        try:
            self.assertTrue(TestParser.test(input,expect,219))
        except:
            print("fail testcase 19")
        
    def test_case_20(self):
        input = """ ##array check
func main( )
begin
number arr <- [1,2,3]
end

 """
        expect = "successful"
        try:
            self.assertTrue(TestParser.test(input,expect,220))
        except:
            print("fail testcase 20")
        
    def test_case_21(self):
        input = """ ## array check
func main()
begin
var a[2,3] = [[0.1,1e9,3.14e-23],[-2,-3,-4]]

end
 """
        expect = "Error on line 4 col 5: ["
        try:
            self.assertTrue(TestParser.test(input,expect,221))
        except:
            print("fail testcase 21")
        
    def test_case_22(self):
        input = """ ## array test
func root(number n)
func main() 
begin
var a<-2
number b<-3
number c<-5
number arr[2,3] <- [[-2,root(3.12),-3.14E-88],[a,b,c]]
end
 """
        expect = "successful"
        try:
            self.assertTrue(TestParser.test(input,expect,222))
        except:
            print("fail testcase 22")
        
    def test_case_23(self):
        input = """ ## func declare
func root(dynamic a)
 """
        expect = "Error on line 2 col 10: dynamic"
        try:
            self.assertTrue(TestParser.test(input,expect,223))
        except:
            print("fail testcase 23")
        
    def test_case_24(self):
        input = """ ##func declare
func test[number a,string b] 
begin

end
 """
        expect = "Error on line 2 col 9: ["
        try:
            self.assertTrue(TestParser.test(input,expect,224))
        except:
            print("fail testcase 24")
        
    def test_case_25(self):
        input = """ ## end line in statement
func len(string s)
begin
var i<-0
for i until s[i] by 1
begin
end
return i
end
func main()
begin
string a<-"we will check the end of statement is \\n" ##correct statement
if (len(s)<3) printString("this is short string") else
printString("this is long string")
end

 """
        expect = "Error on line 13 col 50: else"
        try:
            self.assertTrue(TestParser.test(input,expect,225))
        except:
            print("fail testcase 25")
        
    def test_case_26(self):
        input = """ ##if else check
func main() begin
if (a>b*c%d)
	if ((s..."##tesecase")=="abc") 

	a <- (k*-3 = -15) and not (true or false)

	else if ((s == "ghi") or (s == "hello")) b<- -2*b
var error
end

 """
        expect = "Error on line 9 col 10: \n"
        try:
            self.assertTrue(TestParser.test(input,expect,226))
        except:
            print("fail testcase 26")
        
    def test_case_27(self):
        input = """ ##if else check
func main() begin
if (a>b*c%d)
	if ((s..."##tesecase")=="abc") 

	a <- (k*-3 = -15) and not (true or false)

	elif (true)
		if ((s == "ghi") or (s == "hello")) b<- -2*b
		elif (a) begin
		a <- (a=a)
		end
	else a<- -2*a
elif (s== "elif")
s <- "else"
else s<-"elif"
var error
end
 """
        expect = "Error on line 17 col 10: \n"
        try:
            self.assertTrue(TestParser.test(input,expect,227))
        except:
            print("fail testcase 27")
        
    def test_case_28(self):
        input = """ ##if else check
func main() begin
if (a>b*c%d)
	if ((s..."##tesecase")=="abc") 

	a <- (k*-3 = -15) and not (true or false)

	elif (true)
		if ((s == "ghi") or (s == "hello")) b<- -2*b
		elif (a) begin
		a <- (a=a)
		end
	else a<- -2*a
elif (s== "elif")
s <- "else"

var error
end
 """
        expect = "Error on line 17 col 10: \n"
        try:
            self.assertTrue(TestParser.test(input,expect,228))
        except:
            print("fail testcase 28")
        
    def test_case_29(self):
        input = """ ##if else check
func main() begin
if (a>b*c%d)
	if ((s..."##tesecase")=="abc") 

	a <- (k*-3 = -15) and not (true or false)

	elif (true)
		if ((s == "ghi") or (s == "hello")) b<- -2*b
		elif (a) begin
		a <- (a=a)
		end
	else a<- -2*a
elif (s== "elif")
s <- "else"
else if (true) if (true) if (true) callFunc()
else __callfunc()
var error
end
 """
        expect = "Error on line 18 col 10: \n"
        try:
            self.assertTrue(TestParser.test(input,expect,229))
        except:
            print("fail testcase 29")
        
        
    def test_case_30(self):
        input = """ ##for in for
func main()
begin
var i<-0
var j<-0
var k<-0
number x<-readNumber()
for i until i<x/2 by 1 for j until j<x/2 by 1 for k until k<x/2 by 1 x <- x + 1
end

 """
        expect = "successful"
        try:
            self.assertTrue(TestParser.test(input,expect,230))
        except:
            print("fail testcase 30")
        
    def test_case_31(self):
        input = """ ##for in for
func main()
begin
var i<-0
var j<-0
var k<-0
number x<-readNumber()
for i until i<x/2 by 1 
for j until j<x/2 by 1 
for k until k<x/2 by 1 
x <- x + 1
end


 """
        expect = "successful"
        try:
            self.assertTrue(TestParser.test(input,expect,231))
        except:
            print("fail testcase 31")
        
    def test_case_32(self):
        input = """ ##mergesort with zcode
func merge(number arr[100], number left, number mid, number right)
begin
    number i
    number j
    number k
    number n1 <- mid - left + 1
    number n2 <- right - mid
    number L[100]
    number R[100]

    for i until i < n1 by 1
        L[i] <- arr[left + i]

    for j until j < n2 by 1
        R[j] <- arr[mid + 1 + j]

    i <- 0
    j <- 0
    k <- left

    for k until k <= right by 1
    begin
        if (i < n1 and (j >= n2 or L[i] <= R[j]))
        begin
            arr[k] <- L[i]
            i <- i + 1
        end
        else begin
            arr[k] <- R[j]
            j <- j + 1
        end
    end
end

func mergeSort(number arr[100], number left, number right)
begin
    if (left < right)
    begin
        number mid <- (left + right) / 2

        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)

        merge(arr, left, mid, right)
    end
end
 """
        expect = "Error on line 24 col 40: <="
        try:
            self.assertTrue(TestParser.test(input,expect,232))
        except:
            print("fail testcase 32")
        
    def test_case_33(self):
        input = """ ##mergesort with zcode
func merge(number arr[100], number left, number mid, number right)
begin
    number i
    number j
    number k
    number n1 <- mid - left + 1
    number n2 <- right - mid
    number L[100]
    number R[100]

    for i until i < n1 by 1
        L[i] <- arr[left + i]

    for j until j < n2 by 1
        R[j] <- arr[mid + 1 + j]

    i <- 0
    j <- 0
    k <- left

    for k until k <= right by 1
    begin
        if ((i < n1) and (j >= n2) or (L[i] <= R[j]))
        begin
            arr[k] <- L[i]
            i <- i + 1
        end
        else begin
            arr[k] <- R[j]
            j <- j + 1
        end
    end
end

func mergeSort(number arr[100], number left, number right)
begin
    if (left < right)
    begin
        number mid <- (left + right) / 2

        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)

        merge(arr, left, mid, right)
    end
end

 """
        expect = "successful"
        try:
            self.assertTrue(TestParser.test(input,expect,233))
        except:
            print("fail testcase 33")
        
    def test_case_34(self):
        input = """ var dynamic <- -1
 """
        expect = "Error on line 1 col 5: dynamic"
        try:
            self.assertTrue(TestParser.test(input,expect,234))
        except:
            print("fail testcase 34")
        
    def test_case_35(self):
        input = """ func foo(a,b) return 1
 """
        expect = "Error on line 1 col 10: a"
        try:
            self.assertTrue(TestParser.test(input,expect,235))
        except:
            print("fail testcase 35")
        
    def test_case_36(self):
        input = """ func main() ##main function
begin

end
 """
        expect = "successful"
        try:
            self.assertTrue(TestParser.test(input,expect,236))
        except:
            print("fail testcase 36")
        
    def test_case_37(self):
        input = """ func main() begin
true<-false
return
end
 """
        expect = "Error on line 2 col 0: true"
        try:
            self.assertTrue(TestParser.test(input,expect,237))
        except:
            print("fail testcase 37")
        
    def test_case_38(self):
        input = """ func main() begin
bool a <- foo((x < -2) or (("a'""..."a\\'") == "a'"a\\'"))[3,2]
end
 """
        expect = "successful"
        try:
            self.assertTrue(TestParser.test(input,expect,238))
        except:
            print("fail testcase 38")
        
    def test_case_39(self):
        input = """ func main() begin
bool a <- foo((x <-2) or (("a'""..."a\\'") == "a'"a\\'"))[3,2]
end

 """
        expect = "Error on line 2 col 17: <-"
        try:
            self.assertTrue(TestParser.test(input,expect,239))
        except:
            print("fail testcase 39")
        
    def test_case_40(self):
        input = """ func main() begin
for _ until _ by _
if (_) break
__()
1
end

 """
        expect = "Error on line 5 col 0: 1"
        try:
            self.assertTrue(TestParser.test(input,expect,240))
        except:
            print("fail testcase 40")
        
    def test_case_41(self):
        input = """ func main() begin
number numbeR[1,2,3,4,5]
var a <- ((((numbeR[0])[1])[2])[3])[4] = numbeR[0,1,2,3,4]
end

 """
        # expect = "successful"
        expect = "Error on line 3 col 23: ["
        try:
            self.assertTrue(TestParser.test(input,expect,241))
        except:
            print("fail testcase 41")
        
    def test_case_42(self):
        input = """ func main()
begin
number arr[]
end
 """
        expect = "Error on line 3 col 11: ]"
        try:
            self.assertTrue(TestParser.test(input,expect,242))
        except:
            print("fail testcase 42")
        
    def test_case_43(self):
        input = """ 
func foo(number a) begin
if (a=1 or a=0) return 1
return a*foo(a)
end

number arr[2,3] <- [[1,2,3],[5*6,7%2,-3.13E-6*foo(foo(3))]

func main()
begin
number a<- arr[foo(1),foo(3)%3]
return
end
 """
        expect = "Error on line 3 col 12: ="
        try:
            self.assertTrue(TestParser.test(input,expect,243))
        except:
            print("fail testcase 43")
        
    def test_case_44(self):
        input = """ 
func foo(number a) begin
if ((a=1) or (a=0)) return 1
return a*foo(a)
end

number arr[2,3] <- [[1,2,3],[5*6,7%2,-3.13E-6*foo(foo(3))]

func main()
begin
number a<- arr[foo(1),foo(3)%3]*(-1
return
end

 """
        expect = "Error on line 7 col 59: \n"
        try:
            self.assertTrue(TestParser.test(input,expect,244))
        except:
            print("fail testcase 44")
        
    def test_case_45(self):
        input = """ 
func foo(number a) begin
if ((a=1) or (a=0)) return 1
return a*foo(a)
end

number arr[2,3] <- [[1,2,3],[5*6,7%2,-3.13E-6*foo(foo(3))]]

func main()
begin
number a<- arr[foo(1),foo(3)%3]*(-1
return
end


 """
        expect = "Error on line 11 col 36: \n"
        try:
            self.assertTrue(TestParser.test(input,expect,245))
        except:
            print("fail testcase 45")
        
    def test_case_46(self):
        input = """ func main()
begin
var a,b,c
end
 """
        expect = "Error on line 3 col 5: ,"
        try:
            self.assertTrue(TestParser.test(input,expect,246))
        except:
            print("fail testcase 46")
        
    def test_case_47(self):
        input = """ func main() 
begin
dynamic a
a <- ((A or B and C + 3*2%4/3)<=(not(-1+foo(x+y*(z-1))))...(x!=y)
end
 """
        expect = "Error on line 4 col 66: \n"
        try:
            self.assertTrue(TestParser.test(input,expect,247))
        except:
            print("fail testcase 47")
        
    def test_case_48(self):
        input = """ func main()
begin
number _ <- readNumber()
number __<- readNumber()
for _ until _*_ = _+_*_-2*_ by _+_
if (_) 
for _ until _/(_*_)%_ < _/(_*_+_) by _/_
if (_*_<_+_) begin
end
elif (__<_) if ((__+_/__ = _%__) and (__*_<-1)) for _ until _/(_*_)%_ < _/(_*_+_) by _/_ if (true) break 
else continue
else break
elif (true) continue
else break
end

 """
        expect = "Error on line 10 col 42: <-"
        try:
            self.assertTrue(TestParser.test(input,expect,248))
        except:
            print("fail testcase 48")
        
    def test_case_49(self):
        input = """ func main()
begin
number _ <- readNumber()
number __<- readNumber()
for _ until _*_ = _+_*_-2*_ by _+_
if (_) 
for _ until _/(_*_)%_ < _/(_*_+_) by _/_
if (_*_<_+_) begin
end
elif (__<_) if ((__+_/__ = _%__) and (__*_< -1)) for _ until _/(_*_)%_ < _/(_*_+_) by _/_ if (true) break 
else continue
else break
elif (true) continue
else break
end
 """
        expect = "successful"
        try:
            self.assertTrue(TestParser.test(input,expect,249))
        except:
            print("fail testcase 49")
        
    def test_case_50(self):
        input = """ func main() 
begin
dynamic a
a <- ((A or B and C + 3*2%4/3)<=(not(-1+foo(x+y*(z-1)))))...(x!=y)
end
 """
        expect = "successful"
        try:
            self.assertTrue(TestParser.test(input,expect,250))
        except:
            print("fail testcase 50")
        
    def test_case_51(self):
        input = """ continue
func main()
 """
        expect = "Error on line 1 col 1: continue"
        try:
            self.assertTrue(TestParser.test(input,expect,251))
        except:
            print("fail testcase 51")
        
    def test_case_52(self):
        input = """ func func()
 """
        expect = "Error on line 1 col 6: func"
        try:
            self.assertTrue(TestParser.test(input,expect,252))
        except:
            print("fail testcase 52")
        
    def test_case_53(self):
        input = """ func main()




begin
if (a)
if (b)
c <- 1
else c <- 2
end
 """
        expect = "successful"
        try:
            self.assertTrue(TestParser.test(input,expect,253))
        except:
            print("fail testcase 53")
        
    def test_case_54(self):
        input = """ func main()
begin
number _ <- readNumber()
number __<- readNumber()
for _ until _*_ = _+_*_-2*_ by _+_
if (_) 
for _ until _/(_*_)%_ < _/(_*_+_) by _/_
if (_*_<_+_) begin
end
elif (__<_) if ((__+_/__ = _%__) and (__*_< -1)) for _ until _/(_*_)%_ < _/(_*_+_) by _/_ if (true) break 
else continue
else break
elif (true) continue
end
 """
        expect = "successful"
        try:
            self.assertTrue(TestParser.test(input,expect,254))
        except:
            print("fail testcase 54")
        
    def test_case_55(self):
        input = """ ##for in for
func main()
begin
var i<-0
var j<-0
var k<-0
number x<-readNumber()
for i until i<x/2 by 1 for j until j<x/2 by 1 for k until k<x/2 by 1 if (i<j) if (k<i) break
end
 """
        expect = "successful"
        try:
            self.assertTrue(TestParser.test(input,expect,255))
        except:
            print("fail testcase 55")
    def test_case_56(self):
        input = """ ##for in for
func main()
begin
var i<-0
var j<-0
var k<-0
number x<-readNumber()
for i until i<x/2 by 1 for j until j<x/2 by 1 for k until k<x/2 by 1 if (i<j) if (k<i) break
end"""
        expect = "Error on line 9 col 3: <EOF>"
        try:
            self.assertTrue(TestParser.test(input,expect,256))
        except:
            print("fail testcase 56")
        
    def test_case_57(self):
        input = """ func foo()
func f()
func main() return
func foo() return
func _____________f_____() 




	return
 """
        expect = "successful"
        try:
            self.assertTrue(TestParser.test(input,expect,257))
        except:
            print("fail testcase 57")
        
    def test_case_58(self):
        input = """ func returnArray()
	return [1,2,3,4]
_
 """
        expect = "Error on line 3 col 0: _"
        try:
            self.assertTrue(TestParser.test(input,expect,258))
        except:
            print("fail testcase 58")
        
    def test_case_59(self):
        input = """ func abc/def()
	return "I love PPL"
func main()
begin
printString(abc/def())
end
 """
        expect = "Error on line 1 col 9: /"
        try:
            self.assertTrue(TestParser.test(input,expect,259))
        except:
            print("fail testcase 59")
        
    def test_case_60(self):
        input = """ func abcdef()
	return "I love PPL"
func main()

printString(abcdef())
 """
        expect = "Error on line 5 col 0: printString"
        try:
            self.assertTrue(TestParser.test(input,expect,260))
        except:
            print("fail testcase 60")
        
    def test_case_61(self):
        input = """ ##index op
func main() begin
number a<- "abc"[0]
end
 """
        expect = "Error on line 3 col 16: ["
        try:
            self.assertTrue(TestParser.test(input,expect,261))
        except:
            print("fail testcase 61")
        
    def test_case_62(self):
        input = """ func jump(number address,number reg) 
	begin
reg<-address
return reg
end func main() begin
number reg
printString(jump(123,reg))
end
 """
        expect = "Error on line 5 col 4: func"
        try:
            self.assertTrue(TestParser.test(input,expect,262))
        except:
            print("fail testcase 62")
        
    def test_case_63(self):
        input = """ func main() begin
number arr[3] <- []
end
 """
        expect = "Error on line 2 col 18: ]"
        try:
            self.assertTrue(TestParser.test(input,expect,263))
        except:
            print("fail testcase 63")
        
    def test_case_64(self):
        input = """ func foo( number n,
string s
)
 """
        expect = "Error on line 1 col 21: \n"
        try:
            self.assertTrue(TestParser.test(input,expect,264))
        except:
            print("fail testcase 64")
        
    def test_case_65(self):
        input = """ func foo(number n ##this is a function )
begin

end

 """
        expect = "Error on line 1 col 42: \n"
        try:
            self.assertTrue(TestParser.test(input,expect,265))
        except:
            print("fail testcase 65")
        
    def test_case_66(self):
        input = """ ##comment
dynamic d
var k<-result = ((not a[1] * (b - c[2]) + d / e) == f % g) and (-h >= i[3, 4] or not (j < k[0, 1] * 2)) or not not l[5, 6] == m + n
func main() begin
writeNumber(k)
end


 """
        expect = "Error on line 3 col 123: =="
        try:
            self.assertTrue(TestParser.test(input,expect,266))
        except:
            print("fail testcase 66")
        
    def test_case_67(self):
        input = """ func main() begin
bool result <- (
    (not is_prime(get_nth_element(get_sublist(matrix, 2), find_index(numbers, 8)))) 
    and (
        abs(sum_elements(vector) * 3) / custom_function(5, -7) 
        == power_func(sqrt_func(a[2]), 4) % 10
    )
) or (
    bitwise_shift(left_shift(32, 2), right_shift(64, 3)) > bitwise_and(15, bitwise_or(7, 9))
)

end
 """
        expect = "Error on line 2 col 17: \n"
        try:
            self.assertTrue(TestParser.test(input,expect,267))
        except:
            print("fail testcase 67")
        
    def test_case_68(self):
        input = """ func main ()
begin
begin
begin
end
end
end
 """
        expect = "successful"
        try:
            self.assertTrue(TestParser.test(input,expect,268))
        except:
            print("fail testcase 68")
        
    def test_case_69(self):
        input = """ func main()
begin
number dump
func help() begin

end
end
 """
        expect = "Error on line 4 col 0: func"
        try:
            self.assertTrue(TestParser.test(input,expect,269))
        except:
            print("fail testcase 69")
        
    def test_case_70(self):
        input = """ func main()                                            begin
if (a or b) == c 
return











end
 """
        expect = "Error on line 2 col 12: =="
        try:
            self.assertTrue(TestParser.test(input,expect,270))
        except:
            print("fail testcase 70")
        
    def test_case_71(self):
        input = """ bool a[2,4]<- [[1,2,3,4],[2,3],2]
 """
        expect = "successful"
        try:
            self.assertTrue(TestParser.test(input,expect,271))
        except:
            print("fail testcase 71")
        
    def test_case_72(self):
        input = """ number a[2,3] <- [[1,2,3],[1,2,3]]
 """
        expect = "successful"
        try:
            self.assertTrue(TestParser.test(input,expect,272))
        except:
            print("fail testcase 72")
        
    def test_case_73(self):
        input = """ var pi <- 3.14
number a<- -3.14ea+14


 """
        expect = "Error on line 2 col 16: ea"
        try:
            self.assertTrue(TestParser.test(input,expect,273))
        except:
            print("fail testcase 73")
        
    def test_case_74(self):
        input = """ func main()
begin
number b<-1
var a<- --------[1,2]*----------------b
end


 """
        expect = "successful"
        try:
            self.assertTrue(TestParser.test(input,expect,274))
        except:
            print("fail testcase 74")
        
    def test_case_75(self):
        input = """ func main()
begin
bool a<- -_-_------_-_*-_<---------_+_
end


 """
        expect = "Error on line 3 col 25: <-"
        try:
            self.assertTrue(TestParser.test(input,expect,275))
        except:
            print("fail testcase 75")
        
    def test_case_76(self):
        input = """ func main()
begin
number i<-0
if (a or b and c)
	if (a and b or c)
for i until i==k by a[1]
elif (k==1) return
end
 """
        expect = "Error on line 7 col 0: elif"
        try:
            self.assertTrue(TestParser.test(input,expect,276))
        except:
            print("fail testcase 76")
        
    def test_case_77(self):
        input = """dynamic a"""
        expect = "Error on line 1 col 9: <EOF>"
        try:
            self.assertTrue(TestParser.test(input,expect,277))
        except:
            print("fail testcase 77")
        
    def test_case_78(self):
        input = """ ##comment
dynamic d
var k<-result = ((not a[1] * (b - c[2]) + d / e) == f % g) and (-h >= i[3, 4] or not (by < k[0, 1] * 2)) or not not l[5, 6] == m + n
func main() begin
writeNumber(k)
end
 """
        expect = "Error on line 3 col 86: by"
        try:
            self.assertTrue(TestParser.test(input,expect,278))
        except:
            print("fail testcase 78")
        
    def test_case_79(self):
        input = """ string s <- "abc '"..."...a"abc"
 """
        expect = "Error on line 1 col 28: abc"
        try:
            self.assertTrue(TestParser.test(input,expect,279))
        except:
            print("fail testcase 79")
        
    def test_case_80(self):
        input = """ ##string test
func str(number n,bool b<-True)
func main()
begin
string s<- str(True)
end
 """
        expect = "Error on line 2 col 24: <-"
        try:
            self.assertTrue(TestParser.test(input,expect,280))
        except:
            print("fail testcase 80")
        
    def test_case_81(self):
        input = """ ##string test
func str(number n,bool b)
func main()
begin
string s<- str(null,True)..."In zcode we have \\''"..."## to start a comment " if
end
 """
        expect = "successful"
        try:
            self.assertTrue(TestParser.test(input,expect,281))
        except:
            print("fail testcase 81")
        
    def test_case_82(self):
        input = """ ##check name rule
func 12abc()
func main
 """
        expect = "Error on line 2 col 5: 12"
        try:
            self.assertTrue(TestParser.test(input,expect,282))
        except:
            print("fail testcase 82")
        
    def test_case_83(self):
        input = """ ##check keyword rule
func foo(number start,number end)
func main()
return
 """
        expect = "Error on line 2 col 29: end"
        try:
            self.assertTrue(TestParser.test(input,expect,283))
        except:
            print("fail testcase 83")
        
    def test_case_84(self):
        input = """ dynamic a[3,4,True] <- [2,3,4,5,6,7,8]
 """
        expect = "Error on line 1 col 10: ["
        try:
            self.assertTrue(TestParser.test(input,expect,284))
        except:
            print("fail testcase 84")
        
    def test_case_85(self):
        input = """ 
number line[1e9] <- createArray(10)


 """
        # expect = "successful"
        expect = "Error on line 2 col 20: createArray"
        try:
            self.assertTrue(TestParser.test(input,expect,285))
        except:
            print("fail testcase 85")
        
    def test_case_86(self):
        input = """ string a[10] <- "abc"
 """
        expect = "Error on line 1 col 17: abc"
        # expect = "successful"
        try:
            self.assertTrue(TestParser.test(input,expect,286))
        except:
            print("fail testcase 86")
        
    def test_case_87(self):
        input = """ dynamic a
var b<-2
func main()
	begin
if (b=2)
	a <- b
elif (b=3)
	a <- b*2 + 1
else if(True) a <- -1
return
end
 """
        expect = "successful"
        try:
            self.assertTrue(TestParser.test(input,expect,287))
        except:
            print("fail testcase 87")
        
    def test_case_88(self):
        input = """ dynamic a
var b<-2
func main()
	begin
if (b=2)
	a <- b
elif (b=3)
	a <- b*2 + 1
else if(True) a <- -1
elif (isTrue()) if (ok) begin
 end
return
end

 """
        expect = "successful"
        try:
            self.assertTrue(TestParser.test(input,expect,288))
        except:
            print("fail testcase 88")
        
    def test_case_89(self):
        input = """ func main()
begin
if () return
end
 """
        expect = "Error on line 3 col 4: )"
        try:
            self.assertTrue(TestParser.test(input,expect,289))
        except:
            print("fail testcase 89")
        
    def test_case_90(self):
        input = """ "I love PPL" == "10 mark PPL"
 """
        expect = "Error on line 1 col 1: I love PPL"
        try:
            self.assertTrue(TestParser.test(input,expect,290))
        except:
            print("fail testcase 90")
        
    def test_case_91(self):
        input = """ func main()
begin
for i until i by i for j until j by j for k until k by k for l until l by l for 1 until 1 by 1 pass
end
 """
        expect = "Error on line 3 col 80: 1"
        try:
            self.assertTrue(TestParser.test(input,expect,291))
        except:
            print("fail testcase 91")
        
    def test_case_92(self):
        input = """ ## func declare
func root(var a)
 """
        expect = "Error on line 2 col 10: var"
        try:
            self.assertTrue(TestParser.test(input,expect,292))
        except:
            print("fail testcase 92")
        
    def test_case_93(self):
        input = """ func _____(number __, string ___, bool ____)
begin
if (____) ___ <- ___...str(__)
else ___<-___..."_______"
return ___
end
func main()
begin
dynamic __<-1
bool ____<-True
string ___<-"________"
__ <- (___..._____(__,___,_____))..."________"
return __
end
 """
        expect = "successful"
        try:
            self.assertTrue(TestParser.test(input,expect,293))
        except:
            print("fail testcase 93")
        
    def test_case_94(self):
        input = """ func _____(number __, string ___, bool ____)
begin
if (____) ___ <- ___...str(__)
else ___<-___..."_______"
return ___
end
func main()
begin
number __________ <-10
number __[___________]<-1
bool ____<-True
string ___<-"________"
__ <- (___..._____(__,___,_____))..."________"
return __
end

 """
        expect = "Error on line 10 col 10: ___________"
        try:
            self.assertTrue(TestParser.test(input,expect,294))
        except:
            print("fail testcase 94")
        
    def test_case_95(self):
        input = """ func main()
begin
for <number-variable> until <condition expression> by <update-expression>
<statement>
end
 """
        expect = "Error on line 3 col 4: <"
        try:
            self.assertTrue(TestParser.test(input,expect,295))
        except:
            print("fail testcase 95")
        
    def test_case_96(self):
        input = """ func __init__(self)
	return 1
 """
        expect = "Error on line 1 col 15: self"
        try:
            self.assertTrue(TestParser.test(input,expect,296))
        except:
            print("fail testcase 96")
        
    def test_case_97(self):
        input = """ number foo(2) <- 3
 """
        expect = "Error on line 1 col 11: ("
        try:
            self.assertTrue(TestParser.test(input,expect,297))
        except:
            print("fail testcase 97")
        
    def test_case_98(self):
        input = """ func main()
begin
[1,2,3] <- [4,5,6]
end
 """
        expect = "Error on line 3 col 0: ["
        try:
            self.assertTrue(TestParser.test(input,expect,298))
        except:
            print("fail testcase 98")
        
    def test_case_99(self):
        input = """ func main()
begin
dynamic a <- [-1<3,foo(4),[1,2,3]]
end
 """
        expect = "successful"
        try:
            self.assertTrue(TestParser.test(input,expect,299))
        except:
            print("fail testcase 99")
        