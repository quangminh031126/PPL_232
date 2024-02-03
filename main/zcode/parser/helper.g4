STRING_LITERAL:
	QUOTE (STRING_CONTENT)* QUOTE {self.text = self.text[1:-1] };

fragment STRING_CONTENT:
	LINE_STR_TEXT
	| LINE_STR_ESCAPED_CHAR
	| DOUBLE_QUOTE_CHAR;

fragment QUOTE: '"';

fragment LINE_STR_TEXT: ~('\n' | '\r' | '\\' | '"');

fragment LINE_STR_ESCAPED_CHAR: ESCAPED_IDENTIFIER;

fragment ILLEGAL_SEQUENCE: '\\' ~[btnfr'\\] | '\\';
fragment ESCAPED_IDENTIFIER: '\\' [btnfr'\\];

fragment ESCAPE_SEQ: ESCAPED_IDENTIFIER;

fragment DOUBLE_QUOTE_CHAR: '\'"';

UNCLOSE_STRING: QUOTE STRING_CONTENT* ([\r\n"] | EOF);
// { if self.text[-1] in ['\b', '\t', '\f', '\r', '\n', '"']: raise UncloseString(self.text[1:-1])
// else: raise UncloseString(self.text[1:]) };

ILLEGAL_ESCAPE: QUOTE STRING_CONTENT* (~[\\t"\n\f\r\b]);
//  { raise IllegalEscape(self.text[1:]) };