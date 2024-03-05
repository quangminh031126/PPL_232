from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *


class ASTGeneration(ZCodeVisitor):

    def visitProgram(self, ctx: ZCodeParser.ProgramContext):
        return Program([VarDecl(Id(ctx.IDENTIFIER().getText()), NumberType())])
# Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stms.
    def visitStms(self, ctx:ZCodeParser.StmsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stm_lists.
    def visitStm_lists(self, ctx:ZCodeParser.Stm_listsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stm.
    def visitStm(self, ctx:ZCodeParser.StmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#r_break.
    def visitR_break(self, ctx:ZCodeParser.R_breakContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#r_continue.
    def visitR_continue(self, ctx:ZCodeParser.R_continueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#r_return.
    def visitR_return(self, ctx:ZCodeParser.R_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#r_if.
    def visitR_if(self, ctx:ZCodeParser.R_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#r_elifs.
    def visitR_elifs(self, ctx:ZCodeParser.R_elifsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#r_elif.
    def visitR_elif(self, ctx:ZCodeParser.R_elifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#r_else.
    def visitR_else(self, ctx:ZCodeParser.R_elseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#r_for.
    def visitR_for(self, ctx:ZCodeParser.R_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#block.
    def visitBlock(self, ctx:ZCodeParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#block_stms.
    def visitBlock_stms(self, ctx:ZCodeParser.Block_stmsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func.
    def visitFunc(self, ctx:ZCodeParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arg_group.
    def visitArg_group(self, ctx:ZCodeParser.Arg_groupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#args.
    def visitArgs(self, ctx:ZCodeParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arg_list.
    def visitArg_list(self, ctx:ZCodeParser.Arg_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arg.
    def visitArg(self, ctx:ZCodeParser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#type_index.
    def visitType_index(self, ctx:ZCodeParser.Type_indexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#type_index_nums.
    def visitType_index_nums(self, ctx:ZCodeParser.Type_index_numsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#type_index_num_list.
    def visitType_index_num_list(self, ctx:ZCodeParser.Type_index_num_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ass.
    def visitAss(self, ctx:ZCodeParser.AssContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl.
    def visitDecl(self, ctx:ZCodeParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr.
    def visitExpr(self, ctx:ZCodeParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr1.
    def visitExpr1(self, ctx:ZCodeParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr2.
    def visitExpr2(self, ctx:ZCodeParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr3.
    def visitExpr3(self, ctx:ZCodeParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr4.
    def visitExpr4(self, ctx:ZCodeParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr5.
    def visitExpr5(self, ctx:ZCodeParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr6.
    def visitExpr6(self, ctx:ZCodeParser.Expr6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.term())
        return 


    # Visit a parse tree produced by ZCodeParser#term.
    def visitTerm(self, ctx:ZCodeParser.TermContext):
        if ctx.getChildCount() == 1:
            if ctx.NumberLit(): return float(NumberLiteral(ctx.NumberLit().getText()))
            if ctx.StringLit(): return StringLiteral(ctx.StringLit().getText())
            if ctx.BoolLit(): return BooleanLiteral(ctx.BoolLit().getText())
            if ctx.IDENTIFIER(): return Id(ctx.IDENTIFIER().getText())
        if ctx.expr_list(): return self.visit(ctx.expr_list())
        if ctx.expr(): return self.visit(ctx.expr())


    # Visit a parse tree produced by ZCodeParser#expr_list.
    def visitExpr_list(self, ctx:ZCodeParser.Expr_listContext):
        if ctx.getChildCount() == 0: return []
        return self.visit(ctx.exprPrime())


    # Visit a parse tree produced by ZCodeParser#exprPrime.
    def visitExprPrime(self, ctx:ZCodeParser.ExprPrimeContext):
        if ctx.getChildCount() == 1: return [self.visit(ctx.expr())]
        return self.visit(ctx.expr()) + self.visit(ctx.exprPrime())


    # Visit a parse tree produced by ZCodeParser#listOfNEWLINE.
    def visitListOfNEWLINE(self, ctx:ZCodeParser.ListOfNEWLINEContext):
        return self.visitChildren(ctx)