from tknkinds import TokenType

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

