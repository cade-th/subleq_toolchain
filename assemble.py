from assembler.src.lexer import Lexer
from assembler.src.parser import Parser
import sys

def assembler():
    file_path = sys.argv[1]
    input_string = ""
    with open(file_path, "r") as src_code:
       input_string = src_code.read() 

    if sys.argv[2] == "lex":
        lexer = Lexer(input_string)
        tokens = lexer.lex()

        for i in tokens:
            print(f"{i},")
    elif sys.argv[2] == "p1_macro":
        lexer = Lexer(input_string)
        tokens = lexer.lex()
        parser = Parser(tokens) 
        tokens, mnt, mdt = parser.macro_p1()

        for i in tokens:
            print(f"{i},")

    elif sys.argv[2] == "p2_macro":
        lexer = Lexer(input_string)
        tokens = lexer.lex()
        parser = Parser(tokens) 
        tokens, mnt, mdt = parser.macro_p1()
        tokens = parser.macro_p2(mnt,mdt)

        for i in tokens:
            print(f"{i},")


if __name__ == "__main__":
    assembler()
