from dataclasses import dataclass
from ziplang.position import Position
from ziplang.constants import ZL_TOKEN_MAP

@dataclass
class Token:
    type: int
    img: str
    pos: Position

    def __repr__(self) -> str:
        return f'[{ZL_TOKEN_MAP[self.type]}, {self.img}]'

