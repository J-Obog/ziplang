
class Position:
    def __init__(self, col: int, line: int):
        self.__col: int = col
        self.__line: int = line
    
    def col(self) -> int:
        return self.__col

    def line(self) -> int:
        return self.__line

    def set_col(self, col: int):
        self.__col = col

    def set_line(self, line: int):
        self.__line = line

    def __repr__(self) -> str:
        return f'Position({self.__col},{self.__line})'