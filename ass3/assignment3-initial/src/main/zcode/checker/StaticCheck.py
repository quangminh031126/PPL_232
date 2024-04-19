from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce
from typing import Union, List, TypedDict


class VariableSymbol():
    def __init__(self, var_name: str = None, var_type: Type = None) -> None:
        self.name = var_name
        self.type = var_type
class FunctionSymbol():
    def __init__(self, func_name: str = None, func_params: List[VariableSymbol]= [],func_type: Type = None, func_body: Stmt = None) -> None:
        self.name = func_name
        self.params = func_params
        self.type = func_type
        self.body = func_body
class SymbolTable():
    def __init__(self) -> None:
        self.scopes = [{}]

    def open_scope(self) -> None:
        self.scopes.append({})

    def close_scope(self) -> None:
        self.scopes.pop()

    def define_symbol(self, symbol_name: str, symbol: Union[VariableSymbol, FunctionSymbol]) -> None:
        self.scopes[-1][symbol_name] = symbol

    def lookup_symbol(self, symbol_name: str) -> Union[VariableSymbol, FunctionSymbol, None]:
        for scope in reversed(self.scopes):
            if symbol_name in scope:
                return scope[symbol_name]
        return None

class StaticChecker(BaseVisitor, Utils):
    def __init__(self, ast: Program) -> None:
        self.ast = ast
        self.envs = [[]]
        self.no_body = []
        self.function_calling = False
        self.can_be_inferred = True
        self.visiting_var = None


    def inferType(self, expr: Id | CallExpr | CallStmt | ArrayLiteral, to_type: Type, param):
        if type(expr) is Id:
            pass
        elif type(expr) in [CallExpr,CallStmt]:
            pass
        elif type(expr) is ArrayLiteral:
            pass
        else:
            self.can_be_inferred = False


    def visitProgram(self, ast: Program, param):
        for decl in ast.decl:
            self.visit(decl,param)
        if self.no_body != []:
            raise NoDefinition(self.no_body[0].name.name)
        for func in param[-1]:
            if type(func) is FunctionSymbol and func.name == "main" and type(func.type) is VoidType and func.params == []:
                break
            else: 
                raise NoEntryPoint()

    def visitVarDecl(self, ast: VarDecl, param):
        if self.lookup(ast.name.name,param[0],lambda x: x.name) is not None:
            raise Redeclared(Variable(),ast.name.name)
        
        self.visiting_var = ast.name.name
        l_type = ast.varType
        r_type = ast.varInit
        mod = ast.modifier


    def visitFuncDecl(self, ast, param):
        pass

    def visitNumberType(self, ast, param):
        return NumberType()

    def visitBoolType(self, ast, param):
        return BoolType()

    def visitStringType(self, ast, param):
        return StringType()

    def visitArrayType(self, ast, param):
        return ArrayType()

    def visitBinaryOp(self, ast: BinaryOp, param):
        left_type, right_type = self.visit(ast.left), self.visit(ast.right)
        op = ast.op
        if op in ['+','-','*','/','%','=','!=','>','<','>=','<=']:
            if left_type is None:
                if type(ast.left) in [Id, CallExpr]:
                    self.inferType(ast.left,NumberType(),param)
                    left_type = NumberType()
                    if self.can_be_inferred == False:
                        return None
                else:
                    return None
            if right_type is None:
                if type(ast.right) in [Id, CallExpr]:
                    self.inferType(ast.right,NumberType(),param)
                    right_type = NumberType()
                    if self.can_be_inferred == False:
                        return None
            if type(left_type) is not NumberType or type(right_type) is not NumberType:
                raise TypeMismatchInExpression(ast)
            return NumberType() if op in ['+','-','*','/','%'] else BoolType()
        elif op in ['and','or']:
            if left_type is None:
                if type(ast.left) in [Id, CallExpr]:
                    self.inferType(ast.left,BoolType(),param)
                    left_type = BoolType()
                    if self.can_be_inferred == False:
                        return None
                else:
                    return None
            if right_type is None:
                if type(ast.right) in [Id, CallExpr]:
                    self.inferType(ast.right,BoolType(),param)
                    right_type = BoolType()
                    if self.can_be_inferred == False:
                        return None
            if type(left_type) is not BoolType or type(right_type) is not BoolType:
                raise TypeMismatchInExpression(ast)
            return BoolType()
        else: # elif op in ['...','==']
            if left_type is None:
                if type(ast.left) in [Id, CallExpr]:
                    self.inferType(ast.left,StringType(),param)
                    left_type = StringType()
                    if self.can_be_inferred == False:
                        return None
                else:
                    return None
            if right_type is None:
                if type(ast.right) in [Id, CallExpr]:
                    self.inferType(ast.right,StringType(),param)
                    right_type = StringType()
                    if self.can_be_inferred == False:
                        return None
            if type(left_type) is not StringType or type(right_type) is not StringType:
                raise TypeMismatchInExpression(ast)
            return BoolType() if op == '==' else StringType()

    def visitUnaryOp(self, ast: UnaryOp, param):
        operand_type = self.visit(ast.operand,param)
        op = ast.op
        if op == '!':
            if operand_type is None:
                if type(ast.operand) in [Id,CallExpr]:
                    self.inferType(ast.operand, BoolType(),param)
                if self.can_be_inferred == False:
                    return None
                
                else:
                    return BoolType()
            else:
                if type(ast.operand) is not BoolType():
                    raise TypeMismatchInExpression(ast)
                else:
                    return BoolType()
        if op == '-':
            if operand_type is None:
                if type(ast.operand) in [Id,CallExpr]:
                    self.inferType(ast.operand, NumberType(),param)
                if self.can_be_inferred == False:
                    return None
                
                else:
                    return NumberType()
            else:
                if type(ast.operand) is not NumberType():
                    raise TypeMismatchInExpression(ast)
                else:
                    return NumberType()


    def visitCallExpr(self, ast, param):
        pass

    def visitId(self, ast: Id, param):
        if self.visiting_var is not None and ast.name == self.visiting_var:
            raise Undeclared(Identifier(),ast.name)
        
        self.can_be_inferred = True

        for env in param:
            sym = Utils.lookup(ast.name,env,lambda x: x.name)
            if sym is not None and type(sym) is VariableSymbol:
                return sym.typ
        raise Undeclared(Identifier(), ast.name)

    def visitArrayCell(self, ast:ArrayCell, param):
        arr_type = self.visit(ast.arr,param) # la 1 expression tra ve type la ArrayType
        indices = ast.idx # la toa do cua phan tu trong mang
        if arr_type is None:
            pass
        else:
            if type(arr_type) is not ArrayType:
                raise TypeMismatchInExpression(ast)
            else:
                if len(arr_type.size) < len(indices):
                    raise TypeMismatchInExpression(ast)
                else:
                    for i in range(len(ast.idx)):
                        idx_type = self.visit(ast.idx[i],param)
                        if idx_type is None: # bien chua duoc suy dien kieu
                            if type(idx_type) in [Id,CallExpr]: 
                                self.inferType(ast.idx[i], NumberType(),param)
                                if self.can_be_inferred == False:
                                    return None
                                else:
                                    idx_type = NumberType()
                            else:
                                return None
                        if type(idx_type) is not NumberType:
                            raise TypeMismatchInExpression(ast)
                    return arr_type.eleType if len(arr_type) == len(indices) else ArrayType(arr_type.size[len(ast.idx):], arr_type.eleType)

    def visitBlock(self, ast, param):
        pass

    def visitIf(self, ast, param):
        pass

    def visitFor(self, ast, param):
        pass

    def visitContinue(self, ast, param):
        pass

    def visitBreak(self, ast, param):
        pass

    def visitReturn(self, ast, param):
        pass

    def visitAssign(self, ast, param):
        pass

    def visitCallStmt(self, ast, param):
        pass

    def visitNumberLiteral(self, ast: NumberLiteral, param):
        return NumberType()

    def visitBooleanLiteral(self, ast: BooleanLiteral, param):
        return BoolType()

    def visitStringLiteral(self, ast: StringLiteral, param):
        return StringType()

    def visitArrayLiteral(self, ast: ArrayType, param):
        return ArrayType(ast.size,ast.eleType)
