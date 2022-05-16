from ziplang.lexer import Lexer
import ziplang.ast as zlast

class Parser:
    def __init__(self, lex: Lexer):
        self.lex: Lexer = lex

    def next_node(self) -> zlast.ASTNode:
        pass
