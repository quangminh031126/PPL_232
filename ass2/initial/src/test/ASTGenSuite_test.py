import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """
            var x <- [1, "a", true, false]
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  ArrayLiteral([NumberLiteral(1.0), StringLiteral("a"), BooleanLiteral(True), BooleanLiteral(False)]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 313))   
        
        input = """
            var x <- [[1], [1]]
            var x <- [[1]]
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  ArrayLiteral([ArrayLiteral([NumberLiteral(1.0)]), ArrayLiteral([NumberLiteral(1.0)])])),
                    VarDecl(Id("x"), None, "var",  ArrayLiteral([ArrayLiteral([NumberLiteral(1.0)])]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 314))  
        
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
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 315))  
        
        input = """
            var x <- 2 or 3 and 1 <= 2 ... 4 <= 5 + a * 3 + c - -1 + not - 2
        """
        expect = str(Program([
                VarDecl(Id("x"), None, "var",  BinaryOp("...", BinaryOp("<=", BinaryOp("and", BinaryOp("or", NumberLiteral(2.0), NumberLiteral(3.0)), NumberLiteral(1.0)), NumberLiteral(2.0)), BinaryOp("<=", NumberLiteral(4.0), BinaryOp("+", BinaryOp("-", BinaryOp("+", BinaryOp("+", NumberLiteral(5.0), BinaryOp("*", Id("a"), NumberLiteral(3.0))), Id("c")), UnaryOp("-", NumberLiteral(1.0))), UnaryOp("not", UnaryOp("-", NumberLiteral(2.0)))))))
            ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 316))  
        
        input = """
            var x <- -a[1+2] ... 2
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  BinaryOp("...", UnaryOp("-", ArrayCell(Id("a"), [BinaryOp("+", NumberLiteral(1.0), NumberLiteral(2.0))])), NumberLiteral(2.0)))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 317))  
        
        input = """
            var x <- fun()
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  CallExpr(Id("fun"), []))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 318)) 
        
        input = """
            var x <- fun(1+1, "a")
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  CallExpr(Id("fun"), [BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0)), StringLiteral("a")]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 319)) 
        
        input = """
            var x <- fun(fun())
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  CallExpr(Id("fun"), [CallExpr(Id("fun"), [])]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 320))