from tests.tester import run
from assembler.src.lexer import Lexer
import json
 
def lexer_test(test_name, data):
    print(f"Test {test_name}:")
    success = False

    lexer = Lexer(data["input"]) 
    tokens = lexer.lex()

    if tokens != data["output"]:
        error_log(data["output"], tokens, "tokens")
        return success

    success = True
    return success

def error_log(expected, received, string):
    print(f"\tIncorrect {string}:")
    print(f"\t\tExpected {string}: {expected}")
    print(f"\t\tRecieved {string}: {received}")

if __name__ == "__main__":
    with open("tests/assembler_tests/lexer_tests.json", "r") as f:
        test_data = json.load(f)
        run("Lexer", test_data, lexer_test)

