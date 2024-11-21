class NumberNode:
    def __init__(self, value):
        self.value = value


class VariableNode:
    def __init__(self, name):
        self.name = name


class BinOpNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class AssignNode:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class PrintNode:
    def __init__(self, expression):
        self.expression = expression
