
GRAMMAR	    = lc
CODE	    = achurch

default: 
	antlr4 -Dlanguage=Python3 -no-listener -visitor $(GRAMMAR).g4
	python3 $(CODE).py

fast:
	python3 $(CODE).py

visitors: 
	antlr4 -Dlanguage=Python3 -no-listener -visitor $(GRAMMAR).g4

clean:
	rm -rf *.interp *.tokens *Parser.py *Visitor.py *Lexer.py __pycache__ .antlr 