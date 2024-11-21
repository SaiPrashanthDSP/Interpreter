from Nodes import NumberNode, VariableNode, BinOpNode, AssignNode, PrintNode
from Tokens import NUMBER, MULTIPLY, DIVIDE, PLUS, MINUS, IDENTIFIER, ASSIGN, PRINT, LET


class Parser:
    def __init__(self, lexer_tokens):
        self.tokens = lexer_tokens
        self.token_iter = iter(self.tokens)
        self.current_token = next(self.token_iter)

    # Function to check the syntax as per the production rules
    def checksyntax(self, token_type):
        if self.current_token.type == token_type:
            if self.current_token.value != self.tokens[-1].value:
                self.current_token = next(self.token_iter)

        else:
            raise Exception(f'Unexpected token: {self.current_token}')

    # <term>  ::= <factor> (("*" | "/") <factor>)*
    def factor(self):
        token = self.current_token
        if token.type == NUMBER and token.value.isdigit():
            self.checksyntax(NUMBER)
            return NumberNode(token.value)

        elif token.type == IDENTIFIER:
            # if token.value not in variable_storage:
            #     raise Exception(f'Unexpected token: {self.current_token}')
            self.checksyntax(IDENTIFIER)
            return VariableNode(token.value)
        else:
            raise Exception(f'Unexpected token: {self.current_token}')

    # < term >: := < factor > (("*" | "/") < factor >) *
    def term(self):
        node = self.factor()
        while self.current_token.type in (MULTIPLY, DIVIDE):
            token = self.current_token
            if token.type == MULTIPLY:
                self.checksyntax(MULTIPLY)
            elif token.type == DIVIDE:
                self.checksyntax(DIVIDE)
            node = BinOpNode(left=node, op=token.type, right=self.factor())
        return node

    # <expression> ::= <term> (("+" | "-") <term>)*
    def expr(self):
        node = self.term()
        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.checksyntax(PLUS)
            elif token.type == MINUS:
                self.checksyntax(MINUS)
            node = BinOpNode(left=node, op=token.type, right=self.term())
        return node

    # < statement >: := < assignment > | < print >
    def statement(self):
        if self.current_token.type == LET or self.current_token.type == IDENTIFIER:
            if self.current_token.type == LET:
                self.current_token = next(self.token_iter)

            var_name = self.current_token.value
            self.checksyntax(IDENTIFIER)
            self.checksyntax(ASSIGN)
            value = self.expr()
            return AssignNode(var_name, value)
        elif self.current_token.type == PRINT:
            self.checksyntax(PRINT)
            expression = self.expr()
            return PrintNode(expression)

    def parse(self):
        return self.statement()
