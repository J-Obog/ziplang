from lexer import Lexer

txt = "somevariable int"

l = Lexer(txt)
 
print(l.next_token()) 
print(l.next_token()) 