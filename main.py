from lex import Lexer


k = '"123.45 8485"""'
a = "'jwekekw'"

l = Lexer(a)
l.lex()
 
print(l.tokens()[0].datatype()) 