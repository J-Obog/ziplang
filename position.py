
class Position:
    def __init__(self, col: int, line: int):
        self.__col: int = col
        self.__line: int = line
    
    def get_columnno(self) -> int:
        return self.__col

    def get_lineno(self) -> int:
        return self.__line

    def set_columnno(self, col: int):
        self.__col = col

    def set_lineno(self, line: int):
        self.__line = line