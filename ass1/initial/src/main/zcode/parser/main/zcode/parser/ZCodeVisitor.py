# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#literal.
    def visitLiteral(self, ctx:ZCodeParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#functionDecl.
    def visitFunctionDecl(self, ctx:ZCodeParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#declaration.
    def visitDeclaration(self, ctx:ZCodeParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function.
    def visitFunction(self, ctx:ZCodeParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function1.
    def visitFunction1(self, ctx:ZCodeParser.Function1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arrayDeclaration.
    def visitArrayDeclaration(self, ctx:ZCodeParser.ArrayDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arrayDim.
    def visitArrayDim(self, ctx:ZCodeParser.ArrayDimContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arrayAssign.
    def visitArrayAssign(self, ctx:ZCodeParser.ArrayAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arrayElementList.
    def visitArrayElementList(self, ctx:ZCodeParser.ArrayElementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arrayList.
    def visitArrayList(self, ctx:ZCodeParser.ArrayListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#literalList.
    def visitLiteralList(self, ctx:ZCodeParser.LiteralListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elementAccessExpr.
    def visitElementAccessExpr(self, ctx:ZCodeParser.ElementAccessExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arrExpr.
    def visitArrExpr(self, ctx:ZCodeParser.ArrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#indexList.
    def visitIndexList(self, ctx:ZCodeParser.IndexListContext):
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


    # Visit a parse tree produced by ZCodeParser#paramDeclList.
    def visitParamDeclList(self, ctx:ZCodeParser.ParamDeclListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paramDeclPrime.
    def visitParamDeclPrime(self, ctx:ZCodeParser.ParamDeclPrimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paramDeclAtom.
    def visitParamDeclAtom(self, ctx:ZCodeParser.ParamDeclAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#functionPreDecl.
    def visitFunctionPreDecl(self, ctx:ZCodeParser.FunctionPreDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paramDecl.
    def visitParamDecl(self, ctx:ZCodeParser.ParamDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#functionBody.
    def visitFunctionBody(self, ctx:ZCodeParser.FunctionBodyContext):
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


    # Visit a parse tree produced by ZCodeParser#expressionList.
    def visitExpressionList(self, ctx:ZCodeParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression.
    def visitExpression(self, ctx:ZCodeParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression1.
    def visitExpression1(self, ctx:ZCodeParser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression2.
    def visitExpression2(self, ctx:ZCodeParser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression3.
    def visitExpression3(self, ctx:ZCodeParser.Expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression4.
    def visitExpression4(self, ctx:ZCodeParser.Expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression5.
    def visitExpression5(self, ctx:ZCodeParser.Expression5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression6.
    def visitExpression6(self, ctx:ZCodeParser.Expression6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression7.
    def visitExpression7(self, ctx:ZCodeParser.Expression7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#operands.
    def visitOperands(self, ctx:ZCodeParser.OperandsContext):
        return self.visitChildren(ctx)



del ZCodeParser