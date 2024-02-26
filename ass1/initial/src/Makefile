# Makefile

.PHONY: gen
gen:
	python run.py gen

.PHONY: parser_test
parser_test:
	python genTestCase.py ParserSuite

.PHONY: parser
parser:
	python run.py test ParserSuite

.PHONY: lexer_test
lexer_test:
	python run.py genTest LexerSuite

.PHONY: lexer
lexer:
	python run.py test LexerSuite

# Add other targets and rules as needed

# Usage instructions
printUsage:
	@echo "Usage:"
	@echo "make gen             # Clean and generate"
	@echo "make parser_test     # Generate test cases for ParserSuite"
	@echo "make parser          # Run tests for ParserSuite"
	@echo "make lexer_test      # Generate test cases for LexerSuite"
	@echo "make lexer           # Run tests for LexerSuite"
	@echo "..."