from lexer import Lexer

txt = "'a'"

l = Lexer(txt)
 
print(l.next_token()) 
print(l.next_token()) 