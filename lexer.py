from position import Position
from scanner import Scanner
from tokens import Token, TokenLiteral, DataType, TokenType
from typing import List
import copy
import re
import math

DIGITS = '0123456789'
WS = '\t\r\n '
SPECIAL_CHARS = '{}[]()><=!+-*/%^|&.,:\"\''

class Lexer:
    def __init__(self, input: str):
        self.__scanner: Scanner = Scanner(input)
        self.__tokens: List[Token] = []

    def tokens(self) -> List[Token]:
        return self.__tokens

    def __lex_num(self) -> Token:
        pos: Position = copy.deepcopy(self.__scanner.position())
        buff: str = ''

        while re.match('\d|\.', str(self.__scanner.curr_chr())) and not self.__scanner.end():
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

    def __lex_str(self) -> Token:
        pos: Position = copy.deepcopy(self.__scanner.position())
        buff: str = ''

        while self.__scanner.curr_chr() != '\"' and not self.__scanner.end():
            buff += self.__scanner.curr_chr()
            self.__scanner.advance()

        if not self.__scanner.end():
            return TokenLiteral(TokenType.Literal, buff, pos, buff, DataType.String)
        else:
            raise Exception('Error while scanning string literal')
    
    def __lex_chr(self) -> Token:
        pos: Position = copy.deepcopy(self.__scanner.position())
        buff: str = ''

        while self.__scanner.curr_chr() != '\'' and not self.__scanner.end():
            buff += self.__scanner.curr_chr()
            self.__scanner.advance()

        if not self.__scanner.end() and len(buff) == 1:
            return TokenLiteral(TokenType.Literal, buff, pos, buff, DataType.Character)
        else:
            raise Exception('Error while scanning string literal')

    def lex(self):
        while not self.__scanner.end():
            c = self.__scanner.curr_chr()
            try:
                if c in WS:
                    self.__scanner.advance()
                elif c in DIGITS:
                    self.__tokens.append(self.__lex_num())
                elif c in SPECIAL_CHARS:
                    if c == '\"':
                        self.__scanner.advance()
                        self.__tokens.append(self.__lex_str())
                        self.__scanner.advance()
                    elif c == '\'':
                        self.__scanner.advance()
                        self.__tokens.append(self.__lex_chr())
                        self.__scanner.advance()
                    else:
                        pass
            except Exception as e:
                print(e)
                exit(1)



            


              
