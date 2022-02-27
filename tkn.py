from tknkinds import TokenType, DataType

class Token:
    def __init__(self, type: TokenType, img: str, col: int, line: int):
        self.__type: TokenType = type 
        self.__img: str = img
        self.__col: int = col
        self.__line: int = line

    def get_type(self) -> TokenType:
        return self.__type

    def get_text(self) -> str:
        return self.__img

    def get_columnno(self) -> int:
        return self.__col

    def get_lineno(self) -> int:
        return self.__line

    def get_length(self) -> int: 
        return len(self.__img)


class TokenLiteral(Token):
    def __init__(self, type: TokenType, img: str, col: int, line: int, val: any, data: DataType):
        super().__init__(type, img, col, line) 
        self.__val: any = val
        self.__data: DataType = DataType

    def get_value(self) -> any:
        return self.__val

    def get_datatype(self) -> DataType:
        return self.__data
