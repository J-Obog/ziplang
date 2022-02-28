import scanner
import tokens
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
        self.__scanner: scanner.Scanner = scanner.Scanner(input)
        self.__tokens: List[tokens.Token] = []
        self.__state: ScanState = ScanState.Scanning

    def tokens(self) -> List[tokens.Token]:
        return self.__tkns

    def lex(self):
        while not self.__scanner.end():
                try:
                    pass
                except Exception as e:
                    print(e)
                    exit(1)

