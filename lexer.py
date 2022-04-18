from typing import Optional
from tokens import Token#, TokenType
from position import Position
#import copy
import re

class Lexer:
    def __init__(self, input: str):
        self.__input: str = input
        self.__idx: int = 0
        self.__pos: Position = Position(0,0)

    def __curr(self):
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

    def next_token(self) -> Optional[Token]:
        while re.match(r"\s", self.__curr()):
            self.__advance()

        c = self.__curr()

        if not c:
            return None