from ziplang.lexer import Lexer

txt = "if (a > b) {\n\tc = 2;\n\tret c;\n} else {\n\tc = 3;\n}"

l = Lexer(txt)
 
print(l.next_token()) 
print(l.next_token()) 
print(l.next_token()) 
print(l.next_token()) 
print(l.next_token()) 
print(l.next_token()) 
print(l.next_token()) 
print(l.next_token()) 
print(l.next_token()) 
print(l.next_token()) 
print(l.next_token()) 
print(l.next_token()) 
print(l.next_token()) 
print(l.next_token()) 
print(l.next_token()) 
print(l.next_token()) 
print(l.next_token()) 
print(l.next_token()) 
print(l.next_token()) 
print(l.next_token()) 
print(l.next_token()) 
print(l.next_token()) 