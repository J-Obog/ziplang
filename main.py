from lex import Lexer


k = '"123.45 8485"""'
a = "5 > 7"

l = Lexer(a)
l.lex()
 
print(l.tokens()) 