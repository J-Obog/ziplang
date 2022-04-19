from ast import AST
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

class BinaryExpression(ASTNode):
    def __init__(self, operator: str, lhs: ASTNode, rhs: ASTNode):
        super().__init__("BINEXPR")
        self.__op: str = operator

class UnaryExpression(ASTNode):
    def __init__(self, operator: str, operand: ASTNode):
        super().__init__("UNEXPR")
        self.__op: str = operator