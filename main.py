from lexer import Lexer

txt = "\"This is some string\""

l = Lexer(txt)
 
print(l.next_token()) 
print(l.next_token()) 