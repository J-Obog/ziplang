from typing import List

class ASTNode:
    def __init__(self, type: str):
        self.__type: str = type

class ScopeBlock(ASTNode):
    def __init__(self, type: str):
        super().__init__(type)
        self.__body: List[ASTNode] = []

    def add_node(self, node: ASTNode):
        self.__body.append(node)


