from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *


class ASTGeneration(ZCodeVisitor):

# Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return Program(self.visit(ctx.stms()))


    # Visit a parse tree produced by ZCodeParser#stms.
    def visitStms(self, ctx:ZCodeParser.StmsContext):
        if ctx.getChildCount() == 0: return []
        return self.visit(ctx.stm_lists())


    # Visit a parse tree produced by ZCodeParser#stm_lists.
    def visitStm_lists(self, ctx:ZCodeParser.Stm_listsContext):
        if ctx.stm() is None and ctx.stm_lists() is None:
            return []
        elif ctx.getChildCount() == 1: 
            stm = self.visit(ctx.stm())
            return [stm] if stm is not None else []
        else:
            stm = self.visit(ctx.stm())
            stm_lists = self.visit(ctx.stm_lists())
            return ([stm] if stm is not None else []) + (stm_lists if stm_lists is not None else [])
  
# program: stms EOF;

# stms: (listOfNEWLINE | ) stm_lists (listOfNEWLINE | ) | /* empty */;

# stm_lists: stm | stm listOfNEWLINE stm_lists;
    # Visit a parse tree produced by ZCodeParser#stm.
    def visitStm(self, ctx:ZCodeParser.StmContext):
        if ctx.expr6():
            return CallStmt(self.visit(ctx.expr6()),self.visit(ctx.expr_list()))
        elif ctx.expr():
            return self.visit(ctx.expr())
        elif ctx.decl():
            return self.visit(ctx.decl())
        elif ctx.ass():
            return self.visit(ctx.ass())
        elif ctx.block():
            return self.visit(ctx.block())
        elif ctx.func():
            return self.visit(ctx.func())
        elif ctx.r_break():
            return self.visit(ctx.r_break())
        elif ctx.r_continue():
            return self.visit(ctx.r_continue())
        elif ctx.r_return():
            return self.visit(ctx.r_return())
        elif ctx.r_if():
            return self.visit(ctx.r_if())
        elif ctx.r_for():
            return self.visit(ctx.r_for())
        else:
            return self.visitChildren(ctx)
# stm: (expr6 LP expr_list RP) | expr | decl | ass | block | func | r_break | r_continue | r_return | r_if | r_for;


    # Visit a parse tree produced by ZCodeParser#r_break.
    def visitR_break(self, ctx:ZCodeParser.R_breakContext):
        return Break()

    # Visit a parse tree produced by ZCodeParser#r_continue.
    def visitR_continue(self, ctx:ZCodeParser.R_continueContext):
        return Continue()


    # Visit a parse tree produced by ZCodeParser#r_return.
    def visitR_return(self, ctx:ZCodeParser.R_returnContext):
        expr = self.visit(ctx.expr()) if ctx.expr() else None
        return Return(expr)

    # Visit a parse tree produced by ZCodeParser#r_if.
    def visitR_if(self, ctx:ZCodeParser.R_ifContext):
        expr = self.visit(ctx.expr())
        then_stmt = self.visit(ctx.stm())
        elifs = []
        elseStmt = None

        if ctx.r_elifs():
            elifs = self.visit(ctx.r_elifs())
        if ctx.r_else():
            elseStmt = self.visit(ctx.r_else())
        return If(expr,then_stmt,elifs,elseStmt)

# r_if: IF LP expr RP (listOfNEWLINE | ) stm
# 	| IF LP expr RP (listOfNEWLINE | ) stm r_elifs
# 	| IF LP expr RP (listOfNEWLINE | ) stm r_else
# 	| IF LP expr RP (listOfNEWLINE | ) stm r_elifs r_else;

    # Visit a parse tree produced by ZCodeParser#r_elifs.
    def visitR_elifs(self, ctx:ZCodeParser.R_elifsContext):
        if ctx.getChildCount() == 1: return [self.visit(ctx.r_elif())]
        return [self.visit(ctx.r_elif())] + self.visit(ctx.r_elifs())


    # Visit a parse tree produced by ZCodeParser#r_elif.
    def visitR_elif(self, ctx:ZCodeParser.R_elifContext):
        expr = self.visit(ctx.expr())
        stm = self.visit(ctx.stm())
        return expr,stm
# r_elifs: r_elif | r_elif r_elifs;

# r_elif: (listOfNEWLINE | ) ELIF LP expr RP (listOfNEWLINE | ) stm;
    # Visit a parse tree produced by ZCodeParser#r_else.
    def visitR_else(self, ctx:ZCodeParser.R_elseContext):
        return self.visit(ctx.stm())
# r_else: (listOfNEWLINE | ) ELSE (listOfNEWLINE | ) stm;


    # Visit a parse tree produced by ZCodeParser#r_for.
    def visitR_for(self, ctx:ZCodeParser.R_forContext):
        return For(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.expr(0)),self.visit(ctx.expr(1)),self.visit(ctx.stm()))
# r_for: FOR IDENTIFIER UNTIL expr BY expr (listOfNEWLINE | ) stm;


    # Visit a parse tree produced by ZCodeParser#block.
    def visitBlock(self, ctx:ZCodeParser.BlockContext):
        if ctx.block_stms(): return Block(self.visit(ctx.block_stms()))
        return Block([])


    # Visit a parse tree produced by ZCodeParser#block_stms.
    def visitBlock_stms(self, ctx:ZCodeParser.Block_stmsContext):
        if ctx.getChildCount() == 1: return [self.visit(ctx.stm())]
        return [self.visit(ctx.stm())] + self.visit(ctx.block_stms())
# block_stms: stm | stm listOfNEWLINE block_stms;


    # Visit a parse tree produced by ZCodeParser#func.
    def visitFunc(self, ctx:ZCodeParser.FuncContext):
        body = None
        if ctx.r_return():
            body = self.visit(ctx.r_return())
        elif ctx.block():
            body = self.visit(ctx.block())
        return FuncDecl(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.arg_group()),body)
# func: FUNC IDENTIFIER arg_group ( ( (listOfNEWLINE | ) (r_return | block) ) | );


    # Visit a parse tree produced by ZCodeParser#arg_group.
    def visitArg_group(self, ctx:ZCodeParser.Arg_groupContext):
        return self.visit(ctx.args())


    # Visit a parse tree produced by ZCodeParser#args.
    def visitArgs(self, ctx:ZCodeParser.ArgsContext):
        if ctx.getChildCount() == 0 : return []
        return self.visit(ctx.arg_list())


    # Visit a parse tree produced by ZCodeParser#arg_list.
    def visitArg_list(self, ctx:ZCodeParser.Arg_listContext):
        if ctx.getChildCount() == 1: return [self.visit(ctx.arg())]
        return [self.visit(ctx.arg())] + self.visit(ctx.arg_list())


    # Visit a parse tree produced by ZCodeParser#arg.
    def visitArg(self, ctx:ZCodeParser.ArgContext):
        id=Id(ctx.IDENTIFIER().getText())
        type_text = ctx.TYPE().getText() if ctx.TYPE() else None
        var_type = None
        if type_text:
            if type_text == 'number':
                var_type = NumberType()
            elif type_text == 'bool':
                var_type = BoolType()
            else:
                var_type = StringType()

        if ctx.getChildCount() == 2:
            return VarDecl(id,var_type,None,None)
        
        type_index = self.visit(ctx.type_index()) if ctx.type_index() else None
        return VarDecl(id,ArrayType(type_index,var_type),None,None)

# arg_group: LP args RP;
# args: arg_list | /* empty */;
# arg_list: arg | arg COMMA arg_list;
# arg: TYPE IDENTIFIER (type_index | );

    # Visit a parse tree produced by ZCodeParser#type_index.
    # return list of float
    def visitType_index(self, ctx:ZCodeParser.Type_indexContext):
        return self.visit(ctx.type_index_nums())

    # Visit a parse tree produced by ZCodeParser#type_index_nums.
    def visitType_index_nums(self, ctx:ZCodeParser.Type_index_numsContext):
        if ctx.getChildCount()==0: return []
        return self.visit(ctx.type_index_num_list())
        

    # Visit a parse tree produced by ZCodeParser#type_index_num_list.
    def visitType_index_num_list(self, ctx:ZCodeParser.Type_index_num_listContext):
        if ctx.getChildCount() == 1 : return [float(ctx.NumberLit().getText())]
        return [float(ctx.NumberLit().getText())] + self.visit(ctx.type_index_num_list())
# type_index: LB type_index_nums RB;
# type_index_nums: type_index_num_list | /* empty */;
# type_index_num_list: NumberLit | NumberLit COMMA type_index_num_list;

    # Visit a parse tree produced by ZCodeParser#ass.
    # ass: expr ASSIGN expr;
    def visitAss(self, ctx:ZCodeParser.AssContext):
        left_expr = self.visit(ctx.expr(0))
        right_expr = self.visit(ctx.expr(1))
        return Assign(left_expr,right_expr)

    # Visit a parse tree produced by ZCodeParser#decl.
    # grammar rules:
    # decl: TYPE IDENTIFIER (type_index | ) ((ASSIGN expr) | )
    # 	| VAR IDENTIFIER ASSIGN expr
    # 	| DYN IDENTIFIER ((ASSIGN expr) | );
    def visitDecl(self, ctx:ZCodeParser.DeclContext):
        identifier = Id(ctx.IDENTIFIER().getText())
        type_text = ctx.TYPE().getText() if ctx.TYPE() else None
        type_index = self.visit(ctx.type_index()) if ctx.type_index() else None
        expr = self.visit(ctx.expr()) if ctx.ASSIGN() else None
        var_type = None

        if type_text:
            if type_text == 'number':
                var_type = NumberType()
            elif type_text == 'bool':
                var_type = BoolType()
            else:
                var_type = StringType()

        if ctx.TYPE(): # array decl or normal variable decl
            if type_index:
                var_type = ArrayType(type_index, var_type)
            return VarDecl(identifier, var_type, None, expr)
        elif ctx.VAR(): # var decl
            return VarDecl(identifier, None, ctx.VAR().getText(), expr)
        elif ctx.DYN(): # dynamic decl
            return VarDecl(identifier, None, ctx.DYN().getText(), expr)

        return self.visitChildren(ctx)

    # Visit a parse tree produced by ZCodeParser#expr.
    # expr: expr1 op=CONCAT expr1 | expr1;
    def visitExpr(self, ctx:ZCodeParser.ExprContext):
        if ctx.getChildCount() == 1: return self.visit(ctx.expr1(0))
        return BinaryOp(ctx.CONCAT().getText(),self.visit(ctx.expr1(0)),self.visit(ctx.expr1(1)))


    # Visit a parse tree produced by ZCodeParser#expr1.
    # expr1: expr2 op=(EQ | DEQ | NEQ | LT | GT | LE | GE) expr2 | expr2;
    def visitExpr1(self, ctx:ZCodeParser.Expr1Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.expr2(0))
        return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.expr2(0)),self.visit(ctx.expr2(1)))


    # Visit a parse tree produced by ZCodeParser#expr2.
    # expr2: expr2 op=(AND | OR) expr3 | expr3;
    def visitExpr2(self, ctx:ZCodeParser.Expr2Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.expr3())
        return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.expr2()),self.visit(ctx.expr3()))


    # Visit a parse tree produced by ZCodeParser#expr3.
    # expr3: expr3 op=(ADD | SUB) expr4 | expr4;
    def visitExpr3(self, ctx:ZCodeParser.Expr3Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.expr4())
        return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.expr3()),self.visit(ctx.expr4()))

    # Visit a parse tree produced by ZCodeParser#expr4.
    # expr4: expr4 op=(MUL | DIV | MOD) expr5 | expr5;
    def visitExpr4(self, ctx:ZCodeParser.Expr4Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.expr5());
        return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.expr4()),self.visit(ctx.expr5()))


    # Visit a parse tree produced by ZCodeParser#expr5.
    def visitExpr5(self, ctx:ZCodeParser.Expr5Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.expr6())
        return UnaryOp(ctx.getChild(0),self.visit(ctx.expr5()))


    # Visit a parse tree produced by ZCodeParser#expr6.
    def visitExpr6(self, ctx:ZCodeParser.Expr6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.term())
        if ctx.LB(): return ArrayCell(self.visit(ctx.expr6()),self.visit(ctx.expr_list()))
        if ctx.LP(): return CallExpr(self.visit(ctx.expr6()),self.visit(ctx.expr_list()))
# expr6: expr6 LB expr_list RB // Array Expression
# 	| expr6 LP expr_list RP // Function Call Expression
# 	| term;

    # Visit a parse tree produced by ZCodeParser#term.
    def visitTerm(self, ctx:ZCodeParser.TermContext):
        if ctx.getChildCount() == 1:
            if ctx.NumberLit(): return NumberLiteral(float(ctx.NumberLit().getText()))
            if ctx.StringLit(): return StringLiteral(ctx.StringLit().getText())
            if ctx.BoolLit(): return BooleanLiteral(ctx.BoolLit().getText() == 'true')
            if ctx.IDENTIFIER(): return Id(ctx.IDENTIFIER().getText())
        if ctx.expr_list(): return ArrayLiteral(self.visit(ctx.expr_list()))
        if ctx.expr(): return self.visit(ctx.expr())


    # Visit a parse tree produced by ZCodeParser#expr_list.
    def visitExpr_list(self, ctx:ZCodeParser.Expr_listContext):
        if ctx.getChildCount() == 0: return []
        return self.visit(ctx.exprPrime())

# expr6: expr6 LB expr_list RB // Array Expression
# 	| expr6 LP expr_list RP // Function Call Expression
# 	| term;

# term: NumberLit
# 	| StringLit
# 	| BoolLit
# 	| IDENTIFIER	
# 	| LB expr_list RB
# 	| LP expr RP;
    
# expr_list: exprPrime | /* empty */;
# exprPrime: expr | expr COMMA exprPrime;
    # Visit a parse tree produced by ZCodeParser#exprPrime.
    def visitExprPrime(self, ctx:ZCodeParser.ExprPrimeContext):
        if ctx.getChildCount() == 1: return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.exprPrime())


    # Visit a parse tree produced by ZCodeParser#listOfNEWLINE.
    def visitListOfNEWLINE(self, ctx:ZCodeParser.ListOfNEWLINEContext):
        return self.visitChildren(ctx)