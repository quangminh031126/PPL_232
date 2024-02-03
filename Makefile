.PHONY: gen
gen:
	python run.py gen
.PHONY: parser
parser:
	python run.py test ParserSuite
.PHONY lexer:
lexer:
	python run.py test LexerSuite