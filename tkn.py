from tknkinds import TokenType, DataType
from position import Position

class Token:
    def __init__(self, type: TokenType, img: str, pos: Position):
        self.__type: TokenType = type 
        self.__img: str = img
        self.__pos: Position = pos

    def get_position(self) -> Position:
        return self.__pos

    def get_type(self) -> TokenType:
        return self.__type

    def get_text(self) -> str:
        return self.__img

    def get_length(self) -> int: 
        return len(self.__img)


class TokenLiteral(Token):
    def __init__(self, type: TokenType, img: str, pos: Position, val: any, data: DataType):
        super().__init__(type, img, pos)
        self.__val: any = val
        self.__data: DataType = DataType

    def get_value(self) -> any:
        return self.__val

    def get_datatype(self) -> DataType:
        return self.__data 

