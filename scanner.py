from typing import Optional
from position import Position

class Scanner:
    def __init__(self, text: str):
        self.__text: str = text
        self.__pos: Position = Position(0,0)
        self.__idx: int = 0 

    def __move(self, col: int, ln: int):
        self.__pos.set_col(self.__pos.get_col() + col)
        self.__pos.set_ln(self.__pos.get_ln() + ln)

    def __get_chr(self, offset: int) -> Optional[chr]:
        p = self.__idx + offset
        if -1 < p < len(self.__text):
            return self.__text[p]
        return None

    def next_chr(self) -> Optional[chr]:
        return self.__get_chr(1)

    def curr_chr(self) -> Optional[chr]:
        return self.__get_chr(0)

    def prev_chr(self) -> Optional[chr]:
        return self.__get_chr(-1)

    def end(self) -> bool:
        return self.__idx >= len(self.__text)

    def advance(self):
        if not self.end():
            c = self.curr_chr()

            if c == '\n':
                self.__move(-self.__pos.get_col(),1)
            elif c == '\t':
                self.__move(4,0)
            else:  
                self.__move(1,0)
            
            self.__idx += 1

    def position(self) -> str:
        return self.__pos

    def text(self) -> str: 
        return self.__text