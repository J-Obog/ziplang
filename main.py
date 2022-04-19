from ziplang.lexer import Lexer

txt = "myfunction(){}"

l = Lexer(txt)
 
print(l.next_token()) 
print(l.next_token()) 
print(l.next_token()) 
print(l.next_token()) 
print(l.next_token()) 