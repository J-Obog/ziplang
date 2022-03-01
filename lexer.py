from scanner import Scanner
from tokens import Token, TokenLiteral, DataType, TokenType
import copy
import re
import math
from enum import Enum
from typing import List

class ScanState(Enum):
    String = 'STR'
    Number = 'NUM'
    Character = 'CHR'
    Identifier = 'ID'
    Scanning = 'SCAN'

class Lexer:
    def __init__(self, input: str):
        self.__scanner: Scanner = Scanner(input)
        self.__tokens: List[Token] = []
        self.__state: ScanState = ScanState.Scanning
        self.__buffer: str = ''

    def tokens(self) -> List[Token]:
        return self.__tokens

    def state(self) -> ScanState:
        return self.__state 

    def lex(self):
        while not self.__scanner.end():
            c = self.__scanner.curr_chr()
            p = self.__scanner.position()
            self.__buffer += c

            if self.__state == ScanState.Number:
                if not re.match('\d*\.?\d*$', c) or (not self.__scanner.next_chr()):
                    v = float(self.__buffer[:-1])
                    if v % 1 == 0:
                        self.__tokens.append(TokenLiteral(TokenType.Literal, self.__buffer[:-1], p, math.floor(v), DataType.Integer))
                    else:
                        self.__tokens.append(TokenLiteral(TokenType.Literal, self.__buffer[:-1], p, v, DataType.Float))
                    self.__buffer = c
                    self.__state = ScanState.Scanning

            if self.__state == ScanState.String:
                if c == '"':
                    self.__tokens.append(TokenLiteral(TokenType.Literal, self.__buffer[1:-1], p, self.__buffer[1:-1], DataType.String))
                    self.__buffer = c
                    self.__state = ScanState.Scanning
                    self.__scanner.advance()
                if not self.__scanner.next_chr():
                    pass
                    #handle error

            if self.__state == ScanState.Scanning:
                if re.match('\d', c):
                    self.__state = ScanState.Number
                elif c == '"':
                    self.__state = ScanState.String
            
            self.__scanner.advance()
            


              
