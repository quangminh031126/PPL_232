grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

program: function* mainFunction function* EOF;
mainFunction: 'main' '(' ')' '{' (statement)* '}' NEWLINE;


/* LEXER */

/* Keywords */
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

NumberLit: INTEGER (DECIMAL|DECIMAL? EXPONENT);
fragment DECIMAL: '.' INTEGER* ;
fragment EXPONENT: [eE] ('+'|'-')? INTEGER;
fragment INTEGER: DIGIT+;

BooleanLit: 'true'| 'false';

StringLit
	: '"' StringChars? '"'
	{setText(getText().substring(1, getText().length()-1));};

fragment StringChars: StringChar+;

fragment StringChar: ~["\\\r\n] | EscapedSequence | DoubleQuote;
fragment DoubleQuote: '\'"';
fragment EscapedSequence
    : '\\' [btnfr'\\]
    ;

IDENTIFIER: (LETTER|UNDERSCORE) (LETTER|UNDERSCORE|DIGIT)*;
fragment LETTER: [a-zA-Z];
fragment UNDERSCORE: '_';
fragment DIGIT: [0-9];




/* PARSER */


/* ARRAY */
arrayDeclaration: (NUMBER | BOOL | STRING) IDENTIFIER LSBracket arrayDim RSBracket LEFTARR LSBracket arrayInit RSBracket;
arrayDim: NumberLit COMMA arrayDim | NumberLit;
arrayInit
	: LSBracket numberList RSBracket
	| LSBracket boolList RSBracket 
	| LSBracket stringList RSBracket
	| LSBracket arrayList RSBracket
	;
numberList: numberPrime | /* empty */;
numberPrime: NumberLit COMMA numberPrime | NumberLit;

boolList: boolPrime| /* empty */;
boolPrime: BooleanLit COMMA boolPrime | BooleanLit;

stringList: stringPrime | /* empty */;
stringPrime: StringLit COMMA stringPrime | StringLit;

arrayList: arrayPrime | /* empty */;
arrayPrime: arrayInit COMMA arrayPrime | arrayInit;

/* NEGATION > MULT | DIV | MOD > PLUS | MINUS */
arithExpr: arithExpr (PLUS | MINUS) arithExpr1 | arithExpr1; /* Left associative */
arithExpr1: arithExpr1 (MULT | DIV | MOD) arithExpr2 | arithExpr2; /* Left associative */
arithExpr2: MINUS arithExpr2 | arithExpr3 ;
arithExpr3: IDENTIFIER | NumberLit;

/* NOT > AND > OR */
logicExpr: logicExpr OR logicExpr1 | logicExpr1;
logicExpr1: logicExpr1 AND logicExpr2 | logicExpr2;
logicExpr2: NOT logicExpr2 | logicExpr3;
logicExpr3: BooleanLit | IDENTIFIER;

/* String Expression */
stringConcatExpr: stringConcatExpr ELLIPSIS stringConcatExpr | StringLit | IDENTIFIER;

/* Relational Expression */

relExpr: arithComp | literalComp;
arithComp: arithExpr arithRelOp arithExpr;
literalComp: stringConcatExpr literalOp stringConcatExpr;
arithRelOp: EQUAL | NOTEQUAL | LESS | GREATER | LESSOREQUAL | GREATEROREQUAL;
literalOp: EQUALEQUAL;

/* Index Operator */

elementAccessExpr: arrExpr LSBracket indexOp RSBracket;
arrExpr: IDENTIFIER | functionCall;
indexOp: arrExpr COMMA indexOp | arrExpr;

/* Function Call */
functionCall: IDENTIFIER LBracket functionArgsList RBracket;
functionArgsList: argsPrime | /* Empty */;
argsPrime: arg COMMA argsPrime | arg;
arg: expression;


/* Variable and Function Declaration */

variableDeclaration: normalDeclaration | arrayDeclaration | varDecl | dynamicDecl;
normalDeclaration: varType variableInitialization?;
varType: (NUMBER|BOOL|STRING);
varDecl: VAR variableInitialization;
dynamicDecl: DYNAMIC variableInitialization?;

variableInitialization: LEFTARR expression;
expression: arithExpr | stringConcatExpr | relExpr | logicExpr | elementAccessExpr | functionCall;

paramDeclList: paramDeclPrime | /* empty */;
paramDeclPrime: paramDeclAtom COMMA paramDeclPrime | paramDeclAtom;
paramDeclAtom: varType IDENTIFIER (LSBracket arrayDim RSBracket)?;

function: FUNC IDENTIFIER LBracket paramDeclList RBracket nullableListOfNEWLINE (returnStatement | blockStatement)?;

nullableListOfNEWLINE: NEWLINE nullableListOfNEWLINE | /* empty */;

/* statements */
/* An action that a program performs */

/* Variable Declaration Statement */


/* If statement */
ifStatement: IF logicExpr statement elifStatementList elseStatement?;
elifStatementList: elifStatementPrime | /* empty */ ;
elifStatementPrime: elifStatement nullableListOfNEWLINE elifStatementPrime | elifStatement;
elifStatement: ELIF logicExpr statement;
elseStatement: ELSE logicExpr statement;

/* For statement */
forStatement
	: 
	FOR IDENTIFIER UNTIL logicExpr BY updateExpr nullableListOfNEWLINE statement
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
blockStatement: BEGIN NEWLINE+ blockStatementBody END NEWLINE+;
blockStatementBody: nullableListOfStatement;
nullableListOfStatement: statement nullableListOfStatement;

statement: (functionCallStatement|continueStatement|returnStatement|breakStatement|blockStatement|ifStatement | forStatement) nullableListOfNEWLINE;

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
ILLEGAL_ESCAPE: '\\' (~[bfrnt'\\] | ~'\\') {
    temp = self.text
    raise IllegalEscape(temp[1:])
};