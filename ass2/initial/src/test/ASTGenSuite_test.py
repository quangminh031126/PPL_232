import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Statements Statements Statements"""
        input = r"""## print function 
func print(string src, string dst) begin
    output <- "Move 1 disk from tower "
    output <- output ... src
    output <- output ... " to tower "
    output <- output ... des
    output <- output ... "\n"
    writeString(output)
end
"""
        expect = r'''Program([FuncDecl(Id(print), [VarDecl(Id(src), StringType, None, None), VarDecl(Id(dst), StringType, None, None)], Block([AssignStmt(Id(output), StringLit(Move 1 disk from tower )), AssignStmt(Id(output), BinaryOp(..., Id(output), Id(src))), AssignStmt(Id(output), BinaryOp(..., Id(output), StringLit( to tower ))), AssignStmt(Id(output), BinaryOp(..., Id(output), Id(des))), AssignStmt(Id(output), BinaryOp(..., Id(output), StringLit(\n))), CallStmt(Id(writeString), [Id(output)])]))])'''
        self.assertTrue(TestAST.test(input, expect, 3079))


