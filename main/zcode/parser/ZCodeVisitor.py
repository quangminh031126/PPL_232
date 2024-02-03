# Generated from ./main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#mainFunction.
    def visitMainFunction(self, ctx:ZCodeParser.MainFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl.
    def visitDecl(self, ctx:ZCodeParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arrayDeclaration.
    def visitArrayDeclaration(self, ctx:ZCodeParser.ArrayDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arrayDim.
    def visitArrayDim(self, ctx:ZCodeParser.ArrayDimContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arrayInit.
    def visitArrayInit(self, ctx:ZCodeParser.ArrayInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#numberList.
    def visitNumberList(self, ctx:ZCodeParser.NumberListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#numberPrime.
    def visitNumberPrime(self, ctx:ZCodeParser.NumberPrimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#boolList.
    def visitBoolList(self, ctx:ZCodeParser.BoolListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#boolPrime.
    def visitBoolPrime(self, ctx:ZCodeParser.BoolPrimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stringList.
    def visitStringList(self, ctx:ZCodeParser.StringListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stringPrime.
    def visitStringPrime(self, ctx:ZCodeParser.StringPrimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arrayList.
    def visitArrayList(self, ctx:ZCodeParser.ArrayListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arrayPrime.
    def visitArrayPrime(self, ctx:ZCodeParser.ArrayPrimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arithExpr.
    def visitArithExpr(self, ctx:ZCodeParser.ArithExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arithExpr1.
    def visitArithExpr1(self, ctx:ZCodeParser.ArithExpr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arithExpr2.
    def visitArithExpr2(self, ctx:ZCodeParser.ArithExpr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arithExpr3.
    def visitArithExpr3(self, ctx:ZCodeParser.ArithExpr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#logicExpr.
    def visitLogicExpr(self, ctx:ZCodeParser.LogicExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#logicExpr1.
    def visitLogicExpr1(self, ctx:ZCodeParser.LogicExpr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#logicExpr2.
    def visitLogicExpr2(self, ctx:ZCodeParser.LogicExpr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#logicExpr3.
    def visitLogicExpr3(self, ctx:ZCodeParser.LogicExpr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stringConcatExpr.
    def visitStringConcatExpr(self, ctx:ZCodeParser.StringConcatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#relExpr.
    def visitRelExpr(self, ctx:ZCodeParser.RelExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arithComp.
    def visitArithComp(self, ctx:ZCodeParser.ArithCompContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#literalComp.
    def visitLiteralComp(self, ctx:ZCodeParser.LiteralCompContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arithRelOp.
    def visitArithRelOp(self, ctx:ZCodeParser.ArithRelOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#literalOp.
    def visitLiteralOp(self, ctx:ZCodeParser.LiteralOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elementAccessExpr.
    def visitElementAccessExpr(self, ctx:ZCodeParser.ElementAccessExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arrExpr.
    def visitArrExpr(self, ctx:ZCodeParser.ArrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#indexOp.
    def visitIndexOp(self, ctx:ZCodeParser.IndexOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#functionCall.
    def visitFunctionCall(self, ctx:ZCodeParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#functionArgsList.
    def visitFunctionArgsList(self, ctx:ZCodeParser.FunctionArgsListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#argsPrime.
    def visitArgsPrime(self, ctx:ZCodeParser.ArgsPrimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arg.
    def visitArg(self, ctx:ZCodeParser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#statement.
    def visitStatement(self, ctx:ZCodeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:ZCodeParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#normalDeclaration.
    def visitNormalDeclaration(self, ctx:ZCodeParser.NormalDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#varType.
    def visitVarType(self, ctx:ZCodeParser.VarTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#varDecl.
    def visitVarDecl(self, ctx:ZCodeParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#dynamicDecl.
    def visitDynamicDecl(self, ctx:ZCodeParser.DynamicDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#variableInitialization.
    def visitVariableInitialization(self, ctx:ZCodeParser.VariableInitializationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression.
    def visitExpression(self, ctx:ZCodeParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paramDeclList.
    def visitParamDeclList(self, ctx:ZCodeParser.ParamDeclListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paramDeclPrime.
    def visitParamDeclPrime(self, ctx:ZCodeParser.ParamDeclPrimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paramDeclAtom.
    def visitParamDeclAtom(self, ctx:ZCodeParser.ParamDeclAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#functionDecl.
    def visitFunctionDecl(self, ctx:ZCodeParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#nullableListOfNEWLINE.
    def visitNullableListOfNEWLINE(self, ctx:ZCodeParser.NullableListOfNEWLINEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ifStatement.
    def visitIfStatement(self, ctx:ZCodeParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elifStatementList.
    def visitElifStatementList(self, ctx:ZCodeParser.ElifStatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elifStatementPrime.
    def visitElifStatementPrime(self, ctx:ZCodeParser.ElifStatementPrimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elifStatement.
    def visitElifStatement(self, ctx:ZCodeParser.ElifStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elseStatement.
    def visitElseStatement(self, ctx:ZCodeParser.ElseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#forStatement.
    def visitForStatement(self, ctx:ZCodeParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#updateExpr.
    def visitUpdateExpr(self, ctx:ZCodeParser.UpdateExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#breakStatement.
    def visitBreakStatement(self, ctx:ZCodeParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#continueStatement.
    def visitContinueStatement(self, ctx:ZCodeParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#returnStatement.
    def visitReturnStatement(self, ctx:ZCodeParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#functionCallStatement.
    def visitFunctionCallStatement(self, ctx:ZCodeParser.FunctionCallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#blockStatement.
    def visitBlockStatement(self, ctx:ZCodeParser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#blockStatementBody.
    def visitBlockStatementBody(self, ctx:ZCodeParser.BlockStatementBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#nullableListOfStatement.
    def visitNullableListOfStatement(self, ctx:ZCodeParser.NullableListOfStatementContext):
        return self.visitChildren(ctx)



del ZCodeParser