from position import Position
from scanner import Scanner
from tokens import Token, TokenLiteral, DataType, TokenType
from typing import List
import copy
import re
import math


class Lexer:
    def __init__(self, input: str):
        self.__scanner: Scanner = Scanner(input)
        self.__tokens: List[Token] = []

    def tokens(self) -> List[Token]:
        return self.__tokens

    def __lex_num(self) -> Token:
        pos: Position = copy.deepcopy(self.__scanner.position())
        buff: str = ''

        while re.match('\d|\.', self.__scanner.curr_chr()) and not self.__scanner.end():
            buff += self.__scanner.curr_chr()
            self.__scanner.advance()

        if re.match('\d*\.?\d*$', buff):
            v: float = float(buff)
            if v % 1 == 0:
                return TokenLiteral(TokenType.Literal, buff, pos, math.floor(v), DataType.Integer)
            else:
                return TokenLiteral(TokenType.Literal, buff, pos, v, DataType.Float)
        else:
            raise Exception('Error while scanning num literal')

    
    def lex(self):
        while not self.__scanner.end():
            c = self.__scanner.curr_chr()
            try:
                if re.match('\s', c):
                    self.__scanner.advance()
                elif re.match('\d', c):
                    self.__lex_num()
            except Exception as e:
                print(e)
                exit(1)



            


              
