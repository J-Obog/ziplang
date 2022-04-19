from ziplang.position import Position
from ziplang.constants import ZL_TOKEN_MAP

class Token:
    def __init__(self, type: int, img: str, pos: Position):
        self.__type: int = type 
        self.__img: str = img
        self.__pos: Position = pos

    def position(self) -> Position:
        return self.__pos

    def type(self) -> int:
        return self.__type

    def text(self) -> str:
        return self.__img

    def length(self) -> int: 
        return len(self.__img)

    def __repr__(self) -> str:
        return f'[{ZL_TOKEN_MAP[self.__type]}, {self.__img}]'

