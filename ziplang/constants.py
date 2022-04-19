
ZL_KEYWORD_LST = frozenset({"int","chr","str","bool","float","fn","ret","for","while","true","false","if","else","elf"})
ZL_OPERATOR_LST = frozenset({'>','<','+','-','*','%','^','=','!','/','&','\\','==','!=','>=','<='})
ZL_SPECIALCHRS_LST = frozenset({'{','}','[',']','(',')',',', ';', ':'})

ZL_KEYWORD = 0
ZL_LITERAL = 1
ZL_IDENTIFIER = 2
ZL_SPECIALCHAR = 3 
ZL_OPERATOR = 4

ZL_TOKEN_MAP = {0: 'KEY', 1: 'LIT', 2: 'ID', 3: 'SCHR', 4: 'OP'}