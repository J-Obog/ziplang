from typing import Optional, Callable
from ziplang.token import Token
from ziplang.position import Position
import ziplang.constants as zlc
import copy
import re

class Lexer:
    def __init__(self, input: str):
        self.input: str = input
        self.idx: int = 0
        self.pos: Position = Position(0,0)

    def curr(self) -> chr:
        return '' if self.end() else self.input[self.idx]

    def advance(self):
        c = self.curr()

        if c == '\n':
            self.pos.col = 0
            self.pos.line += 1
        elif c == '\t': 
            self.pos.col += 4
        else: 
            self.pos.col += 1
        
        self.idx += 1

    def end(self):
        return self.idx >= len(self.input)

    def buffered_lex(self, fn: Callable) -> str:
        buf = ""
        while fn(buf + self.curr(), self.curr()) and not self.end():
            buf += self.curr()
            self.advance()
        return buf

    def lexstr(self) -> Token:
        tpos = copy.deepcopy(self.pos) 
        buf = self.buffered_lex(lambda _,c: c != "\"")

        if self.end(): raise Exception('Error while scanning string literal')

        self.advance()
        return Token(zlc.ZL_LITERAL, buf, tpos)

    def lexchar(self) -> Token:
        tpos = copy.deepcopy(self.pos) 
        buf = self.buffered_lex(lambda _,c: c != "\'")

        if len(buf) > 1 or self.end(): raise Exception('Error while scanning character literal')

        self.advance()
        return Token(zlc.ZL_LITERAL, buf, tpos)

    def lexnum(self) -> Token:
        tpos = copy.deepcopy(self.pos) 
        buf = self.buffered_lex(lambda b,_: re.match(r"^\d+\.?\d*$", b))
        return Token(zlc.ZL_LITERAL, buf, tpos)

    def lexalphnum(self) -> Token:
        tpos = copy.deepcopy(self.pos) 
        buf = self.buffered_lex(lambda b,_: re.match(r"^[a-zA-Z_][a-zA-Z_\d]*$", b))
        return Token(zlc.ZL_KEYWORD, buf, tpos) if buf in zlc.ZL_KEYWORD_LST else Token(zlc.ZL_IDENTIFIER, buf, tpos)

    def lexop(self) -> Token:
        tpos = copy.deepcopy(self.pos) 
        buf = self.buffered_lex(lambda b,_: b in zlc.ZL_OPERATOR_LST)
        return Token(zlc.ZL_OPERATOR, buf, tpos)


    def next_token(self) -> Optional[Token]:
        while re.match(r"\s", self.curr()):
            self.advance()

        c = self.curr()

        if not c:
            return None
        elif re.match(r"\d", c):
            return self.lexnum()
        elif c == '\'':
            self.advance()
            return self.lexchar()
        elif c == '\"':
            self.advance()
            return self.lexstr()
        elif re.match(r"[a-zA-Z_]", c):
            return self.lexalphnum()
        elif c in zlc.ZL_OPERATOR_LST:
            return self.lexop()
        elif c in zlc.ZL_SPECIALCHRS_LST:
            tpos = copy.deepcopy(self.pos)
            self.advance()
            return Token(zlc.ZL_SPECIALCHAR, c, tpos)
