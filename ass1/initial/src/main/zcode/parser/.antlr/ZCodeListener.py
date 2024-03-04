# Generated from /Users/phamvoquangminh/repos/ass_PPL/PPL_232/ass1/initial/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete listener for a parse tree produced by ZCodeParser.
class ZCodeListener(ParseTreeListener):

    # Enter a parse tree produced by ZCodeParser#literal.
    def enterLiteral(self, ctx:ZCodeParser.LiteralContext):
        pass

    # Exit a parse tree produced by ZCodeParser#literal.
    def exitLiteral(self, ctx:ZCodeParser.LiteralContext):
        pass


    # Enter a parse tree produced by ZCodeParser#program.
    def enterProgram(self, ctx:ZCodeParser.ProgramContext):
        pass

    # Exit a parse tree produced by ZCodeParser#program.
    def exitProgram(self, ctx:ZCodeParser.ProgramContext):
        pass


    # Enter a parse tree produced by ZCodeParser#declaration.
    def enterDeclaration(self, ctx:ZCodeParser.DeclarationContext):
        pass

    # Exit a parse tree produced by ZCodeParser#declaration.
    def exitDeclaration(self, ctx:ZCodeParser.DeclarationContext):
        pass


    # Enter a parse tree produced by ZCodeParser#function.
    def enterFunction(self, ctx:ZCodeParser.FunctionContext):
        pass

    # Exit a parse tree produced by ZCodeParser#function.
    def exitFunction(self, ctx:ZCodeParser.FunctionContext):
        pass


    # Enter a parse tree produced by ZCodeParser#function1.
    def enterFunction1(self, ctx:ZCodeParser.Function1Context):
        pass

    # Exit a parse tree produced by ZCodeParser#function1.
    def exitFunction1(self, ctx:ZCodeParser.Function1Context):
        pass


    # Enter a parse tree produced by ZCodeParser#arrayDeclaration.
    def enterArrayDeclaration(self, ctx:ZCodeParser.ArrayDeclarationContext):
        pass

    # Exit a parse tree produced by ZCodeParser#arrayDeclaration.
    def exitArrayDeclaration(self, ctx:ZCodeParser.ArrayDeclarationContext):
        pass


    # Enter a parse tree produced by ZCodeParser#arrayDim.
    def enterArrayDim(self, ctx:ZCodeParser.ArrayDimContext):
        pass

    # Exit a parse tree produced by ZCodeParser#arrayDim.
    def exitArrayDim(self, ctx:ZCodeParser.ArrayDimContext):
        pass


    # Enter a parse tree produced by ZCodeParser#arrayAssign.
    def enterArrayAssign(self, ctx:ZCodeParser.ArrayAssignContext):
        pass

    # Exit a parse tree produced by ZCodeParser#arrayAssign.
    def exitArrayAssign(self, ctx:ZCodeParser.ArrayAssignContext):
        pass


    # Enter a parse tree produced by ZCodeParser#arrayElementList.
    def enterArrayElementList(self, ctx:ZCodeParser.ArrayElementListContext):
        pass

    # Exit a parse tree produced by ZCodeParser#arrayElementList.
    def exitArrayElementList(self, ctx:ZCodeParser.ArrayElementListContext):
        pass


    # Enter a parse tree produced by ZCodeParser#arrayList.
    def enterArrayList(self, ctx:ZCodeParser.ArrayListContext):
        pass

    # Exit a parse tree produced by ZCodeParser#arrayList.
    def exitArrayList(self, ctx:ZCodeParser.ArrayListContext):
        pass


    # Enter a parse tree produced by ZCodeParser#literalList.
    def enterLiteralList(self, ctx:ZCodeParser.LiteralListContext):
        pass

    # Exit a parse tree produced by ZCodeParser#literalList.
    def exitLiteralList(self, ctx:ZCodeParser.LiteralListContext):
        pass


    # Enter a parse tree produced by ZCodeParser#elementAccessExpr.
    def enterElementAccessExpr(self, ctx:ZCodeParser.ElementAccessExprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#elementAccessExpr.
    def exitElementAccessExpr(self, ctx:ZCodeParser.ElementAccessExprContext):
        pass


    # Enter a parse tree produced by ZCodeParser#arrExpr.
    def enterArrExpr(self, ctx:ZCodeParser.ArrExprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#arrExpr.
    def exitArrExpr(self, ctx:ZCodeParser.ArrExprContext):
        pass


    # Enter a parse tree produced by ZCodeParser#indexList.
    def enterIndexList(self, ctx:ZCodeParser.IndexListContext):
        pass

    # Exit a parse tree produced by ZCodeParser#indexList.
    def exitIndexList(self, ctx:ZCodeParser.IndexListContext):
        pass


    # Enter a parse tree produced by ZCodeParser#functionCall.
    def enterFunctionCall(self, ctx:ZCodeParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by ZCodeParser#functionCall.
    def exitFunctionCall(self, ctx:ZCodeParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by ZCodeParser#functionArgsList.
    def enterFunctionArgsList(self, ctx:ZCodeParser.FunctionArgsListContext):
        pass

    # Exit a parse tree produced by ZCodeParser#functionArgsList.
    def exitFunctionArgsList(self, ctx:ZCodeParser.FunctionArgsListContext):
        pass


    # Enter a parse tree produced by ZCodeParser#argsPrime.
    def enterArgsPrime(self, ctx:ZCodeParser.ArgsPrimeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#argsPrime.
    def exitArgsPrime(self, ctx:ZCodeParser.ArgsPrimeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#arg.
    def enterArg(self, ctx:ZCodeParser.ArgContext):
        pass

    # Exit a parse tree produced by ZCodeParser#arg.
    def exitArg(self, ctx:ZCodeParser.ArgContext):
        pass


    # Enter a parse tree produced by ZCodeParser#assignStatement.
    def enterAssignStatement(self, ctx:ZCodeParser.AssignStatementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#assignStatement.
    def exitAssignStatement(self, ctx:ZCodeParser.AssignStatementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#scalarAssignStatement.
    def enterScalarAssignStatement(self, ctx:ZCodeParser.ScalarAssignStatementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#scalarAssignStatement.
    def exitScalarAssignStatement(self, ctx:ZCodeParser.ScalarAssignStatementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#arrayAssignStatement.
    def enterArrayAssignStatement(self, ctx:ZCodeParser.ArrayAssignStatementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#arrayAssignStatement.
    def exitArrayAssignStatement(self, ctx:ZCodeParser.ArrayAssignStatementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#statement.
    def enterStatement(self, ctx:ZCodeParser.StatementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#statement.
    def exitStatement(self, ctx:ZCodeParser.StatementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:ZCodeParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by ZCodeParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:ZCodeParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by ZCodeParser#normalDeclaration.
    def enterNormalDeclaration(self, ctx:ZCodeParser.NormalDeclarationContext):
        pass

    # Exit a parse tree produced by ZCodeParser#normalDeclaration.
    def exitNormalDeclaration(self, ctx:ZCodeParser.NormalDeclarationContext):
        pass


    # Enter a parse tree produced by ZCodeParser#varType.
    def enterVarType(self, ctx:ZCodeParser.VarTypeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#varType.
    def exitVarType(self, ctx:ZCodeParser.VarTypeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#varDecl.
    def enterVarDecl(self, ctx:ZCodeParser.VarDeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#varDecl.
    def exitVarDecl(self, ctx:ZCodeParser.VarDeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#dynamicDecl.
    def enterDynamicDecl(self, ctx:ZCodeParser.DynamicDeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#dynamicDecl.
    def exitDynamicDecl(self, ctx:ZCodeParser.DynamicDeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#variableInitialization.
    def enterVariableInitialization(self, ctx:ZCodeParser.VariableInitializationContext):
        pass

    # Exit a parse tree produced by ZCodeParser#variableInitialization.
    def exitVariableInitialization(self, ctx:ZCodeParser.VariableInitializationContext):
        pass


    # Enter a parse tree produced by ZCodeParser#paramDeclList.
    def enterParamDeclList(self, ctx:ZCodeParser.ParamDeclListContext):
        pass

    # Exit a parse tree produced by ZCodeParser#paramDeclList.
    def exitParamDeclList(self, ctx:ZCodeParser.ParamDeclListContext):
        pass


    # Enter a parse tree produced by ZCodeParser#paramDeclPrime.
    def enterParamDeclPrime(self, ctx:ZCodeParser.ParamDeclPrimeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#paramDeclPrime.
    def exitParamDeclPrime(self, ctx:ZCodeParser.ParamDeclPrimeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#paramDeclAtom.
    def enterParamDeclAtom(self, ctx:ZCodeParser.ParamDeclAtomContext):
        pass

    # Exit a parse tree produced by ZCodeParser#paramDeclAtom.
    def exitParamDeclAtom(self, ctx:ZCodeParser.ParamDeclAtomContext):
        pass


    # Enter a parse tree produced by ZCodeParser#functionDecl.
    def enterFunctionDecl(self, ctx:ZCodeParser.FunctionDeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#functionDecl.
    def exitFunctionDecl(self, ctx:ZCodeParser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#functionPreDecl.
    def enterFunctionPreDecl(self, ctx:ZCodeParser.FunctionPreDeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#functionPreDecl.
    def exitFunctionPreDecl(self, ctx:ZCodeParser.FunctionPreDeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#paramDecl.
    def enterParamDecl(self, ctx:ZCodeParser.ParamDeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#paramDecl.
    def exitParamDecl(self, ctx:ZCodeParser.ParamDeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#functionBody.
    def enterFunctionBody(self, ctx:ZCodeParser.FunctionBodyContext):
        pass

    # Exit a parse tree produced by ZCodeParser#functionBody.
    def exitFunctionBody(self, ctx:ZCodeParser.FunctionBodyContext):
        pass


    # Enter a parse tree produced by ZCodeParser#ifStatement.
    def enterIfStatement(self, ctx:ZCodeParser.IfStatementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#ifStatement.
    def exitIfStatement(self, ctx:ZCodeParser.IfStatementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#elifStatementList.
    def enterElifStatementList(self, ctx:ZCodeParser.ElifStatementListContext):
        pass

    # Exit a parse tree produced by ZCodeParser#elifStatementList.
    def exitElifStatementList(self, ctx:ZCodeParser.ElifStatementListContext):
        pass


    # Enter a parse tree produced by ZCodeParser#elifStatementPrime.
    def enterElifStatementPrime(self, ctx:ZCodeParser.ElifStatementPrimeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#elifStatementPrime.
    def exitElifStatementPrime(self, ctx:ZCodeParser.ElifStatementPrimeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#elifStatement.
    def enterElifStatement(self, ctx:ZCodeParser.ElifStatementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#elifStatement.
    def exitElifStatement(self, ctx:ZCodeParser.ElifStatementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#elseStatement.
    def enterElseStatement(self, ctx:ZCodeParser.ElseStatementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#elseStatement.
    def exitElseStatement(self, ctx:ZCodeParser.ElseStatementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#forStatement.
    def enterForStatement(self, ctx:ZCodeParser.ForStatementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#forStatement.
    def exitForStatement(self, ctx:ZCodeParser.ForStatementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#updateExpr.
    def enterUpdateExpr(self, ctx:ZCodeParser.UpdateExprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#updateExpr.
    def exitUpdateExpr(self, ctx:ZCodeParser.UpdateExprContext):
        pass


    # Enter a parse tree produced by ZCodeParser#breakStatement.
    def enterBreakStatement(self, ctx:ZCodeParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#breakStatement.
    def exitBreakStatement(self, ctx:ZCodeParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#continueStatement.
    def enterContinueStatement(self, ctx:ZCodeParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#continueStatement.
    def exitContinueStatement(self, ctx:ZCodeParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#returnStatement.
    def enterReturnStatement(self, ctx:ZCodeParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#returnStatement.
    def exitReturnStatement(self, ctx:ZCodeParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#functionCallStatement.
    def enterFunctionCallStatement(self, ctx:ZCodeParser.FunctionCallStatementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#functionCallStatement.
    def exitFunctionCallStatement(self, ctx:ZCodeParser.FunctionCallStatementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#blockStatement.
    def enterBlockStatement(self, ctx:ZCodeParser.BlockStatementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#blockStatement.
    def exitBlockStatement(self, ctx:ZCodeParser.BlockStatementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#blockStatementBody.
    def enterBlockStatementBody(self, ctx:ZCodeParser.BlockStatementBodyContext):
        pass

    # Exit a parse tree produced by ZCodeParser#blockStatementBody.
    def exitBlockStatementBody(self, ctx:ZCodeParser.BlockStatementBodyContext):
        pass


    # Enter a parse tree produced by ZCodeParser#nullableListOfStatement.
    def enterNullableListOfStatement(self, ctx:ZCodeParser.NullableListOfStatementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#nullableListOfStatement.
    def exitNullableListOfStatement(self, ctx:ZCodeParser.NullableListOfStatementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expressionList.
    def enterExpressionList(self, ctx:ZCodeParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expressionList.
    def exitExpressionList(self, ctx:ZCodeParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expression.
    def enterExpression(self, ctx:ZCodeParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expression.
    def exitExpression(self, ctx:ZCodeParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expression1.
    def enterExpression1(self, ctx:ZCodeParser.Expression1Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expression1.
    def exitExpression1(self, ctx:ZCodeParser.Expression1Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expression2.
    def enterExpression2(self, ctx:ZCodeParser.Expression2Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expression2.
    def exitExpression2(self, ctx:ZCodeParser.Expression2Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expression3.
    def enterExpression3(self, ctx:ZCodeParser.Expression3Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expression3.
    def exitExpression3(self, ctx:ZCodeParser.Expression3Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expression4.
    def enterExpression4(self, ctx:ZCodeParser.Expression4Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expression4.
    def exitExpression4(self, ctx:ZCodeParser.Expression4Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expression5.
    def enterExpression5(self, ctx:ZCodeParser.Expression5Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expression5.
    def exitExpression5(self, ctx:ZCodeParser.Expression5Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expression6.
    def enterExpression6(self, ctx:ZCodeParser.Expression6Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expression6.
    def exitExpression6(self, ctx:ZCodeParser.Expression6Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expression7.
    def enterExpression7(self, ctx:ZCodeParser.Expression7Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expression7.
    def exitExpression7(self, ctx:ZCodeParser.Expression7Context):
        pass


    # Enter a parse tree produced by ZCodeParser#operands.
    def enterOperands(self, ctx:ZCodeParser.OperandsContext):
        pass

    # Exit a parse tree produced by ZCodeParser#operands.
    def exitOperands(self, ctx:ZCodeParser.OperandsContext):
        pass



del ZCodeParser