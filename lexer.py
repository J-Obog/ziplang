from typing import List, Optional
from tkn import Token

class Lexer:
    def __init__(self, input: str):
        self.__txt: str = input
        self.__idx: int = 0
        self.__tkns: List[Token]

    def __next(self) -> Optional[Token]:
        return None

    def scan(self):
        while self.__idx < len(self.__txt):
            tkn = self.__next()
            
            if tkn != None:
                self.__tkns.append(tkn)

            self.__idx += 1 