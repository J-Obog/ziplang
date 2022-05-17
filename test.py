from ziplang.lexer import Lexer
import io

input = io.StringIO("obj.foobar()")


l = Lexer(input)

tkn = l.next_token() 

while tkn != None:
    print(tkn)
    tkn = l.next_token()


 