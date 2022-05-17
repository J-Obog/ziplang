from dataclasses import dataclass
import ziplang.tokenlist as tkns
import io
import copy

@dataclass
class Position:
    line: int
    col: int

@dataclass
class Token:
    type: int
    image: str
    #pos: Position

class Lexer:
    def __init__(self, buf: io.StringIO):
        self.buf: io.StringIO = buf
        self.pos: Position = Position(-1,0)

    def lex_str_lit(self) -> Token:
        curr = self.buf.read(1)
        img = ""

        while curr != '"':
            if curr == '':
                raise Exception("ERROR lexing string literal")
            img += curr
            curr = self.buf.read(1)

        return Token(tkns.TKN_STRING_LIT, img)


    def lex_char_lit(self) -> Token:
        c = self.buf.read(1)
        curr = self.buf.read(1)

        if curr != '\'':
            raise Exception("ERROR lexing char literal")

        return Token(tkns.TKN_CHAR_LIT, c)


    def lex_num_lit(self) -> Token:
        curr = self.buf.read(1)
        has_dec = False
        img = ""
        
        while curr.isdigit() or curr == '.':
            if curr == '.':
                if has_dec:
                    raise Exception("ERROR lexing num literal")
                else:
                    has_dec = True
        
            img += curr
            curr = self.buf.read(1)

        if curr != '':
            self.buf.seek(self.buf.tell() - 1)
        
        return Token(tkns.TKN_FLOAT_LIT, img) if has_dec else Token(tkns.TKN_INT_LIT, img)


    def lex_ident(self) -> Token:
        curr = self.buf.read(1)
        img = ""

        while curr == '_' or curr.isalpha() or curr.isdigit():
            img += curr
            curr = self.buf.read(1)

        if curr != '':
            self.buf.seek(self.buf.tell() - 1)

        kw = tkns.KEYWORD_TBL.get(img, None)
        return Token(kw, img) if kw != None else Token(tkns.TKN_IDENT, img)

    def lex_operator(self) -> Token:
        fst = self.buf.read(1)
        snd = self.buf.read(1)
        twb = fst + snd
        
        if twb in tkns.OPERATOR2_TBL:
            return Token(tkns.OPERATOR2_TBL[twb], twb)
        else:
            if snd != '':
                self.buf.seek(self.buf.tell() - 1)
            return Token(tkns.OPERATOR1_TBL[fst], fst)
            

    def next_token(self) -> Token:
        curr = self.buf.read(1)

        while curr.isspace():
            curr = self.buf.read(1)

        if curr == '':
            return None

        elif curr.isdigit():
            self.buf.seek(self.buf.tell() - 1)
            return self.lex_num_lit()
        
        elif curr == '\'':
            return self.lex_char_lit()
        
        elif curr == '"':
            return self.lex_str_lit()
       
        elif curr == '_' or curr.isalpha():
            self.buf.seek(self.buf.tell() - 1)
            return self.lex_ident()

        elif curr in tkns.OPERATOR1_TBL:
            self.buf.seek(self.buf.tell() - 1)
            return self.lex_operator()

        elif curr in tkns.SPECIAL_CHAR_TBL:
            return Token(tkns.SPECIAL_CHAR_TBL[curr], curr)

        else:
            raise Exception("ERROR unrecognized token")