from lexer import Lexer


k = '"123.45 8485"""'
a = '12345.900'

l = Lexer(a)
l.lex()
 
print(l.tokens()) 