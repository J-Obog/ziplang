
#token list
TKN_INT = 0
TKN_CHR = 1
#TKN_STR = 2
TKN_BOOL = 3 
TKN_FLOAT = 4
TKN_FOR = 5 
TKN_WHILE = 6
TKN_IF = 7 
TKN_ELSE = 8
TKN_ELF = 9
TKN_FN = 10
TKN_RET = 11
TKN_ASSIGN = 12
TKN_PLUS = 13
TKN_SUB = 14
TKN_MUL = 15
TKN_DIV = 16
TKN_MOD = 17
TKN_EXP = 18
TKN_GRT = 19
TKN_GRT_EQ = 20 
TKN_LESS = 21
TKN_LESS_EQ = 22 
TKN_EQ = 23
TKN_NOT_EQ = 24 
TKN_NOT = 25
TKN_OR = 26
TKN_AND = 27
TKN_LCURLY = 28
TKN_RCURLY = 29
TKN_LSQR = 30
TKN_RSQR = 31
TKN_LPAREN = 32
TKN_RPAREN = 33
TKN_COMMA = 34
TKN_NUMBER = 35 
TKN_STRING = 36
TKN_CHAR = 37
TKN_IDENT = 38
#TKN_ARR = 39
TKN_PTR = 40
TKN_STRUCT = 41
TKN_CONST = 42
TKN_SEMICOL = 43
TKN_AT = 43
TKN_TILDE = 44
TKN_ALIAS = 45

#token mappers
KEYWORD_TBL = {
    'int': TKN_INT,
    #'str': TKN_STR,
    'chr': TKN_CHR,
    'float': TKN_FLOAT,
    'bool': TKN_BOOL,
    'for': TKN_IF,
    'while': TKN_WHILE,
    'if': TKN_IF,
    'else': TKN_ELSE,
    'elf': TKN_ELF,
    'fn': TKN_FN, 
    'ret': TKN_RET,
    #'arr': TKN_ARR, 
    'ptr': TKN_PTR, 
    'struct': TKN_STRUCT,
    'const': TKN_CONST, 
    'alias': TKN_ALIAS
}

SPECIAL_CHAR_TBL = {
    '{': TKN_LCURLY, 
    '}': TKN_RCURLY,
    '[': TKN_LSQR, 
    ']': TKN_RSQR,
    '(': TKN_LPAREN,
    ')': TKN_RPAREN,
    ',': TKN_COMMA, 
    ';': TKN_SEMICOL,
    '@': TKN_AT,
    '~': TKN_TILDE
}

OPERATOR_TBL = {
    '=': TKN_ASSIGN,
    '+': TKN_PLUS, 
    '-': TKN_SUB,
    '*': TKN_MUL, 
    '/': TKN_DIV, 
    '%': TKN_MOD, 
    '^': TKN_EXP, 
    '>': TKN_GRT,
    '>=': TKN_GRT_EQ,
    '<': TKN_LESS,
    '<=': TKN_LESS_EQ,
    '==': TKN_EQ,
    '!=': TKN_NOT_EQ,
    '!': TKN_NOT, 
    '|': TKN_OR,
    '&': TKN_AND
}