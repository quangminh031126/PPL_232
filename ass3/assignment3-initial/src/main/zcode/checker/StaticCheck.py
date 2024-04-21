from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from typing import Union, List
import warnings


from typing import List, Union, Type

class Symbol:
    def __init__(self, name: str = None, type: Type = None) -> None:
        self.name = name
        self.type = type
    def __str__(self) -> str:
        return f"Name: {self.name}, Type: {self.type}"

class VariableSymbol(Symbol):
    def __init__(self, var_name: str = None, var_type: Type = None) -> None:
        super().__init__(var_name, var_type)
    def __str__(self) -> str:
        return f"Variable Name: {self.name}, Variable Type: {self.type}"

class FunctionSymbol(Symbol):
    def __init__(self, func_name: str = None, func_params: List[VariableSymbol] = [], func_type: Type = None, func_body: Stmt = None) -> None:
        super().__init__(func_name, func_type)
        self.params = func_params
        self.body = func_body
    def __str__(self) -> str:
        params_str = ", ".join([str(param) for param in self.params])
        return f"Function Name: {self.name}, Return Type: {self.type}, Parameters: [{params_str}]"
    def redefine(self, other: 'FunctionSymbol'):
        self.name = other.name if other.name is not None else self.name
        self.type = other.type if other.type is not None else self.type
        self.params = other.params if other.params is not None else self.params
        self.body = other.body if other.body is not None else self.body
class SymbolTable():
    def __init__(self) -> None:
        self.scopes: List[List[Symbol]] = []
        self.new_scope()
        self.add_function_symbol(FunctionSymbol('readNumber',[],NumberType(),None))
        self.add_function_symbol(FunctionSymbol('writeNumber',[VariableSymbol('anArg',NumberType())],VoidType(),None))
        self.add_function_symbol(FunctionSymbol('readBool',[],BoolType(),None))
        self.add_function_symbol(FunctionSymbol('writeBool',[VariableSymbol('anArg',BoolType())],VoidType(),None))
        self.add_function_symbol(FunctionSymbol('readString',[],StringType(),None))
        self.add_function_symbol(FunctionSymbol('writeString',[VariableSymbol('anArg',StringType())],VoidType(),None))

    def new_scope(self) -> None:
        self.scopes.append([])

    def close_scope(self) -> None:
        self.scopes.pop()

    def curr_scope(self):
        return self.scopes[-1]
    
    def exclude_global(self):
        return self.scopes[1:]

    def global_scope(self):
        return self.scopes[0]
    
    def add_variable_symbol(self,variable_symbol: VariableSymbol):
        self.curr_scope().append(variable_symbol)

    def add_function_symbol(self,function_symbol: FunctionSymbol):
        self.global_scope().append(function_symbol)

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
    def lookup_symbol_exclude_global(self,symbol_name:str) -> Symbol:
        for scope in reversed(self.exclude_global()):
            for symbol in scope:
                if symbol_name == symbol.name:
                    return symbol
        return None

class StaticChecker(BaseVisitor, Utils):
    def __init__(self, ast: Program) -> None:
        self.ast = ast
        self.no_body: List[FuncDecl] = []
        self.can_be_inferred: bool = True
        self.visiting_var_name = None
        self.is_calling_function: bool = False
        self.array_stack: List[ArrayLiteral]
        self.func_name = None
        self.return_type: Type = None
        self.return_list: List[Return] = []
        self.in_loop = []

    def check(self):
        symbol_table = SymbolTable()
        self.visit(self.ast, symbol_table)
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



    def visitFuncDecl(self, ast:FuncDecl, param: SymbolTable):
        function_symbol = param.lookup_function_symbol(ast.name.name)
        if function_symbol is not None and function_symbol.body is not None and self.is_calling_function == False:
            raise Redeclared(Function(),ast.name.name)
        param.new_scope() # new scope for param scope
        for param_decl in ast.param:
            if param.lookup_variable_current_scope(param_decl.name.name) is not None:
                Redeclared(Parameter(),param_decl.name.name)
            else:
                param.add_variable_symbol(VariableSymbol(param_decl.name.name,self.visit(param_decl.varType,param)))
        if ast.body is None: # goi ham
            if self.is_calling_function == False:
                self.no_body.append(ast)
            param.add_function_symbol(FunctionSymbol(ast.name.name,func_params=param.curr_scope()))
        else: # khai bao ham
            self.func_name = ast.name.name
            for f in self.no_body:
                if f.name.name == self.func_name:
                    self.no_body.remove(f)
            function_symbol = param.lookup_function_symbol(ast.name.name) # param[-1][idx]
            if function_symbol is not None:
                if len(function_symbol.params) != len(param.curr_scope()):
                    raise Redeclared(Function(),ast.name.name)
                for i in range(len(param.curr_scope())):
                    if (type(function_symbol.params[i].type) is not type(param.curr_scope()[i].type)) or (type(function_symbol.params[i].type) is ArrayType and function_symbol.params[i].type.size != param.curr_scope()[i].type.size):
                        raise Redeclared(Function(), ast.name.name)
                self.visit(ast.body, param)
                function_symbol.redefine(FunctionSymbol(ast.name.name,param.curr_scope(),self.return_type if self.return_type is not None else (VoidType() if self.return_list == [] else None),ast.body))
            else:
                param.add_function_symbol(FunctionSymbol(ast.name.name,param.curr_scope(),self.return_type,ast.body))
                self.visit(ast.body, param)
                return_type = self.return_type if self.return_type is not None else (VoidType() if self.return_list == [] else None)
                if param.global_scope()[-1].type is None:
                    param.global_scope()[-1] = FunctionSymbol(ast.name.name,param.curr_scope(),return_type,ast.body)
        self.return_type = None
        self.has_return = False
        param.close_scope()
        self.return_list = []

        
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


    def visitCallExpr(self, ast:CallExpr, param: SymbolTable):
        if self.visiting_var_name is not None and ast.name.name == self.visiting_var_name:
            raise TypeMismatchInExpression(ast)
        self.can_be_inferred = True
        if param.lookup_symbol_exclude_global(ast.name.name) is not None:
            raise TypeMismatchInExpression(ast)
        
        function_symbol = param.lookup_function_symbol(ast.name.name)

        if function_symbol is None:
            raise Undeclared(Function(),ast.name.name)
        else:
            if type(function_symbol) is VoidType:
                raise TypeMismatchInExpression(ast)
            if len(ast.args) != len(function_symbol.params):
                raise TypeMismatchInExpression(ast)
            for i,arg in enumerate(ast.args):
                arg_type = self.visit(arg,param)
                if arg_type is None:
                    if type(arg) in [Id, CallExpr,ArrayLiteral]:
                        self.inferType(arg, function_symbol.params[i].type,param)
                        if self.can_be_inferred == False:
                            return None
                    else: 
                        return None
                elif arg_type is None: # case cho Array Cell # bug fix before nop bai please
                    self.can_be_inferred = False
                    return None
                else:
                    if type(arg_type) is not type(function_symbol.params[i].type):
                        raise TypeMismatchInExpression(ast)    
                    else:                
                        if type(arg_type) is ArrayType:
                            if function_symbol.params[i].type.size[:len(arg_type.size)] != arg_type.size:
                                raise TypeMismatchInExpression(ast)
                            if arg_type.eleType is None:
                                if type(arg) in [Id, CallExpr, ArrayLiteral]:
                                    self.inferType(arg,function_symbol.params[i].type,param)
                                    if self.can_be_inferred == False:
                                        raise TypeCannotBeInferred(ast)
                                    arg_type = function_symbol.params[i].type
                                else:
                                    raise TypeCannotBeInferred(ast)
                            if type(arg_type.eleType) is not type(function_symbol.params[i].type.eleType) or function_symbol.params[i].size != arg_type.size:
                                raise TypeMismatchInExpression(ast)
            return function_symbol.type



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
        self.can_be_inferred = True
        arr_type = self.visit(ast.arr,param) # la 1 expression tra ve type la ArrayType
        indices = ast.idx # la toa do cua phan tu trong mang
        if arr_type is None:
            self.can_be_inferred = False
            return None
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

    def visitBlock(self, ast: Block, param: SymbolTable):
        param.new_scope()
        for stmt in ast.stmt:
            self.visit(stmt,param)
        self.has_return = False
        param.close_scope()
        self.array_stack = []

    def visitIf(self, ast:If, param: SymbolTable):
        condition_type = self.visit(ast.expr,param)
        if condition_type is None:
            if type(ast.expr) in [Id, CallExpr, ArrayLiteral]:
                self.inferType(ast.expr,BoolType(),param)
                if self.can_be_inferred == False: # removeable
                    raise TypeCannotBeInferred(ast)
                condition_type = BoolType()
            else:
                raise TypeCannotBeInferred(ast)
        if type(condition_type) is not BoolType:
            raise TypeMismatchInStatement(ast)
        then_type = self.visit(ast.thenStmt,param)
        self.has_return = False

        for elif_expr, elif_stmt in ast.elifStmt:
            condition_type = self.visit(elif_expr,param)
            if condition_type is None:
                if type(elif_expr) in [Id, CallExpr, ArrayLiteral]:
                    self.inferType(elif_expr,BoolType(),param)
                    if self.can_be_inferred == False:
                        raise TypeCannotBeInferred(ast)
                    condition_type = BoolType()
                else:
                    raise TypeCannotBeInferred(ast)
            if type(condition_type) is not BoolType:
                raise TypeMismatchInStatement(ast)
            
            self.visit(elif_stmt,param)
            self.has_return = False
        if ast.elseStmt:
            self.visit(ast.elseStmt,param)
        self.array_stack = []

    def visitFor(self, ast:For, param: SymbolTable):
        self.in_loop.append(True)
        scala_type = self.visit(ast.name,param)
        if scala_type is None:
            self.inferType(ast.name,NumberType(),param)
            scala_type = NumberType()
        if scala_type is not NumberType():
            raise TypeMismatchInStatement(ast)
        condition_type = self.visit(ast.condExpr,param)

        if condition_type is not None:
            if type(ast.condExpr) in [Id,CallExpr]:
                self.inferType(ast.condExpr,BoolType(),param)
                if self.can_be_inferred == False:
                    raise TypeCannotBeInferred(ast)
            else:
                raise TypeCannotBeInferred(ast)
        if type(condition_type) is not BoolType:
            raise TypeMismatchInExpression(ast)
        update_type = self.visit(ast.updExpr,param)
        if update_type is None:
            if type(ast.updExpr) in [Id,CallExpr]:
                self.inferType(ast.updExpr,NumberType(),param)
                if self.can_be_inferred == False:
                    raise TypeCannotBeInferred(ast)
            else:
                raise TypeCannotBeInferred(ast)
        if type(update_type) is not NumberType:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.body,param)
        self.array_stack = []
        self.in_loop.pop()

    def visitContinue(self, ast, param: SymbolTable):
        if self.in_loop == []:
            raise MustInLoop(ast)
        self.array_stack = []

    def visitBreak(self, ast: Break, param: SymbolTable):
        if self.in_loop == []:
            raise MustInLoop(ast)
        self.array_stack = []


    def visitReturn(self, ast: Return, param: SymbolTable):
        if self.has_return:
            return
        
        self.has_return = True
        if ast.expr is None:
            self.return_type = VoidType()
        else:
            return_type = self.visit(ast.expr,param)
            function_symbol = param.lookup_function_symbol(self.func_name)
            if function_symbol.type is None:
                if return_type is None:
                    if self.can_be_inferred == False:
                        raise TypeCannotBeInferred(ast)
                    else:
                        self.return_list.append(ast)
                else:
                    self.return_type = return_type
                    function_symbol.redefine(FunctionSymbol(None,None,return_type,None))
                    if self.return_list != []:
                        while self.return_list != []:
                            if type(self.return_list[0].expr) in [Id,CallExpr,ArrayLiteral]:
                                self.inferType(self.return_list[0].expr,return_type,param)
                                if self.can_be_inferred == False:
                                    raise TypeCannotBeInferred(self.return_list[0])
                                else:
                                    self.return_list = self.return_list[1:]
                            else:
                                raise TypeCannotBeInferred(self.return_list[0])
            else:
                if type(function_symbol.type) is VoidType:
                    raise TypeMismatchInExpression(ast)
                if return_type is None:
                    if self.can_be_inferred == False:
                        raise TypeCannotBeInferred(ast)
                    elif type(ast.expr) in [Id,CallExpr,ArrayLiteral]:
                        self.inferType(ast.expr,function_symbol.type,param)
                        if self.can_be_inferred == False:
                            raise TypeCannotBeInferred(ast)
                    else:
                        raise TypeCannotBeInferred(ast)
                else:
                    if type(function_symbol.type) is not type(return_type):
                        raise TypeMismatchInExpression(ast)
                    else:
                        if type(function_symbol.type) is ArrayType:
                            if function_symbol.type.size[:len(return_type.size)] != return_type.size:
                                raise TypeMismatchInExpression
                            if return_type.eleType is None:
                                if type(ast.expr) in [Id, CallExpr, ArrayLiteral]:
                                    self.inferType(ast.expr,function_symbol.type,param)
                                    if self.can_be_inferred == False:
                                        raise TypeCannotBeInferred(ast)
                                    return_type = function_symbol.type
                                else:
                                    raise TypeCannotBeInferred(ast)
                            if type(return_type.eleType) is not type(function_symbol.type.eleType) or function_symbol.type.size != return_type.size:
                                raise TypeMismatchInExpression(ast)
                        self.return_type = function_symbol
        self.array_stack = []

    def visitAssign(self, ast:Assign, param: SymbolTable):
        r_type, l_type = self.visit(ast.rhs,param), self.visit(ast.lhs,param)
        if r_type is None and l_type is None:
            raise TypeCannotBeInferred(ast)
        if r_type is not None and l_type is None: # biet Phai chua biet Trai
            if type(ast.lhs) is Id:
                self.inferType(ast.lhs,r_type,param)
            else:
                raise TypeCannotBeInferred(ast)
        elif r_type is None and l_type is not None:
            if type(ast.exp) in [Id,CallExpr,ArrayLiteral]:
                self.inferType(ast.rhs,l_type,param)
                if self.can_be_inferred == False:
                    raise TypeCannotBeInferred(ast)
            else:
                raise TypeCannotBeInferred(ast)
        else:
            if type(l_type) is VoidType:
                raise TypeMismatchInStatement(ast)
            elif type(l_type) is not type(r_type):
                raise TypeMismatchInStatement(ast)
            else:
                if type(l_type) is ArrayType:
                    if l_type.size[:len(r_type.size)] != r_type.size:
                        raise TypeMismatchInStatement(ast)
                    else:
                        if r_type.eleType is None:
                            if type(ast.rhs) in [Id, CallExpr,ArrayLiteral]:
                                self.inferType(ast.rhs,l_type,param)
                            if self.can_be_inferred == False:
                                raise TypeCannotBeInferred(ast)
                            r_type = l_type
                        else:
                            raise TypeCannotBeInferred(ast)
                    if type(l_type.eleType) is not type(r_type.eleType) or l_type.size != r_type.size:
                        raise TypeMismatchInStatement
        self.array_stack = []

    def visitCallStmt(self, ast, param: SymbolTable):
        self.can_be_inferred = True
        if param.lookup_symbol_exclude_global(ast.name.name) is not None:
            raise TypeMismatchInStatement(ast)
        
        function_symbol = param.lookup_function_symbol(ast.name.name)

        if function_symbol is None:
            raise Undeclared(Function(),ast.name.name)
        else:
            if type(function_symbol) is VoidType:
                raise TypeMismatchInStatement(ast)
            if len(ast.args) != len(function_symbol.params):
                raise TypeMismatchInStatement(ast)
            for i,arg in enumerate(ast.args):
                arg_type = self.visit(arg,param)
                if arg_type is None:
                    if type(arg) in [Id, CallExpr,ArrayLiteral]:
                        self.inferType(arg, function_symbol.params[i].type,param)
                        if self.can_be_inferred == False:
                            return None
                    else: 
                        return None
                elif arg_type is None: # case cho Array Cell # bug fix before nop bai please
                    self.can_be_inferred = False
                    return None
                else:
                    if type(arg_type) is not type(function_symbol.params[i].type):
                        raise TypeMismatchInStatement(ast)    
                    else:                
                        if type(arg_type) is ArrayType:
                            if function_symbol.params[i].type.size[:len(arg_type.size)] != arg_type.size:
                                raise TypeMismatchInStatement(ast)
                            if arg_type.eleType is None:
                                if type(arg) in [Id, CallExpr, ArrayLiteral]:
                                    self.inferType(arg,function_symbol.params[i].type,param)
                                    if self.can_be_inferred == False:
                                        raise TypeCannotBeInferred(ast)
                                    arg_type = function_symbol.params[i].type
                                else:
                                    raise TypeCannotBeInferred(ast)
                            if type(arg_type.eleType) is not type(function_symbol.params[i].type.eleType) or function_symbol.params[i].size != arg_type.size:
                                raise TypeMismatchInStatement(ast)
            if function_symbol.type is None:
                self.inferType(ast,VoidType(),param)
        self.array_stack = []


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
                                if type(element) in [Id,CallExpr,ArrayLiteral]:
                                    self.inferType(element,first_element_type_found,param)
                                    if self.can_be_inferred == False:
                                        return None
                                    element_type = first_element_type_found
                                else:
                                    return None
                            if type(element_type.eleType) is not type(first_element_type_found.eleType) or element_type.size != first_element_type_found.size:
                                raise TypeMismatchInExpression(self.array_stack[0])
            if type(first_element_type_found) is not ArrayType:
                self.array_stack = self.array_stack[:-1]
                return ArrayType([len(ast.value)],first_element_type_found)
            else:
                self.array_stack = self.array_stack[:-1]
                return ArrayType([len(ast.value)] + first_element_type_found.size, first_element_type_found.eleType)