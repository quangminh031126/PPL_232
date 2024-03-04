import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase): 

    def test_case_0(self):
        input = """ and ] string break	var	elif begin ...
true
return if
= elif - string	break
>	and break
[	if string until /	] >=	begin a1	until	until - continue	/	begin
if	( not	[	var
or %
= != begin	<
% == a1	14e-49 , break	for -
>= true
89.42 number
    """
        expect = "and,],string,break,var,elif,begin,...,\n,true,\n,return,if,\n,=,elif,-,string,break,\n,>,and,break,\n,[,if,string,until,/,],>=,begin,a1,until,until,-,continue,/,begin,\n,if,(,not,[,var,\n,or,%,\n,=,!=,begin,<,\n,%,==,a1,14e-49,,,break,for,-,\n,>=,true,\n,89.42,number,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,100))
        except:
            print("fail testcase 0")
        
    def test_case_1(self):
        input = """ < <= ...	> (
break	not
a1 <=	true	%	for	>=	for func	dynamic begin	[	< and false ...	else
by	...
    """
        expect = "<,<=,...,>,(,\n,break,not,\n,a1,<=,true,%,for,>=,for,func,dynamic,begin,[,<,and,false,...,else,\n,by,...,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,101))
        except:
            print("fail testcase 1")
        
    def test_case_2(self):
        input = """	until , !=	-
< until 98E5476
+ false or
begin =	[ end < string +
*
dynamic
<-	a1	end	not for true else	/ and
< -	elif >= by
== func for
return	func	... [ var func and	<
a1	or elif	number	bool ==
< >= string	%
<= string continue <	"abcd"
    """
        expect = "until,,,!=,-,\n,<,until,98E5476,\n,+,false,or,\n,begin,=,[,end,<,string,+,\n,*,\n,dynamic,\n,<-,a1,end,not,for,true,else,/,and,\n,<,-,elif,>=,by,\n,==,func,for,\n,return,func,...,[,var,func,and,<,\n,a1,or,elif,number,bool,==,\n,<,>=,string,%,\n,<=,string,continue,<,abcd,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,102))
        except:
            print("fail testcase 2")
        
    def test_case_3(self):
        input = """	until	)	or	return	<
break	]
( ) <=	78.3
bool
...
=	<=	false != var ==	[	< if	func	
	bool	true	/
)
, / not	*	92.13	== var	func for !=
    """
        expect = "until,),or,return,<,\n,break,],\n,(,),<=,78.3,\n,bool,\n,...,\n,=,<=,false,!=,var,==,[,<,if,func,\n,bool,true,/,\n,),\n,,,/,not,*,92.13,==,var,func,for,!=,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,103))
        except:
            print("fail testcase 3")
        
    def test_case_4(self):
        input = """ +	/ [ - number a1	true
begin	bool
<-	93.6 ...
+	=
or
string >=	for	( ,
%
dynamic >= continue	and false	var	func a1	+	) <- a1 <
=	] break	"abcd" var	<-	* ,	% until string	not - ( ( % by elif	not	func var func dynamic
    """
        expect = "+,/,[,-,number,a1,true,\n,begin,bool,\n,<-,93.6,...,\n,+,=,\n,or,\n,string,>=,for,(,,,\n,%,\n,dynamic,>=,continue,and,false,var,func,a1,+,),<-,a1,<,\n,=,],break,abcd,var,<-,*,,,%,until,string,not,-,(,(,%,by,elif,not,func,var,func,dynamic,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,104))
        except:
            print("fail testcase 4")
        
    def test_case_5(self):
        input = """ begin ( elif	else % not	end	!=
/ end 
 begin "abcd"	=	, bool continue	begin /
<	and	+ false	/ continue continue <-
break >=	false
< >	dynamic	) number	>	* by	else break [ dynamic ] continue
and	( [	>
-	
	break	!=	* number for break not
) begin	return >	>
by	"abcd"
if
elif	elif - var	/ < 
 
	return until	break	==	and (	< ]	<-
<
    """
        expect = "begin,(,elif,else,%,not,end,!=,\n,/,end,\n,begin,abcd,=,,,bool,continue,begin,/,\n,<,and,+,false,/,continue,continue,<-,\n,break,>=,false,\n,<,>,dynamic,),number,>,*,by,else,break,[,dynamic,],continue,\n,and,(,[,>,\n,-,\n,break,!=,*,number,for,break,not,\n,),begin,return,>,>,\n,by,abcd,\n,if,\n,elif,elif,-,var,/,<,\n,\n,return,until,break,==,and,(,<,],<-,\n,<,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,105))
        except:
            print("fail testcase 5")
        
    def test_case_6(self):
        input = """ by or	... true	<=	until	elif elif ] <=	-	continue ] string dynamic	"abcd" elif	number	/ for / by false * ) )	bool not	= bool or	number / >= by (
    """
        expect = "by,or,...,true,<=,until,elif,elif,],<=,-,continue,],string,dynamic,abcd,elif,number,/,for,/,by,false,*,),),bool,not,=,bool,or,number,/,>=,by,(,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,106))
        except:
            print("fail testcase 6")
        
    def test_case_7(self):
        input = """ bool
else var
28.48E1444 92.66
>= < break	<- a1 func	<
and	begin * <- by > continue ,
begin and
    """
        expect = "bool,\n,else,var,\n,28.48E1444,92.66,\n,>=,<,break,<-,a1,func,<,\n,and,begin,*,<-,by,>,continue,,,\n,begin,and,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,107))
        except:
            print("fail testcase 7")
        
    def test_case_8(self):
        input = """	%	%	<= != ) number not and	for	a1 %
=	for
for var
until * elif not ,	a1
"abcd" and false , bool
]
...	<	else
return , number [ >=
==	= %	= ...	not until	false [ - dynamic
bool	number begin > elif , + =	=
, 
 > [ var	>=	!=
begin else	...	not
[ var
continue	end	*	func false	) true	begin	and not or number break ( true bool	and	by	if	* elif
    """
        expect = "%,%,<=,!=,),number,not,and,for,a1,%,\n,=,for,\n,for,var,\n,until,*,elif,not,,,a1,\n,abcd,and,false,,,bool,\n,],\n,...,<,else,\n,return,,,number,[,>=,\n,==,=,%,=,...,not,until,false,[,-,dynamic,\n,bool,number,begin,>,elif,,,+,=,=,\n,,,\n,>,[,var,>=,!=,\n,begin,else,...,not,\n,[,var,\n,continue,end,*,func,false,),true,begin,and,not,or,number,break,(,true,bool,and,by,if,*,elif,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,108))
        except:
            print("fail testcase 8")
        
    def test_case_9(self):
        input = """
]	else == a1 <=	%	60e-1521 and	number (	!=	var	return	[ 22 ,
if string dynamic
end
if	>= +	( <	not <-	
	== begin	a1
a1 until + [ and	=	end 
	number	string break	continue	elif false
var != and string	<- ,
<- <- >=	"abcd" dynamic <
elif	number	<= elif continue and	until dynamic break	or	* ) +
var not	var < >= var
dynamic	% =
118 (	begin
number number	<-	87E729	or
    """
        expect = "\n,],else,==,a1,<=,%,60e-1521,and,number,(,!=,var,return,[,22,,,\n,if,string,dynamic,\n,end,\n,if,>=,+,(,<,not,<-,\n,==,begin,a1,\n,a1,until,+,[,and,=,end,\n,number,string,break,continue,elif,false,\n,var,!=,and,string,<-,,,\n,<-,<-,>=,abcd,dynamic,<,\n,elif,number,<=,elif,continue,and,until,dynamic,break,or,*,),+,\n,var,not,var,<,>=,var,\n,dynamic,%,=,\n,118,(,begin,\n,number,number,<-,87E729,or,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,109))
        except:
            print("fail testcase 9")
        
    def test_case_10(self):
        input = """dynamic abc123
    """
        expect = "dynamic,abc123,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,110))
        except:
            print("fail testcase 10")
        
    def test_case_11(self):
        input = """dynamic 1ae
    """
        expect = "dynamic,1,ae,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,111))
        except:
            print("fail testcase 11")
        
    def test_case_12(self):
        input = """dynamic 1.232eabc
    """
        expect = "dynamic,1.232,eabc,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,112))
        except:
            print("fail testcase 12")
        
    def test_case_13(self):
        input = """dynamic abC1#
    """
        expect = "dynamic,abC1,Error Token #"
        try:
            self.assertTrue(TestLexer.test(input,expect,113))
        except:
            print("fail testcase 13")
        
    def test_case_14(self):
        input = """dynamic _abt
    """
        expect = "dynamic,_abt,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,114))
        except:
            print("fail testcase 14")
        
    def test_case_15(self):
        input = """
## comment
func main()
begin 
              ##hello
## "hello"
var a <- "## comment in string"    
end

    """
        expect = "\n,\n,func,main,(,),\n,begin,\n,\n,\n,var,a,<-,## comment in string,\n,end,\n,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,115))
        except:
            print("fail testcase 15")
        
    def test_case_16(self):
        input = """

func main()
begin ## comment
              ##hello
## "hello"
var a <- "## comment in string"    
end

    """
        expect = "\n,\n,func,main,(,),\n,begin,\n,\n,\n,var,a,<-,## comment in string,\n,end,\n,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,116))
        except:
            print("fail testcase 16")
        
    def test_case_17(self):
        input = """

func main()
begin 
             ## comment ##hello
## "hello"
var a <- "## comment in string"    
end

    """
        expect = "\n,\n,func,main,(,),\n,begin,\n,\n,\n,var,a,<-,## comment in string,\n,end,\n,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,117))
        except:
            print("fail testcase 17")
        
    def test_case_18(self):
        input = """

func main()
begin 
              ##hello
## "hello"
var a <- "## comment in string"    ## comment
end

    """
        expect = "\n,\n,func,main,(,),\n,begin,\n,\n,\n,var,a,<-,## comment in string,\n,end,\n,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,118))
        except:
            print("fail testcase 18")
        
    def test_case_19(self):
        input = """

func main()
begin 
              ##hello
## "hello"
var a <- "## comment in string"    
end
## comment
    """
        expect = "\n,\n,func,main,(,),\n,begin,\n,\n,\n,var,a,<-,## comment in string,\n,end,\n,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,119))
        except:
            print("fail testcase 19")
        
    def test_case_20(self):
        input = """string a<-"PV9i\"s\"
    """
        expect = "string,a,<-,PV9i,s,Unclosed String: "
        try:
            self.assertTrue(TestLexer.test(input,expect,120))
        except:
            print("fail testcase 20")
        
    def test_case_21(self):
        input = """string a<-"G5aS'\"s\n\"a
    """
        expect = "string,a,<-,Unclosed String: G5aS'\"s"
        try:
            self.assertTrue(TestLexer.test(input,expect,121))
        except:
            print("fail testcase 21")
        
    def test_case_22(self):
        input = """string a<-"xLSc'\"s\"
    """
        expect = "string,a,<-,xLSc'\"s,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,122))
        except:
            print("fail testcase 22")
        
    def test_case_23(self):
        input = """string a<-"ThvW'\"s\n\"a
    """
        expect = "string,a,<-,Unclosed String: ThvW'\"s"
        try:
            self.assertTrue(TestLexer.test(input,expect,123))
        except:
            print("fail testcase 23")
        
    def test_case_24(self):
        input = """string a<-"VOJK'\"s a
    """
        expect = "string,a,<-,Unclosed String: VOJK'\"s a"
        try:
            self.assertTrue(TestLexer.test(input,expect,124))
        except:
            print("fail testcase 24")
        
    def test_case_25(self):
        input = """string a<-"LHIi'\"s a
    """
        expect = "string,a,<-,Unclosed String: LHIi'\"s a"
        try:
            self.assertTrue(TestLexer.test(input,expect,125))
        except:
            print("fail testcase 25")
        
    def test_case_26(self):
        input = """string a<-"8Erl'\"s a
    """
        expect = "string,a,<-,Unclosed String: 8Erl'\"s a"
        try:
            self.assertTrue(TestLexer.test(input,expect,126))
        except:
            print("fail testcase 26")
        
    def test_case_27(self):
        input = """string a<-"8vNz'\"s\n\"a
    """
        expect = "string,a,<-,Unclosed String: 8vNz'\"s"
        try:
            self.assertTrue(TestLexer.test(input,expect,127))
        except:
            print("fail testcase 27")
        
    def test_case_28(self):
        input = """string a<-"U0i0'\"s a
    """
        expect = "string,a,<-,Unclosed String: U0i0'\"s a"
        try:
            self.assertTrue(TestLexer.test(input,expect,128))
        except:
            print("fail testcase 28")
        
    def test_case_29(self):
        input = """string a<-"mWVo\"s\"
    """
        expect = "string,a,<-,mWVo,s,Unclosed String: "
        try:
            self.assertTrue(TestLexer.test(input,expect,129))
        except:
            print("fail testcase 29")
        
    def test_case_30(self):
        input = """ not not * for true <- number ^
    """
        expect = "not,not,*,for,true,<-,number,Error Token ^"
        try:
            self.assertTrue(TestLexer.test(input,expect,130))
        except:
            print("fail testcase 30")
        
    def test_case_31(self):
        input = """ begin not dynamic ) continue ] + }
    """
        expect = "begin,not,dynamic,),continue,],+,Error Token }"
        try:
            self.assertTrue(TestLexer.test(input,expect,131))
        except:
            print("fail testcase 31")
        
    def test_case_32(self):
        input = """ / <= ^
    """
        expect = "/,<=,Error Token ^"
        try:
            self.assertTrue(TestLexer.test(input,expect,132))
        except:
            print("fail testcase 32")
        
    def test_case_33(self):
        input = """ true func func false '
    """
        expect = "true,func,func,false,Error Token '"
        try:
            self.assertTrue(TestLexer.test(input,expect,133))
        except:
            print("fail testcase 33")
        
    def test_case_34(self):
        input = """ ... return by end ;
    """
        expect = "...,return,by,end,Error Token ;"
        try:
            self.assertTrue(TestLexer.test(input,expect,134))
        except:
            print("fail testcase 34")
        
    def test_case_35(self):
        input = """ dynamic until false ^
    """
        expect = "dynamic,until,false,Error Token ^"
        try:
            self.assertTrue(TestLexer.test(input,expect,135))
        except:
            print("fail testcase 35")
        
    def test_case_36(self):
        input = """ <= >= '
    """
        expect = "<=,>=,Error Token '"
        try:
            self.assertTrue(TestLexer.test(input,expect,136))
        except:
            print("fail testcase 36")
        
    def test_case_37(self):
        input = """ bool - #
    """
        expect = "bool,-,Error Token #"
        try:
            self.assertTrue(TestLexer.test(input,expect,137))
        except:
            print("fail testcase 37")
        
    def test_case_38(self):
        input = """ IDENTIFIER func end false elif if ) end ~
    """
        expect = "IDENTIFIER,func,end,false,elif,if,),end,Error Token ~"
        try:
            self.assertTrue(TestLexer.test(input,expect,138))
        except:
            print("fail testcase 38")
        
    def test_case_39(self):
        input = """ until = continue != ;
    """
        expect = "until,=,continue,!=,Error Token ;"
        try:
            self.assertTrue(TestLexer.test(input,expect,139))
        except:
            print("fail testcase 39")
        
    def test_case_40(self):
        input = """ / $
    """
        expect = "/,Error Token $"
        try:
            self.assertTrue(TestLexer.test(input,expect,140))
        except:
            print("fail testcase 40")
        
    def test_case_41(self):
        input = """ until ;
    """
        expect = "until,Error Token ;"
        try:
            self.assertTrue(TestLexer.test(input,expect,141))
        except:
            print("fail testcase 41")
        
    def test_case_42(self):
        input = """ >= ] false == #
    """
        expect = ">=,],false,==,Error Token #"
        try:
            self.assertTrue(TestLexer.test(input,expect,142))
        except:
            print("fail testcase 42")
        
    def test_case_43(self):
        input = """ ( string bool [ ( / by >= {
    """
        expect = "(,string,bool,[,(,/,by,>=,Error Token {"
        try:
            self.assertTrue(TestLexer.test(input,expect,143))
        except:
            print("fail testcase 43")
        
    def test_case_44(self):
        input = """ , begin <= #
    """
        expect = ",,begin,<=,Error Token #"
        try:
            self.assertTrue(TestLexer.test(input,expect,144))
        except:
            print("fail testcase 44")
        
    def test_case_45(self):
        input = """ / STRINGLIT IDENTIFIER ] NUMLIT != STRINGLIT number by @
    """
        expect = "/,STRINGLIT,IDENTIFIER,],NUMLIT,!=,STRINGLIT,number,by,Error Token @"
        try:
            self.assertTrue(TestLexer.test(input,expect,145))
        except:
            print("fail testcase 45")
        
    def test_case_46(self):
        input = """ number % ( func dynamic
 continue until @
    """
        expect = "number,%,(,func,dynamic,\n,continue,until,Error Token @"
        try:
            self.assertTrue(TestLexer.test(input,expect,146))
        except:
            print("fail testcase 46")
        
    def test_case_47(self):
        input = """ number , bool if @
    """
        expect = "number,,,bool,if,Error Token @"
        try:
            self.assertTrue(TestLexer.test(input,expect,147))
        except:
            print("fail testcase 47")
        
    def test_case_48(self):
        input = """ <= string , bool &
    """
        expect = "<=,string,,,bool,Error Token &"
        try:
            self.assertTrue(TestLexer.test(input,expect,148))
        except:
            print("fail testcase 48")
        
    def test_case_49(self):
        input = """ == >= continue end and != IDENTIFIER ^
    """
        expect = "==,>=,continue,end,and,!=,IDENTIFIER,Error Token ^"
        try:
            self.assertTrue(TestLexer.test(input,expect,149))
        except:
            print("fail testcase 49")
        
    def test_case_50(self):
        input = """string s <- " Y \\| "
    """
        expect = "string,s,<-,Illegal Escape In String:  Y \\|"
        try:
            self.assertTrue(TestLexer.test(input,expect,150))
        except:
            print("fail testcase 50")
        
    def test_case_51(self):
        input = """string s <- " 0LktgF \\| "
    """
        expect = "string,s,<-,Illegal Escape In String:  0LktgF \\|"
        try:
            self.assertTrue(TestLexer.test(input,expect,151))
        except:
            print("fail testcase 51")
        
    def test_case_52(self):
        input = """string s <- " vAYpu1nS \\\" "
    """
        expect = "string,s,<-,Illegal Escape In String:  vAYpu1nS \\\""
        try:
            self.assertTrue(TestLexer.test(input,expect,152))
        except:
            print("fail testcase 52")
        
    def test_case_53(self):
        input = """string s <- " Oz2D3bUuX \\A "
    """
        expect = "string,s,<-,Illegal Escape In String:  Oz2D3bUuX \\A"
        try:
            self.assertTrue(TestLexer.test(input,expect,153))
        except:
            print("fail testcase 53")
        
    def test_case_54(self):
        input = """string s <- " NkJVQAv \\, "
    """
        expect = "string,s,<-,Illegal Escape In String:  NkJVQAv \\,"
        try:
            self.assertTrue(TestLexer.test(input,expect,154))
        except:
            print("fail testcase 54")
        
    def test_case_55(self):
        input = """string s <- " i \\a "
    """
        expect = "string,s,<-,Illegal Escape In String:  i \\a"
        try:
            self.assertTrue(TestLexer.test(input,expect,155))
        except:
            print("fail testcase 55")
        
    def test_case_56(self):
        input = """string s <- " jsG63gV5z \\~ "
    """
        expect = "string,s,<-,Illegal Escape In String:  jsG63gV5z \\~"
        try:
            self.assertTrue(TestLexer.test(input,expect,156))
        except:
            print("fail testcase 56")
        
    def test_case_57(self):
        input = """string s <- " LZ \\, "
    """
        expect = "string,s,<-,Illegal Escape In String:  LZ \\,"
        try:
            self.assertTrue(TestLexer.test(input,expect,157))
        except:
            print("fail testcase 57")
        
    def test_case_58(self):
        input = """string s <- " asJk4s6g9 \\< "
    """
        expect = "string,s,<-,Illegal Escape In String:  asJk4s6g9 \\<"
        try:
            self.assertTrue(TestLexer.test(input,expect,158))
        except:
            print("fail testcase 58")
        
    def test_case_59(self):
        input = """string s <- " NbmDU6M \\z "
    """
        expect = "string,s,<-,Illegal Escape In String:  NbmDU6M \\z"
        try:
            self.assertTrue(TestLexer.test(input,expect,159))
        except:
            print("fail testcase 59")
        
    def test_case_60(self):
        input = """string s <- "  \\? "
    """
        expect = "string,s,<-,Illegal Escape In String:   \\?"
        try:
            self.assertTrue(TestLexer.test(input,expect,160))
        except:
            print("fail testcase 60")
        
    def test_case_61(self):
        input = """string s <- " 59dp38mQw \\9 "
    """
        expect = "string,s,<-,Illegal Escape In String:  59dp38mQw \\9"
        try:
            self.assertTrue(TestLexer.test(input,expect,161))
        except:
            print("fail testcase 61")
        
    def test_case_62(self):
        input = """string s <- "  \\9 "
    """
        expect = "string,s,<-,Illegal Escape In String:   \\9"
        try:
            self.assertTrue(TestLexer.test(input,expect,162))
        except:
            print("fail testcase 62")
        
    def test_case_63(self):
        input = """string s <- "  \\= "
    """
        expect = "string,s,<-,Illegal Escape In String:   \\="
        try:
            self.assertTrue(TestLexer.test(input,expect,163))
        except:
            print("fail testcase 63")
        
    def test_case_64(self):
        input = """string s <- " vr \\# "
    """
        expect = "string,s,<-,Illegal Escape In String:  vr \\#"
        try:
            self.assertTrue(TestLexer.test(input,expect,164))
        except:
            print("fail testcase 64")
        
    def test_case_65(self):
        input = """string s <- " 1wm \\  "
    """
        expect = "string,s,<-,Illegal Escape In String:  1wm \\ "
        try:
            self.assertTrue(TestLexer.test(input,expect,165))
        except:
            print("fail testcase 65")
        
    def test_case_66(self):
        input = """string s <- " Dbhfojb0V \\- "
    """
        expect = "string,s,<-,Illegal Escape In String:  Dbhfojb0V \\-"
        try:
            self.assertTrue(TestLexer.test(input,expect,166))
        except:
            print("fail testcase 66")
        
    def test_case_67(self):
        input = """string s <- "  \\  "
    """
        expect = "string,s,<-,Illegal Escape In String:   \\ "
        try:
            self.assertTrue(TestLexer.test(input,expect,167))
        except:
            print("fail testcase 67")
        
    def test_case_68(self):
        input = """string s <- " P6Kmsw \\| "
    """
        expect = "string,s,<-,Illegal Escape In String:  P6Kmsw \\|"
        try:
            self.assertTrue(TestLexer.test(input,expect,168))
        except:
            print("fail testcase 68")
        
    def test_case_69(self):
        input = """string s <- "  \\< "
    """
        expect = "string,s,<-,Illegal Escape In String:   \\<"
        try:
            self.assertTrue(TestLexer.test(input,expect,169))
        except:
            print("fail testcase 69")
        
    def test_case_70(self):
        input = """beginnN
    """
        expect = "beginnN,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,170))
        except:
            print("fail testcase 70")
        
    def test_case_71(self):
        input = """stringzY
    """
        expect = "stringzY,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,171))
        except:
            print("fail testcase 71")
        
    def test_case_72(self):
        input = """varoL
    """
        expect = "varoL,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,172))
        except:
            print("fail testcase 72")
        
    def test_case_73(self):
        input = """elselR
    """
        expect = "elselR,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,173))
        except:
            print("fail testcase 73")
        
    def test_case_74(self):
        input = """dynamicJV
    """
        expect = "dynamicJV,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,174))
        except:
            print("fail testcase 74")
        
    def test_case_75(self):
        input = """end7E
    """
        expect = "end7E,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,175))
        except:
            print("fail testcase 75")
        
    def test_case_76(self):
        input = """endyP
    """
        expect = "endyP,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,176))
        except:
            print("fail testcase 76")
        
    def test_case_77(self):
        input = """orSb
    """
        expect = "orSb,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,177))
        except:
            print("fail testcase 77")
        
    def test_case_78(self):
        input = """falseGS
    """
        expect = "falseGS,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,178))
        except:
            print("fail testcase 78")
        
    def test_case_79(self):
        input = """beginuc
    """
        expect = "beginuc,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,179))
        except:
            print("fail testcase 79")
        
    def test_case_80(self):
        input = """boolean vr40y7N <--459
    """
        expect = "boolean,vr40y7N,<-,-,459,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,180))
        except:
            print("fail testcase 80")
        
    def test_case_81(self):
        input = """dynamic vguDwDR <-411
    """
        expect = "dynamic,vguDwDR,<-,411,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,181))
        except:
            print("fail testcase 81")
        
    def test_case_82(self):
        input = """dynamic vqYguUd <--173
    """
        expect = "dynamic,vqYguUd,<-,-,173,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,182))
        except:
            print("fail testcase 82")
        
    def test_case_83(self):
        input = """func fI62Oil(pHkDXTY,pMI7YFn) \n begin \nv285HOZ <--750\n end
    """
        expect = "func,fI62Oil,(,pHkDXTY,,,pMI7YFn,),\n,begin,\n,v285HOZ,<-,-,750,\n,end,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,183))
        except:
            print("fail testcase 83")
        
    def test_case_84(self):
        input = """func fhUGqdl(pUq0i3s,p0lXUKZ,pmggdXX) \n begin \nnumber vqUdLOI <-739\n end
    """
        expect = "func,fhUGqdl,(,pUq0i3s,,,p0lXUKZ,,,pmggdXX,),\n,begin,\n,number,vqUdLOI,<-,739,\n,end,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,184))
        except:
            print("fail testcase 84")
        
    def test_case_85(self):
        input = """func fzGA6Ou(p5VUjBo,pJ4lXDt) \n begin \nvwtoVTs <-825\n end
    """
        expect = "func,fzGA6Ou,(,p5VUjBo,,,pJ4lXDt,),\n,begin,\n,vwtoVTs,<-,825,\n,end,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,185))
        except:
            print("fail testcase 85")
        
    def test_case_86(self):
        input = """vZvM0Gz <--1388
    """
        expect = "vZvM0Gz,<-,-,1388,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,186))
        except:
            print("fail testcase 86")
        
    def test_case_87(self):
        input = """number v5KJNxD <--2445
    """
        expect = "number,v5KJNxD,<-,-,2445,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,187))
        except:
            print("fail testcase 87")
        
    def test_case_88(self):
        input = """number vB67JRA <-1419
    """
        expect = "number,vB67JRA,<-,1419,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,188))
        except:
            print("fail testcase 88")
        
    def test_case_89(self):
        input = """func fJ8owMN(pH40YOY,pZ9cWnT) \n begin \nfunc f7JQJhg(pcnbmp2) \n begin \nvtQVAmL <-1738\n end\n end
    """
        expect = "func,fJ8owMN,(,pH40YOY,,,pZ9cWnT,),\n,begin,\n,func,f7JQJhg,(,pcnbmp2,),\n,begin,\n,vtQVAmL,<-,1738,\n,end,\n,end,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,189))
        except:
            print("fail testcase 89")
        
    def test_case_90(self):
        input = """func fAoBEE5() \n begin \nvo3hITB <-522\n end
    """
        expect = "func,fAoBEE5,(,),\n,begin,\n,vo3hITB,<-,522,\n,end,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,190))
        except:
            print("fail testcase 90")
        
    def test_case_91(self):
        input = """var vrJZXGF <--126
    """
        expect = "var,vrJZXGF,<-,-,126,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,191))
        except:
            print("fail testcase 91")
        
    def test_case_92(self):
        input = """var vufMv55 <--754
    """
        expect = "var,vufMv55,<-,-,754,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,192))
        except:
            print("fail testcase 92")
        
    def test_case_93(self):
        input = """number v9B7mmA <-1181
    """
        expect = "number,v9B7mmA,<-,1181,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,193))
        except:
            print("fail testcase 93")
        
    def test_case_94(self):
        input = """var vB4Sr1k <-1211
    """
        expect = "var,vB4Sr1k,<-,1211,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,194))
        except:
            print("fail testcase 94")
        
    def test_case_95(self):
        input = """dynamic vtPBtki <-1237
    """
        expect = "dynamic,vtPBtki,<-,1237,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,195))
        except:
            print("fail testcase 95")
        
    def test_case_96(self):
        input = """vIbls05 <--697
    """
        expect = "vIbls05,<-,-,697,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,196))
        except:
            print("fail testcase 96")
        
    def test_case_97(self):
        input = """vIVgKEd <--2130
    """
        expect = "vIVgKEd,<-,-,2130,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,197))
        except:
            print("fail testcase 97")
        
    def test_case_98(self):
        input = """number vwCuun1 <--1574
    """
        expect = "number,vwCuun1,<-,-,1574,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,198))
        except:
            print("fail testcase 98")
        
    def test_case_99(self):
        input = """func fXweobc(pIqCeep,pXPKzHr,pDfaKPx) \n begin \nvar vH7Cccr <--2634\n end
    """
        expect = "func,fXweobc,(,pIqCeep,,,pXPKzHr,,,pDfaKPx,),\n,begin,\n,var,vH7Cccr,<-,-,2634,\n,end,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,199))
        except:
            print("fail testcase 99")
        