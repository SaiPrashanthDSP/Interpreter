from AST import Parser
from Lexer import tokenize

variable_storage = {}
def main():

    while True:
        try:
            text = input('>>> ')
            if text.strip().lower() == 'exit':
                break
            # Call the functions here from Lexer to Interpreter
            # code = "let x = 10 + 5; print(x);"
            tokens = tokenize(text)
            parser = Parser(tokens)
            tree = parser.parse()
            print(tree)
        except Exception as e:
            print(f'Error: {e}')


if __name__ == '__main__':
    main()
