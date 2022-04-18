from lexer import Lexer

txt = "2.45 5.6 8"

l = Lexer(txt)
 
print(l.next_token()) 
print(l.next_token()) 
print(l.next_token()) 
print(l.next_token()) 