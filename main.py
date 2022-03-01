from lexer import Lexer


k = '"123.45 8485"""'
a = "'h'"

l = Lexer(a)
l.lex()
 
print(l.tokens()) 