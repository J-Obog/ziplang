from lex import Lexer


k = '"123.45 8485"""'
a = "if( 5 > 8 ) { }"

l = Lexer(a)
l.lex()
 
print(l.tokens()) 