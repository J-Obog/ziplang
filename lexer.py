from typing import Optional
from tokens import Token#, TokenType
from position import Position
#import copy
#import re

class Lexer:
    def __init__(self, input: str):
        self.__input: str = input
        self.__idx: int = 0
        self.__pos: Position = Position(0,0)

    def __end(self):
        return self.__idx >= len(self.__input)

    def next_token(self) -> Optional[Token]:
        pass