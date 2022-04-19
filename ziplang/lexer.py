from typing import Optional, Callable
from ziplang.tokens import Token
from ziplang.position import Position
import ziplang.constants as zlc
import copy
import re

class Lexer:
    def __init__(self, input: str):
        self.__input: str = input
        self.__idx: int = 0
        self.__pos: Position = Position(0,0)

    def __curr(self) -> chr:
        return '' if self.__end() else self.__input[self.__idx]

    def __advance(self):
        c = self.__curr()

        if c == '\n':
            self.__pos.col = 0
            self.__pos.line += 1
        elif c == '\t': 
            self.__pos.col += 4
        else: 
            self.__pos.col += 1
        
        self.__idx += 1

    def __end(self):
        return self.__idx >= len(self.__input)

    def __buffered_lex(self, fn: Callable) -> str:
        buf = ""
        while fn(buf, self.__curr()) and not self.__end():
            buf += self.__curr()
            self.__advance()
        return buf

    def __lexstr(self) -> Token:
        tpos = copy.deepcopy(self.__pos) 
        buf = self.__buffered_lex(lambda _,c: c != "\"")

        if self.__end(): raise Exception('Error while scanning string literal')

        self.__advance()
        return Token(zlc.ZL_LITERAL, buf, tpos)

    def __lexchar(self) -> Token:
        tpos = copy.deepcopy(self.__pos) 
        buf = self.__buffered_lex(lambda _,c: c != "\'")

        if len(buf) > 1 or self.__end(): raise Exception('Error while scanning character literal')

        self.__advance()
        return Token(zlc.ZL_LITERAL, buf, tpos)


    def __lexnum(self) -> Token:
        tpos = copy.deepcopy(self.__pos) 
        buf = self.__buffered_lex(lambda b,_: re.match(r"^\d+\.?\d*$", b))
        return Token(zlc.ZL_LITERAL, buf, tpos)

    def __lexalphnum(self) -> Token:
        tpos = copy.deepcopy(self.__pos) 
        buf = self.__buffered_lex(lambda b,_: re.match(r"^[a-zA-Z_][a-zA-Z_\d]*$", b))
        return Token(zlc.ZL_KEYWORD, buf, tpos) if buf in zlc.ZL_KEYWORD_LST else Token(zlc.ZL_IDENTIFIER, buf, tpos)

    def __lexop(self) -> Token:
        tpos = copy.deepcopy(self.__pos) 
        buf = self.__buffered_lex(lambda b,_: b in zlc.ZL_OPERATOR_LST)
        return Token(zlc.ZL_OPERATOR, buf, tpos)


    def next_token(self) -> Optional[Token]:
        while re.match(r"\s", self.__curr()):
            self.__advance()

        c = self.__curr()

        if not c:
            return None
        elif re.match(r"\d", c):
            return self.__lexnum()
        elif c == '\'':
            self.__advance()
            return self.__lexchar()
        elif c == '\"':
            self.__advance()
            return self.__lexstr()
        elif re.match(r"[a-zA-Z_]", c):
            return self.__lexalphnum()
        elif c in zlc.ZL_OPERATOR_LST:
            return self.__lexop()
        elif c in zlc.ZL_SPECIALCHRS_LST:
            tpos = copy.deepcopy(self.__pos)
            self.__advance()
            return Token(zlc.ZL_SPECIALCHAR, c, tpos)
