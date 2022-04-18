from enum import Enum
from position import Position

class TokenType(Enum):
    Keyword = 'KEY'
    Literal = 'LIT'
    Identifier = 'ID'
    SpecialCharacter = 'SPEC'
    Operator = 'OP'


class Token:
    def __init__(self, type: TokenType, img: str, pos: Position):
        self.__type: TokenType = type 
        self.__img: str = img
        self.__pos: Position = pos

    def position(self) -> Position:
        return self.__pos

    def type(self) -> TokenType:
        return self.__type

    def text(self) -> str:
        return self.__img

    def length(self) -> int: 
        return len(self.__img)

    def __repr__(self) -> str:
        return f'[{self.__type.value}, {self.__img}]'

