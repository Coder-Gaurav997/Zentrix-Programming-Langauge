from ast_nodes import *

class Interpreter:
    def __init__(self):
        self.env = {}

    def visit(self, node):

        if isinstance(node, Number):
            return node.value

        elif isinstance(node, String):
            return node.value

        elif isinstance(node, Boolean):
            return node.value

        elif isinstance(node, Null):
            return None

        elif isinstance(node, VarAssign):
            value = self.visit(node.value)
            self.env[node.name] = value

        elif isinstance(node, VarAccess):
            if node.name in self.env:
                return self.env[node.name]
            raise Exception(f"Undefined variable {node.name}")

        elif isinstance(node, BinOp):
            left = self.visit(node.left)
            right = self.visit(node.right)

            if node.op == '+': return left + right
            if node.op == '-': return left - right
            if node.op == '*': return left * right
            if node.op == '/': return left / right
            if node.op == '%': return left % right

            if node.op == '==': return left == right
            if node.op == '!=': return left != right
            if node.op == '<': return left < right
            if node.op == '>': return left > right
            if node.op == '<=': return left <= right
            if node.op == '>=': return left >= right

            if node.op == '&&': return left and right
            if node.op == '||': return left or right

        elif isinstance(node, Echo):
            print(self.visit(node.expr))

        elif isinstance(node, Input):
            prompt = self.visit(node.prompt)
            return input(prompt)

        elif isinstance(node, IfNode):
            if self.visit(node.condition):
                for stmt in node.true_block:
                    self.visit(stmt)
            elif node.false_block:
                for stmt in node.false_block:
                    self.visit(stmt)

        elif isinstance(node, WhileNode):
            while self.visit(node.condition):
                for stmt in node.body:
                    self.visit(stmt)

        elif isinstance(node, ForNode):
            start = self.visit(node.start)
            end = self.visit(node.end)

            for i in range(start, end):
                self.env[node.var_name] = i
                for stmt in node.body:
                    self.visit(stmt)