import scan
import tkn
import copy
import re
import math
from typing import List


class Lexer:
    def __init__(self, input: str):
        self.__scanner: scan.Scanner = scan.Scanner(input)
        self.__tkns: List[tkn.Token] = []

    def tokens(self) -> List[tkn.Token]:
        return self.__tkns

    def __lex_num(self):
        p = copy.deepcopy(self.__scanner.position())
        b = ''

        while (not self.__scanner.end()) and (not self.__scanner.curr_chr().isspace()):
            c = self.__scanner.curr_chr()
            b += c
            self.__scanner.advance()

        if re.match('^[+-]?([0-9]+\.?[0-9]*|\.[0-9]+)$', b):
            v = float(b)
            if v % 1 != 0:
                self.__tkns.append(tkn.TokenLiteral(tkn.TokenType.Literal, b, p, v, tkn.DataType.Float))
            else:
                self.__tkns.append(tkn.TokenLiteral(tkn.TokenType.Literal, b, p, math.floor(v), tkn.DataType.Integer))
        else:
            raise Exception('Invalid syntax')


    def scan(self):
        while not self.__scanner.end():
            c = self.__scanner.curr_chr()
            try:
                if c.isdigit():
                    self.__lex_num()

                self.__scanner.advance()
                
            except Exception as e:
                print(e)
                exit(1)

