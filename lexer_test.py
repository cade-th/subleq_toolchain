from assembler.src.lexer import Lexer
from test_utils import error_log

 
def lexer(test_name, data):
    # print(f"Test {test_name}:")
    success = False

    lexer = Lexer(data["input"]) 
    tokens = lexer.lex()

    if tokens != data["output"]:
        error_log(test_name, data["output"], tokens, "tokens")
        return success

    success = True
    return success


