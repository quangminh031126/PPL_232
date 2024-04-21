import unittest
from TestUtils import TestChecker
from AST import *


class CheckSuite(unittest.TestCase):
    def test_6_TypeMismatchInStatement(self):
        input = """
            number a <- "1"

            func main() return
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), NumberType, None, StringLit(1))"
        #self.assertTrue(TestChecker.test(input, expect, 444))
        
        input = """
            number a[1,2] <- [[1,2]]

            func main() return
        """
        expect = ""
        #self.assertTrue(TestChecker.test(input, expect, 445))
        
        input = """
            number a[1,2,3] <- [[1,2]]

            func main() return
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([1.0, 2.0, 3.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0))))"
        self.assertTrue(TestChecker.test(input, expect, 446))

        input = """
            number a[1] <- [[1,2]]

            func main() return
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([1.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0))))"
        #self.assertTrue(TestChecker.test(input, expect, 447))       

        input = """
            func foo() return

            func main()begin
                foo()
                foo(1)
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [NumLit(1.0)])"
        #self.assertTrue(TestChecker.test(input, expect, 448))    
        
        input = """
            func foo(number a) return

            func main()begin
                foo()
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [])"
        #self.assertTrue(TestChecker.test(input, expect, 449))     
        
        input = """
            func foo(number a) return

            func main()begin
                foo("1")
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [StringLit(1)])"
        #self.assertTrue(TestChecker.test(input, expect, 450))    
        
        input = """
            func foo(number a) return

            func main()begin
                dynamic a
                foo(a)
                number c <- a
            end
        """
        expect = ""
        #self.assertTrue(TestChecker.test(input, expect, 451))                

        input = """
            func main()begin
                dynamic a
                if (a) return
                a <- true
            end
        """
        expect = ""
        #self.assertTrue(TestChecker.test(input, expect, 452))     
        
        input = """
            func main()begin
                dynamic a <- 1
                if (a) return
            end
        """
        expect = "Type Mismatch In Statement: If((Id(a), Return()), [], None)"
        #self.assertTrue(TestChecker.test(input, expect, 453))                 

        input = """
            func main()begin
                dynamic a
                if (a) number a
                elif (a)  return
                else number a
                
                if(true) number a
                elif (1) number a
            end
        """
        expect = "Type Mismatch In Statement: If((BooleanLit(True), VarDecl(Id(a), NumberType, None, None)), [(NumLit(1.0), VarDecl(Id(a), NumberType, None, None))], None)"
        #self.assertTrue(TestChecker.test(input, expect, 454)) 
        
        input = """
            func foo() begin
                dynamic a
                dynamic b
                dynamic c
                for a until b by c return
                a <- 1
                b <- true
                c <- 1
            end
            func main() return
        """
        expect = ""
        #self.assertTrue(TestChecker.test(input, expect, 455))   
        
        input = """
            func foo() begin
                dynamic a <- true
                dynamic b
                dynamic c
                for a until b by c return
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: For(Id(a), Id(b), Id(c), Return())"
        #self.assertTrue(TestChecker.test(input, expect, 456))    
        
        input = """
            func foo() begin
                dynamic a 
                dynamic b <- 2
                dynamic c
                for a until b by c return
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: For(Id(a), Id(b), Id(c), Return())"
        #self.assertTrue(TestChecker.test(input, expect, 457))  

        input = """
            func foo() begin
                dynamic a 
                dynamic b
                dynamic c <- "1"
                for a until b by c return
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: For(Id(a), Id(b), Id(c), Return())"
        #self.assertTrue(TestChecker.test(input, expect, 458))    
        
        input = """
            func foo() begin
                number a
                return 1
                return a
                return "!"
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: Return(StringLit(!))"
        #self.assertTrue(TestChecker.test(input, expect, 459))  
        
        
        input = """
            func foo() begin
                number a
                a <- 1
                a <- true
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), BooleanLit(True))"
        #self.assertTrue(TestChecker.test(input, expect, 460))  
