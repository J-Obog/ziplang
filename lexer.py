from typing import Optional
from tokens import Token, TokenType
from position import Position
import copy
import re

KEYWORD_LST = r"^(int|chr|str|bool|float|fn|ret|for|while|true|false|if|else|elf)$"
OPERATOR_LST = r"^(\>|\<|\+|\-|\*|\%|\^|\=|\!|\/|\&|\||==|!=|>=|<=)$"

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

    def __lexstr(self) -> Token:
        tpos = copy.deepcopy(self.__pos) 
        buf = ""

        while self.__curr() != '\"' and not self.__end():
            buf += self.__curr()
            self.__advance()

        if self.__end():
            raise Exception('Error while scanning string literal')

        self.__advance()
        return Token(TokenType.Literal, buf, tpos)

    def __lexchar(self) -> Token:
        tpos = copy.deepcopy(self.__pos) 
        buf = ""

        while self.__curr() != '\'' and not self.__end():
            if len(buf) > 1:
                raise Exception('Error while scanning character literal')
            buf += self.__curr()
            self.__advance()

        if self.__end():
            raise Exception('Error while scanning character literal')

        self.__advance()
        return Token(TokenType.Literal, buf, tpos)


    def __lexnum(self) -> Token:
        tpos = copy.deepcopy(self.__pos) 
        buf = ""

        while re.match(r"^\d+\.?\d*$", buf + self.__curr()) and not self.__end():
            buf += self.__curr()
            self.__advance()

        return Token(TokenType.Literal, buf, tpos)

    def __lexalphnum(self) -> Token:
        tpos = copy.deepcopy(self.__pos) 
        buf = ""

        while re.match(r"^[a-zA-Z_][a-zA-Z_\d]*$", buf + self.__curr()) and not self.__end():
            buf += self.__curr()
            self.__advance()

        return Token(TokenType.Keyword, buf, tpos) if re.match(KEYWORD_LST, buf) else Token(TokenType.Identifier, buf, tpos)

    def __lexop(self) -> Token:
        tpos = copy.deepcopy(self.__pos) 
        buf = ""

        while re.match(OPERATOR_LST, buf + self.__curr()) and not self.__end():
            buf += self.__curr()
            self.__advance()

        return Token(TokenType.Operator, buf, tpos)


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
        elif re.match(OPERATOR_LST, c):
            return self.__lexop()
            