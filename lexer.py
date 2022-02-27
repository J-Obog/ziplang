from typing import List
from tkn import Token, TokenLiteral
from tknkinds import TokenType, DataType
from position import Position
import re

class Lexer:
    def __init__(self, input: str):
        self.__text: str = input
        self.__counter: int = 0
        self.__pos: Position = Position(0,0)
        self.__tkns: List[Token] = []

    def get_tokens(self) -> List[Token]:
        return self.__tkns

    def __move(self, col: int, ln: int):
        self.__pos.set_col(self.__pos.get_col() + col)
        self.__pos.set_ln(self.__pos.get_ln() + ln)

    def __curr(self) -> chr:
        return self.__text[self.__counter]

    def __next(self) -> bool:
        return self.__counter < len(self.__text)

    def __lex_ws(self): 
        c = self.__curr()
        
        if c == '\n':
            self.__move(-self.__pos.get_col(),1)
        elif c == '\t':
            self.__move(4,0)
        else:
            self.__move(1,0)

    def __lex_num(self):
        p = self.__pos
        b = ''
        dp = False

        while self.__next() and not self.__curr().isspace():
            c = self.__curr()
            
            if c == '.':
                dp = True

            b += c
            self.__counter += 1

        if re.match('^[+-]?([0-9]+\.?[0-9]*|\.[0-9]+)$', b):
            if dp:
                self.__tkns.append(TokenLiteral(TokenType.Literal, b, p, float(b), DataType.Float))
            else:
                self.__tkns.append(TokenLiteral(TokenType.Literal, b, p, int(b), DataType.Integer))
        else:
            raise Exception('Invalid syntax')


    def scan(self):
        while self.__next():
            c = self.__curr()

            try:
                if c.isspace():
                    self.__lex_ws()
                elif c.isdigit():
                    self.__lex_num() 
            except Exception as e:
                print(e)
                exit(1)

