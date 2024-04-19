from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce
from typing import Union, List, Dict
import warnings


from typing import List, Dict, Union, Type

class Symbol:
    def __init__(self, name: str = None, type: Type = None) -> None:
        self.name = name
        self.type = type

class VariableSymbol(Symbol):
    def __init__(self, var_name: str = None, var_type: Type = None) -> None:
        super().__init__(var_name, var_type)

class FunctionSymbol(Symbol):
    def __init__(self, func_name: str = None, func_params: List[VariableSymbol] = [], func_type: Type = None, func_body: Stmt = None) -> None:
        super().__init__(func_name, func_type)
        self.params = func_params
        self.body = func_body
class SymbolTable():
    def __init__(self) -> None:
        self.scopes: List[List[Symbol]] = []

    def open_scope(self) -> None:
        self.scopes.append([])

    def close_scope(self) -> None:
        self.scopes.pop()

    def curr_scope(self):
        return self.scopes[-1]

    def global_scope(self):
        return self.scopes[0]

    def define_symbol(self, symbol: Symbol) -> None:
        self.scopes[-1].append(symbol)
    
    def update_variable_type(self, variable_name:str, variable_type: Type) -> bool:
        for scope in reversed(self.scopes):
            for symbol in scope:
                if variable_name == symbol.name:
                    symbol.type = variable_type
                    return True
        return False
    
    def update_function_sym(self, function_name:str, function_type: Type) -> bool:
        for symbol in self.global_scope():
            if function_name == symbol.name and type(symbol) is FunctionSymbol:
                symbol.type = function_type
                return True
        return False
    
    def lookup_variable_current_scope(self,variable_name: str) -> Union[VariableSymbol,None]:
        for symbol in self.curr_scope():
            if variable_name == symbol.name:
                return symbol
        return None

    def add_variable_symbol(self,variable_symbol: VariableSymbol):
        self.curr_scope.append(variable_symbol)
    
    def lookup_variable_symbol(self,variable_name:str) -> Union[VariableSymbol,None]:
        for scope in reversed(self.scopes):
            for symbol in scope:
                if variable_name == symbol.name and type(symbol) is VariableSymbol:
                    return symbol
        return None
    
    def lookup_function_symbol(self,function_name:str) -> Union[FunctionSymbol,None]:
        for symbol in self.global_scope():
            if function_name == symbol.name and type(symbol) is FunctionSymbol:
                return symbol
        return None

class StaticChecker(BaseVisitor, Utils):
    def __init__(self, ast: Program) -> None:
        self.ast = ast
        self.no_body = []
        self.can_be_inferred = True
        self.visiting_var_name = None
        self.is_calling_function = False
        self.array_stack: List[ArrayLiteral]

    def is_same_type(self,l_type: Type,r_type: Type) -> bool:
        if type(l_type) is type(r_type):
            return True
        return False

    def inferType(self, expr: Union[Id, CallExpr, CallStmt, ArrayLiteral], to_type: Type, param: SymbolTable):
        # Assumption that 
        if type(expr) is Id:
            var_symbol = param.lookup_variable_symbol(expr.name)
            if var_symbol is None: warnings.warn("Chưa check sự tồn tại của biến!!",expr)
            else:
                param.update_variable_type(var_symbol.name,to_type)

        elif type(expr) in [CallExpr,CallStmt]:
            func_symbol = param.lookup_function_symbol(expr.name)
            if func_symbol is None: warnings.warn("Chưa check sự tồn tại của hàm!!",expr)
            else:
                param.update_function_sym(func_symbol.name,to_type)
                self.is_calling_function = True
                self.visit(FuncDecl(Id(func_symbol.name),list(map(lambda x: VarDecl(Id(x.name),x.typ,None,None),func_symbol.params)),func_symbol.body),param)
                self.is_calling_function = False

        elif type(expr) is ArrayLiteral:
            if type(to_type) is not ArrayType:
                self.can_be_inferred = False
            else:
                for val in expr.value:
                    val_type = (
                        to_type.eleType 
                        if len(to_type.size) == 1 
                        else  ArrayType(to_type.size[1:], to_type.eleType)
                        )
                    self.inferType(val,val_type,param)
        else:
            self.can_be_inferred = False


    def visitProgram(self, ast: Program, param: SymbolTable):
        for decl in ast.decl:
            self.visit(decl,param)
        if self.no_body != []:
            raise NoDefinition(self.no_body[0].name.name)
        main_func_symbol = param.lookup_function_symbol("main")
        if main_func_symbol is None or type(main_func_symbol.type) is not VoidType or type(main_func_symbol.params) != []:
            raise NoEntryPoint()
        
    def visitVarDecl(self, ast: VarDecl, param: SymbolTable):        
        if param.lookup_variable_current_scope(ast.name.name) is not None:
            raise Redeclared(Variable(),ast.name.name)
        
        self.visiting_var_name = ast.name.name
        l_type = ast.varType
        if ast.varInit is not None:
            r_type = self.visit(ast.varInit,param)
            if l_type is not None and r_type is not None:
                if not self.is_same_type(l_type,r_type):
                    raise TypeMismatchInExpression(ast)
                if type(l_type) is ArrayType:
                    if l_type.size[:len(r_type.size)] != r_type.size:
                        self.inferType(ast.varInit,l_type,param)
                        if not self.can_be_inferred:
                            raise TypeCannotBeInferred(ast)
                        param.add_variable_symbol(VariableSymbol(ast.name.name,l_type))
                    else:
                        if type(r_type.eleType) is not type(l_type.eleType):
                            raise TypeMismatchInExpression(ast)
                param.add_variable_symbol(VariableSymbol(ast.name.name,l_type))
            elif l_type is None and r_type is None:
                raise TypeCannotBeInferred(ast)
            elif r_type is None and l_type is not None:
                if type(ast.varInit) in [Id, CallExpr, ArrayLiteral]:
                    self.inferType(ast.varInit,l_type,param)
                    if not self.can_be_inferred:
                        raise TypeCannotBeInferred(ast)
                    param.add_variable_symbol(VariableSymbol(ast.name.name,l_type))
                else:
                    raise TypeCannotBeInferred(ast)
            else:
                param.add_variable_symbol(VariableSymbol(ast.name.name,r_type))
        else:
            param.add_variable_symbol(VariableSymbol(ast.name.name,l_type))
        
        self.array_stack = []
        self.visiting_var_name = None



    def visitFuncDecl(self, ast, param: SymbolTable):
        pass

    def visitNumberType(self, ast, param: SymbolTable):
        return NumberType()

    def visitBoolType(self, ast, param: SymbolTable):
        return BoolType()

    def visitStringType(self, ast, param: SymbolTable):
        return StringType()

    def visitArrayType(self, ast, param: SymbolTable):
        return ArrayType()

    def visitBinaryOp(self, ast: BinaryOp, param: SymbolTable):
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

    def visitUnaryOp(self, ast: UnaryOp, param: SymbolTable):
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


    def visitCallExpr(self, ast, param: SymbolTable):
        pass

    def visitId(self, ast: Id, param: SymbolTable):
        if self.visiting_var_name is not None and ast.name == self.visiting_var_name:
            raise Undeclared(Identifier(),ast.name)
        
        self.can_be_inferred = True

        sym = param.lookup_variable_symbol(ast.name)
        if sym is None:
            raise Undeclared(Identifier(), ast.name)
        else:
            return sym.type

    def visitArrayCell(self, ast:ArrayCell, param: SymbolTable):
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

    def visitBlock(self, ast, param: SymbolTable):
        pass

    def visitIf(self, ast, param: SymbolTable):
        pass

    def visitFor(self, ast, param: SymbolTable):
        pass

    def visitContinue(self, ast, param: SymbolTable):
        pass

    def visitBreak(self, ast, param: SymbolTable):
        pass

    def visitReturn(self, ast, param: SymbolTable):
        pass

    def visitAssign(self, ast, param: SymbolTable):
        pass

    def visitCallStmt(self, ast, param: SymbolTable):
        pass

    def visitNumberLiteral(self, ast: NumberLiteral, param: SymbolTable):
        return NumberType()

    def visitBooleanLiteral(self, ast: BooleanLiteral, param: SymbolTable):
        return BoolType()

    def visitStringLiteral(self, ast: StringLiteral, param: SymbolTable):
        return StringType()

    def visitArrayLiteral(self, ast: ArrayLiteral, param: SymbolTable):
        if ast not in self.array_stack:
            self.array_stack.append(ast)
        
        first_element_type_found = next((self.visit(val, param) for val in ast.value if self.visit(val, param) is not None), None)
        if first_element_type_found is not None:
            for element in ast.value:
                element_type = self.visit(element,param)
                if element_type is None:
                    if type(element) in [Id, CallExpr, ArrayLiteral]:
                        self.inferType(element,first_element_type_found,param)
                        if self.can_be_inferred == False:
                            return None
                        element_type = first_element_type_found
                    else: return None
                if type(element_type) is not type(first_element_type_found):
                    TypeMismatchInExpression(self.array_stack[0])
                else:
                    if type(element_type) is ArrayType:
                        if element_type.size[:len(first_element_type_found.size)] != first_element_type_found.size:
                            raise TypeMismatchInExpression(self.array_stack[0])
                        else:
                            if type(element_type) is None:
                                if type(ast.value) in [Id,CallExpr,ArrayLiteral]:
                                    self.inferType(ast.value)