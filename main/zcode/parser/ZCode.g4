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


BooleanLit: TRUE| FALSE;

StringLit
    : '"' StringChar* '"'{        
    temp = self.text
    temp = temp[1:-1]  # Remove the opening and closing quotes
    self.text = temp
};

literal: NumberLit | BooleanLit | StringLit;
IDENTIFIER: (LETTER|UNDERSCORE) (LETTER|UNDERSCORE|DIGIT)*;


/* PARSER */

program: NEWLINE* declaration* EOF;

declaration: (functionDecl | variableDeclaration );

/* ARRAY */

arrayDeclaration: varType IDENTIFIER LSBracket arrayDim RSBracket arrayAssign?;
arrayDim: NumberLit COMMA arrayDim | NumberLit;
arrayAssign: LEFTARR LSBracket arrayElementList RSBracket;
arrayElementList
    : literalList
    | arrayList
    ;
arrayList
    : LSBracket arrayElementList RSBracket COMMA arrayList
    | LSBracket arrayElementList RSBracket;
literalList: literal COMMA literalList | literal;
// numberList: numberPrime | /* empty */;
// numberPrime: NumberLit COMMA numberPrime | NumberLit;

// boolList: boolPrime| /* empty */;
// boolPrime: BooleanLit COMMA boolPrime | BooleanLit;

// stringList: stringPrime | /* empty */;
// stringPrime: StringLit COMMA stringPrime | StringLit;



// /* NEGATION > MULT | DIV | MOD > PLUS | MINUS */
// arithExpr: arithExpr (PLUS | MINUS) arithExpr1 | arithExpr1; /* Left associative */
// arithExpr1: arithExpr1 (MULT | DIV | MOD) arithExpr2 | arithExpr2; /* Left associative */
// arithExpr2: MINUS arithExpr2 | arithExpr3 ;
// arithExpr3: IDENTIFIER | NumberLit;

// /* NOT > AND > OR */
// logicExpr: logicExpr OR logicExpr1 | logicExpr1;
// logicExpr1: logicExpr1 AND logicExpr2 | logicExpr2;
// logicExpr2: NOT logicExpr2 | logicExpr3;
// logicExpr3: BooleanLit | IDENTIFIER;

// /* String Expression */
// stringConcatExpr: stringConcatExpr ELLIPSIS stringConcatExpr | StringLit | IDENTIFIER;

// /* Relational Expression */

// relExpr: arithComp | literalComp;
// arithComp: arithExpr arithRelOp arithExpr;
// literalComp: stringConcatExpr literalOp stringConcatExpr;
// arithRelOp: EQUAL | NOTEQUAL | LESS | GREATER | LESSOREQUAL | GREATEROREQUAL;
// literalOp: EQUALEQUAL;
// expression: arithExpr | stringConcatExpr | relExpr | logicExpr | elementAccessExpr | functionCall;

/* Index Operator */

elementAccessExpr: arrExpr LSBracket indexList RSBracket;
arrExpr: IDENTIFIER | functionCall;
indexList: expression COMMA indexList | expression;/* Non empty list of expression */

/* Function Call */
functionCall: IDENTIFIER LBracket functionArgsList RBracket;
functionArgsList: argsPrime | /* Empty */;
argsPrime: arg COMMA argsPrime | arg;
arg: expression;


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
    )
    (NEWLINE+|EOF);

variableDeclaration: (normalDeclaration | arrayDeclaration | varDecl | dynamicDecl) NEWLINE+;
normalDeclaration: varType variableInitialization?;
varType: (NUMBER|BOOL|STRING);
varDecl: VAR variableInitialization;
dynamicDecl: DYNAMIC variableInitialization?;

variableInitialization: LEFTARR expression;

paramDeclList: paramDeclPrime | /* empty */;
paramDeclPrime: paramDeclAtom COMMA paramDeclPrime | paramDeclAtom;
paramDeclAtom: varType IDENTIFIER (LSBracket arrayDim RSBracket)?;

functionDecl: FUNC IDENTIFIER paramDecl NEWLINE* functionBody NEWLINE+;
paramDecl: LBracket paramDeclList RBracket;
functionBody: (returnStatement | blockStatement)?;


/* statements */
/* An action that a program performs */

/* Variable Declaration Statement */


/* If statement */
ifStatement: IF expression statement elifStatementList elseStatement?;
elifStatementList: elifStatementPrime | /* empty */ ;
elifStatementPrime: elifStatement NEWLINE* elifStatementPrime | elifStatement;
elifStatement: ELIF expression statement;
elseStatement: ELSE expression statement;

/* For statement */
forStatement
    : 
    FOR IDENTIFIER UNTIL expression BY updateExpr NEWLINE* statement
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
blockStatement: BEGIN NEWLINE+ blockStatementBody END;
blockStatementBody: nullableListOfStatement;
nullableListOfStatement: (statement|declaration) nullableListOfStatement|/* empty */;

expressionList: expression COMMA expressionList | expression;
expression: expression1 ELLIPSIS expression1 | expression1;
expression1: expression1 ( EQUAL | EQUALEQUAL | NOTEQUAL | LESS | LESSOREQUAL | GREATER | GREATEROREQUAL ) expression1 | expression2;
expression2: expression2 (AND | OR) expression3 | expression3;
expression3: expression3 (PLUS | MINUS) expression4 | expression4;
expression4: expression4 (MULT | DIV | MOD) expression5 | expression5;
expression5: NOT expression5 | expression6;
expression6: MINUS expression6 | expression7;
expression7: elementAccessExpr | operands;
operands: IDENTIFIER | literal | (LBracket expression RBracket) | functionCall ; 

COMMENT: '##' .*? ('\n'| EOF) -> skip;
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
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