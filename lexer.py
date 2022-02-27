from typing import List
from tkn import Token, TokenLiteral
from tknkinds import TokenType, DataType
from scanner import Scanner
from copy import deepcopy
import re

class Lexer:
    def __init__(self, input: str):
        self.__scanner: Scanner = Scanner(input)
        self.__tkns: List[Token] = []

    def get_tokens(self) -> List[Token]:
        return self.__tkns

    def __lex_num(self):
        p = deepcopy(self.__scanner.position())
        b = ''
        dp = False

        while (not self.__scanner.end()) and (not self.__scanner.curr_chr().isspace()):
            c = self.__scanner.curr_chr()
            
            if c == '.':
                dp = True

            b += c
            self.__scanner.advance()

        if re.match('^[+-]?([0-9]+\.?[0-9]*|\.[0-9]+)$', b):
            if dp:
                self.__tkns.append(TokenLiteral(TokenType.Literal, b, p, float(b), DataType.Float))
            else:
                self.__tkns.append(TokenLiteral(TokenType.Literal, b, p, int(b), DataType.Integer))
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

