from enum import Enum
from position import Position

class TokenType(Enum):
    Keyword = 'KEY'
    Literal = 'LIT'
    Identifier = 'ID'
    SpecialCharacter = 'SPC'

class DataType(Enum):
    Integer = 'INT'
    String = 'STR'
    Float = 'FLOAT'
    Character = 'CHR'
    Boolean = 'BOOL'

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
        return f'Token({self.__type.value}, {self.__img}, {self.__pos})'


class TokenLiteral(Token):
    def __init__(self, type: TokenType, img: str, pos: Position, val: any, data: DataType):
        super().__init__(type, img, pos)
        self.__val: any = val
        self.__data: DataType = data

    def value(self) -> any:
        return self.__val

    def datatype(self) -> DataType:
        return self.__data 

