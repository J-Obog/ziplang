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
            b += self.__scanner.curr_chr()
            self.__scanner.advance()

        if re.match('^[+-]?([0-9]+\.?[0-9]*|\.[0-9]+)$', b):
            v = float(b)
            if v % 1 != 0:
                self.__tkns.append(tkn.TokenLiteral(tkn.TokenType.Literal, b, p, v, tkn.DataType.Float))
            else:
                self.__tkns.append(tkn.TokenLiteral(tkn.TokenType.Literal, b, p, math.floor(v), tkn.DataType.Integer))
        else:
            raise Exception('Error while scanning num literal')

    def __lex_string(self):
        p = copy.deepcopy(self.__scanner.position())
        b = '' 

        while (not self.__scanner.end()) and (self.__scanner.curr_chr() != '"'):
            b += self.__scanner.curr_chr()
            self.__scanner.advance()

        if not self.__scanner.end():
            self.__tkns.append(tkn.TokenLiteral(tkn.TokenType.Literal, b, p, b, tkn.DataType.String))
        else:
            raise Exception('Error while scanning string literal')

    def __lex_char(self):
        p = copy.deepcopy(self.__scanner.position())
        b = '' 

        while (not self.__scanner.end()) and (self.__scanner.curr_chr() != '\''):
            b += self.__scanner.curr_chr()
            self.__scanner.advance()

        if not self.__scanner.end() and len(b) == 1:
            self.__tkns.append(tkn.TokenLiteral(tkn.TokenType.Literal, b, p, b, tkn.DataType.Character))
        else:
            raise Exception('Error while scanning character literal')


    def lex(self):
        while not self.__scanner.end():
            c = self.__scanner.curr_chr()
            try:
                if c.isdigit():
                    print(c)
                    self.__lex_num()
                elif c == '"':
                    self.__scanner.advance()
                    self.__lex_string()
                elif c == '\'':
                    self.__scanner.advance()
                    self.__lex_char()

                self.__scanner.advance()
                
            except Exception as e:
                print(e)
                exit(1)

