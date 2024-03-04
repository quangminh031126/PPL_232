grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
    language=Python3;
}


/* LEXER */

/* Fragments */
fragment DECIMAL: '.' INTEGER? ;
fragment EXPONENT: [eE] ('+'|'-')? INTEGER;
fragment INTEGER: DIGIT+;
fragment StringChar: ~["\\\r\n] | EscapedSequence | DoubleQuote;
fragment DoubleQuote: '\'"';
fragment EscapedSequence
    : '\\' [btnfr'\\]
    ;
fragment LETTER: [a-zA-Z];
fragment UNDERSCORE: '_';
fragment DIGIT: [0-9];


/* Keywords */
TRUE: 'true';
FALSE: 'false';
NUMBER: 'number';
BOOL: 'bool';
STRING: 'string';
RETURN: 'return';
VAR: 'var';
DYNAMIC: 'dynamic';
FUNC: 'func';
FOR: 'for';
UNTIL: 'until';
BY: 'by';
BREAK: 'break';
CONTINUE: 'continue';
IF: 'if';
ELSE: 'else';
ELIF: 'elif';
BEGIN: 'begin';
END: 'end';
NOT: 'not';
AND: 'and';
OR: 'or';

/* Operators */
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
MOD: '%';
EQUAL: '=';
LEFTARR: '<-';
EQUALEQUAL: '==';
NOTEQUAL: '!=';
LESS: '<';
GREATER: '>';
LESSOREQUAL: '<=';
GREATEROREQUAL: '>=';
ELLIPSIS: '...';

/* Separator */
LBracket: '(';
RBracket: ')';
LSBracket: '[';
RSBracket: ']';
COMMA: ',';
NEWLINE: '\n';

/* Literals */

NumberLit: INTEGER (DECIMAL|DECIMAL? EXPONENT)?;


StringLit
    : '"' StringChar* '"'{        
    temp = self.text
    temp = temp[1:-1]  # Remove the opening and closing quotes
    self.text = temp
};

BoolLit: TRUE | FALSE;
literal: NumberLit | BoolLit | StringLit;
IDENTIFIER: (LETTER|UNDERSCORE) (LETTER|UNDERSCORE|DIGIT)*;


/* PARSER */

nullableListOfNEWLINE: NEWLINE nullableListOfNEWLINE |;
listOfNEWLINE: NEWLINE listOfNEWLINE | NEWLINE;
program: nullableListOfNEWLINE globalLevelDeclList EOF;

globalLevelDecl: functionDecl | variableDeclaration;
globalLevelDeclList: globalLevelDeclListPrime | /* empty */; // nullable
globalLevelDeclListPrime: globalLevelDecl listOfNEWLINE globalLevelDeclListPrime | globalLevelDecl;

blockLevelDecl: functionDecl | variableDeclaration;
blockLevelDeclList: blockLevelDeclListPrime | /* empty */;
blockLevelDeclListPrime: blockLevelDecl listOfNEWLINE blockLevelDeclListPrime | blockLevelDecl;

// declaration: (functionDecl | variableDeclaration ) (NEWLINE+|EOF);
functionDecl: functionFullDecl | functionPreDecl;

/* ARRAY */

arrayDeclaration: varType IDENTIFIER LSBracket arrayDim RSBracket arrayAssign?;
arrayDim: NumberLit COMMA arrayDim | NumberLit;
arrayAssign: LEFTARR ((LSBracket arrayElementList RSBracket) | expression);
arrayElementList
    : literalList
    | arrayList
    | expressionList
    ;
arrayList
    : LSBracket arrayElementList RSBracket COMMA arrayList
    | LSBracket arrayElementList RSBracket;
literalList: literal COMMA literalList | literal;

/* Index Operator */

elementAccessExpr: arrExpr LSBracket indexList RSBracket;
arrExpr: IDENTIFIER | functionCall;
indexList: expression COMMA indexList | expression;/* Non empty list of expression */

/* Function Call */
functionCall: IDENTIFIER LBracket functionArgsList RBracket;
functionArgsList: argsPrime | /* Empty */;
argsPrime: arg COMMA argsPrime | arg;
arg: expression;


assignStatement: scalarAssignStatement | arrayAssignStatement;
scalarAssignStatement: IDENTIFIER LEFTARR expression;
arrayAssignStatement: (IDENTIFIER | elementAccessExpr) arrayAssign;
/* Variable and Function Declaration */
statement
    : 
    ( /* variableDeclaration */
    /* variableInitialization arrayAssign */
    ifStatement
    | forStatement
    | breakStatement
    | continueStatement
    | returnStatement
    | functionCallStatement
    | blockStatement
    | assignStatement
    )
    (NEWLINE+|EOF);

variableDeclaration: (normalDeclaration | arrayDeclaration | varDecl | dynamicDecl);
normalDeclaration: varType IDENTIFIER variableInitialization?;
varType: (NUMBER|BOOL|STRING);
varDecl: VAR IDENTIFIER variableInitialization;
dynamicDecl: DYNAMIC IDENTIFIER variableInitialization?;

variableInitialization: LEFTARR expression;



functionPreDecl: FUNC IDENTIFIER LBracket paramDecl RBracket;
functionFullDecl: FUNC IDENTIFIER LBracket paramDecl RBracket nullableListOfNEWLINE functionBody;
paramDecl:  paramDeclList ;
paramDeclList: paramDeclPrime | /* empty */;
paramDeclPrime: paramDeclAtom COMMA paramDeclPrime | paramDeclAtom;
paramDeclAtom: varType IDENTIFIER (LSBracket arrayDim RSBracket)?;
functionBody: blockStatement | returnStatement;


/* statements */
/* An action that a program performs */

/* Variable Declaration Statement */


/* If statement */
ifStatement: IF expression nullableListOfNEWLINE statement elifStatementList elseStatement?;
elifStatementList: elifStatementPrime | /* empty */ ;
elifStatementPrime: elifStatement nullableListOfNEWLINE elifStatementPrime | elifStatement;
elifStatement: ELIF expression nullableListOfNEWLINE statement;
elseStatement: ELSE expression nullableListOfNEWLINE statement;

/* For statement */
forStatement
    : 
    FOR IDENTIFIER UNTIL expression BY updateExpr nullableListOfNEWLINE statement
    ;
updateExpr: expression;
/* Break statement */
breakStatement: BREAK;

/* Continute statement */
continueStatement: CONTINUE;

/* Return statement */
returnStatement: RETURN expression?;

/* Function call statement */
functionCallStatement: functionCall;

/* Block statement */
blockStatement: BEGIN (blockStatementBody) END;
blockStatementBody: nullableListOfStatement;
nullableListOfStatement: nullableListOfStatementPrime | /* empty */;
nullableListOfStatementPrime: (statement|blockLevelDecl) listOfNEWLINE nullableListOfStatementPrime| (statement|blockLevelDecl) ;


expressionList: expression COMMA expressionList | expression;
expression: expression1 ELLIPSIS expression1 | expression1;
expression1: expression2 ( EQUAL | EQUALEQUAL | NOTEQUAL | LESS | LESSOREQUAL | GREATER | GREATEROREQUAL ) expression2 | expression2;
expression2: expression2 (AND | OR) expression3 | expression3;
expression3: expression3 (PLUS | MINUS) expression4 | expression4;
expression4: expression4 (MULT | DIV | MOD) expression5 | expression5;
expression5: NOT expression5 | expression6;
expression6: MINUS expression6 | expression7;
expression7: elementAccessExpr | operands;
operands: literal | IDENTIFIER | (LBracket expression RBracket) | functionCall ; 

COMMENT: '##' .*? ~[\n\r\f]* -> skip;
WS : [ \t\r\f]+ -> skip ; // skip spaces, tabs, newlines, form feed

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING:  '"' StringChar* (NEWLINE|EOF){
    esc = ['\n']
    temp = str(self.text)
    if (temp[-1] in esc):
        raise UncloseString(temp[1:-1])
    else:
        raise UncloseString(temp[1:])
};
ILLEGAL_ESCAPE: '"' StringChar* '\\' (~[bfrnt'\\] | ~'\\') {
    temp = self.text
    raise IllegalEscape(temp[1:])
};