grammar: regEx.g4
	antlr4 -Dlanguage=Python3 -no-listener -visitor regEx.g4

clear:
	rm -f *.interp
	rm -f *.tokens
	rm -f regExLexer.py
	rm -f regExVisitor.py
	rm -f regExParser.py
