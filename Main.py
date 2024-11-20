def main():
    while True:
        try:
            text = input('>>> ')
            if text.strip().lower() == 'exit':
                break
            # Call the functions here from Lexer to Interpreter
        except Exception as e:
            print(f'Error: {e}')

if __name__ == '__main__':
    main()