from typing import List
from unicodedata import digit
from tkn import Token, TokenLiteral
from tknkinds import TokenType, DataType
from position import Position

class Lexer:
    def __init__(self, input: str):
        self.__text: str = input
        self.__counter: int = 0
        self.__pos: Position = Position(0,0)
        self.__tkns: List[Token] = []

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
        v = 0
        while self.__next() and not self.__curr().isspace():
            c = self.__curr()
            b += c
            if c == '.':
                if b.count('.') > 1:
                    raise Exception('Too many decimal points')
            elif not c.isdigit():
                    raise Exception('Not a real number')

            self.__counter += 1

        for i in range(len(b)):
            v += int(b[i]) * (10 ** (len(b) - i - 1))

        dp = b.find('.')

        if dp != -1:
            self.__tkns.append(TokenLiteral(TokenType.Literal, b, p, v * (10 * -((len(b) - dp) - 1)), DataType.Float))
        else:
            self.__tkns.append(TokenLiteral(TokenType.Literal, b, p, v, DataType.Integer))


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

