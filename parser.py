from ast_nodes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return ('EOF', None)

    def eat(self, token_type):
        if self.current()[0] == token_type:
            self.pos += 1
        else:
            raise Exception(f"Expected {token_type}, got {self.current()}")

    def parse(self):
        statements = []
        while self.current()[0] != 'EOF':
            statements.append(self.statement())
        return statements

    def statement(self):
        token = self.current()

        if token[0] == 'LET':
            return self.var_assign()

        elif token[0] == 'ECHO':
            return self.echo_stmt()

        elif token[0] == 'IF':
            return self.if_stmt()

        elif token[0] == 'WHILE':
            return self.while_stmt()

        elif token[0] == 'FOR':
            return self.for_stmt()

        return self.expr_statement()

    def block(self):
        statements = []
        self.eat('LBRACE')
        while self.current()[0] != 'RBRACE':
            statements.append(self.statement())
        self.eat('RBRACE')
        return statements

    def var_assign(self):
        self.eat('LET')
        name = self.current()[1]
        self.eat('ID')
        self.eat('ASSIGN')
        value = self.expr()
        self.eat('SEMI')
        return VarAssign(name, value)

    def echo_stmt(self):
        self.eat('ECHO')
        self.eat('LPAREN')
        expr = self.expr()
        self.eat('RPAREN')
        self.eat('SEMI')
        return Echo(expr)

    def if_stmt(self):
        self.eat('IF')
        self.eat('LPAREN')
        condition = self.expr()
        self.eat('RPAREN')

        true_block = self.block()

        false_block = None
        if self.current()[0] == 'ELSE':
            self.eat('ELSE')
            false_block = self.block()

        return IfNode(condition, true_block, false_block)

    def while_stmt(self):
        self.eat('WHILE')
        self.eat('LPAREN')
        condition = self.expr()
        self.eat('RPAREN')
        body = self.block()
        return WhileNode(condition, body)

    def for_stmt(self):
        self.eat('FOR')
        self.eat('LPAREN')

        var_name = self.current()[1]
        self.eat('ID')

        self.eat('IN')
        start = self.expr()

        if self.current()[1] != 'to':
            raise Exception("Expected 'to'")
        self.eat('ID')

        end = self.expr()

        self.eat('RPAREN')
        body = self.block()

        return ForNode(var_name, start, end, body)

    def expr_statement(self):
        expr = self.expr()
        self.eat('SEMI')
        return expr

    def expr(self):
        return self.logic()

    def logic(self):
        left = self.equality()
        while self.current()[0] in ('AND', 'OR'):
            op = self.current()[1]
            self.eat(self.current()[0])
            right = self.equality()
            left = BinOp(left, op, right)
        return left

    def equality(self):
        left = self.comparison()
        while self.current()[0] in ('EQ', 'NE'):
            op = self.current()[1]
            self.eat(self.current()[0])
            right = self.comparison()
            left = BinOp(left, op, right)
        return left

    def comparison(self):
        left = self.term()
        while self.current()[0] in ('LT','GT','LE','GE'):
            op = self.current()[1]
            self.eat(self.current()[0])
            right = self.term()
            left = BinOp(left, op, right)
        return left

    def term(self):
        left = self.factor()
        while self.current()[0] == 'OP':
            op = self.current()[1]
            self.eat('OP')
            right = self.factor()
            left = BinOp(left, op, right)
        return left

    def factor(self):
        token = self.current()

        if token[0] == 'NUMBER':
            self.eat('NUMBER')
            return Number(token[1])

        elif token[0] == 'STRING':
            self.eat('STRING')
            return String(token[1])

        elif token[0] == 'TRUE':
            self.eat('TRUE')
            return Boolean(True)

        elif token[0] == 'FALSE':
            self.eat('FALSE')
            return Boolean(False)

        elif token[0] == 'NULL':
            self.eat('NULL')
            return Null()

        elif token[0] == 'ID':
            name = token[1]
            self.eat('ID')
            return VarAccess(name)

        elif token[0] == 'LPAREN':
            self.eat('LPAREN')
            expr = self.expr()
            self.eat('RPAREN')
            return expr

        elif token[0] == 'INPUT':
            return self.input_call()

    def input_call(self):
        self.eat('INPUT')
        self.eat('LPAREN')
        prompt = self.expr()
        self.eat('RPAREN')
        return Input(prompt)