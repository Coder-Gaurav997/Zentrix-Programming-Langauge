from lexer import tokenize
from parser import Parser
from interpreter import Interpreter
import sys

def run_file(filename):
    with open(filename, 'r') as f:
        code = f.read()

    tokens = tokenize(code)
    parser = Parser(tokens)
    tree = parser.parse()

    interpreter = Interpreter()

    for stmt in tree:
        interpreter.visit(stmt)

if __name__ == "__main__":
    run_file("test.zx")