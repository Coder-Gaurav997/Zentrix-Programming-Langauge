import re

TOKEN_SPEC = [
    ('NUMBER', r'\d+(\.\d+)?'),
    ('STRING', r'"[^"]*"'),

    ('TRUE', r'true'),
    ('FALSE', r'false'),
    ('NULL', r'null'),

    ('LET', r'let'),
    ('ECHO', r'echo'),
    ('INPUT', r'input'),

    ('IF', r'if'),
    ('ELSE', r'else'),
    ('WHILE', r'while'),
    ('FOR', r'for'),
    ('IN', r'in'),

    ('EQ', r'=='),
    ('NE', r'!='),
    ('LE', r'<='),
    ('GE', r'>='),
    ('LT', r'<'),
    ('GT', r'>'),

    ('AND', r'&&'),
    ('OR', r'\|\|'),
    ('NOT', r'!'),

    ('ASSIGN', r'='),
    ('OP', r'[+\-*/%]'),

    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('LBRACE', r'\{'),
    ('RBRACE', r'\}'),

    ('SEMI', r';'),

    ('ID', r'[A-Za-z_][A-Za-z0-9_]*'),
    ('SKIP', r'[ \t\n]+'),
]

token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPEC)

def tokenize(code):
    tokens = []
    for match in re.finditer(token_regex, code):
        kind = match.lastgroup
        value = match.group()

        if kind == 'NUMBER':
            value = float(value) if '.' in value else int(value)
        elif kind == 'STRING':
            value = value[1:-1]
        elif kind == 'SKIP':
            continue

        tokens.append((kind, value))
    return tokens