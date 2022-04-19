from ziplang.lexer import Lexer, Token
import ziplang.ast as zlast

class Parser:
    def __init__(self, lexer: Lexer):
        self.lexer: Lexer = lexer
        self.curr_tkn: Token = lexer.next_token()

    def advance(self):
        self.curr_tkn = self.lexer.next_token()

    def end(self) -> bool:
        return self.curr_tkn == None

    def parse(self) -> zlast.ASTNode:
        pass            