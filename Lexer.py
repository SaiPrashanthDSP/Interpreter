import re

from Tokens import LET, PRINT, IDENTIFIER, ASSIGN, NUMBER, PLUS, MINUS, MULTIPLY, DIVIDE, SEMI

LPAREN = 'LPAREN'  # Left parenthesis
RPAREN = 'RPAREN'  # Right parenthesis

# Token specifications using regular expressions
token_specification = [
    (LET, r'\blet\b'),  # 'let' keyword
    (PRINT, r'\bprint\b'),  # 'print' keyword
    (IDENTIFIER, r'[a-zA-Z_][a-zA-Z_0-9]*'),  # Identifiers
    (ASSIGN, r'='),  # Assignment operator
    (NUMBER, r'\d+'),  # Integer numbers
    (PLUS, r'\+'),  # Plus operator
    (MINUS, r'-'),  # Minus operator
    (MULTIPLY, r'\*'),  # Multiplication operator
    (DIVIDE, r'/'),  # Division operator
    (SEMI, r';'),  # Semicolon
    (LPAREN, r'\('),  # Left parenthesis
    (RPAREN, r'\)'),  # Right parenthesis
    (r'WHITESPACE', r'\s+'),  # Whitespace (ignored)
]


# Tokenizer function
def tokenize(code):
    tokens = []
    position = 0
    while position < len(code):
        match = None
        for token_type, pattern in token_specification:
            regex = re.compile(pattern)
            match = regex.match(code, position)
            if match:
                if token_type != 'WHITESPACE':  # Skip whitespace
                    tokens.append(Token(token_type, match.group()))
                position = match.end()
                break
        if not match:
            raise SyntaxError(f"Unexpected character: {code[position]}")
    return tokens


# Test the lexer
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f'Token({self.type}, {repr(self.value)})'