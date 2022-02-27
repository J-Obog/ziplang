from lex import Lexer


k = "123.45 8485"

l = Lexer(k)
l.scan()

print(l.tokens()) 