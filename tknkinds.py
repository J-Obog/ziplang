from enum import Enum

class TokenType(Enum):
    Keyword = 'KEY'
    Literal = 'LIT'
    Identifier = 'ID'
    SpecialCharacter = 'SPC'


class DataType(Enum):
    Integer = 'INT'
    String = 'STR'
    Float = 'FLOAT'
    Character = 'CHR'
    Boolean = 'BOOL'