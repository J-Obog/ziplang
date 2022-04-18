from lexer import Lexer

txt = "somevar | othervar"

l = Lexer(txt)
 
print(l.next_token()) 
print(l.next_token()) 
print(l.next_token()) 