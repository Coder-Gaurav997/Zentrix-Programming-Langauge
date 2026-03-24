class Number:
    def __init__(self, value):
        self.value = value

class String:
    def __init__(self, value):
        self.value = value

class Boolean:
    def __init__(self, value):
        self.value = value

class Null:
    pass

class VarAssign:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class VarAccess:
    def __init__(self, name):
        self.name = name

class BinOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class UnaryOp:
    def __init__(self, op, expr):
        self.op = op
        self.expr = expr

class Echo:
    def __init__(self, expr):
        self.expr = expr

class Input:
    def __init__(self, prompt):
        self.prompt = prompt

class IfNode:
    def __init__(self, condition, true_block, false_block=None):
        self.condition = condition
        self.true_block = true_block
        self.false_block = false_block

class WhileNode:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class ForNode:
    def __init__(self, var_name, start, end, body):
        self.var_name = var_name
        self.start = start
        self.end = end
        self.body = body