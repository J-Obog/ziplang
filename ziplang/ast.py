from typing import List

class ASTNode:
    def __init__(self, type: str):
        self.type: str = type

class ScopedBlock(ASTNode):
    def __init__(self, type: str):
        super().__init__(type)
        self.body: List[ASTNode] = []

class BinaryExpression(ASTNode):
    def __init__(self, operator: str, lhs: ASTNode, rhs: ASTNode):
        super().__init__("BINEXPR")
        self.op: str = operator
        self.lhs: ASTNode = lhs
        self.rhs: ASTNode = rhs

class UnaryExpression(ASTNode):
    def __init__(self, operator: str, operand: ASTNode):
        super().__init__("UNEXPR")
        self.op: str = operator
        self.opr: ASTNode = operator